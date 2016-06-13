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
            wpileup = self.chain.weight_pileup
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
class FakeFactor(pyframe.core.Algorithm):
    """
    python implementation of the fake-factor getter.

    takes input histograms from the FakeWeights package.

    'key' must be specified as the fakefactor is put in the store
    """
    #__________________________________________________________________________
    def __init__(self, name="FakeFactor",config_file=None,tau_index=None,key=None,scale=None):
        pyframe.core.Algorithm.__init__(self,name=name)
        self.config_file = config_file
        self.tau_index = tau_index
        self.key = key
        self.scale = scale

        assert config_file, "Must provide config file!"
        assert key, "Must provide key for storing fakefactor"
    #_________________________________________________________________________
    def initialize(self):
        f = ROOT.TFile.Open(self.config_file)
        assert f, "Failed to open fake-factor config file: %s"%(self.config_file)
        
        h_1P_NoS = f.Get("fake_factor_1P_NoS")
        assert h_1P_NoS, "Failed to get 'fake_factor_1P_NoS' from %s"%(self.config_file)

        h_3P_NoS = f.Get("fake_factor_3P_NoS")
        assert h_3P_NoS, "Failed to get 'fake_factor_3P_NoS' from %s"%(self.config_file)

        self.h_1P_NoS = h_1P_NoS.Clone()
        #self.h_1P_NoS.SetDirectory(0)

        self.h_3P_NoS = h_3P_NoS.Clone()
        #self.h_3P_NoS.SetDirectory(0)

        f.Close()

    #_________________________________________________________________________
    def execute(self, weight):
        taus = self.store['taus']
        tau = taus[self.tau_index]

        pt = tau.tlv.Pt()/GeV

        for ibin in xrange(0,self.h_1P_NoS.GetN()):
          edlow = self.h_1P_NoS.GetX()[ibin] - self.h_1P_NoS.GetEX()[ibin]
          edhi  = self.h_1P_NoS.GetX()[ibin] + self.h_1P_NoS.GetEX()[ibin]
          if pt>=edlow and pt<edhi: break

        #ibin = self.h_1P_NoS.GetXaxis().FindBin(pt)

        # error bars are symmetric
        if tau.numTrack == 1: 
          ff = self.h_1P_NoS.GetY()[ibin]
          eff = self.h_1P_NoS.GetEY()[ibin]
        elif tau.numTrack == 3:
          ff = self.h_3P_NoS.GetY()[ibin]
          eff = self.h_3P_NoS.GetEY()[ibin]
        else: 
            assert False, "Cannot compute fake-factor for tau with %d tracks"%(tau.numTrack)

        if self.scale == 'up': ff +=eff
        if self.scale == 'dn': ff -=eff

        if self.key: self.store[self.key] = ff

        return True


#------------------------------------------------------------------------------
class FakeWeight(pyframe.core.Algorithm):
    """
    python wrapper for FakeWeight tool
   
    tau_id_level: 
      1 - loose
      2 - medium
      3 - tight

    has_trigger
      True  - ID+Trigger
      False - ID

    fail_id - for fail ID control regions

    'key' must be specified as the fakeweight is put in the store
    """
    #__________________________________________________________________________
    def __init__(self, name="FakeWeight",
            config_file=None,
            tau_index=None,
            tau_id_level=None,
            has_trigger=False,
            fail_id=False,
            key=None,
            uncertainty=None,
            scale=None,
            ):
        pyframe.core.Algorithm.__init__(self, name=name)
        self.config_file = config_file
        self.tau_index = tau_index
        self.tau_id_level = tau_id_level
        self.has_trigger = has_trigger
        self.fail_id = fail_id
        self.key = key
        self.scale = scale
        self.uncertainty = uncertainty

        assert config_file, "Must provide config file!"
        assert key, "Must provide key for storing fakefactor"
    #_________________________________________________________________________
    def initialize(self):

        ROOT.gSystem.Load('libFakeWeightTool')
        self.tool = ROOT.FakeWeightScaler()
        self.tool.readGraphsFromFile(self.config_file)

    #_________________________________________________________________________
    def execute(self, weight):
        fw=1.0
        if "mc" in self.sampletype: 
            taus = self.store['taus']
            charge_product = int(taus[0].charge * taus[1].charge)
            tau = taus[self.tau_index]
            ## only apply fake weight to fake-taus   
            # pT has to be passed in MeV
            if not tau.trueTauAssoc_matched:
                fw = self.tool.getWeight(
                        tau.tlv.Pt(),
                        tau.numTrack,
                        self.tau_id_level,
                        self.has_trigger,
                        charge_product,
                        self.fail_id,
                        )

                ## if is_statonly take unc from the tool
                if not self.uncertainty:
                  unc_dir = 0 
                  if self.scale == 'up': unc_dir =  1
                  if self.scale == 'dn': unc_dir = -1

                  efw = self.tool.getUncertainty(
                           tau.tlv.Pt(),
                           tau.numTrack,
                           self.tau_id_level,
                           self.has_trigger,
                           charge_product,
                           unc_dir,
                           )
                  if self.scale   == 'up': fw += efw
                  elif self.scale == 'dn': fw -= efw

                else:
                  if self.scale   == 'up': fw *= (1.+self.uncertainty)
                  elif self.scale == 'dn': fw *= (1.-self.uncertainty)

        if self.key: self.store[self.key] = fw

        return True

