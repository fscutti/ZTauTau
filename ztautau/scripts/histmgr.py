# encoding: utf-8
'''
histmgr.py

description:

'''

## modules
from pyplot import histutils, fileio
import os 
import random
import ROOT
import copy
import math

from array import array
from copy import copy

import logging
log = logging.getLogger(__name__)

# - - - - - - - - - - - class defs  - - - - - - - - - - - - #
#------------------------------------------------------------
class HistMgr():
    '''
    description of HistMgr 
    '''
    #____________________________________________________________
    def __init__(self,
            basedir = None,
            target_lumi = None,
            cutflow_histname = 'h_metadata', 
            ):
        self.basedir = basedir
        self.target_lumi = target_lumi
        self.cutflow_histname = cutflow_histname

    #____________________________________________________________
    def get_file_path(self,pathmod=None,samplename=None,sampletype=None,sys=None,mode=None):
        '''
        construct path to file for sample+systematic
        '''
        ## get systematics path
        syspath = 'nominal'
        #if sys and not sys.flat_err:
        if sys:
            if mode == 'up': syspath = sys#.var_up
            else:            syspath = sys#.var_dn

        ## get file path
        path_to_file = ''
        path_to_file = os.path.join(self.basedir,syspath,samplename)
        
        if pathmod:    path_to_file = path_to_file.replace(syspath,os.path.join(pathmod,syspath))
        if sampletype: path_to_file = path_to_file.replace(syspath,os.path.join(syspath,sampletype))
        
        if not os.path.isdir(path_to_file) and os.path.exists(path_to_file): path_to_file += ".root"
        return path_to_file

    #____________________________________________________________
    def hist(self, # retrieve folder with longer name
            pathmod    = None,
            histname   = None,
            samplename = None,
            sampletype = None,
            region     = None,
            icut       = None, 
            sys        = None,
            mode       = None,
            ):
        assert histname,  'must define histname'
        assert samplename,    'must define samplename'
        if sys: 
            assert mode in ['up','dn'], "mode must be either 'up' or 'dn'"
        
        #print '#########################################################################'
        #print 'HistMgr', pathmod, histname, samplename, sampletype, region, sys, mode
        path_to_file = self.get_file_path(pathmod,samplename,sampletype,sys,mode)
        f_list = []

        #print path_to_file
        if os.path.isdir(path_to_file): f_list = [os.path.join(path_to_file,f) for f in os.listdir(path_to_file)] 
        else:                           f_list = [path_to_file]

        h_list = []
        
        total_c, total_h = 0, 0
        for file in f_list:

            #print file
            f = ROOT.TFile.Open(file)
            assert f, 'Failed to open input file!'
            
            ## get hist path
            path_to_hist = ''
            if region and not "cutflow" in histname:
               path_to_hist = os.path.join('regions',region)
               
               ## check region exists
               if not f.Get(path_to_hist):
                   #print "Failed to retrieve", file, path_to_hist
                   f.Close()
                   continue
                   #if f.Get('cutflow_'+path_to_hist.split('/')[1]).GetBinContent(16) > 0:
                   #    print file
                   #    print "%%%%%%%%%%%%%%%%%", f.Get('cutflow_'+path_to_hist.split('/')[1]).GetBinContent(16)
                   #f.Close()
                   #return None
               
               cutflow = get_icut_path(file,      path_to_hist, icut)
               if icut == 0: pass #cutflow = "ALL"
               if not cutflow: 
                   log.debug( '%s no cut: %s'% (samplename,icut) )
                   f.Close()
                   #return None
                   continue
               path_to_hist = os.path.join(path_to_hist,cutflow)
              
            path_to_hist = os.path.join(path_to_hist,histname)
            
            h = None
            #print path_to_hist
            h = f.Get(path_to_hist)
            #if not 'cutflow' in path_to_hist:
            #    bin_uf    = (h.GetBinContent(0), h.GetBinError(0))
            #    bin_first = (h.GetBinContent(1), h.GetBinError(1))
            #    last      = h.GetNbinsX()
            #    bin_of    = (h.GetBinContent(last  ), h.GetBinError(last  ))
            #    bin_last  = (h.GetBinContent(last+1), h.GetBinError(last+1))
            #    # Rebinning shit
            #    import math
            #    print "#################"
            #    h.Print("all")
            #    h.SetBinContent(1,bin_uf[0]+bin_first[0])
            #    h.SetBinError  (1,math.sqrt(bin_uf[1]*bin_uf[1]+bin_first[1]*bin_first[1]))
            #    h.SetBinContent(last,bin_of[0]+bin_last[0])
            #    h.SetBinError  (last,math.sqrt(bin_of[1]*bin_of[1]+bin_last[1]*bin_last[1]))
            #    print "#################"
            #    h.Print("all")
            #if not 'cutflow' in path_to_hist:
            #    cutflow = f.Get('cutflow_'+path_to_hist.split('/')[1]).GetBinContent(16)
            #    total_c += cutflow
            #    total_h += h.GetEntries()
            #    if not h.GetEntries() == cutflow:
            #        print '%s:%s'%(file,path_to_hist)
            #        print h.GetEntries(), cutflow
            #    if not h:
            #        f.Close()
            #        print 'failed retrieveing hist: %s:%s'%(file,path_to_hist)
            #        return None

            h = h.Clone()
            h.SetDirectory(0)
            
            f.Close()
            
            ## apply flat sys (if specified)
            #if sys and sys.flat_err:
            #    if mode == 'up': h.Scale(1.+sys.flat_err)
            #    else:            h.Scale(1.-sys.flat_err)
            
            #print file, h.GetBinContent(12)
            h_list.append(h)
        
        #print samplename, total_c, total_h
        #print '#########################################################################'
        #print h_list
        return histutils.add_hists(h_list)
          
    #____________________________________________________________
    def get_nevents(self,samplename,sampletype,pathmod=None,sys=None,mode=None):
        '''
        retrieves cutflow hist for given sample 
        and given systematic (which contains the 
        total events before skim)
        '''
        assert samplename, 'must provide samplename'
    
        nevents = 0

        path_to_file = self.get_file_path(pathmod,samplename,sampletype,sys,mode)
        
        f_list = []

        if os.path.isdir(path_to_file): f_list = [os.path.join(path_to_file,f) for f in os.listdir(path_to_file)] 
        else:                           f_list = [path_to_file]

        for file in f_list:
          f = ROOT.TFile.Open(file)
          assert f, 'get_nevents: failed to open input file'
          if f: 
              #print f.ls()
              #print "cutflow", self.cutflow_histname
              cutflow_histname = self.cutflow_histname
              for hist in f.GetListOfKeys():
                  if 'h_metadata' in hist.GetName():
                      cutflow_histname = hist.GetName()
              h = f.Get(cutflow_histname)
              assert h, 'get_nevents: failed to retrieve histogram from file'
              if 'lm15hp20' in file or 'lp15hm20' in file or 'MINLO' in file or '_filt' in file:
                  #print file
                  if 'ggH' in file:
                      #print 'ggH'
                      if h: nevents += h.GetBinContent(14)
                  elif 'VBF' in file or 'MINLO' in file:#'WmH125J' in file or 'WpH125J' in file or 'ZH125J' in file:
                      #print 'VBF'
                      if h: nevents += h.GetBinContent(15)
              else:
                  if h: nevents += h.GetBinContent(8)
              f.Close()
          
        return nevents


