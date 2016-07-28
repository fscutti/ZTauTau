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

#GeV = 1000.0


#_____________________________________________________________________________
def analyze(config):
  
    ##-------------------------------------------------------------------------
    ## setup
    ##-------------------------------------------------------------------------
    config['tree']       = 'NOMINAL'
    config['do_var_log'] = True
    main_path = os.getenv('MAIN')
    
    ## build chain
    chain = ROOT.TChain(config['tree'])
    for fn in config['input']: chain.Add(fn)

    ##-------------------------------------------------------------------------
    ## systematics 
    ##-------------------------------------------------------------------------
    """
    pass systematics on the command line like this:
    python j.plotter.py --config="sys:SYS_UP"
    """
    config.setdefault('sys',None)
    systematic = config['sys']

    sys_somesys    = None

    if   systematic == None: pass
    elif systematic == 'SOMESYS_UP':      sys_somesys    = 'up'
    elif systematic == 'SOMESYS_DN':      sys_somesys    = 'dn'
    else: 
        assert False, "Invalid systematic %s!"%(systematic)


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
    #loop += ztautau.algs.weights.Pileup(cutflow='presel',key='weight_pileup')
    loop += ztautau.algs.weights.WeightTotal(cutflow='presel',key='weight_total')
   
    ## cuts
    ## +++++++++++++++++++++++++++++++++++++++

    #---- BASE CUT ----#   

    loop += ztautau.algs.algs.CutAlg(cutflow='presel',cut='OneMuon')
    loop += ztautau.algs.algs.CutAlg(cutflow='presel',cut='NoElectrons')
    loop += ztautau.algs.algs.CutAlg(cutflow='presel',cut='AtLeastOneTau')
    loop += ztautau.algs.algs.CutAlg(cutflow='presel',cut='NoBJets')
    loop += ztautau.algs.algs.CutAlg(cutflow='presel',cut='AtLeastOnePvx')
    #loop += ztautau.algs.algs.CutAlg(cutflow='presel',cut='MuonHLTmu20ilooseL1MU15ORmu50') #2015
    loop += ztautau.algs.algs.CutAlg(cutflow='presel',cut='MuonHLTmu24imediumORHLTmu50') #2016
    #loop += ztautau.algs.algs.CutAlg(cutflow='presel',cut='MuonMuTrigMatch0HLTmu20ilooseL1MU15')

    #---- MUONS ----#

    loop += ztautau.algs.algs.CutAlg(cutflow='presel',cut='MuonIdMedium')
    #loop += ztautau.algs.algs.CutAlg(cutflow='presel',cut='MuonPt22') #2015
    loop += ztautau.algs.algs.CutAlg(cutflow='presel',cut='MuonPt26') #2016
    loop += ztautau.algs.algs.CutAlg(cutflow='presel',cut='MuonEta25')

    #---- TAUS ----#

    loop += ztautau.algs.algs.CutAlg(cutflow='presel',cut='TauPt25')
    loop += ztautau.algs.algs.CutAlg(cutflow='presel',cut='TauEta247')
    loop += ztautau.algs.algs.CutAlg(cutflow='presel',cut='TauCharge1')
    loop += ztautau.algs.algs.CutAlg(cutflow='presel',cut='TauTrack')
    loop += ztautau.algs.algs.CutAlg(cutflow='presel',cut='BDTtauMed')

    
    ## weights configuration
    ## ---------------------------------------
    ## event
    ## +++++++++++++++++++++++++++++++++++++++
    loop += ztautau.algs.weights.MuonSF(
            key='MuonTotalWeight',
            scale=None,
            )
    loop += ztautau.algs.weights.MuonSFIsoGrad(
            key='MuonWeightAI',
            scale=None,
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

#-----------------------------#
#       THREE TRACK TAU
#-----------------------------#

    loop += ztautau.algs.algs.PlotAlg(
            region    = 'Wjets_OS_highPT_Tau3Track',
            plot_all  = False,
            cut_flow  = [
              ['MTrans60',None],
              ['MET30',None],
              ['OS',None],
              ['MuonGradIso',["MuonTotalWeight"]],
              #['MuonGradIso',["MuonTotalWeight"]],
	      ['TauHighPt',None],
       	      ['Tau3Track',None],
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
	      ['Tau3Track',None],
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
       	      ['Tau3Track',None],
              ],
            )

    loop += ztautau.algs.algs.PlotAlg(
            region    = 'Wjets_OS_25med_Tau3Track',
            plot_all  = False,
            cut_flow  = [
              ['MTrans60',None],
              ['MET30',None],
              ['OS',None],
              ['MuonGradIso',["MuonTotalWeight"]],
	      ['HLTTau25Med1TrackTwo',None],
       	      ['Tau3Track',None],
              ],
            )

    loop += ztautau.algs.algs.PlotAlg(
            region    = 'Wjets_OS_35med_Tau3Track',
            plot_all  = False,
            cut_flow  = [
              ['MTrans60',None],
              ['MET30',None],
              ['OS',None],
              ['MuonGradIso',["MuonTotalWeight"]],
	      ['HLTTau35Med1TrackTwo',None],
       	      ['Tau3Track',None],
              ],
            )


    loop += ztautau.algs.algs.PlotAlg(
            region    = 'Wjets_OS_25med_lowPT_Tau3Track',
            plot_all  = False,
            cut_flow  = [
              ['MTrans60',None],
              ['MET30',None],
              ['OS',None],
              ['MuonGradIso',["MuonTotalWeight"]],
	      ['HLTTau25Med1TrackTwo',None],
       	      ['Tau3Track',None],
	      ['TauLowPt',None],
              ],
            )

    loop += ztautau.algs.algs.PlotAlg(
            region    = 'Wjets_OS_35med_lowPT_Tau3Track',
            plot_all  = False,
            cut_flow  = [
              ['MTrans60',None],
              ['MET30',None],
              ['OS',None],
              ['MuonGradIso',["MuonTotalWeight"]],
	      ['HLTTau35Med1TrackTwo',None],
       	      ['Tau3Track',None],
	      ['TauLowPt',None],
              ],
            )


    loop += ztautau.algs.algs.PlotAlg(
            region    = 'Wjets_OS_25med_highPT_Tau3Track',
            plot_all  = False,
            cut_flow  = [
              ['MTrans60',None],
              ['MET30',None],
              ['OS',None],
              ['MuonGradIso',["MuonTotalWeight"]],
	      ['HLTTau25Med1TrackTwo',None],
       	      ['Tau3Track',None],
	      ['TauHighPt',None],
              ],
            )


    loop += ztautau.algs.algs.PlotAlg(
            region    = 'Wjets_OS_35med_highPT_Tau3Track',
            plot_all  = False,
            cut_flow  = [
              ['MTrans60',None],
              ['MET30',None],
              ['OS',None],
              ['MuonGradIso',["MuonTotalWeight"]],
	      ['HLTTau35Med1TrackTwo',None],
       	      ['Tau3Track',None],
	      ['TauHighPt',None],
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
       	      ['Tau3Track',None],
              ],
            )

    loop += ztautau.algs.algs.PlotAlg(
            region    = 'Wjets_SS_25med_Tau3Track',
            plot_all  = False,
            cut_flow  = [
              ['MTrans60',None],
              ['MET30',None],
              ['SS',None],
              ['MuonGradIso',["MuonTotalWeight"]],
	      ['HLTTau25Med1TrackTwo',None],
       	      ['Tau3Track',None],
              ],
            )

    loop += ztautau.algs.algs.PlotAlg(
            region    = 'Wjets_SS_35med_Tau3Track',
            plot_all  = False,
            cut_flow  = [
              ['MTrans60',None],
              ['MET30',None],
              ['SS',None],
              ['MuonGradIso',["MuonTotalWeight"]],
	      ['HLTTau35Med1TrackTwo',None],
       	      ['Tau3Track',None],
              ],
            )


    loop += ztautau.algs.algs.PlotAlg(
            region    = 'Wjets_SS_25med_lowPT_Tau3Track',
            plot_all  = False,
            cut_flow  = [
              ['MTrans60',None],
              ['MET30',None],
              ['SS',None],
              ['MuonGradIso',["MuonTotalWeight"]],
	      ['HLTTau25Med1TrackTwo',None],
       	      ['Tau3Track',None],
	      ['TauLowPt',None],
              ],
            )

    loop += ztautau.algs.algs.PlotAlg(
            region    = 'Wjets_SS_35med_lowPT_Tau3Track',
            plot_all  = False,
            cut_flow  = [
              ['MTrans60',None],
              ['MET30',None],
              ['SS',None],
              ['MuonGradIso',["MuonTotalWeight"]],
	      ['HLTTau35Med1TrackTwo',None],
       	      ['Tau3Track',None],
	      ['TauLowPt',None],
              ],
            )


    loop += ztautau.algs.algs.PlotAlg(
            region    = 'Wjets_SS_25med_highPT_Tau3Track',
            plot_all  = False,
            cut_flow  = [
              ['MTrans60',None],
              ['MET30',None],
              ['SS',None],
              ['MuonGradIso',["MuonTotalWeight"]],
	      ['HLTTau25Med1TrackTwo',None],
       	      ['Tau3Track',None],
	      ['TauHighPt',None],
              ],
            )

    loop += ztautau.algs.algs.PlotAlg(
            region    = 'Wjets_SS_35med_highPT_Tau3Track',
            plot_all  = False,
            cut_flow  = [
              ['MTrans60',None],
              ['MET30',None],
              ['SS',None],
              ['MuonGradIso',["MuonTotalWeight"]],
	      ['HLTTau35Med1TrackTwo',None],
       	      ['Tau3Track',None],
	      ['TauHighPt',None],
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
       	      ['Tau3Track',None],
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
       	      ['Tau3Track',None],
              ],
            )

    loop += ztautau.algs.algs.PlotAlg(
            region    = 'SR_25med_Tau3Track',
            plot_all  = False,
            cut_flow  = [
              ['MTrans50',None],
              ['SumCosDPhi05',None],
              ['MuonGradIso',["MuonTotalWeight"]],
              ['VisMass4580',None],
              ['OS',None],
	      ['HLTTau25Med1TrackTwo',None],
       	      ['Tau3Track',None],
              ],
            )

    loop += ztautau.algs.algs.PlotAlg(
            region    = 'SR_25med_lowPT_Tau3Track',
            plot_all  = False,
            cut_flow  = [
              ['MTrans50',None],
              ['SumCosDPhi05',None],
              ['MuonGradIso',["MuonTotalWeight"]],
              ['VisMass4580',None],
              ['OS',None],
	      ['HLTTau25Med1TrackTwo',None],
       	      ['Tau3Track',None],
              ['TauLowPt',None],
              ],
            )

    loop += ztautau.algs.algs.PlotAlg(
            region    = 'SR_25med_highPT_Tau3Track',
            plot_all  = False,
            cut_flow  = [
              ['MTrans50',None],
              ['SumCosDPhi05',None],
              ['MuonGradIso',["MuonTotalWeight"]],
              ['VisMass4580',None],
              ['OS',None],
	      ['HLTTau25Med1TrackTwo',None],
       	      ['Tau3Track',None],
              ['TauHighPt',None],
              ],
            )


    loop += ztautau.algs.algs.PlotAlg(
            region    = 'SR_35med_Tau3Track',
            plot_all  = False,
            cut_flow  = [
              ['MTrans50',None],
              ['SumCosDPhi05',None],
              ['MuonGradIso',["MuonTotalWeight"]],
              ['VisMass4580',None],
              ['OS',None],
	      ['HLTTau35Med1TrackTwo',None],
       	      ['Tau3Track',None],
              ],
            )

    loop += ztautau.algs.algs.PlotAlg(
            region    = 'SR_35med_lowPT_Tau3Track',
            plot_all  = False,
            cut_flow  = [
              ['MTrans50',None],
              ['SumCosDPhi05',None],
              ['MuonGradIso',["MuonTotalWeight"]],
              ['VisMass4580',None],
              ['OS',None],
	      ['HLTTau35Med1TrackTwo',None],
       	      ['Tau3Track',None],
              ['TauLowPt',None],
              ],
            )

    loop += ztautau.algs.algs.PlotAlg(
            region    = 'SR_35med_highPT_Tau3Track',
            plot_all  = False,
            cut_flow  = [
              ['MTrans50',None],
              ['SumCosDPhi05',None],
              ['MuonGradIso',["MuonTotalWeight"]],
              ['VisMass4580',None],
              ['OS',None],
	      ['HLTTau35Med1TrackTwo',None],
       	      ['Tau3Track',None],
              ['TauHighPt',None],
              ],
            )


    loop += ztautau.algs.algs.PlotAlg(
            region    = 'SR_Tau3Track',
            plot_all  = False,
            cut_flow  = [
              ['MTrans50',None],
              ['SumCosDPhi05',None],
              ['MuonGradIso',["MuonTotalWeight"]],
              ['VisMass4580',None],
              ['OS',None],
       	      ['Tau3Track',None],
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
       	      ['Tau3Track',None],
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
       	      ['Tau3Track',None],
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
       	      ['Tau3Track',None],
              ],
            )

    loop += ztautau.algs.algs.PlotAlg(
            region    = 'SR_SS_25med_Tau3Track',
            plot_all  = False,
            cut_flow  = [
              ['MTrans50',None],
              ['SumCosDPhi05',None],
              ['MuonGradIso',["MuonTotalWeight"]],
              ['VisMass4580',None],
              ['SS',None],
	      ['HLTTau25Med1TrackTwo',None],
       	      ['Tau3Track',None],
              ],
            )

    loop += ztautau.algs.algs.PlotAlg(
            region    = 'SR_SS_25med_lowPT_Tau3Track',
            plot_all  = False,
            cut_flow  = [
              ['MTrans50',None],
              ['SumCosDPhi05',None],
              ['MuonGradIso',["MuonTotalWeight"]],
              ['VisMass4580',None],
              ['SS',None],
	      ['HLTTau25Med1TrackTwo',None],
       	      ['Tau3Track',None],
              ['TauLowPt',None],
              ],
            )

    loop += ztautau.algs.algs.PlotAlg(
            region    = 'SR_SS_25med_highPT_Tau3Track',
            plot_all  = False,
            cut_flow  = [
              ['MTrans50',None],
              ['SumCosDPhi05',None],
              ['MuonGradIso',["MuonTotalWeight"]],
              ['VisMass4580',None],
              ['SS',None],
	      ['HLTTau25Med1TrackTwo',None],
       	      ['Tau3Track',None],
              ['TauHighPt',None],
              ],
            )

    loop += ztautau.algs.algs.PlotAlg(
            region    = 'SR_SS_35med_Tau3Track',
            plot_all  = False,
            cut_flow  = [
              ['MTrans50',None],
              ['SumCosDPhi05',None],
              ['MuonGradIso',["MuonTotalWeight"]],
              ['VisMass4580',None],
              ['SS',None],
	      ['HLTTau35Med1TrackTwo',None],
       	      ['Tau3Track',None],
              ],
            )

    loop += ztautau.algs.algs.PlotAlg(
            region    = 'SR_SS_35med_lowPT_Tau3Track',
            plot_all  = False,
            cut_flow  = [
              ['MTrans50',None],
              ['SumCosDPhi05',None],
              ['MuonGradIso',["MuonTotalWeight"]],
              ['VisMass4580',None],
              ['SS',None],
	      ['HLTTau35Med1TrackTwo',None],
       	      ['Tau3Track',None],
              ['TauLowPt',None],
              ],
            )

    loop += ztautau.algs.algs.PlotAlg(
            region    = 'SR_SS_35med_highPT_Tau3Track',
            plot_all  = False,
            cut_flow  = [
              ['MTrans50',None],
              ['SumCosDPhi05',None],
              ['MuonGradIso',["MuonTotalWeight"]],
              ['VisMass4580',None],
              ['SS',None],
	      ['HLTTau35Med1TrackTwo',None],
       	      ['Tau3Track',None],
              ['TauHighPt',None],
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
       	      ['Tau3Track',None],
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
       	      ['Tau3Track',None],
              ],
            )

    loop += ztautau.algs.algs.PlotAlg(
            region    = 'AntiIsoCR_OS_Tau3Track',
            plot_all  = False,
            cut_flow  = [
              ['InvMuonGradIso',["MuonWeightAI"]],
              ['SumCosDPhi05',None],
              ['OS',None],
       	      ['Tau3Track',None],
              ],
            )

    loop += ztautau.algs.algs.PlotAlg(
            region    = 'AntiIsoCR_OS_25med_Tau3Track',
            plot_all  = False,
            cut_flow  = [
              ['InvMuonGradIso',["MuonWeightAI"]],
              ['SumCosDPhi05',None],
              ['OS',None],
	      ['HLTTau25Med1TrackTwo',None],
       	      ['Tau3Track',None],
              ],
            )

    loop += ztautau.algs.algs.PlotAlg(
            region    = 'AntiIsoCR_OS_25med_lowPT_Tau3Track',
            plot_all  = False,
            cut_flow  = [
              ['InvMuonGradIso',["MuonWeightAI"]],
              ['SumCosDPhi05',None],
              ['OS',None],
	      ['HLTTau25Med1TrackTwo',None],
       	      ['Tau3Track',None],
              ['TauLowPt',None],
              ],
            )

    loop += ztautau.algs.algs.PlotAlg(
            region    = 'AntiIsoCR_OS_25med_highPT_Tau3Track',
            plot_all  = False,
            cut_flow  = [
              ['InvMuonGradIso',["MuonWeightAI"]],
              ['SumCosDPhi05',None],
              ['OS',None],
	      ['HLTTau25Med1TrackTwo',None],
       	      ['Tau3Track',None],
              ['TauHighPt',None],
              ],
            )

    loop += ztautau.algs.algs.PlotAlg(
            region    = 'AntiIsoCR_OS_35med_Tau3Track',
            plot_all  = False,
            cut_flow  = [
              ['InvMuonGradIso',["MuonWeightAI"]],
              ['SumCosDPhi05',None],
              ['OS',None],
	      ['HLTTau35Med1TrackTwo',None],
       	      ['Tau3Track',None],
              ],
            )

    loop += ztautau.algs.algs.PlotAlg(
            region    = 'AntiIsoCR_OS_35med_lowPT_Tau3Track',
            plot_all  = False,
            cut_flow  = [
              ['InvMuonGradIso',["MuonWeightAI"]],
              ['SumCosDPhi05',None],
              ['OS',None],
	      ['HLTTau35Med1TrackTwo',None],
       	      ['Tau3Track',None],
              ['TauLowPt',None],
              ],
            )

    loop += ztautau.algs.algs.PlotAlg(
            region    = 'AntiIsoCR_OS_35med_highPT_Tau3Track',
            plot_all  = False,
            cut_flow  = [
              ['InvMuonGradIso',["MuonWeightAI"]],
              ['SumCosDPhi05',None],
              ['OS',None],
	      ['HLTTau35Med1TrackTwo',None],
       	      ['Tau3Track',None],
              ['TauHighPt',None],
              ],
            )

    loop += ztautau.algs.algs.PlotAlg(
            region    = 'AntiIsoCR_OS_highPT_Tau3Track',
            plot_all  = False,
            cut_flow  = [
              ['InvMuonGradIso',["MuonWeightAI"]],
              ['SumCosDPhi05',None],
              ['OS',None],
	      ['TauHighPt',None],
       	      ['Tau3Track',None],
              ],
            )

    loop += ztautau.algs.algs.PlotAlg(
            region    = 'AntiIsoCR_OS_lowPT_Tau3Track',
            plot_all  = False,
            cut_flow  = [
              ['InvMuonGradIso',["MuonWeightAI"]],
              ['SumCosDPhi05',None],
              ['OS',None],
	      ['TauLowPt',None],
       	      ['Tau3Track',None],
              ],
            )

    loop += ztautau.algs.algs.PlotAlg(
            region    = 'AntiIsoCR_SS_Tau3Track',
            plot_all  = False,
            cut_flow  = [
              ['InvMuonGradIso',["MuonWeightAI"]],
              ['SumCosDPhi05',None],
              ['SS',None],
       	      ['Tau3Track',None],
              ],
            )

    loop += ztautau.algs.algs.PlotAlg(
            region    = 'AntiIsoCR_SS_25med_Tau3Track',
            plot_all  = False,
            cut_flow  = [
              ['InvMuonGradIso',["MuonWeightAI"]],
              ['SumCosDPhi05',None],
              ['SS',None],
	      ['HLTTau25Med1TrackTwo',None],
       	      ['Tau3Track',None],
              ],
            )

    loop += ztautau.algs.algs.PlotAlg(
            region    = 'AntiIsoCR_SS_25med_lowPT_Tau3Track',
            plot_all  = False,
            cut_flow  = [
              ['InvMuonGradIso',["MuonWeightAI"]],
              ['SumCosDPhi05',None],
              ['SS',None],
	      ['HLTTau25Med1TrackTwo',None],
       	      ['Tau3Track',None],
              ['TauLowPt',None],
              ],
            )

    loop += ztautau.algs.algs.PlotAlg(
            region    = 'AntiIsoCR_SS_25med_highPT_Tau3Track',
            plot_all  = False,
            cut_flow  = [
              ['InvMuonGradIso',["MuonWeightAI"]],
              ['SumCosDPhi05',None],
              ['SS',None],
	      ['HLTTau25Med1TrackTwo',None],
       	      ['Tau3Track',None],
              ['TauHighPt',None],
              ],
            )

    loop += ztautau.algs.algs.PlotAlg(
            region    = 'AntiIsoCR_SS_35med_Tau3Track',
            plot_all  = False,
            cut_flow  = [
              ['InvMuonGradIso',["MuonWeightAI"]],
              ['SumCosDPhi05',None],
              ['SS',None],
	      ['HLTTau35Med1TrackTwo',None],
       	      ['Tau3Track',None],
              ],
            )

    loop += ztautau.algs.algs.PlotAlg(
            region    = 'AntiIsoCR_SS_35med_lowPT_Tau3Track',
            plot_all  = False,
            cut_flow  = [
              ['InvMuonGradIso',["MuonWeightAI"]],
              ['SumCosDPhi05',None],
              ['SS',None],
	      ['HLTTau35Med1TrackTwo',None],
       	      ['Tau3Track',None],
              ['TauLowPt',None],
              ],
            )

    loop += ztautau.algs.algs.PlotAlg(
            region    = 'AntiIsoCR_SS_35med_highPT_Tau3Track',
            plot_all  = False,
            cut_flow  = [
              ['InvMuonGradIso',["MuonWeightAI"]],
              ['SumCosDPhi05',None],
              ['SS',None],
	      ['HLTTau35Med1TrackTwo',None],
       	      ['Tau3Track',None],
              ['TauHighPt',None],
              ],
            )

    loop += ztautau.algs.algs.PlotAlg(
            region    = 'AntiIsoCR_SS_highPT_Tau3Track',
            plot_all  = False,
            cut_flow  = [
              ['InvMuonGradIso',["MuonWeightAI"]],
              ['SumCosDPhi05',None],
              ['SS',None],
	      ['TauHighPt',None],
       	      ['Tau3Track',None],
              ],
            )

    loop += ztautau.algs.algs.PlotAlg(
            region    = 'AntiIsoCR_SS_lowPT_Tau3Track',
            plot_all  = False,
            cut_flow  = [
              ['InvMuonGradIso',["MuonWeightAI"]],
              ['SumCosDPhi05',None],
              ['SS',None],
	      ['TauLowPt',None],
       	      ['Tau3Track',None],
              ],
            )

#-----------------------------#
#	ONE TRACK TAU
#-----------------------------#
    
    loop += ztautau.algs.algs.PlotAlg(
            region    = 'Wjets_OS_highPT_Tau1Track',
            plot_all  = False,
            cut_flow  = [
              ['MTrans60',None],
              ['MET30',None],
              ['OS',None],
              ['MuonGradIso',["MuonTotalWeight"]],
	      ['TauHighPt',None],
       	      ['Tau1Track',None],
              ],
            )

    loop += ztautau.algs.algs.PlotAlg(
            region    = 'Wjets_OS_Tau1Track',
            plot_all  = False,
            cut_flow  = [
              ['MTrans60',None],
              ['MET30',None],
              ['OS',None],
              ['MuonGradIso',["MuonTotalWeight"]],
	      ['Tau1Track',None],
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
       	      ['Tau1Track',None],
              ],
            )

    loop += ztautau.algs.algs.PlotAlg(
            region    = 'Wjets_OS_25med_Tau1Track',
            plot_all  = False,
            cut_flow  = [
              ['MTrans60',None],
              ['MET30',None],
              ['OS',None],
              ['MuonGradIso',["MuonTotalWeight"]],
	      ['HLTTau25Med1TrackTwo',None],
       	      ['Tau1Track',None],
              ],
            )

    loop += ztautau.algs.algs.PlotAlg(
            region    = 'Wjets_OS_25med_lowPT_Tau1Track',
            plot_all  = False,
            cut_flow  = [
              ['MTrans60',None],
              ['MET30',None],
              ['OS',None],
              ['MuonGradIso',["MuonTotalWeight"]],
	      ['HLTTau25Med1TrackTwo',None],
       	      ['Tau1Track',None],
              ['TauLowPt',None],
              ],
            )

    loop += ztautau.algs.algs.PlotAlg(
            region    = 'Wjets_OS_25med_highPT_Tau1Track',
            plot_all  = False,
            cut_flow  = [
              ['MTrans60',None],
              ['MET30',None],
              ['OS',None],
              ['MuonGradIso',["MuonTotalWeight"]],
	      ['HLTTau25Med1TrackTwo',None],
       	      ['Tau1Track',None],
              ['TauHighPt',None],
              ],
            )

    loop += ztautau.algs.algs.PlotAlg(
            region    = 'Wjets_OS_35med_Tau1Track',
            plot_all  = False,
            cut_flow  = [
              ['MTrans60',None],
              ['MET30',None],
              ['OS',None],
              ['MuonGradIso',["MuonTotalWeight"]],
	      ['HLTTau35Med1TrackTwo',None],
       	      ['Tau1Track',None],
              ],
            )

    loop += ztautau.algs.algs.PlotAlg(
            region    = 'Wjets_OS_35med_lowPT_Tau1Track',
            plot_all  = False,
            cut_flow  = [
              ['MTrans60',None],
              ['MET30',None],
              ['OS',None],
              ['MuonGradIso',["MuonTotalWeight"]],
	      ['HLTTau35Med1TrackTwo',None],
       	      ['Tau1Track',None],
              ['TauLowPt',None],
              ],
            )

    loop += ztautau.algs.algs.PlotAlg(
            region    = 'Wjets_OS_35med_highPT_Tau1Track',
            plot_all  = False,
            cut_flow  = [
              ['MTrans60',None],
              ['MET30',None],
              ['OS',None],
              ['MuonGradIso',["MuonTotalWeight"]],
	      ['HLTTau35Med1TrackTwo',None],
       	      ['Tau1Track',None],
              ['TauHighPt',None],
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
       	      ['Tau1Track',None],
              ],
            )

    loop += ztautau.algs.algs.PlotAlg(
            region    = 'Wjets_SS_25med_Tau1Track',
            plot_all  = False,
            cut_flow  = [
              ['MTrans60',None],
              ['MET30',None],
              ['SS',None],
              ['MuonGradIso',["MuonTotalWeight"]],
	      ['HLTTau25Med1TrackTwo',None],
       	      ['Tau1Track',None],
              ],
            )

    loop += ztautau.algs.algs.PlotAlg(
            region    = 'Wjets_SS_25med_lowPT_Tau1Track',
            plot_all  = False,
            cut_flow  = [
              ['MTrans60',None],
              ['MET30',None],
              ['SS',None],
              ['MuonGradIso',["MuonTotalWeight"]],
	      ['HLTTau25Med1TrackTwo',None],
       	      ['Tau1Track',None],
              ['TauLowPt',None],
              ],
            )

    loop += ztautau.algs.algs.PlotAlg(
            region    = 'Wjets_SS_25med_highPT_Tau1Track',
            plot_all  = False,
            cut_flow  = [
              ['MTrans60',None],
              ['MET30',None],
              ['SS',None],
              ['MuonGradIso',["MuonTotalWeight"]],
	      ['HLTTau25Med1TrackTwo',None],
       	      ['Tau1Track',None],
              ['TauHighPt',None],
              ],
            )

    loop += ztautau.algs.algs.PlotAlg(
            region    = 'Wjets_SS_35med_Tau1Track',
            plot_all  = False,
            cut_flow  = [
              ['MTrans60',None],
              ['MET30',None],
              ['SS',None],
              ['MuonGradIso',["MuonTotalWeight"]],
	      ['HLTTau35Med1TrackTwo',None],
       	      ['Tau1Track',None],
              ],
            )

    loop += ztautau.algs.algs.PlotAlg(
            region    = 'Wjets_SS_35med_lowPT_Tau1Track',
            plot_all  = False,
            cut_flow  = [
              ['MTrans60',None],
              ['MET30',None],
              ['SS',None],
              ['MuonGradIso',["MuonTotalWeight"]],
	      ['HLTTau35Med1TrackTwo',None],
       	      ['Tau1Track',None],
              ['TauLowPt',None],
              ],
            )

    loop += ztautau.algs.algs.PlotAlg(
            region    = 'Wjets_SS_35med_highPT_Tau1Track',
            plot_all  = False,
            cut_flow  = [
              ['MTrans60',None],
              ['MET30',None],
              ['SS',None],
              ['MuonGradIso',["MuonTotalWeight"]],
	      ['HLTTau35Med1TrackTwo',None],
       	      ['Tau1Track',None],
              ['TauHighPt',None],
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
       	      ['Tau1Track',None],
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
       	      ['Tau1Track',None],
              ],
            )

    loop += ztautau.algs.algs.PlotAlg(
            region    = 'SR_25med_Tau1Track',
            plot_all  = False,
            cut_flow  = [
              ['MTrans50',None],
              ['SumCosDPhi05',None],
              ['MuonGradIso',["MuonTotalWeight"]],
              ['VisMass4580',None],
              ['OS',None],
	      ['HLTTau25Med1TrackTwo',None],
       	      ['Tau1Track',None],
              ],
            )

    loop += ztautau.algs.algs.PlotAlg(
            region    = 'SR_25med_lowPT_Tau1Track',
            plot_all  = False,
            cut_flow  = [
              ['MTrans50',None],
              ['SumCosDPhi05',None],
              ['MuonGradIso',["MuonTotalWeight"]],
              ['VisMass4580',None],
              ['OS',None],
	      ['HLTTau25Med1TrackTwo',None],
       	      ['Tau1Track',None],
              ['TauLowPt',None],
              ],
            )

    loop += ztautau.algs.algs.PlotAlg(
            region    = 'SR_25med_highPT_Tau1Track',
            plot_all  = False,
            cut_flow  = [
              ['MTrans50',None],
              ['SumCosDPhi05',None],
              ['MuonGradIso',["MuonTotalWeight"]],
              ['VisMass4580',None],
              ['OS',None],
	      ['HLTTau25Med1TrackTwo',None],
       	      ['Tau1Track',None],
              ['TauHighPt',None],
              ],
            )

    loop += ztautau.algs.algs.PlotAlg(
            region    = 'SR_35med_Tau1Track',
            plot_all  = False,
            cut_flow  = [
              ['MTrans50',None],
              ['SumCosDPhi05',None],
              ['MuonGradIso',["MuonTotalWeight"]],
              ['VisMass4580',None],
              ['OS',None],
	      ['HLTTau35Med1TrackTwo',None],
       	      ['Tau1Track',None],
              ],
            )

    loop += ztautau.algs.algs.PlotAlg(
            region    = 'SR_35med_lowPT_Tau1Track',
            plot_all  = False,
            cut_flow  = [
              ['MTrans50',None],
              ['SumCosDPhi05',None],
              ['MuonGradIso',["MuonTotalWeight"]],
              ['VisMass4580',None],
              ['OS',None],
	      ['HLTTau35Med1TrackTwo',None],
       	      ['Tau1Track',None],
              ['TauLowPt',None],
              ],
            )

    loop += ztautau.algs.algs.PlotAlg(
            region    = 'SR_35med_highPT_Tau1Track',
            plot_all  = False,
            cut_flow  = [
              ['MTrans50',None],
              ['SumCosDPhi05',None],
              ['MuonGradIso',["MuonTotalWeight"]],
              ['VisMass4580',None],
              ['OS',None],
	      ['HLTTau35Med1TrackTwo',None],
       	      ['Tau1Track',None],
              ['TauHighPt',None],
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
       	      ['Tau1Track',None],
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
       	      ['Tau1Track',None],
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
       	      ['Tau1Track',None],
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
       	      ['Tau1Track',None],
              ],
            )

    loop += ztautau.algs.algs.PlotAlg(
            region    = 'SR_SS_25med_Tau1Track',
            plot_all  = False,
            cut_flow  = [
              ['MTrans50',None],
              ['SumCosDPhi05',None],
              ['MuonGradIso',["MuonTotalWeight"]],
              ['VisMass4580',None],
              ['SS',None],
	      ['HLTTau25Med1TrackTwo',None],
       	      ['Tau1Track',None],
              ],
            )

    loop += ztautau.algs.algs.PlotAlg(
            region    = 'SR_SS_25med_lowPT_Tau1Track',
            plot_all  = False,
            cut_flow  = [
              ['MTrans50',None],
              ['SumCosDPhi05',None],
              ['MuonGradIso',["MuonTotalWeight"]],
              ['VisMass4580',None],
              ['SS',None],
	      ['HLTTau25Med1TrackTwo',None],
       	      ['Tau1Track',None],
              ['TauLowPt',None],
              ],
            )

    loop += ztautau.algs.algs.PlotAlg(
            region    = 'SR_SS_25med_highPT_Tau1Track',
            plot_all  = False,
            cut_flow  = [
              ['MTrans50',None],
              ['SumCosDPhi05',None],
              ['MuonGradIso',["MuonTotalWeight"]],
              ['VisMass4580',None],
              ['SS',None],
	      ['HLTTau25Med1TrackTwo',None],
       	      ['Tau1Track',None],
              ['TauHighPt',None],
              ],
            )

    loop += ztautau.algs.algs.PlotAlg(
            region    = 'SR_SS_35med_Tau1Track',
            plot_all  = False,
            cut_flow  = [
              ['MTrans50',None],
              ['SumCosDPhi05',None],
              ['MuonGradIso',["MuonTotalWeight"]],
              ['VisMass4580',None],
              ['SS',None],
	      ['HLTTau35Med1TrackTwo',None],
       	      ['Tau1Track',None],
              ],
            )

    loop += ztautau.algs.algs.PlotAlg(
            region    = 'SR_SS_35med_lowPT_Tau1Track',
            plot_all  = False,
            cut_flow  = [
              ['MTrans50',None],
              ['SumCosDPhi05',None],
              ['MuonGradIso',["MuonTotalWeight"]],
              ['VisMass4580',None],
              ['SS',None],
	      ['HLTTau35Med1TrackTwo',None],
       	      ['Tau1Track',None],
              ['TauLowPt',None],
              ],
            )

    loop += ztautau.algs.algs.PlotAlg(
            region    = 'SR_SS_35med_highPT_Tau1Track',
            plot_all  = False,
            cut_flow  = [
              ['MTrans50',None],
              ['SumCosDPhi05',None],
              ['MuonGradIso',["MuonTotalWeight"]],
              ['VisMass4580',None],
              ['SS',None],
	      ['HLTTau35Med1TrackTwo',None],
       	      ['Tau1Track',None],
              ['TauHighPt',None],
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
       	      ['Tau1Track',None],
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
       	      ['Tau1Track',None],
              ],
            )

    loop += ztautau.algs.algs.PlotAlg(
            region    = 'AntiIsoCR_OS_Tau1Track',
            plot_all  = False,
            cut_flow  = [
              ['InvMuonGradIso',["MuonWeightAI"]],
              ['SumCosDPhi05',None],
              ['OS',None],
       	      ['Tau1Track',None],
              ],
            )

    loop += ztautau.algs.algs.PlotAlg(
            region    = 'AntiIsoCR_OS_25med_Tau1Track',
            plot_all  = False,
            cut_flow  = [
              ['InvMuonGradIso',["MuonWeightAI"]],
              ['SumCosDPhi05',None],
              ['OS',None],
	      ['HLTTau25Med1TrackTwo',None],
       	      ['Tau1Track',None],
              ],
            )

    loop += ztautau.algs.algs.PlotAlg(
            region    = 'AntiIsoCR_OS_25med_lowPT_Tau1Track',
            plot_all  = False,
            cut_flow  = [
              ['InvMuonGradIso',["MuonWeightAI"]],
              ['SumCosDPhi05',None],
              ['OS',None],
	      ['HLTTau25Med1TrackTwo',None],
       	      ['Tau1Track',None],
              ['TauLowPt',None],
              ],
            )

    loop += ztautau.algs.algs.PlotAlg(
            region    = 'AntiIsoCR_OS_25med_highPT_Tau1Track',
            plot_all  = False,
            cut_flow  = [
              ['InvMuonGradIso',["MuonWeightAI"]],
              ['SumCosDPhi05',None],
              ['OS',None],
	      ['HLTTau25Med1TrackTwo',None],
       	      ['Tau1Track',None],
              ['TauHighPt',None],
              ],
            )

    loop += ztautau.algs.algs.PlotAlg(
            region    = 'AntiIsoCR_OS_35med_Tau1Track',
            plot_all  = False,
            cut_flow  = [
              ['InvMuonGradIso',["MuonWeightAI"]],
              ['SumCosDPhi05',None],
              ['OS',None],
	      ['HLTTau35Med1TrackTwo',None],
       	      ['Tau1Track',None],
              ],
            )

    loop += ztautau.algs.algs.PlotAlg(
            region    = 'AntiIsoCR_OS_35med_lowPT_Tau1Track',
            plot_all  = False,
            cut_flow  = [
              ['InvMuonGradIso',["MuonWeightAI"]],
              ['SumCosDPhi05',None],
              ['OS',None],
	      ['HLTTau35Med1TrackTwo',None],
       	      ['Tau1Track',None],
              ['TauLowPt',None],
              ],
            )

    loop += ztautau.algs.algs.PlotAlg(
            region    = 'AntiIsoCR_OS_35med_highPT_Tau1Track',
            plot_all  = False,
            cut_flow  = [
              ['InvMuonGradIso',["MuonWeightAI"]],
              ['SumCosDPhi05',None],
              ['OS',None],
	      ['HLTTau35Med1TrackTwo',None],
       	      ['Tau1Track',None],
              ['TauHighPt',None],
              ],
            )

    loop += ztautau.algs.algs.PlotAlg(
            region    = 'AntiIsoCR_OS_highPT_Tau1Track',
            plot_all  = False,
            cut_flow  = [
              ['InvMuonGradIso',["MuonWeightAI"]],
              ['SumCosDPhi05',None],
              ['OS',None],
	      ['TauHighPt',None],
       	      ['Tau1Track',None],
              ],
            )

    loop += ztautau.algs.algs.PlotAlg(
            region    = 'AntiIsoCR_OS_lowPT_Tau1Track',
            plot_all  = False,
            cut_flow  = [
              ['InvMuonGradIso',["MuonWeightAI"]],
              ['SumCosDPhi05',None],
              ['OS',None],
	      ['TauLowPt',None],
       	      ['Tau1Track',None],
              ],
            )

    loop += ztautau.algs.algs.PlotAlg(
            region    = 'AntiIsoCR_SS_Tau1Track',
            plot_all  = False,
            cut_flow  = [
              ['InvMuonGradIso',["MuonWeightAI"]],
              ['SumCosDPhi05',None],
              ['SS',None],
       	      ['Tau1Track',None],
              ],
            )

    loop += ztautau.algs.algs.PlotAlg(
            region    = 'AntiIsoCR_SS_25med_Tau1Track',
            plot_all  = False,
            cut_flow  = [
              ['InvMuonGradIso',["MuonWeightAI"]],
              ['SumCosDPhi05',None],
              ['SS',None],
	      ['HLTTau25Med1TrackTwo',None],
       	      ['Tau1Track',None],
              ],
            )

    loop += ztautau.algs.algs.PlotAlg(
            region    = 'AntiIsoCR_SS_25med_lowPT_Tau1Track',
            plot_all  = False,
            cut_flow  = [
              ['InvMuonGradIso',["MuonWeightAI"]],
              ['SumCosDPhi05',None],
              ['SS',None],
	      ['HLTTau25Med1TrackTwo',None],
       	      ['Tau1Track',None],
              ['TauLowPt',None],
              ],
            )

    loop += ztautau.algs.algs.PlotAlg(
            region    = 'AntiIsoCR_SS_25med_highPT_Tau1Track',
            plot_all  = False,
            cut_flow  = [
              ['InvMuonGradIso',["MuonWeightAI"]],
              ['SumCosDPhi05',None],
              ['SS',None],
	      ['HLTTau25Med1TrackTwo',None],
       	      ['Tau1Track',None],
              ['TauHighPt',None],
              ],
            )

    loop += ztautau.algs.algs.PlotAlg(
            region    = 'AntiIsoCR_SS_35med_Tau1Track',
            plot_all  = False,
            cut_flow  = [
              ['InvMuonGradIso',["MuonWeightAI"]],
              ['SumCosDPhi05',None],
              ['SS',None],
	      ['HLTTau35Med1TrackTwo',None],
       	      ['Tau1Track',None],
              ],
            )

    loop += ztautau.algs.algs.PlotAlg(
            region    = 'AntiIsoCR_SS_35med_lowPT_Tau1Track',
            plot_all  = False,
            cut_flow  = [
              ['InvMuonGradIso',["MuonWeightAI"]],
              ['SumCosDPhi05',None],
              ['SS',None],
	      ['HLTTau35Med1TrackTwo',None],
       	      ['Tau1Track',None],
              ['TauLowPt',None],
              ],
            )

    loop += ztautau.algs.algs.PlotAlg(
            region    = 'AntiIsoCR_SS_35med_highPT_Tau1Track',
            plot_all  = False,
            cut_flow  = [
              ['InvMuonGradIso',["MuonWeightAI"]],
              ['SumCosDPhi05',None],
              ['SS',None],
	      ['HLTTau35Med1TrackTwo',None],
       	      ['Tau1Track',None],
              ['TauHighPt',None],
              ],
            )

    loop += ztautau.algs.algs.PlotAlg(
            region    = 'AntiIsoCR_SS_highPT_Tau1Track',
            plot_all  = False,
            cut_flow  = [
              ['InvMuonGradIso',["MuonWeightAI"]],
              ['SumCosDPhi05',None],
              ['SS',None],
	      ['TauHighPt',None],
       	      ['Tau1Track',None],
              ],
            )

    loop += ztautau.algs.algs.PlotAlg(
            region    = 'AntiIsoCR_SS_lowPT_Tau1Track',
            plot_all  = False,
            cut_flow  = [
              ['InvMuonGradIso',["MuonWeightAI"]],
              ['SumCosDPhi05',None],
              ['SS',None],
	      ['TauLowPt',None],
       	      ['Tau1Track',None],
              ],
            )

#-----------------------------#
#       BOTH TRACKS TAU
#-----------------------------#

    loop += ztautau.algs.algs.PlotAlg(
            region    = 'Wjets_OS_highPT',
            plot_all  = False,
            cut_flow  = [
              ['MTrans60',None],
              ['MET30',None],
              ['OS',None],
              ['MuonGradIso',["MuonTotalWeight"]],
	      ['TauHighPt',None],
              ],
            )

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

############## KW SYSTEMATICS

    loop += ztautau.algs.algs.PlotAlg(
            region    = 'Wjets_OS_MTrans625',
            plot_all  = False,
            cut_flow  = [
              ['MTrans625',None],
              ['MET30',None],
              ['OS',None],
              ['MuonGradIso',["MuonTotalWeight"]],
              ],
            )
    loop += ztautau.algs.algs.PlotAlg(
            region    = 'Wjets_OS_MTrans675',
            plot_all  = False,
            cut_flow  = [
              ['MTrans675',None],
              ['MET30',None],
              ['OS',None],
              ['MuonGradIso',["MuonTotalWeight"]],
              ],
            )

    loop += ztautau.algs.algs.PlotAlg(
            region    = 'Wjets_OS_MTrans725',
            plot_all  = False,
            cut_flow  = [
              ['MTrans725',None],
              ['MET30',None],
              ['OS',None],
              ['MuonGradIso',["MuonTotalWeight"]],
              ],
            )

    loop += ztautau.algs.algs.PlotAlg(
            region    = 'Wjets_OS_MTrans775',
            plot_all  = False,
            cut_flow  = [
              ['MTrans775',None],
              ['MET30',None],
              ['OS',None],
              ['MuonGradIso',["MuonTotalWeight"]],
              ],
            )

    loop += ztautau.algs.algs.PlotAlg(
            region    = 'Wjets_OS_MTrans825',
            plot_all  = False,
            cut_flow  = [
              ['MTrans825',None],
              ['MET30',None],
              ['OS',None],
              ['MuonGradIso',["MuonTotalWeight"]],
              ],
            )

    loop += ztautau.algs.algs.PlotAlg(
            region    = 'Wjets_OS_MTrans875',
            plot_all  = False,
            cut_flow  = [
              ['MTrans875',None],
              ['MET30',None],
              ['OS',None],
              ['MuonGradIso',["MuonTotalWeight"]],
              ],
            )

    loop += ztautau.algs.algs.PlotAlg(
            region    = 'Wjets_OS_MTrans925',
            plot_all  = False,
            cut_flow  = [
              ['MTrans925',None],
              ['MET30',None],
              ['OS',None],
              ['MuonGradIso',["MuonTotalWeight"]],
              ],
            )

    loop += ztautau.algs.algs.PlotAlg(
            region    = 'Wjets_OS_MTrans975',
            plot_all  = False,
            cut_flow  = [
              ['MTrans975',None],
              ['MET30',None],
              ['OS',None],
              ['MuonGradIso',["MuonTotalWeight"]],
              ],
            )

    loop += ztautau.algs.algs.PlotAlg(
            region    = 'Wjets_OS_MTrans1025',
            plot_all  = False,
            cut_flow  = [
              ['MTrans1025',None],
              ['MET30',None],
              ['OS',None],
              ['MuonGradIso',["MuonTotalWeight"]],
              ],
            )

    loop += ztautau.algs.algs.PlotAlg(
            region    = 'Wjets_OS_MTrans1075',
            plot_all  = False,
            cut_flow  = [
              ['MTrans1075',None],
              ['MET30',None],
              ['OS',None],
              ['MuonGradIso',["MuonTotalWeight"]],
              ],
            )


    loop += ztautau.algs.algs.PlotAlg(
            region    = 'Wjets_SS_MTrans625',
            plot_all  = False,
            cut_flow  = [
              ['MTrans625',None],
              ['MET30',None],
              ['SS',None],
              ['MuonGradIso',["MuonTotalWeight"]],
              ],
            )
    loop += ztautau.algs.algs.PlotAlg(
            region    = 'Wjets_SS_MTrans675',
            plot_all  = False,
            cut_flow  = [
              ['MTrans675',None],
              ['MET30',None],
              ['SS',None],
              ['MuonGradIso',["MuonTotalWeight"]],
              ],
            )

    loop += ztautau.algs.algs.PlotAlg(
            region    = 'Wjets_SS_MTrans725',
            plot_all  = False,
            cut_flow  = [
              ['MTrans725',None],
              ['MET30',None],
              ['SS',None],
              ['MuonGradIso',["MuonTotalWeight"]],
              ],
            )

    loop += ztautau.algs.algs.PlotAlg(
            region    = 'Wjets_SS_MTrans775',
            plot_all  = False,
            cut_flow  = [
              ['MTrans775',None],
              ['MET30',None],
              ['SS',None],
              ['MuonGradIso',["MuonTotalWeight"]],
              ],
            )

    loop += ztautau.algs.algs.PlotAlg(
            region    = 'Wjets_SS_MTrans825',
            plot_all  = False,
            cut_flow  = [
              ['MTrans825',None],
              ['MET30',None],
              ['SS',None],
              ['MuonGradIso',["MuonTotalWeight"]],
              ],
            )

    loop += ztautau.algs.algs.PlotAlg(
            region    = 'Wjets_SS_MTrans875',
            plot_all  = False,
            cut_flow  = [
              ['MTrans875',None],
              ['MET30',None],
              ['SS',None],
              ['MuonGradIso',["MuonTotalWeight"]],
              ],
            )

    loop += ztautau.algs.algs.PlotAlg(
            region    = 'Wjets_SS_MTrans925',
            plot_all  = False,
            cut_flow  = [
              ['MTrans925',None],
              ['MET30',None],
              ['SS',None],
              ['MuonGradIso',["MuonTotalWeight"]],
              ],
            )

    loop += ztautau.algs.algs.PlotAlg(
            region    = 'Wjets_SS_MTrans975',
            plot_all  = False,
            cut_flow  = [
              ['MTrans975',None],
              ['MET30',None],
              ['SS',None],
              ['MuonGradIso',["MuonTotalWeight"]],
              ],
            )

    loop += ztautau.algs.algs.PlotAlg(
            region    = 'Wjets_SS_MTrans1025',
            plot_all  = False,
            cut_flow  = [
              ['MTrans1025',None],
              ['MET30',None],
              ['SS',None],
              ['MuonGradIso',["MuonTotalWeight"]],
              ],
            )

    loop += ztautau.algs.algs.PlotAlg(
            region    = 'Wjets_SS_MTrans1075',
            plot_all  = False,
            cut_flow  = [
              ['MTrans1075',None],
              ['MET30',None],
              ['SS',None],
              ['MuonGradIso',["MuonTotalWeight"]],
              ],
            )



#######################
    loop += ztautau.algs.algs.PlotAlg(
            region    = 'Wjets_OS_lowPT',
            plot_all  = False,
            cut_flow  = [
              ['MTrans60',None],
              ['MET30',None],
              ['OS',None],
              ['MuonGradIso',["MuonTotalWeight"]],
	      ['TauLowPt',None],
              ],
            )

    loop += ztautau.algs.algs.PlotAlg(
            region    = 'Wjets_OS_25med',
            plot_all  = False,
            cut_flow  = [
              ['MTrans60',None],
              ['MET30',None],
              ['OS',None],
              ['MuonGradIso',["MuonTotalWeight"]],
	      ['HLTTau25Med1TrackTwo',None],
              ],
            )

    loop += ztautau.algs.algs.PlotAlg(
            region    = 'Wjets_OS_25med_lowPT',
            plot_all  = False,
            cut_flow  = [
              ['MTrans60',None],
              ['MET30',None],
              ['OS',None],
              ['MuonGradIso',["MuonTotalWeight"]],
	      ['HLTTau25Med1TrackTwo',None],
              ['TauLowPt',None],
              ],
            )

    loop += ztautau.algs.algs.PlotAlg(
            region    = 'Wjets_OS_25med_highPT',
            plot_all  = False,
            cut_flow  = [
              ['MTrans60',None],
              ['MET30',None],
              ['OS',None],
              ['MuonGradIso',["MuonTotalWeight"]],
	      ['HLTTau25Med1TrackTwo',None],
              ['TauHighPt',None],
              ],
            )

    loop += ztautau.algs.algs.PlotAlg(
            region    = 'Wjets_OS_35med',
            plot_all  = False,
            cut_flow  = [
              ['MTrans60',None],
              ['MET30',None],
              ['OS',None],
              ['MuonGradIso',["MuonTotalWeight"]],
	      ['HLTTau35Med1TrackTwo',None],
              ],
            )

    loop += ztautau.algs.algs.PlotAlg(
            region    = 'Wjets_OS_35med_lowPT',
            plot_all  = False,
            cut_flow  = [
              ['MTrans60',None],
              ['MET30',None],
              ['OS',None],
              ['MuonGradIso',["MuonTotalWeight"]],
	      ['HLTTau35Med1TrackTwo',None],
              ['TauLowPt',None],
              ],
            )

    loop += ztautau.algs.algs.PlotAlg(
            region    = 'Wjets_OS_35med_highPT',
            plot_all  = False,
            cut_flow  = [
              ['MTrans60',None],
              ['MET30',None],
              ['OS',None],
              ['MuonGradIso',["MuonTotalWeight"]],
	      ['HLTTau35Med1TrackTwo',None],
              ['TauHighPt',None],
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
            region    = 'Wjets_SS_25med',
            plot_all  = False,
            cut_flow  = [
              ['MTrans60',None],
              ['MET30',None],
              ['SS',None],
              ['MuonGradIso',["MuonTotalWeight"]],
	      ['HLTTau25Med1TrackTwo',None],
              ],
            )

    loop += ztautau.algs.algs.PlotAlg(
            region    = 'Wjets_SS_25med_lowPT',
            plot_all  = False,
            cut_flow  = [
              ['MTrans60',None],
              ['MET30',None],
              ['SS',None],
              ['MuonGradIso',["MuonTotalWeight"]],
	      ['HLTTau25Med1TrackTwo',None],
              ['TauLowPt',None],
              ],
            )

    loop += ztautau.algs.algs.PlotAlg(
            region    = 'Wjets_SS_25med_highPT',
            plot_all  = False,
            cut_flow  = [
              ['MTrans60',None],
              ['MET30',None],
              ['SS',None],
              ['MuonGradIso',["MuonTotalWeight"]],
	      ['HLTTau25Med1TrackTwo',None],
              ['TauHighPt',None],
              ],
            )

    loop += ztautau.algs.algs.PlotAlg(
            region    = 'Wjets_SS_35med',
            plot_all  = False,
            cut_flow  = [
              ['MTrans60',None],
              ['MET30',None],
              ['SS',None],
              ['MuonGradIso',["MuonTotalWeight"]],
	      ['HLTTau35Med1TrackTwo',None],
              ],
            )

    loop += ztautau.algs.algs.PlotAlg(
            region    = 'Wjets_SS_35med_lowPT',
            plot_all  = False,
            cut_flow  = [
              ['MTrans60',None],
              ['MET30',None],
              ['SS',None],
              ['MuonGradIso',["MuonTotalWeight"]],
	      ['HLTTau35Med1TrackTwo',None],
              ['TauLowPt',None],
              ],
            )

    loop += ztautau.algs.algs.PlotAlg(
            region    = 'Wjets_SS_35med_highPT',
            plot_all  = False,
            cut_flow  = [
              ['MTrans60',None],
              ['MET30',None],
              ['SS',None],
              ['MuonGradIso',["MuonTotalWeight"]],
	      ['HLTTau35Med1TrackTwo',None],
              ['TauHighPt',None],
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
	      ['TauLowPt',None],
              ],
            )

    loop += ztautau.algs.algs.PlotAlg(
            region    = 'SR_25med',
            plot_all  = False,
            cut_flow  = [
              ['MTrans50',None],
              ['SumCosDPhi05',None],
              ['MuonGradIso',["MuonTotalWeight"]],
              ['VisMass4580',None],
              ['OS',None],
	      ['HLTTau25Med1TrackTwo',None],
              ],
            )

    loop += ztautau.algs.algs.PlotAlg(
            region    = 'SR_25med_lowPT',
            plot_all  = False,
            cut_flow  = [
              ['MTrans50',None],
              ['SumCosDPhi05',None],
              ['MuonGradIso',["MuonTotalWeight"]],
              ['VisMass4580',None],
              ['OS',None],
	      ['HLTTau25Med1TrackTwo',None],
              ['TauLowPt',None],
              ],
            )

    loop += ztautau.algs.algs.PlotAlg(
            region    = 'SR_25med_highPT',
            plot_all  = False,
            cut_flow  = [
              ['MTrans50',None],
              ['SumCosDPhi05',None],
              ['MuonGradIso',["MuonTotalWeight"]],
              ['VisMass4580',None],
              ['OS',None],
	      ['HLTTau25Med1TrackTwo',None],
              ['TauHighPt',None],
              ],
            )

    loop += ztautau.algs.algs.PlotAlg(
            region    = 'SR_35med',
            plot_all  = False,
            cut_flow  = [
              ['MTrans50',None],
              ['SumCosDPhi05',None],
              ['MuonGradIso',["MuonTotalWeight"]],
              ['VisMass4580',None],
              ['OS',None],
	      ['HLTTau35Med1TrackTwo',None],
              ],
            )

    loop += ztautau.algs.algs.PlotAlg(
            region    = 'SR_35med_lowPT',
            plot_all  = False,
            cut_flow  = [
              ['MTrans50',None],
              ['SumCosDPhi05',None],
              ['MuonGradIso',["MuonTotalWeight"]],
              ['VisMass4580',None],
              ['OS',None],
	      ['HLTTau35Med1TrackTwo',None],
              ['TauLowPt',None],
              ],
            )

    loop += ztautau.algs.algs.PlotAlg(
            region    = 'SR_35med_highPT',
            plot_all  = False,
            cut_flow  = [
              ['MTrans50',None],
              ['SumCosDPhi05',None],
              ['MuonGradIso',["MuonTotalWeight"]],
              ['VisMass4580',None],
              ['OS',None],
	      ['HLTTau35Med1TrackTwo',None],
              ['TauHighPt',None],
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
            region    = 'SR_highPT',
            plot_all  = False,
            cut_flow  = [
              ['MTrans50',None],
              ['SumCosDPhi05',None],
              ['MuonGradIso',["MuonTotalWeight"]],
              ['VisMass4580',None],
              ['OS',None],
	      ['TauHighPt',None],
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
	      ['TauLowPt',None],
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
            region    = 'SR_SS_25med',
            plot_all  = False,
            cut_flow  = [
              ['MTrans50',None],
              ['SumCosDPhi05',None],
              ['MuonGradIso',["MuonTotalWeight"]],
              ['VisMass4580',None],
              ['SS',None],
	      ['HLTTau25Med1TrackTwo',None],
              ],
            )

    loop += ztautau.algs.algs.PlotAlg(
            region    = 'SR_SS_25med_lowPT',
            plot_all  = False,
            cut_flow  = [
              ['MTrans50',None],
              ['SumCosDPhi05',None],
              ['MuonGradIso',["MuonTotalWeight"]],
              ['VisMass4580',None],
              ['SS',None],
	      ['HLTTau25Med1TrackTwo',None],
              ['TauLowPt',None],
              ],
            )

    loop += ztautau.algs.algs.PlotAlg(
            region    = 'SR_SS_25med_highPT',
            plot_all  = False,
            cut_flow  = [
              ['MTrans50',None],
              ['SumCosDPhi05',None],
              ['MuonGradIso',["MuonTotalWeight"]],
              ['VisMass4580',None],
              ['SS',None],
	      ['HLTTau25Med1TrackTwo',None],
              ['TauHighPt',None],
              ],
            )

    loop += ztautau.algs.algs.PlotAlg(
            region    = 'SR_SS_35med',
            plot_all  = False,
            cut_flow  = [
              ['MTrans50',None],
              ['SumCosDPhi05',None],
              ['MuonGradIso',["MuonTotalWeight"]],
              ['VisMass4580',None],
              ['SS',None],
	      ['HLTTau35Med1TrackTwo',None],
              ],
            )

    loop += ztautau.algs.algs.PlotAlg(
            region    = 'SR_SS_35med_lowPT',
            plot_all  = False,
            cut_flow  = [
              ['MTrans50',None],
              ['SumCosDPhi05',None],
              ['MuonGradIso',["MuonTotalWeight"]],
              ['VisMass4580',None],
              ['SS',None],
	      ['HLTTau35Med1TrackTwo',None],
              ['TauLowPt',None],
              ],
            )

    loop += ztautau.algs.algs.PlotAlg(
            region    = 'SR_SS_35med_highPT',
            plot_all  = False,
            cut_flow  = [
              ['MTrans50',None],
              ['SumCosDPhi05',None],
              ['MuonGradIso',["MuonTotalWeight"]],
              ['VisMass4580',None],
              ['SS',None],
	      ['HLTTau35Med1TrackTwo',None],
              ['TauHighPt',None],
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
	      ['TauHighPt',None],
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
	      ['TauLowPt',None],
              ],
            )

#-----------------------------------------------
#   ANTI-ISO WITH DIFFERENT CUTS (CHECK BIAS)    ------>   decision to use ONLY MUON INVERSION FROM NOW ON
#-----------------------------------------------

    loop += ztautau.algs.algs.PlotAlg(
            region    = 'AntiIsoCR_OS',
            plot_all  = False,
            cut_flow  = [
              ['SumCosDPhi05',None],
              ['OS',None],
              ['InvMuonGradIso',["MuonWeightAI"]],
              ],
            )

############ #RQCD SYSTEMATICS

    loop += ztautau.algs.algs.PlotAlg(
            region    = 'AntiIsoCR_OS_Topoetcone20pt010',
            plot_all  = False,
            cut_flow  = [
              ['SumCosDPhi05',None],
              ['OS',None],
              ['InvMuonGradIso',["MuonWeightAI"]],
              ['Topoetcone20pt010',None],
              ],
            )
    loop += ztautau.algs.algs.PlotAlg(
            region    = 'AntiIsoCR_OS_Topoetcone20pt011',
            plot_all  = False,
            cut_flow  = [
              ['SumCosDPhi05',None],
              ['OS',None],
              ['InvMuonGradIso',["MuonWeightAI"]],
              ['Topoetcone20pt011',None],
              ],
            )

    loop += ztautau.algs.algs.PlotAlg(
            region    = 'AntiIsoCR_OSTopoetcone20pt012',
            plot_all  = False,
            cut_flow  = [
              ['SumCosDPhi05',None],
              ['OS',None],
              ['InvMuonGradIso',["MuonWeightAI"]],
              ['Topoetcone20pt012',None],
              ],
            )


    loop += ztautau.algs.algs.PlotAlg(
            region    = 'AntiIsoCR_OSTopoetcone20pt013',
            plot_all  = False,
            cut_flow  = [
              ['SumCosDPhi05',None],
              ['OS',None],
              ['Topoetcone20pt013',None],
              ['InvMuonGradIso',["MuonWeightAI"]],
              ],
            )


    loop += ztautau.algs.algs.PlotAlg(
            region    = 'AntiIsoCR_OS_Topoetcone20pt014',
            plot_all  = False,
            cut_flow  = [
              ['SumCosDPhi05',None],
              ['OS',None],
              ['Topoetcone20pt014',None],
              ['InvMuonGradIso',["MuonWeightAI"]],
              ],
            )


    loop += ztautau.algs.algs.PlotAlg(
            region    = 'AntiIsoCR_OS_Topoetcone20pt015',
            plot_all  = False,
            cut_flow  = [
              ['SumCosDPhi05',None],
              ['OS',None],
              ['InvMuonGradIso',["MuonWeightAI"]],
              ['Topoetcone20pt015',None],
              ],
            )


    loop += ztautau.algs.algs.PlotAlg(
            region    = 'AntiIsoCR_OS_Topoetcone20pt016',
            plot_all  = False,
            cut_flow  = [
              ['SumCosDPhi05',None],
              ['OS',None],
              ['InvMuonGradIso',["MuonWeightAI"]],
              ['Topoetcone20pt016',None],
              ],
            )


    loop += ztautau.algs.algs.PlotAlg(
            region    = 'AntiIsoCR_OS_Topoetcone20pt017',
            plot_all  = False,
            cut_flow  = [
              ['SumCosDPhi05',None],
              ['OS',None],
              ['InvMuonGradIso',["MuonWeightAI"]],
              ['Topoetcone20pt017',None],
              ],
            )

 
    loop += ztautau.algs.algs.PlotAlg(
            region    = 'AntiIsoCR_OS_Topoetcone20pt018',
            plot_all  = False,
            cut_flow  = [
              ['SumCosDPhi05',None],
              ['OS',None],
              ['InvMuonGradIso',["MuonWeightAI"]],
              ['Topoetcone20pt018',None],
              ],
            )

  
    loop += ztautau.algs.algs.PlotAlg(
            region    = 'AntiIsoCR_OS_Topoetcone20pt019',
            plot_all  = False,
            cut_flow  = [
              ['SumCosDPhi05',None],
              ['OS',None],
              ['InvMuonGradIso',["MuonWeightAI"]],
              ['Topoetcone20pt019',None],
              ],
            )

    loop += ztautau.algs.algs.PlotAlg(
            region    = 'AntiIsoCR_OS_Topoetcone20pt02',
            plot_all  = False,
            cut_flow  = [
              ['SumCosDPhi05',None],
              ['OS',None],
              ['InvMuonGradIso',["MuonWeightAI"]],
              ['Topoetcone20pt02',None],
              ],
            )
    loop += ztautau.algs.algs.PlotAlg(
            region    = 'AntiIsoCR_OS_Topoetcone20pt021',
            plot_all  = False,
            cut_flow  = [
              ['SumCosDPhi05',None],
              ['OS',None],
              ['InvMuonGradIso',["MuonWeightAI"]],
              ['Topoetcone20pt021',None],
              ],
            )

    loop += ztautau.algs.algs.PlotAlg(
            region    = 'AntiIsoCR_OSTopoetcone20pt022',
            plot_all  = False,
            cut_flow  = [
              ['SumCosDPhi05',None],
              ['OS',None],
              ['InvMuonGradIso',["MuonWeightAI"]],
              ['Topoetcone20pt022',None],
              ],
            )


    loop += ztautau.algs.algs.PlotAlg(
            region    = 'AntiIsoCR_OSTopoetcone20pt023',
            plot_all  = False,
            cut_flow  = [
              ['SumCosDPhi05',None],
              ['OS',None],
              ['Topoetcone20pt023',None],
              ['InvMuonGradIso',["MuonWeightAI"]],
              ],
            )


    loop += ztautau.algs.algs.PlotAlg(
            region    = 'AntiIsoCR_OS_Topoetcone20pt024',
            plot_all  = False,
            cut_flow  = [
              ['SumCosDPhi05',None],
              ['OS',None],
              ['Topoetcone20pt024',None],
              ['InvMuonGradIso',["MuonWeightAI"]],
              ],
            )


    loop += ztautau.algs.algs.PlotAlg(
            region    = 'AntiIsoCR_OS_Topoetcone20pt025',
            plot_all  = False,
            cut_flow  = [
              ['SumCosDPhi05',None],
              ['OS',None],
              ['InvMuonGradIso',["MuonWeightAI"]],
              ['Topoetcone20pt025',None],
              ],
            )

    loop += ztautau.algs.algs.PlotAlg(
            region    = 'AntiIsoCR_OS_Topoetcone20pt026',
            plot_all  = False,
            cut_flow  = [
              ['SumCosDPhi05',None],
              ['OS',None],
              ['InvMuonGradIso',["MuonWeightAI"]],
              ['Topoetcone20pt026',None],
              ],
            )


    loop += ztautau.algs.algs.PlotAlg(
            region    = 'AntiIsoCR_OS_Topoetcone20pt027',
            plot_all  = False,
            cut_flow  = [
              ['SumCosDPhi05',None],
              ['OS',None],
              ['InvMuonGradIso',["MuonWeightAI"]],
              ['Topoetcone20pt027',None],
              ],
            )

 
    loop += ztautau.algs.algs.PlotAlg(
            region    = 'AntiIsoCR_OS_Topoetcone20pt028',
            plot_all  = False,
            cut_flow  = [
              ['SumCosDPhi05',None],
              ['OS',None],
              ['InvMuonGradIso',["MuonWeightAI"]],
              ['Topoetcone20pt028',None],
              ],
            )

  
    loop += ztautau.algs.algs.PlotAlg(
            region    = 'AntiIsoCR_OS_Topoetcone20pt029',
            plot_all  = False,
            cut_flow  = [
              ['SumCosDPhi05',None],
              ['OS',None],
              ['InvMuonGradIso',["MuonWeightAI"]],
              ['Topoetcone20pt029',None],
              ],
            )



    loop += ztautau.algs.algs.PlotAlg(
            region    = 'AntiIsoCR_OS_Topoetcone20pt03',
            plot_all  = False,
            cut_flow  = [
              ['SumCosDPhi05',None],
              ['OS',None],
              ['InvMuonGradIso',["MuonWeightAI"]],
              ['Topoetcone20pt03',None],
              ],
            )

    loop += ztautau.algs.algs.PlotAlg(
            region    = 'AntiIsoCR_OS_Topoetcone20pt031',
            plot_all  = False,
            cut_flow  = [
              ['SumCosDPhi05',None],
              ['OS',None],
              ['InvMuonGradIso',["MuonWeightAI"]],
              ['Topoetcone20pt031',None],
              ],
            )

    loop += ztautau.algs.algs.PlotAlg(
            region    = 'AntiIsoCR_OSTopoetcone20pt032',
            plot_all  = False,
            cut_flow  = [
              ['SumCosDPhi05',None],
              ['OS',None],
              ['InvMuonGradIso',["MuonWeightAI"]],
              ['Topoetcone20pt032',None],
              ],
            )


    loop += ztautau.algs.algs.PlotAlg(
            region    = 'AntiIsoCR_OSTopoetcone20pt033',
            plot_all  = False,
            cut_flow  = [
              ['SumCosDPhi05',None],
              ['OS',None],
              ['Topoetcone20pt033',None],
              ['InvMuonGradIso',["MuonWeightAI"]],
              ],
            )


    loop += ztautau.algs.algs.PlotAlg(
            region    = 'AntiIsoCR_OS_Topoetcone20pt034',
            plot_all  = False,
            cut_flow  = [
              ['SumCosDPhi05',None],
              ['OS',None],
              ['Topoetcone20pt034',None],
              ['InvMuonGradIso',["MuonWeightAI"]],
              ],
            )


    loop += ztautau.algs.algs.PlotAlg(
            region    = 'AntiIsoCR_OS_Topoetcone20pt035',
            plot_all  = False,
            cut_flow  = [
              ['SumCosDPhi05',None],
              ['OS',None],
              ['InvMuonGradIso',["MuonWeightAI"]],
              ['Topoetcone20pt035',None],
              ],
            )

    loop += ztautau.algs.algs.PlotAlg(
            region    = 'AntiIsoCR_OS_Topoetcone20pt036',
            plot_all  = False,
            cut_flow  = [
              ['SumCosDPhi05',None],
              ['OS',None],
              ['InvMuonGradIso',["MuonWeightAI"]],
              ['Topoetcone20pt036',None],
              ],
            )


    loop += ztautau.algs.algs.PlotAlg(
            region    = 'AntiIsoCR_OS_Topoetcone20pt037',
            plot_all  = False,
            cut_flow  = [
              ['SumCosDPhi05',None],
              ['OS',None],
              ['InvMuonGradIso',["MuonWeightAI"]],
              ['Topoetcone20pt037',None],
              ],
            )

 
    loop += ztautau.algs.algs.PlotAlg(
            region    = 'AntiIsoCR_OS_Topoetcone20pt038',
            plot_all  = False,
            cut_flow  = [
              ['SumCosDPhi05',None],
              ['OS',None],
              ['InvMuonGradIso',["MuonWeightAI"]],
              ['Topoetcone20pt038',None],
              ],
            )

  
    loop += ztautau.algs.algs.PlotAlg(
            region    = 'AntiIsoCR_OS_Topoetcone20pt039',
            plot_all  = False,
            cut_flow  = [
              ['SumCosDPhi05',None],
              ['OS',None],
              ['InvMuonGradIso',["MuonWeightAI"]],
              ['Topoetcone20pt039',None],
              ],
            )

    loop += ztautau.algs.algs.PlotAlg(
            region    = 'AntiIsoCR_OS_Topoetcone20pt04',
            plot_all  = False,
            cut_flow  = [
              ['SumCosDPhi05',None],
              ['OS',None],
              ['InvMuonGradIso',["MuonWeightAI"]],
              ['Topoetcone20pt04',None],
              ],
            )


#########################

    loop += ztautau.algs.algs.PlotAlg(
            region    = 'AntiIsoCR_OS_25med',
            plot_all  = False,
            cut_flow  = [
              ['SumCosDPhi05',None],
              ['OS',None],
	      ['HLTTau25Med1TrackTwo',None],
              ['InvMuonGradIso',["MuonWeightAI"]],
              ],
            )

    loop += ztautau.algs.algs.PlotAlg(
            region    = 'AntiIsoCR_OS_25med_lowPT',
            plot_all  = False,
            cut_flow  = [
              ['SumCosDPhi05',None],
              ['OS',None],
	      ['HLTTau25Med1TrackTwo',None],
              ['InvMuonGradIso',["MuonWeightAI"]],
              ['TauLowPt',None],
              ],
            )

    loop += ztautau.algs.algs.PlotAlg(
            region    = 'AntiIsoCR_OS_25med_highPT',
            plot_all  = False,
            cut_flow  = [
              ['SumCosDPhi05',None],
              ['OS',None],
	      ['HLTTau25Med1TrackTwo',None],
              ['InvMuonGradIso',["MuonWeightAI"]],
              ['TauHighPt',None],
              ],
            )

    loop += ztautau.algs.algs.PlotAlg(
            region    = 'AntiIsoCR_OS_35med',
            plot_all  = False,
            cut_flow  = [
              ['SumCosDPhi05',None],
              ['OS',None],
	      ['HLTTau35Med1TrackTwo',None],
              ['InvMuonGradIso',["MuonWeightAI"]],
              ],
            )

    loop += ztautau.algs.algs.PlotAlg(
            region    = 'AntiIsoCR_OS_35med_lowPT',
            plot_all  = False,
            cut_flow  = [
              ['SumCosDPhi05',None],
              ['OS',None],
	      ['HLTTau35Med1TrackTwo',None],
              ['InvMuonGradIso',["MuonWeightAI"]],
              ['TauLowPt',None],
              ],
            )

    loop += ztautau.algs.algs.PlotAlg(
            region    = 'AntiIsoCR_OS_35med_highPT',
            plot_all  = False,
            cut_flow  = [
              ['SumCosDPhi05',None],
              ['OS',None],
	      ['HLTTau35Med1TrackTwo',None],
              ['InvMuonGradIso',["MuonWeightAI"]],
              ['TauHighPt',None],
              ],
            )

    loop += ztautau.algs.algs.PlotAlg(
            region    = 'AntiIsoCR_OS_highPT',
            plot_all  = False,
            cut_flow  = [
              ['SumCosDPhi05',None],
              ['OS',None],
	      ['TauHighPt',None],
              ['InvMuonGradIso',["MuonWeightAI"]],
              ],
            )

    loop += ztautau.algs.algs.PlotAlg(
            region    = 'AntiIsoCR_OS_lowPT',
            plot_all  = False,
            cut_flow  = [
              ['SumCosDPhi05',None],
              ['OS',None],
	      ['TauLowPt',None],
              ['InvMuonGradIso',["MuonWeightAI"]],
              ],
            )

    loop += ztautau.algs.algs.PlotAlg(
            region    = 'AntiIsoCR_SS',
            plot_all  = False,
            cut_flow  = [
              ['SumCosDPhi05',None],
              ['SS',None],
              ['InvMuonGradIso',["MuonWeightAI"]],
              ],
            )

    loop += ztautau.algs.algs.PlotAlg(
            region    = 'AntiIsoCR_SS_25med',
            plot_all  = False,
            cut_flow  = [
              ['SumCosDPhi05',None],
              ['SS',None],
	      ['HLTTau25Med1TrackTwo',None],
              ['InvMuonGradIso',["MuonWeightAI"]],
              ],
            )

    loop += ztautau.algs.algs.PlotAlg(
            region    = 'AntiIsoCR_SS_25med_lowPT',
            plot_all  = False,
            cut_flow  = [
              ['SumCosDPhi05',None],
              ['SS',None],
	      ['HLTTau25Med1TrackTwo',None],
              ['InvMuonGradIso',["MuonWeightAI"]],
              ['TauLowPt',None],
              ],
            )

    loop += ztautau.algs.algs.PlotAlg(
            region    = 'AntiIsoCR_SS_25med_highPT',
            plot_all  = False,
            cut_flow  = [
              ['SumCosDPhi05',None],
              ['SS',None],
	      ['HLTTau25Med1TrackTwo',None],
              ['InvMuonGradIso',["MuonWeightAI"]],
              ['TauHighPt',None],
              ],
            )

    loop += ztautau.algs.algs.PlotAlg(
            region    = 'AntiIsoCR_SS_35med',
            plot_all  = False,
            cut_flow  = [
              ['SumCosDPhi05',None],
              ['SS',None],
	      ['HLTTau35Med1TrackTwo',None],
              ['InvMuonGradIso',["MuonWeightAI"]],
              ],
            )

    loop += ztautau.algs.algs.PlotAlg(
            region    = 'AntiIsoCR_SS_35med_lowPT',
            plot_all  = False,
            cut_flow  = [
              ['SumCosDPhi05',None],
              ['SS',None],
	      ['HLTTau35Med1TrackTwo',None],
              ['InvMuonGradIso',["MuonWeightAI"]],
              ['TauLowPt',None],
              ],
            )

    loop += ztautau.algs.algs.PlotAlg(
            region    = 'AntiIsoCR_SS_35med_highPT',
            plot_all  = False,
            cut_flow  = [
              ['SumCosDPhi05',None],
              ['SS',None],
	      ['HLTTau35Med1TrackTwo',None],
              ['InvMuonGradIso',["MuonWeightAI"]],
              ['TauHighPt',None],
              ],
            )

    loop += ztautau.algs.algs.PlotAlg(
            region    = 'AntiIsoCR_SS_highPT',
            plot_all  = False,
            cut_flow  = [
              ['SumCosDPhi05',None],
              ['SS',None],
	      ['TauHighPt',None],
              ['InvMuonGradIso',["MuonWeightAI"]],
              ],
            )

    loop += ztautau.algs.algs.PlotAlg(
            region    = 'AntiIsoCR_SS_lowPT',
            plot_all  = False,
            cut_flow  = [
              ['SumCosDPhi05',None],
              ['SS',None],
	      ['TauLowPt',None],
              ['InvMuonGradIso',["MuonWeightAI"]],
              ],
            )
    """
    loop += ztautau.algs.algs.PlotAlg(
            region    = 'AntiIsoCR_OS_both',
            plot_all  = False,
            cut_flow  = [
              ['MTrans50',None],
              ['SumCosDPhi05',None],
              ['OS',None],
              ['InvMuonGradIso',["MuonWeightAI"]],
              ],
            )

    loop += ztautau.algs.algs.PlotAlg(
            region    = 'AntiIsoCR_OS_25med_both',
            plot_all  = False,
            cut_flow  = [
              ['MTrans50',None],
              ['SumCosDPhi05',None],
              ['OS',None],
	      ['HLTTau25Med1TrackTwo',None],
              ['InvMuonGradIso',["MuonWeightAI"]],
              ],
            )


    loop += ztautau.algs.algs.PlotAlg(
            region    = 'AntiIsoCR_OS_highPT_both',
            plot_all  = False,
            cut_flow  = [
              ['MTrans50',None],
              ['SumCosDPhi05',None],
              ['OS',None],
	      ['TauHighPt',None],
              ['InvMuonGradIso',["MuonWeightAI"]],
              ],
            )

    loop += ztautau.algs.algs.PlotAlg(
            region    = 'AntiIsoCR_OS_lowPT_both',
            plot_all  = False,
            cut_flow  = [
              ['MTrans50',None],
              ['SumCosDPhi05',None],
              ['OS',None],
	      ['TauLowPt',None],
              ['InvMuonGradIso',["MuonWeightAI"]],
              ],
            )

    loop += ztautau.algs.algs.PlotAlg(
            region    = 'AntiIsoCR_SS_both',
            plot_all  = False,
            cut_flow  = [
              ['MTrans50',None],
              ['SumCosDPhi05',None],
              ['SS',None],
              ['InvMuonGradIso',["MuonWeightAI"]],
              ],
            )

    loop += ztautau.algs.algs.PlotAlg(
            region    = 'AntiIsoCR_SS_25med_both',
            plot_all  = False,
            cut_flow  = [
              ['MTrans50',None],
              ['SumCosDPhi05',None],
              ['SS',None],
	      ['HLTTau25Med1TrackTwo',None],
              ['InvMuonGradIso',["MuonWeightAI"]],
              ],
            )


    loop += ztautau.algs.algs.PlotAlg(
            region    = 'AntiIsoCR_SS_highPT_both',
            plot_all  = False,
            cut_flow  = [
              ['MTrans50',None],
              ['SumCosDPhi05',None],
              ['SS',None],
	      ['TauHighPt',None],
              ['InvMuonGradIso',["MuonWeightAI"]],
              ],
            )

    loop += ztautau.algs.algs.PlotAlg(
            region    = 'AntiIsoCR_SS_lowPT_both',
            plot_all  = False,
            cut_flow  = [
              ['MTrans50',None],
              ['SumCosDPhi05',None],
              ['SS',None],
	      ['TauLowPt',None],
              ['InvMuonGradIso',["MuonWeightAI"]],
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