#------------------------------------------------------------------------------
class TauTriggerSFLowPt(pyframe.core.Algorithm):
    """
    Same as TauTriggerSF but only applies a weight to 
    low pt (<100 GeV) taus. Used to split the tau
    trigger systematics in different components

    """
    #__________________________________________________________________________
    def __init__(self, name="TauTriggerUncertainty",
            config_file=None,
            tau_id_level=None,
            tau_index=None,
            key=None,
            scale=None,
            ):
        pyframe.core.Algorithm.__init__(self, name=name)
        self.config_file = config_file
        self.tau_id_level = tau_id_level
        self.tau_index = tau_index
        self.key = key
        self.scale = scale

        assert key, "Must provide key for storing trigger sf"
        assert scale in [None,'up','dn'], "scale must be in [None,'up','dn']"

    #_________________________________________________________________________
    def initialize(self):
        if self.config_file: 
            ROOT.gSystem.Load('libTrigTauEfficiency') 
            self.tool = ROOT.TrigTauEfficiency()
            assert self.tool.loadInputFile(self.config_file) == 0, "Failed initialising from input file: %s"%(self.config_file)
            
            if   self.tau_id_level == 1: self.level = 'BDTl' 
            elif self.tau_id_level == 2: self.level = 'BDTm' 
            elif self.tau_id_level == 3: self.level = 'BDTt'
            else:
                assert False, "Invalid tau ID level, must be in [1,2,3]!"
   
    #_________________________________________________________________________
    def execute(self, weight):
        sf=1.0
        if "mc" in self.sampletype: 
            taus = self.store['taus']
            tau = taus[self.tau_index]
            ## only apply trigger sf if trigger-matched tau is truth-matched
            if tau.trueTauAssoc_matched:
                ## pt < 100 GeV -> SF from tag and probe
                if self.config_file and tau.tlv.Pt()<100.0*GeV:
                    pt = tau.tlv.Pt()
                    eta = tau.tlv.Eta()
                    prong_str = '1p' if tau.numTrack == 1 else '3p'
                    eveto_str = 'EVnone'
                    run = self.chain.RandomRunNumber
                    # pT has to be in MeV for the tool
                    if tau.tlv.Pt()<55.0*GeV: 
                      sf = self.tool.getSF(pt,eta,0,run,prong_str,self.level,eveto_str)
                    else: pass
                    sf_tool = self.tool.getSF(pt,eta,0,run,prong_str,self.level,eveto_str)
                    # WARNING: flip the uncertainty due to bug in trigger package
                    if self.scale: 
                        if self.scale=='up':
                            data_stat = self.tool.getSF(pt,eta,+1,run,prong_str,self.level,eveto_str) 
                            mc_stat   = self.tool.getSF(pt,eta,+2,run,prong_str,self.level,eveto_str) 
                            sys       = self.tool.getSF(pt,eta,+3,run,prong_str,self.level,eveto_str) 
                        elif self.scale=='dn':
                            data_stat = self.tool.getSF(pt,eta,-1,run,prong_str,self.level,eveto_str) 
                            mc_stat   = self.tool.getSF(pt,eta,-2,run,prong_str,self.level,eveto_str) 
                            sys       = self.tool.getSF(pt,eta,-3,run,prong_str,self.level,eveto_str) 
                        # sum all in quadrature and then obtain relative unc
                        unc = sqrt(sum([pow(p,2) for p in [data_stat,mc_stat,sys]]))
                        rel_unc = unc / sf_tool
                        if self.scale=='up':   sf += rel_unc * sf
                        elif self.scale=='dn': sf -= rel_unc * sf
                ## pt > 100 -> does not do anything
                else: pass

        if self.key: 
          self.store[self.key] = sf

        return True


# EOF
