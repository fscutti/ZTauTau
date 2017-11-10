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
class FFTotal(pyframe.core.Algorithm):
    """
    multiply event weight by pileup*mc weight

    if 'key' is specified the pileup weight will be put in the store
    """
    #__________________________________________________________________________
    def __init__(self, cutflow=None,key=None,file='/coepp/cephfs/share/atlas/LFV/FF_nominal.root'):
        pyframe.core.Algorithm.__init__(self, name="FFWeight", isfilter=True)
        self.cutflow = cutflow
        self.key = key
        self.ff_file = ROOT.TFile.Open('/coepp/cephfs/share/atlas/LFV/FF_nominal.root')
        self.ff = {'el': {'1p': None, '3p': None}, 'mu': {'1p': None, '3p': None}}
        self.ff['el']['1p'] = self.ff_file.Get('etau_FF_1Prong')
        self.ff['el']['3p'] = self.ff_file.Get('etau_FF_3Prong')
        self.ff['mu']['1p'] = self.ff_file.Get('mtau_FF_1Prong')
        self.ff['mu']['3p'] = self.ff_file.Get('mtau_FF_3Prong')
    #_________________________________________________________________________
    def execute(self, weight):
        if "data" in self.sampletype:
            def getBins(ff):
                bins = {}
                for i in range(ff.GetNbinsX()):
                    low = ff.GetBinLowEdge(i+1)
                    high = low + ff.GetBinWidth(i+1)
                    val = ff.GetBinContent(i+1)
                    bins.update({i+1: {'low': low, 'high': high, 'val': val}})
                return bins

            def getFFvalue(value, ff):
                bins = getBins(ff)
                for k, rge in bins.iteritems():
                    if value > rge['low'] and value < rge['high']:
                        #print value, rge
                        return rge['val']
                print "Error finding FF value for pt value %s" % value
                return bins[max(bins.keys())]['val']

            fNorm = 1
            if   self.chain.tau_0_n_tracks == 1:
                if self.chain.n_electrons == 1:
                    fNorm = getFFvalue(self.chain.tau_0_pt, self.ff['el']['1p'])
                elif self.chain.n_muons == 1:
                    fNorm = getFFvalue(self.chain.tau_0_pt, self.ff['mu']['1p'])
            elif self.chain.tau_0_n_tracks == 3:
                if self.chain.n_electrons == 1:
                    fNorm = getFFvalue(self.chain.tau_0_pt, self.ff['el']['3p'])
                elif self.chain.n_muons == 1:
                    fNorm = getFFvalue(self.chain.tau_0_pt, self.ff['mu']['3p'])
            #print "FF", fNorm
            if self.key: self.store[self.key] = fNorm
            self.set_weight(fNorm*weight)
            return True

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
class ObjWeight(pyframe.core.Algorithm):
    """
    Object weight:
    This is a generic object weight. You give it the name of the object, e.g. tau_0, lep_0 etc.
    and the name of the branch corresponding to the weight
    """
    #__________________________________________________________________________
    def __init__(self, name="ObjWeight",
            obj_name    = None,
            branch_name = None,
            key         = None,
            scale       = None,
            ):
        pyframe.core.Algorithm.__init__(self, name=name)
        self.obj_name    = obj_name
        self.branch_name = branch_name
        self.key         = key
        self.scale       = scale

        assert key, "Must provide key for storing object weight"

    #_________________________________________________________________________
    def initialize(self):
      pass
    
    #_________________________________________________________________________
    def execute(self, weight):

        weight = 1.0
        var = "NOMINAL"

        if "mc" in self.sampletype:
          if self.scale: 
            """
            implement systematics here: e.g.
            var = "UP"
            """
            pass

          weight *= getattr(self.chain,"_".join([self.obj_name,"NOMINAL",self.branch_name]))
        
        if self.key:
          self.store[self.key] = weight
        return True

# EOF
