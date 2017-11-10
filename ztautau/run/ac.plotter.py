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
            scale       = None,
            )
    loop += ztautau.algs.weights.ObjWeight(
            obj_name    = "tau_0",
            branch_name = "TauEffSF_JetBDTmedium",
            key         = "TauIDMedium",
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
        cutflow[c[0]][c[1]][c[2]] += [[c[2]                      , None ],
                                      ['%sOnly' % lep            , None ],
                                      #['TrueTau'                , None ],
                                      ['20%s%sTrig' % (c[1],lep) , None ],
                                      ['PVX'                     , None ],
                                      ['LepQual'                 , None ],
                                      ['LepIso'                  , None ],
                                      ['TauQual'                 , None ],
                                      ['OS'                      , None ],
                                      ['TauID'                   , None ],
                                      ['NoJetFake'               , None ],
                                      ['LepPt'                   , None ],
                                      ['TauPt'                   , None ],
                                      ['tauEveto'                , None ],
                                      ['SCDP'                    , None ],
                                      ['dEta'                    , None ],
                                      ['BVeto'                   , None ]
                                      ]
        regname[c[0]][c[1]][c[2]] = c[0]+c[1]+c[2]
        if  config['datatype'] == 'qcd': 
            cutflow[c[0]][c[1]][c[2]] = replace_cut(cutflow[c[0]][c[1]][c[2]], ['LepIso', None], ['LepAntiIso',   None])
        elif config['datatype'] == 'osw':
            cutflow[c[0]][c[1]][c[2]] = replace_cut(cutflow[c[0]][c[1]][c[2]], ['TauID',  None], ['TauLooseNMed', None])
        elif config['datatype'] == 'ssw':
            cutflow[c[0]][c[1]][c[2]] = replace_cut(cutflow[c[0]][c[1]][c[2]], ['OS',     None], ['SS',           None])
            cutflow[c[0]][c[1]][c[2]] = replace_cut(cutflow[c[0]][c[1]][c[2]], ['TauID',  None], ['TauLoose',     None])
        elif config['datatype'] == 'ff' :
            cutflow[c[0]][c[1]][c[2]] = replace_cut(cutflow[c[0]][c[1]][c[2]], ['TauID',  None], ['TauAntiID',    None])
        #print cutflow[c[0]][c[1]][c[2]]

    ## ---------------------------------------
    print "Running over SR"
    for c in comb:
        loop += ztautau.algs.algs.PlotAlg(
                region       = 'presel'+suffix+regname[c[0]][c[1]][c[2]],
                do_var_check = True,
                hist_list    = ztautau.hists.Main_hists.hist_ac,
                plot_all     = False,
                cut_flow  =  cutflow[c[0]][c[1]][c[2]],
                )
    
    #loop += ztautau.algs.algs.PlotAlg(
    #        region       = 'presel_test',
    #        do_var_check = True,
    #        hist_list    = ztautau.hists.Main_hists.hist_ac,
    #        plot_all     = False,
    #        cut_flow  =  [['ElecOnly', None], ['tauEveto', None]]
    #        )
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

