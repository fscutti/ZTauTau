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
def get_sys_dict(sys_name=None, sys_tree="NOMINAL", sys_var=None):
  return {"name":sys_name, "tree":sys_tree, "variation":sys_var}
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
    
    chain = ROOT.TChain(config['tree'])
    for fn in config['input']: chain.Add(fn)

    ##-------------------------------------------------------------------------
    ## event loop
    ##-------------------------------------------------------------------------
    loop = pyframe.core.EventLoop(name='ztautau',
                                  sampletype=config['sampletype'],
                                  samplename=config['samplename'],
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
    
    ## TEST region
    ## ---------------------------------------
    PreselEl2016 = ztautau.algs.algs.PlotAlg(
            region       = 'PreselEl2016',
            do_var_check = True,
            hist_list    = hist_list+hist_presel,
            plot_all     = False,
            cut_flow  = [
                          ['ElecOnly'     , ['weight_total']] ,
                          ['2016ElecTrig' , ['ElTrig2016']] ,
                          ['OS'           , None] ,
                          ['LepPt'        , ['ElRecoTrk']] , 
                          ['LepQual'      , ['ElID']] ,
                          ['LepIso'       , ['ElIsoGrad']] ,
                          ['TauPt'        , ['TauReco']] , 
                          ['TauQual'      , None] , 
                          ['TauID'        , ['TauID']] , 
                          ['TauEVeto'     , ['TauEVeto']] , 
                          ['BVeto'        , ['JetEff', 'JetIneff']] , 
                          ['SCDP'         , None] , 
                          ['dEta'         , None] , 
                        ],
            )
    PreselEl2015 = ztautau.algs.algs.PlotAlg(
            region       = 'PreselEl2015',
            do_var_check = True,
            hist_list    = hist_list+hist_presel,
            plot_all     = False,
            cut_flow  = [
                          ['ElecOnly'     , ['weight_total']] ,
                          ['2015ElecTrig' , ['ElTrig2015']] ,
                          ['OS'           , None] ,
                          ['LepPt'        , ['ElRecoTrk']] , 
                          ['LepQual'      , ['ElID']] ,
                          ['LepIso'       , ['ElIsoGrad']] ,
                          ['TauPt'        , ['TauReco']] , 
                          ['TauQual'      , None] , 
                          ['TauID'        , ['TauID']] , 
                          ['TauEVeto'     , ['TauEVeto']] , 
                          ['BVeto'        , ['JetEff', 'JetIneff']] , 
                          ['SCDP'         , None] , 
                          ['dEta'         , None] , 
                        ],
            )
    PreselMu2016 = ztautau.algs.algs.PlotAlg(
            region       = 'PreselMu2016',
            do_var_check = True,
            hist_list    = hist_list+hist_presel,
            plot_all     = False,
            cut_flow  = [
                          ['MuonOnly'     , ['weight_total']] ,
                          ['2016MuonTrig' , ['MuTrig2016']] ,
                          ['OS'           , None] ,
                          ['LepPt'        , ['MuTTVA']] , 
                          ['LepQual'      , ['MuRecoID']] ,
                          ['LepIso'       , ['MuIsoGrad']] ,
                          ['TauPt'        , ['TauReco']] , 
                          ['TauQual'      , None] , 
                          ['TauID'        , ['TauID']] , 
                          ['TauEVeto'     , ['TauEVeto']] , 
                          ['BVeto'        , ['JetEff', 'JetIneff']] , 
                          ['SCDP'         , None] , 
                          ['dEta'         , None] , 
                        ],
            )
    PreselMu2015 = ztautau.algs.algs.PlotAlg(
            region       = 'PreselMu2015',
            do_var_check = True,
            hist_list    = hist_list+hist_presel,
            plot_all     = False,
            cut_flow  = [
                          ['MuonOnly'     , ['weight_total']] ,
                          ['2015MuonTrig' , ['MuTrig2015']] ,
                          ['OS'           , None] ,
                          ['LepPt'        , ['MuTTVA']] , 
                          ['LepQual'      , ['MuRecoID']] ,
                          ['LepIso'       , ['MuIsoGrad']] ,
                          ['TauPt'        , ['TauReco']] , 
                          ['TauQual'      , None] , 
                          ['TauID'        , ['TauID']] , 
                          ['TauEVeto'     , ['TauEVeto']] , 
                          ['BVeto'        , ['JetEff', 'JetIneff']] , 
                          ['SCDP'         , None] , 
                          ['dEta'         , None] , 
                        ],
            )

    loop += PreselMu2015
    loop += PreselMu2016
    loop += PreselEl2015
    loop += PreselEl2016

    #######
    # SR1 #
    #######
    loop += ztautau.algs.algs.PlotAlg(
            region       = 'SR1Mu2015',
            do_var_check = True,
            hist_list    = hist_list,
            plot_all     = False,
            cut_flow     = PreselMu2015.cut_flow+[['SR1', None]]
            )
    
    loop += ztautau.algs.algs.PlotAlg(
            region       = 'SR1Mu2016',
            do_var_check = True,
            hist_list    = hist_list,
            plot_all     = False,
            cut_flow     = PreselMu2016.cut_flow+[['SR1', None]]
            )
    
    loop += ztautau.algs.algs.PlotAlg(
            region       = 'SR1El2015',
            do_var_check = True,
            hist_list    = hist_list,
            plot_all     = False,
            cut_flow     = PreselEl2015.cut_flow+[['SR1', None]]
            )
    
    loop += ztautau.algs.algs.PlotAlg(
            region       = 'SR1El2016',
            do_var_check = True,
            hist_list    = hist_list,
            plot_all     = False,
            cut_flow     = PreselEl2016.cut_flow+[['SR1', None]]
            )
    
    #######
    # SR2 #
    #######
    loop += ztautau.algs.algs.PlotAlg(
            region       = 'SR2Mu2015',
            do_var_check = True,
            hist_list    = hist_list,
            plot_all     = False,
            cut_flow     = PreselMu2015.cut_flow+[['SR2', None]]
            )
    
    loop += ztautau.algs.algs.PlotAlg(
            region       = 'SR2Mu2016',
            do_var_check = True,
            hist_list    = hist_list,
            plot_all     = False,
            cut_flow     = PreselMu2016.cut_flow+[['SR2', None]]
            )
    
    loop += ztautau.algs.algs.PlotAlg(
            region       = 'SR2El2015',
            do_var_check = True,
            hist_list    = hist_list,
            plot_all     = False,
            cut_flow     = PreselEl2015.cut_flow+[['SR2', None]]
            )
    
    loop += ztautau.algs.algs.PlotAlg(
            region       = 'SR2El2016',
            do_var_check = True,
            hist_list    = hist_list,
            plot_all     = False,
            cut_flow     = PreselEl2016.cut_flow+[['SR2', None]]
            )
    
    #######
    # SR3 #
    #######
    loop += ztautau.algs.algs.PlotAlg(
            region       = 'SR3Mu2015',
            do_var_check = True,
            hist_list    = hist_list,
            plot_all     = False,
            cut_flow     = PreselMu2015.cut_flow+[['SR3', None]]
            )
    
    loop += ztautau.algs.algs.PlotAlg(
            region       = 'SR3Mu2016',
            do_var_check = True,
            hist_list    = hist_list,
            plot_all     = False,
            cut_flow     = PreselMu2016.cut_flow+[['SR3', None]]
            )
    
    loop += ztautau.algs.algs.PlotAlg(
            region       = 'SR3El2015',
            do_var_check = True,
            hist_list    = hist_list,
            plot_all     = False,
            cut_flow     = PreselEl2015.cut_flow+[['SR3', None]]
            )
    
    loop += ztautau.algs.algs.PlotAlg(
            region       = 'SR3El2016',
            do_var_check = True,
            hist_list    = hist_list,
            plot_all     = False,
            cut_flow     = PreselEl2016.cut_flow+[['SR3', None]]
            )
    
    #######
    # TCR #
    #######
    loop += ztautau.algs.algs.PlotAlg(
            region       = 'TopCREl2016',
            do_var_check = True,
            hist_list    = hist_list,
            plot_all     = False,
            cut_flow  = [
                          ['ElecOnly'     , ['weight_total']] ,
                          ['2016ElecTrig' , ['ElTrig2016']] ,
                          ['OS'           , None] ,
                          ['LepPt'        , ['ElRecoTrk']] , 
                          ['LepQual'      , ['ElID']] ,
                          ['LepIso'       , ['ElIsoGrad']] ,
                          ['TauPt'        , ['TauReco']] , 
                          ['TauQual'      , None] , 
                          ['TauID'        , ['TauID']] , 
                          ['TauEVeto'     , ['TauEVeto']] , 
                          ['TCR'          , ['JetEff', 'JetIneff']] , 
                          ['SCDP'         , None] , 
                          ['dEta'         , None] , 
                        ],
            )
    loop += ztautau.algs.algs.PlotAlg(
            region       = 'TopCREl2015',
            do_var_check = True,
            hist_list    = hist_list,
            plot_all     = False,
            cut_flow  = [
                          ['ElecOnly'     , ['weight_total']] ,
                          ['2015ElecTrig' , ['ElTrig2015']] ,
                          ['OS'           , None] ,
                          ['LepPt'        , ['ElRecoTrk']] , 
                          ['LepQual'      , ['ElID']] ,
                          ['LepIso'       , ['ElIsoGrad']] ,
                          ['TauPt'        , ['TauReco']] , 
                          ['TauQual'      , None] , 
                          ['TauID'        , ['TauID']] , 
                          ['TauEVeto'     , ['TauEVeto']] , 
                          ['TCR'          , ['JetEff', 'JetIneff']] , 
                          ['SCDP'         , None] , 
                          ['dEta'         , None] , 
                        ],
            )
    loop += ztautau.algs.algs.PlotAlg(
            region       = 'TopCRMu2016',
            do_var_check = True,
            hist_list    = hist_list,
            plot_all     = False,
            cut_flow  = [
                          ['MuonOnly'     , ['weight_total']] ,
                          ['2016MuonTrig' , ['MuTrig2016']] ,
                          ['OS'           , None] ,
                          ['LepPt'        , ['MuTTVA']] , 
                          ['LepQual'      , ['MuRecoID']] ,
                          ['LepIso'       , ['MuIsoGrad']] ,
                          ['TauPt'        , ['TauReco']] , 
                          ['TauQual'      , None] , 
                          ['TauID'        , ['TauID']] , 
                          ['TauEVeto'     , ['TauEVeto']] , 
                          ['TCR'          , ['JetEff', 'JetIneff']] , 
                          ['SCDP'         , None] , 
                          ['dEta'         , None] , 
                        ],
            )
    loop += ztautau.algs.algs.PlotAlg(
            region       = 'TopCRMu2015',
            do_var_check = True,
            hist_list    = hist_list,
            plot_all     = False,
            cut_flow  = [
                          ['MuonOnly'     , ['weight_total']] ,
                          ['2015MuonTrig' , ['MuTrig2015']] ,
                          ['OS'           , None] ,
                          ['LepPt'        , ['MuTTVA']] , 
                          ['LepQual'      , ['MuRecoID']] ,
                          ['LepIso'       , ['MuIsoGrad']] ,
                          ['TauPt'        , ['TauReco']] , 
                          ['TauQual'      , None] , 
                          ['TauID'        , ['TauID']] , 
                          ['TauEVeto'     , ['TauEVeto']] , 
                          ['TCR'          , ['JetEff', 'JetIneff']] , 
                          ['SCDP'         , None] , 
                          ['dEta'         , None] , 
                        ],
            )
    #######
    # WCR #
    #######
    loop += ztautau.algs.algs.PlotAlg(
            region       = 'WCRMu2015',
            do_var_check = True,
            hist_list    = hist_list,
            plot_all     = False,
            cut_flow     = PreselMu2015.cut_flow+[['WCR', None]]
            )
    
    loop += ztautau.algs.algs.PlotAlg(
            region       = 'WCRMu2016',
            do_var_check = True,
            hist_list    = hist_list,
            plot_all     = False,
            cut_flow     = PreselMu2016.cut_flow+[['WCR', None]]
            )
    
    loop += ztautau.algs.algs.PlotAlg(
            region       = 'WCREl2015',
            do_var_check = True,
            hist_list    = hist_list,
            plot_all     = False,
            cut_flow     = PreselEl2015.cut_flow+[['WCR', None]]
            )
    
    loop += ztautau.algs.algs.PlotAlg(
            region       = 'WCREl2016',
            do_var_check = True,
            hist_list    = hist_list,
            plot_all     = False,
            cut_flow     = PreselEl2016.cut_flow+[['WCR', None]]
            )

    #########
    # QCDCR #
    #########
    loop += ztautau.algs.algs.PlotAlg(
            region       = 'QCDCREl2016',
            do_var_check = True,
            hist_list    = hist_list,
            plot_all     = False,
            cut_flow  = [
                          ['ElecOnly'     , ['weight_total']] ,
                          ['2016ElecTrig' , ['ElTrig2016']] ,
                          ['OS'           , None] ,
                          ['LepPt'        , ['ElRecoTrk']] , 
                          ['LepQual'      , ['ElID']] ,
                          ['LepIso'       , ['ElIsoGrad']] ,
                          ['TauPt'        , ['TauReco']] , 
                          ['TauQual'      , None] , 
                          ['TauID'        , ['TauID']] , 
                          ['TauEVeto'     , ['TauEVeto']] , 
                          ['BVeto'        , ['JetEff', 'JetIneff']] , 
                          ['SCDP'         , None] , 
                          ['QCDCR'        , None] , 
                        ],
            )
    loop += ztautau.algs.algs.PlotAlg(
            region       = 'QCDCREl2015',
            do_var_check = True,
            hist_list    = hist_list,
            plot_all     = False,
            cut_flow  = [
                          ['ElecOnly'     , ['weight_total']] ,
                          ['2015ElecTrig' , ['ElTrig2015']] ,
                          ['OS'           , None] ,
                          ['LepPt'        , ['ElRecoTrk']] , 
                          ['LepQual'      , ['ElID']] ,
                          ['LepIso'       , ['ElIsoGrad']] ,
                          ['TauPt'        , ['TauReco']] , 
                          ['TauQual'      , None] , 
                          ['TauID'        , ['TauID']] , 
                          ['TauEVeto'     , ['TauEVeto']] , 
                          ['BVeto'        , ['JetEff', 'JetIneff']] , 
                          ['SCDP'         , None] , 
                          ['QCDCR'        , None] , 
                        ],
            )
    loop += ztautau.algs.algs.PlotAlg(
            region       = 'QCDCRMu2016',
            do_var_check = True,
            hist_list    = hist_list,
            plot_all     = False,
            cut_flow  = [
                          ['MuonOnly'     , ['weight_total']] ,
                          ['2016MuonTrig' , ['MuTrig2016']] ,
                          ['OS'           , None] ,
                          ['LepPt'        , ['MuTTVA']] , 
                          ['LepQual'      , ['MuRecoID']] ,
                          ['LepIso'       , ['MuIsoGrad']] ,
                          ['TauPt'        , ['TauReco']] , 
                          ['TauQual'      , None] , 
                          ['TauID'        , ['TauID']] , 
                          ['TauEVeto'     , ['TauEVeto']] , 
                          ['BVeto'        , ['JetEff', 'JetIneff']] , 
                          ['SCDP'         , None] , 
                          ['QCDCR'        , None] , 
                        ],
            )
    loop += ztautau.algs.algs.PlotAlg(
            region       = 'QCDCRMu2015',
            do_var_check = True,
            hist_list    = hist_list,
            plot_all     = False,
            cut_flow  = [
                          ['MuonOnly'     , ['weight_total']] ,
                          ['2015MuonTrig' , ['MuTrig2015']] ,
                          ['OS'           , None] ,
                          ['LepPt'        , ['MuTTVA']] , 
                          ['LepQual'      , ['MuRecoID']] ,
                          ['LepIso'       , ['MuIsoGrad']] ,
                          ['TauPt'        , ['TauReco']] , 
                          ['TauQual'      , None] , 
                          ['TauID'        , ['TauID']] , 
                          ['TauEVeto'     , ['TauEVeto']] , 
                          ['BVeto'        , ['JetEff', 'JetIneff']] , 
                          ['SCDP'         , None] , 
                          ['QCDCR'        , None] , 
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