#------------------------------------------------------------
class BaseEstimator(object):
    '''
    TODO: put description of estimatior functionality here
    '''
    #____________________________________________________________
    def __init__(self,hm=None,sample=None):
        self.hm = hm
        self.sample = sample
        
        ## allowed systematics 
        self.allowed_systematics = []
        self.hist_store = {}

        assert self.sample, 'must provide sample to BaseEstimator'
    
    #____________________________________________________________
    def get_hist_tag(self,pathmod=None,histname=None,region=None,icut=None,sys=None,mode=None):
      if isinstance(region,list): region = "_".join(region)
      htag = "_".join([str(s) for s in [pathmod,histname,region,icut,sys,mode]])
      return htag
        
    #____________________________________________________________
    def hist(self,pathmod=None,histname=None,region=None,icut=None,sys=None,mode=None):
        """
        Supports list of regions to be added
        """
        #print "<ztautau.scripts.histmgr> BaseEst hist", pathmod, histname, self.sample.name, self.sample.type, region, sys
        if sys: self.add_systematics(sys)
        if not self.is_affected_by_systematic(sys): sys=mode=None
        #print 'BaseEst', sys
        htag = self.get_hist_tag(pathmod,histname,region,icut,sys,mode)
        #print htag
        if not isinstance(region,list): region = [region]
        if not self.hist_store.has_key(htag):
          h_dict = {}
          for r in region:
             h_dict[r] = self.__hist__(
                     pathmod=pathmod,
                     histname=histname,
                     region=r,
                     icut=icut,
                     sys=sys,
                     mode=mode,
                     )
          h = None
          if not all(v is None for v in h_dict.values()):
            h = histutils.add_hists(h_dict.values())
          if h: 
            self.sample.plotopts.configure(h)
            log.debug('%s: %s'%(self.sample.name,h.Integral()))

          self.hist_store[htag] = h
        return self.hist_store[htag]
    
    #__________________________________________________________________________
    def add_systematics(self, sys):
        if not isinstance(sys,list): sys = [sys]
        self.allowed_systematics += sys
    
    #__________________________________________________________________________
    def is_affected_by_systematic(self, sys):
        return sys in self.allowed_systematics

    #__________________________________________________________________________
    def flush_hists(self):
        for h in self.hist_store.values():
            if h: h.Delete()
        self.hist_store = {}


