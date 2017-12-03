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
class FFTotal_SM(pyframe.core.Algorithm):
    """
    multiply event weight by pileup*mc weight

    if 'key' is specified the pileup weight will be put in the store
    """
    #__________________________________________________________________________
    def __init__(self, cutflow=None,key=None,ff_file='/coepp/cephfs/share/atlas/LFV/FF_july_2017.root', r_file='/coepp/cephfs/share/atlas/LFV/R_july_2017.root' ):
        pyframe.core.Algorithm.__init__(self, name="FFWeight", isfilter=True)
        self.cutflow = cutflow
        self.key = key
        self.ff_file = ROOT.TFile.Open(ff_file)
        self.r_file = ROOT.TFile.Open(r_file)
        self.leps = {'el': 'e', 'mu': 'mu'}
        self.prng = {'1p': '1Prong', '3p': '3Prong'}
        self.prng = {'QCD': 'QCD', 'W': 'W'}
        self.taup = {40: '2040', 90: '4090', 200: '90200'}
        for x in self.prng.keys():
            self.ff[x] = {}
            self.r [x] = {}
            for y in self.bkgd.keys():
                self.ff[x][y] = self.ff_file.Get('%s_CBBOOST_%s_SLT' % (self.prng[x], self.bkgd[y]))
                self.r [x][y] = {}
                for z in self.leps.keys():
                    self.r [x][y][z] = {}
                    for a in self.taup.keys:
                        self.r [x][y][z][a] = self.r_file.Get('%s_CBPreselection_%s_SLT_SR_%s_%s' % (y,self.prng[y],self.leps[z],self.taup[a]))
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

            def getRvalue(taupt_val, dphi_val, ff):
                if taupt_val < 40:
                    taupt = 40
                elif taupt_val < 90:
                    taupt = 90
                elif taupt_val < 200:
                    taupt = 200
                else:
                    print "Issue taupt, setting to 90-200" % taupt_val
                    taupt = 200

                bins = getBins(ff[taupt])
                for k, rge in bins.iteritems():
                    if dphi_val > rge['low'] and dphi_val < rge['high']:
                        #print value, rge
                        return rge['val']
                print "Error finding FF value for pt value %s" % value
                return bins[max(bins.keys())]['val']

            fNorm = 1
            fqcd, fw, rqcd, rw = 1, 1, 1, 0
            # Choose prong
            if   self.chain.tau_0_n_tracks == 1:
                prong = '1p'
            elif self.chain.tau_0_n_tracks == 3:
                prong = '3p'
            else:
                print 'Issue with prong, setting to 3p'
                prong = '3p'
            # Choose channel
            if self.chain.n_electrons == 1:
                lep = 'el'
            elif self.chain.n_muons == 1:
                lep = 'mu'
            else:
                print 'Issue with lep, setting to mu'
                prong = 'mu'
            # Calculate channel
            fqcd = getFFvalue(self.chain.tau_0_pt, self.ff[prong]['QCD'])
            fw   = getFFvalue(self.chain.tau_0_pt, self.ff[prong]['W'  ])
            rqcd = getRvalue (self.chain.tau_0_pt, abs(self.chain.tau_0_phi, self.chain.met_reco_phi), self.r[prong]['QCD'][lep])

            fNorm = fqcd*rqcd + fw*(1-rqcd)

            if self.key: self.store[self.key] = fNorm
            self.set_weight(fNorm*weight)
            return True

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
    def __init__(self, cutflow=None,key=None,isSig=False):
        pyframe.core.Algorithm.__init__(self, name="WeightTotal", isfilter=True)
        self.cutflow = cutflow
        self.key = key
        self.isSig = isSig
    #_________________________________________________________________________
    def execute(self, weight):
        if "mc" in self.sampletype: 
            if self.isSig:
                wtotal = self.chain.theory_weights_nominal
            else:
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
