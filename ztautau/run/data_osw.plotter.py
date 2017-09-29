#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
j.postprocessor.py
"""

## std modules
import os,re

## ROOT
import ROOT
ROOT.gROOT.SetBatch(True)

## my modules
import pyframe

## local modules
import ztautau

#_____________________________________________________________________________
def get_sys_dict(sys_name=None, sys_tree="NOMINAL",sys_friendtree="NN_NOMINAL", sys_var=None):
  return {"name":sys_name, "tree":sys_tree, "friendtree":sys_friendtree, "variation":sys_var}
#_____________________________________________________________________________
def analyze(config):
  
    ##-------------------------------------------------------------------------
    ## setup
    ##-------------------------------------------------------------------------
    config['do_var_log'] = True
    main_path = os.getenv('MAIN')
    

    ##-------------------------------------------------------------------------
    ## systematics 
    ##-------------------------------------------------------------------------
    
    """
    pass systematics on the command line like this:
    python j.plotter.py --config="sys:SYS_UP"
    """
    config.setdefault('sys',None)

    sys = config['sys']
    
    sys_dict = None
    
    if   sys == None: sys_dict = get_sys_dict()
    
    # this is how you tell the weights 
    # what is the direction of the variation
    elif sys == 'SYS_UP':     sys_dict = get_sys_dict(sys_name = sys, sys_var = "up")
    elif sys == 'SYS_UP':     sys_dict = get_sys_dict(sys_name = sys, sys_var = "dn")
    elif sys == 'TREESYS_UP': sys_dict = get_sys_dict(sys_name = sys, sys_tree = "MySysTreeName", sys_var = "up")
    elif sys == 'TREESYS_DN': sys_dict = get_sys_dict(sys_name = sys, sys_tree = "MySysTreeName", sys_var = "dn")
    elif sys == 'MUID_DN':    sys_dict = get_sys_dict(sys_name = sys, sys_tree = "MUONS_ID_1down", sys_var = "dn")
    else: 
        assert False, "Invalid sys %s!"%(sys)
    
    ## build chain
    config['tree'] = sys_dict['tree']
    config['friendtree'] = sys_dict['friendtree'] 
    
    chain = ROOT.TChain(config['tree'])
    for fn in config['input']: chain.Add(fn)
    if config['friendinput']: 
      assert config['friendtree'], 'ERROR: name of friendtree not provided for friendfile %s'%config['friendinput']
      chain.AddFriend(config['friendtree'],config['friendinput'])

    ##-------------------------------------------------------------------------
    ## event loop
    ##-------------------------------------------------------------------------
    loop = pyframe.core.EventLoop(name='ztautau',
                                  sampletype=config['sampletype'],
                                  samplename=config['samplename'],
                                  friendtree=config['friendtree'],
                                  outfile=config['samplename']+".root",
                                  quiet=False,
                                  )

    ## start preselection cutflow 
    ## ---------------------------------------
    loop += pyframe.algs.CutFlowAlg(key='PreselMu2016')
    
    ## weights
    ## +++++++++++++++++++++++++++++++++++++++
    loop += ztautau.algs.weights.WeightTotal(cutflow='PreselMu2016',key='weight_total')


    ## initialize and/or decorate objects
    ## ---------------------------------------
    #loop += ztautau.algs.vars.Vars()

    ## cuts
    ## +++++++++++++++++++++++++++++++++++++++
    #loop += ztautau.algs.algs.CutAlg(cutflow='presel',cut='AtLeastOneMuon') 

    
    ## weights configuration
    ## ---------------------------------------
    ## event
    ## +++++++++++++++++++++++++++++++++++++++
    
    
    ## objects
    ## +++++++++++++++++++++++++++++++++++++++
    loop += ztautau.algs.weights.ObjWeight(
            obj_name    = "tau_0",
            branch_name = "TauEffSF_reco",
            key         = "TauReco",
            scale       = None,
            )
    loop += ztautau.algs.weights.ObjWeight(
            obj_name    = "tau_0",
            branch_name = "TauEffSF_JetBDTmedium",
            key         = "TauID",
            scale       = None,
            )
    #loop += ztautau.algs.weights.ObjWeight(
    #        obj_name    = "tau_0",
    #        branch_name = "TauEffSF_JetBDTloose",
    #        key         = "TauLoose",
    #        scale       = None,
    #        )
    loop += ztautau.algs.weights.ObjWeight(
            obj_name    = "tau_0",
            branch_name = "TauEffSF_HadTauEleOLR_tauhad",
            key         = "TauEVeto",
            scale       = None,
            )
    loop += ztautau.algs.weights.ObjWeight(
            obj_name    = "lep_0",
            branch_name = "MuEffSF_TTVA",
            key         = "MuTTVA",
            scale       = None,
            )
    loop += ztautau.algs.weights.ObjWeight(
            obj_name    = "lep_0",
            branch_name = "MuEffSF_Reco_QualMedium",
            key         = "MuRecoID",
            scale       = None,
            )
    loop += ztautau.algs.weights.ObjWeight(
            obj_name    = "lep_0",
            branch_name = "MuEffSF_IsoGradient",
            key         = "MuIsoGrad",
            scale       = None,
            )
    loop += ztautau.algs.weights.ObjWeight(
            obj_name    = "lep_0",
            branch_name = "MuEffSF_IsoLoose",
            key         = "MuIsoLoose",
            scale       = None,
            )
    loop += ztautau.algs.weights.ObjWeight(
            obj_name    = "lep_0",
            branch_name = "EleEffSF_offline_RecoTrk",
            key         = "ElRecoTrk",
            scale       = None,
            )
    loop += ztautau.algs.weights.ObjWeight(
            obj_name    = "lep_0",
            branch_name = "EleEffSF_offline_MediumLLH_d0z0_v11",
            key         = "ElID",
            scale       = None,
            )
    loop += ztautau.algs.weights.ObjWeight(
            obj_name    = "lep_0",
            branch_name = "EleEffSF_Isolation_MediumLLH_d0z0_v11_isolGradient",
            key         = "ElIsoGrad",
            scale       = None,
            )
    loop += ztautau.algs.weights.ObjWeight(
            obj_name    = "lep_0",
            branch_name = "EleEffSF_Isolation_MediumLLH_d0z0_v11_isolLoose",
            key         = "ElIsoLoose",
            scale       = None,
            )
    loop += ztautau.algs.weights.ObjWeight(
            obj_name    = "lep_0",
            branch_name = "MuEffSF_HLT_mu20_iloose_L1MU15_OR_HLT_mu40_QualMedium_IsoNone",
            key         = "MuTrig2015",
            scale       = None,
            )
    loop += ztautau.algs.weights.ObjWeight(
            obj_name    = "lep_0",
            branch_name = "MuEffSF_HLT_mu26_ivarmedium_OR_HLT_mu50_QualMedium_IsoNone",
            key         = "MuTrig2016",
            scale       = None,
            )
    loop += ztautau.algs.weights.ObjWeight(
            obj_name    = "lep_0",
            branch_name = "EleEffSF_SINGLE_E_2015_e24_lhmedium_L1EM20VH_OR_e60_lhmedium_OR_e120_lhloose_2016_e26_lhtight_nod0_ivarloose_OR_e60_lhmedium_nod0_OR_e140_lhloose_nod0_MediumLLH_d0z0_v11_isolGradient",
            key         = "ElTrig2015",
            scale       = None,
            )
    loop += ztautau.algs.weights.ObjWeight(
            obj_name    = "lep_0",
            branch_name = "EleEffSF_SINGLE_E_2015_e24_lhmedium_L1EM20VH_OR_e60_lhmedium_OR_e120_lhloose_2016_e26_lhtight_nod0_ivarloose_OR_e60_lhmedium_nod0_OR_e140_lhloose_nod0_MediumLLH_d0z0_v11_isolGradient",
            key         = "ElTrig2016",
            scale       = None,
            )
    loop += ztautau.algs.weights.ObjWeight(
            obj_name    = "jet",
            branch_name = "global_effSF_MVX",
            key         = "JetEff",
            scale       = None,
            )
    loop += ztautau.algs.weights.ObjWeight(
            obj_name    = "jet",
            branch_name = "global_ineffSF_MVX",
            key         = "JetIneff",
            scale       = None,
            )
    loop += ztautau.algs.weights.ObjWeight(
            obj_name    = "jet",
            branch_name = "central_jets_global_effSF_JVT",
            key         = "JetJVT",
            scale       = None,
            )
    


    ## configure histograms
    ## ---------------------------------------
    hist_list = []
    hist_list += ztautau.hists.Main_hists.hist_list
    hist_presel = []
    hist_presel += ztautau.hists.Main_hists.hist_presel
    hist_list += ztautau.hists.H2D_hists.hist_list
   


    ##-------------------------------------------------------------------------
    ## make plots
    ##-------------------------------------------------------------------------
    
    import itertools as it
    chan = ['mu', 'el']
    year = ['15', '16']
    comb = list(it.product(chan, year))
    cutbase = [
    ]
    cutflow = {'mu': {'15': [], '16': []}, 'el': {'15': [], '16': []}}
    ## Data regions for bkgd estimate
    antiiso = {'mu': {'15': [], '16': []}, 'el': {'15': [], '16': []}}
    sswjtcr = {'mu': {'15': [], '16': []}, 'el': {'15': [], '16': []}}
    osaidcr = {'mu': {'15': [], '16': []}, 'el': {'15': [], '16': []}}
    ## Canonical region name
    regname = {'mu': {'15': [], '16': []}, 'el': {'15': [], '16': []}}
    for c in comb:
        if c[0] == 'mu': 
            if   c[1] == '15':
                cutflow[c[0]][c[1]] += [['MuonOnly', None] , ['2015MuonTrig' , ['MuTrig2015']]]
                antiiso[c[0]][c[1]] += [['MuonOnly', None] , ['2015MuonTrig' , ['MuTrig2015']]]
                sswjtcr[c[0]][c[1]] += [['MuonOnly', None] , ['2015MuonTrig' , ['MuTrig2015']]]
                osaidcr[c[0]][c[1]] += [['MuonOnly', None] , ['2015MuonTrig' , ['MuTrig2015']]]
            elif c[1] == '16':
                cutflow[c[0]][c[1]] += [['MuonOnly', None] , ['2016MuonTrig' , ['MuTrig2016']]]
                antiiso[c[0]][c[1]] += [['MuonOnly', None] , ['2016MuonTrig' , ['MuTrig2016']]]
                sswjtcr[c[0]][c[1]] += [['MuonOnly', None] , ['2016MuonTrig' , ['MuTrig2016']]]
                osaidcr[c[0]][c[1]] += [['MuonOnly', None] , ['2016MuonTrig' , ['MuTrig2016']]]
            cutflow[c[0]][c[1]] += [
                                   ['OS'           , None] ,
                                   ['LepPt'        , ['MuTTVA']] , 
                                   ['LepQual'      , ['MuRecoID']] ,
                                   ['LepIso'       , ['MuIsoGrad']] ,
                                   ['TauPt'        , ['TauReco']] , 
                                   ['TauQual'      , None] , 
                                   ['TauID'        , ['TauID']] , 
                                   ['SCDP'         , None] , 
                                   ]
            antiiso[c[0]][c[1]] += [
                                   ['OS'           , None] ,
                                   ['LepPt'        , ['MuTTVA']] , 
                                   ['LepQual'      , ['MuRecoID']] ,
                                   ['LepIsoLoose'  , ['MuIsoLoose']] ,
                                   ['TauPt'        , ['TauReco']] , 
                                   ['TauQual'      , None] , 
                                   ['TauID'        , ['TauID']] , 
                                   ['SCDP'         , None] , 
                                   ]
            sswjtcr[c[0]][c[1]] += [
                                   ['SS'           , None] ,
                                   ['LepPt'        , ['MuTTVA']] , 
                                   ['LepQual'      , ['MuRecoID']] ,
                                   ['LepIso'       , ['MuIsoGrad']] ,
                                   ['TauPt'        , ['TauReco']] , 
                                   ['TauQual'      , None] , 
                                   ['TauLoose'     , None] , 
                                   ['SCDP'         , None] , 
                                   ]
            osaidcr[c[0]][c[1]] += [
                                   ['OS'           , None] ,
                                   ['LepPt'        , ['MuTTVA']] , 
                                   ['LepQual'      , ['MuRecoID']] ,
                                   ['LepIso'       , ['MuIsoGrad']] ,
                                   ['TauPt'        , ['TauReco']] , 
                                   ['TauQual'      , None] , 
                                   ['TauLooseNMed' , None] , 
                                   ['SCDP'         , None] , 
                                   ]
        if c[0] == 'el': 
            if   c[1] == '15':
                cutflow[c[0]][c[1]] += [['ElecOnly', None] , ['2015ElecTrig' , ['ElTrig2015']]]
                antiiso[c[0]][c[1]] += [['ElecOnly', None] , ['2015ElecTrig' , ['ElTrig2015']]]
                sswjtcr[c[0]][c[1]] += [['ElecOnly', None] , ['2015ElecTrig' , ['ElTrig2015']]]
                osaidcr[c[0]][c[1]] += [['ElecOnly', None] , ['2015ElecTrig' , ['ElTrig2015']]]
            elif c[1] == '16':
                cutflow[c[0]][c[1]] += [['ElecOnly', None] , ['2016ElecTrig' , ['ElTrig2016']]]
                antiiso[c[0]][c[1]] += [['ElecOnly', None] , ['2016ElecTrig' , ['ElTrig2016']]]
                sswjtcr[c[0]][c[1]] += [['ElecOnly', None] , ['2016ElecTrig' , ['ElTrig2016']]]
                osaidcr[c[0]][c[1]] += [['ElecOnly', None] , ['2016ElecTrig' , ['ElTrig2016']]]
            cutflow[c[0]][c[1]] += [
                                   ['OS'           , None] ,
                                   ['LepPt'        , ['ElRecoTrk']] , 
                                   ['LepQual'      , ['ElID']] ,
                                   ['LepIso'       , ['ElIsoGrad']] ,
                                   ['TauPt'        , ['TauReco']] , 
                                   ['TauQual'      , None] , 
                                   ['TauID'        , ['TauID']] , 
                                   ['TauEVeto'     , ['TauEVeto']] , 
                                   ['SCDP'         , None] , 
                                   ]
            antiiso[c[0]][c[1]] += [
                                   ['OS'           , None] ,
                                   ['LepPt'        , ['ElRecoTrk']] , 
                                   ['LepQual'      , ['ElID']] ,
                                   ['LepIsoLoose'  , ['ElIsoLoose']] ,
                                   ['TauPt'        , ['TauReco']] , 
                                   ['TauQual'      , None] , 
                                   ['TauID'        , ['TauID']] , 
                                   ['TauEVeto'     , ['TauEVeto']] , 
                                   ['SCDP'         , None] , 
                                   ]
            sswjtcr[c[0]][c[1]] += [
                                   ['SS'           , None] ,
                                   ['LepPt'        , ['ElRecoTrk']] , 
                                   ['LepQual'      , ['ElID']] ,
                                   ['LepIso'       , ['ElIsoGrad']] ,
                                   ['TauPt'        , ['TauReco']] , 
                                   ['TauQual'      , None] , 
                                   ['TauLoose'     , None] , 
                                   ['TauEVeto'     , ['TauEVeto']] , 
                                   ['SCDP'         , None] , 
                                   ]
            osaidcr[c[0]][c[1]] += [
                                   ['OS'           , None] ,
                                   ['LepPt'        , ['ElRecoTrk']] , 
                                   ['LepQual'      , ['ElID']] ,
                                   ['LepIso'       , ['ElIsoGrad']] ,
                                   ['TauPt'        , ['TauReco']] , 
                                   ['TauQual'      , None] , 
                                   ['TauLooseNMed' , None] , 
                                   ['TauEVeto'     , ['TauEVeto']] , 
                                   ['SCDP'         , None] , 
                                   ]
        regname[c[0]][c[1]] = c[0]+c[1]
    ## ---------------------------------------
    runSR = False
    if runSR:
        print "Running over SR"
        for c in comb:
            loop += ztautau.algs.algs.PlotAlg(
                    region       = 'presel_'+regname[c[0]][c[1]],
                    do_var_check = True,
                    hist_list    = hist_list+hist_presel,
                    plot_all     = False,
                    cut_flow  = cutflow[c[0]][c[1]]+[
                                  ['Presel', ['JetEff', 'JetIneff']] , 
                                ],
                    )
            loop += ztautau.algs.algs.PlotAlg(
                    region       = 'sr1_'+regname[c[0]][c[1]],
                    do_var_check = True,
                    hist_list    = hist_list,
                    plot_all     = False,
                    cut_flow  = cutflow[c[0]][c[1]]+[
                                  ['SR1', ['JetEff', 'JetIneff']] , 
                                ],
                    )
            loop += ztautau.algs.algs.PlotAlg(
                    region       = 'sr2_'+regname[c[0]][c[1]],
                    do_var_check = True,
                    hist_list    = hist_list,
                    plot_all     = False,
                    cut_flow  = cutflow[c[0]][c[1]]+[
                                  ['SR2', ['JetEff', 'JetIneff']] , 
                                ],
                    )
            loop += ztautau.algs.algs.PlotAlg(
                    region       = 'sr3_'+regname[c[0]][c[1]],
                    do_var_check = True,
                    hist_list    = hist_list,
                    plot_all     = False,
                    cut_flow  = cutflow[c[0]][c[1]]+[
                                  ['SR3', ['JetEff', 'JetIneff']] , 
                                ],
                    )
    runCR = False
    if runCR:
        print "Running over CR"
        for c in comb:
            loop += ztautau.algs.algs.PlotAlg(
                    region       = 'tcr_'+regname[c[0]][c[1]],
                    do_var_check = True,
                    hist_list    = hist_list,
                    plot_all     = False,
                    cut_flow  = cutflow[c[0]][c[1]]+[
                                  ['TCR', ['JetEff', 'JetIneff']] , 
                                ],
                    )
            loop += ztautau.algs.algs.PlotAlg(
                    region       = 'wcr_'+regname[c[0]][c[1]],
                    do_var_check = True,
                    hist_list    = hist_list,
                    plot_all     = False,
                    cut_flow  = cutflow[c[0]][c[1]]+[
                                  ['WCR', ['JetEff', 'JetIneff']] , 
                                ],
                    )
            loop += ztautau.algs.algs.PlotAlg(
                    region       = 'qcdcr_'+regname[c[0]][c[1]],
                    do_var_check = True,
                    hist_list    = hist_list,
                    plot_all     = False,
                    cut_flow  = cutflow[c[0]][c[1]]+[
                                  ['QCDCR', ['JetEff', 'JetIneff']] , 
                                ],
                    )
            loop += ztautau.algs.algs.PlotAlg(
                    region       = 'qcdcr2_'+regname[c[0]][c[1]],
                    do_var_check = True,
                    hist_list    = hist_list,
                    plot_all     = False,
                    cut_flow  = cutflow[c[0]][c[1]]+[
                                  ['QCDCR2', ['JetEff', 'JetIneff']] , 
                                ],
                    )
            loop += ztautau.algs.algs.PlotAlg(
                    region       = 'zcr_'+regname[c[0]][c[1]],
                    do_var_check = True,
                    hist_list    = hist_list,
                    plot_all     = False,
                    cut_flow  = cutflow[c[0]][c[1]]+[
                                  ['ZCR', ['JetEff', 'JetIneff']] , 
                                  ['TESTFRIEND', None] , 
                                ],
                    )
    ## Comment following lines out
    runDD = True
    runAntiIso = False
    runOSAntiID = True
    runSS = False
    if config['sampletype'] == 'data' and runDD:
        print "Running over data-driven regions"
        if runAntiIso:
            for c in comb:
                loop += ztautau.algs.algs.PlotAlg(
                        region       = 'presel_antiiso'+regname[c[0]][c[1]],
                        do_var_check = True,
                        hist_list    = hist_list+hist_presel,
                        plot_all     = False,
                        cut_flow  = antiiso[c[0]][c[1]]+[
                                      ['Presel', ['JetEff', 'JetIneff']] , 
                                    ],
                        )
                loop += ztautau.algs.algs.PlotAlg(
                        region       = 'sr1_antiiso'+regname[c[0]][c[1]],
                        do_var_check = True,
                        hist_list    = hist_list,
                        plot_all     = False,
                        cut_flow  = antiiso[c[0]][c[1]]+[
                                      ['SR1', ['JetEff', 'JetIneff']] , 
                                    ],
                        )
                loop += ztautau.algs.algs.PlotAlg(
                        region       = 'sr2_antiiso'+regname[c[0]][c[1]],
                        do_var_check = True,
                        hist_list    = hist_list,
                        plot_all     = False,
                        cut_flow  = antiiso[c[0]][c[1]]+[
                                      ['SR2', ['JetEff', 'JetIneff']] , 
                                    ],
                        )
                loop += ztautau.algs.algs.PlotAlg(
                        region       = 'sr3_antiiso'+regname[c[0]][c[1]],
                        do_var_check = True,
                        hist_list    = hist_list,
                        plot_all     = False,
                        cut_flow  = antiiso[c[0]][c[1]]+[
                                      ['SR3', ['JetEff', 'JetIneff']] , 
                                    ],
                        )
                if not runCR: continue
                loop += ztautau.algs.algs.PlotAlg(
                        region       = 'tcr_antiiso'+regname[c[0]][c[1]],
                        do_var_check = True,
                        hist_list    = hist_list,
                        plot_all     = False,
                        cut_flow  = antiiso[c[0]][c[1]]+[
                                      ['TCR', ['JetEff', 'JetIneff']] , 
                                    ],
                        )
                loop += ztautau.algs.algs.PlotAlg(
                        region       = 'wcr_antiiso'+regname[c[0]][c[1]],
                        do_var_check = True,
                        hist_list    = hist_list,
                        plot_all     = False,
                        cut_flow  = antiiso[c[0]][c[1]]+[
                                      ['WCR', ['JetEff', 'JetIneff']] , 
                                    ],
                        )
                loop += ztautau.algs.algs.PlotAlg(
                        region       = 'qcdcr_antiiso'+regname[c[0]][c[1]],
                        do_var_check = True,
                        hist_list    = hist_list,
                        plot_all     = False,
                        cut_flow  = antiiso[c[0]][c[1]]+[
                                      ['QCDCR', ['JetEff', 'JetIneff']] , 
                                    ],
                        )
                loop += ztautau.algs.algs.PlotAlg(
                        region       = 'qcdcr2_antiiso'+regname[c[0]][c[1]],
                        do_var_check = True,
                        hist_list    = hist_list,
                        plot_all     = False,
                        cut_flow  = antiiso[c[0]][c[1]]+[
                                      ['QCDCR2', ['JetEff', 'JetIneff']] , 
                                    ],
                        )
                loop += ztautau.algs.algs.PlotAlg(
                        region       = 'zcr_antiiso'+regname[c[0]][c[1]],
                        do_var_check = True,
                        hist_list    = hist_list,
                        plot_all     = False,
                        cut_flow  = antiiso[c[0]][c[1]]+[
                                      ['ZCR', ['JetEff', 'JetIneff']] , 
                                    ],
                        )
        if runOSAntiID:
            for c in comb:
                print "Analysing", c
                loop += ztautau.algs.algs.PlotAlg(
                        region       = 'presel_osaidcr'+regname[c[0]][c[1]],
                        do_var_check = True,
                        hist_list    = hist_list+hist_presel,
                        plot_all     = False,
                        cut_flow  = osaidcr[c[0]][c[1]]+[
                                      ['Presel', ['JetEff', 'JetIneff']] , 
                                    ],
                        )
                loop += ztautau.algs.algs.PlotAlg(
                        region       = 'sr1_osaidcr'+regname[c[0]][c[1]],
                        do_var_check = True,
                        hist_list    = hist_list,
                        plot_all     = False,
                        cut_flow  = osaidcr[c[0]][c[1]]+[
                                      ['SR1', ['JetEff', 'JetIneff']] , 
                                    ],
                        )
                loop += ztautau.algs.algs.PlotAlg(
                        region       = 'sr2_osaidcr'+regname[c[0]][c[1]],
                        do_var_check = True,
                        hist_list    = hist_list,
                        plot_all     = False,
                        cut_flow  = osaidcr[c[0]][c[1]]+[
                                      ['SR2', ['JetEff', 'JetIneff']] , 
                                    ],
                        )
                loop += ztautau.algs.algs.PlotAlg(
                        region       = 'sr3_osaidcr'+regname[c[0]][c[1]],
                        do_var_check = True,
                        hist_list    = hist_list,
                        plot_all     = False,
                        cut_flow  = osaidcr[c[0]][c[1]]+[
                                      ['SR3', ['JetEff', 'JetIneff']] , 
                                    ],
                        )
                if not runCR: continue
                loop += ztautau.algs.algs.PlotAlg(
                        region       = 'tcr_osaidcr'+regname[c[0]][c[1]],
                        do_var_check = True,
                        hist_list    = hist_list,
                        plot_all     = False,
                        cut_flow  = osaidcr[c[0]][c[1]]+[
                                      ['TCR', ['JetEff', 'JetIneff']] , 
                                    ],
                        )
                loop += ztautau.algs.algs.PlotAlg(
                        region       = 'wcr_osaidcr'+regname[c[0]][c[1]],
                        do_var_check = True,
                        hist_list    = hist_list,
                        plot_all     = False,
                        cut_flow  = osaidcr[c[0]][c[1]]+[
                                      ['WCR', ['JetEff', 'JetIneff']] , 
                                    ],
                        )
                loop += ztautau.algs.algs.PlotAlg(
                        region       = 'qcdcr_osaidcr'+regname[c[0]][c[1]],
                        do_var_check = True,
                        hist_list    = hist_list,
                        plot_all     = False,
                        cut_flow  = osaidcr[c[0]][c[1]]+[
                                      ['QCDCR', ['JetEff', 'JetIneff']] , 
                                    ],
                        )
                loop += ztautau.algs.algs.PlotAlg(
                        region       = 'qcdcr2_osaidcr'+regname[c[0]][c[1]],
                        do_var_check = True,
                        hist_list    = hist_list,
                        plot_all     = False,
                        cut_flow  = osaidcr[c[0]][c[1]]+[
                                      ['QCDCR2', ['JetEff', 'JetIneff']] , 
                                    ],
                        )
                loop += ztautau.algs.algs.PlotAlg(
                        region       = 'zcr_osaidcr'+regname[c[0]][c[1]],
                        do_var_check = True,
                        hist_list    = hist_list,
                        plot_all     = False,
                        cut_flow  = osaidcr[c[0]][c[1]]+[
                                      ['ZCR', ['JetEff', 'JetIneff']] , 
                                    ],
                        )
        if runSS:
            for c in comb:
                print "Analysing", c
                loop += ztautau.algs.algs.PlotAlg(
                        region       = 'presel_sswjtcr'+regname[c[0]][c[1]],
                        do_var_check = True,
                        hist_list    = hist_list+hist_presel,
                        plot_all     = False,
                        cut_flow  = sswjtcr[c[0]][c[1]]+[
                                      ['Presel', ['JetEff', 'JetIneff']] , 
                                    ],
                        )
                loop += ztautau.algs.algs.PlotAlg(
                        region       = 'sr1_sswjtcr'+regname[c[0]][c[1]],
                        do_var_check = True,
                        hist_list    = hist_list,
                        plot_all     = False,
                        cut_flow  = sswjtcr[c[0]][c[1]]+[
                                      ['SR1', ['JetEff', 'JetIneff']] , 
                                    ],
                        )
                loop += ztautau.algs.algs.PlotAlg(
                        region       = 'sr2_sswjtcr'+regname[c[0]][c[1]],
                        do_var_check = True,
                        hist_list    = hist_list,
                        plot_all     = False,
                        cut_flow  = sswjtcr[c[0]][c[1]]+[
                                      ['SR2', ['JetEff', 'JetIneff']] , 
                                    ],
                        )
                loop += ztautau.algs.algs.PlotAlg(
                        region       = 'sr3_sswjtcr'+regname[c[0]][c[1]],
                        do_var_check = True,
                        hist_list    = hist_list,
                        plot_all     = False,
                        cut_flow  = sswjtcr[c[0]][c[1]]+[
                                      ['SR3', ['JetEff', 'JetIneff']] , 
                                    ],
                        )
                if not runCR: continue
                loop += ztautau.algs.algs.PlotAlg(
                        region       = 'tcr_sswjtcr'+regname[c[0]][c[1]],
                        do_var_check = True,
                        hist_list    = hist_list,
                        plot_all     = False,
                        cut_flow  = sswjtcr[c[0]][c[1]]+[
                                      ['TCR', ['JetEff', 'JetIneff']] , 
                                    ],
                        )
                loop += ztautau.algs.algs.PlotAlg(
                        region       = 'wcr_sswjtcr'+regname[c[0]][c[1]],
                        do_var_check = True,
                        hist_list    = hist_list,
                        plot_all     = False,
                        cut_flow  = sswjtcr[c[0]][c[1]]+[
                                      ['WCR', ['JetEff', 'JetIneff']] , 
                                    ],
                        )
                loop += ztautau.algs.algs.PlotAlg(
                        region       = 'qcdcr_sswjtcr'+regname[c[0]][c[1]],
                        do_var_check = True,
                        hist_list    = hist_list,
                        plot_all     = False,
                        cut_flow  = sswjtcr[c[0]][c[1]]+[
                                      ['QCDCR', ['JetEff', 'JetIneff']] , 
                                    ],
                        )
                loop += ztautau.algs.algs.PlotAlg(
                        region       = 'qcdcr2_sswjtcr'+regname[c[0]][c[1]],
                        do_var_check = True,
                        hist_list    = hist_list,
                        plot_all     = False,
                        cut_flow  = sswjtcr[c[0]][c[1]]+[
                                      ['QCDCR2', ['JetEff', 'JetIneff']] , 
                                    ],
                        )
                loop += ztautau.algs.algs.PlotAlg(
                        region       = 'zcr_sswjtcr'+regname[c[0]][c[1]],
                        do_var_check = True,
                        hist_list    = hist_list,
                        plot_all     = False,
                        cut_flow  = sswjtcr[c[0]][c[1]]+[
                                      ['ZCR', ['JetEff', 'JetIneff']] , 
                                    ],
                        )
    
    loop += pyframe.algs.HistCopyAlg()

    ##-------------------------------------------------------------------------
    ## run the job
    ##-------------------------------------------------------------------------
    loop.run(chain, 0, config['events'],
            branches_on_file = config.get('branches_on_file'),
            do_var_log = config.get('do_var_log'),
            )

#______________________________________________________________________________
if __name__ == '__main__':
    pyframe.config.main(analyze)