#------------------------------------------------------------
class ProxyEstimator(BaseEstimator):
    '''
    Standard Estimator class (for MC and data) 
    '''
    #____________________________________________________________
    def __init__(self,**kw):
        BaseEstimator.__init__(self,**kw)

        ## xsec / Ntotal, seperately for each systematic
        ## (set on first call to hist)
        self.mc_lumi_frac = {}
   

    #____________________________________________________________
    def __hist__(self,pathmod=None,histname=None,region=None,icut=None,sys=None,mode=None):
        """
        implementation of nominal hist getter
        """
        #print "<ztautau.scripts.histmgr> ProxyEst hist", pathmod, histname, self.sample.name, self.sample.type, region
        h = self.hm.hist(
                         pathmod=pathmod,
                         histname=histname,
                         samplename=self.sample.name,  
                         sampletype=self.sample.type,
                         region=region,
                         icut=icut,
                         sys=sys,
                         mode=mode,
                         )
        #print "<ztautau.scripts.histmgr> ProxyEst hist", h
        if h and self.sample.type == 'mc' and ('cutflow_weighted' in histname or not 'cutflow' in histname): 
            #print 'scaling'
            lumi_frac = self.get_mc_lumi_frac(sys,mode,pathmod)
            h.Scale(self.hm.target_lumi * lumi_frac)

        return h    
    #____________________________________________________________
    def get_mc_lumi_frac(self,sys,mode,pathmod=None):
        '''
        Gets the effective luminosity fraction of the mc sample. 
        This is done seperately for each sys, since the total 
        number of events can potentially be different for different 
        sys samples. Once retrieved, the value is stored for 
        further access. 
        '''
        if sys: 
            assert mode in ['up','dn'], "mode must be either 'up' or 'dn'"
        
        sysname = 'nominal'
        if sys:
            if mode == 'up': sysname = '%s_up'%(sys)
            else:            sysname = '%s_dn'%(sys)

        if not self.mc_lumi_frac.has_key(sysname): 
            xsec    = self.sample.xsec
            feff    = self.sample.feff
            kfactor = self.sample.kfactor
            Ntotal  = self.hm.get_nevents(self.sample.name,self.sample.type,pathmod,sys,mode)
            # there seems to be no need for feff and kfactor
            self.mc_lumi_frac[sys] = (xsec * feff * kfactor) / Ntotal if Ntotal else 0.0
        return self.mc_lumi_frac[sys]


