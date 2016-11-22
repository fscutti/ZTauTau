#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
j.postprocessor.py
"""

from __future__ import division

## std modules
import os,re

## ROOT
import ROOT
ROOT.gROOT.SetBatch(True)

## my modules
import pyframe

## local modules
import ztautau



#GeV = 1000.0


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

    """
    IMPORTANT: no not really. This docstring is useless
    https://www.youtube.com/watch?v=sjJBpw5WNtU
    """

    sys_dict = None
    
    if   sys == None: sys_dict = get_sys_dict()
    
    # this is how you tell the weights 
    # what is the direction of the variation
    elif sys == 'MUSF_STAT_UP':     sys_dict = get_sys_dict(sys_name = sys, sys_var = "up")
    elif sys == 'MUSF_STAT_DN':     sys_dict = get_sys_dict(sys_name = sys, sys_var = "dn")
    elif sys == 'TAUSF_SYS_UP':     sys_dict = get_sys_dict(sys_name = sys, sys_var = "up") 
    elif sys == 'TAUSF_SYS_DN':     sys_dict = get_sys_dict(sys_name = sys, sys_var = "dn")
    elif sys == 'MUSF_SYS_UP':     sys_dict = get_sys_dict(sys_name = sys, sys_var = "up")
    elif sys == 'MUSF_SYS_DN':     sys_dict = get_sys_dict(sys_name = sys, sys_var = "dn")
    elif sys == 'PILEUP_DN':    sys_dict = get_sys_dict(sys_name = sys, sys_var = "dn")
    elif sys == 'PILEUP_UP':       sys_dict = get_sys_dict(sys_name = sys, sys_var = "up")
    elif sys == 'MUMS_UP': sys_dict = get_sys_dict(sys_name = sys, sys_tree = "MUONS_MS_1up", sys_var = "up")
    elif sys == 'MUMS_DN': sys_dict = get_sys_dict(sys_name = sys, sys_tree = "MUONS_MS_1down", sys_var = "dn")
    elif sys == 'MUSCALE_UP': sys_dict = get_sys_dict(sys_name = sys, sys_tree = "MUONS_SCALE_1up", sys_var = "up")
    elif sys == 'MUSCALE_DN': sys_dict = get_sys_dict(sys_name = sys, sys_tree = "MUONS_SCALE_1down", sys_var = "dn")
    elif sys == 'MUID_UP':    sys_dict = get_sys_dict(sys_name = sys, sys_tree = "MUONS_ID_1up", sys_var = "up")
    elif sys == 'MUID_DN':    sys_dict = get_sys_dict(sys_name = sys, sys_tree = "MUONS_ID_1down", sys_var = "dn")
    elif sys == 'METSCALE_UP':    sys_dict = get_sys_dict(sys_name = sys, sys_tree = "MET_SoftTrk_ScaleUp", sys_var = "up")
    elif sys == 'METSCALE_DN':    sys_dict = get_sys_dict(sys_name = sys, sys_tree = "MET_SoftTrk_ScaleDown", sys_var = "dn")
    elif sys == 'METResoPara':    sys_dict = get_sys_dict(sys_name = sys, sys_tree = "MET_SoftTrk_ResoPara", sys_var = "up")
    elif sys == 'METResoPerp':    sys_dict = get_sys_dict(sys_name = sys, sys_tree = "MET_SoftTrk_ResoPerp", sys_var = "dn")
    else: 
        assert False, "Invalid sys %s!"%(sys)
    
    ## build chain
    config['tree'] = sys_dict['tree']
    
    chain = ROOT.TChain(config['tree'])
    chain.SetCacheSize(0)
    for fn in config['input']: chain.Add(fn)


    ##-------------------------------------------------------------------------
    ## event loop
    ##-------------------------------------------------------------------------
    loop = pyframe.core.EventLoop(name='ztautau',
                                  sampletype=config['sampletype'],
                                  outfile='ntuple.root',
                                  quiet=False,
                                  )
    
    ## build and pt-sort objects
    ## ---------------------------------------
    #loop += pyframe.algs.ListBuilder(
    #    prefixes = ['lep_0_','tau_0_','jet_0_'],
    #    keys = ['muons','taus','jets'],
    #    )
    #loop += pyframe.algs.AttachTLVs(
    #    keys = ['muons','taus','jets'],
    #    )
    # just a decoration of particles ...
    #loop += ztautau.algs.vars.ParticlesBuilder(
    #    key='muons',
    #    )
    
    """
    ## build MET
    ## ---------------------------------------
    loop += ztautau.algs.met.METCLUS(
        prefix='metFinalClus',
        key = 'met_clus',
        )
    loop += ztautau.algs.met.METTRK(
        prefix='metFinalTrk',
        key = 'met_trk',
        )
   
    ## initialize and/or decorate objects
    ## ---------------------------------------
    loop += ztautau.algs.vars.PairsBuilder(
        obj_keys=['muons'],
        pair_key='mu_pairs',
        met_key='met_clus', 
        )
    """ 

    ## start preselection cutflow 
    ## ---------------------------------------
    loop += pyframe.algs.CutFlowAlg(key='presel')
    
    ## weights
    ## +++++++++++++++++++++++++++++++++++++++
    #loop += ztautau.algs.weights.MCEventWeight(cutflow='presel',key='weight_mc_event')
    loop += ztautau.algs.weights.JetsSF(cutflow='presel',key='jets_sf')
    loop += ztautau.algs.weights.Pileup(cutflow='presel',key='weight_pileup', sys_name=sys_dict['name'], scale=sys_dict['variation'])
    #loop += ztautau.algs.weights.WeightTotal(cutflow='presel',key='weight_total')
  
    ## cuts
    ## +++++++++++++++++++++++++++++++++++++++

    #---- BASE CUT ----#   

    loop += ztautau.algs.algs.CutAlg(cutflow='presel',cut='OneMuon')
    loop += ztautau.algs.algs.CutAlg(cutflow='presel',cut='NoElectrons')
    loop += ztautau.algs.algs.CutAlg(cutflow='presel',cut='AtLeastOneTau')
    loop += ztautau.algs.algs.CutAlg(cutflow='presel',cut='AtLeastOnePvx')
    #loop += ztautau.algs.algs.CutAlg(cutflow='presel',cut='NoBJets')
    #loop += ztautau.algs.algs.CutAlg(cutflow='presel',cut='MuonHLTmu20ilooseL1MU15ORmu40') #2015
    #loop += ztautau.algs.algs.CutAlg(cutflow='presel',cut='MuonHLTmu24imediumORHLTmu50') #2016

    #loop += ztautau.algs.algs.CutAlg(cutflow='presel',cut='MuonHLTmu20ilooseL1MU15ORmu40') #2015
    #loop += ztautau.algs.algs.CutAlg(cutflow='presel',cut='MuonHLTmu24imediumORHLTmu40')
    #loop += ztautau.algs.algs.CutAlg(cutflow='presel',cut='MuonHLTmu24imediumORHLTmu50') 
    #loop += ztautau.algs.algs.CutAlg(cutflow='presel',cut='MuonHLTmu26ivarmediumORHLTmu50') # v22 2016
    #loop += ztautau.algs.algs.CutAlg(cutflow='presel',cut='MuonMuTrigMatch0HLTmu20ilooseL1MU15')
    loop += ztautau.algs.algs.CutAlg(cutflow='presel',cut='MuonHLTmuOptions')
    #---- MUONS ----#

    loop += ztautau.algs.algs.CutAlg(cutflow='presel',cut='MuonIdMedium')
    #loop += ztautau.algs.algs.CutAlg(cutflow='presel',cut='MuonPt22') #2015
    #loop += ztautau.algs.algs.CutAlg(cutflow='presel',cut='MuonPt26') #2016
    loop += ztautau.algs.algs.CutAlg(cutflow='presel',cut='MuonEta25')
    #loop += ztautau.algs.algs.CutAlg(cutflow='presel',cut='MuonPt28') #2016
    loop += ztautau.algs.algs.CutAlg(cutflow='presel',cut='MuonPtOptions')
 
    #---- TAUS ----#

    loop += ztautau.algs.algs.CutAlg(cutflow='presel',cut='TauPt25')
    loop += ztautau.algs.algs.CutAlg(cutflow='presel',cut='TauEta247')
    loop += ztautau.algs.algs.CutAlg(cutflow='presel',cut='TauCharge1')
    loop += ztautau.algs.algs.CutAlg(cutflow='presel',cut='TauTrack')
    #loop += ztautau.algs.algs.CutAlg(cutflow='presel',cut='BDTtauLoose')
    loop += ztautau.algs.algs.CutAlg(cutflow='presel',cut='BDTtauMed')
    #loop += ztautau.algs.algs.CutAlg(cutflow='presel',cut='BDTtauTight')

    
    ## weights configuration
    ## ---------------------------------------
    ## event
    ## +++++++++++++++++++++++++++++++++++++++
    loop += ztautau.algs.weights.MuonSF(
        key='MuonTotalWeight',
        scale=sys_dict['variation'],
        sys_name=sys_dict['name'], #to pass entire dictionary
        )
    loop += ztautau.algs.weights.MuonSFIsoGrad(
        key='MuonWeightAI',
        scale=sys_dict['variation'],
        sys_name=sys_dict['name'],
        )
    loop += ztautau.algs.weights.TauSF(
        key='TauTotalWeight',
        scale=sys_dict['variation'],
        sys_name=sys_dict['name'],
        )
   
    """
    loop += ztautau.algs.EvWeights.MuTrigSF(
            is_di_mu = True,
            mu_trig_level="Loose_Loose",
            mu_trig_chain="HLT_2mu10",
            key='DiMuonTrigSF',
            scale=None,
            )
    """ 
    ## objects
    ## +++++++++++++++++++++++++++++++++++++++
    """
    loop += ztautau.algs.ObjWeights.MuAllSF(
            #mu_level="Tight",
            mu_index=0,
            key='MuLeadAllSF',
            scale=None,
            )
    loop += ztautau.algs.ObjWeights.MuAllSF(
            #mu_level="NotTight",
            mu_index=1,
            key='MuSubLeadAllSF',
            scale=None,
            )
    """ 
    ##-------------------------------------------------------------------------
    ## make plots
    ##-------------------------------------------------------------------------
    #triggers = [160]
    #trigchains = [] 

    triggers = [25,35,"50L1TAU12", 80, "80L1TAU60", 125, 160, "L1TAU12IM"]
    trigchains = ["tracktwo", "ptonly"]
    trax = [1,3]

    #---------------------#
    #    NO TRIG
    #---------------------#

        
    loop += ztautau.algs.algs.PlotAlg(
            region    = 'SR_OS_no_cuts',
            plot_all  = False,
            cut_flow  = [
                ['OS',None],
                ],
              )

    loop += ztautau.algs.algs.PlotAlg(
            region    = 'SR_SS_no_cuts',
            plot_all  = False,
            cut_flow  = [
              ['SS',None],
              ],
            )

    loop += ztautau.algs.algs.PlotAlg(
            region    = 'SR_OS_no_cuts_for2D',
            plot_all  = False,
            cut_flow  = [
              ['OS',None],
              ['VisMass4580',None],
              ['MuonGradIso',["MuonTotalWeight"]],
              ],
            )

    loop += ztautau.algs.algs.PlotAlg(
            region    = 'SR_SS_no_cuts_2D',
            plot_all  = False,
            cut_flow  = [
              ['SS',None],
              ['VisMass4580',None],
              ['MuonGradIso',["MuonTotalWeight"]],
              ],
            )


    loop += ztautau.algs.algs.PlotAlg(
            region    = 'SR_OS_no_cuts_forvismass',
            plot_all  = False,
            cut_flow  = [
              ['OS',None],
              ['MuonGradIso',["MuonTotalWeight"]],
              ['MTrans50',None],
              ['SumCosDPhi05',None],
              ],
            )

    loop += ztautau.algs.algs.PlotAlg(
            region    = 'SR_SS_no_cuts_forvismass',
            plot_all  = False,
            cut_flow  = [
              ['SS',None],
              ['MuonGradIso',["MuonTotalWeight"]],
              ['MTrans50',None],
              ['SumCosDPhi05',None],
              ],
            )


    loop += ztautau.algs.algs.PlotAlg(
            region    = 'SR_no_cuts',
            plot_all  = False,
            cut_flow  = [
              ['TauPt25',None],
              ],
            )

#-----------------------------#
#       THREE TRACK TAU
#-----------------------------#
        
    loop += ztautau.algs.algs.PlotAlg(
            region    = 'SR_Tau3Track',
            plot_all  = False,
            cut_flow  = [
              ['MTrans50',None],
              ['SumCosDPhi05',None],
              ['MuonGradIso',["MuonTotalWeight"]],
              ['VisMass4580',None],
              ['OS',None],
              ['Tau3Track',["TauTotalWeight"]],
              ],
            )

    loop += ztautau.algs.algs.PlotAlg(
            region    = 'SR_SS_Tau3Track',
            plot_all  = False,
            cut_flow  = [
              ['MTrans50',None],
              ['SumCosDPhi05',None],
              ['MuonGradIso',["MuonTotalWeight"]],
              ['VisMass4580',None],
              ['SS',None],
              ['Tau3Track',["TauTotalWeight"]],
              ],
            )

    loop += ztautau.algs.algs.PlotAlg(
            region    = 'AntiIsoCR_OS_Tau3Track',
            plot_all  = False,
            cut_flow  = [
              ['MTrans50',None],
              ['InvMuonGradIso',["MuonWeightAI"]],
              ['SumCosDPhi05',None],
              ['OS',None],
              ['Tau3Track',["TauTotalWeight"]],
              ],
            )


    loop += ztautau.algs.algs.PlotAlg(
            region    = 'AntiIsoCR_SS_Tau3Track',
            plot_all  = False,
            cut_flow  = [
              ['MTrans50',None],
              ['InvMuonGradIso',["MuonWeightAI"]],
              ['SumCosDPhi05',None],
              ['SS',None],
              ['Tau3Track',["TauTotalWeight"]],
              ],
            )


    loop += ztautau.algs.algs.PlotAlg(
            region    = 'Wjets_OS_Tau3Track',
            plot_all  = False,
            cut_flow  = [
              ['MTrans60',None],
              ['MET30',None],
              ['OS',None],
              ['MuonGradIso',["MuonTotalWeight"]],
              ['Tau3Track',["TauTotalWeight"]],
              ],
            )


    loop += ztautau.algs.algs.PlotAlg(
            region    = 'Wjets_SS_Tau3Track',
            plot_all  = False,
            cut_flow  = [
              ['MTrans60',None],
              ['MET30',None],
              ['SS',None],
              ['MuonGradIso',["MuonTotalWeight"]],
              ['Tau3Track',["TauTotalWeight"]],
              ],
            )

    loop += ztautau.algs.algs.PlotAlg(
            region    = 'Wjets_OS_highPT_Tau3Track',
            plot_all  = False,
            cut_flow  = [
              ['MTrans60',None],
              ['MET30',None],
              ['OS',None],
              ['MuonGradIso',["MuonTotalWeight"]],
              ['TauHighPt',None],
              ['Tau3Track',["TauTotalWeight"]],
              ],
            )
    
    loop += ztautau.algs.algs.PlotAlg(
            region    = 'Wjets_OS_lowPT_Tau3Track',
            plot_all  = False,
            cut_flow  = [
              ['MTrans60',None],
              ['MET30',None],
              ['OS',None],
              ['MuonGradIso',["MuonTotalWeight"]],
              ['TauLowPt',None],
              ['Tau3Track',["TauTotalWeight"]],
              ],
            )


    loop += ztautau.algs.algs.PlotAlg(
            region    = 'Wjets_SS_highPT_Tau3Track',
            plot_all  = False,
            cut_flow  = [
              ['MTrans60',None],
              ['MET30',None],
              ['SS',None],
              ['MuonGradIso',["MuonTotalWeight"]],
              ['TauHighPt',None],
              ['Tau3Track',["TauTotalWeight"]],
              ],
            )

    loop += ztautau.algs.algs.PlotAlg(
            region    = 'Wjets_SS_lowPT_Tau3Track',
            plot_all  = False,
            cut_flow  = [
              ['MTrans60',None],
              ['MET30',None],
              ['SS',None],
              ['MuonGradIso',["MuonTotalWeight"]],
              ['TauLowPt',None],
              ['Tau3Track',["TauTotalWeight"]],
              ],
            )
    loop += ztautau.algs.algs.PlotAlg(
            region    = 'SR_highPT_Tau3Track',
            plot_all  = False,
            cut_flow  = [
              ['MTrans50',None],
              ['SumCosDPhi05',None],
              ['MuonGradIso',["MuonTotalWeight"]],
              ['VisMass4580',None],
              ['OS',None],
              ['Tau3Track',["TauTotalWeight"]],
              ['TauHighPt',None],
              ],
            )

    loop += ztautau.algs.algs.PlotAlg(
            region    = 'SR_lowPT_Tau3Track',
            plot_all  = False,
            cut_flow  = [
              ['MTrans50',None],
              ['SumCosDPhi05',None],
              ['MuonGradIso',["MuonTotalWeight"]],
              ['VisMass4580',None],
              ['OS',None],
              ['TauLowPt',None],
              ['Tau3Track',["TauTotalWeight"]],
              ],
            )

    loop += ztautau.algs.algs.PlotAlg(
            region    = 'SR_SS_highPT_Tau3Track',
            plot_all  = False,
            cut_flow  = [
              ['MTrans50',None],
              ['SumCosDPhi05',None],
              ['MuonGradIso',["MuonTotalWeight"]],
              ['VisMass4580',None],
              ['SS',None],
              ['Tau3Track',["TauTotalWeight"]],
              ['TauHighPt',None],
              ],
            )

    loop += ztautau.algs.algs.PlotAlg(
            region    = 'SR_SS_lowPT_Tau3Track',
            plot_all  = False,
            cut_flow  = [
              ['MTrans50',None],
              ['SumCosDPhi05',None],
              ['MuonGradIso',["MuonTotalWeight"]],
              ['VisMass4580',None],
              ['SS',None],
              ['TauLowPt',None],
              ['Tau3Track',["TauTotalWeight"]],
              ],
            )

    loop += ztautau.algs.algs.PlotAlg(
            region    = 'AntiIsoCR_OS_highPT_Tau3Track',
            plot_all  = False,
            cut_flow  = [
              ['MTrans50',None],
              ['InvMuonGradIso',["MuonWeightAI"]],
              ['SumCosDPhi05',None],
              ['OS',None],
              ['TauHighPt',None],
              ['Tau3Track',["TauTotalWeight"]],
              ],
            )

    loop += ztautau.algs.algs.PlotAlg(
            region    = 'AntiIsoCR_OS_lowPT_Tau3Track',
            plot_all  = False,
            cut_flow  = [
              ['MTrans50',None],
              ['InvMuonGradIso',["MuonWeightAI"]],
              ['SumCosDPhi05',None],
              ['OS',None],
              ['TauLowPt',None],
              ['Tau3Track',["TauTotalWeight"]],
              ],
            )

    loop += ztautau.algs.algs.PlotAlg(
            region    = 'AntiIsoCR_SS_highPT_Tau3Track',
            plot_all  = False,
            cut_flow  = [
              ['MTrans50',None],
              ['InvMuonGradIso',["MuonWeightAI"]],
              ['SumCosDPhi05',None],
              ['SS',None],
              ['TauHighPt',None],
              ['Tau3Track',["TauTotalWeight"]],
              ],
            )

    loop += ztautau.algs.algs.PlotAlg(
            region    = 'AntiIsoCR_SS_lowPT_Tau3Track',
            plot_all  = False,
            cut_flow  = [
              ['MTrans50',None],
              ['InvMuonGradIso',["MuonWeightAI"]],
              ['SumCosDPhi05',None],
              ['SS',None],
              ['TauLowPt',None],
              ['Tau3Track',["TauTotalWeight"]],
              ],
            )


#-----------------------------#
#    ONE TRACK TAU
#-----------------------------#
    

    loop += ztautau.algs.algs.PlotAlg(
            region    = 'Wjets_OS_Tau1Track',
            plot_all  = False,
            cut_flow  = [
              ['MTrans60',None],
              ['MET30',None],
              ['OS',None],
              ['MuonGradIso',["MuonTotalWeight"]],
              ['Tau1Track',["TauTotalWeight"]],
              ],
            )


    loop += ztautau.algs.algs.PlotAlg(
            region    = 'Wjets_SS_Tau1Track',
            plot_all  = False,
            cut_flow  = [
              ['MTrans60',None],
              ['MET30',None],
              ['SS',None],
              ['MuonGradIso',["MuonTotalWeight"]],
              ['Tau1Track',["TauTotalWeight"]],
              ],
            )

    loop += ztautau.algs.algs.PlotAlg(
            region    = 'SR_Tau1Track',
            plot_all  = False,
            cut_flow  = [
              ['MTrans50',None],
              ['SumCosDPhi05',None],
              ['MuonGradIso',["MuonTotalWeight"]],
              ['VisMass4580',None],
              ['OS',None],
              ['Tau1Track',["TauTotalWeight"]],
              ],
            )

    loop += ztautau.algs.algs.PlotAlg(
            region    = 'SR_SS_Tau1Track',
            plot_all  = False,
            cut_flow  = [
              ['MTrans50',None],
              ['SumCosDPhi05',None],
              ['MuonGradIso',["MuonTotalWeight"]],
              ['VisMass4580',None],
              ['SS',None],
              ['Tau1Track',["TauTotalWeight"]],
              ],
            )

    loop += ztautau.algs.algs.PlotAlg(
            region    = 'AntiIsoCR_OS_Tau1Track',
            plot_all  = False,
            cut_flow  = [
              ['MTrans50',None],
              ['InvMuonGradIso',["MuonWeightAI"]],
              ['SumCosDPhi05',None],
              ['OS',None],
              ['Tau1Track',["TauTotalWeight"]],
              ],
            )

    loop += ztautau.algs.algs.PlotAlg(
            region    = 'AntiIsoCR_SS_Tau1Track',
            plot_all  = False,
            cut_flow  = [
              ['MTrans50',None],
              ['InvMuonGradIso',["MuonWeightAI"]],
              ['SumCosDPhi05',None],
              ['SS',None],
              ['Tau1Track',["TauTotalWeight"]],
              ],
            )




   
    loop += ztautau.algs.algs.PlotAlg(
            region    = 'Wjets_OS_highPT_Tau1Track',
            plot_all  = False,
            cut_flow  = [
              ['MTrans60',None],
              ['MET30',None],
              ['OS',None],
              ['MuonGradIso',["MuonTotalWeight"]],
              ['TauHighPt',None],
              ['Tau1Track',["TauTotalWeight"]],
              ],
            )

    loop += ztautau.algs.algs.PlotAlg(
            region    = 'Wjets_OS_lowPT_Tau1Track',
            plot_all  = False,
            cut_flow  = [
              ['MTrans60',None],
              ['MET30',None],
              ['OS',None],
              ['MuonGradIso',["MuonTotalWeight"]],
              ['TauLowPt',None],
              ['Tau1Track',["TauTotalWeight"]],
              ],
            )
    loop += ztautau.algs.algs.PlotAlg(
            region    = 'Wjets_SS_highPT_Tau1Track',
            plot_all  = False,
            cut_flow  = [
              ['MTrans60',None],
              ['MET30',None],
              ['SS',None],
              ['MuonGradIso',["MuonTotalWeight"]],
              ['TauHighPt',None],
              ['Tau1Track',["TauTotalWeight"]],
              ],
            )

    loop += ztautau.algs.algs.PlotAlg(
            region    = 'Wjets_SS_lowPT_Tau1Track',
            plot_all  = False,
            cut_flow  = [
              ['MTrans60',None],
              ['MET30',None],
              ['SS',None],
              ['MuonGradIso',["MuonTotalWeight"]],
              ['TauLowPt',None],
              ['Tau1Track',["TauTotalWeight"]],
              ],
            )
    loop += ztautau.algs.algs.PlotAlg(
            region    = 'SR_highPT_Tau1Track',
            plot_all  = False,
            cut_flow  = [
              ['MTrans50',None],
              ['SumCosDPhi05',None],
              ['MuonGradIso',["MuonTotalWeight"]],
              ['VisMass4580',None],
              ['OS',None],
              ['Tau1Track',["TauTotalWeight"]],
              ['TauHighPt',None],
              ],
            )

    loop += ztautau.algs.algs.PlotAlg(
            region    = 'SR_lowPT_Tau1Track',
            plot_all  = False,
            cut_flow  = [
              ['MTrans50',None],
              ['SumCosDPhi05',None],
              ['MuonGradIso',["MuonTotalWeight"]],
              ['VisMass4580',None],
              ['OS',None],
              ['TauLowPt',None],
              ['Tau1Track',["TauTotalWeight"]],
              ],
            )
    loop += ztautau.algs.algs.PlotAlg(
            region    = 'SR_SS_highPT_Tau1Track',
            plot_all  = False,
            cut_flow  = [
              ['MTrans50',None],
              ['SumCosDPhi05',None],
              ['MuonGradIso',["MuonTotalWeight"]],
              ['VisMass4580',None],
              ['SS',None],
              ['Tau1Track',["TauTotalWeight"]],
              ['TauHighPt',None],
              ],
            )

    loop += ztautau.algs.algs.PlotAlg(
            region    = 'SR_SS_lowPT_Tau1Track',
            plot_all  = False,
            cut_flow  = [
              ['MTrans50',None],
              ['SumCosDPhi05',None],
              ['MuonGradIso',["MuonTotalWeight"]],
              ['VisMass4580',None],
              ['SS',None],
              ['TauLowPt',None],
              ['Tau1Track',["TauTotalWeight"]],
              ],
            )

    loop += ztautau.algs.algs.PlotAlg(
            region    = 'AntiIsoCR_OS_highPT_Tau1Track',
            plot_all  = False,
            cut_flow  = [
              ['MTrans50',None],
              ['InvMuonGradIso',["MuonWeightAI"]],
              ['SumCosDPhi05',None],
              ['OS',None],
              ['TauHighPt',None],
              ['Tau1Track',["TauTotalWeight"]],
              ],
            )

    loop += ztautau.algs.algs.PlotAlg(
            region    = 'AntiIsoCR_OS_lowPT_Tau1Track',
            plot_all  = False,
            cut_flow  = [
              ['MTrans50',None],
              ['InvMuonGradIso',["MuonWeightAI"]],
              ['SumCosDPhi05',None],
              ['OS',None],
              ['TauLowPt',None],
              ['Tau1Track',["TauTotalWeight"]],
              ],
            )

    loop += ztautau.algs.algs.PlotAlg(
            region    = 'AntiIsoCR_SS_highPT_Tau1Track',
            plot_all  = False,
            cut_flow  = [
              ['MTrans50',None],
              ['InvMuonGradIso',["MuonWeightAI"]],
              ['SumCosDPhi05',None],
              ['SS',None],
              ['TauHighPt',None],
              ['Tau1Track',["TauTotalWeight"]],
              ],
            )

    loop += ztautau.algs.algs.PlotAlg(
            region    = 'AntiIsoCR_SS_lowPT_Tau1Track',
            plot_all  = False,
            cut_flow  = [
              ['MTrans50',None],
              ['InvMuonGradIso',["MuonWeightAI"]],
              ['SumCosDPhi05',None],
              ['SS',None],
              ['TauLowPt',None],
              ['Tau1Track',["TauTotalWeight"]],
              ],
            )
    
#-----------------------------#
#       INCLUSIVE
#-----------------------------#
    

    loop += ztautau.algs.algs.PlotAlg(
            region    = 'Wjets_OS',
            plot_all  = False,
            cut_flow  = [
              ['MTrans60',None],
              ['MET30',None],
              ['OS',None],
              ['MuonGradIso',["MuonTotalWeight"]],
              ],
            )
    loop += ztautau.algs.algs.PlotAlg(
            region    = 'Wjets_SS',
            plot_all  = False,
            cut_flow  = [
              ['MTrans60',None],
              ['MET30',None],
              ['SS',None],
              ['MuonGradIso',["MuonTotalWeight"]],
              ],
            )

    loop += ztautau.algs.algs.PlotAlg(
            region    = 'SR',
            plot_all  = False,
            cut_flow  = [
              ['MTrans50',None],
              ['SumCosDPhi05',None],
              ['MuonGradIso',["MuonTotalWeight"]],
              ['VisMass4580',None],
              ['OS',None],
              ],
            )

    loop += ztautau.algs.algs.PlotAlg(
            region    = 'SR_SS',
            plot_all  = False,
            cut_flow  = [
              ['MTrans50',None],
              ['SumCosDPhi05',None],
              ['MuonGradIso',["MuonTotalWeight"]],
              ['VisMass4580',None],
              ['SS',None],
              ],
            )

    loop += ztautau.algs.algs.PlotAlg(
            region    = 'AntiIsoCR_OS',
            plot_all  = False,
            cut_flow  = [
              ['MTrans50',None],
              ['SumCosDPhi05',None],
              ['OS',None],
              ['InvMuonGradIso',["MuonWeightAI"]],
              ],
            )

    loop += ztautau.algs.algs.PlotAlg(
            region    = 'AntiIsoCR_SS',
            plot_all  = False,
            cut_flow  = [
              ['MTrans50',None],
              ['SumCosDPhi05',None],
              ['SS',None],
              ['InvMuonGradIso',["MuonWeightAI"]],
              ],
            )

      
    loop += ztautau.algs.algs.PlotAlg(
            region    = 'Wjets_OS_highPT',
            plot_all  = False,
            cut_flow  = [
              ['MTrans60',None],
              ['MET30',None],
              ['OS',None],
              ['MuonGradIso',["MuonTotalWeight"]],
              ['TauHighPt',["TauTotalWeight"]],
              ],
            )
    loop += ztautau.algs.algs.PlotAlg(
            region    = 'Wjets_OS_lowPT',
            plot_all  = False,
            cut_flow  = [
              ['MTrans60',None],
              ['MET30',None],
              ['OS',None],
              ['MuonGradIso',["MuonTotalWeight"]],
              ['TauLowPt',["TauTotalWeight"]],
              ],
            )

    loop += ztautau.algs.algs.PlotAlg(
            region    = 'Wjets_SS_highPT',
            plot_all  = False,
            cut_flow  = [
              ['MTrans60',None],
              ['MET30',None],
              ['SS',None],
              ['MuonGradIso',["MuonTotalWeight"]],
              ['TauHighPt',None],
              ],
            )

    loop += ztautau.algs.algs.PlotAlg(
            region    = 'Wjets_SS_lowPT',
            plot_all  = False,
            cut_flow  = [
              ['MTrans60',None],
              ['MET30',None],
              ['SS',None],
              ['MuonGradIso',["MuonTotalWeight"]],
              ['TauLowPt',["TauTotalWeight"]],
              ],
            )
    loop += ztautau.algs.algs.PlotAlg(
            region    = 'SR_highPT',
            plot_all  = False,
            cut_flow  = [
              ['MTrans50',None],
              ['SumCosDPhi05',None],
              ['MuonGradIso',["MuonTotalWeight"]],
              ['VisMass4580',None],
              ['OS',None],
              ['TauHighPt',["TauTotalWeight"]],
              ],
            )

    loop += ztautau.algs.algs.PlotAlg(
            region    = 'SR_lowPT',
            plot_all  = False,
            cut_flow  = [
              ['MTrans50',None],
              ['SumCosDPhi05',None],
              ['MuonGradIso',["MuonTotalWeight"]],
              ['VisMass4580',None],
              ['OS',None],
              ['TauLowPt',["TauTotalWeight"]],
              ],
            )

    loop += ztautau.algs.algs.PlotAlg(
            region    = 'SR_SS_highPT',
            plot_all  = False,
            cut_flow  = [
              ['MTrans50',None],
              ['SumCosDPhi05',None],
              ['MuonGradIso',["MuonTotalWeight"]],
              ['VisMass4580',None],
              ['SS',None],
              ['TauHighPt',["TauTotalWeight"]],
              ],
            )

    loop += ztautau.algs.algs.PlotAlg(
            region    = 'SR_SS_lowPT',
            plot_all  = False,
            cut_flow  = [
              ['MTrans50',None],
              ['SumCosDPhi05',None],
              ['MuonGradIso',["MuonTotalWeight"]],
              ['VisMass4580',None],
              ['SS',None],
              ['TauLowPt',["TauTotalWeight"]],
              ],
            )

    loop += ztautau.algs.algs.PlotAlg(
            region    = 'AntiIsoCR_OS_highPT',
            plot_all  = False,
            cut_flow  = [
              ['MTrans50',None],
              ['SumCosDPhi05',None],
              ['OS',None],
              ['TauHighPt',["TauTotalWeight"]],
              ['InvMuonGradIso',["MuonWeightAI"]],
              ],
            )

    loop += ztautau.algs.algs.PlotAlg(
            region    = 'AntiIsoCR_OS_lowPT',
            plot_all  = False,
            cut_flow  = [
              ['MTrans50',None],
              ['SumCosDPhi05',None],
              ['OS',None],
              ['TauLowPt',["TauTotalWeight"]],
              ['InvMuonGradIso',["MuonWeightAI"]],
              ],
            )
    loop += ztautau.algs.algs.PlotAlg(
            region    = 'AntiIsoCR_SS_highPT',
            plot_all  = False,
            cut_flow  = [
              ['MTrans50',None],
              ['SumCosDPhi05',None],
              ['SS',None],
              ['TauHighPt',["TauTotalWeight"]],
              ['InvMuonGradIso',["MuonWeightAI"]],
              ],
            )

    loop += ztautau.algs.algs.PlotAlg(
            region    = 'AntiIsoCR_SS_lowPT',
            plot_all  = False,
            cut_flow  = [
              ['MTrans50',None],
              ['SumCosDPhi05',None],
              ['SS',None],
              ['TauLowPt',["TauTotalWeight"]],
              ['InvMuonGradIso',["MuonWeightAI"]],
              ],
            )
 
    loop += ztautau.algs.algs.PlotAlg(
            region    = 'SR_highSCDP_nomtcut',
            plot_all  = False,
            cut_flow  = [
              ['SumCosDPhi05',None],
              ['MuonGradIso',["MuonTotalWeight"]],
              ['VisMass4580',None],
              ['OS',None],
              ],
            )

    loop += ztautau.algs.algs.PlotAlg(
            region    = 'SR_lowSCDP_nomtcut',
            plot_all  = False,
            cut_flow  = [
              ['SumCosDPhi06',None],
              ['MuonGradIso',["MuonTotalWeight"]],
              ['VisMass4580',None],
              ['OS',None],
              ],
            )

    loop += ztautau.algs.algs.PlotAlg(
            region    = 'SR_lowSCDP_nomtcut_forvismass',
            plot_all  = False,
            cut_flow  = [
              ['SumCosDPhi06',None],
              ['MuonGradIso',["MuonTotalWeight"]],
              ['TauPt25',None],
              ['OS',None],
              ],
            )

    loop += ztautau.algs.algs.PlotAlg(
            region    = 'SR_SS_highSCDP_nomtcut',
            plot_all  = False,
            cut_flow  = [
              ['SumCosDPhi05',None],
              ['MuonGradIso',["MuonTotalWeight"]],
              ['VisMass4580',None],
              ['SS',None],
              ],
            )

    loop += ztautau.algs.algs.PlotAlg(
            region    = 'SR_SS_lowSCDP_nomtcut_forvismass',
            plot_all  = False,
            cut_flow  = [
              ['SumCosDPhi06',None],
              ['MuonGradIso',["MuonTotalWeight"]],
              ['TauPt25',None],
              ['SS',None],
              ],
            )


    loop += ztautau.algs.algs.PlotAlg(
            region    = 'SR_SS_lowSCDP_nomtcut',
            plot_all  = False,
            cut_flow  = [
              ['SumCosDPhi06',None],
              ['MuonGradIso',["MuonTotalWeight"]],
              ['VisMass4580',None],
              ['SS',None],
              ],
            )

    loop += ztautau.algs.algs.PlotAlg(
            region    = 'SR_highSCDP',
            plot_all  = False,
            cut_flow  = [
              ['SumCosDPhi05',None],
              ['MuonGradIso',["MuonTotalWeight"]],
              ['VisMass4580',None],
              ['TauPt25',None],
              ['OS',None],
              ],
            )

    loop += ztautau.algs.algs.PlotAlg(
            region    = 'SR_lowSCDP',
            plot_all  = False,
            cut_flow  = [
              ['SumCosDPhi06',None],
              ['MuonGradIso',["MuonTotalWeight"]],
              ['VisMass4580',None],
              ['TauPt25',None],             
              ['OS',None],
              ],
            )

    loop += ztautau.algs.algs.PlotAlg(
            region    = 'SR_SS_highSCDP',
            plot_all  = False,
            cut_flow  = [
              ['SumCosDPhi05',None],
              ['MuonGradIso',["MuonTotalWeight"]],
              ['VisMass4580',None],
              ['SS',None],
              ['TauPt25',None],
              ],
            )

    loop += ztautau.algs.algs.PlotAlg(
            region    = 'SR_SS_lowSCDP',
            plot_all  = False,
            cut_flow  = [
              ['SumCosDPhi06',None],
              ['MuonGradIso',["MuonTotalWeight"]],
              ['VisMass4580',None],
              ['SS',None],
              ['TauPt25',None],
              ],
            )


###########################################################################
    # HIGH SCDP ALL MT

    loop += ztautau.algs.algs.PlotAlg(
            region    = 'SR_OS_no_cuts_highSCDP',
            plot_all  = False,
            cut_flow  = [
              ['MuonGradIso',["MuonTotalWeight"]],
              ['SumCosDPhi05',None],
              ['OS',None],
              ],
            )

    loop += ztautau.algs.algs.PlotAlg(
            region    = 'SR_SS_no_cuts_highSCDPT',
            plot_all  = False,
            cut_flow  = [
              ['MuonGradIso',["MuonTotalWeight"]],
              ['SumCosDPhi05',None],
              ['MTrans50',None],
              ['SS',None],
              ],
            )


    loop += ztautau.algs.algs.PlotAlg(
            region    = 'SR_highSCDP_Tau1Track',
            plot_all  = False,
            cut_flow  = [
              ['SumCosDPhi05',None],
              ['MuonGradIso',["MuonTotalWeight"]],
              ['VisMass4580',None],
              ['TauPt25',None],
              ['OS',None],
              ['Tau1Track',["TauTotalWeight"]],
              ],
            )

    loop += ztautau.algs.algs.PlotAlg(
            region    = 'SR_highSCDP_highPT_Tau1Track',
            plot_all  = False,
            cut_flow  = [
              ['SumCosDPhi05',None],
              ['MuonGradIso',["MuonTotalWeight"]],
              ['VisMass4580',None],
              ['OS',None],
              ['TauPt25',None],
              ['Tau1Track',["TauTotalWeight"]],
              ['TauHighPt',None],
              ],
            )

    loop += ztautau.algs.algs.PlotAlg(
            region    = 'SR_highSCDP_lowPT_Tau1Track',
            plot_all  = False,
            cut_flow  = [
              ['SumCosDPhi05',None],
              ['MuonGradIso',["MuonTotalWeight"]],
              ['VisMass4580',None],
              ['OS',None],
              ['TauPt25',None],
              ['TauLowPt',None],
              ['Tau1Track',["TauTotalWeight"]],
              ],
            )

    loop += ztautau.algs.algs.PlotAlg(
            region    = 'SR_highSCDP_SS_Tau1Track',
            plot_all  = False,
            cut_flow  = [
              ['SumCosDPhi05',None],
              ['MuonGradIso',["MuonTotalWeight"]],
              ['VisMass4580',None],
              ['TauPt25',None],
              ['SS',None],
              ['Tau1Track',["TauTotalWeight"]],
              ],
            )

    loop += ztautau.algs.algs.PlotAlg(
            region    = 'SR_highSCDP_SS_highPT_Tau1Track',
            plot_all  = False,
            cut_flow  = [
              ['TauPt25',None],
              ['SumCosDPhi05',None],
              ['MuonGradIso',["MuonTotalWeight"]],
              ['VisMass4580',None],
              ['SS',None],
              ['Tau1Track',["TauTotalWeight"]],
              ['TauHighPt',None],
              ],
            )

    loop += ztautau.algs.algs.PlotAlg(
            region    = 'SR_highSCDP_SS_lowPT_Tau1Track',
            plot_all  = False,
            cut_flow  = [
              ['SumCosDPhi05',None],
              ['TauPt25',None],             
              ['MuonGradIso',["MuonTotalWeight"]],
              ['VisMass4580',None],
              ['SS',None],
              ['TauLowPt',None],
              ['Tau1Track',["TauTotalWeight"]],
              ],
            )

    loop += ztautau.algs.algs.PlotAlg(
            region    = 'SR_highSCDP_Tau3Track',
            plot_all  = False,
            cut_flow  = [
              ['SumCosDPhi05',None],
              ['MuonGradIso',["MuonTotalWeight"]],
              ['VisMass4580',None],
              ['OS',None],
              ['TauPt25',None],
              ['Tau3Track',["TauTotalWeight"]],
              ],
            )

    loop += ztautau.algs.algs.PlotAlg(
            region    = 'SR_highSCDP_highPT_Tau3Track',
            plot_all  = False,
            cut_flow  = [
              ['TauPt25',None],
              ['SumCosDPhi05',None],
              ['MuonGradIso',["MuonTotalWeight"]],
              ['VisMass4580',None],
              ['OS',None],
              ['Tau3Track',["TauTotalWeight"]],
              ['TauHighPt',None],
              ],
            )

    loop += ztautau.algs.algs.PlotAlg(
            region    = 'SR_highSCDP_lowPT_Tau3Track',
            plot_all  = False,
            cut_flow  = [
              ['TauPt25',None],
              ['SumCosDPhi05',None],
              ['MuonGradIso',["MuonTotalWeight"]],
              ['VisMass4580',None],
              ['OS',None],
              ['TauLowPt',None],
              ['Tau3Track',["TauTotalWeight"]],
              ],
            )

    loop += ztautau.algs.algs.PlotAlg(
            region    = 'SR_highSCDP_SS_Tau3Track',
            plot_all  = False,
            cut_flow  = [
              ['SumCosDPhi05',None],
              ['MuonGradIso',["MuonTotalWeight"]],
              ['VisMass4580',None],
              ['SS',None],
              ['TauPt25',None],
              ['Tau3Track',["TauTotalWeight"]],
              ],
            )

    loop += ztautau.algs.algs.PlotAlg(
            region    = 'SR_highSCDP_SS_highPT_Tau3Track',
            plot_all  = False,
            cut_flow  = [
              ['SumCosDPhi05',None],
              ['MuonGradIso',["MuonTotalWeight"]],
              ['VisMass4580',None],
              ['SS',None],
              ['TauPt25',None],
              ['Tau3Track',["TauTotalWeight"]],
              ['TauHighPt',None],
              ],
            )

    loop += ztautau.algs.algs.PlotAlg(
            region    = 'SR_highSCDP_SS_lowPT_Tau3Track',
            plot_all  = False,
            cut_flow  = [
              ['SumCosDPhi05',None],
              ['MuonGradIso',["MuonTotalWeight"]],
              ['VisMass4580',None],
              ['SS',None],
              ['TauPt25',None],
              ['TauLowPt',None],
              ['Tau3Track',["TauTotalWeight"]],
              ],
            )

    loop += ztautau.algs.algs.PlotAlg(
            region    = 'SR_highSCDP_highMT',
            plot_all  = False,
            cut_flow  = [
              ['SumCosDPhi05',None],
              ['MuonGradIso',["MuonTotalWeight"]],
              ['VisMass4580',None],
              ['OS',None],
              ['TauPt25',None],
              ],
            )

    loop += ztautau.algs.algs.PlotAlg(
            region    = 'SR_highSCDP_highPT',
            plot_all  = False,
            cut_flow  = [
              ['SumCosDPhi05',None],
              ['MuonGradIso',["MuonTotalWeight"]],
              ['VisMass4580',None],
              ['OS',None],
              ['TauPt25',None],
              ['TauHighPt',["TauTotalWeight"]],
              ],
            )

    loop += ztautau.algs.algs.PlotAlg(
            region    = 'SR_highSCDP_lowPT',
            plot_all  = False,
            cut_flow  = [
              ['SumCosDPhi05',None],
              ['TauPt25',None],
              ['MuonGradIso',["MuonTotalWeight"]],
              ['VisMass4580',None],
              ['OS',None],
              ['TauLowPt',["TauTotalWeight"]],
              ],
            )

    loop += ztautau.algs.algs.PlotAlg(
            region    = 'SR_highSCDP_SS',
            plot_all  = False,
            cut_flow  = [
              ['SumCosDPhi05',None],
              ['TauPt25',None],
              ['MuonGradIso',["MuonTotalWeight"]],
              ['VisMass4580',None],
              ['SS',None],
              ],
            )


    loop += ztautau.algs.algs.PlotAlg(
            region    = 'SR_highSCDP_SS_highPT',
            plot_all  = False,
            cut_flow  = [
              ['SumCosDPhi05',None],
              ['TauPt25',None],
              ['MuonGradIso',["MuonTotalWeight"]],
              ['VisMass4580',None],
              ['SS',None],
              ['TauHighPt',["TauTotalWeight"]],
              ],
            )

    loop += ztautau.algs.algs.PlotAlg(
            region    = 'SR_highSCDP_SS_lowPT',
            plot_all  = False,
            cut_flow  = [
              ['TauPt25',None],
              ['SumCosDPhi05',None],
              ['MuonGradIso',["MuonTotalWeight"]],
              ['VisMass4580',None],
              ['SS',None],
              ['TauLowPt',["TauTotalWeight"]],
              ],
            )


#############################################################

    # LOW SCDP ALL MT

    loop += ztautau.algs.algs.PlotAlg(
            region    = 'SR_OS_no_cuts_lowSCDP',
            plot_all  = False,
            cut_flow  = [
              ['MuonGradIso',["MuonTotalWeight"]],
              ['SumCosDPhi06',None],
              ['OS',None],
              ],
            )

    loop += ztautau.algs.algs.PlotAlg(
            region    = 'SR_SS_no_cuts_lowSCDPT',
            plot_all  = False,
            cut_flow  = [
              ['MuonGradIso',["MuonTotalWeight"]],
              ['SumCosDPhi06',None],
              ['MTrans50',None],
              ['SS',None],
              ],
            )

    loop += ztautau.algs.algs.PlotAlg(
            region    = 'SR_lowSCDP_Tau1Track',
            plot_all  = False,
            cut_flow  = [
              ['SumCosDPhi06',None],
              ['MuonGradIso',["MuonTotalWeight"]],
              ['VisMass4580',None],
              ['OS',None],
              ['TauPt25',None],
              ['Tau1Track',["TauTotalWeight"]],
              ],
            )

    loop += ztautau.algs.algs.PlotAlg(
            region    = 'SR_lowSCDP_highPT_Tau1Track',
            plot_all  = False,
            cut_flow  = [
              ['SumCosDPhi06',None],
              ['MuonGradIso',["MuonTotalWeight"]],
              ['VisMass4580',None],
              ['OS',None],
              ['TauPt25',None],
              ['Tau1Track',["TauTotalWeight"]],
              ['TauHighPt',None],
              ],
            )

    loop += ztautau.algs.algs.PlotAlg(
            region    = 'SR_lowSCDP_lowPT_Tau1Track',
            plot_all  = False,
            cut_flow  = [
              ['SumCosDPhi06',None],
              ['MuonGradIso',["MuonTotalWeight"]],
              ['VisMass4580',None],
              ['OS',None],
              ['TauPt25',None],
              ['TauLowPt',None],
              ['Tau1Track',["TauTotalWeight"]],
              ],
            )

    loop += ztautau.algs.algs.PlotAlg(
            region    = 'SR_lowSCDP_SS_Tau1Track',
            plot_all  = False,
            cut_flow  = [
              ['SumCosDPhi06',None],
              ['MuonGradIso',["MuonTotalWeight"]],
              ['VisMass4580',None],
              ['SS',None],
              ['TauPt25',None],
              ['Tau1Track',["TauTotalWeight"]],
              ],
            )

    loop += ztautau.algs.algs.PlotAlg(
            region    = 'SR_lowSCDP_SS_highPT_Tau1Track',
            plot_all  = False,
            cut_flow  = [
              ['SumCosDPhi06',None],
              ['MuonGradIso',["MuonTotalWeight"]],
              ['VisMass4580',None],
              ['SS',None],
              ['TauPt25',None],
              ['Tau1Track',["TauTotalWeight"]],
              ['TauHighPt',None],
              ],
            )


    loop += ztautau.algs.algs.PlotAlg(
            region    = 'SR_lowSCDP_SS_lowPT_Tau1Track',
            plot_all  = False,
            cut_flow  = [
              ['SumCosDPhi06',None],
              ['TauPt25',None],
              ['MuonGradIso',["MuonTotalWeight"]],
              ['VisMass4580',None],
              ['SS',None],
              ['Tau1Track',["TauTotalWeight"]],
              ['TauLowPt',None],
              ],
            )


    loop += ztautau.algs.algs.PlotAlg(
            region    = 'SR_lowSCDP_Tau3Track',
            plot_all  = False,
            cut_flow  = [
              ['TauPt25',None],
              ['SumCosDPhi06',None],
              ['MuonGradIso',["MuonTotalWeight"]],
              ['VisMass4580',None],
              ['OS',None],
              ['Tau3Track',["TauTotalWeight"]],
              ],
            )

    loop += ztautau.algs.algs.PlotAlg(
            region    = 'SR_lowSCDP_highPT_Tau3Track',
            plot_all  = False,
            cut_flow  = [
              ['TauPt25',None],
              ['SumCosDPhi06',None],
              ['MuonGradIso',["MuonTotalWeight"]],
              ['VisMass4580',None],
              ['OS',None],
              ['Tau3Track',["TauTotalWeight"]],
              ['TauHighPt',None],
              ],
            )

    loop += ztautau.algs.algs.PlotAlg(
            region    = 'SR_lowSCDP_lowPT_Tau3Track',
            plot_all  = False,
            cut_flow  = [
              ['TauPt25',None],
              ['SumCosDPhi06',None],
              ['MuonGradIso',["MuonTotalWeight"]],
              ['VisMass4580',None],
              ['OS',None],
              ['TauLowPt',None],
              ['Tau3Track',["TauTotalWeight"]],
              ],
            )

    loop += ztautau.algs.algs.PlotAlg(
            region    = 'SR_lowSCDP_SS_Tau3Track',
            plot_all  = False,
            cut_flow  = [
              ['TauPt25',None],
              ['SumCosDPhi06',None],
              ['MuonGradIso',["MuonTotalWeight"]],
              ['VisMass4580',None],
              ['SS',None],
              ['Tau3Track',["TauTotalWeight"]],
              ],
            )

    loop += ztautau.algs.algs.PlotAlg(
            region    = 'SR_lowSCDP_SS_highPT_Tau3Track',
            plot_all  = False,
            cut_flow  = [
              ['TauPt25',None],
              ['SumCosDPhi06',None],
              ['MuonGradIso',["MuonTotalWeight"]],
              ['VisMass4580',None],
              ['SS',None],
              ['Tau3Track',["TauTotalWeight"]],
              ['TauHighPt',None],
              ],
            )

    loop += ztautau.algs.algs.PlotAlg(
            region    = 'SR_lowSCDP_SS_lowPT_Tau3Track',
            plot_all  = False,
            cut_flow  = [
              ['TauPt25',None],
              ['SumCosDPhi06',None],
              ['MuonGradIso',["MuonTotalWeight"]],
              ['VisMass4580',None],
              ['SS',None],
              ['TauLowPt',None],
              ['Tau3Track',["TauTotalWeight"]],
              ],
            )

    loop += ztautau.algs.algs.PlotAlg(
            region    = 'SR_lowSCDP_lowMT',
            plot_all  = False,
            cut_flow  = [
              ['TauPt25',None],
              ['SumCosDPhi06',None],
              ['MuonGradIso',["MuonTotalWeight"]],
              ['VisMass4580',None],
              ['OS',None],
              ],
            )

    loop += ztautau.algs.algs.PlotAlg(
            region    = 'SR_lowSCDP_highPT',
            plot_all  = False,
            cut_flow  = [
              ['TauPt25',None],
              ['SumCosDPhi06',None],
              ['MuonGradIso',["MuonTotalWeight"]],
              ['VisMass4580',None],
              ['OS',None],
              ['TauHighPt',["TauTotalWeight"]],
              ],
            )

    loop += ztautau.algs.algs.PlotAlg(
            region    = 'SR_lowSCDP_lowPT',
            plot_all  = False,
            cut_flow  = [
              ['TauPt25',None],
              ['SumCosDPhi06',None],
              ['MuonGradIso',["MuonTotalWeight"]],
              ['VisMass4580',None],
              ['OS',None],
              ['TauLowPt',["TauTotalWeight"]],
              ],
            )

    loop += ztautau.algs.algs.PlotAlg(
            region    = 'SR_lowSCDP_SS',
            plot_all  = False,
            cut_flow  = [
              ['TauPt25',None],
              ['SumCosDPhi06',None],
              ['MuonGradIso',["MuonTotalWeight"]],
              ['VisMass4580',None],
              ['SS',None],
              ],
            )

    loop += ztautau.algs.algs.PlotAlg(
            region    = 'SR_lowSCDP_SS_highPT',
            plot_all  = False,
            cut_flow  = [
              ['TauPt25',None],
              ['SumCosDPhi06',None],
              ['MuonGradIso',["MuonTotalWeight"]],
              ['VisMass4580',None],
              ['SS',None],
              ['TauHighPt',["TauTotalWeight"]],
              ],
            )

    loop += ztautau.algs.algs.PlotAlg(
            region    = 'SR_lowSCDP_SS_lowPT',
            plot_all  = False,
            cut_flow  = [
              ['TauPt25',None],
              ['SumCosDPhi06',None],
              ['MuonGradIso',["MuonTotalWeight"]],
              ['VisMass4580',None],
              ['SS',None],
              ['TauLowPt',["TauTotalWeight"]],
              ],
            )


   
############ TRIGGERS
    

    
    for i in range(len(triggers)):
        loop += ztautau.algs.algs.PlotAlg(
                region    = 'Wjets_OS_'+str(triggers[i])+'med',
                plot_all  = False,
                cut_flow  = [
                  ['MTrans60',None],
                  ['MET30',None],
                  ['OS',None],
                  ['MuonGradIso',["MuonTotalWeight"]],
                  ['HLTTau'+str(triggers[i])+'Med1TrackTwo',None],
                  ],
                ) 


        loop += ztautau.algs.algs.PlotAlg(
                region    = 'Wjets_SS_'+str(triggers[i])+'med',
                plot_all  = False,
                cut_flow  = [
                  ['MTrans60',None],
                  ['MET30',None],
                  ['SS',None],
                  ['MuonGradIso',["MuonTotalWeight"]],
                  ['HLTTau'+str(triggers[i])+'Med1TrackTwo',None],
                  ],
                ) 

        loop += ztautau.algs.algs.PlotAlg(
                region    = 'SR_'+str(triggers[i])+'med',
                plot_all  = False,
                cut_flow  = [
                  ['MTrans50',None],
                  ['SumCosDPhi05',None],
                  ['MuonGradIso',["MuonTotalWeight"]],
                  ['VisMass4580',None],
                  ['OS',None],
                  ['HLTTau'+str(triggers[i])+'Med1TrackTwo',None],
                  ],
                )

        loop += ztautau.algs.algs.PlotAlg(
                region    = 'SR_SS'+str(triggers[i])+'med',
                plot_all  = False,
                cut_flow  = [
                  ['MTrans50',None],
                  ['SumCosDPhi05',None],
                  ['MuonGradIso',["MuonTotalWeight"]],
                  ['VisMass4580',None],
                  ['SS',None],
                  ['HLTTau'+str(triggers[i])+'Med1TrackTwo',None],
                  ],
                )

        loop += ztautau.algs.algs.PlotAlg(
                region    = 'AntiIsoCR_OS_'+str(triggers[i])+'med',
                plot_all  = False,
                cut_flow  = [
                  ['MTrans50',None],
                  ['InvMuonGradIso',["MuonWeightAI"]],
                  ['SumCosDPhi05',None],
                  ['OS',None],
                  ['HLTTau'+str(triggers[i])+'Med1TrackTwo',None],
                  ],
                )

        loop += ztautau.algs.algs.PlotAlg(
                region    = 'AntiIsoCR_SS_'+str(triggers[i])+'med',
                plot_all  = False,
                cut_flow  = [
                  ['MTrans50',None],
                  ['InvMuonGradIso',["MuonWeightAI"]],
                  ['SumCosDPhi05',None],
                  ['SS',None],
                  ['HLTTau'+str(triggers[i])+'Med1TrackTwo',None],
                  ],
                )

        loop += ztautau.algs.algs.PlotAlg(
                region    = 'Wjets_OS_'+str(triggers[i])+'med_lowPT',
                plot_all  = False,
                cut_flow  = [
                  ['MTrans60',None],
                  ['MET30',None],
                  ['OS',None],
                  ['MuonGradIso',["MuonTotalWeight"]],
                  ['HLTTau'+str(triggers[i])+'Med1TrackTwo',None],
                  ['TauLowPt',None],
                  ],
                )

        loop += ztautau.algs.algs.PlotAlg(
                region    = 'Wjets_OS_'+str(triggers[i])+'med_highPT',
                plot_all  = False,
                cut_flow  = [
                  ['MTrans60',None],
                  ['MET30',None],
                  ['OS',None],
                  ['MuonGradIso',["MuonTotalWeight"]],
                  ['HLTTau'+str(triggers[i])+'Med1TrackTwo',None],
                  ['TauHighPt',None],
                  ],
                )

        loop += ztautau.algs.algs.PlotAlg(
                region    = 'Wjets_SS_'+str(triggers[i])+'med_lowPT',
                plot_all  = False,
                cut_flow  = [
                  ['MTrans60',None],
                  ['MET30',None],
                  ['SS',None],
                  ['MuonGradIso',["MuonTotalWeight"]],
                  ['HLTTau'+str(triggers[i])+'Med1TrackTwo',None],
                  ['TauLowPt',None],
                  ],
                )

        loop += ztautau.algs.algs.PlotAlg(
                region    = 'Wjets_SS_'+str(triggers[i])+'med_highPT',
                plot_all  = False,
                cut_flow  = [
                  ['MTrans60',None],
                  ['MET30',None],
                  ['SS',None],
                  ['MuonGradIso',["MuonTotalWeight"]],
                  ['HLTTau'+str(triggers[i])+'Med1TrackTwo',None],
                  ['TauHighPt',None],
                  ],
                )

        loop += ztautau.algs.algs.PlotAlg(
                region    = 'SR_'+str(triggers[i])+'med_lowPT',
                plot_all  = False,
                cut_flow  = [
                  ['MTrans50',None],
                  ['SumCosDPhi05',None],
                  ['MuonGradIso',["MuonTotalWeight"]],
                  ['VisMass4580',None],
                  ['OS',None],
                  ['HLTTau'+str(triggers[i])+'Med1TrackTwo',None],
                  ['TauLowPt',None],
                  ],
                )

        loop += ztautau.algs.algs.PlotAlg(
                region    = 'SR_'+str(triggers[i])+'med_highPT',
                plot_all  = False,
                cut_flow  = [
                  ['MTrans50',None],
                  ['SumCosDPhi05',None],
                  ['MuonGradIso',["MuonTotalWeight"]],
                  ['VisMass4580',None],
                  ['OS',None],
                  ['HLTTau'+str(triggers[i])+'Med1TrackTwo',None],
                  ['TauHighPt',None],
                  ],
                )

        loop += ztautau.algs.algs.PlotAlg(
                region    = 'SR_SS'+str(triggers[i])+'med_lowPT',
                plot_all  = False,
                cut_flow  = [
                  ['MTrans50',None],
                  ['SumCosDPhi05',None],
                  ['MuonGradIso',["MuonTotalWeight"]],
                  ['VisMass4580',None],
                  ['SS',None],
                  ['HLTTau'+str(triggers[i])+'Med1TrackTwo',None],
                  ['TauLowPt',None],
                  ],
                )

        loop += ztautau.algs.algs.PlotAlg(
                region    = 'SR_SS'+str(triggers[i])+'med_highPT',
                plot_all  = False,
                cut_flow  = [
                  ['MTrans50',None],
                  ['SumCosDPhi05',None],
                  ['MuonGradIso',["MuonTotalWeight"]],
                  ['VisMass4580',None],
                  ['SS',None],
                  ['HLTTau'+str(triggers[i])+'Med1TrackTwo',None],
                  ['TauHighPt',None],
                  ],
                )

        loop += ztautau.algs.algs.PlotAlg(
                region    = 'AntiIsoCR_OS_'+str(triggers[i])+'med_lowPT',
                plot_all  = False,
                cut_flow  = [
                  ['MTrans50',None],
                  ['InvMuonGradIso',["MuonWeightAI"]],
                  ['SumCosDPhi05',None],
                  ['OS',None],
                  ['HLTTau'+str(triggers[i])+'Med1TrackTwo',None],
                  ['TauLowPt',None],
                  ],
                )

        loop += ztautau.algs.algs.PlotAlg(
                region    = 'AntiIsoCR_OS_'+str(triggers[i])+'med_highPT',
                plot_all  = False,
                cut_flow  = [
                  ['MTrans50',None],
                  ['InvMuonGradIso',["MuonWeightAI"]],
                  ['SumCosDPhi05',None],
                  ['OS',None],
                  ['HLTTau'+str(triggers[i])+'Med1TrackTwo',None],
                  ['TauHighPt',None],
                  ],
                )

        loop += ztautau.algs.algs.PlotAlg(
                region    = 'AntiIsoCR_SS_'+str(triggers[i])+'med_lowPT',
                plot_all  = False,
                cut_flow  = [
                  ['MTrans50',None],
                  ['InvMuonGradIso',["MuonWeightAI"]],
                  ['SumCosDPhi05',None],
                  ['SS',None],
                  ['HLTTau'+str(triggers[i])+'Med1TrackTwo',None],
                  ['TauLowPt',None],
                  ],
                )

        loop += ztautau.algs.algs.PlotAlg(
                region    = 'AntiIsoCR_SS_'+str(triggers[i])+'med_highPT',
                plot_all  = False,
                cut_flow  = [
                  ['MTrans50',None],
                  ['InvMuonGradIso',["MuonWeightAI"]],
                  ['SumCosDPhi05',None],
                  ['SS',None],
                  ['HLTTau'+str(triggers[i])+'Med1TrackTwo',None],
                  ['TauHighPt',None],
                  ],
                )

        loop += ztautau.algs.algs.PlotAlg(
                region    = 'SR_highSCDP_'+str(triggers[i])+'med',
                plot_all  = False,
                cut_flow  = [
                  ['SumCosDPhi05',None],
                  ['MuonGradIso',["MuonTotalWeight"]],
                  ['VisMass4580',None],
                  ['TauPt25',None],
                  ['OS',None],
                  ['HLTTau'+str(triggers[i])+'Med1TrackTwo',None],
                  ],
                )

        loop += ztautau.algs.algs.PlotAlg(
                region    = 'SR_highSCDP_'+str(triggers[i])+'med_lowPT',
                plot_all  = False,
                cut_flow  = [
                  ['TauPt25',None],        
                  ['SumCosDPhi05',None],
                  ['MuonGradIso',["MuonTotalWeight"]],
                  ['VisMass4580',None],
                  ['OS',None],
                  ['HLTTau'+str(triggers[i])+'Med1TrackTwo',None],
                  ['TauLowPt',None],
                  ],
                )

        loop += ztautau.algs.algs.PlotAlg(
                region    = 'SR_highSCDP_'+str(triggers[i])+'med_highPT',
                plot_all  = False,
                cut_flow  = [
                  ['SumCosDPhi05',None],
                  ['TauPt25',None],
                  ['MuonGradIso',["MuonTotalWeight"]],
                  ['VisMass4580',None],
                  ['OS',None],
                  ['HLTTau'+str(triggers[i])+'Med1TrackTwo',None],
                  ['TauHighPt',None],
                  ],
                )

        loop += ztautau.algs.algs.PlotAlg(
                region    = 'SR_highSCDP_SS'+str(triggers[i])+'med',
                plot_all  = False,
                cut_flow  = [
                  ['TauPt25',None],
                  ['SumCosDPhi05',None],
                  ['MuonGradIso',["MuonTotalWeight"]],
                  ['VisMass4580',None],
                  ['SS',None],
                  ['HLTTau'+str(triggers[i])+'Med1TrackTwo',None],
                  ],
                )

        loop += ztautau.algs.algs.PlotAlg(
                region    = 'SR_highSCDP_SS'+str(triggers[i])+'med_lowPT',
                plot_all  = False,
                cut_flow  = [
                  ['SumCosDPhi05',None],
                  ['MuonGradIso',["MuonTotalWeight"]],
                  ['VisMass4580',None],
                  ['SS',None],
                  ['TauPt25',None],
                  ['HLTTau'+str(triggers[i])+'Med1TrackTwo',None],
                  ['TauLowPt',None],
                  ],
                )

        loop += ztautau.algs.algs.PlotAlg(
        region    = 'SR_highSCDP_SS'+str(triggers[i])+'med_highPT',
        plot_all  = False,
        cut_flow  = [
          ['SumCosDPhi05',None],
          ['MuonGradIso',["MuonTotalWeight"]],
          ['VisMass4580',None],
          ['SS',None],
          ['TauPt25',None],
          ['HLTTau'+str(triggers[i])+'Med1TrackTwo',None],
          ['TauHighPt',None],
          ],
          )
  
        loop += ztautau.algs.algs.PlotAlg(
        region    = 'SR_lowSCDP_'+str(triggers[i])+'med',
        plot_all  = False,
        cut_flow  = [
          ['TauPt25',None],
          ['SumCosDPhi06',None],
          ['MuonGradIso',["MuonTotalWeight"]],
          ['VisMass4580',None],
          ['OS',None],
          ['HLTTau'+str(triggers[i])+'Med1TrackTwo',None],
          ],
          )

        loop += ztautau.algs.algs.PlotAlg(
        region    = 'SR_lowSCDP_'+str(triggers[i])+'med_lowPT',
        plot_all  = False,
        cut_flow  = [
          ['TauPt25',None],
          ['SumCosDPhi06',None],
          ['MuonGradIso',["MuonTotalWeight"]],
          ['VisMass4580',None],
          ['OS',None],
          ['HLTTau'+str(triggers[i])+'Med1TrackTwo',None],
          ['TauLowPt',None],
          ],
          )

        loop += ztautau.algs.algs.PlotAlg(
        region    = 'SR_lowSCDP_'+str(triggers[i])+'med_highPT',
        plot_all  = False,
        cut_flow  = [
          ['TauPt25',None],
          ['SumCosDPhi06',None],
          ['MuonGradIso',["MuonTotalWeight"]],
          ['VisMass4580',None],
          ['OS',None],
          ['HLTTau'+str(triggers[i])+'Med1TrackTwo',None],
          ['TauHighPt',None],
          ],
          )

        loop += ztautau.algs.algs.PlotAlg(
        region    = 'SR_lowSCDP_SS'+str(triggers[i])+'med',
        plot_all  = False,
        cut_flow  = [
          ['TauPt25',None],
          ['SumCosDPhi06',None],
          ['MuonGradIso',["MuonTotalWeight"]],
          ['VisMass4580',None],
          ['SS',None],
          ['HLTTau'+str(triggers[i])+'Med1TrackTwo',None],
          ],
          )


        loop += ztautau.algs.algs.PlotAlg(
        region    = 'SR_lowSCDP_SS'+str(triggers[i])+'med_lowPT',
        plot_all  = False,
        cut_flow  = [
          ['TauPt25',None],
          ['SumCosDPhi06',None],
          ['MuonGradIso',["MuonTotalWeight"]],
          ['VisMass4580',None],
          ['SS',None],
          ['HLTTau'+str(triggers[i])+'Med1TrackTwo',None],
          ['TauLowPt',None],
          ],
          )

        loop += ztautau.algs.algs.PlotAlg(
        region    = 'SR_lowSCDP_SS'+str(triggers[i])+'med_highPT',
        plot_all  = False,
        cut_flow  = [
          ['TauPt25',None],
          ['SumCosDPhi06',None],
          ['MuonGradIso',["MuonTotalWeight"]],
          ['VisMass4580',None],
          ['SS',None],
          ['HLTTau'+str(triggers[i])+'Med1TrackTwo',None],
          ['TauHighPt',None],
          ],
          )

 
        for j in range(len(trax)):

            loop += ztautau.algs.algs.PlotAlg(
            region    = 'Wjets_OS_'+str(triggers[i])+'med_Tau'+str(trax[j])+'Track',
            plot_all  = False,
            cut_flow  = [
              ['MTrans60',None],
              ['MET30',None],
              ['OS',None],
              ['MuonGradIso',["MuonTotalWeight"]],
              ['HLTTau'+str(triggers[i])+'Med1TrackTwo',None],
              ['Tau'+str(trax[j])+'Track',["TauTotalWeight"]],
              ],
            ) 

            loop += ztautau.algs.algs.PlotAlg(
            region    = 'Wjets_OS_'+str(triggers[i])+'med_lowPT_Tau'+str(trax[j])+'Track',
            plot_all  = False,
            cut_flow  = [
              ['MTrans60',None],
              ['MET30',None],
              ['OS',None],
              ['MuonGradIso',["MuonTotalWeight"]],
              ['HLTTau'+str(triggers[i])+'Med1TrackTwo',None],
              ['Tau'+str(trax[j])+'Track',["TauTotalWeight"]],
              ['TauLowPt',None],
              ],
              )

            loop += ztautau.algs.algs.PlotAlg(
            region    = 'Wjets_OS_'+str(triggers[i])+'med_highPT_Tau'+str(trax[j])+'Track',
            plot_all  = False,
            cut_flow  = [
              ['MTrans60',None],
              ['MET30',None],
              ['OS',None],
              ['MuonGradIso',["MuonTotalWeight"]],
              ['HLTTau'+str(triggers[i])+'Med1TrackTwo',None],
              ['Tau'+str(trax[j])+'Track',["TauTotalWeight"]],
              ['TauHighPt',None],
              ],
              )

            loop += ztautau.algs.algs.PlotAlg(
            region    = 'Wjets_SS_'+str(triggers[i])+'med_Tau'+str(trax[j])+'Track',
            plot_all  = False,
            cut_flow  = [
              ['MTrans60',None],
              ['MET30',None],
              ['SS',None],
              ['MuonGradIso',["MuonTotalWeight"]],
              ['HLTTau'+str(triggers[i])+'Med1TrackTwo',None],
              ['Tau'+str(trax[j])+'Track',["TauTotalWeight"]],
              ],
            ) 

            loop += ztautau.algs.algs.PlotAlg(
            region    = 'Wjets_SS_'+str(triggers[i])+'med_lowPT_Tau'+str(trax[j])+'Track',
            plot_all  = False,
            cut_flow  = [
              ['MTrans60',None],
              ['MET30',None],
              ['SS',None],
              ['MuonGradIso',["MuonTotalWeight"]],
              ['HLTTau'+str(triggers[i])+'Med1TrackTwo',None],
              ['Tau'+str(trax[j])+'Track',["TauTotalWeight"]],
              ['TauLowPt',None],
              ],
              )

            loop += ztautau.algs.algs.PlotAlg(
            region    = 'Wjets_SS_'+str(triggers[i])+'med_highPT_Tau'+str(trax[j])+'Track',
            plot_all  = False,
            cut_flow  = [
              ['MTrans60',None],
              ['MET30',None],
              ['SS',None],
              ['MuonGradIso',["MuonTotalWeight"]],
              ['HLTTau'+str(triggers[i])+'Med1TrackTwo',None],
              ['Tau'+str(trax[j])+'Track',["TauTotalWeight"]],
              ['TauHighPt',None],
              ],
              )

            loop += ztautau.algs.algs.PlotAlg(
            region    = 'SR_'+str(triggers[i])+'med_Tau'+str(trax[j])+'Track',
            plot_all  = False,
            cut_flow  = [
              ['MTrans50',None],
              ['SumCosDPhi05',None],
              ['MuonGradIso',["MuonTotalWeight"]],
              ['VisMass4580',None],
              ['OS',None],
              ['HLTTau'+str(triggers[i])+'Med1TrackTwo',None],
              ['Tau'+str(trax[j])+'Track',["TauTotalWeight"]],
              ],
              )

            loop += ztautau.algs.algs.PlotAlg(
            region    = 'SR_'+str(triggers[i])+'med_lowPT_Tau'+str(trax[j])+'Track',
            plot_all  = False,
            cut_flow  = [
              ['MTrans50',None],
              ['SumCosDPhi05',None],
              ['MuonGradIso',["MuonTotalWeight"]],
              ['VisMass4580',None],
              ['OS',None],
              ['HLTTau'+str(triggers[i])+'Med1TrackTwo',None],
              ['Tau'+str(trax[j])+'Track',["TauTotalWeight"]],
              ['TauLowPt',None],
              ],
              )

            loop += ztautau.algs.algs.PlotAlg(
            region    = 'SR_'+str(triggers[i])+'med_highPT_Tau'+str(trax[j])+'Track',
            plot_all  = False,
            cut_flow  = [
              ['MTrans50',None],
              ['SumCosDPhi05',None],
              ['MuonGradIso',["MuonTotalWeight"]],
              ['VisMass4580',None],
              ['OS',None],
              ['HLTTau'+str(triggers[i])+'Med1TrackTwo',None],
              ['Tau'+str(trax[j])+'Track',["TauTotalWeight"]],
              ['TauHighPt',None],
              ],
              )

            loop += ztautau.algs.algs.PlotAlg(
            region    = 'SR_SS'+str(triggers[i])+'med_Tau'+str(trax[j])+'Track',
            plot_all  = False,
            cut_flow  = [
              ['MTrans50',None],
              ['SumCosDPhi05',None],
              ['MuonGradIso',["MuonTotalWeight"]],
              ['VisMass4580',None],
              ['SS',None],
              ['HLTTau'+str(triggers[i])+'Med1TrackTwo',None],
              ['Tau'+str(trax[j])+'Track',["TauTotalWeight"]],
              ],
              )

            loop += ztautau.algs.algs.PlotAlg(
            region    = 'SR_SS'+str(triggers[i])+'med_lowPT_Tau'+str(trax[j])+'Track',
            plot_all  = False,
            cut_flow  = [
              ['MTrans50',None],
              ['SumCosDPhi05',None],
              ['MuonGradIso',["MuonTotalWeight"]],
              ['VisMass4580',None],
              ['SS',None],
              ['HLTTau'+str(triggers[i])+'Med1TrackTwo',None],
              ['Tau'+str(trax[j])+'Track',["TauTotalWeight"]],
              ['TauLowPt',None],
              ],
              )

            loop += ztautau.algs.algs.PlotAlg(
            region    = 'SR_SS'+str(triggers[i])+'med_highPT_Tau'+str(trax[j])+'Track',
            plot_all  = False,
            cut_flow  = [
              ['MTrans50',None],
              ['SumCosDPhi05',None],
              ['MuonGradIso',["MuonTotalWeight"]],
              ['VisMass4580',None],
              ['SS',None],
              ['HLTTau'+str(triggers[i])+'Med1TrackTwo',None],
              ['Tau'+str(trax[j])+'Track',["TauTotalWeight"]],
              ['TauHighPt',None],
              ],
              )

            loop += ztautau.algs.algs.PlotAlg(
            region    = 'AntiIsoCR_OS_'+str(triggers[i])+'med_Tau'+str(trax[j])+'Track',
            plot_all  = False,
            cut_flow  = [
              ['MTrans50',None],
              ['InvMuonGradIso',["MuonWeightAI"]],
              ['SumCosDPhi05',None],
              ['OS',None],
              ['HLTTau'+str(triggers[i])+'Med1TrackTwo',None],
              ['Tau'+str(trax[j])+'Track',["TauTotalWeight"]],
              ],
              )

            loop += ztautau.algs.algs.PlotAlg(
            region    = 'AntiIsoCR_OS_'+str(triggers[i])+'med_lowPT_Tau'+str(trax[j])+'Track',
            plot_all  = False,
            cut_flow  = [
              ['MTrans50',None],
              ['InvMuonGradIso',["MuonWeightAI"]],
              ['SumCosDPhi05',None],
              ['OS',None],
              ['HLTTau'+str(triggers[i])+'Med1TrackTwo',None],
              ['Tau'+str(trax[j])+'Track',["TauTotalWeight"]],
              ['TauLowPt',None],
              ],
              )

            loop += ztautau.algs.algs.PlotAlg(
            region    = 'AntiIsoCR_OS_'+str(triggers[i])+'med_highPT_Tau'+str(trax[j])+'Track',
            plot_all  = False,
            cut_flow  = [
              ['MTrans50',None],
              ['InvMuonGradIso',["MuonWeightAI"]],
              ['SumCosDPhi05',None],
              ['OS',None],
              ['HLTTau'+str(triggers[i])+'Med1TrackTwo',None],
              ['Tau'+str(trax[j])+'Track',["TauTotalWeight"]],
              ['TauHighPt',None],
              ],
              )
            loop += ztautau.algs.algs.PlotAlg(
            region    = 'AntiIsoCR_SS_'+str(triggers[i])+'med_Tau'+str(trax[j])+'Track',
            plot_all  = False,
            cut_flow  = [
              ['MTrans50',None],
              ['InvMuonGradIso',["MuonWeightAI"]],
              ['SumCosDPhi05',None],
              ['SS',None],
              ['HLTTau'+str(triggers[i])+'Med1TrackTwo',None],
              ['Tau'+str(trax[j])+'Track',["TauTotalWeight"]],
              ],
              )

            loop += ztautau.algs.algs.PlotAlg(
            region    = 'AntiIsoCR_SS_'+str(triggers[i])+'med_lowPT_Tau'+str(trax[j])+'Track',
            plot_all  = False,
            cut_flow  = [
              ['MTrans50',None],
              ['InvMuonGradIso',["MuonWeightAI"]],
              ['SumCosDPhi05',None],
              ['SS',None],
              ['HLTTau'+str(triggers[i])+'Med1TrackTwo',None],
              ['Tau'+str(trax[j])+'Track',["TauTotalWeight"]],
              ['TauLowPt',None],
              ],
              )

            loop += ztautau.algs.algs.PlotAlg(
            region    = 'AntiIsoCR_SS_'+str(triggers[i])+'med_highPT_Tau'+str(trax[j])+'Track',
            plot_all  = False,
            cut_flow  = [
              ['MTrans50',None],
              ['InvMuonGradIso',["MuonWeightAI"]],
              ['SumCosDPhi05',None],
              ['SS',None],
              ['HLTTau'+str(triggers[i])+'Med1TrackTwo',None],
              ['Tau'+str(trax[j])+'Track',["TauTotalWeight"]],
              ['TauHighPt',None],
              ],
              )

    
            loop += ztautau.algs.algs.PlotAlg(
            region    = 'SR_highSCDP_'+str(triggers[i])+'med_Tau'+str(trax[j])+'Track',
            plot_all  = False,
            cut_flow  = [
              ['SumCosDPhi05',None],
              ['MuonGradIso',["MuonTotalWeight"]],
              ['VisMass4580',None],
              ['OS',None],
              ['TauPt25',None],
              ['HLTTau'+str(triggers[i])+'Med1TrackTwo',None],
              ['Tau'+str(trax[j])+'Track',["TauTotalWeight"]],
              ],
              )


            loop += ztautau.algs.algs.PlotAlg(
            region    = 'SR_highSCDP_'+str(triggers[i])+'med_lowPT_Tau'+str(trax[j])+'Track',
            plot_all  = False,
            cut_flow  = [
              ['SumCosDPhi05',None],
              ['MuonGradIso',["MuonTotalWeight"]],
              ['VisMass4580',None],
              ['OS',None],
              ['HLTTau'+str(triggers[i])+'Med1TrackTwo',None],
              ['Tau'+str(trax[j])+'Track',["TauTotalWeight"]],
              ['TauLowPt',None],
              ['TauPt25',None],              
              ],
              )

            loop += ztautau.algs.algs.PlotAlg(
            region    = 'SR_highSCDP_'+str(triggers[i])+'med_highPT_Tau'+str(trax[j])+'Track',
            plot_all  = False,
            cut_flow  = [
              ['SumCosDPhi05',None],
              ['MuonGradIso',["MuonTotalWeight"]],
              ['VisMass4580',None],
              ['OS',None],
              ['TauPt25',None],
              ['HLTTau'+str(triggers[i])+'Med1TrackTwo',None],
              ['Tau'+str(trax[j])+'Track',["TauTotalWeight"]],
              ['TauHighPt',None],
              ],
              )

            loop += ztautau.algs.algs.PlotAlg(
            region    = 'SR_highSCDP_SS'+str(triggers[i])+'med_Tau'+str(trax[j])+'Track',
            plot_all  = False,
            cut_flow  = [
              ['SumCosDPhi05',None],
              ['MuonGradIso',["MuonTotalWeight"]],
              ['VisMass4580',None],
              ['SS',None],
              ['TauPt25',None],
              ['HLTTau'+str(triggers[i])+'Med1TrackTwo',None],
              ['Tau'+str(trax[j])+'Track',["TauTotalWeight"]],
              ],
              )


            loop += ztautau.algs.algs.PlotAlg(
            region    = 'SR_highSCDP_SS'+str(triggers[i])+'med_lowPT_Tau'+str(trax[j])+'Track',
            plot_all  = False,
            cut_flow  = [
              ['SumCosDPhi05',None],
              ['MuonGradIso',["MuonTotalWeight"]],
              ['VisMass4580',None],
              ['SS',None],
              ['TauPt25',None],
              ['HLTTau'+str(triggers[i])+'Med1TrackTwo',None],
              ['Tau'+str(trax[j])+'Track',["TauTotalWeight"]],
              ['TauLowPt',None],
              ],
              )

            loop += ztautau.algs.algs.PlotAlg(
            region    = 'SR_highSCDP_SS'+str(triggers[i])+'med_highPT_Tau'+str(trax[j])+'Track',
            plot_all  = False,
            cut_flow  = [
              ['SumCosDPhi05',None],
              ['MuonGradIso',["MuonTotalWeight"]],
              ['VisMass4580',None],
              ['SS',None],
              ['TauPt25',None],
              ['HLTTau'+str(triggers[i])+'Med1TrackTwo',None],
              ['Tau'+str(trax[j])+'Track',["TauTotalWeight"]],
              ['TauHighPt',None],
              ],
              )

        
            loop += ztautau.algs.algs.PlotAlg(
            region    = 'SR_lowSCDP_'+str(triggers[i])+'med_Tau'+str(trax[j])+'Track',
            plot_all  = False,
            cut_flow  = [
              ['TauPt25',None],
              ['SumCosDPhi06',None],
              ['MuonGradIso',["MuonTotalWeight"]],
              ['VisMass4580',None],
              ['OS',None],
              ['HLTTau'+str(triggers[i])+'Med1TrackTwo',None],
              ['Tau'+str(trax[j])+'Track',["TauTotalWeight"]],
              ],
              )


            loop += ztautau.algs.algs.PlotAlg(
            region    = 'SR_lowSCDP_'+str(triggers[i])+'med_lowPT_Tau'+str(trax[j])+'Track',
            plot_all  = False,
            cut_flow  = [
              ['TauPt25',None],
              ['SumCosDPhi06',None],
              ['MuonGradIso',["MuonTotalWeight"]],
              ['VisMass4580',None],
              ['OS',None],
              ['HLTTau'+str(triggers[i])+'Med1TrackTwo',None],
              ['Tau'+str(trax[j])+'Track',["TauTotalWeight"]],
              ['TauLowPt',None],
              ],
              )

            loop += ztautau.algs.algs.PlotAlg(
            region    = 'SR_lowSCDP_'+str(triggers[i])+'med_highPT_Tau'+str(trax[j])+'Track',
            plot_all  = False,
            cut_flow  = [
              ['TauPt25',None],
              ['SumCosDPhi06',None],
              ['MuonGradIso',["MuonTotalWeight"]],
              ['VisMass4580',None],
              ['OS',None],
              ['HLTTau'+str(triggers[i])+'Med1TrackTwo',None],
              ['Tau'+str(trax[j])+'Track',["TauTotalWeight"]],
              ['TauHighPt',None],
              ],
              )

            loop += ztautau.algs.algs.PlotAlg(
            region    = 'SR_lowSCDP_SS'+str(triggers[i])+'med_Tau'+str(trax[j])+'Track',
            plot_all  = False,
            cut_flow  = [
              ['TauPt25',None],
              ['SumCosDPhi06',None],
              ['MuonGradIso',["MuonTotalWeight"]],
              ['VisMass4580',None],
              ['SS',None],
              ['HLTTau'+str(triggers[i])+'Med1TrackTwo',None],
              ['Tau'+str(trax[j])+'Track',["TauTotalWeight"]],
              ],
              )


            loop += ztautau.algs.algs.PlotAlg(
            region    = 'SR_lowSCDP_SS'+str(triggers[i])+'med_lowPT_Tau'+str(trax[j])+'Track',
            plot_all  = False,
            cut_flow  = [
              ['TauPt25',None],
              ['SumCosDPhi06',None],
              ['MuonGradIso',["MuonTotalWeight"]],
              ['VisMass4580',None],
              ['SS',None],
              ['HLTTau'+str(triggers[i])+'Med1TrackTwo',None],
              ['Tau'+str(trax[j])+'Track',["TauTotalWeight"]],
              ['TauLowPt',None],
              ],
              )

            loop += ztautau.algs.algs.PlotAlg(
            region    = 'SR_lowSCDP_SS'+str(triggers[i])+'med_highPT_Tau'+str(trax[j])+'Track',
            plot_all  = False,
            cut_flow  = [
                          ['TauPt25',None],
              ['SumCosDPhi06',None],
              ['MuonGradIso',["MuonTotalWeight"]],
              ['VisMass4580',None],
              ['SS',None],
              ['HLTTau'+str(triggers[i])+'Med1TrackTwo',None],
              ['Tau'+str(trax[j])+'Track',["TauTotalWeight"]],
              ['TauHighPt',None],
              ],
              )

    for c in range(len(trigchains)):

        loop += ztautau.algs.algs.PlotAlg(
        region    = 'Wjets_OS_'+str(trigchains[c]),
        plot_all  = False,
        cut_flow  = [
          ['MTrans60',None],
          ['MET30',None],
          ['OS',None],
          ['MuonGradIso',["MuonTotalWeight"]],
          ['HLTtau25perf'+str(trigchains[c]),None],
          ],
        ) 

        loop += ztautau.algs.algs.PlotAlg(
        region    = 'Wjets_SS_'+str(trigchains[c]),
        plot_all  = False,
        cut_flow  = [
          ['MTrans60',None],
          ['MET30',None],
          ['SS',None],
          ['MuonGradIso',["MuonTotalWeight"]],
          ['HLTtau25perf'+str(trigchains[c]),None],
          ],
        ) 

        loop += ztautau.algs.algs.PlotAlg(
        region    = 'SR_'+str(trigchains[c]),
        plot_all  = False,
        cut_flow  = [
          ['MTrans50',None],
          ['SumCosDPhi05',None],
          ['MuonGradIso',["MuonTotalWeight"]],
          ['VisMass4580',None],
          ['OS',None],
          ['HLTtau25perf'+str(trigchains[c]),None],
          ],
          )

        loop += ztautau.algs.algs.PlotAlg(
        region    = 'SR_SS'+str(trigchains[c]),
        plot_all  = False,
        cut_flow  = [
          ['MTrans50',None],
          ['SumCosDPhi05',None],
          ['MuonGradIso',["MuonTotalWeight"]],
          ['VisMass4580',None],
          ['SS',None],
          ['HLTtau25perf'+str(trigchains[c]),None],
          ],
          )

        loop += ztautau.algs.algs.PlotAlg(
        region    = 'AntiIsoCR_OS_'+str(trigchains[c]),
        plot_all  = False,
        cut_flow  = [
          ['MTrans50',None],
          ['InvMuonGradIso',["MuonWeightAI"]],
          ['SumCosDPhi05',None],
          ['OS',None],
          ['HLTtau25perf'+str(trigchains[c]),None],
          ],
          )

        loop += ztautau.algs.algs.PlotAlg(
        region    = 'AntiIsoCR_SS_'+str(trigchains[c]),
        plot_all  = False,
        cut_flow  = [
          ['MTrans50',None],
          ['InvMuonGradIso',["MuonWeightAI"]],
          ['SumCosDPhi05',None],
          ['SS',None],
          ['HLTtau25perf'+str(trigchains[c]),None],
          ],
          )

        loop += ztautau.algs.algs.PlotAlg(
        region    = 'Wjets_OS_'+str(trigchains[c])+'_lowPT',
        plot_all  = False,
        cut_flow  = [
          ['MTrans60',None],
          ['MET30',None],
          ['OS',None],
          ['MuonGradIso',["MuonTotalWeight"]],
          ['HLTtau25perf'+str(trigchains[c]),None],
          ['TauLowPt',None],
          ],
          )

        loop += ztautau.algs.algs.PlotAlg(
        region    = 'Wjets_OS_'+str(trigchains[c])+'_highPT',
        plot_all  = False,
        cut_flow  = [
          ['MTrans60',None],
          ['MET30',None],
          ['OS',None],
          ['MuonGradIso',["MuonTotalWeight"]],
          ['HLTtau25perf'+str(trigchains[c]),None],
          ['TauHighPt',None],
          ],
          )

        loop += ztautau.algs.algs.PlotAlg(
        region    = 'Wjets_SS_'+str(trigchains[c])+'_lowPT',
        plot_all  = False,
        cut_flow  = [
          ['MTrans60',None],
          ['MET30',None],
          ['SS',None],
          ['MuonGradIso',["MuonTotalWeight"]],
          ['HLTtau25perf'+str(trigchains[c]),None],
          ['TauLowPt',None],
          ],
          )

        loop += ztautau.algs.algs.PlotAlg(
        region    = 'Wjets_SS_'+str(trigchains[c])+'_highPT',
        plot_all  = False,
        cut_flow  = [
          ['MTrans60',None],
          ['MET30',None],
          ['SS',None],
          ['MuonGradIso',["MuonTotalWeight"]],
          ['HLTtau25perf'+str(trigchains[c]),None],
          ['TauHighPt',None],
          ],
          )

        loop += ztautau.algs.algs.PlotAlg(
        region    = 'SR_'+str(trigchains[c])+'_lowPT',
        plot_all  = False,
        cut_flow  = [
          ['MTrans50',None],
          ['SumCosDPhi05',None],
          ['MuonGradIso',["MuonTotalWeight"]],
          ['VisMass4580',None],
          ['OS',None],
          ['HLTtau25perf'+str(trigchains[c]),None],
          ['TauLowPt',None],
          ],
          )

        loop += ztautau.algs.algs.PlotAlg(
        region    = 'SR_'+str(trigchains[c])+'_highPT',
        plot_all  = False,
        cut_flow  = [
          ['MTrans50',None],
          ['SumCosDPhi05',None],
          ['MuonGradIso',["MuonTotalWeight"]],
          ['VisMass4580',None],
          ['OS',None],
          ['HLTtau25perf'+str(trigchains[c]),None],
          ['TauHighPt',None],
          ],
          )

        loop += ztautau.algs.algs.PlotAlg(
        region    = 'SR_SS'+str(trigchains[c])+'_lowPT',
        plot_all  = False,
        cut_flow  = [
          ['MTrans50',None],
          ['SumCosDPhi05',None],
          ['MuonGradIso',["MuonTotalWeight"]],
          ['VisMass4580',None],
          ['SS',None],
          ['HLTtau25perf'+str(trigchains[c]),None],
          ['TauLowPt',None],
          ],
          )

        loop += ztautau.algs.algs.PlotAlg(
        region    = 'SR_SS'+str(trigchains[c])+'_highPT',
        plot_all  = False,
        cut_flow  = [
          ['MTrans50',None],
          ['SumCosDPhi05',None],
          ['MuonGradIso',["MuonTotalWeight"]],
          ['VisMass4580',None],
          ['SS',None],
          ['HLTtau25perf'+str(trigchains[c]),None],
          ['TauHighPt',None],
          ],
          )

        loop += ztautau.algs.algs.PlotAlg(
        region    = 'AntiIsoCR_OS_'+str(trigchains[c])+'_lowPT',
        plot_all  = False,
        cut_flow  = [
          ['MTrans50',None],
          ['InvMuonGradIso',["MuonWeightAI"]],
          ['SumCosDPhi05',None],
          ['OS',None],
          ['HLTtau25perf'+str(trigchains[c]),None],
          ['TauLowPt',None],
          ],
          )

        loop += ztautau.algs.algs.PlotAlg(
        region    = 'AntiIsoCR_OS_'+str(trigchains[c])+'_highPT',
        plot_all  = False,
        cut_flow  = [
          ['MTrans50',None],
          ['InvMuonGradIso',["MuonWeightAI"]],
          ['SumCosDPhi05',None],
          ['OS',None],
          ['HLTtau25perf'+str(trigchains[c]),None],
          ['TauHighPt',None],
          ],
          )

        loop += ztautau.algs.algs.PlotAlg(
        region    = 'AntiIsoCR_SS_'+str(trigchains[c])+'_lowPT',
        plot_all  = False,
        cut_flow  = [
          ['MTrans50',None],
          ['InvMuonGradIso',["MuonWeightAI"]],
          ['SumCosDPhi05',None],
          ['SS',None],
          ['HLTtau25perf'+str(trigchains[c]),None],
          ['TauLowPt',None],
          ],
          )

        loop += ztautau.algs.algs.PlotAlg(
        region    = 'AntiIsoCR_SS_'+str(trigchains[c])+'_highPT',
        plot_all  = False,
        cut_flow  = [
          ['MTrans50',None],
          ['InvMuonGradIso',["MuonWeightAI"]],
          ['SumCosDPhi05',None],
          ['SS',None],
          ['HLTtau25perf'+str(trigchains[c]),None],
          ['TauHighPt',None],
          ],
          )
 
        loop += ztautau.algs.algs.PlotAlg(
        region    = 'SR_highSCDP_'+str(trigchains[c]),
        plot_all  = False,
        cut_flow  = [
          ['SumCosDPhi05',None],
          ['MuonGradIso',["MuonTotalWeight"]],
          ['VisMass4580',None],
          ['TauPt25',None],
          ['OS',None],
          ['HLTtau25perf'+str(trigchains[c]),None],
          ],
          )

        loop += ztautau.algs.algs.PlotAlg(
        region    = 'SR_highSCDP_'+str(trigchains[c])+'_lowPT',
        plot_all  = False,
        cut_flow  = [
          ['TauPt25',None],        
          ['SumCosDPhi05',None],
          ['MuonGradIso',["MuonTotalWeight"]],
          ['VisMass4580',None],
          ['OS',None],
          ['HLTtau25perf'+str(trigchains[c]),None],
          ['TauLowPt',None],
          ],
          )

        loop += ztautau.algs.algs.PlotAlg(
        region    = 'SR_highSCDP_'+str(trigchains[c])+'_highPT',
        plot_all  = False,
        cut_flow  = [
          ['SumCosDPhi05',None],
          ['TauPt25',None],
          ['MuonGradIso',["MuonTotalWeight"]],
          ['VisMass4580',None],
          ['OS',None],
          ['HLTtau25perf'+str(trigchains[c]),None],
          ['TauHighPt',None],
          ],
          )

        loop += ztautau.algs.algs.PlotAlg(
        region    = 'SR_highSCDP_SS'+str(trigchains[c]),
        plot_all  = False,
        cut_flow  = [
          ['TauPt25',None],
          ['SumCosDPhi05',None],
          ['MuonGradIso',["MuonTotalWeight"]],
          ['VisMass4580',None],
          ['SS',None],
          ['HLTtau25perf'+str(trigchains[c]),None],
          ],
          )


        loop += ztautau.algs.algs.PlotAlg(
        region    = 'SR_highSCDP_SS'+str(trigchains[c])+'_lowPT',
        plot_all  = False,
        cut_flow  = [
          ['SumCosDPhi05',None],
          ['MuonGradIso',["MuonTotalWeight"]],
          ['VisMass4580',None],
          ['SS',None],
          ['TauPt25',None],
          ['HLTtau25perf'+str(trigchains[c]),None],
          ['TauLowPt',None],
          ],
          )

        loop += ztautau.algs.algs.PlotAlg(
        region    = 'SR_highSCDP_SS'+str(trigchains[c])+'_highPT',
        plot_all  = False,
        cut_flow  = [
          ['SumCosDPhi05',None],
          ['MuonGradIso',["MuonTotalWeight"]],
          ['VisMass4580',None],
          ['SS',None],
          ['TauPt25',None],
          ['HLTtau25perf'+str(trigchains[c]),None],
          ['TauHighPt',None],
          ],
          )
  
        loop += ztautau.algs.algs.PlotAlg(
        region    = 'SR_lowSCDP_'+str(trigchains[c]),
        plot_all  = False,
        cut_flow  = [
          ['TauPt25',None],
          ['SumCosDPhi06',None],
          ['MuonGradIso',["MuonTotalWeight"]],
          ['VisMass4580',None],
          ['OS',None],
          ['HLTtau25perf'+str(trigchains[c]),None],
          ],
          )

        loop += ztautau.algs.algs.PlotAlg(
        region    = 'SR_lowSCDP_'+str(trigchains[c])+'_lowPT',
        plot_all  = False,
        cut_flow  = [
          ['TauPt25',None],
          ['SumCosDPhi06',None],
          ['MuonGradIso',["MuonTotalWeight"]],
          ['VisMass4580',None],
          ['OS',None],
          ['HLTtau25perf'+str(trigchains[c]),None],
          ['TauLowPt',None],
          ],
          )

        loop += ztautau.algs.algs.PlotAlg(
        region    = 'SR_lowSCDP_'+str(trigchains[c])+'_highPT',
        plot_all  = False,
        cut_flow  = [
          ['TauPt25',None],
          ['SumCosDPhi06',None],
          ['MuonGradIso',["MuonTotalWeight"]],
          ['VisMass4580',None],
          ['OS',None],
          ['HLTtau25perf'+str(trigchains[c]),None],
          ['TauHighPt',None],
          ],
          )

        loop += ztautau.algs.algs.PlotAlg(
        region    = 'SR_lowSCDP_SS'+str(trigchains[c]),
        plot_all  = False,
        cut_flow  = [
          ['TauPt25',None],
          ['SumCosDPhi06',None],
          ['MuonGradIso',["MuonTotalWeight"]],
          ['VisMass4580',None],
          ['SS',None],
          ['HLTtau25perf'+str(trigchains[c]),None],
          ],
          )

        loop += ztautau.algs.algs.PlotAlg(
        region    = 'SR_lowSCDP_SS'+str(trigchains[c])+'_lowPT',
        plot_all  = False,
        cut_flow  = [
          ['TauPt25',None],
          ['SumCosDPhi06',None],
          ['MuonGradIso',["MuonTotalWeight"]],
          ['VisMass4580',None],
          ['SS',None],
          ['HLTtau25perf'+str(trigchains[c]),None],
          ['TauLowPt',None],
          ],
          )

        loop += ztautau.algs.algs.PlotAlg(
        region    = 'SR_lowSCDP_SS'+str(trigchains[c])+'_highPT',
        plot_all  = False,
        cut_flow  = [
          ['TauPt25',None],
          ['SumCosDPhi06',None],
          ['MuonGradIso',["MuonTotalWeight"]],
          ['VisMass4580',None],
          ['SS',None],
          ['HLTtau25perf'+str(trigchains[c]),None],
          ['TauHighPt',None],
          ],
          )
 
        for j in range(len(trax)):
            loop += ztautau.algs.algs.PlotAlg(
            region    = 'Wjets_OS_'+str(trigchains[c])+'_Tau'+str(trax[j])+'Track',
            plot_all  = False,
            cut_flow  = [
              ['MTrans60',None],
              ['MET30',None],
              ['OS',None],
              ['MuonGradIso',["MuonTotalWeight"]],
              ['HLTtau25perf'+str(trigchains[c]),None],
              ['Tau'+str(trax[j])+'Track',["TauTotalWeight"]],
              ],
            ) 

            loop += ztautau.algs.algs.PlotAlg(
            region    = 'Wjets_OS_'+str(trigchains[c])+'_lowPT_Tau'+str(trax[j])+'Track',
            plot_all  = False,
            cut_flow  = [
              ['MTrans60',None],
              ['MET30',None],
              ['OS',None],
              ['MuonGradIso',["MuonTotalWeight"]],
              ['HLTtau25perf'+str(trigchains[c]),None],
              ['Tau'+str(trax[j])+'Track',["TauTotalWeight"]],
              ['TauLowPt',None],
              ],
              )

            loop += ztautau.algs.algs.PlotAlg(
            region    = 'Wjets_OS_'+str(trigchains[c])+'_highPT_Tau'+str(trax[j])+'Track',
            plot_all  = False,
            cut_flow  = [
              ['MTrans60',None],
              ['MET30',None],
              ['OS',None],
              ['MuonGradIso',["MuonTotalWeight"]],
              ['HLTtau25perf'+str(trigchains[c]),None],
              ['Tau'+str(trax[j])+'Track',["TauTotalWeight"]],
              ['TauHighPt',None],
              ],
              )

            loop += ztautau.algs.algs.PlotAlg(
            region    = 'Wjets_SS_'+str(trigchains[c])+'_Tau'+str(trax[j])+'Track',
            plot_all  = False,
            cut_flow  = [
              ['MTrans60',None],
              ['MET30',None],
              ['SS',None],
              ['MuonGradIso',["MuonTotalWeight"]],
              ['HLTtau25perf'+str(trigchains[c]),None],
              ['Tau'+str(trax[j])+'Track',["TauTotalWeight"]],
              ],
            ) 

            loop += ztautau.algs.algs.PlotAlg(
            region    = 'Wjets_SS_'+str(trigchains[c])+'_lowPT_Tau'+str(trax[j])+'Track',
            plot_all  = False,
            cut_flow  = [
              ['MTrans60',None],
              ['MET30',None],
              ['SS',None],
              ['MuonGradIso',["MuonTotalWeight"]],
              ['HLTtau25perf'+str(trigchains[c]),None],
              ['Tau'+str(trax[j])+'Track',["TauTotalWeight"]],
              ['TauLowPt',None],
              ],
              )

            loop += ztautau.algs.algs.PlotAlg(
            region    = 'Wjets_SS_'+str(trigchains[c])+'_highPT_Tau'+str(trax[j])+'Track',
            plot_all  = False,
            cut_flow  = [
              ['MTrans60',None],
              ['MET30',None],
              ['SS',None],
              ['MuonGradIso',["MuonTotalWeight"]],
              ['HLTtau25perf'+str(trigchains[c]),None],
              ['Tau'+str(trax[j])+'Track',["TauTotalWeight"]],
              ['TauHighPt',None],
              ],
              )

            loop += ztautau.algs.algs.PlotAlg(
            region    = 'SR_'+str(trigchains[c])+'_Tau'+str(trax[j])+'Track',
            plot_all  = False,
            cut_flow  = [
              ['MTrans50',None],
              ['SumCosDPhi05',None],
              ['MuonGradIso',["MuonTotalWeight"]],
              ['VisMass4580',None],
              ['OS',None],
              ['HLTtau25perf'+str(trigchains[c]),None],
              ['Tau'+str(trax[j])+'Track',["TauTotalWeight"]],
              ],
              )


            loop += ztautau.algs.algs.PlotAlg(
            region    = 'SR_'+str(trigchains[c])+'_lowPT_Tau'+str(trax[j])+'Track',
            plot_all  = False,
            cut_flow  = [
              ['MTrans50',None],
              ['SumCosDPhi05',None],
              ['MuonGradIso',["MuonTotalWeight"]],
              ['VisMass4580',None],
              ['OS',None],
              ['HLTtau25perf'+str(trigchains[c]),None],
              ['Tau'+str(trax[j])+'Track',["TauTotalWeight"]],
              ['TauLowPt',None],
              ],
              )

            loop += ztautau.algs.algs.PlotAlg(
            region    = 'SR_'+str(trigchains[c])+'_highPT_Tau'+str(trax[j])+'Track',
            plot_all  = False,
            cut_flow  = [
              ['MTrans50',None],
              ['SumCosDPhi05',None],
              ['MuonGradIso',["MuonTotalWeight"]],
              ['VisMass4580',None],
              ['OS',None],
              ['HLTtau25perf'+str(trigchains[c]),None],
              ['Tau'+str(trax[j])+'Track',["TauTotalWeight"]],
              ['TauHighPt',None],
              ],
              )

            loop += ztautau.algs.algs.PlotAlg(
            region    = 'SR_SS'+str(trigchains[c])+'_Tau'+str(trax[j])+'Track',
            plot_all  = False,
            cut_flow  = [
              ['MTrans50',None],
              ['SumCosDPhi05',None],
              ['MuonGradIso',["MuonTotalWeight"]],
              ['VisMass4580',None],
              ['SS',None],
              ['HLTtau25perf'+str(trigchains[c]),None],
              ['Tau'+str(trax[j])+'Track',["TauTotalWeight"]],
              ],
              )


            loop += ztautau.algs.algs.PlotAlg(
            region    = 'SR_SS'+str(trigchains[c])+'_lowPT_Tau'+str(trax[j])+'Track',
            plot_all  = False,
            cut_flow  = [
              ['MTrans50',None],
              ['SumCosDPhi05',None],
              ['MuonGradIso',["MuonTotalWeight"]],
              ['VisMass4580',None],
              ['SS',None],
              ['HLTtau25perf'+str(trigchains[c]),None],
              ['Tau'+str(trax[j])+'Track',["TauTotalWeight"]],
              ['TauLowPt',None],
              ],
              )

            loop += ztautau.algs.algs.PlotAlg(
            region    = 'SR_SS'+str(trigchains[c])+'_highPT_Tau'+str(trax[j])+'Track',
            plot_all  = False,
            cut_flow  = [
              ['MTrans50',None],
              ['SumCosDPhi05',None],
              ['MuonGradIso',["MuonTotalWeight"]],
              ['VisMass4580',None],
              ['SS',None],
              ['HLTtau25perf'+str(trigchains[c]),None],
              ['Tau'+str(trax[j])+'Track',["TauTotalWeight"]],
              ['TauHighPt',None],
              ],
              )

            loop += ztautau.algs.algs.PlotAlg(
            region    = 'AntiIsoCR_OS_'+str(trigchains[c])+'_Tau'+str(trax[j])+'Track',
            plot_all  = False,
            cut_flow  = [
              ['MTrans50',None],
              ['InvMuonGradIso',["MuonWeightAI"]],
              ['SumCosDPhi05',None],
              ['OS',None],
              ['HLTtau25perf'+str(trigchains[c]),None],
              ['Tau'+str(trax[j])+'Track',["TauTotalWeight"]],
              ],
              )

            loop += ztautau.algs.algs.PlotAlg(
            region    = 'AntiIsoCR_OS_'+str(trigchains[c])+'_lowPT_Tau'+str(trax[j])+'Track',
            plot_all  = False,
            cut_flow  = [
              ['MTrans50',None],
              ['InvMuonGradIso',["MuonWeightAI"]],
              ['SumCosDPhi05',None],
              ['OS',None],
              ['HLTtau25perf'+str(trigchains[c]),None],
              ['Tau'+str(trax[j])+'Track',["TauTotalWeight"]],
              ['TauLowPt',None],
              ],
              )

            loop += ztautau.algs.algs.PlotAlg(
            region    = 'AntiIsoCR_OS_'+str(trigchains[c])+'_highPT_Tau'+str(trax[j])+'Track',
            plot_all  = False,
            cut_flow  = [
              ['MTrans50',None],
              ['InvMuonGradIso',["MuonWeightAI"]],
              ['SumCosDPhi05',None],
              ['OS',None],
              ['HLTtau25perf'+str(trigchains[c]),None],
              ['Tau'+str(trax[j])+'Track',["TauTotalWeight"]],
              ['TauHighPt',None],
              ],
              )
            loop += ztautau.algs.algs.PlotAlg(
            region    = 'AntiIsoCR_SS_'+str(trigchains[c])+'_Tau'+str(trax[j])+'Track',
            plot_all  = False,
            cut_flow  = [
              ['MTrans50',None],
              ['InvMuonGradIso',["MuonWeightAI"]],
              ['SumCosDPhi05',None],
              ['SS',None],
              ['HLTtau25perf'+str(trigchains[c]),None],
              ['Tau'+str(trax[j])+'Track',["TauTotalWeight"]],
              ],
              )

            loop += ztautau.algs.algs.PlotAlg(
            region    = 'AntiIsoCR_SS_'+str(trigchains[c])+'_lowPT_Tau'+str(trax[j])+'Track',
            plot_all  = False,
            cut_flow  = [
              ['MTrans50',None],
              ['InvMuonGradIso',["MuonWeightAI"]],
              ['SumCosDPhi05',None],
              ['SS',None],
              ['HLTtau25perf'+str(trigchains[c]),None],
              ['Tau'+str(trax[j])+'Track',["TauTotalWeight"]],
              ['TauLowPt',None],
              ],
              )

            loop += ztautau.algs.algs.PlotAlg(
            region    = 'AntiIsoCR_SS_'+str(trigchains[c])+'_highPT_Tau'+str(trax[j])+'Track',
            plot_all  = False,
            cut_flow  = [
              ['MTrans50',None],
              ['InvMuonGradIso',["MuonWeightAI"]],
              ['SumCosDPhi05',None],
              ['SS',None],
              ['HLTtau25perf'+str(trigchains[c]),None],
              ['Tau'+str(trax[j])+'Track',["TauTotalWeight"]],
              ['TauHighPt',None],
              ],
              )

            loop += ztautau.algs.algs.PlotAlg(
            region    = 'SR_highSCDP_'+str(trigchains[c])+'_Tau'+str(trax[j])+'Track',
            plot_all  = False,
            cut_flow  = [
              ['SumCosDPhi05',None],
              ['MuonGradIso',["MuonTotalWeight"]],
              ['VisMass4580',None],
              ['OS',None],
              ['TauPt25',None],
              ['HLTtau25perf'+str(trigchains[c]),None],
              ['Tau'+str(trax[j])+'Track',["TauTotalWeight"]],
              ],
              )


            loop += ztautau.algs.algs.PlotAlg(
            region    = 'SR_highSCDP_'+str(trigchains[c])+'_lowPT_Tau'+str(trax[j])+'Track',
            plot_all  = False,
            cut_flow  = [
              ['SumCosDPhi05',None],
              ['MuonGradIso',["MuonTotalWeight"]],
              ['VisMass4580',None],
              ['OS',None],
              ['HLTtau25perf'+str(trigchains[c]),None],
              ['Tau'+str(trax[j])+'Track',["TauTotalWeight"]],
              ['TauLowPt',None],
              ['TauPt25',None],              
              ],
              )

            loop += ztautau.algs.algs.PlotAlg(
            region    = 'SR_highSCDP_'+str(trigchains[c])+'_highPT_Tau'+str(trax[j])+'Track',
            plot_all  = False,
            cut_flow  = [
              ['SumCosDPhi05',None],
              ['MuonGradIso',["MuonTotalWeight"]],
              ['VisMass4580',None],
              ['OS',None],
              ['TauPt25',None],
              ['HLTtau25perf'+str(trigchains[c]),None],
              ['Tau'+str(trax[j])+'Track',["TauTotalWeight"]],
              ['TauHighPt',None],
              ],
              )

            loop += ztautau.algs.algs.PlotAlg(
            region    = 'SR_highSCDP_SS'+str(trigchains[c])+'_Tau'+str(trax[j])+'Track',
            plot_all  = False,
            cut_flow  = [
              ['SumCosDPhi05',None],
              ['MuonGradIso',["MuonTotalWeight"]],
              ['VisMass4580',None],
              ['SS',None],
              ['TauPt25',None],
              ['HLTtau25perf'+str(trigchains[c]),None],
              ['Tau'+str(trax[j])+'Track',["TauTotalWeight"]],
              ],
              )


            loop += ztautau.algs.algs.PlotAlg(
            region    = 'SR_highSCDP_SS'+str(trigchains[c])+'_lowPT_Tau'+str(trax[j])+'Track',
            plot_all  = False,
            cut_flow  = [
              ['SumCosDPhi05',None],
              ['MuonGradIso',["MuonTotalWeight"]],
              ['VisMass4580',None],
              ['SS',None],
              ['TauPt25',None],
              ['HLTtau25perf'+str(trigchains[c]),None],
              ['Tau'+str(trax[j])+'Track',["TauTotalWeight"]],
              ['TauLowPt',None],
              ],
              )

            loop += ztautau.algs.algs.PlotAlg(
            region    = 'SR_highSCDP_SS'+str(trigchains[c])+'_highPT_Tau'+str(trax[j])+'Track',
            plot_all  = False,
            cut_flow  = [
              ['SumCosDPhi05',None],
              ['MuonGradIso',["MuonTotalWeight"]],
              ['VisMass4580',None],
              ['SS',None],
              ['TauPt25',None],
              ['HLTtau25perf'+str(trigchains[c]),None],
              ['Tau'+str(trax[j])+'Track',["TauTotalWeight"]],
              ['TauHighPt',None],
              ],
              )

            loop += ztautau.algs.algs.PlotAlg(
            region    = 'SR_lowSCDP_'+str(trigchains[c])+'_Tau'+str(trax[j])+'Track',
            plot_all  = False,
            cut_flow  = [
              ['TauPt25',None],
              ['SumCosDPhi06',None],
              ['MuonGradIso',["MuonTotalWeight"]],
              ['VisMass4580',None],
              ['OS',None],
              ['HLTtau25perf'+str(trigchains[c]),None],
              ['Tau'+str(trax[j])+'Track',["TauTotalWeight"]],
              ],
              )

            loop += ztautau.algs.algs.PlotAlg(
            region    = 'SR_lowSCDP_'+str(trigchains[c])+'_lowPT_Tau'+str(trax[j])+'Track',
            plot_all  = False,
            cut_flow  = [
              ['TauPt25',None],
              ['SumCosDPhi06',None],
              ['MuonGradIso',["MuonTotalWeight"]],
              ['VisMass4580',None],
              ['OS',None],
              ['HLTtau25perf'+str(trigchains[c]),None],
              ['Tau'+str(trax[j])+'Track',["TauTotalWeight"]],
              ['TauLowPt',None],
              ],
              )

            loop += ztautau.algs.algs.PlotAlg(
            region    = 'SR_lowSCDP_'+str(trigchains[c])+'_highPT_Tau'+str(trax[j])+'Track',
            plot_all  = False,
            cut_flow  = [
              ['TauPt25',None],
              ['SumCosDPhi06',None],
              ['MuonGradIso',["MuonTotalWeight"]],
              ['VisMass4580',None],
              ['OS',None],
              ['HLTtau25perf'+str(trigchains[c]),None],
              ['Tau'+str(trax[j])+'Track',["TauTotalWeight"]],
              ['TauHighPt',None],
              ],
              )

            loop += ztautau.algs.algs.PlotAlg(
            region    = 'SR_lowSCDP_SS'+str(trigchains[c])+'_Tau'+str(trax[j])+'Track',
            plot_all  = False,
            cut_flow  = [
              ['TauPt25',None],
              ['SumCosDPhi06',None],
              ['MuonGradIso',["MuonTotalWeight"]],
              ['VisMass4580',None],
              ['SS',None],
              ['HLTtau25perf'+str(trigchains[c]),None],
              ['Tau'+str(trax[j])+'Track',["TauTotalWeight"]],
              ],
              )

            loop += ztautau.algs.algs.PlotAlg(
            region    = 'SR_lowSCDP_SS'+str(trigchains[c])+'_lowPT_Tau'+str(trax[j])+'Track',
            plot_all  = False,
            cut_flow  = [
              ['TauPt25',None],
              ['SumCosDPhi06',None],
              ['MuonGradIso',["MuonTotalWeight"]],
              ['VisMass4580',None],
              ['SS',None],
              ['HLTtau25perf'+str(trigchains[c]),None],
              ['Tau'+str(trax[j])+'Track',["TauTotalWeight"]],
              ['TauLowPt',None],
              ],
              )

            loop += ztautau.algs.algs.PlotAlg(
            region    = 'SR_lowSCDP_SS'+str(trigchains[c])+'_highPT_Tau'+str(trax[j])+'Track',
            plot_all  = False,
            cut_flow  = [
              ['TauPt25',None],
              ['SumCosDPhi06',None],
              ['MuonGradIso',["MuonTotalWeight"]],
              ['VisMass4580',None],
              ['SS',None],
              ['HLTtau25perf'+str(trigchains[c]),None],
              ['Tau'+str(trax[j])+'Track',["TauTotalWeight"]],
              ['TauHighPt',None],
              ],
              )


    
############ # RQCD SYSTEMATICS
    """ 
    
    #test region no iso
    loop += ztautau.algs.algs.PlotAlg(
            region    = 'SR_no_iso',
            plot_all  = False,
            cut_flow  = [
              ['MTrans50',None],
              ['SumCosDPhi05',None],
              ['VisMass4580',None],
              ['OS',None],
              ],
            )

    """
    
     
    """ 
    n = 10
    while n < 31:
        loop += ztautau.algs.algs.PlotAlg(
                region   = 'AntiIsoCR_OS_Topoetcone20pt0'+str(n),
                plot_all = False,
                cut_flow = [
                    ['MTrans50',None],
                    ['SumCosDPhi05',None],
                    ['OS',None],
                    ['InvMuonGradIso',None],
                    ['Topoetcone20pt0'+str(n),["MuonWeightAI"]],
                    ],
                  )

    	    
        loop += ztautau.algs.algs.PlotAlg(
                region   = 'AntiIsoCR_OS_lowPT_Topoetcone20pt0'+str(n),
                plot_all = False,
                cut_flow = [
                    ['MTrans50',None],
                    ['SumCosDPhi05',None],
                    ['OS',None],
                    ['TauLowPt',["TauTotalWeight"]],
                    ['InvMuonGradIso',None],
                    ['Topoetcone20pt0'+str(n),["MuonWeightAI"]],
                    ],
                  )

        loop += ztautau.algs.algs.PlotAlg(
                region   = 'AntiIsoCR_OS_highPT_Topoetcone20pt0'+str(n),
                plot_all = False,
                cut_flow = [
                    ['MTrans50',None],
                    ['SumCosDPhi05',None],
                    ['OS',None],
                    ['TauHighPt',["TauTotalWeight"]],          
                    ['InvMuonGradIso',None],
                    ['Topoetcone20pt0'+str(n),["MuonWeightAI"]],
                    ],
                  )


        loop += ztautau.algs.algs.PlotAlg(
                region   = 'AntiIsoCR_SS_Topoetcone20pt0'+str(n),
                plot_all = False,
                cut_flow = [
                    ['MTrans50',None],
                    ['SumCosDPhi05',None],
                    ['SS',None],
                    ['InvMuonGradIso',None],
                    ['Topoetcone20pt0'+str(n),["MuonWeightAI"]],
                    ],
                  )

        loop += ztautau.algs.algs.PlotAlg(
                region   = 'AntiIsoCR_SS_lowPT_Topoetcone20pt0'+str(n),
                plot_all = False,
                cut_flow = [
                    ['MTrans50',None],
                    ['SumCosDPhi05',None],
                    ['SS',None],
                    ['TauLowPt',["TauTotalWeight"]],
                    ['InvMuonGradIso',None],
                    ['Topoetcone20pt0'+str(n),["MuonWeightAI"]],
                    ],
                  )

        loop += ztautau.algs.algs.PlotAlg(
                region   = 'AntiIsoCR_SS_highPT_Topoetcone20pt0'+str(n),
                plot_all = False,
                cut_flow = [
                    ['MTrans50',None],
                    ['SumCosDPhi05',None],
                    ['SS',None],
                    ['TauHighPt',["TauTotalWeight"]],          
                    ['InvMuonGradIso',None],
                    ['Topoetcone20pt0'+str(n),["MuonWeightAI"]],
                    ],
                 )
	     
        
        for j in range(len(trax)):

                loop += ztautau.algs.algs.PlotAlg(
                        region   = 'AntiIsoCR_OS_Tau'+str(trax[j])+'Track_Topoetcone20pt0'+str(n),
                        plot_all = False,
                        cut_flow = [
                            ['MTrans50',None],
                            ['SumCosDPhi05',None],
                            ['OS',None],
                            ['Tau'+str(trax[j])+'Track',["TauTotalWeight"]],
                            ['InvMuonGradIso',None],
                            ['Topoetcone20pt0'+str(n),["MuonWeightAI"]],
                            ],
                          )

                loop += ztautau.algs.algs.PlotAlg(
                        region   = 'AntiIsoCR_OS_lowPT_Tau'+str(trax[j])+'Track_Topoetcone20pt0'+str(n),
                        plot_all = False,
                        cut_flow = [
                            ['MTrans50',None],
                            ['Tau'+str(trax[j])+'Track',["TauTotalWeight"]],
                            ['SumCosDPhi05',None],
                            ['OS',None],
                            ['TauLowPt',["TauTotalWeight"]],
                            ['InvMuonGradIso',None],
                            ['Topoetcone20pt0'+str(n),["MuonWeightAI"]],
                            ],
                          )

                loop += ztautau.algs.algs.PlotAlg(
                        region   = 'AntiIsoCR_OS_highPT_Tau'+str(trax[j])+'Track_Topoetcone20pt0'+str(n),
                        plot_all = False,
                        cut_flow = [
                            ['MTrans50',None],
                            ['SumCosDPhi05',None],
                            ['OS',None],
                            ['TauHighPt',["TauTotalWeight"]],          
                            ['Tau'+str(trax[j])+'Track',["TauTotalWeight"]],
                            ['InvMuonGradIso',None],
                            ['Topoetcone20pt0'+str(n),["MuonWeightAI"]],
                            ],
                          )


                loop += ztautau.algs.algs.PlotAlg(
                        region   = 'AntiIsoCR_SS_Tau'+str(trax[j])+'Track_Topoetcone20pt0'+str(n),
                        plot_all = False,
                        cut_flow = [
                            ['MTrans50',None],
                            ['SumCosDPhi05',None],
                            ['Tau'+str(trax[j])+'Track',["TauTotalWeight"]],
                            ['SS',None],
                            ['InvMuonGradIso',None],
                            ['Topoetcone20pt0'+str(n),["MuonWeightAI"]],
                            ],
                          )

                loop += ztautau.algs.algs.PlotAlg(
                        region   = 'AntiIsoCR_SS_lowPT_Tau'+str(trax[j])+'Track_Topoetcone20pt0'+str(n),
                        plot_all = False,
                        cut_flow = [
                            ['MTrans50',None],
                            ['SumCosDPhi05',None],
                            ['Tau'+str(trax[j])+'Track',["TauTotalWeight"]],
                            ['SS',None],
                            ['TauLowPt',["TauTotalWeight"]],
                            ['InvMuonGradIso',None],
                            ['Topoetcone20pt0'+str(n),["MuonWeightAI"]],
                            ],
                          )

                loop += ztautau.algs.algs.PlotAlg(
                        region   = 'AntiIsoCR_SS_highPT_Tau'+str(trax[j])+'Track_Topoetcone20pt0'+str(n),
                        plot_all = False,
                        cut_flow = [
                            ['MTrans50',None],
                            ['SumCosDPhi05',None],
                            ['Tau'+str(trax[j])+'Track',["TauTotalWeight"]],
                            ['SS',None],
                            ['TauHighPt',["TauTotalWeight"]],          
                            ['InvMuonGradIso',None],
                            ['Topoetcone20pt0'+str(n),["MuonWeightAI"]],
                            ],
                          )

        for i in range(len(triggers)):
        
                loop += ztautau.algs.algs.PlotAlg(
                        region   = 'AntiIsoCR_OS_'+str(triggers[i])+'med_Topoetcone20pt0'+str(n),
                        plot_all = False,
                        cut_flow = [
                            ['MTrans50',None],
                            ['SumCosDPhi05',None],
                            ['OS',None],
                            ['InvMuonGradIso',None],
                            ['Topoetcone20pt0'+str(n),["MuonWeightAI"]],
                            ['HLTTau'+str(triggers[i])+'Med1TrackTwo',None],
                            ],
                          )
                
                loop += ztautau.algs.algs.PlotAlg(
                        region   = 'AntiIsoCR_OS_'+str(triggers[i])+'med_lowPT_Topoetcone20pt0'+str(n),
                        plot_all = False,
                        cut_flow = [
                            ['MTrans50',None],
		            ['SumCosDPhi05',None],
                            ['OS',None],
                            ['TauLowPt',["TauTotalWeight"]],
                            ['HLTTau'+str(triggers[i])+'Med1TrackTwo',None],
                            ['InvMuonGradIso',None],
                            ['Topoetcone20pt0'+str(n),["MuonWeightAI"]],
                            ],
                          )

                loop += ztautau.algs.algs.PlotAlg(
                        region   = 'AntiIsoCR_OS_'+str(triggers[i])+'med_highPT_Topoetcone20pt0'+str(n),
                        plot_all = False,
                        cut_flow = [
                            ['MTrans50',None],
                            ['SumCosDPhi05',None],
                            ['OS',None],
                            ['HLTTau'+str(triggers[i])+'Med1TrackTwo',None],
                            ['TauHighPt',["TauTotalWeight"]],          
                            ['InvMuonGradIso',None],
                            ['Topoetcone20pt0'+str(n),["MuonWeightAI"]],
                            ],
                          )


                loop += ztautau.algs.algs.PlotAlg(
                        region   = 'AntiIsoCR_SS_'+str(triggers[i])+'med_Topoetcone20pt0'+str(n),
                        plot_all = False,
                        cut_flow = [
                            ['MTrans50',None],
                            ['HLTTau'+str(triggers[i])+'Med1TrackTwo',None],
                            ['SumCosDPhi05',None],
                            ['SS',None],
                            ['InvMuonGradIso',None],
                            ['Topoetcone20pt0'+str(n),["MuonWeightAI"]],
                            ],
                          )

                loop += ztautau.algs.algs.PlotAlg(
                        region   = 'AntiIsoCR_SS_'+str(triggers[i])+'med_lowPT_Topoetcone20pt0'+str(n),
                        plot_all = False,
                        cut_flow = [
                            ['MTrans50',None],
                            ['SumCosDPhi05',None],
                            ['SS',None],
                            ['TauLowPt',["TauTotalWeight"]],
                            ['HLTTau'+str(triggers[i])+'Med1TrackTwo',None],
                            ['InvMuonGradIso',None],
                            ['Topoetcone20pt0'+str(n),["MuonWeightAI"]],
                            ],
                          )

                loop += ztautau.algs.algs.PlotAlg(
                        region   = 'AntiIsoCR_SS_'+str(triggers[i])+'med_highPT_Topoetcone20pt0'+str(n),
                        plot_all = False,
                        cut_flow = [
                            ['MTrans50',None],
                            ['SumCosDPhi05',None],
                            ['HLTTau'+str(triggers[i])+'Med1TrackTwo',None],
                            ['SS',None],
                            ['TauHighPt',["TauTotalWeight"]],          
                            ['InvMuonGradIso',None],
                            ['Topoetcone20pt0'+str(n),["MuonWeightAI"]],
                            ],
                          )

    
                for k in range(len(trax)):
    
                        loop += ztautau.algs.algs.PlotAlg(
                                region   = 'AntiIsoCR_OS_'+str(triggers[i])+'med_Tau'+str(trax[k])+'Track_Topoetcone20pt0'+str(n),
                                plot_all = False,
                                cut_flow = [
                                    ['MTrans50',None],
                                    ['SumCosDPhi05',None],
                                    ['OS',None],
                                    ['Tau'+str(trax[k])+'Track',["TauTotalWeight"]],
                                    ['InvMuonGradIso',None],
                                    ['Topoetcone20pt0'+str(n),["MuonWeightAI"]],
                                    ['HLTTau'+str(triggers[i])+'Med1TrackTwo',None],
                                    ],
                                  )

			loop += ztautau.algs.algs.PlotAlg(
                                region   = 'AntiIsoCR_OS_'+str(triggers[i])+'med_lowPT_Tau'+str(trax[k])+'Track_Topoetcone20pt0'+str(n),
                                plot_all = False,
                                cut_flow = [
                                    ['MTrans50',None],
                                    ['SumCosDPhi05',None],
                                    ['OS',None],
                                    ['Tau'+str(trax[k])+'Track',["TauTotalWeight"]],
                                    ['TauLowPt',["TauTotalWeight"]],
                                    ['HLTTau'+str(triggers[i])+'Med1TrackTwo',None],
                                    ['InvMuonGradIso',None],
                                    ['Topoetcone20pt0'+str(n),["MuonWeightAI"]],
                                    ],
                                  )
		    
                        loop += ztautau.algs.algs.PlotAlg(
                                region   = 'AntiIsoCR_OS_'+str(triggers[i])+'med_highPT_Tau'+str(trax[k])+'Track_Topoetcone20pt0'+str(n),
                                plot_all = False,
                                cut_flow = [
                                    ['MTrans50',None],
                                    ['Tau'+str(trax[k])+'Track',["TauTotalWeight"]],
                                    ['SumCosDPhi05',None],
                                    ['OS',None],
                                    ['HLTTau'+str(triggers[i])+'Med1TrackTwo',None],
                                    ['TauHighPt',["TauTotalWeight"]],          
                                    ['InvMuonGradIso',None],
                                    ['Topoetcone20pt0'+str(n),["MuonWeightAI"]],
                                    ],
				  )


                        loop += ztautau.algs.algs.PlotAlg(
                                region   = 'AntiIsoCR_SS_'+str(triggers[i])+'med_Tau'+str(trax[k])+'Track_Topoetcone20pt0'+str(n),
                                plot_all = False,
                                cut_flow = [
                                    ['MTrans50',None],
                                    ['HLTTau'+str(triggers[i])+'Med1TrackTwo',None],
                                    ['SumCosDPhi05',None],
                                    ['SS',None],
                                    ['InvMuonGradIso',None],
                                    ['Topoetcone20pt0'+str(n),["MuonWeightAI"]],
                                    ['Tau'+str(trax[k])+'Track',["TauTotalWeight"]],
                                    ],
                                  )

                        loop += ztautau.algs.algs.PlotAlg(
                                region   = 'AntiIsoCR_SS_'+str(triggers[i])+'med_lowPT_Tau'+str(trax[k])+'Track_Topoetcone20pt0'+str(n),
                                plot_all = False,
                                cut_flow = [
                                    ['MTrans50',None],
                                    ['SumCosDPhi05',None],
                                    ['SS',None],
                                    ['TauLowPt',["TauTotalWeight"]],
                                    ['HLTTau'+str(triggers[i])+'Med1TrackTwo',None],
                                    ['InvMuonGradIso',None],
                                    ['Tau'+str(trax[k])+'Track',["TauTotalWeight"]],
                                    ['Topoetcone20pt0'+str(n),["MuonWeightAI"]],
                                    ],
                                  )

                        loop += ztautau.algs.algs.PlotAlg(
                                region   = 'AntiIsoCR_SS_'+str(triggers[i])+'med_highPT_Tau'+str(trax[k])+'Track_Topoetcone20pt0'+str(n),
                                plot_all = False,
                                cut_flow = [
                                    ['MTrans50',None],
                                    ['SumCosDPhi05',None],
                                    ['HLTTau'+str(triggers[i])+'Med1TrackTwo',None],
                                    ['Tau'+str(trax[k])+'Track',["TauTotalWeight"]],
                                    ['SS',None],
                                    ['TauHighPt',["TauTotalWeight"]],          
                                    ['InvMuonGradIso',None],
                                    ['Topoetcone20pt0'+str(n),["MuonWeightAI"]],
                                    ],
                                  )

		    
                   

        for c in range(len(trigchains)):
        
                loop += ztautau.algs.algs.PlotAlg(
                        region   = 'AntiIsoCR_OS_'+str(trigchains[c])+'med_Topoetcone20pt0'+str(n),
                        plot_all = False,
                        cut_flow = [
                            ['MTrans50',None],
                            ['SumCosDPhi05',None],
                            ['OS',None],
                            ['InvMuonGradIso',None],
                            ['Topoetcone20pt0'+str(n),["MuonWeightAI"]],
                            ['HLTtau25perf'+str(trigchains[c]),None],
                            ],
                          )
                
                loop += ztautau.algs.algs.PlotAlg(
                        region   = 'AntiIsoCR_OS_'+str(trigchains[c])+'med_lowPT_Topoetcone20pt0'+str(n),
                        plot_all = False,
                        cut_flow = [
                            ['MTrans50',None],
		            ['SumCosDPhi05',None],
                            ['OS',None],
                            ['TauLowPt',["TauTotalWeight"]],
                            ['HLTtau25perf'+str(trigchains[c]),None],
                            ['InvMuonGradIso',None],
                            ['Topoetcone20pt0'+str(n),["MuonWeightAI"]],
                            ],
                          )

                loop += ztautau.algs.algs.PlotAlg(
                        region   = 'AntiIsoCR_OS_'+str(trigchains[c])+'med_highPT_Topoetcone20pt0'+str(n),
                        plot_all = False,
                        cut_flow = [
                            ['MTrans50',None],
                            ['SumCosDPhi05',None],
                            ['OS',None],
                            ['HLTtau25perf'+str(trigchains[c]),None],
                            ['TauHighPt',["TauTotalWeight"]],          
                            ['InvMuonGradIso',None],
                            ['Topoetcone20pt0'+str(n),["MuonWeightAI"]],
                            ],
                          )

                loop += ztautau.algs.algs.PlotAlg(
                        region   = 'AntiIsoCR_SS_'+str(trigchains[c])+'med_Topoetcone20pt0'+str(n),
                        plot_all = False,
                        cut_flow = [
                            ['MTrans50',None],
                            ['HLTtau25perf'+str(trigchains[c]),None],
                            ['SumCosDPhi05',None],
                            ['SS',None],
                            ['InvMuonGradIso',None],
                            ['Topoetcone20pt0'+str(n),["MuonWeightAI"]],
                            ],
                          )

                loop += ztautau.algs.algs.PlotAlg(
                        region   = 'AntiIsoCR_SS_'+str(trigchains[c])+'med_lowPT_Topoetcone20pt0'+str(n),
                        plot_all = False,
                        cut_flow = [
                            ['MTrans50',None],
                            ['SumCosDPhi05',None],
                            ['SS',None],
                            ['TauLowPt',["TauTotalWeight"]],
                            ['HLTtau25perf'+str(trigchains[c]),None],
                            ['InvMuonGradIso',None],
                            ['Topoetcone20pt0'+str(n),["MuonWeightAI"]],
                            ],
                          )

                loop += ztautau.algs.algs.PlotAlg(
                        region   = 'AntiIsoCR_SS_'+str(trigchains[c])+'med_highPT_Topoetcone20pt0'+str(n),
                        plot_all = False,
                        cut_flow = [
                            ['MTrans50',None],
                            ['SumCosDPhi05',None],
                            ['HLTtau25perf'+str(trigchains[c]),None],
                            ['SS',None],
                            ['TauHighPt',["TauTotalWeight"]],          
                            ['InvMuonGradIso',None],
                            ['Topoetcone20pt0'+str(n),["MuonWeightAI"]],
                            ],
                          )

                for k in range(len(trax)):
    
                        loop += ztautau.algs.algs.PlotAlg(
                                region   = 'AntiIsoCR_OS_'+str(trigchains[c])+'med_Tau'+str(trax[k])+'Track_Topoetcone20pt0'+str(n),
                                plot_all = False,
                                cut_flow = [
                                    ['MTrans50',None],
                                    ['SumCosDPhi05',None],
                                    ['OS',None],
                                    ['Tau'+str(trax[k])+'Track',["TauTotalWeight"]],
                                    ['InvMuonGradIso',None],
                                    ['Topoetcone20pt0'+str(n),["MuonWeightAI"]],
                                    ['HLTtau25perf'+str(trigchains[c]),None],
                                    ],
                                  )

			loop += ztautau.algs.algs.PlotAlg(
                                region   = 'AntiIsoCR_OS_'+str(trigchains[c])+'med_lowPT_Tau'+str(trax[k])+'Track_Topoetcone20pt0'+str(n),
                                plot_all = False,
                                cut_flow = [
                                    ['MTrans50',None],
                                    ['SumCosDPhi05',None],
                                    ['OS',None],
                                    ['Tau'+str(trax[k])+'Track',["TauTotalWeight"]],
                                    ['TauLowPt',["TauTotalWeight"]],
                                    ['HLTtau25perf'+str(trigchains[c]),None],
                                    ['InvMuonGradIso',None],
                                    ['Topoetcone20pt0'+str(n),["MuonWeightAI"]],
                                    ],
                                  )
		    
                        loop += ztautau.algs.algs.PlotAlg(
                                region   = 'AntiIsoCR_OS_'+str(trigchains[c])+'med_highPT_Tau'+str(trax[k])+'Track_Topoetcone20pt0'+str(n),
                                plot_all = False,
                                cut_flow = [
                                    ['MTrans50',None],
                                    ['Tau'+str(trax[k])+'Track',["TauTotalWeight"]],
                                    ['SumCosDPhi05',None],
                                    ['OS',None],
                                    ['HLTtau25perf'+str(trigchains[c]),None],
                                    ['TauHighPt',["TauTotalWeight"]],          
                                    ['InvMuonGradIso',None],
                                    ['Topoetcone20pt0'+str(n),["MuonWeightAI"]],
                                    ],
				  )

                        loop += ztautau.algs.algs.PlotAlg(
                                region   = 'AntiIsoCR_SS_'+str(trigchains[c])+'med_Tau'+str(trax[k])+'Track_Topoetcone20pt0'+str(n),
                                plot_all = False,
                                cut_flow = [
                                    ['MTrans50',None],
                                    ['HLTtau25perf'+str(trigchains[c]),None],
                                    ['SumCosDPhi05',None],
                                    ['SS',None],
                                    ['InvMuonGradIso',None],
                                    ['Topoetcone20pt0'+str(n),["MuonWeightAI"]],
                                    ['Tau'+str(trax[k])+'Track',["TauTotalWeight"]],
                                    ],
                                  )

                        loop += ztautau.algs.algs.PlotAlg(
                                region   = 'AntiIsoCR_SS_'+str(trigchains[c])+'med_lowPT_Tau'+str(trax[k])+'Track_Topoetcone20pt0'+str(n),
                                plot_all = False,
                                cut_flow = [
                                    ['MTrans50',None],
                                    ['SumCosDPhi05',None],
                                    ['SS',None],
                                    ['TauLowPt',["TauTotalWeight"]],
                                    ['HLTtau25perf'+str(trigchains[c]),None],
                                    ['InvMuonGradIso',None],
                                    ['Tau'+str(trax[k])+'Track',["TauTotalWeight"]],
                                    ['Topoetcone20pt0'+str(n),["MuonWeightAI"]],
                                    ],
                                  )

                        loop += ztautau.algs.algs.PlotAlg(
                                region   = 'AntiIsoCR_SS_'+str(trigchains[c])+'med_highPT_Tau'+str(trax[k])+'Track_Topoetcone20pt0'+str(n),
                                plot_all = False,
                                cut_flow = [
                                    ['MTrans50',None],
                                    ['SumCosDPhi05',None],
                                    ['HLTtau25perf'+str(trigchains[c]),None],
                                    ['Tau'+str(trax[k])+'Track',["TauTotalWeight"]],
                                    ['SS',None],
                                    ['TauHighPt',["TauTotalWeight"]],          
                                    ['InvMuonGradIso',None],
                                    ['Topoetcone20pt0'+str(n),["MuonWeightAI"]],
                                    ],
                                  )
        n += 1
    """ 
    """
    m = 10		    
    while m < 16:

        loop += ztautau.algs.algs.PlotAlg(
                region   = 'AntiIsoCR_OS_Ptvarcone30pt0'+str(m),
                plot_all = False,
                cut_flow = [
                    ['MTrans50',None],
                    ['SumCosDPhi05',None],
                    ['OS',None],
                    ['InvMuonGradIso',None],
                    ['Ptvarcone30pt0'+str(m),["MuonWeightAI"]],
                    ],
                  )
 
        loop += ztautau.algs.algs.PlotAlg(
                region   = 'AntiIsoCR_OS_lowPT_Ptvarcone30pt0'+str(m),
                plot_all = False,
                cut_flow = [
                    ['MTrans50',None],
                    ['SumCosDPhi05',None],
                    ['OS',None],
                    ['TauLowPt',["TauTotalWeight"]],
                    ['InvMuonGradIso',None],
                    ['Ptvarcone30pt0'+str(m),["MuonWeightAI"]],
                    ],
                  )

        loop += ztautau.algs.algs.PlotAlg(
                region   = 'AntiIsoCR_OS_highPT_Ptvarcone30pt0'+str(m),
                plot_all = False,
                cut_flow = [
                    ['MTrans50',None],
                    ['SumCosDPhi05',None],
                    ['OS',None],
                    ['TauHighPt',["TauTotalWeight"]],
                    ['InvMuonGradIso',None],
                    ['Ptvarcone30pt0'+str(m),["MuonWeightAI"]],
                    ],
                  )

	     
        loop += ztautau.algs.algs.PlotAlg(
                region   = 'AntiIsoCR_SS_Ptvarcone30pt0'+str(m),
                plot_all = False,
                cut_flow = [
                    ['MTrans50',None],
                    ['SumCosDPhi05',None],
                    ['SS',None],
                    ['InvMuonGradIso',None],
                    ['Ptvarcone30pt0'+str(m),["MuonWeightAI"]],
                    ],
                  )
 
        loop += ztautau.algs.algs.PlotAlg(
                region   = 'AntiIsoCR_SS_lowPT_Ptvarcone30pt0'+str(m),
                plot_all = False,
                cut_flow = [
                    ['MTrans50',None],
                    ['SumCosDPhi05',None],
                    ['SS',None],
                    ['TauLowPt',["TauTotalWeight"]],
                    ['InvMuonGradIso',None],
                    ['Ptvarcone30pt0'+str(m),["MuonWeightAI"]],
                    ],
                  )

        loop += ztautau.algs.algs.PlotAlg(
                region   = 'AntiIsoCR_SS_highPT_Ptvarcone30pt0'+str(m),
                plot_all = False,
                cut_flow = [
                    ['MTrans50',None],
                    ['SumCosDPhi05',None],
                    ['SS',None],
                    ['TauHighPt',["TauTotalWeight"]],
                    ['InvMuonGradIso',None],
                    ['Ptvarcone30pt0'+str(m),["MuonWeightAI"]],
                    ],
                  )
        
        for j in range(len(trax)):


                loop += ztautau.algs.algs.PlotAlg(
                        region   = 'AntiIsoCR_OS_Tau'+str(trax[j])+'Track_Ptvarcone30pt0'+str(m),
                        plot_all = False,
                        cut_flow = [
                            ['MTrans50',None],
                            ['SumCosDPhi05',None],
                            ['OS',None],
                            ['Tau'+str(trax[j])+'Track',["TauTotalWeight"]],
                            ['InvMuonGradIso',None],
                            ['Ptvarcone30pt0'+str(m),["MuonWeightAI"]],
                            ],
                          )

                loop += ztautau.algs.algs.PlotAlg(
                        region   = 'AntiIsoCR_OS_lowPT_Tau'+str(trax[j])+'Track_Ptvarcone30pt0'+str(m),
                        plot_all = False,
                        cut_flow = [
                            ['MTrans50',None],
                            ['SumCosDPhi05',None],
                            ['OS',None],
                            ['Tau'+str(trax[j])+'Track',["TauTotalWeight"]],
                            ['TauLowPt',["TauTotalWeight"]],
                            ['InvMuonGradIso',None],
                            ['Ptvarcone30pt0'+str(m),["MuonWeightAI"]],
                            ],
                          )

                loop += ztautau.algs.algs.PlotAlg(
                        region   = 'AntiIsoCR_OS_highPT_Tau'+str(trax[j])+'Track_Ptvarcone30pt0'+str(m),
                        plot_all = False,
                        cut_flow = [
                            ['MTrans50',None],
                            ['SumCosDPhi05',None],
                            ['OS',None],
                            ['TauHighPt',["TauTotalWeight"]],
                            ['Tau'+str(trax[j])+'Track',["TauTotalWeight"]],
                            ['InvMuonGradIso',None],
                            ['Ptvarcone30pt0'+str(m),["MuonWeightAI"]],
                            ],
                          )


                loop += ztautau.algs.algs.PlotAlg(
                        region   = 'AntiIsoCR_SS_Tau'+str(trax[j])+'Track_Ptvarcone30pt0'+str(m),
                        plot_all = False,
                        cut_flow = [
                            ['MTrans50',None],
                            ['SumCosDPhi05',None],
                            ['Tau'+str(trax[j])+'Track',["TauTotalWeight"]],
                            ['SS',None],
                            ['InvMuonGradIso',None],
                            ['Ptvarcone30pt0'+str(m),["MuonWeightAI"]],
                            ],
                          )

                loop += ztautau.algs.algs.PlotAlg(
                        region   = 'AntiIsoCR_SS_lowPT_Tau'+str(trax[j])+'Track_Ptvarcone30pt0'+str(m),
                        plot_all = False,
                        cut_flow = [
                            ['MTrans50',None],
                            ['SumCosDPhi05',None],
                            ['Tau'+str(trax[j])+'Track',["TauTotalWeight"]],
                            ['SS',None],
                            ['TauLowPt',["TauTotalWeight"]],
                            ['InvMuonGradIso',None],
                            ['Ptvarcone30pt0'+str(m),["MuonWeightAI"]],
                            ],
                          )

                loop += ztautau.algs.algs.PlotAlg(
                        region   = 'AntiIsoCR_SS_highPT_Tau'+str(trax[j])+'Track_Ptvarcone30pt0'+str(m),
                        plot_all = False,
                        cut_flow = [
                            ['MTrans50',None],
                            ['Tau'+str(trax[j])+'Track',["TauTotalWeight"]],
                            ['SumCosDPhi05',None],
                            ['SS',None],
                            ['TauHighPt',["TauTotalWeight"]],
                            ['InvMuonGradIso',None],
                            ['Ptvarcone30pt0'+str(m),["MuonWeightAI"]],
                            ],
                          )

        for i in range(len(triggers)):
        

                loop += ztautau.algs.algs.PlotAlg(
                        region   = 'AntiIsoCR_OS_'+str(triggers[i])+'med_Ptvarcone30pt0'+str(m),
                        plot_all = False,
                        cut_flow = [
                            ['MTrans50',None],
                            ['HLTTau'+str(triggers[i])+'Med1TrackTwo',None],
                            ['SumCosDPhi05',None],
                            ['OS',None],
                            ['InvMuonGradIso',None],
                            ['Ptvarcone30pt0'+str(m),["MuonWeightAI"]],
                            ],
                          )
     
                loop += ztautau.algs.algs.PlotAlg(
                        region   = 'AntiIsoCR_OS_'+str(triggers[i])+'med_lowPT_Ptvarcone30pt0'+str(m),
                        plot_all = False,
                        cut_flow = [
                            ['MTrans50',None],
                            ['SumCosDPhi05',None],
                            ['OS',None],
                            ['HLTTau'+str(triggers[i])+'Med1TrackTwo',None],
                            ['TauLowPt',["TauTotalWeight"]],
                            ['InvMuonGradIso',None],
                            ['Ptvarcone30pt0'+str(m),["MuonWeightAI"]],
                            ],
                          )

                loop += ztautau.algs.algs.PlotAlg(
                        region   = 'AntiIsoCR_OS_'+str(triggers[i])+'med_highPT_Ptvarcone30pt0'+str(m),
                        plot_all = False,
                        cut_flow = [
                            ['MTrans50',None],
                            ['SumCosDPhi05',None],
                            ['HLTTau'+str(triggers[i])+'Med1TrackTwo',None],
                            ['OS',None],
                            ['TauHighPt',["TauTotalWeight"]],
                            ['InvMuonGradIso',None],
                            ['Ptvarcone30pt0'+str(m),["MuonWeightAI"]],
                            ],
                          )


                loop += ztautau.algs.algs.PlotAlg(
                        region   = 'AntiIsoCR_SS_'+str(triggers[i])+'med_Ptvarcone30pt0'+str(m),
                        plot_all = False,
                        cut_flow = [
                            ['MTrans50',None],
                            ['SumCosDPhi05',None],
                            ['SS',None],
                            ['HLTTau'+str(triggers[i])+'Med1TrackTwo',None],
                            ['InvMuonGradIso',None],
                            ['Ptvarcone30pt0'+str(m),["MuonWeightAI"]],
                            ],
                          )
         
                loop += ztautau.algs.algs.PlotAlg(
                        region   = 'AntiIsoCR_SS_'+str(triggers[i])+'med_lowPT_Ptvarcone30pt0'+str(m),
                        plot_all = False,
                        cut_flow = [
                            ['MTrans50',None],
                            ['HLTTau'+str(triggers[i])+'Med1TrackTwo',None],
                            ['SumCosDPhi05',None],
                            ['SS',None],
                            ['TauLowPt',["TauTotalWeight"]],
                            ['InvMuonGradIso',None],
                            ['Ptvarcone30pt0'+str(m),["MuonWeightAI"]],
                            ],
                          )

                loop += ztautau.algs.algs.PlotAlg(
                        region   = 'AntiIsoCR_SS_'+str(triggers[i])+'med_highPT_Ptvarcone30pt0'+str(m),
                        plot_all = False,
                        cut_flow = [
                            ['MTrans50',None],
                            ['SumCosDPhi05',None],
                            ['SS',None],
                            ['TauHighPt',["TauTotalWeight"]],
                            ['HLTTau'+str(triggers[i])+'Med1TrackTwo',None],
                            ['InvMuonGradIso',None],
                            ['Ptvarcone30pt0'+str(m),["MuonWeightAI"]],
                            ],
                          )    
    
                for k in range(len(trax)):
    

                        loop += ztautau.algs.algs.PlotAlg(
                                region   = 'AntiIsoCR_OS_'+str(triggers[i])+'med_Tau'+str(trax[k])+'Track_Ptvarcone30pt0'+str(m),
                                plot_all = False,
                                cut_flow = [
				    ['MTrans50',None],
                                    ['HLTTau'+str(triggers[i])+'Med1TrackTwo',None],
                                    ['SumCosDPhi05',None],
                                    ['OS',None],
                                    ['InvMuonGradIso',None],
                                    ['Ptvarcone30pt0'+str(m),["MuonWeightAI"]],
                                    ['Tau'+str(trax[k])+'Track',["TauTotalWeight"]],
                                    ],
                                  )
		 
                        loop += ztautau.algs.algs.PlotAlg(
                                region   = 'AntiIsoCR_OS_'+str(triggers[i])+'med_lowPT_Tau'+str(trax[k])+'Track_Ptvarcone30pt0'+str(m),
                                plot_all = False,
                                cut_flow = [
                                    ['MTrans50',None],
                                    ['SumCosDPhi05',None],
                                    ['OS',None],
                                    ['HLTTau'+str(triggers[i])+'Med1TrackTwo',None],
                                    ['TauLowPt',["TauTotalWeight"]],
                                    ['InvMuonGradIso',None],
                                    ['Tau'+str(trax[k])+'Track',["TauTotalWeight"]],
                                    ['Ptvarcone30pt0'+str(m),["MuonWeightAI"]],
                                    ],
                                  )

                        loop += ztautau.algs.algs.PlotAlg(
                                region   = 'AntiIsoCR_OS_'+str(triggers[i])+'med_highPT_Tau'+str(trax[k])+'Track_Ptvarcone30pt0'+str(m),
                                plot_all = False,
                                cut_flow = [
                                    ['MTrans50',None],
                                    ['SumCosDPhi05',None],
                                    ['HLTTau'+str(triggers[i])+'Med1TrackTwo',None],
                                    ['OS',None],
                                    ['TauHighPt',["TauTotalWeight"]],
                                    ['Tau'+str(trax[k])+'Track',["TauTotalWeight"]],
                                    ['InvMuonGradIso',None],
                                    ['Ptvarcone30pt0'+str(m),["MuonWeightAI"]],
                                    ],
                                  )


                        loop += ztautau.algs.algs.PlotAlg(
                                region   = 'AntiIsoCR_SS_'+str(triggers[i])+'med_Tau'+str(trax[k])+'Track_Ptvarcone30pt0'+str(m),
                                plot_all = False,
                                cut_flow = [
                                    ['MTrans50',None],
                                    ['SumCosDPhi05',None],
                                    ['SS',None],
                                    ['Tau'+str(trax[k])+'Track',["TauTotalWeight"]],
                                    ['HLTTau'+str(triggers[i])+'Med1TrackTwo',None],
                                    ['InvMuonGradIso',None],
                                    ['Ptvarcone30pt0'+str(m),["MuonWeightAI"]],
                                    ],
                                  )
		 
                        loop += ztautau.algs.algs.PlotAlg(
                                region   = 'AntiIsoCR_SS_'+str(triggers[i])+'med_lowPT_Tau'+str(trax[k])+'Track_Ptvarcone30pt0'+str(m),
                                plot_all = False,
                                cut_flow = [
                                    ['MTrans50',None],
                                    ['Tau'+str(trax[k])+'Track',["TauTotalWeight"]],
                                    ['HLTTau'+str(triggers[i])+'Med1TrackTwo',None],
                                    ['SumCosDPhi05',None],
                                    ['SS',None],
                                    ['TauLowPt',["TauTotalWeight"]],
                                    ['InvMuonGradIso',None],
                                    ['Ptvarcone30pt0'+str(m),["MuonWeightAI"]],
                                    ],
                                  )

                        loop += ztautau.algs.algs.PlotAlg(
                                region   = 'AntiIsoCR_SS_'+str(triggers[i])+'med_highPT_Tau'+str(trax[k])+'Track_Ptvarcone30pt0'+str(m),
                                plot_all = False,
                                cut_flow = [
                                    ['MTrans50',None],
                                    ['Tau'+str(trax[k])+'Track',["TauTotalWeight"]],
                                    ['SumCosDPhi05',None],
                                    ['SS',None],
                                    ['TauHighPt',["TauTotalWeight"]],
                                    ['HLTTau'+str(triggers[i])+'Med1TrackTwo',None],
                                    ['InvMuonGradIso',None],
                                    ['Ptvarcone30pt0'+str(m),["MuonWeightAI"]],
                                    ],
                                  )
		    
                   

        for c in range(len(trigchains)):
        

                loop += ztautau.algs.algs.PlotAlg(
                        region   = 'AntiIsoCR_OS_'+str(trigchains[c])+'med_Ptvarcone30pt0'+str(m),
                        plot_all = False,
                        cut_flow = [
                            ['MTrans50',None],
                            ['HLTtau25perf'+str(trigchains[c]),None],
                            ['SumCosDPhi05',None],
                            ['OS',None],
                            ['InvMuonGradIso',None],
                            ['Ptvarcone30pt0'+str(m),["MuonWeightAI"]],
                            ],
                          )
     
                loop += ztautau.algs.algs.PlotAlg(
                        region   = 'AntiIsoCR_OS_'+str(trigchains[c])+'med_lowPT_Ptvarcone30pt0'+str(m),
                        plot_all = False,
                        cut_flow = [
                            ['MTrans50',None],
                            ['SumCosDPhi05',None],
                            ['OS',None],
                            ['HLTtau25perf'+str(trigchains[c]),None],
                            ['TauLowPt',["TauTotalWeight"]],
                            ['InvMuonGradIso',None],
                            ['Ptvarcone30pt0'+str(m),["MuonWeightAI"]],
                            ],
                          )

                loop += ztautau.algs.algs.PlotAlg(
                        region   = 'AntiIsoCR_OS_'+str(trigchains[c])+'med_highPT_Ptvarcone30pt0'+str(m),
                        plot_all = False,
                        cut_flow = [
                            ['MTrans50',None],
                            ['SumCosDPhi05',None],
                            ['HLTtau25perf'+str(trigchains[c]),None],
                            ['OS',None],
                            ['TauHighPt',["TauTotalWeight"]],
                            ['InvMuonGradIso',None],
                            ['Ptvarcone30pt0'+str(m),["MuonWeightAI"]],
                            ],
                          )

                loop += ztautau.algs.algs.PlotAlg(
                        region   = 'AntiIsoCR_SS_'+str(trigchains[c])+'med_Ptvarcone30pt0'+str(m),
                        plot_all = False,
                        cut_flow = [
                            ['MTrans50',None],
                            ['SumCosDPhi05',None],
                            ['SS',None],
                            ['HLTtau25perf'+str(trigchains[c]),None],
                            ['InvMuonGradIso',None],
                            ['Ptvarcone30pt0'+str(m),["MuonWeightAI"]],
                            ],
                          )
         
                loop += ztautau.algs.algs.PlotAlg(
                        region   = 'AntiIsoCR_SS_'+str(trigchains[c])+'med_lowPT_Ptvarcone30pt0'+str(m),
                        plot_all = False,
                        cut_flow = [
                            ['MTrans50',None],
                            ['HLTtau25perf'+str(trigchains[c]),None],
                            ['SumCosDPhi05',None],
                            ['SS',None],
                            ['TauLowPt',["TauTotalWeight"]],
                            ['InvMuonGradIso',None],
                            ['Ptvarcone30pt0'+str(m),["MuonWeightAI"]],
                            ],
                          )

                loop += ztautau.algs.algs.PlotAlg(
                        region   = 'AntiIsoCR_SS_'+str(trigchains[c])+'med_highPT_Ptvarcone30pt0'+str(m),
                        plot_all = False,
                        cut_flow = [
                            ['MTrans50',None],
                            ['SumCosDPhi05',None],
                            ['SS',None],
                            ['TauHighPt',["TauTotalWeight"]],
                            ['HLTtau25perf'+str(trigchains[c]),None],
                            ['InvMuonGradIso',None],
                            ['Ptvarcone30pt0'+str(m),["MuonWeightAI"]],
                            ],
                          )    
    
                for k in range(len(trax)):
    
                        loop += ztautau.algs.algs.PlotAlg(
                                region   = 'AntiIsoCR_OS_'+str(trigchains[c])+'med_Tau'+str(trax[k])+'Track_Ptvarcone30pt0'+str(m),
                                plot_all = False,
                                cut_flow = [
				    ['MTrans50',None],
                                    ['HLTtau25perf'+str(trigchains[c]),None],
                                    ['SumCosDPhi05',None],
                                    ['OS',None],
                                    ['InvMuonGradIso',None],
                                    ['Ptvarcone30pt0'+str(m),["MuonWeightAI"]],
                                    ['Tau'+str(trax[k])+'Track',["TauTotalWeight"]],
                                    ],
                                  )
		 
                        loop += ztautau.algs.algs.PlotAlg(
                                region   = 'AntiIsoCR_OS_'+str(trigchains[c])+'med_lowPT_Tau'+str(trax[k])+'Track_Ptvarcone30pt0'+str(m),
                                plot_all = False,
                                cut_flow = [
                                    ['MTrans50',None],
                                    ['SumCosDPhi05',None],
                                    ['OS',None],
                                    ['HLTtau25perf'+str(trigchains[c]),None],
                                    ['TauLowPt',["TauTotalWeight"]],
                                    ['InvMuonGradIso',None],
                                    ['Tau'+str(trax[k])+'Track',["TauTotalWeight"]],
                                    ['Ptvarcone30pt0'+str(m),["MuonWeightAI"]],
                                    ],
                                  )

                        loop += ztautau.algs.algs.PlotAlg(
                                region   = 'AntiIsoCR_OS_'+str(trigchains[c])+'med_highPT_Tau'+str(trax[k])+'Track_Ptvarcone30pt0'+str(m),
                                plot_all = False,
                                cut_flow = [
                                    ['MTrans50',None],
                                    ['SumCosDPhi05',None],
                                    ['HLTtau25perf'+str(trigchains[c]),None],
                                    ['OS',None],
                                    ['TauHighPt',["TauTotalWeight"]],
                                    ['Tau'+str(trax[k])+'Track',["TauTotalWeight"]],
                                    ['InvMuonGradIso',None],
                                    ['Ptvarcone30pt0'+str(m),["MuonWeightAI"]],
                                    ],
                                  )

                        loop += ztautau.algs.algs.PlotAlg(
                                region   = 'AntiIsoCR_SS_'+str(trigchains[c])+'med_Tau'+str(trax[k])+'Track_Ptvarcone30pt0'+str(m),
                                plot_all = False,
                                cut_flow = [
                                    ['MTrans50',None],
                                    ['SumCosDPhi05',None],
                                    ['SS',None],
                                    ['Tau'+str(trax[k])+'Track',["TauTotalWeight"]],
                                    ['HLTtau25perf'+str(trigchains[c]),None],
                                    ['InvMuonGradIso',None],
                                    ['Ptvarcone30pt0'+str(m),["MuonWeightAI"]],
                                    ],
                                  )
		 
                        loop += ztautau.algs.algs.PlotAlg(
                                region   = 'AntiIsoCR_SS_'+str(trigchains[c])+'med_lowPT_Tau'+str(trax[k])+'Track_Ptvarcone30pt0'+str(m),
                                plot_all = False,
                                cut_flow = [
                                    ['MTrans50',None],
                                    ['Tau'+str(trax[k])+'Track',["TauTotalWeight"]],
                                    ['HLTtau25perf'+str(trigchains[c]),None],
                                    ['SumCosDPhi05',None],
                                    ['SS',None],
                                    ['TauLowPt',["TauTotalWeight"]],
                                    ['InvMuonGradIso',None],
                                    ['Ptvarcone30pt0'+str(m),["MuonWeightAI"]],
                                    ],
                                  )

                        loop += ztautau.algs.algs.PlotAlg(
                                region   = 'AntiIsoCR_SS_'+str(trigchains[c])+'med_highPT_Tau'+str(trax[k])+'Track_Ptvarcone30pt0'+str(m),
                                plot_all = False,
                                cut_flow = [
                                    ['MTrans50',None],
                                    ['Tau'+str(trax[k])+'Track',["TauTotalWeight"]],
                                    ['SumCosDPhi05',None],
                                    ['SS',None],
                                    ['TauHighPt',["TauTotalWeight"]],
                                    ['HLTtau25perf'+str(trigchains[c]),None],
                                    ['InvMuonGradIso',None],
                                    ['Ptvarcone30pt0'+str(m),["MuonWeightAI"]],
                                    ],
                                  )
		    
                   
             
        m  += 1
   
   
    """ 
    ############ # KW SYSTEMATICS
    """ 
    namekw = [625,675,725,775,825,875,925,975,1025,1075]
    for i in range(len(namekw)):

        loop += ztautau.algs.algs.PlotAlg(
                region    = 'Wjets_SS_MTrans'+str(namekw[i]),
                plot_all  = False,
                cut_flow  = [
                    ['MTrans'+str(namekw[i]),None],
                    ['MET30',None],
                    ['SS',None],
              	    ['MuonGradIso',["MuonTotalWeight"]],
              	    ],
            	  ) 
    
        loop += ztautau.algs.algs.PlotAlg(
              	region    = 'Wjets_OS_MTrans'+str(namekw[i]),
            	plot_all  = False,
            	cut_flow  = [
              	    ['MTrans'+str(namekw[i]),None],
                    ['MET30',None],
              	    ['OS',None],
              	    ['MuonGradIso',["MuonTotalWeight"]],
              	    ],
            	  ) 

        loop += ztautau.algs.algs.PlotAlg(
            	region    = 'Wjets_OS_MTrans'+str(namekw[i])+'_highPT',
            	plot_all  = False,
            	cut_flow  = [
              	    ['MTrans60',None],
              	    ['MTrans'+str(namekw[i]),None],
              	    ['MET30',None],
              	    ['OS',None],
              	    ['MuonGradIso',["MuonTotalWeight"]],
              	    ['TauHighPt',["TauTotalWeight"]],
              	    ],
            	  )


        loop += ztautau.algs.algs.PlotAlg(
            	region    = 'Wjets_OS_MTrans'+str(namekw[i])+'_lowPT',
            	plot_all  = False,
            	cut_flow  = [
              	    ['MTrans60',None],
              	    ['MET30',None],
              	    ['OS',None],
             	    ['MTrans'+str(namekw[i]),None],
              	    ['MuonGradIso',["MuonTotalWeight"]],
              	    ['TauLowPt',["TauTotalWeight"]],
              	    ],
            	  )


        loop += ztautau.algs.algs.PlotAlg(
            	region    = 'Wjets_SS_MTrans'+str(namekw[i])+'_highPT',
            	plot_all  = False,
            	cut_flow  = [
              	    ['MTrans60',None],
              	    ['MTrans'+str(namekw[i]),None],
              	    ['MET30',None],
              	    ['SS',None],
              	    ['MuonGradIso',["MuonTotalWeight"]],
              	    ['TauHighPt',None],
              	    ],
            	  )

        loop += ztautau.algs.algs.PlotAlg(
            	region    = 'Wjets_SS_MTrans'+str(namekw[i])+'_lowPT',
            	plot_all  = False,
            	cut_flow  = [
              	    ['MTrans60',None],
              	    ['MET30',None],
              	    ['MTrans'+str(namekw[i]),None],
              	    ['SS',None],
              	    ['MuonGradIso',["MuonTotalWeight"]],
              	    ['TauLowPt',["TauTotalWeight"]],
              	    ],
            	  )

        for k in range(len(triggers)):

		  loop += ztautau.algs.algs.PlotAlg(
			  region    = 'Wjets_OS_MTrans'+str(namekw[i])+'_'+str(triggers[k])+'med',
			  plot_all  = False,
			  cut_flow  = [
			      ['MTrans60',None],
			      ['MTrans'+str(namekw[i]),None],
			      ['MET30',None],
			      ['OS',None],
			      ['MuonGradIso',["MuonTotalWeight"]],
			      ['HLTTau'+str(triggers[k])+'Med1TrackTwo',None],
			      ],
		   	    ) 

		  loop += ztautau.algs.algs.PlotAlg(
			  region    = 'Wjets_OS_MTrans'+str(namekw[i])+'_'+str(triggers[k])+'med_lowPT',
			  plot_all  = False,
			  cut_flow  = [
			      ['MTrans60',None],
			      ['MET30',None],
			      ['MTrans'+str(namekw[i]),None],
			      ['OS',None],
			      ['MuonGradIso',["MuonTotalWeight"]],
			      ['HLTTau'+str(triggers[k])+'Med1TrackTwo',None],
			      ['TauLowPt',None],
			      ],
			    )

		  loop += ztautau.algs.algs.PlotAlg(
			  region    = 'Wjets_OS_MTrans'+str(namekw[i])+'_'+str(triggers[k])+'med_highPT',
			  plot_all  = False,
			  cut_flow  = [
			      ['MTrans60',None],
			      ['MET30',None],
			      ['OS',None],
			      ['MTrans'+str(namekw[i]),None],
			      ['MuonGradIso',["MuonTotalWeight"]],
			      ['HLTTau'+str(triggers[k])+'Med1TrackTwo',None],
			      ['TauHighPt',None],
			      ],
			    )

		  loop += ztautau.algs.algs.PlotAlg(
			  region    = 'Wjets_SS_MTrans'+str(namekw[i])+'_'+str(triggers[k])+'med',
			  plot_all  = False,
			  cut_flow  = [
			      ['MTrans60',None],
			      ['MET30',None],
			      ['SS',None],
			      ['MTrans'+str(namekw[i]),None],
			      ['MuonGradIso',["MuonTotalWeight"]],
			      ['HLTTau'+str(triggers[k])+'Med1TrackTwo',None],
			      ],
			    ) 

		  loop += ztautau.algs.algs.PlotAlg(
			  region    = 'Wjets_SS_MTrans'+str(namekw[i])+'_'+str(triggers[k])+'med_lowPT',
			  plot_all  = False,
			  cut_flow  = [
			      ['MTrans60',None],
			      ['MET30',None],
			      ['SS',None],
			      ['MTrans'+str(namekw[i]),None],
			      ['MuonGradIso',["MuonTotalWeight"]],
			      ['HLTTau'+str(triggers[k])+'Med1TrackTwo',None],
			      ['TauLowPt',None],
			      ],
			    )
    
		  loop += ztautau.algs.algs.PlotAlg(
			  region    = 'Wjets_SS_MTrans'+str(namekw[i])+'_'+str(triggers[k])+'med_highPT',
			  plot_all  = False,
			  cut_flow  = [
			      ['MTrans60',None],
			      ['MET30',None],
			      ['SS',None],
			      ['MTrans'+str(namekw[i]),None],
			      ['MuonGradIso',["MuonTotalWeight"]],
			      ['HLTTau'+str(triggers[k])+'Med1TrackTwo',None],
			      ['TauHighPt',None],
			      ],
			    )
        for c in range(len(trigchains)):

		  loop += ztautau.algs.algs.PlotAlg(
			  region    = 'Wjets_OS_MTrans'+str(namekw[i])+'_'+str(trigchains[c])+'med',
			  plot_all  = False,
			  cut_flow  = [
			      ['MTrans60',None],
			      ['MTrans'+str(namekw[i]),None],
			      ['MET30',None],
			      ['OS',None],
			      ['MuonGradIso',["MuonTotalWeight"]],
			      ['HLTtau25perf'+str(trigchains[c]),None],
			      ],
		   	    ) 

		  loop += ztautau.algs.algs.PlotAlg(
			  region    = 'Wjets_OS_MTrans'+str(namekw[i])+'_'+str(trigchains[c])+'med_lowPT',
			  plot_all  = False,
			  cut_flow  = [
			      ['MTrans60',None],
			      ['MET30',None],
			      ['MTrans'+str(namekw[i]),None],
			      ['OS',None],
			      ['MuonGradIso',["MuonTotalWeight"]],
			      ['HLTtau25perf'+str(trigchains[c]),None],
			      ['TauLowPt',None],
			      ],
			    )

		  loop += ztautau.algs.algs.PlotAlg(
			  region    = 'Wjets_OS_MTrans'+str(namekw[i])+'_'+str(trigchains[c])+'med_highPT',
			  plot_all  = False,
			  cut_flow  = [
			      ['MTrans60',None],
			      ['MET30',None],
			      ['OS',None],
			      ['MTrans'+str(namekw[i]),None],
			      ['MuonGradIso',["MuonTotalWeight"]],
			      ['HLTtau25perf'+str(trigchains[c]),None],
			      ['TauHighPt',None],
			      ],
			    )

		  loop += ztautau.algs.algs.PlotAlg(
			  region    = 'Wjets_SS_MTrans'+str(namekw[i])+'_'+str(trigchains[c])+'med',
			  plot_all  = False,
			  cut_flow  = [
			      ['MTrans60',None],
			      ['MET30',None],
			      ['SS',None],
			      ['MTrans'+str(namekw[i]),None],
			      ['MuonGradIso',["MuonTotalWeight"]],
			      ['HLTtau25perf'+str(trigchains[c]),None],
			      ],
			    ) 

		  loop += ztautau.algs.algs.PlotAlg(
			  region    = 'Wjets_SS_MTrans'+str(namekw[i])+'_'+str(trigchains[c])+'med_lowPT',
			  plot_all  = False,
			  cut_flow  = [
			      ['MTrans60',None],
			      ['MET30',None],
			      ['SS',None],
			      ['MTrans'+str(namekw[i]),None],
			      ['MuonGradIso',["MuonTotalWeight"]],
			      ['HLTtau25perf'+str(trigchains[c]),None],
			      ['TauLowPt',None],
			      ],
			    )
    
		  loop += ztautau.algs.algs.PlotAlg(
			  region    = 'Wjets_SS_MTrans'+str(namekw[i])+'_'+str(trigchains[c])+'med_highPT',
			  plot_all  = False,
			  cut_flow  = [
			      ['MTrans60',None],
			      ['MET30',None],
			      ['SS',None],
			      ['MTrans'+str(namekw[i]),None],
			      ['MuonGradIso',["MuonTotalWeight"]],
			      ['HLTtau25perf'+str(trigchains[c]),None],
			      ['TauHighPt',None],
			      ],
			    )


        for j in range(len(trax)):
		  
		  loop += ztautau.algs.algs.PlotAlg(
			  region    = 'Wjets_OS_MTrans'+str(namekw[i])+'_Tau'+str(trax[j])+'Track',
			  plot_all  = False,
			  cut_flow  = [
			      ['MTrans60',None],
			      ['MET30',None],
			      ['OS',None],
			      ['MTrans'+str(namekw[i]),None],
			      ['MuonGradIso',["MuonTotalWeight"]],
			      ['Tau'+str(trax[j])+'Track',["TauTotalWeight"]],
			      ],
			    ) 
    
		  loop += ztautau.algs.algs.PlotAlg(
			  region    = 'Wjets_OS_MTrans'+str(namekw[i])+'_lowPT_Tau'+str(trax[j])+'Track',
			  plot_all  = False,
			  cut_flow  = [
			      ['MTrans60',None],
			      ['MET30',None],
			      ['OS',None],
			      ['MTrans'+str(namekw[i]),None],
			      ['Tau'+str(trax[j])+'Track',["TauTotalWeight"]],
			      ['MuonGradIso',["MuonTotalWeight"]],
			      ['TauLowPt',None],
			      ],
			    )

		  loop += ztautau.algs.algs.PlotAlg(
			  region    = 'Wjets_OS_MTrans'+str(namekw[i])+'_highPT_Tau'+str(trax[j])+'Track',
			  plot_all  = False,
			  cut_flow  = [
			      ['MTrans60',None],
			      ['MET30',None],
			      ['OS',None],
			      ['MTrans'+str(namekw[i]),None],
			      ['MuonGradIso',["MuonTotalWeight"]],
			      ['Tau'+str(trax[j])+'Track',["TauTotalWeight"]],
			      ['TauHighPt',None],
			      ],
			    )

		  loop += ztautau.algs.algs.PlotAlg(
			  region    = 'Wjets_SS_MTrans'+str(namekw[i])+'_Tau'+str(trax[j])+'Track',
			  plot_all  = False,
			  cut_flow  = [
			      ['MTrans60',None],
			      ['MET30',None],
			      ['SS',None],
			      ['MTrans'+str(namekw[i]),None],
			      ['MuonGradIso',["MuonTotalWeight"]],
			      ['Tau'+str(trax[j])+'Track',["TauTotalWeight"]],
			      ],
			    ) 

		  loop += ztautau.algs.algs.PlotAlg(
			  region    = 'Wjets_SS_MTrans'+str(namekw[i])+'_lowPT_Tau'+str(trax[j])+'Track',
			  plot_all  = False,
			  cut_flow  = [
			      ['MTrans60',None],
			      ['MET30',None],
			      ['SS',None],
			      ['MTrans'+str(namekw[i]),None],
			      ['MuonGradIso',["MuonTotalWeight"]],
			      ['Tau'+str(trax[j])+'Track',["TauTotalWeight"]],
			      ['TauLowPt',None],
			      ],
			    )

		  loop += ztautau.algs.algs.PlotAlg(
			  region    = 'Wjets_SS_MTrans'+str(namekw[i])+'_highPT_Tau'+str(trax[j])+'Track',
			  plot_all  = False,
			  cut_flow  = [
			      ['MTrans60',None],
			      ['MET30',None],
			      ['SS',None],
			      ['MTrans'+str(namekw[i]),None],
			      ['MuonGradIso',["MuonTotalWeight"]],
			      ['Tau'+str(trax[j])+'Track',["TauTotalWeight"]],
			      ['TauHighPt',None],
			      ],
			    )
		
		  for l in range(len(triggers)):

		  	  loop += ztautau.algs.algs.PlotAlg(
				  region    = 'Wjets_OS_MTrans'+str(namekw[i])+'_'+str(triggers[l])+'med_Tau'+str(trax[j])+'Track',
				  plot_all  = False,
				  cut_flow  = [
				      ['MTrans60',None],
				      ['MET30',None],
				      ['OS',None],
				      ['MTrans'+str(namekw[i]),None],
			              ['MuonGradIso',["MuonTotalWeight"]],
				      ['HLTTau'+str(triggers[l])+'Med1TrackTwo',None],			
				      ['Tau'+str(trax[j])+'Track',["TauTotalWeight"]],
				      ],
				    ) 
			 
			  loop += ztautau.algs.algs.PlotAlg(
				  region    = 'Wjets_OS_MTrans'+str(namekw[i])+'_'+str(triggers[l])+'med_lowPT_Tau'+str(trax[j])+'Track',
				  plot_all  = False,
				  cut_flow  = [
				      ['MTrans60',None],
				      ['MET30',None],
				      ['OS',None],
				      ['HLTTau'+str(triggers[l])+'Med1TrackTwo',None],
				      ['MTrans'+str(namekw[i]),None],
				      ['MuonGradIso',["MuonTotalWeight"]],
				      ['Tau'+str(trax[j])+'Track',["TauTotalWeight"]],
				      ['TauLowPt',None],
				      ],
				    )

			  loop += ztautau.algs.algs.PlotAlg(
				  region    = 'Wjets_OS_MTrans'+str(namekw[i])+'_'+str(triggers[l])+'med_highPT_Tau'+str(trax[j])+'Track',
				  plot_all  = False,
				  cut_flow  = [
				      ['MTrans60',None],
				      ['MET30',None],
				      ['OS',None],
				      ['HLTTau'+str(triggers[l])+'Med1TrackTwo',None],				     
				      ['MTrans'+str(namekw[i]),None],
				      ['MuonGradIso',["MuonTotalWeight"]],
				      ['Tau'+str(trax[j])+'Track',["TauTotalWeight"]],
				      ['TauHighPt',None],
				      ],
				    )

			  loop += ztautau.algs.algs.PlotAlg(
				  region    = 'Wjets_SS_MTrans'+str(namekw[i])+'_'+str(triggers[l])+'med_Tau'+str(trax[j])+'Track',
				  plot_all  = False,
				  cut_flow  = [
				      ['MTrans60',None],
				      ['MET30',None],
				      ['SS',None],
				      ['HLTTau'+str(triggers[l])+'Med1TrackTwo',None],				     
				      ['MTrans'+str(namekw[i]),None],
				      ['MuonGradIso',["MuonTotalWeight"]],
				      ['Tau'+str(trax[j])+'Track',["TauTotalWeight"]],
				      ],
				    ) 

			  loop += ztautau.algs.algs.PlotAlg(
				  region    = 'Wjets_SS_MTrans'+str(namekw[i])+'_'+str(triggers[l])+'med_lowPT_Tau'+str(trax[j])+'Track',
				  plot_all  = False,
				  cut_flow  = [
				      ['MTrans60',None],
				      ['MET30',None],
				      ['SS',None],
				      ['MTrans'+str(namekw[i]),None],
				      ['MuonGradIso',["MuonTotalWeight"]],
				      ['HLTTau'+str(triggers[l])+'Med1TrackTwo',None],				     
				      ['Tau'+str(trax[j])+'Track',["TauTotalWeight"]],
				      ['TauLowPt',None],
				      ],
				    )

			  loop += ztautau.algs.algs.PlotAlg(
				  region    = 'Wjets_SS_MTrans'+str(namekw[i])+'_'+str(triggers[l])+'med_highPT_Tau'+str(trax[j])+'Track',
				  plot_all  = False,
				  cut_flow  = [
				      ['MTrans60',None],
				      ['MET30',None],
				      ['HLTTau'+str(triggers[l])+'Med1TrackTwo',None],				     
			              ['SS',None],
				      ['MTrans'+str(namekw[i]),None],
				      ['MuonGradIso',["MuonTotalWeight"]],
				      ['Tau'+str(trax[j])+'Track',["TauTotalWeight"]],
				      ['TauHighPt',None],
				      ],
				    )
     
		  for c in range(len(trigchains)):

			  loop += ztautau.algs.algs.PlotAlg(
				  region    = 'Wjets_OS_MTrans'+str(namekw[i])+'_'+str(trigchains[c])+'med'+str(trax[j])+'Track',
				  plot_all  = False,
				  cut_flow  = [
				      ['MTrans60',None],
				      ['Tau'+str(trax[j])+'Track',["TauTotalWeight"]],
				      ['MTrans'+str(namekw[i]),None],
				      ['MET30',None],
				      ['OS',None],
				      ['MuonGradIso',["MuonTotalWeight"]],
				      ['HLTtau25perf'+str(trigchains[c]),None],
				      ],
				    ) 

			  loop += ztautau.algs.algs.PlotAlg(
				  region    = 'Wjets_OS_MTrans'+str(namekw[i])+'_'+str(trigchains[c])+'med_lowPT'+str(trax[j])+'Track',
				  plot_all  = False,
				  cut_flow  = [
				      ['MTrans60',None],
				      ['Tau'+str(trax[j])+'Track',["TauTotalWeight"]],
				      ['MET30',None],
				      ['MTrans'+str(namekw[i]),None],
				      ['OS',None],
				      ['MuonGradIso',["MuonTotalWeight"]],
				      ['HLTtau25perf'+str(trigchains[c]),None],
				      ['TauLowPt',None],
				      ],
				    )

			  loop += ztautau.algs.algs.PlotAlg(
				  region    = 'Wjets_OS_MTrans'+str(namekw[i])+'_'+str(trigchains[c])+'med_highPT'+str(trax[j])+'Track',
				  plot_all  = False,
				  cut_flow  = [
				      ['MTrans60',None],
				      ['MET30',None],
				      ['OS',None],
				      ['MTrans'+str(namekw[i]),None],
				      ['MuonGradIso',["MuonTotalWeight"]],
				      ['HLTtau25perf'+str(trigchains[c]),None],
				      ['Tau'+str(trax[j])+'Track',["TauTotalWeight"]],
				      ['TauHighPt',None],
				      ],
				    )

			  loop += ztautau.algs.algs.PlotAlg(
				  region    = 'Wjets_SS_MTrans'+str(namekw[i])+'_'+str(trigchains[c])+'med'+str(trax[j])+'Track',
				  plot_all  = False,
				  cut_flow  = [
				      ['MTrans60',None],
				      ['MET30',None],
				      ['SS',None],
				      ['MTrans'+str(namekw[i]),None],
				      ['Tau'+str(trax[j])+'Track',["TauTotalWeight"]],
				      ['MuonGradIso',["MuonTotalWeight"]],
				      ['HLTtau25perf'+str(trigchains[c]),None],
				      ],
				    ) 

			  loop += ztautau.algs.algs.PlotAlg(
				  region    = 'Wjets_SS_MTrans'+str(namekw[i])+'_'+str(trigchains[c])+'med_lowPT'+str(trax[j])+'Track',
				  plot_all  = False,
				  cut_flow  = [
				      ['MTrans60',None],
				      ['MET30',None],
				      ['SS',None],
				      ['Tau'+str(trax[j])+'Track',["TauTotalWeight"]],
				      ['MTrans'+str(namekw[i]),None],
				      ['MuonGradIso',["MuonTotalWeight"]],
				      ['HLTtau25perf'+str(trigchains[c]),None],
				      ['TauLowPt',None],
				      ],
				    )
	    
			  loop += ztautau.algs.algs.PlotAlg(
				  region    = 'Wjets_SS_MTrans'+str(namekw[i])+'_'+str(trigchains[c])+'med_highPT'+str(trax[j])+'Track',
				  plot_all  = False,
				  cut_flow  = [
				      ['MTrans60',None],
				      ['MET30',None],
				      ['SS',None],
				      ['MTrans'+str(namekw[i]),None],
				      ['Tau'+str(trax[j])+'Track',["TauTotalWeight"]],
				      ['MuonGradIso',["MuonTotalWeight"]],
				      ['HLTtau25perf'+str(trigchains[c]),None],
				      ['TauHighPt',None],
				      ],
				    )
    """
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



