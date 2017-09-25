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
import sys

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
    def cut_MuonOnly(self):
        return self.chain.n_muons == 1 and self.chain.n_electrons == 0 and self.chain.n_pvx > 0
    #__________________________________________________________________________
    def cut_ElecOnly(self):
        return self.chain.n_muons == 0 and self.chain.n_electrons == 1 and self.chain.n_pvx > 0
    #__________________________________________________________________________
    def cut_2015MuonTrig(self):
        if ((self.chain.HLT_mu20_iloose_L1MU15 == 1 and self.chain.muTrigMatch_0_HLT_mu20_iloose_L1MU15 == 1) or (self.chain.HLT_mu40 == 1 and self.chain.muTrigMatch_0_HLT_mu40 == 1)):
            if self.sampletype == 'mc':
                return self.chain.NOMINAL_pileup_random_run_number > 0 and self.chain.NOMINAL_pileup_random_run_number <= 284484
            else:
                return self.chain.run_number > 0 and self.chain.run_number <= 284484
    #__________________________________________________________________________
    def cut_2015ElecTrig(self):
        if ((self.chain.HLT_e24_lhmedium_L1EM20VH == 1 and self.chain.eleTrigMatch_0_HLT_e24_lhmedium_L1EM20VH == 1) or (self.chain.HLT_e60_lhmedium == 1 and self.chain.eleTrigMatch_0_HLT_e60_lhmedium == 1) or (self.chain.HLT_e120_lhloose == 1 and self.chain.eleTrigMatch_0_HLT_e120_lhloose == 1)):
            if self.sampletype == 'mc':
                return self.chain.NOMINAL_pileup_random_run_number > 0 and self.chain.NOMINAL_pileup_random_run_number <= 284484
            else:
                return self.chain.run_number > 0 and self.chain.run_number <= 284484
    #__________________________________________________________________________
    def cut_2016MuonTrig(self):
        if ((self.chain.HLT_mu26_ivarmedium == 1 and self.chain.muTrigMatch_0_HLT_mu26_ivarmedium == 1) or (self.chain.HLT_mu50 == 1 and self.chain.muTrigMatch_0_HLT_mu50 == 1) ):
            if self.sampletype == 'mc':
                return self.chain.NOMINAL_pileup_random_run_number > 284484
            else:
                return self.chain.run_number > 284484
    #__________________________________________________________________________
    def cut_2016ElecTrig(self):
        if ((self.chain.HLT_e26_lhtight_nod0_ivarloose == 1 and self.chain.eleTrigMatch_0_HLT_e26_lhtight_nod0_ivarloose == 1) or (self.chain.HLT_e60_lhmedium_nod0 == 1 and self.chain.eleTrigMatch_0_HLT_e60_lhmedium_nod0 == 1) or (self.chain.HLT_e140_lhloose_nod0 == 1 and self.chain.eleTrigMatch_0_HLT_e140_lhloose_nod0 == 1)):
            if self.sampletype == 'mc':
                return self.chain.NOMINAL_pileup_random_run_number > 284484
            else:
                return self.chain.run_number > 284484
    #__________________________________________________________________________
    def cut_RRN2015(self):
        return self.chain.NOMINAL_pileup_random_run_number > 0 and self.chain.NOMINAL_pileup_random_run_number <= 284484
    #__________________________________________________________________________
    def cut_RRN2016(self):
        return self.chain.NOMINAL_pileup_random_run_number > 284484
    #__________________________________________________________________________
    def cut_LepQual(self):
        return self.chain.lep_0_id_medium == 1 and abs(self.chain.lep_0_eta) < 2.5
    #__________________________________________________________________________
    def cut_LepIso(self):
        return self.chain.lep_0_iso_Gradient == 1
    #__________________________________________________________________________
    def cut_LepAntiIso(self):
        return self.chain.lep_0_iso_Gradient == 0
    #__________________________________________________________________________
    def cut_LepPt(self):
        return self.chain.lep_0_pt > 27
    #__________________________________________________________________________
    def cut_TauQual(self):
        return self.chain.n_taus > 0 and abs(self.chain.tau_0_q) == 1 and abs(self.chain.tau_0_eta) < 2.4
    #__________________________________________________________________________
    def cut_TauID(self):
        return self.chain.n_taus_medium == 1 and self.chain.tau_0_jet_bdt_medium == 1
    #__________________________________________________________________________
    def cut_TauAntiID(self):
        return self.chain.n_taus_medium == 0 and self.chain.tau_0_jet_bdt_medium == 0 and self.chain.tau_0_jet_bdt_score > 0.25 
    #__________________________________________________________________________
    def cut_TauPt(self):
        return self.chain.tau_0_pt > 25
    #__________________________________________________________________________
    def cut_OS(self):
        return self.chain.lephad_qxq == 1
    #__________________________________________________________________________
    def cut_SS(self):
        return self.chain.lephad_qxq == -1
    #__________________________________________________________________________
    def cut_TauEVeto(self):
        return self.chain.n_electrons == 1 and ((self.chain.tau_0_n_tracks == 1 and self.chain.tau_0_ele_BDTEleScoreTrans_run2 > 0.15) or (self.chain.tau_0_n_tracks == 3 and self.chain.tau_0_ele_BDTEleScoreTrans_run2 > 0.05))
    #__________________________________________________________________________
    def cut_SCDP(self):
        return self.chain.lephad_met_sum_cos_dphi > -0.35
    #__________________________________________________________________________
    def cut_Presel(self):
        return self.chain.n_bjets == 0 and abs(self.chain.lephad_deta) < 2
    #__________________________________________________________________________
    def cut_SR1(self):
        return self.chain.n_bjets == 0 and abs(self.chain.lephad_deta) < 2 and self.chain.tau_0_pt > 45 and self.chain.lephad_mt_lep1_met < 30 and self.chain.lephad_mt_lep0_met > 40
    #__________________________________________________________________________
    def cut_SR2(self):
        return self.chain.n_bjets == 0 and abs(self.chain.lephad_deta) < 2 and self.chain.tau_0_pt > 45 and self.chain.lephad_mt_lep1_met > 60 and self.chain.lephad_mt_lep0_met < 40
    #__________________________________________________________________________
    def cut_SR3(self):
        return self.chain.n_bjets == 0 and abs(self.chain.lephad_deta) < 2 and self.chain.tau_0_pt < 45 and self.chain.lephad_mt_lep1_met < 30 and self.chain.lephad_mt_lep0_met > 40 and self.chain.lep_0_pt > 45
    ##__________________________________________________________________________
    def cut_WCR(self):
        # W CR
        return self.chain.n_bjets == 0 and abs(self.chain.lephad_deta) < 2 and self.chain.lephad_mt_lep1_met > 40 and self.chain.lephad_mt_lep0_met > 60 
    #__________________________________________________________________________
    def cut_TCR(self):
        # TopCR
        return self.chain.n_bjets  > 0 and abs(self.chain.lephad_deta) < 2 and self.chain.n_jets > 1
    #__________________________________________________________________________
    def cut_QCDCR(self):
        # QCD CR 1
        return self.chain.n_bjets == 0 and abs(self.chain.lephad_deta) > 2 and self.chain.tau_0_pt > 45 and self.chain.lephad_mt_lep1_met < 60
    #__________________________________________________________________________
    def cut_QCDCR2(self):
        # QCD CR 2 : What is this used for
        return self.chain.n_bjets == 0 and abs(self.chain.lephad_deta) > 2 and self.chain.tau_0_pt < 45 and self.chain.lephad_mt_lep1_met < 60 and self.chain.lephad_mt_lep0_met < 40
    #__________________________________________________________________________
    def cut_ZCR(self):
      # QCD CR
      # This one I'm sure is orthogonal
      return self.chain.n_bjets == 0 and abs(self.chain.lephad_deta) < 2 and self.chain.tau_0_pt < 45 and self.chain.lephad_mt_lep1_met < 60 and self.chain.lephad_mt_lep0_met < 40
    
    
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
                 name          = 'PlotAlg',
                 region        = '',
                 hist_list     = [], # list of histograms to be filled
                 cut_flow      = None,
                 plot_all      = True,
                 do_var_check  = False,
                 ):
        pyframe.algs.CutFlowAlg.__init__(self,key=region)
        CutAlg.__init__(self,name,isfilter=False)
        self.cut_flow     = cut_flow
        self.region       = region
        self.plot_all     = plot_all
        self.hist_list    = hist_list
        self.do_var_check = do_var_check
    
    #_________________________________________________________________________
    def initialize(self):

        # remove eventual repetitions from list of histograms
        h_dict = {}
        for h in self.hist_list: h_dict[h.hname] = h
        self.hist_list = h_dict.values()
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
               
               self.plot(region, passed, list_cuts, cut, weight=weight)

        return True

    #__________________________________________________________________________
    def finalize(self):
        pyframe.algs.CutFlowAlg.finalize(self)

    #__________________________________________________________________________
    def plot(self, region, passed, list_cuts, cut, weight=1.0):
        
        # should probably make this configurable

        # -----------------
        # Create histograms
        # -----------------
        for h in self.hist_list:
            if h.get_name() == "Hist1D":
              h.instance = self.hist(h.hname, "ROOT.TH1F('$', ';%s;%s', %d, %lf, %lf)" % (h.xtitle,h.ytitle,h.nbins,h.xmin,h.xmax), dir=os.path.join(region, '%s'%h.dir))
            elif h.get_name() == "Hist2D":
              h.instance = self.hist(h.hname, "ROOT.TH2F('$', ';%s;%s', %d, %lf, %lf, %d, %lf, %lf)" % (h.hname,h.hname,h.nbinsx,h.xmin,h.xmax,h.nbinsy,h.ymin,h.ymax), dir=os.path.join(region, '%s'%h.dir))
              h.set_axis_titles()


        # ---------------
        # Fill histograms
        # ---------------
        if passed:
          for h in self.hist_list:
            if self.do_var_check:
              exec ( "present = %s"%h.varcheck() )
              if not present:
                sys.exit( "ERROR: variable %s  not found for hist %s"%(h.vexpr,h.hname) )

            if h.get_name() == "Hist1D":
              var = -999.

              # this all part gives me the shivers. But is just temporary. Don't panic
              exec( "var = %s" % h.vexpr ) # so dirty !!!

              if h.instance and var!=-999.: h.fill(var, weight)

            elif h.get_name() == "Hist2D":
              varx = -999.
              vary = -999.
              exec( "varx,vary = %s" % h.vexpr ) # so dirty !!!
              if h.instance and varx!=-999. and vary!=-999.: h.fill(varx,vary, weight)


    #__________________________________________________________________________
    def check_region(self,cutnames):
        cut_passed = True
        for cn in cutnames:
            if cn == 'ALL': continue

            if cn.startswith('!'):
                cut_passed = not self.apply_cut(cn[1:])
            else:
                cut_passed = self.apply_cut(cn) and cut_passed
        return cut_passed


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