#------------------------------------------------------------
class SimpleEstimator(BaseEstimator):
    '''
    DataBkgSub Estimator class 
    subtracts bkgs from data for estimate
    '''
    #____________________________________________________________
    def __init__(self,
        data_sample=None,
        mc_sample=None,
        pathmod_main=None,     # force the estimator to read from preconfigured path
        pathmod_aux=None,
        ext_hist_path=None,
        **kw
        ):

        BaseEstimator.__init__(self,**kw)
        self.data_sample = data_sample
        self.mc_sample = mc_sample
        self.pathmod_main = pathmod_main
        self.pathmod_aux = pathmod_aux
        self.ext_hist_path = ext_hist_path

    #____________________________________________________________
    def __hist__(self,pathmod=None,histname=None,region=None,icut=None,sys=None,mode=None):
        
       # Initiate combinations for replacing strings
       from itertools import product
       years = []
       if 'all' in region:
           years = ["15", "16"]
       else:
           years = ['15'] if '15' in region else ['16']
       if 'inc' in region:
           prong = ["1p", "3p"]
       else:
           prong = ['1p'] if '1p' in region else ['3p']
       replace = list(product(years, prong))
       #print "running over regions", replace

       if self.sample.type == "data":
         if self.pathmod_main: pathmod_main = self.pathmod_main
         h_list = []
         total = 0
         cutflow = 0

         for item in replace:
             if 'cutflow' in histname:
                 #print "Running over data", pathmod_main, histname.replace("inc",item[1]).replace('all',item[0])
                 h_list.append(self.sample.hist(pathmod=pathmod_main,histname=histname.replace("inc",item[1]).replace('all',item[0]),region=region.replace("inc",item[1]).replace('all',item[0]),icut=icut,sys=sys,mode=mode).Clone())
                 #print h_list
             else:
                 h_list.append(self.sample.hist(pathmod=pathmod_main,histname=histname,region=region.replace("inc",item[1]).replace('all',item[0]),icut=icut,sys=sys,mode=mode).Clone())
                 #h_list.append(self.sample.hist(pathmod=pathmod_main,histname='cutflow_presel_elallinc'.replace("inc",item[1]).replace('all',item[0]),region=region.replace("inc",item[1]).replace('all',item[0]),icut=icut,sys=sys,mode=mode).Clone())
         ### DEBUG
         #        c = self.sample.hist(pathmod=pathmod_main,histname='cutflow_presel_elallinc'.replace("inc",item[1]).replace('all',item[0]),region=region.replace("inc",item[1]).replace('all',item[0]),icut=icut,sys=sys,mode=mode).GetBinContent(16)
         #        t = self.sample.hist(pathmod=pathmod_main,histname=histname,region=region.replace("inc",item[1]).replace('all',item[0]),icut=icut,sys=sys,mode=mode).GetEntries()
         #        cutflow += c
         #        total   += t
         #        if not cutflow == total:
         #            print "#######################"
         #            print c, t
         #
         #print cutflow, total
         #total_everything = histutils.add_hists(h_list)
         #print 'total', total_everything.GetEntries()
         #print 'total cutflow', total_everything.GetBinContent(16)
         return histutils.add_hists(h_list)
       
      
       if self.sample.type == "mc":
         if self.pathmod_main: pathmod_main = self.pathmod_main
         h_list = []
         for item in replace:
             if 'cutflow' in histname:
                 h_list.append(self.sample.hist(pathmod=pathmod_main,histname=histname.replace("inc",item[1]).replace('all',item[0]),region=region.replace("inc",item[1]).replace('all',item[0]),icut=icut,sys=sys,mode=mode).Clone())
             else:
                 hist = self.sample.hist(pathmod=pathmod_main,histname=histname,region=region.replace("inc",item[1]).replace('all',item[0]),icut=icut,sys=sys,mode=mode)
                 if hist:
                     h_list.append(hist.Clone())
                 else:
                     print "Warning no hist for", self.sample.name, pathmod_main, histname, region.replace("inc",item[1]).replace('all',item[0]), icut, sys, mode
         
         return histutils.add_hists(h_list)


       if self.sample.type == "datadriven":
         
         if self.pathmod_aux: pathmod_aux = self.pathmod_aux
         
         assert self.data_sample, "ERROR: should define a data sample for data-driven estimation"
         assert self.mc_sample,   "ERROR: should define a mc sample for data-driven estimation"
         
         def getMCsub(pathmod, histname, region, sf=None):
             h_list = []
             total = 0
             for sample in self.mc_sample:
                 if 'cutflow' in histname:
                     hist = sample.hist(pathmod=pathmod,histname=histname,region=region,icut=icut,sys=sys,mode=mode).Clone()
                     hist.Scale(-1)
                 else:
                     hist = sample.hist(pathmod=pathmod,histname=histname,region=region,icut=icut,sys=sys,mode=mode).Clone()
                     hist.Scale(-1)
                 total += hist.Integral()
                 #print sample.name, hist.Integral()
                 #print sample.name, hist
                 if hist and sf:
                     hist.Scale(sf)
                 if hist:
                     h_list.append(hist.Clone())
                 else:
                     print "Warning no hist for", sample.name, pathmod_aux+'_'+aux_type, histname, region, icut, sys, mode
             print "mc sub", histname, total
             return h_list
         
         def addWjet(histname):
             fin_mu = ROOT.TFile.Open(os.path.join(self.ext_hist_path, "h_fake_norm_mu.root"))
             fin_el = ROOT.TFile.Open(os.path.join(self.ext_hist_path, "h_fake_norm_e.root"))
             
             if 'sr2' in region:
                 h_fwjets_mu = fin_mu.Get("h_fwjets_sr2")
                 h_fwjets_el = fin_el.Get("h_fwjets_sr2")
             elif 'sr3' in region:
                 h_fwjets_mu = fin_mu.Get("h_fwjets_sr3")
                 h_fwjets_el = fin_el.Get("h_fwjets_sr3")
             else:
                 h_fwjets_mu = fin_mu.Get("h_fwjets_sr1")
                 h_fwjets_el = fin_el.Get("h_fwjets_sr1")

             nf_mu_1p = h_fwjets_mu.GetBinContent(1)
             nf_mu_3p = h_fwjets_mu.GetBinContent(2)

             nf_el_1p = h_fwjets_el.GetBinContent(1)
             nf_el_3p = h_fwjets_el.GetBinContent(2)

             fin_el.Close()
             fin_mu.Close()

             # sum of os and ss contributions
             # ------------------------------ 
          
             nf_1p = 1.0
             nf_3p = 1.0
             
             if "_mu" in region: 
               nf_1p = nf_mu_1p
               nf_3p = nf_mu_3p
             if "_el" in region: 
               nf_1p = nf_el_1p
               nf_3p = nf_el_3p
             
             h_w_tot_list = []
             factor =  {"1p":nf_1p,"3p":nf_3p}

             region_os = ''
             region_ss = ''
             if "_mu" in region: region_os = region.replace("_mu","_osaidcrmu")
             if "_el" in region: region_os = region.replace("_el","_osaidcrel")
             if "_mu" in region: region_ss = region.replace("_mu","_sswjtcrmu")
             if "_el" in region: region_ss = region.replace("_el","_sswjtcrel")
          
             if "cutflow" in histname: histname_os = histname.replace(region, region_os)
             if "cutflow" in histname: histname_ss = histname.replace(region, region_ss)

             for item in replace:
                 print "adding to wjet", item
                 h_os = None
                 h_ss = None
                 if 'cutflow' in histname:
                     h_os_mc = getMCsub          (        pathmod_aux+'_osw',         histname_os.replace("inc",item[1]).replace('all',item[0]),       region_os.replace("inc",item[1]).replace('all',item[0]),sf=factor[item[1]])
                     h_ss_mc = getMCsub          (        pathmod_aux+'_ssw',         histname_ss.replace("inc",item[1]).replace('all',item[0]),       region_ss.replace("inc",item[1]).replace('all',item[0]),sf=factor[item[1]])
                     h_os = self.data_sample.hist(pathmod=pathmod_aux+'_osw',histname=histname_os.replace("inc",item[1]).replace('all',item[0]),region=region_os.replace("inc",item[1]).replace('all',item[0]),icut=icut,sys=sys,mode=mode).Clone()
                     h_ss = self.data_sample.hist(pathmod=pathmod_aux+'_ssw',histname=histname_ss.replace("inc",item[1]).replace('all',item[0]),region=region_ss.replace("inc",item[1]).replace('all',item[0]),icut=icut,sys=sys,mode=mode).Clone()
                 else:
                     #print pathmod_aux+'_osw', histname, region_os.replace("inc",item[1]).replace('all',item[0]), icut, sys, mode
                     h_os_mc = getMCsub          (        pathmod_aux+'_osw',         histname,       region_os.replace("inc",item[1]).replace('all',item[0]),sf=factor[item[1]])
                     h_ss_mc = getMCsub          (        pathmod_aux+'_ssw',         histname,       region_ss.replace("inc",item[1]).replace('all',item[0]),sf=factor[item[1]])
                     h_os = self.data_sample.hist(pathmod=pathmod_aux+'_osw',histname=histname,region=region_os.replace("inc",item[1]).replace('all',item[0]),icut=icut,sys=sys,mode=mode).Clone()
                     h_ss = self.data_sample.hist(pathmod=pathmod_aux+'_ssw',histname=histname,region=region_ss.replace("inc",item[1]).replace('all',item[0]),icut=icut,sys=sys,mode=mode).Clone()

                 h_os.Scale(factor[item[1]])
                 h_ss.Scale(factor[item[1]])
                 h_w_tot_list.append(h_os)
                 h_w_tot_list.append(h_ss)
                 # MC LIST ALREADY SCALED
                 h_w_tot_list+=h_os_mc
                 h_w_tot_list+=h_ss_mc
                 

             #return histutils.add_hists(h_w_tot_list)
             return h_w_tot_list
           
         def addQCD(histname):
             fin_mu = ROOT.TFile.Open(os.path.join(self.ext_hist_path,"h_fake_norm_mu.root"))
             fin_el = ROOT.TFile.Open(os.path.join(self.ext_hist_path,"h_fake_norm_e.root"))

             #h_fqcd_mu = fin_mu.Get("h_fqcd_sr1")
             #h_fqcd_el = fin_el.Get("h_fqcd_sr1")
             if 'sr2' in region:
                 h_fqcd_mu = fin_mu.Get("h_fqcd_sr2")
                 h_fqcd_el = fin_el.Get("h_fqcd_sr2")
             elif 'sr3' in region:
                 h_fqcd_mu = fin_mu.Get("h_fqcd_sr3")
                 h_fqcd_el = fin_el.Get("h_fqcd_sr3")
             else:
                 h_fqcd_mu = fin_mu.Get("h_fqcd_sr1")
                 h_fqcd_el = fin_el.Get("h_fqcd_sr1")

             nf_mu_1p = h_fqcd_mu.GetBinContent(1)
             nf_mu_3p = h_fqcd_mu.GetBinContent(2)

             nf_el_1p = h_fqcd_el.GetBinContent(1)
             nf_el_3p = h_fqcd_el.GetBinContent(2)

             fin_el.Close()
             fin_mu.Close()

             # sum of os and ss contributions
             # ------------------------------ 
          
             nf_1p = 1.0
             nf_3p = 1.0
             
             if "_mu" in region: 
               nf_1p = nf_mu_1p
               nf_3p = nf_mu_3p
             if "_el" in region: 
               nf_1p = nf_el_1p
               nf_3p = nf_el_3p
             
             h_qcd_tot_list = []
             factor =  {"1p":nf_1p,"3p":nf_3p}

             region_qcd = ''
             
             if "_mu" in region: region_qcd = region.replace("_mu","_antiisomu")
             if "_el" in region: region_qcd = region.replace("_el","_antiisoel")
          
             if "cutflow" in histname: histname = histname.replace(region, region_qcd)
             
             for item in replace:
                 print "adding to qcd", item
                 h_qcd = None
                 if 'cutflow' in histname:
                     h_qcd_mc = getMCsub          (        pathmod_aux+'_qcd',         histname.replace("inc",item[1]).replace('all',item[0]),       region_qcd.replace("inc",item[1]).replace('all',item[0]),sf=factor[item[1]])
                     h_qcd = self.data_sample.hist(pathmod=pathmod_aux+'_qcd',histname=histname.replace("inc",item[1]).replace('all',item[0]),region=region_qcd.replace("inc",item[1]).replace('all',item[0]),icut=icut,sys=sys,mode=mode).Clone()
                 else:
                     h_qcd_mc = getMCsub          (        pathmod_aux+'_qcd',         histname,       region_qcd.replace("inc",item[1]).replace('all',item[0]),sf=factor[item[1]])
                     h_qcd = self.data_sample.hist(pathmod=pathmod_aux+'_qcd',histname=histname,region=region_qcd.replace("inc",item[1]).replace('all',item[0]),icut=icut,sys=sys,mode=mode).Clone()

                 h_qcd.Scale(factor[item[1]])
                 h_qcd_tot_list.append(h_qcd)
                 # MC LIST ALREADY SCALED
                 h_qcd_tot_list+=h_qcd_mc

             #return histutils.add_hists(h_qcd_tot_list)
             return h_qcd_tot_list

         def addFF(histname):
             h_ff_tot_list=[]
             region_ff = ''
             
             #if "cutflow" in histname: histname = histname.replace(region, region_ff)
             
             if "_mu" in region: region_ff = region.replace("_mu","_mu")
             if "_el" in region: region_ff = region.replace("_el","_el")
          
             for item in replace:
                 print "adding to ff", item
                 h_ff = None
                 if 'cutflow' in histname:
                     #print histname, histname.replace("inc",item[1]).replace('all',item[0])
                     h_ff = self.data_sample.hist(pathmod=pathmod_aux+'_ff',histname=histname.replace("inc",item[1]).replace('all',item[0]),region=region_ff.replace("inc",item[1]).replace('all',item[0]),icut=icut,sys=sys,mode=mode).Clone()
                     h_ff_mc = getMCsub          (        pathmod_aux+'_ff',         histname.replace("inc",item[1]).replace('all',item[0]),       region_ff.replace("inc",item[1]).replace('all',item[0]))
                 else:
                     h_ff = self.data_sample.hist(pathmod=pathmod_aux+'_ff',histname=histname,region=region_ff.replace("inc",item[1]).replace('all',item[0]),icut=icut,sys=sys,mode=mode).Clone()
                     h_ff_mc = getMCsub          (        pathmod_aux+'_ff',         histname,       region_ff.replace("inc",item[1]).replace('all',item[0]))

                 h_ff_tot_list.append(h_ff)
                 # MC LIST ALREADY SCALED
                 h_ff_tot_list+=h_ff_mc

             #return histutils.add_hists(h_ff_tot_list)
             return h_ff_tot_list


         if self.sample.name == "Multijet_dd": 
             qcd = addQCD (histname)
             return histutils.add_hists(qcd)
         if self.sample.name == "Wjets_dd":    
             wjt = addWjet(histname)
             return histutils.add_hists(wjt)
         if self.sample.name == "Fake":
             print "Adding Fake sample"
             wjt = addWjet(histname)
             qcd = addQCD (histname)
             #return histutils.add_hists(wjt)
             return histutils.add_hists(wjt+qcd)
         if self.sample.name == "FF_Fake":
             ff  = addFF  (histname)
             return histutils.add_hists(ff)

    #__________________________________________________________________________
    def is_affected_by_systematic(self, sys):
        """
        Override BaseEstimator implementation.
        Check all daughter systematics
        """
        if sys in self.allowed_systematics: return True
        if self.data_sample:
          if self.data_sample.estimator.is_affected_by_systematic(sys): return True
        return False
    #__________________________________________________________________________
    def flush_hists(self):
        BaseEstimator.flush_hists(self)
        if self.data_sample:
          self.data_sample.estimator.flush_hists()


