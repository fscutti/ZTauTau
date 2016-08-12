#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
weights.py
"""

#import fnmatch
#import os
#import sys
from math import sqrt
from array import array
# logging
import logging
log = logging.getLogger(__name__)
log.setLevel(logging.DEBUG)

# ROOT
import ROOT
import metaroot

# pyframe
import pyframe

# pyutils
import rootutils


GeV = 1000.0

#------------------------------------------------------------------------------
class WeightTotal(pyframe.core.Algorithm):
    """
    multiply event weight by pileup*mc weight

    if 'key' is specified the pileup weight will be put in the store
    """
    #__________________________________________________________________________
    def __init__(self, cutflow=None,key=None):
        pyframe.core.Algorithm.__init__(self, name="WeightTotal", isfilter=True)
        self.cutflow = cutflow
        self.key = key
    #_________________________________________________________________________
    def execute(self, weight):
        if "mc" in self.sampletype: 
            wtotal = self.chain.weight_total
            if self.key: self.store[self.key] = wtotal
            self.set_weight(wtotal*weight)
        return True

#------------------------------------------------------------------------------
class Pileup(pyframe.core.Algorithm):
    """
    multiply event weight by pileup weight

    if 'key' is specified the pileup weight will be put in the store
    """
    #__________________________________________________________________________
    def __init__(self, cutflow=None,key=None):
        pyframe.core.Algorithm.__init__(self, name="Pileup", isfilter=True)
        self.cutflow = cutflow
        self.key = key
    #_________________________________________________________________________
    def execute(self, weight):
        if "mc" in self.sampletype: 
            wpileup = self.chain.weight_mc*self.chain.NOMINAL_pileup_combined_weight
            if self.key: self.store[self.key] = wpileup
            self.set_weight(wpileup*weight)
        return True

#------------------------------------------------------------------------------
class MCEventWeight(pyframe.core.Algorithm):
    """
    multiply event weight by MC weight

    if 'key' is specified the MC weight will be put in the store
    """
    #__________________________________________________________________________
    def __init__(self, cutflow=None,key=None):
        pyframe.core.Algorithm.__init__(self, name="MCEventWeight", isfilter=True)
        self.cutflow = cutflow
        self.key = key
    #_________________________________________________________________________
    def execute(self, weight):
        if "mc" in self.sampletype: 
            wmc = self.chain.weight_mc
            if self.key: self.store[self.key] = wmc
            self.set_weight(wmc*weight)
        return True


#------------------------------------------------------------------------------
class MuonSF(pyframe.core.Algorithm):
    """
    Muon scale factor not just the trigger
    This is not configurable for different working points. Might change that
    in the future.
    """
    #__________________________________________________________________________
    def __init__(self, name="MuonScaleFactor",
            key=None,
            scale=None,
            ):
        pyframe.core.Algorithm.__init__(self, name=name)
        self.key = key
        self.scale = scale

        assert key, "Must provide key for storing muon sf"
        assert scale in [None,'up','dn'], "scale must be in [None,'up','dn']"

    #_________________________________________________________________________
    def initialize(self): pass
   
    #________________________________________________________________________
    def execute(self, weight):
        sf=1.0
        if "mc" in self.sampletype: 

	  #sf=1.0

          sf *= self.chain.lep_0_NOMINAL_MuEffSF_Reco_QualMedium #lep_0_NOMINAL_effSF_RecoMedium
          sf *= self.chain.lep_0_NOMINAL_MuEffSF_IsoGradient

	  #sf *= self.chain.lep_0_NOMINAL_MuEffSF_HLT_mu20_iloose_L1MU15_OR_HLT_mu40_QualMedium_IsoIsoGradient # v12 2015
          #sf *= self.chain.lep_0_NOMINAL_MuEffSF_HLT_mu20_iloose_L1MU15_OR_HLT_mu40_QualMedium_IsoGradient # 2015
          sf *= self.chain.lep_0_NOMINAL_MuEffSF_HLT_mu24_imedium_OR_HLT_mu50_QualMedium_IsoGradient  # 2016
 
	  #print "pt(mu) %lf, trig SF %lf, reco SF %lf, isoGrad SF %lf" % (self.chain.lep_0_pt, self.chain.lep_0_NOMINAL_MuEffSF_HLT_mu24_imedium_OR_HLT_mu50_QualMedium_IsoGradient, self.chain.lep_0_NOMINAL_MuEffSF_Reco_QualMedium, self.chain.lep_0_NOMINAL_MuEffSF_IsoGradient)
 
          if self.scale: 
               if self.scale=='up': pass
               elif self.scale=='dn': pass
        else: pass

        if self.key: 
          self.store[self.key] = sf

        return True

#------------------------------------------------------------------------------
class MuonSFIsoGrad(pyframe.core.Algorithm):
    """
    Muon scale factor not just the trigger
    This is not configurable for different working points. Might change that
    in the future.
    """
    #__________________________________________________________________________
    def __init__(self, name="MuonScaleFactor",
            key=None,
            scale=None,
            ):
        pyframe.core.Algorithm.__init__(self, name=name)
        self.key = key
        self.scale = scale

        assert key, "Must provide key for storing muon sf"
        assert scale in [None,'up','dn'], "scale must be in [None,'up','dn']"

    #_________________________________________________________________________
    def initialize(self): pass

    #_________________________________________________________________________
    def execute(self, weight):
        sf=1.0
        if "mc" in self.sampletype:

	  #sf=1.0

          sf *= self.chain.lep_0_NOMINAL_MuEffSF_Reco_QualMedium

	  #sf *= self.chain.lep_0_NOMINAL_MuEffSF_HLT_mu20_iloose_L1MU15_OR_HLT_mu40_QualMedium_IsoIsoNone # v12 2015
          #sf *= self.chain.lep_0_NOMINAL_MuEffSF_HLT_mu20_iloose_L1MU15_OR_HLT_mu40_QualMedium_IsoNone # 2015
          sf *= self.chain.lep_0_NOMINAL_MuEffSF_HLT_mu24_imedium_OR_HLT_mu50_QualMedium_IsoNone # 2016

	  #print "pt(mu) %lf, antiIso trig SF %lf, reco SF %lf " % (self.chain.lep_0_pt, self.chain.lep_0_NOMINAL_MuEffSF_HLT_mu24_imedium_OR_HLT_mu50_QualMedium_IsoNone, self.chain.lep_0_NOMINAL_MuEffSF_Reco_QualMedium)          

          if self.scale:
               if self.scale=='up': pass
               elif self.scale=='dn': pass
        else: pass

        if self.key:
          self.store[self.key] = sf

        return True

#------------------------------------------------------------------------------
class TauSF(pyframe.core.Algorithm):
    """
    Tau scale factor not just the trigger
    This is not configurable for different working points. Might change that
    in the future.
    """
    #__________________________________________________________________________
    def __init__(self, name="TauScaleFactor",
            key=None,
            scale=None,
            ):
        pyframe.core.Algorithm.__init__(self, name=name)
        self.key = key
        self.scale = scale

        assert key, "Must provide key for storing tau sf"
        assert scale in [None,'up','dn'], "scale must be in [None,'up','dn']"

    #_________________________________________________________________________
    def initialize(self): pass
   
    #________________________________________________________________________
    def execute(self, weight):
        sf=1.0
        if "mc" in self.sampletype: 
 
	  #sf=1.0

          #sf *= self.chain.tau_0_NOMINAL_TauEffSF_selection #v19
	  #sf *= self.chain.tau_0_NOMINAL_TAU_EFF_SELECTION #v12 

	  sf *= self.chain.tau_0_NOMINAL_TauEffSF_JetBDTmedium
	  sf *= self.chain.tau_0_NOMINAL_TauEffSF_reco
	  sf *= self.chain.tau_0_NOMINAL_TauEffSF_HadTauEleOLR_tauhad
	  
	  #print "tau(mu) %lf, tau id trig SF %lf, tau reco SF %lf, tau olr SF %lf " % (self.chain.tau_0_pt, self.chain.tau_0_NOMINAL_TauEffSF_JetBDTmedium, self.chain.tau_0_NOMINAL_TauEffSF_reco, self.chain.tau_0_NOMINAL_TauEffSF_HadTauEleOLR_tauhad)

          if self.scale: 
               if self.scale=='up': pass
               elif self.scale=='dn': pass
        else: pass

        if self.key: 
          self.store[self.key] = sf

        return True


# EOF
