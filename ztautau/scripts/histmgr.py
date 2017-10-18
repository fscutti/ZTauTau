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
        if sys and not sys.flat_err:
            if mode == 'up': syspath = sys.var_up
            else:            syspath = sys.var_dn

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
        
        path_to_file = self.get_file_path(pathmod,samplename,sampletype,sys,mode)
        f_list = []

        if os.path.isdir(path_to_file): f_list = [os.path.join(path_to_file,f) for f in os.listdir(path_to_file)] 
        else:                           f_list = [path_to_file]

        h_list = []
        
        for file in f_list:

            f = ROOT.TFile.Open(file)
            assert f, 'Failed to open input file!'
            
            ## get hist path
            path_to_hist = ''
            if region != None:
               path_to_hist = os.path.join('regions',region)
               
               ## check region exists
               if not f.Get(path_to_hist):
                   f.Close()
                   return None
               
               cutflow = get_icut_path(file,      path_to_hist, icut)
               if icut == 0: pass #cutflow = "ALL"
               if not cutflow: 
                   log.debug( '%s no cut: %s'% (samplename,icut) )
                   f.Close()
                   return None
               path_to_hist = os.path.join(path_to_hist,cutflow)
              
            path_to_hist = os.path.join(path_to_hist,histname)
            
            h = None
            h = f.Get(path_to_hist)
            
            if not h:
                f.Close()
                print 'failed retrieveing hist: %s:%s'%(file,path_to_hist)
                return None
            
            h = h.Clone()
            h.SetDirectory(0)
            
            f.Close()
            
            ## apply flat sys (if specified)
            if sys and sys.flat_err:
                if mode == 'up': h.Scale(1.+sys.flat_err)
                else:            h.Scale(1.-sys.flat_err)
            
            h_list.append(h)
        
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
              h = f.Get(self.cutflow_histname)
              assert h, 'get_nevents: failed to retrieve histogram from file'
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
    def get_hist_tag(self,histname=None,region=None,icut=None,sys=None,mode=None):
      if isinstance(region,list): region = "_".join(region)
      htag = "_".join([str(s) for s in [histname,region,icut,sys,mode]])
      return htag
        
    #____________________________________________________________
    def hist(self,pathmod=None,histname=None,region=None,icut=None,sys=None,mode=None):
        """
        Supports list of regions to be added
        """
        if not self.is_affected_by_systematic(sys): sys=mode=None
        htag = self.get_hist_tag(histname,region,icut,sys,mode)
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
        if h and self.sample.type == 'mc': 
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
            if mode == 'up': sysname = '%s_up'%(sys.name)
            else:            sysname = '%s_dn'%(sys.name)

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
        pathmod=None,     # force the estimator to read from preconfigured path
        ext_hist_path=None,
        **kw
        ):

        BaseEstimator.__init__(self,**kw)
        self.data_sample = data_sample
        self.pathmod = pathmod
        self.ext_hist_path = ext_hist_path

    #____________________________________________________________
    def __hist__(self,pathmod=None,histname=None,region=None,icut=None,sys=None,mode=None):
        
       if self.sample.type == "data":
         if self.pathmod: pathmod = self.pathmod
         h_list = []
         if "inc" in region:
           for r in ["1p","3p"]: h_list.append(self.sample.hist(pathmod=pathmod,histname=histname,region=region.replace("inc",r),icut=icut,sys=sys,mode=mode).Clone())
         else: h_list.append(self.sample.hist(pathmod=pathmod,histname=histname,region=region,icut=icut,sys=sys,mode=mode).Clone())
         
         return histutils.add_hists(h_list)
       
      
       if self.sample.type == "mc":
         if self.pathmod: pathmod = self.pathmod
         h_list = []
         if "inc" in region:
           for r in ["1p","3p"]: h_list.append(self.sample.hist(pathmod=pathmod,histname=histname,region=region.replace("inc",r),icut=icut,sys=sys,mode=mode).Clone())
         else: h_list.append(self.sample.hist(pathmod=pathmod,histname=histname,region=region,icut=icut,sys=sys,mode=mode).Clone())
         
         return histutils.add_hists(h_list)


       elif self.sample.type == "datadriven":
         
         
         assert self.data_sample, "ERROR: should define a data sample for data-driven estimation"
         
         if self.sample.name == "Wjets_dd":
         
           fin_mu = ROOT.TFile.Open(os.path.join(self.ext_hist_path,"presel","h_fake_norm_mu.root"))
           fin_el = ROOT.TFile.Open(os.path.join(self.ext_hist_path,"presel","h_fake_norm_e.root"))
           
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

           region_os = ''
           if "_mu" in region: region_os = region.replace("_mu","_osaidcrmu")
           if "_el" in region: region_os = region.replace("_el","_osaidcrel")
           
           if "inc" in region:
             for r,f in {"1p":nf_1p,"3p":nf_3p}.iteritems():
               h_os_inc = self.data_sample.hist(pathmod="NN_allregions_v2_data_osw",histname=histname,region=region_os.replace("inc",r),icut=icut,sys=sys,mode=mode).Clone()
               h_os_inc.Scale(f)
               h_w_tot_list.append(h_os_inc)
           else: 
             if "1p" in region:
               h_os_1p = self.data_sample.hist(pathmod="NN_allregions_v2_data_osw",histname=histname,region=region_os,icut=icut,sys=sys,mode=mode).Clone()
               h_os_1p.Scale(nf_1p) 
               h_w_tot_list.append(h_os_1p)
             if "3p" in region:
               h_os_3p = self.data_sample.hist(pathmod="NN_allregions_v2_data_osw",histname=histname,region=region_os,icut=icut,sys=sys,mode=mode).Clone()
               h_os_3p.Scale(nf_3p)
               h_w_tot_list.append(h_os_3p)

           region_ss = ''
           if "_mu" in region: region_ss = region.replace("_mu","_sswjtcrmu")
           if "_el" in region: region_ss = region.replace("_el","_sswjtcrel")
           
           if "inc" in region:
             for r,f in {"1p":nf_1p,"3p":nf_3p}.iteritems():
               h_ss_inc = self.data_sample.hist(pathmod="NN_allregions_v2_data_ssw",histname=histname,region=region_ss.replace("inc",r),icut=icut,sys=sys,mode=mode).Clone()
               h_ss_inc.Scale(f)
               h_w_tot_list.append(h_ss_inc)
           else: 
             if "1p" in region:
               h_ss_1p = self.data_sample.hist(pathmod="NN_allregions_v2_data_ssw",histname=histname,region=region_ss,icut=icut,sys=sys,mode=mode).Clone()
               h_ss_1p.Scale(nf_1p) 
               h_w_tot_list.append(h_ss_1p)
             if "3p" in region:
               h_ss_3p = self.data_sample.hist(pathmod="NN_allregions_v2_data_ssw",histname=histname,region=region_ss,icut=icut,sys=sys,mode=mode).Clone()
               h_ss_3p.Scale(nf_3p)
               h_w_tot_list.append(h_ss_3p)
           
           return histutils.add_hists(h_w_tot_list)



         if self.sample.name == "Multijet_dd":
           
           fin_mu = ROOT.TFile.Open(os.path.join(self.ext_hist_path,"presel","h_fake_norm_mu.root"))
           fin_el = ROOT.TFile.Open(os.path.join(self.ext_hist_path,"presel","h_fake_norm_e.root"))

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

           region_qcd = ''
           if "_mu" in region: region_qcd = region.replace("_mu","_antiisomu")
           if "_el" in region: region_qcd = region.replace("_el","_antiisoel")
           
           if "inc" in region:
             for r,f in {"1p":nf_1p,"3p":nf_3p}.iteritems():
               h_qcd_inc = self.data_sample.hist(pathmod="NN_allregions_v2_data_qcd",histname=histname,region=region_qcd.replace("inc",r),icut=icut,sys=sys,mode=mode).Clone()
               h_qcd_inc.Scale(f)
               h_qcd_tot_list.append(h_qcd_inc)
           else: 
             if "1p" in region:
               h_qcd_1p = self.data_sample.hist(pathmod="NN_allregions_v2_data_qcd",histname=histname,region=region_qcd,icut=icut,sys=sys,mode=mode).Clone()
               h_qcd_1p.Scale(nf_1p) 
               h_qcd_tot_list.append(h_qcd_1p)
             if "3p" in region:
               h_qcd_3p = self.data_sample.hist(pathmod="NN_allregions_v2_data_qcd",histname=histname,region=region_qcd,icut=icut,sys=sys,mode=mode).Clone()
               h_qcd_3p.Scale(nf_3p)
               h_qcd_tot_list.append(h_qcd_3p)

           return histutils.add_hists(h_qcd_tot_list)

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
        for s in self.samples: 
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