#------------------------------------------------------------
class DataBkgSubEstimator(BaseEstimator):
    '''
    DataBkgSub Estimator class 
    subtracts bkgs from data for estimate
    '''
    #____________________________________________________________
    def __init__(self,data_sample,mc_samples,mc_samples_rescales,**kw):
        BaseEstimator.__init__(self,**kw)
        self.data_sample         = data_sample
        self.mc_samples          = mc_samples
        self.mc_samples_rescales = mc_samples_rescales
    #____________________________________________________________
    def __hist__(self,pathmod=None,histname=None,region=None,icut=None,sys=None,mode=None):
        h = self.data_sample.hist(pathmod=pathmod,histname=histname,region=region,icut=icut,sys=sys,mode=mode).Clone()
        if self.mc_samples: 
            for s in self.mc_samples: 
                hs = s.hist(pathmod=pathmod,histname=histname,region=region,icut=icut,sys=sys,mode=mode)
                mc_rescale = -1.0
                if self.mc_samples_rescales: 
                  if s in self.mc_samples_rescales.keys():
                    mc_rescale *= self.mc_samples_rescales[s]
                h.Add(hs, mc_rescale)
        return h
    #__________________________________________________________________________
    def is_affected_by_systematic(self, sys):
        """
        Override BaseEstimator implementation.
        Check all daughter systematics
        """
        if sys in self.allowed_systematics: return True
        for s in self.mc_samples + [self.data_sample]: 
            if s.estimator.is_affected_by_systematic(sys): return True
        return False
    #__________________________________________________________________________
    def flush_hists(self):
        BaseEstimator.flush_hists(self)
        self.data_sample.estimator.flush_hists()
        for s in self.mc_samples: 
            s.estimator.flush_hists()


