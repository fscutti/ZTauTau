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
    
    # This is how you tell the weights what is the direction of the variation
    # Within the weight implementation, an alternative branch has to be retrieved for SYS_XX weights,
    # based on the value of sys_var, while for TREE_SYS_XX no preconfiguartion of sys_var is necessary.
    elif sys == 'SYS_UP':            sys_dict = get_sys_dict(sys_name = sys, sys_var = "up")
    elif sys == 'SYS_UP':            sys_dict = get_sys_dict(sys_name = sys, sys_var = "dn")
    elif sys == 'TREESYS_UP':        sys_dict = get_sys_dict(sys_name = sys, sys_tree = "MySysTreeName",  sys_var = "up")
    elif sys == 'TREESYS_DN':        sys_dict = get_sys_dict(sys_name = sys, sys_tree = "MySysTreeName",  sys_var = "dn")
     
    elif sys == "MUON_ID_1down":  
      sys_dict = get_sys_dict(sys_tree = sys, sys_friendtree = "NN_"+sys, sys_var = "dn")
  
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
    isSig = True if ('lp15hm20' in config['friendinput'] or 'lm15hp20' in config['friendinput']) else False
    loop += ztautau.algs.weights.WeightTotal(cutflow='PreselMu2016',key='weight_total', isSig=isSig)
    if config['datatype'] == 'ff': 
        loop += ztautau.algs.weights.FFTotal(cutflow='PreselMu2016',key='ff')


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
            scale       = sys_dict["variation"],
            )
    loop += ztautau.algs.weights.ObjWeight(
            obj_name    = "tau_0",
            branch_name = "TauEffSF_JetBDTmedium",
            key         = "TauIDMedium",
            scale       = sys_dict['variation'],
            )
    #loop += ztautau.algs.weights.ObjWeight(
    #        obj_name    = "tau_0",
    #        branch_name = "TauEffSF_JetBDTloose",
    #        key         = "TauLoose",
    #        scale       = sys_dict["variation"],
    #        )
    loop += ztautau.algs.weights.ObjWeight(
            obj_name    = "tau_0",
            branch_name = "TauEffSF_HadTauEleOLR_tauhad",
            key         = "TauEVeto",
            scale       = sys_dict["variation"],
            )
    loop += ztautau.algs.weights.ObjWeight(
            obj_name    = "lep_0",
            branch_name = "MuEffSF_TTVA",
            key         = "MuonTTVA",
            scale       = sys_dict["variation"],
            )
    loop += ztautau.algs.weights.ObjWeight(
            obj_name    = "lep_0",
            branch_name = "MuEffSF_Reco_QualMedium",
            key         = "MuonRecoID",
            scale       = sys_dict["variation"],
            )
    loop += ztautau.algs.weights.ObjWeight(
            obj_name    = "lep_0",
            branch_name = "MuEffSF_IsoGradient",
            key         = "MuonIsoGrad",
            scale       = sys_dict["variation"],
            )
    loop += ztautau.algs.weights.ObjWeight(
            obj_name    = "lep_0",
            branch_name = "MuEffSF_IsoLoose",
            key         = "MuonIsoLoose",
            scale       = sys_dict["variation"],
            )
    loop += ztautau.algs.weights.ObjWeight(
            obj_name    = "lep_0",
            branch_name = "EleEffSF_offline_RecoTrk",
            key         = "ElecRecoTrk",
            scale       = sys_dict["variation"],
            )
    loop += ztautau.algs.weights.ObjWeight(
            obj_name    = "lep_0",
            branch_name = "EleEffSF_offline_MediumLLH_d0z0_v11",
            key         = "ElecID",
            scale       = sys_dict["variation"],
            )
    loop += ztautau.algs.weights.ObjWeight(
            obj_name    = "lep_0",
            branch_name = "EleEffSF_Isolation_MediumLLH_d0z0_v11_isolGradient",
            key         = "ElecIsoGrad",
            scale       = sys_dict["variation"],
            )
    loop += ztautau.algs.weights.ObjWeight(
            obj_name    = "lep_0",
            branch_name = "EleEffSF_Isolation_MediumLLH_d0z0_v11_isolLoose",
            key         = "ElecIsoLoose",
            scale       = sys_dict["variation"],
            )
    loop += ztautau.algs.weights.ObjWeight(
            obj_name    = "lep_0",
            branch_name = "MuEffSF_HLT_mu20_iloose_L1MU15_OR_HLT_mu40_QualMedium_IsoNone",
            key         = "MuonTrig2015",
            scale       = sys_dict["variation"],
            )
    loop += ztautau.algs.weights.ObjWeight(
            obj_name    = "lep_0",
            branch_name = "MuEffSF_HLT_mu26_ivarmedium_OR_HLT_mu50_QualMedium_IsoNone",
            key         = "MuonTrig2016",
            scale       = sys_dict["variation"],
            )
    loop += ztautau.algs.weights.ObjWeight(
            obj_name    = "lep_0",
            branch_name = "EleEffSF_SINGLE_E_2015_e24_lhmedium_L1EM20VH_OR_e60_lhmedium_OR_e120_lhloose_2016_e26_lhtight_nod0_ivarloose_OR_e60_lhmedium_nod0_OR_e140_lhloose_nod0_MediumLLH_d0z0_v11_isolGradient",
            key         = "ElecTrig2015",
            scale       = sys_dict["variation"],
            )
    loop += ztautau.algs.weights.ObjWeight(
            obj_name    = "lep_0",
            branch_name = "EleEffSF_SINGLE_E_2015_e24_lhmedium_L1EM20VH_OR_e60_lhmedium_OR_e120_lhloose_2016_e26_lhtight_nod0_ivarloose_OR_e60_lhmedium_nod0_OR_e140_lhloose_nod0_MediumLLH_d0z0_v11_isolGradient",
            key         = "ElecTrig2016",
            scale       = sys_dict["variation"],
            )
    loop += ztautau.algs.weights.ObjWeight(
            obj_name    = "jet",
            branch_name = "global_effSF_MVX",
            key         = "JetEff",
            scale       = sys_dict["variation"],
            )
    loop += ztautau.algs.weights.ObjWeight(
            obj_name    = "jet",
            branch_name = "global_ineffSF_MVX",
            key         = "JetIneff",
            scale       = sys_dict["variation"],
            )
    loop += ztautau.algs.weights.ObjWeight(
            obj_name    = "jet",
            branch_name = "central_jets_global_effSF_JVT",
            key         = "JetJVT",
            scale       = sys_dict["variation"],
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
    
    if not 'datatype' in config.keys():
        suffix = '_'
    else:
        if config['datatype'] == 'qcd': 
            suffix = '_antiiso'
        elif config['datatype'] == 'osw':
            suffix = '_osaidcr'
        elif config['datatype'] == 'ssw':
            suffix = '_sswjtcr'
        else:
            suffix = '_'

    def replace_cut(cuts, rm_cut, add_cut):
        newcuts = []
        count = False
        for cut in cuts:
            if cut == rm_cut:
                if add_cut: newcuts.append(add_cut)
                count = True
            else: newcuts.append(cut)
        if not count:
            raise ValueError ("Cut %s not found! Please look into this!" % rm_cut[0])
        return newcuts

    import itertools as it
    chan = ['mu', 'el']
    year = ['15', '16']
    trck = ['1p', '3p']
    comb = list(it.product(chan, year, trck))
    cutflow = {'mu': {'15': {'1p': [], '3p': []}, '16': {'1p': [], '3p': []}}, 'el': {'15': {'1p': [], '3p': []}, '16': {'1p': [], '3p': []}}}
    ## Canonical region name
    regname = {'mu': {'15': {'1p': [], '3p': []}, '16': {'1p': [], '3p': []}}, 'el': {'15': {'1p': [], '3p': []}, '16': {'1p': [], '3p': []}}}
    for c in comb:
        lep = 'Muon' if c[0] == 'mu' else 'Elec' if c[0] =='el' else None
        if lep == 'Muon':
            lepsf    = ['MuonTTVA', 'MuonRecoID']
        else:
            lepsf    = ['ElecRecoTrk', 'ElecID' ]
        cutflow[c[0]][c[1]][c[2]] += [[c[2]                      , None ],
                                      ['%sOnly' % lep            , None ],
                                      #['TrueTau'                , None ],
                                      ['20%s%sTrig' % (c[1],lep) , ['%sTrig20%s' % (lep,c[1])] ],
                                      ['PVX'                     , None ],
                                      ['LepQual'                 , lepsf ],
                                      ['LepIso'                  , ['%sIsoGrad' % lep] ],
                                      ['TauQual'                 , ['TauReco'] ],
                                      ['OS'                      , None ],
                                      ['TauID'                   , ['TauIDMedium'] ],
                                      ['NoJetFake'               , None ],
                                      ['LepPt'                   , None ],
                                      ['TauPt'                   , None ],
                                      ['tauEveto'                , ['TauEVeto'] ],
                                      ['SCDP'                    , None ],
                                      ['dEta'                    , None ],
                                      ['BVeto'                   , None ]
                                      ]
        regname[c[0]][c[1]][c[2]] = c[0]+c[1]+c[2]
        if  config['datatype'] == 'qcd': 
            cutflow[c[0]][c[1]][c[2]] = replace_cut(cutflow[c[0]][c[1]][c[2]], ['LepIso', ['%sIsoGrad' % lep]], ['LepAntiIso',   None])
        elif config['datatype'] == 'osw':
            cutflow[c[0]][c[1]][c[2]] = replace_cut(cutflow[c[0]][c[1]][c[2]], ['TauID',  ['TauIDMedium']],     ['TauLooseNMed', None])
        elif config['datatype'] == 'ssw':
            cutflow[c[0]][c[1]][c[2]] = replace_cut(cutflow[c[0]][c[1]][c[2]], ['OS', None], ['SS', None])
            cutflow[c[0]][c[1]][c[2]] = replace_cut(cutflow[c[0]][c[1]][c[2]], ['TauID',  ['TauIDMedium']],     ['TauLoose',     None])
        elif config['datatype'] == 'ff' :
            cutflow[c[0]][c[1]][c[2]] = replace_cut(cutflow[c[0]][c[1]][c[2]], ['TauID',  ['TauIDMedium']],     ['TauAntiID',    None])
        #print cutflow[c[0]][c[1]][c[2]]

    ## ---------------------------------------
    print "Running over SR"
    for c in comb:
        loop += ztautau.algs.algs.PlotAlg(
                region       = 'presel'+suffix+regname[c[0]][c[1]][c[2]],
                do_var_check = True,
                hist_list    = ztautau.hists.Main_hists.hist_presel,
                plot_all     = False,
                cut_flow  =  cutflow[c[0]][c[1]][c[2]],
                )
        loop += ztautau.algs.algs.PlotAlg(
                region       = 'sr1'+suffix+regname[c[0]][c[1]][c[2]],
                do_var_check = True,
                hist_list    = ztautau.hists.Main_hists.hist_presel,
                plot_all     = False,
                cut_flow  =  cutflow[c[0]][c[1]][c[2]]+[['SR1', None]],
                )
        loop += ztautau.algs.algs.PlotAlg(
                region       = 'sr2'+suffix+regname[c[0]][c[1]][c[2]],
                do_var_check = True,
                hist_list    = ztautau.hists.Main_hists.hist_presel,
                plot_all     = False,
                cut_flow  =  cutflow[c[0]][c[1]][c[2]]+[['SR2', None]],
                )
        loop += ztautau.algs.algs.PlotAlg(
                region       = 'sr3'+suffix+regname[c[0]][c[1]][c[2]],
                do_var_check = True,
                hist_list    = ztautau.hists.Main_hists.hist_presel,
                plot_all     = False,
                cut_flow  =  cutflow[c[0]][c[1]][c[2]]+[['SR3', None]],
                )
        loop += ztautau.algs.algs.PlotAlg(
                region       = 'highZ'+suffix+regname[c[0]][c[1]][c[2]],
                do_var_check = True,
                hist_list    = ztautau.hists.Main_hists.hist_presel,
                plot_all     = False,
                cut_flow  =  cutflow[c[0]][c[1]][c[2]]+[['highZNN', None]],
                )
        loop += ztautau.algs.algs.PlotAlg(
                region       = 'lowZ'+suffix+regname[c[0]][c[1]][c[2]],
                do_var_check = True,
                hist_list    = ztautau.hists.Main_hists.hist_presel,
                plot_all     = False,
                cut_flow  =  cutflow[c[0]][c[1]][c[2]]+[['lowZNN', None]],
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

