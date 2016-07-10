#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
algs.py

This module contains a set of analysis specific algs 
for calculating variables, applying selection and 
plotting.
"""

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

#GeV = 1000.0

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

    def cut_MuonHLTmu20ilooseL1MU15ORmu50(self): #2015
        return self.chain.HLT_mu20_iloose_L1MU15 == 1 or self.chain.HLT_mu50 == 1

    def cut_MuonHLTmu24imediumORHLTmu50(self): #2016
        return self.chain.HLT_mu24_imedium == 1 or self.chain.HLT_mu50 == 1

    def cut_MuonMuTrigMatch0HLTmu20ilooseL1MU15(self):
        return self.chain.muTrigMatch_0_HLT_mu20_iloose_L1MU15 == 1
    #__________________________________________________________________________
    # MUON CUT
    #__________________________________________________________________________

    def cut_MuonIdMedium(self):
        return self.chain.lep_0_id_medium == 1

    def cut_MuonPt22(self):
        return self.chain.lep_0_pt > 22.

    def cut_MuonPt26(self):
        return self.chain.lep_0_pt > 26.

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

    def cut_BDTtauMed(self):
        return self.chain.tau_0_jet_bdt_medium == 1
   
    def cut_TauLowPt(self):
	return self.chain.tau_0_pt < 40.0

    def cut_TauHighPt(self):
	return self.chain.tau_0_pt > 40.0

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

    #---- Ztau ----#

    def cut_VisMass4580(self):
        return abs(self.chain.lephad_vis_mass) > 45 and abs(self.chain.lephad_vis_mass) < 80

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
 

    #----- SYSTEMATICS----#

    def cut_Topoetcone20pt010(self):
         return self.chain.lep_0_iso_topoetcone20/self.chain.lep_0_pt > 0.1

    def cut_Topoetcone20pt011(self):
         return self.chain.lep_0_iso_topoetcone20/self.chain.lep_0_pt > 0.11

    def cut_Topoetcone20pt012(self):
         return self.chain.lep_0_iso_topoetcone20/self.chain.lep_0_pt > 0.12

    def cut_Topoetcone20pt013(self):
         return self.chain.lep_0_iso_topoetcone20/self.chain.lep_0_pt > 0.13

    def cut_Topoetcone20pt014(self):
         return self.chain.lep_0_iso_topoetcone20/self.chain.lep_0_pt > 0.14

    def cut_Topoetcone20pt015(self):
         return self.chain.lep_0_iso_topoetcone20/self.chain.lep_0_pt > 0.15

    def cut_Topoetcone20pt016(self):
         return self.chain.lep_0_iso_topoetcone20/self.chain.lep_0_pt > 0.16

    def cut_Topoetcone20pt017(self):
         return self.chain.lep_0_iso_topoetcone20/self.chain.lep_0_pt > 0.17

    def cut_Topoetcone20pt018(self):
         return self.chain.lep_0_iso_topoetcone20/self.chain.lep_0_pt > 0.18

    def cut_Topoetcone20pt019(self):
         return self.chain.lep_0_iso_topoetcone20/self.chain.lep_0_pt > 0.19


    def cut_Topoetcone20pt02(self):
         return self.chain.lep_0_iso_topoetcone20/self.chain.lep_0_pt > 0.2

    def cut_Topoetcone20pt03(self):
         return self.chain.lep_0_iso_topoetcone20/self.chain.lep_0_pt > 0.3

    def cut_Topoetcone20pt04(self):
         return self.chain.lep_0_iso_topoetcone20/self.chain.lep_0_pt > 0.4
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
        
        self.h_nmuons = self.hist('h_nmuons', "ROOT.TH1F('$', ';N_{#mu};Events', 8, 0, 8)", dir=EVT)

        self.h_met_reco_et = self.hist('h_met_reco_et', "ROOT.TH1F('$', ';E^{miss}_{T} [GeV];Events / (1 GeV)', 1000, 0.0, 1000.0)", dir=MET)

        self.h_mu_pt = self.hist('h_mu_pt', "ROOT.TH1F('$', ';p_{T}(\mu) [GeV];Events / (1 GeV)', 1000, 0.0, 1000.0)", dir=MUONS)

        self.h_tau_pt = self.hist('h_tau_pt', "ROOT.TH1F('$', ';p_{T}(#tau) [GeV];Events / (1 GeV)', 1000, 0.0, 1000.0)", dir=TAUS)

        self.h_n_vx = self.hist('h_n_vx', "ROOT.TH1F('$', ';N_{vx} ;Events', 14, 0.0, 14.0)", dir=EVT)

        self.h_vis_mass = self.hist('h_vis_mass', "ROOT.TH1F('$', ';Visible Mass (#tau,#mu) [GeV];Events', 200, 0.0, 200.0)", dir=EVT)

        self.h_sumcosdphi = self.hist('h_sumcosdphi', "ROOT.TH1F('$', ';\Sum\cos(\Delta \phi) ;Events', 20, -2.0, 2.0)", dir=EVT)

        self.h_m_trans = self.hist('h_m_trans', "ROOT.TH1F('$', ';m_T (\mu,E^{miss}_{T}) [GeV];Events', 200, 0.0, 200.0)", dir=EVT)

        self.h_tau_eta = self.hist('h_tau_eta', "ROOT.TH1F('$', '; \eta ;Events', 12, -3.0, 3.0)", dir=TAUS)

        self.h_tau_phi = self.hist('h_tau_phi', "ROOT.TH1F('$', '; \phi ;Events', 16, -4.0, 4.0)", dir=TAUS)

        self.h_mu_eta = self.hist('h_mu_eta', "ROOT.TH1F('$', '; \eta ;Events', 12, -3.0, 3.0)", dir=MUONS)

        self.h_mu_phi = self.hist('h_mu_phi', "ROOT.TH1F('$', '; \phi ;Events', 16, -4.0, 4.0)", dir=MUONS)

        self.h_met_reco_phi = self.hist('h_met_reco_phi', "ROOT.TH1F('$', '; \phi ;Events', 16, -4.0, 4.0)", dir=MET)

        self.h_tau_n_tracks = self.hist('h_tau_n_tracks', "ROOT.TH1F('$', '; N_{tracks} ;Events', 5, 0.0, 5.0)", dir=TAUS)
        
	self.h_jet_bdt_score = self.hist('h_jet_bdt_score', "ROOT.TH1F('$', '; BDT score ;Events', 8, 0.6, 1.0)", dir=TAUS)



        if passed:

             self.h_nmuons.Fill(self.chain.n_muons, weight)
 
             self.h_met_reco_et.Fill(self.chain.met_reco_et, weight)
 
             self.h_mu_pt.Fill(self.chain.lep_0_pt, weight)
 
             self.h_tau_pt.Fill(self.chain.tau_0_pt, weight)
 
             self.h_n_vx.Fill(self.chain.n_vx, weight)
 
             self.h_vis_mass.Fill(self.chain.lephad_vis_mass, weight)
 
             self.h_sumcosdphi.Fill(self.chain.lephad_met_sum_cos_dphi, weight)
 
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