#------------------------------------------------------------
class AddOnEstimator(BaseEstimator):
    '''
    AddOnEstimator Estimator class 
    '''
    #____________________________________________________________
    def __init__(self,
            data_sample,
            mc_samples,
            rqcd_regions  = {}, #{sample : {"num" : "", "den" : "", "ncuts" : XX}}
            kf_regions    = {}, #{sample : {"OS" :  "", "SS" :  "", "ncuts" : XX}}
            addon_regions = {}, #{sample : {"OS" :  "", "SS" :  "", "ncuts" : XX}}
            print_info    = False,
            **kw
            ):

        BaseEstimator.__init__(self,**kw)
        self.data_sample       = data_sample
        self.mc_samples        = mc_samples
        self.data_minus_mc     = DataBkgSubEstimator(self.data_sample,None,None,**kw)
        self.data_minus_mc_num = DataBkgSubEstimator(self.data_sample,self.mc_samples,None,**kw)
        self.data_minus_mc_den = DataBkgSubEstimator(self.data_sample,self.mc_samples,None,**kw)
        self.rqcd_regions      = rqcd_regions 
        self.kf_regions        = kf_regions 
        self.addon_regions     = addon_regions 
        self.print_info        = print_info
        
        assert self.rqcd_regions,  "ERROR: must provide rqcd regions"
        assert self.kf_regions,    "ERROR: must provide kf regions"
        assert self.addon_regions, "ERROR: must provide addon regions"

    #____________________________________________________________
    def __hist__(self,region=None,pathmod=None,histname=None,icut=None,sys=None,mode=None):
        """
        implementation of nominal hist getter
        """
        # compute k-factors for OS and SS regions 
        kf_OS = {}  
        kf_SS = {}  
         
        # initialise k-factors
        for s in self.mc_samples:
           kf_OS[s] = 1.0
           kf_SS[s] = 1.0 
        
        kf_regions = self.kf_regions 
        
        # compute k-factors 
        for s in self.kf_regions.keys():
           tmp_samples = list(self.mc_samples)
           tmp_samples.remove(s)
           data_sub = copy(self.data_minus_mc)
           data_sub.mc_samples = tmp_samples
           
           kf_OS[s]  = histutils.full_integral(data_sub.hist(pathmod=pathmod,region=kf_regions[s]["OS"],histname=histname,icut=kf_regions[s]["ncuts"],sys=sys,mode=mode))
           kf_OS[s] /= histutils.full_integral(s.hist(pathmod=pathmod,region=kf_regions[s]["OS"],histname=histname,icut=kf_regions[s]["ncuts"],sys=sys,mode=mode))
           kf_SS[s]  = histutils.full_integral(data_sub.hist(pathmod=pathmod,region=kf_regions[s]["SS"],histname=histname,icut=kf_regions[s]["ncuts"],sys=sys,mode=mode))
           kf_SS[s] /= histutils.full_integral(s.hist(pathmod=pathmod,region=kf_regions[s]["SS"],histname=histname,icut=kf_regions[s]["ncuts"],sys=sys,mode=mode))
         

        # compute rqcd transfer factor
        # adding k_factors to the estimators
        self.data_minus_mc_num.mc_samples_rescales = kf_OS
        self.data_minus_mc_den.mc_samples_rescales = kf_SS
        
        rqcd_regions = self.rqcd_regions

        rqcd  = histutils.full_integral(self.data_minus_mc_num.hist(pathmod=pathmod,region=rqcd_regions[self.data_sample]["num"],histname=histname,icut=rqcd_regions[self.data_sample]["ncuts"],sys=sys,mode=mode))
        rqcd /= histutils.full_integral(self.data_minus_mc_den.hist(pathmod=pathmod,region=rqcd_regions[self.data_sample]["den"],histname=histname,icut=rqcd_regions[self.data_sample]["ncuts"],sys=sys,mode=mode))
        
        if self.print_info:
          print 
          print 
          print "++++++++++++++++++++++++++++++++++++++++"
          print "Iteration for %s" % self.sample.name
          print "++++++++++++++++++++++++++++++++++++++++"
          print 
          print "k-factors for %s, sys %s, sys_mode %s" % (histname,sys,mode)
          print "----------------------------------------"
          print "Sample | Region | k-factor | Rqcd"
          print "----------------------------------------"
          for s in self.kf_regions.keys():
            print "%s | %s | %.3lf | %.3lf" % (s.name,kf_regions[s]["OS"],kf_OS[s],rqcd)
            print "%s | %s | %.3lf | %.3lf" % (s.name,kf_regions[s]["SS"],kf_SS[s],rqcd)
            print 
        
        addon_regions = self.addon_regions

        h_fakes = self.data_sample.hist(pathmod=pathmod,region=addon_regions[self.data_sample]["SS"],histname=histname,icut=addon_regions[self.data_sample]["ncuts"]) 
        h_fakes.Scale(rqcd) 
        
        h_addon = {} 
        h_addon[self.data_sample] = h_fakes.Clone()
        
        for s in addon_regions.keys():
           if s==self.data_sample: continue
           h_addon[s] = s.hist(pathmod=pathmod,region=addon_regions[s]["OS"],histname=histname,icut=addon_regions[s]["ncuts"],sys=sys,mode=mode).Clone()
           h_addon[s].Scale(kf_OS[s])
           h_addon[s].Add(s.hist(pathmod=pathmod,region=addon_regions[s]["SS"],histname=histname,icut=addon_regions[s]["ncuts"],sys=sys,mode=mode).Clone(), -1.0 * rqcd * kf_SS[s])
        
        """
        ToDo: implement sys uncertainty for the scales!!!
        """
        if sys and "scale" in sys.name: pass
    
        if not self.sample.name == "fakes":
          for s in h_addon.keys():
            if self.sample.name == s.name:
              return  h_addon[s]
        else:
          return  histutils.add_hists(h_addon.values())
        
    
    #__________________________________________________________________________
    def add_systematics(self, sys):
        if not isinstance(sys,list): sys = [sys]
        self.allowed_systematics += sys
        self.sample.estimator.add_systematics(sys)
 
    #__________________________________________________________________________
    def is_affected_by_systematic(self, sys):
        """
        Override BaseEstimator implementation.
        """
        if sys in self.allowed_systematics: return True
        for s in self.mc_samples + [self.data_sample]: 
            if s.estimator.is_affected_by_systematic(sys): return True
        return False
    
    #__________________________________________________________________________
    def flush_hists(self):
        BaseEstimator.flush_hists(self)
        self.data_sample.estimator.flush_hists()
        for s in self.mc_samples:
          s.estimator.flush_hists()


