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
