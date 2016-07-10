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
    loop += ztautau.algs.algs.CutAlg(cutflow='presel',cut='MuonHLTmu20ilooseL1MU15ORmu50') #2015
    #loop += ztautau.algs.algs.CutAlg(cutflow='presel',cut='MuonHLTmu24imediumORHLTmu50') #2016
    #loop += ztautau.algs.algs.CutAlg(cutflow='presel',cut='MuonMuTrigMatch0HLTmu20ilooseL1MU15')

    #---- MUONS ----#

    loop += ztautau.algs.algs.CutAlg(cutflow='presel',cut='MuonIdMedium')
    loop += ztautau.algs.algs.CutAlg(cutflow='presel',cut='MuonPt22') #2015
    #loop += ztautau.algs.algs.CutAlg(cutflow='presel',cut='MuonPt26') #2016
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
              ['MuonGradIso',None],
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
              ['MuonGradIso',None],
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
              ['MuonGradIso',None],
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
              ['MuonGradIso',None],
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
              ['MuonGradIso',None],
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
              ['MuonGradIso',None],
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
              ['MuonGradIso',None],
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
              ['MuonGradIso',None],
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
              ['MuonGradIso',None],
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
              ['MuonGradIso',None],
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
              ['MuonGradIso',None],
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
              ['MuonGradIso',None],
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
              ['MuonGradIso',None],
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
              ['MuonGradIso',None],
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
              ['MuonGradIso',None],
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
              ['MuonGradIso',None],
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
              ['MuonGradIso',None],
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
              ['MuonGradIso',None],
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
              ['MuonGradIso',None],
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
              ['MuonGradIso',None],
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
              ['MuonGradIso',None],
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
              ['MuonGradIso',None],
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
              ['MuonGradIso',None],
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
              ['MuonGradIso',None],
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
              ['MuonGradIso',None],
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
              ['MuonGradIso',None],
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
              ['MuonGradIso',None],
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
              ['MuonGradIso',None],
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
              ['MuonGradIso',None],
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
              ['MuonGradIso',None],
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
              ['MuonGradIso',None],
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
              ['MuonGradIso',None],
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
              ['MuonGradIso',None],
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
              ['MuonGradIso',None],
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
              ['MuonGradIso',None],
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
              ['InvMuonGradIso',None],
              ['SumCosDPhi05',None],
              ['OS',None],
       	      ['Tau3Track',None],
              ],
            )

    loop += ztautau.algs.algs.PlotAlg(
            region    = 'AntiIsoCR_OS_25med_Tau3Track',
            plot_all  = False,
            cut_flow  = [
              ['InvMuonGradIso',None],
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
              ['InvMuonGradIso',None],
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
              ['InvMuonGradIso',None],
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
              ['InvMuonGradIso',None],
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
              ['InvMuonGradIso',None],
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
              ['InvMuonGradIso',None],
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
              ['InvMuonGradIso',None],
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
              ['InvMuonGradIso',None],
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
              ['InvMuonGradIso',None],
              ['SumCosDPhi05',None],
              ['SS',None],
       	      ['Tau3Track',None],
              ],
            )

    loop += ztautau.algs.algs.PlotAlg(
            region    = 'AntiIsoCR_SS_25med_Tau3Track',
            plot_all  = False,
            cut_flow  = [
              ['InvMuonGradIso',None],
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
              ['InvMuonGradIso',None],
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
              ['InvMuonGradIso',None],
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
              ['InvMuonGradIso',None],
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
              ['InvMuonGradIso',None],
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
              ['InvMuonGradIso',None],
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
              ['InvMuonGradIso',None],
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
              ['InvMuonGradIso',None],
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
              ['MuonGradIso',None],
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
              ['MuonGradIso',None],
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
              ['MuonGradIso',None],
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
              ['MuonGradIso',None],
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
              ['MuonGradIso',None],
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
              ['MuonGradIso',None],
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
              ['MuonGradIso',None],
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
              ['MuonGradIso',None],
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
              ['MuonGradIso',None],
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
              ['MuonGradIso',None],
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
              ['MuonGradIso',None],
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
              ['MuonGradIso',None],
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
              ['MuonGradIso',None],
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
              ['MuonGradIso',None],
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
              ['MuonGradIso',None],
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
              ['MuonGradIso',None],
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
              ['MuonGradIso',None],
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
              ['MuonGradIso',None],
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
              ['MuonGradIso',None],
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
              ['MuonGradIso',None],
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
              ['MuonGradIso',None],
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
              ['MuonGradIso',None],
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
              ['MuonGradIso',None],
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
              ['MuonGradIso',None],
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
              ['MuonGradIso',None],
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
              ['MuonGradIso',None],
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
              ['MuonGradIso',None],
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
              ['MuonGradIso',None],
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
              ['MuonGradIso',None],
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
              ['MuonGradIso',None],
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
              ['MuonGradIso',None],
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
              ['MuonGradIso',None],
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
              ['MuonGradIso',None],
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
              ['MuonGradIso',None],
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
              ['MuonGradIso',None],
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
              ['MuonGradIso',None],
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
              ['InvMuonGradIso',None],
              ['SumCosDPhi05',None],
              ['OS',None],
       	      ['Tau1Track',None],
              ],
            )

    loop += ztautau.algs.algs.PlotAlg(
            region    = 'AntiIsoCR_OS_25med_Tau1Track',
            plot_all  = False,
            cut_flow  = [
              ['InvMuonGradIso',None],
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
              ['InvMuonGradIso',None],
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
              ['InvMuonGradIso',None],
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
              ['InvMuonGradIso',None],
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
              ['InvMuonGradIso',None],
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
              ['InvMuonGradIso',None],
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
              ['InvMuonGradIso',None],
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
              ['InvMuonGradIso',None],
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
              ['InvMuonGradIso',None],
              ['SumCosDPhi05',None],
              ['SS',None],
       	      ['Tau1Track',None],
              ],
            )

    loop += ztautau.algs.algs.PlotAlg(
            region    = 'AntiIsoCR_SS_25med_Tau1Track',
            plot_all  = False,
            cut_flow  = [
              ['InvMuonGradIso',None],
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
              ['InvMuonGradIso',None],
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
              ['InvMuonGradIso',None],
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
              ['InvMuonGradIso',None],
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
              ['InvMuonGradIso',None],
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
              ['InvMuonGradIso',None],
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
              ['InvMuonGradIso',None],
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
              ['InvMuonGradIso',None],
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
              ['MuonGradIso',None],
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
              ['MuonGradIso',None],
              ],
            )


    loop += ztautau.algs.algs.PlotAlg(
            region    = 'Wjets_OS_lowPT',
            plot_all  = False,
            cut_flow  = [
              ['MTrans60',None],
              ['MET30',None],
              ['OS',None],
              ['MuonGradIso',None],
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
              ['MuonGradIso',None],
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
              ['MuonGradIso',None],
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
              ['MuonGradIso',None],
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
              ['MuonGradIso',None],
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
              ['MuonGradIso',None],
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
              ['MuonGradIso',None],
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
              ['MuonGradIso',None],
              ],
            )

    loop += ztautau.algs.algs.PlotAlg(
            region    = 'Wjets_SS_25med',
            plot_all  = False,
            cut_flow  = [
              ['MTrans60',None],
              ['MET30',None],
              ['SS',None],
              ['MuonGradIso',None],
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
              ['MuonGradIso',None],
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
              ['MuonGradIso',None],
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
              ['MuonGradIso',None],
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
              ['MuonGradIso',None],
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
              ['MuonGradIso',None],
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
              ['MuonGradIso',None],
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
              ['MuonGradIso',None],
	      ['TauLowPt',None],
              ],
            )

    loop += ztautau.algs.algs.PlotAlg(
            region    = 'SR_25med',
            plot_all  = False,
            cut_flow  = [
              ['MTrans50',None],
              ['SumCosDPhi05',None],
              ['MuonGradIso',None],
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
              ['MuonGradIso',None],
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
              ['MuonGradIso',None],
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
              ['MuonGradIso',None],
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
              ['MuonGradIso',None],
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
              ['MuonGradIso',None],
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
              ['MuonGradIso',None],
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
              ['MuonGradIso',None],
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
              ['MuonGradIso',None],
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
              ['MuonGradIso',None],
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
              ['MuonGradIso',None],
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
              ['MuonGradIso',None],
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
              ['MuonGradIso',None],
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
              ['MuonGradIso',None],
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
              ['MuonGradIso',None],
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
              ['MuonGradIso',None],
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
              ['MuonGradIso',None],
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
              ['MuonGradIso',None],
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
              ['InvMuonGradIso',None],
              ],
            )

    loop += ztautau.algs.algs.PlotAlg(
            region    = 'AntiIsoCR_OS_25med',
            plot_all  = False,
            cut_flow  = [
              ['SumCosDPhi05',None],
              ['OS',None],
	      ['HLTTau25Med1TrackTwo',None],
              ['InvMuonGradIso',None],
              ],
            )

    loop += ztautau.algs.algs.PlotAlg(
            region    = 'AntiIsoCR_OS_25med_lowPT',
            plot_all  = False,
            cut_flow  = [
              ['SumCosDPhi05',None],
              ['OS',None],
	      ['HLTTau25Med1TrackTwo',None],
              ['InvMuonGradIso',None],
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
              ['InvMuonGradIso',None],
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
              ['InvMuonGradIso',None],
              ],
            )

    loop += ztautau.algs.algs.PlotAlg(
            region    = 'AntiIsoCR_OS_35med_lowPT',
            plot_all  = False,
            cut_flow  = [
              ['SumCosDPhi05',None],
              ['OS',None],
	      ['HLTTau35Med1TrackTwo',None],
              ['InvMuonGradIso',None],
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
              ['InvMuonGradIso',None],
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
              ['InvMuonGradIso',None],
              ],
            )

    loop += ztautau.algs.algs.PlotAlg(
            region    = 'AntiIsoCR_OS_lowPT',
            plot_all  = False,
            cut_flow  = [
              ['SumCosDPhi05',None],
              ['OS',None],
	      ['TauLowPt',None],
              ['InvMuonGradIso',None],
              ],
            )

    loop += ztautau.algs.algs.PlotAlg(
            region    = 'AntiIsoCR_SS',
            plot_all  = False,
            cut_flow  = [
              ['SumCosDPhi05',None],
              ['SS',None],
              ['InvMuonGradIso',None],
              ],
            )

    loop += ztautau.algs.algs.PlotAlg(
            region    = 'AntiIsoCR_SS_25med',
            plot_all  = False,
            cut_flow  = [
              ['SumCosDPhi05',None],
              ['SS',None],
	      ['HLTTau25Med1TrackTwo',None],
              ['InvMuonGradIso',None],
              ],
            )

    loop += ztautau.algs.algs.PlotAlg(
            region    = 'AntiIsoCR_SS_25med_lowPT',
            plot_all  = False,
            cut_flow  = [
              ['SumCosDPhi05',None],
              ['SS',None],
	      ['HLTTau25Med1TrackTwo',None],
              ['InvMuonGradIso',None],
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
              ['InvMuonGradIso',None],
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
              ['InvMuonGradIso',None],
              ],
            )

    loop += ztautau.algs.algs.PlotAlg(
            region    = 'AntiIsoCR_SS_35med_lowPT',
            plot_all  = False,
            cut_flow  = [
              ['SumCosDPhi05',None],
              ['SS',None],
	      ['HLTTau35Med1TrackTwo',None],
              ['InvMuonGradIso',None],
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
              ['InvMuonGradIso',None],
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
              ['InvMuonGradIso',None],
              ],
            )

    loop += ztautau.algs.algs.PlotAlg(
            region    = 'AntiIsoCR_SS_lowPT',
            plot_all  = False,
            cut_flow  = [
              ['SumCosDPhi05',None],
              ['SS',None],
	      ['TauLowPt',None],
              ['InvMuonGradIso',None],
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
              ['InvMuonGradIso',None],
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
              ['InvMuonGradIso',None],
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
              ['InvMuonGradIso',None],
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
              ['InvMuonGradIso',None],
              ],
            )

    loop += ztautau.algs.algs.PlotAlg(
            region    = 'AntiIsoCR_SS_both',
            plot_all  = False,
            cut_flow  = [
              ['MTrans50',None],
              ['SumCosDPhi05',None],
              ['SS',None],
              ['InvMuonGradIso',None],
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
              ['InvMuonGradIso',None],
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
              ['InvMuonGradIso',None],
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
              ['InvMuonGradIso',None],
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