#------------------------------------------------------------
class MergeEstimator(BaseEstimator):
    '''
    Merge Estimator class 
    This estimator can be used for splitting 
    the measurement into different pt bins
    '''
    #____________________________________________________________
    def __init__(self,samples,**kw):
        BaseEstimator.__init__(self,**kw)
        self.samples = samples
    #____________________________________________________________
    def __hist__(self,pathmod=None,region=None,icut=None,histname=None,sys=None,mode=None):
        hists = []
        #print "MergeEst", pathmod, histname, region
        for s in self.samples: 
            #print type(s)
            h = s.hist(pathmod=pathmod,region=region,icut=icut,histname=histname,sys=sys,mode=mode)
            if h: hists.append(h)
        h = histutils.add_hists(hists)
        return h

    #__________________________________________________________________________
    def add_systematics(self, sys):
        '''
        Override BaseEstimator implementation.
        Pass systematics to daughters.
        '''
        for s in self.samples: 
            s.estimator.add_systematics(sys)

    #__________________________________________________________________________
    def is_affected_by_systematic(self, sys):
        """
        Override BaseEstimator implementation.
        Check all daughter systematics
        """
        for s in self.samples: 
            if s.estimator.is_affected_by_systematic(sys): return True
        return False

    #__________________________________________________________________________
    def flush_hists(self):
        BaseEstimator.flush_hists(self)
        for s in self.samples:
            s.estimator.flush_hists()


