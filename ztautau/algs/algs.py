#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
algs.py

This module contains a set of analysis specific algs 
for calculating variables, applying selection and 
plotting.
"""
from __future__ import division

## std modules
import itertools
import os
import math
import ROOT

## logging
import logging
log = logging.getLogger(__name__)

## python
from itertools import combinations

## pyframe
import pyframe

#import mcutils

GeV = 1000.0

#------------------------------------------------------------------------------
class CutAlg(pyframe.core.Algorithm):
    """
    Filtering alg for applying a single cut.  The predefined cuts must be
    implemeneted as a function with the prefix "cut_". One can then specify the
    cut to be applied by passing the cut=<cut name> in the constructor, which
    will execture the cut_<cut name>() function.
    """
    #__________________________________________________________________________
    def __init__(self,
                 name     = None,
                 cut      = None,
                 cutflow  = None,
                 isfilter = True,
                 ):
        pyframe.core.Algorithm.__init__(self, name if name else cut,isfilter=isfilter)
        self.cutflow = cutflow
         
    #__________________________________________________________________________
    def execute(self, weight):
        pyframe.core.Algorithm.execute(self, weight)

        return self.apply_cut(self.name)

    #__________________________________________________________________________
    def apply_cut(self,cutname):
        if self.store.has_key(cutname): return self.store[cutname]
        cut_function = 'cut_%s'%cutname
        assert hasattr(self,cut_function),"cut %s doesnt exist!'"%(cutname)
        self.store[cutname] = result = getattr(self,cut_function)()
        return result
    
    #__________________________________________________________________________
    def cut_AtLeastOneMuon(self):
        return self.chain.n_muons > 0
    #__________________________________________________________________________
    def cut_MuonPt24(self):
        return self.chain.lep_0_pt > 24.
    
   #__________________________________________________________________________
    # BASE CUT
    #__________________________________________________________________________

    def cut_OneMuon(self):
        return self.chain.n_muons == 1

    def cut_NoElectrons(self):
        return self.chain.n_electrons == 0

    def cut_AtLeastOneTau(self):
        return self.chain.n_taus >= 1

    def cut_NoBJets(self):
        return self.chain.n_bjets == 0

    def cut_AtLeastOnePvx(self):
        return self.chain.n_pvx >= 1

    def cut_MuonHLTmu20ilooseL1MU15ORmu40(self): #2015
	mutrig = bool(self.chain.HLT_mu20_iloose_L1MU15 == 1 and self.chain.muTrigMatch_0_HLT_mu20_iloose_L1MU15 ==1 )
	mutrig2 = bool(self.chain.HLT_mu40 == 1 and self.chain.muTrigMatch_0_HLT_mu40 == 1)
	return mutrig or mutrig2

    def cut_MuonHLTmu24imediumORHLTmu40(self): #2015
	mutrig = bool(self.chain.HLT_mu24_imedium == 1 and self.chain.muTrigMatch_0_HLT_mu24_imedium ==1 )
	mutrig2 = bool(self.chain.HLT_mu40 == 1 and self.chain.muTrigMatch_0_HLT_mu40 == 1)
	return mutrig or mutrig2

    def cut_MuonHLTmu24imediumORHLTmu50(self): #2016
	mutrig = bool(self.chain.HLT_mu24_imedium==1 and self.chain.muTrigMatch_0_HLT_mu24_imedium==1)
	mutrig2 = bool(self.chain.HLT_mu50==1 and self.chain.muTrigMatch_0_HLT_mu50==1)
	#return self.chain.HLT_mu24_imedium == 1 or self.chain.HLT_mu50 == 1
	return mutrig or mutrig2

    def cut_MuonHLTmu26ivarmediumORHLTmu50(self): #2016
	mutrig = bool(self.chain.HLT_mu26_ivarmedium==1 and self.chain.muTrigMatch_0_HLT_mu26_ivarmedium==1)
	mutrig2 = bool(self.chain.HLT_mu50==1 and self.chain.muTrigMatch_0_HLT_mu50==1)
	#return self.chain.HLT_mu24_imedium == 1 or self.chain.HLT_mu50 == 1
	#print "correct mu trig"
	return mutrig or mutrig2

    def cut_MuonHLTmuOptions(self):
        if "mc" in self.sampletype:
                run_number = self.chain.NOMINAL_pileup_random_run_number
        else:
                run_number = self.chain.run_number
        if run_number >= 276262 and run_number <= 284484:
                mutrig = bool(self.chain.HLT_mu20_iloose_L1MU15 == 1 and self.chain.muTrigMatch_0_HLT_mu20_iloose_L1MU15 ==1 )
                mutrig2 = bool(self.chain.HLT_mu40 == 1 and self.chain.muTrigMatch_0_HLT_mu40 == 1)
                return mutrig1 or mutrig2
        elif run_number >= 296939 and run_number <= 300287:
                mutrig = bool(self.chain.HLT_mu24_imedium == 1 and self.chain.muTrigMatch_0_HLT_mu24_imedium ==1 )
                mutrig2 = bool(self.chain.HLT_mu40 == 1 and self.chain.muTrigMatch_0_HLT_mu40 == 1)
                return mutrig or mutrig2
        elif run_number >= 300345 and run_number <= 302872:
                mutrig = bool(self.chain.HLT_mu24_imedium==1 and self.chain.muTrigMatch_0_HLT_mu24_imedium==1)
                mutrig2 = bool(self.chain.HLT_mu50==1 and self.chain.muTrigMatch_0_HLT_mu50==1)
                #return self.chain.HLT_mu24_imedium == 1 or self.chain.HLT_mu50 == 1
                return mutrig or mutrig2
        elif run_number >= 302919:
                mutrig = bool(self.chain.HLT_mu26_ivarmedium==1 and self.chain.muTrigMatch_0_HLT_mu26_ivarmedium==1)
                mutrig2 = bool(self.chain.HLT_mu50==1 and self.chain.muTrigMatch_0_HLT_mu50==1)
                #return self.chain.HLT_mu24_imedium == 1 or self.chain.HLT_mu50 == 1
                #print "correct mu trig"
                return mutrig or mutrig2

    def cut_MuonMuTrigMatch0HLTmu20ilooseL1MU15(self):
        return self.chain.muTrigMatch_0_HLT_mu20_iloose_L1MU15 == 1

    def cut_HLTtau25perfptonly(self):
	return self.chain.HLT_tau25_idperf_tracktwo_resurrected == 1

    def cut_HLTtau25perftracktwo(self):
	return self.chain.HLT_tau25_perf_tracktwo_resurrected ==1


    #__________________________________________________________________________
    # MUON CUT
    #__________________________________________________________________________

    def cut_MuonIdMedium(self):
        return self.chain.lep_0_id_medium == 1

    def cut_MuonPt22(self):
        return self.chain.lep_0_pt > 22.

    def cut_MuonPt26(self):
        return self.chain.lep_0_pt > 26.

    def cut_MuonPt28(self):
        return self.chain.lep_0_pt > 28.

    def cut_MuonPtOptions(self):
	if "mc" in self.sampletype:
                run_number = self.chain.NOMINAL_pileup_random_run_number
        else:
                run_number = self.chain.run_number
        if run_number >= 276262 and run_number <= 284484:
		return self.chain.lep_0_pt > 22.
        elif run_number >= 296939 and run_number <= 300287:
		return self.chain.lep_0_pt > 26.
        elif run_number >= 300345 and run_number <= 302872:
		return self.chain.lep_0_pt > 26.
        elif run_number >= 302919:
		return self.chain.lep_0_pt > 28.

    def cut_MuonGradIso(self):
        return self.chain.lep_0_iso_wp>=10000

    def cut_InvMuonGradIso(self):
        return self.chain.lep_0_iso_wp<10000

    def cut_MuonEta25(self):
        return abs(self.chain.lep_0_eta) < 2.5

    #__________________________________________________________________________
    # TAU CUT
    #__________________________________________________________________________

    def cut_TauPt25(self):
        return self.chain.tau_0_pt > 25.0

    def cut_TauEta247(self):
        return abs(self.chain.tau_0_eta) < 1.37 or 1.52 < abs(self.chain.tau_0_eta) < 2.47

    def cut_TauCharge1(self):
        return abs(self.chain.tau_0_q) == 1

    def cut_TauTrack(self):
        return self.chain.tau_0_n_tracks == 1 or self.chain.tau_0_n_tracks == 3

    def cut_Tau1Track(self):
        return self.chain.tau_0_n_tracks == 1

    def cut_Tau3Track(self):
        return self.chain.tau_0_n_tracks == 3

    def cut_BDTtauLoose(self):
        return self.chain.tau_0_jet_bdt_loose == 1

    def cut_BDTtauMed(self):
        return self.chain.tau_0_jet_bdt_medium == 1

    def cut_BDTtauTight(self):
        return self.chain.tau_0_jet_bdt_tight == 1
   
    def cut_TauLowPt(self):
	return self.chain.tau_0_pt < 35.0

    def cut_TauHighPt(self):
	return self.chain.tau_0_pt > 35.0

    def cut_TauPt30(self):
	return self.chain.tau_0_pt > 30.0

    def cut_TauPt40(self):
	return self.chain.tau_0_pt > 40.0

    def cut_TauPt55(self):
	return self.chain.tau_0_pt > 55.0

    def cut_TauPt85(self):
	return self.chain.tau_0_pt > 85.0

    def cut_TauPt130(self):
	return self.chain.tau_0_pt >130.0

    def cut_TauPt165(self):
	return self.chain.tau_0_pt >165.0
   #__________________________________________________________________________
    # REGIONS
    #__________________________________________________________________________

    #---- Wjets ----#

    def cut_MTrans60(self):
        return self.chain.lephad_mt_lep0_met > 60

    def cut_MET30(self):
        return self.chain.met_reco_et > 30

    #---- Control Region ----#

    def cut_MTrans50(self):
        return self.chain.lephad_mt_lep0_met < 50

    def cut_SumCosDPhi05(self):
        return self.chain.lephad_met_sum_cos_dphi > -0.5

    def cut_SumCosDPhi06(self):
        return self.chain.lephad_met_sum_cos_dphi < -0.6


    #---- Ztau ----#

    def cut_VisMass4580(self):
        return abs(self.chain.lephad_vis_mass) > 45 and abs(self.chain.lephad_vis_mass) < 80

    def cut_VisMass5585(self):
        return abs(self.chain.lephad_vis_mass) > 55 and abs(self.chain.lephad_vis_mass) < 85

    def cut_VisMass5590(self):
        return abs(self.chain.lephad_vis_mass) > 55 and abs(self.chain.lephad_vis_mass) < 90

    def cut_VisMass5595(self):
        return abs(self.chain.lephad_vis_mass) > 55 and abs(self.chain.lephad_vis_mass) < 95

    def cut_VisMass55100(self):
        return abs(self.chain.lephad_vis_mass) > 55 and abs(self.chain.lephad_vis_mass) < 100

    def cut_VisMass4585(self):
        return abs(self.chain.lephad_vis_mass) > 45 and abs(self.chain.lephad_vis_mass) < 85

    def cut_VisMass4590(self):
        return abs(self.chain.lephad_vis_mass) > 45 and abs(self.chain.lephad_vis_mass) < 90

    def cut_VisMass4595(self):
        return abs(self.chain.lephad_vis_mass) > 45 and abs(self.chain.lephad_vis_mass) < 95

    def cut_VisMass45100(self):
        return abs(self.chain.lephad_vis_mass) > 45 and abs(self.chain.lephad_vis_mass) < 100


    #---- GENERAL ----#

    def cut_OS(self):
        return self.chain.lephad_qxq==-1

    def cut_SS(self):
        return self.chain.lephad_qxq==1

    #-----TRIGGER-----#

    def cut_HLTTau25Med1TrackTwo(self):
	return self.chain.HLT_tau25_medium1_tracktwo_resurrected == 1    
 
    def cut_HLTTau35Med1TrackTwo(self):
	return self.chain.HLT_tau35_medium1_tracktwo_resurrected == 1    
 
    def cut_HLTTau50L1TAU12Med1TrackTwo(self):
        return self.chain.HLT_tau50_medium1_tracktwo_L1TAU12_resurrected == 1

    def cut_HLTTau80Med1TrackTwo(self):
        return self.chain.HLT_tau80_medium1_tracktwo_resurrected == 1

    def cut_HLTTau80L1TAU60Med1TrackTwo(self):
        return self.chain.HLT_tau80_medium1_tracktwo_L1TAU60_resurrected == 1

    def cut_HLTTau125Med1TrackTwo(self):
        return self.chain.HLT_tau125_medium1_tracktwo_resurrected == 1

    def cut_HLTTau160Med1TrackTwo(self):
        return self.chain.HLT_tau160_medium1_tracktwo_resurrected == 1

    def cut_HLTTauL1TAU12IMMed1TrackTwo(self):
        return self.chain.L1_TAU12IM_resurrected == 1


    #----- SYSTEMATICS----#

    def cut_Topoetcone20pt010(self):
         return (self.chain.lep_0_iso_topoetcone20/GeV)/self.chain.lep_0_pt < 0.1

    def cut_Topoetcone20pt011(self):
         return (self.chain.lep_0_iso_topoetcone20/GeV)/self.chain.lep_0_pt < 0.11

    def cut_Topoetcone20pt012(self):
         return (self.chain.lep_0_iso_topoetcone20/GeV)/self.chain.lep_0_pt < 0.12

    def cut_Topoetcone20pt013(self):
         return (self.chain.lep_0_iso_topoetcone20/GeV)/self.chain.lep_0_pt < 0.13

    def cut_Topoetcone20pt014(self):
         return (self.chain.lep_0_iso_topoetcone20/GeV)/self.chain.lep_0_pt < 0.14

    def cut_Topoetcone20pt015(self):
         return (self.chain.lep_0_iso_topoetcone20/GeV)/self.chain.lep_0_pt < 0.15

    def cut_Topoetcone20pt016(self):
         return (self.chain.lep_0_iso_topoetcone20/GeV)/self.chain.lep_0_pt < 0.16

    def cut_Topoetcone20pt017(self):
         return (self.chain.lep_0_iso_topoetcone20/GeV)/self.chain.lep_0_pt < 0.17

    def cut_Topoetcone20pt018(self):
         return (self.chain.lep_0_iso_topoetcone20/GeV)/self.chain.lep_0_pt < 0.18

    def cut_Topoetcone20pt019(self):
         return (self.chain.lep_0_iso_topoetcone20/GeV)/self.chain.lep_0_pt < 0.19

    def cut_Topoetcone20pt020(self):
         return (self.chain.lep_0_iso_topoetcone20/GeV)/self.chain.lep_0_pt < 0.2

    def cut_Topoetcone20pt021(self):
         return (self.chain.lep_0_iso_topoetcone20/GeV)/self.chain.lep_0_pt < 0.21

    def cut_Topoetcone20pt022(self):
         return (self.chain.lep_0_iso_topoetcone20/GeV)/self.chain.lep_0_pt < 0.22

    def cut_Topoetcone20pt023(self):
         return (self.chain.lep_0_iso_topoetcone20/GeV)/self.chain.lep_0_pt < 0.23

    def cut_Topoetcone20pt024(self):
         return (self.chain.lep_0_iso_topoetcone20/GeV)/self.chain.lep_0_pt < 0.24

    def cut_Topoetcone20pt025(self):
         return (self.chain.lep_0_iso_topoetcone20/GeV)/self.chain.lep_0_pt < 0.25

    def cut_Topoetcone20pt026(self):
         return (self.chain.lep_0_iso_topoetcone20/GeV)/self.chain.lep_0_pt < 0.26

    def cut_Topoetcone20pt027(self):
         return (self.chain.lep_0_iso_topoetcone20/GeV)/self.chain.lep_0_pt < 0.27

    def cut_Topoetcone20pt028(self):
         return (self.chain.lep_0_iso_topoetcone20/GeV)/self.chain.lep_0_pt < 0.28

    def cut_Topoetcone20pt029(self):
         return (self.chain.lep_0_iso_topoetcone20/GeV)/self.chain.lep_0_pt < 0.29

    def cut_Topoetcone20pt030(self):
         return (self.chain.lep_0_iso_topoetcone20/GeV)/self.chain.lep_0_pt < 0.3

    def cut_Topoetcone20pt031(self):
         return (self.chain.lep_0_iso_topoetcone20/GeV)/self.chain.lep_0_pt < 0.31

    def cut_Topoetcone20pt032(self):
         return (self.chain.lep_0_iso_topoetcone20/GeV)/self.chain.lep_0_pt < 0.32

    def cut_Topoetcone20pt033(self):
         return (self.chain.lep_0_iso_topoetcone20/GeV)/self.chain.lep_0_pt < 0.33

    def cut_Topoetcone20pt034(self):
         return (self.chain.lep_0_iso_topoetcone20/GeV)/self.chain.lep_0_pt < 0.34

    def cut_Topoetcone20pt035(self):
         return (self.chain.lep_0_iso_topoetcone20/GeV)/self.chain.lep_0_pt < 0.35

    def cut_Topoetcone20pt036(self):
         return (self.chain.lep_0_iso_topoetcone20/GeV)/self.chain.lep_0_pt < 0.36

    def cut_Topoetcone20pt037(self):
         return (self.chain.lep_0_iso_topoetcone20/GeV)/self.chain.lep_0_pt < 0.37

    def cut_Topoetcone20pt038(self):
         return (self.chain.lep_0_iso_topoetcone20/GeV)/self.chain.lep_0_pt < 0.38

    def cut_Topoetcone20pt039(self):
         return (self.chain.lep_0_iso_topoetcone20/GeV)/self.chain.lep_0_pt < 0.39

    def cut_Topoetcone20pt040(self):
         return (self.chain.lep_0_iso_topoetcone20/GeV)/self.chain.lep_0_pt < 0.4

    #################################

    def cut_Ptvarcone30pt010(self):
         return (self.chain.lep_0_iso_ptvarcone30/GeV)/self.chain.lep_0_pt < 0.1

    def cut_Ptvarcone30pt011(self):
         return (self.chain.lep_0_iso_ptvarcone30/GeV)/self.chain.lep_0_pt < 0.11

    def cut_Ptvarcone30pt012(self):
         return (self.chain.lep_0_iso_ptvarcone30/GeV)/self.chain.lep_0_pt < 0.12

    def cut_Ptvarcone30pt013(self):
         return (self.chain.lep_0_iso_ptvarcone30/GeV)/self.chain.lep_0_pt < 0.13

    def cut_Ptvarcone30pt014(self):
         return (self.chain.lep_0_iso_ptvarcone30/GeV)/self.chain.lep_0_pt < 0.14

    def cut_Ptvarcone30pt015(self):
         return (self.chain.lep_0_iso_ptvarcone30/GeV)/self.chain.lep_0_pt < 0.15

    def cut_Ptvarcone30pt016(self):
         return (self.chain.lep_0_iso_ptvarcone30/GeV)/self.chain.lep_0_pt < 0.16

    def cut_Ptvarcone30pt017(self):
         return (self.chain.lep_0_iso_ptvarcone30/GeV)/self.chain.lep_0_pt < 0.17

    def cut_Ptvarcone30pt018(self):
         return (self.chain.lep_0_iso_ptvarcone30/GeV)/self.chain.lep_0_pt < 0.18

    def cut_Ptvarcone30pt019(self):
         return (self.chain.lep_0_iso_ptvarcone30/GeV)/self.chain.lep_0_pt < 0.19

    def cut_Ptvarcone30pt020(self):
         return (self.chain.lep_0_iso_ptvarcone30/GeV)/self.chain.lep_0_pt < 0.2

    def cut_Ptvarcone30pt021(self):
         return (self.chain.lep_0_iso_ptvarcone30/GeV)/self.chain.lep_0_pt < 0.21

    def cut_Ptvarcone30pt022(self):
         return (self.chain.lep_0_iso_ptvarcone30/GeV)/self.chain.lep_0_pt < 0.22

    def cut_Ptvarcone30pt023(self):
         return (self.chain.lep_0_iso_ptvarcone30/GeV)/self.chain.lep_0_pt < 0.23

    def cut_Ptvarcone30pt024(self):
         return (self.chain.lep_0_iso_ptvarcone30/GeV)/self.chain.lep_0_pt < 0.24

    def cut_Ptvarcone30pt025(self):
         return (self.chain.lep_0_iso_ptvarcone30/GeV)/self.chain.lep_0_pt < 0.25

    def cut_Ptvarcone30pt026(self):
         return (self.chain.lep_0_iso_ptvarcone30/GeV)/self.chain.lep_0_pt < 0.26

    def cut_Ptvarcone30pt027(self):
         return (self.chain.lep_0_iso_ptvarcone30/GeV)/self.chain.lep_0_pt < 0.27

    def cut_Ptvarcone30pt028(self):
         return (self.chain.lep_0_iso_ptvarcone30/GeV)/self.chain.lep_0_pt < 0.28

    def cut_Ptvarcone30pt029(self):
         return (self.chain.lep_0_iso_ptvarcone30/GeV)/self.chain.lep_0_pt < 0.29

    def cut_Ptvarcone30pt030(self):
         return (self.chain.lep_0_iso_ptvarcone30/GeV)/self.chain.lep_0_pt < 0.3

    def cut_Ptvarcone30pt031(self):
         return (self.chain.lep_0_iso_ptvarcone30/GeV)/self.chain.lep_0_pt < 0.31

    def cut_Ptvarcone30pt032(self):
         return (self.chain.lep_0_iso_ptvarcone30/GeV)/self.chain.lep_0_pt < 0.32

    def cut_Ptvarcone30pt033(self):
         return (self.chain.lep_0_iso_ptvarcone30/GeV)/self.chain.lep_0_pt < 0.33

    def cut_Ptvarcone30pt034(self):
         return (self.chain.lep_0_iso_ptvarcone30/GeV)/self.chain.lep_0_pt < 0.34

    def cut_Ptvarcone30pt035(self):
         return (self.chain.lep_0_iso_ptvarcone30/GeV)/self.chain.lep_0_pt < 0.35

    def cut_Ptvarcone30pt036(self):
         return (self.chain.lep_0_iso_ptvarcone30/GeV)/self.chain.lep_0_pt < 0.36

    def cut_Ptvarcone30pt037(self):
         return (self.chain.lep_0_iso_ptvarcone30/GeV)/self.chain.lep_0_pt < 0.37

    def cut_Ptvarcone30pt038(self):
         return (self.chain.lep_0_iso_ptvarcone30/GeV)/self.chain.lep_0_pt < 0.38

    def cut_Ptvarcone30pt039(self):
         return (self.chain.lep_0_iso_ptvarcone30/GeV)/self.chain.lep_0_pt < 0.39

    def cut_Ptvarcone30pt040(self):
         return (self.chain.lep_0_iso_ptvarcone30/GeV)/self.chain.lep_0_pt < 0.4
 
    ################################   
    def cut_MTrans625(self):
         return self.chain.lephad_mt_lep0_met > 62.5

    def cut_MTrans675(self):
         return self.chain.lephad_mt_lep0_met > 67.5

    def cut_MTrans725(self):
         return self.chain.lephad_mt_lep0_met > 72.5

    def cut_MTrans775(self):
         return self.chain.lephad_mt_lep0_met > 77.5

    def cut_MTrans825(self):
         return self.chain.lephad_mt_lep0_met > 82.5

    def cut_MTrans875(self):
         return self.chain.lephad_mt_lep0_met > 87.5

    def cut_MTrans925(self):
         return self.chain.lephad_mt_lep0_met > 92.5

    def cut_MTrans975(self):
         return self.chain.lephad_mt_lep0_met > 97.5

    def cut_MTrans1025(self):
         return self.chain.lephad_mt_lep0_met > 102.5

    def cut_MTrans1075(self):
         return self.chain.lephad_mt_lep0_met > 107.5
#------------------------------------------------------------------------------
class PlotAlg(pyframe.algs.CutFlowAlg,CutAlg):
    """

    For making a set of standard plots after each cut in a cutflow.  PlotAlg
    inherets from CutAlg so all the functionality from CutAlg is available for
    applying selection. In addition you can apply weights at different points
    in the selection.

    The selection should be configured by specifying 'cut_flow' in the
    constructor as such:

    cut_flow = [
        ['Cut1', ['Weight1a','Weight1b'],
        ['Cut2', ['Weight2']],
        ['Cut3', None],
        ...
        ]

    The weights must be available in the store.

    'region' will set the name of the dir where the plots are saved

    Inhereting from CutFlowAlg provides the functionality to produce cutflow
    histograms that will be named 'cutflow_<region>' and 'cutflow_raw_<region>'

    """
    #__________________________________________________________________________
    def __init__(self,
                 name     = 'PlotAlg',
                 region   = '',
                 obj_keys = [], # make cutflow hist for just this objects
                 cut_flow = None,
                 plot_all = True,
                 ):
        pyframe.algs.CutFlowAlg.__init__(self,key=region,obj_keys=obj_keys)
        CutAlg.__init__(self,name,isfilter=False)
        self.cut_flow = cut_flow
        self.region   = region
        self.plot_all = plot_all
        self.obj_keys = obj_keys
    
    #_________________________________________________________________________
    def initialize(self):
        pyframe.algs.CutFlowAlg.initialize(self)
    #_________________________________________________________________________
    def execute(self, weight):
   
        # next line fills in the cutflow hists
        # the first bin of the cutflow does not
        # take into account object weights
        pyframe.algs.CutFlowAlg.execute(self, weight)

        list_cuts = []
        for cut, list_weights in self.cut_flow:
            ## apply weights for this cut
            if list_weights:
              for w in list_weights: weight *= self.store[w]

            list_cuts.append(cut)
            passed = self.check_region(list_cuts)
            self.hists[self.region].count_if(passed, cut, weight)

            ## if plot_all is True, plot after each cut, 
            ## else only plot after full selection
            
            if (self.plot_all or len(list_cuts)==len(self.cut_flow)):
               region_name = os.path.join(self.region,'_'.join(list_cuts))
               region_name = region_name.replace('!', 'N')
               region = os.path.join('/regions/', region_name)
               
               self.plot(region, passed, list_cuts, cut, list_weights=list_weights, weight=weight)

        return True

    #__________________________________________________________________________
    def finalize(self):
        pyframe.algs.CutFlowAlg.finalize(self)

    #__________________________________________________________________________
    def plot(self, region, passed, list_cuts, cut, list_weights=None, weight=1.0):
        
        # should probably make this configurable
        
        ## plot directories
        EVT   = os.path.join(region, 'event')
        MET   = os.path.join(region, 'met')
        MUONS = os.path.join(region, 'muons')
        TAUS  = os.path.join(region, 'taus')

        self.h_topoetcone20pt = self.hist('h_topoetcone20pt', "ROOT.TH1F('$', ';TopoEtCone20/p_{T};Events', 100, -0.5, 0.5)", dir=MUONS)
        self.h_ptvarcone30pt = self.hist('h_ptvarcone30pt', "ROOT.TH1F('$', ';PtVarCone30/p_{T};Events', 100, -0.5, 0.5)", dir=MUONS)
 
        self.h_topoetcone20 = self.hist('h_topoetcone20', "ROOT.TH1F('$', ';TopoEtCone20(GeV);Events', 220, -20, 200)", dir=MUONS)
        self.h_ptvarcone30 = self.hist('h_ptvarcone30', "ROOT.TH1F('$', ';PtVarCone30(GeV);Events', 330, -30, 300)", dir=MUONS)

        self.h_HLT_tau_eta = self.hist('h_HLT_tau_eta', "ROOT.TH1F('$', ';  HLT \eta ;Events', 24, -6.0, 6.0)", dir=TAUS)

        self.h_HLT_tau_phi = self.hist('h_HLT_tau_phi', "ROOT.TH1F('$', ';  HLT \phi ;Events', 20, -5.0, 5.0)", dir=TAUS)

        self.h_HLT_tau_pt = self.hist('h_HLT_tau_pt', "ROOT.TH1F('$', ';HLT p_{T} [GeV];Events', 1000, 0.0, 1000.0)", dir=TAUS)

        self.h_HLT_jet_bdt_score = self.hist('h_HLT_jet_bdt_score', "ROOT.TH1F('$', ';  HLT BDT score ;Events', 54, -1.0, 2.0)", dir=TAUS)

        self.h_HLT_tau_n_tracks = self.hist('h_HLT_tau_n_tracks', "ROOT.TH1F('$', ';  HLT N_{tracks} ;Events', 5, 0.0, 5.0)", dir=TAUS)

        self.h_HLT_tau_n_wide_tracks = self.hist('h_HLT_tau_n_wide_tracks', "ROOT.TH1F('$', '; HLT N_{wide tracks} ;Events', 5, 0.0, 5.0)", dir=TAUS)

        self.h_HLT_pt_res = self.hist('h_HLT_pt_res', "ROOT.TH1F('$', ';HLT p_{T} resolution;Events', 2000, -10.0, 10.0)", dir=TAUS)

        self.h_HLT_pt_res_TProfile = self.hist('h_HLT_pt_res_TProfile', "ROOT.TProfile('h_HLT_pt_res_TProfile','h_HLT_pt_res_TProfile', 2000, 0, 50.0, 0,1000)", dir=TAUS)


        self.h_HLT_fcent = self.hist('h_HLT_fcent', "ROOT.TH1F('$', ';f_{cent};Events', 40, 0, 1.0)", dir=TAUS)
        
	self.h_HLT_ratio_energy_to_trk_p = self.hist('h_HLT_ratio_energy_to_trk_p', "ROOT.TH1F('$', ';f_{track}^{EM};Events', 40, 0, 10)", dir=TAUS)

	self.h_HLT_frac_EM_from_charged_pions = self.hist('h_HLT_frac_EM_from_charged_pions', "ROOT.TH1F('$', ';f_{EM}^{track-HAD};Events', 40, -1.0, 1.0)", dir=TAUS)

	self.h_HLT_lead_trk_p_frac = self.hist('h_HLT_lead_trk_p_frac', "ROOT.TH1F('$', ';f^{-1}_{lead track};Events', 40, 0, 10)", dir=TAUS)

	self.h_HLT_trk_radius = self.hist('h_HLT_trk_radius', "ROOT.TH1F('$', ';R_{track};Events', 40, 0, 0.2)", dir=TAUS)
	
	self.h_HLT_3P_dRmax = self.hist('h_HLT_3P_dRmax', "ROOT.TH1F('$', ';#Delta R_{max};Events', 40, 0, 0.2)", dir=TAUS)

	self.h_HLT_1P_lead_trk_IP_sig = self.hist('h_HLT_1P_lead_trk_IP_sig', "ROOT.TH1F('$', ';S_{lead track};Events', 40, 0, 2.0)", dir=TAUS)

	self.h_HLT_m_trk_EM_system = self.hist('h_HLT_m_trk_EM_system', "ROOT.TH1F('$', ';m_{#pi ^{0} + track}[MeV];Events', 40, 0, 6000)", dir=TAUS)

	self.h_HLT_1P_frac_trks_iso_region = self.hist('h_HLT_1P_frac_trks_iso_region', "ROOT.TH1F('$', ';f_{iso}^{track};Events', 40,  0, 1.0)", dir=TAUS)

	self.h_HLT_ratio_trkemsys_pt = self.hist('h_HLT_ratio_trkemsys_pt', "ROOT.TH1F('$', ';P_{T}^{EM+track}/P_{T};Events', 40, 0, 3.0)", dir=TAUS)

	self.h_HLT_3P_massTrkSysCorrected = self.hist('h_HLT_3P_massTrkSysCorrected', "ROOT.TH1F('$', ';m_{track}[MeV];Events', 40, 0, 6000)", dir=TAUS)

	self.h_HLT_3P_trans_flightpath_sig = self.hist('h_HLT_3P_trans_flightpath_sig', "ROOT.TH1F('$', ';S_{T}^{flight};Events', 40, -10, 10)", dir=TAUS)


        self.h_Presel_tau_eta = self.hist('h_Presel_tau_eta', "ROOT.TH1F('$', ';  HLT \eta ;Events', 24, -6.0, 6.0)", dir=TAUS)

        self.h_Presel_tau_phi = self.hist('h_Presel_tau_phi', "ROOT.TH1F('$', ';  HLT \phi ;Events', 20, -5.0, 5.0)", dir=TAUS)

        self.h_Presel_tau_n_tracks = self.hist('h_Presel_tau_n_tracks', "ROOT.TH1F('$', ';  HLT N_{tracks} ;Events', 5, 0.0, 5.0)", dir=TAUS)

        self.h_Presel_tau_n_wide_tracks = self.hist('h_Presel_tau_n_wide_tracks', "ROOT.TH1F('$', '; HLT N_{wide tracks} ;Events', 5, 0.0, 5.0)", dir=TAUS)

        self.h_Presel_tau_pt = self.hist('h_Presel_tau_pt', "ROOT.TH1F('$', ';HLT p_{T} [GeV];Events', 1000, 0.0, 1000.0)", dir=TAUS)

        self.h_pileup = self.hist('h_pileup', "ROOT.TH1F('$', ';<#mu>;Events', 60, 0, 60)", dir=EVT)

        self.h_nmuons = self.hist('h_nmuons', "ROOT.TH1F('$', ';N_{#mu};Events', 8, 0, 8)", dir=EVT)

        self.h_met_reco_et = self.hist('h_met_reco_et', "ROOT.TH1F('$', ';E^{miss}_{T} [GeV];Events', 1000, 0.0, 1000.0)", dir=MET)

        self.h_mu_pt = self.hist('h_mu_pt', "ROOT.TH1F('$', ';p_{T}(\mu) [GeV];Events', 1000, 0.0, 1000.0)", dir=MUONS)

        self.h_tau_pt = self.hist('h_tau_pt', "ROOT.TH1F('$', ';p_{T}(#tau) [GeV];Events', 1000, 0.0, 1000.0)", dir=TAUS)

        self.h_n_vx = self.hist('h_n_vx', "ROOT.TH1F('$', ';N_{vx} ;Events', 14, 0.0, 14.0)", dir=EVT)

        self.h_n_bjets = self.hist('h_n_bjets', "ROOT.TH1F('$', ';N_{bjets} ;Events', 5, 0.0, 5.0)", dir=EVT)

        self.h_n_jets = self.hist('h_n_jets', "ROOT.TH1F('$', ';N_{jets} ;Events', 19, 0.0, 19.0)", dir=EVT)

        self.h_vis_mass = self.hist('h_vis_mass', "ROOT.TH1F('$', ';Visible Mass (#tau,#mu) [GeV];Events', 200, 0.0, 200.0)", dir=EVT)

        self.h_sumcosdphi = self.hist('h_sumcosdphi', "ROOT.TH1F('$', ';\sum\cos(\Delta \phi) ;Events', 40, -2.0, 2.0)", dir=EVT)

        self.h_lowsumcosdphi = self.hist('h_lowsumcosdphi', "ROOT.TH1F('$', ';\sum\cos(\Delta \phi) ;Events', 10, -2.0, -0.6)", dir=EVT)

        self.h_m_trans = self.hist('h_m_trans', "ROOT.TH1F('$', ';m_T (\mu,E^{miss}_{T}) [GeV];Events', 200, 0.0, 200.0)", dir=EVT)

        self.h_tau_eta = self.hist('h_tau_eta', "ROOT.TH1F('$', '; \eta ;Events', 12, -3.0, 3.0)", dir=TAUS)

        self.h_tau_phi = self.hist('h_tau_phi', "ROOT.TH1F('$', '; \phi ;Events', 16, -4.0, 4.0)", dir=TAUS)

        self.h_mu_eta = self.hist('h_mu_eta', "ROOT.TH1F('$', '; \eta ;Events', 12, -3.0, 3.0)", dir=MUONS)

        self.h_mu_phi = self.hist('h_mu_phi', "ROOT.TH1F('$', '; \phi ;Events', 16, -4.0, 4.0)", dir=MUONS)

        self.h_met_reco_phi = self.hist('h_met_reco_phi', "ROOT.TH1F('$', '; \phi ;Events', 16, -4.0, 4.0)", dir=MET)

        self.h_tau_n_tracks = self.hist('h_tau_n_tracks', "ROOT.TH1F('$', '; N_{tracks} ;Events', 5, 0.0, 5.0)", dir=TAUS)
        
	self.h_jet_bdt_score = self.hist('h_jet_bdt_score', "ROOT.TH1F('$', '; BDT score ;Events', 20, 0.6, 1.0)", dir=TAUS)

        self.h_m_trans_vs_sumcosdphi = self.hist('h_m_trans_vs_sumcosdphi', "ROOT.TH2F('$', '; m_T (\mu,E^{miss}_{T}) vs \sum\cos(\Delta \phi)', 200, 0.0, 200.0, 20, -2.0, 2.0)", dir=TAUS)

        self.h_met_reco_et_vs_sumcosdphi = self.hist('h_met_reco_et_vs_sumcosdphi', "ROOT.TH2F('$', '; E^{miss}_{T} [GeV] vs \sum\cos(\Delta \phi)', 1000, 0.0, 1000.0, 20, -2.0, 2.0)", dir=TAUS)

        self.h_met_reco_et_vs_m_trans = self.hist('h_met_reco_et_vs_m_trans', "ROOT.TH2F('$', '; E^{miss}_{T} [GeV] vs m_T (\mu,E^{miss}_{T})', 1000, 0.0, 1000.0, 200, 0.0, 200.0)", dir=TAUS)

        if passed:

	     self.h_m_trans_vs_sumcosdphi.Fill(self.chain.lephad_mt_lep0_met, self.chain.lephad_met_sum_cos_dphi, weight)
	     self.h_met_reco_et_vs_sumcosdphi.Fill(self.chain.met_reco_et, self.chain.lephad_met_sum_cos_dphi, weight)
	     self.h_met_reco_et_vs_m_trans.Fill(self.chain.met_reco_et, self.chain.lephad_mt_lep0_met, weight)

             self.h_topoetcone20.Fill(self.chain.lep_0_iso_topoetcone20/GeV, weight)
             self.h_ptvarcone30.Fill(self.chain.lep_0_iso_ptvarcone30/GeV, weight)
 
             self.h_HLT_tau_eta.Fill(self.chain.tau_0_trig1_HLT_eta, weight)
             self.h_HLT_tau_phi.Fill(self.chain.tau_0_trig1_HLT_phi, weight) 
             self.h_HLT_tau_pt.Fill(self.chain.tau_0_trig1_HLT_pt, weight) 
             self.h_HLT_jet_bdt_score.Fill(self.chain.tau_0_trig1_HLT_jet_bdt_score, weight) 
             self.h_HLT_tau_n_tracks.Fill(self.chain.tau_0_trig1_HLT_n_tracks, weight)
             self.h_HLT_tau_n_wide_tracks.Fill(self.chain.tau_0_trig1_HLT_n_wide_tracks, weight)
             if self.chain.tau_0_pt>0:
		#print "fillinf pt res", (self.chain.tau_0_trig1_HLT_pt - self.chain.tau_0_pt)/self.chain.tau_0_pt
	     	self.h_HLT_pt_res.Fill( (self.chain.tau_0_trig1_HLT_pt - self.chain.tau_0_pt)/self.chain.tau_0_pt ,weight)
	     else:
		self.h_HLT_pt_res.Fill( 0 , weight)
            
	     self.h_HLT_pt_res_TProfile.Fill(self.chain.n_avg_int_cor, self.chain.tau_0_trig1_HLT_pt - self.chain.tau_0_pt, weight)

             self.h_HLT_fcent.Fill( self.chain.tau_0_trig1_HLT_centFracCorrected, weight)
        
	     self.h_HLT_ratio_energy_to_trk_p.Fill( self.chain.tau_0_trig1_HLT_EMPOverTrkSysPCorrected, weight)

	     self.h_HLT_frac_EM_from_charged_pions.Fill(self.chain.tau_0_trig1_HLT_ChPiEMEOverCaloEMECorrected, weight)

	     self.h_HLT_lead_trk_p_frac.Fill(self.chain.tau_0_trig1_HLT_etOverPtLeadTrkCorrected, weight)

	     self.h_HLT_trk_radius.Fill(self.chain.tau_0_trig1_HLT_innerTrkAvgDistCorrected, weight)

	     self.h_HLT_1P_lead_trk_IP_sig.Fill(self.chain.tau_0_trig1_HLT_ipSigLeadTrkCorrected, weight)

	     self.h_HLT_m_trk_EM_system.Fill(self.chain.tau_0_trig1_HLT_mEflowApproxCorrected, weight)

	     self.h_HLT_1P_frac_trks_iso_region.Fill(self.chain.tau_0_trig1_HLT_SumPtTrkFrac, weight)

             self.h_HLT_ratio_trkemsys_pt.Fill(self.chain.tau_0_trig1_HLT_ptRatioEflowApproxCorrected, weight)

 	     self.h_HLT_3P_dRmax.Fill(self.chain.tau_0_trig1_HLT_dRmaxCorrected, weight)

             self.h_HLT_3P_massTrkSysCorrected.Fill(self.chain.tau_0_trig1_HLT_massTrkSysCorrected*1000, weight)

             self.h_HLT_3P_trans_flightpath_sig.Fill(self.chain.tau_0_trig1_HLT_trFlightPathSigCorrected, weight)

             self.h_Presel_tau_eta.Fill(self.chain.tau_0_trig2_PreselTrig_eta, weight)
             self.h_Presel_tau_phi.Fill(self.chain.tau_0_trig2_PreselTrig_phi, weight) 
             self.h_Presel_tau_pt.Fill(self.chain.tau_0_trig2_PreselTrig_pt, weight) 
             self.h_Presel_tau_n_tracks.Fill(self.chain.tau_0_trig2_PreselTrig_n_tracks, weight)
             self.h_Presel_tau_n_wide_tracks.Fill(self.chain.tau_0_trig2_PreselTrig_n_wide_tracks, weight)

             self.h_topoetcone20pt.Fill( (self.chain.lep_0_iso_topoetcone20/GeV)/self.chain.lep_0_pt, weight)
             self.h_ptvarcone30pt.Fill( (self.chain.lep_0_iso_ptvarcone30/GeV)/self.chain.lep_0_pt, weight)


             self.h_pileup.Fill(self.chain.n_avg_int_cor, weight)

             self.h_nmuons.Fill(self.chain.n_muons, weight)
 
             self.h_met_reco_et.Fill(self.chain.met_reco_et, weight)
 
             self.h_mu_pt.Fill(self.chain.lep_0_pt, weight)
 
             self.h_tau_pt.Fill(self.chain.tau_0_pt, weight)
 
             self.h_n_vx.Fill(self.chain.n_vx, weight)

             self.h_n_jets.Fill(self.chain.n_jets, weight)

             self.h_n_bjets.Fill(self.chain.n_bjets, weight) 

             self.h_vis_mass.Fill(self.chain.lephad_vis_mass, weight)
 
             self.h_sumcosdphi.Fill(self.chain.lephad_met_sum_cos_dphi, weight)

             self.h_lowsumcosdphi.Fill(self.chain.lephad_met_sum_cos_dphi, weight)
 
             self.h_m_trans.Fill(self.chain.lephad_mt_lep0_met, weight)
 
             self.h_tau_eta.Fill(self.chain.tau_0_eta, weight)
 
             self.h_tau_phi.Fill(self.chain.tau_0_phi, weight)
 
             self.h_mu_eta.Fill(self.chain.lep_0_eta, weight)
 
             self.h_mu_phi.Fill(self.chain.lep_0_phi, weight)
 
             self.h_met_reco_phi.Fill(self.chain.met_reco_phi, weight)
 
             self.h_tau_n_tracks.Fill(self.chain.tau_0_n_tracks, weight)
             
 	     self.h_jet_bdt_score.Fill(self.chain.tau_0_jet_bdt_score, weight)


    #__________________________________________________________________________
    def check_region(self,cutnames):
        cut_passed = True
        for cn in cutnames:
            ## could use this to fail when cuts not available
            #if not cuts.has_key(cn): return False
    
            ## pass if None
            if cn == 'ALL': continue

            if cn.startswith('!'):
                cut_passed = not self.apply_cut(cn[1:])
            else:
                cut_passed = self.apply_cut(cn) and cut_passed
            #if not cut_passed:
            #    return False
        return cut_passed
    

#------------------------------------------------------------------------------
class VarsAlg(pyframe.core.Algorithm):
    """
    
    calcualtes derived quantities, like masses, dphi etc...

    """
    #__________________________________________________________________________
    def __init__(self, 
                 name ='VarsAlg',
                 key_muons = 'muons',
                 #key_met = 'met',
                 ):
        pyframe.core.Algorithm.__init__(self, name)
        self.key_muons = key_muons
        #self.key_met = key_met

    #__________________________________________________________________________
    def execute(self, weight):
        pyframe.core.Algorithm.execute(self, weight)
        """
        computes variables and puts them in the store
        """

        ## get objects from event candidate
        ## --------------------------------------------------
        assert self.store.has_key(self.key_muons), "muons key: %s not found in store!" % (self.key_muons)
        muons = self.store[self.key_muons]
        #assert len(muons)>=2, "less than 2 muons in event!"
        
        #assert self.store.has_key(self.key_met), "met key: %s not found in store!" % (self.key_met)
        #met = self.store[self.key_met]

        ## evaluate vars
        ## --------------------------------------------------           
        #muon1 = muons[0]
        #tau1T = ROOT.TLorentzVector()
        #tau1T.SetPtEtaPhiM( tau1.tlv.Pt(), 0., tau1.tlv.Phi(), tau1.tlv.M() )
        
        
        #self.store['charge_product'] = tau2.charge*tau1.charge
        #self.store['mVis']           = (tau2.tlv+tau1.tlv).M()
        #self.store['mTtot']          = (tau1T + tau2T + met.tlv).M()  #TODO once we have MET
        #self.store['taus_dphi']      = abs(tau2.tlv.DeltaPhi(tau1.tlv))
        #self.store['taus_deta']      = abs(tau2.tlv.Eta()-tau1.tlv.Eta())

        return True


#__________________________________________________________________________
def log_bins(nbins,xmin,xmax):
    xmin_log = math.log(xmin)
    xmax_log = math.log(xmax)
    log_bins = [ float(i)/float(nbins)*(xmax_log-xmin_log) + xmin_log for i in xrange(nbins+1)]
    bins = [ math.exp(x) for x in log_bins ]
    return bins

#__________________________________________________________________________
def log_bins_str(nbins,xmin,xmax):
    bins = log_bins(nbins,xmin,xmax)
    bins_str = "%d, array.array('f',%s)" % (len(bins)-1, str(bins))
    return bins_str 