# - - - - - - - - - - function defs - - - - - - - - - - - - #
#____________________________________________________________
def load_proxy_estimator(hm,input_sample):
    '''
    Sets a standard Estimator for samples of type "mc" or "data".
    If sample has daughters, sets the MergeEstimator.
    '''
    if input_sample.estimator == None:

        if input_sample.daughters: 
             input_sample.estimator = MergeEstimator(
                     input_sample.daughters,
                     sample=input_sample,
                     hm=hm,
                     )
             for d in input_sample.daughters:
                 load_proxy_estimator(hm,d)

        else: 
             #load proxy estimators
             if input_sample.type in ["data","mc"]: 
                    input_sample.estimator = ProxyEstimator(hm=hm,sample=input_sample)


#____________________________________________________________
def dir_name_max(filename, dirpath):
    '''
    gets the longest subdirectory in dirpath
    '''
    #f = fileio.open_file( filename )
    f = ROOT.TFile.Open( filename )
    assert f, 'failed to open file %s'%(filename)

    temp = None
    dir = f.GetDirectory(dirpath)
    if not dir:  
        log.warn( '%s doesn\'t exist in %s' % (dirpath,filename) )
    else:
        list = dir.GetListOfKeys()
        next = ROOT.TIter(list)
        d = next()
        temp = ''
        while d != None:
            if len(temp) < len(d.GetName()) and d.IsFolder():
                temp = d.GetName()
            d = next()
    f.Close()  
    return temp 


#____________________________________________________________
def dir_cuts(filename, dirpath):
    '''
    split dir name into individual cuts
    '''
    name = dir_name_max(filename,dirpath)
    return name.split('_')


#____________________________________________________________
def get_ncuts(filename, dirpath):
    cuts = dir_cuts(filename,dirpath)
    return len(cuts)

#____________________________________________________________
def get_icut(filename, dirpath,i):
    cuts = dir_cuts(filename,dirpath)
    if i>= len(cuts): 
        return None
    return cuts[i]

#____________________________________________________________
def get_icut_path(filename, dirpath,i):
    cuts = dir_cuts(filename,dirpath)
    if i>= len(cuts): 
        return None
    return '_'.join(cuts[:i+1])
    

## EOF
