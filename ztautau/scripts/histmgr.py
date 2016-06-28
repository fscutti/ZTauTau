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
    def get_file_path(self,samplename=None,sys=None,mode=None):
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
        path_to_file = os.path.join(self.basedir,syspath)
        filename = '%s.root' % (samplename)
        path_to_file = os.path.join(path_to_file,filename)
        return path_to_file

    #____________________________________________________________
    def hist(self, # retrieve folder with longer name
            histname   = None,
            samplename = None,
            region     = None,
            icut       = None, 
            sys        = None,
            mode       = None,
            ):

        assert histname,  'must define histname'
        assert samplename,    'must define samplename'
        if sys: 
            assert mode in ['up','dn'], "mode must be either 'up' or 'dn'"

        path_to_file = self.get_file_path(samplename,sys,mode)
        f = ROOT.TFile.Open(path_to_file)
        assert f, 'Failed to open input file!'

        ## get hist path
        path_to_hist = ''
        if region != None:
           path_to_hist = os.path.join('regions',region)
           
           ## check region exists
           if not f.Get(path_to_hist):
               f.Close()
               return None
           
           cutflow = get_icut_path(path_to_file, path_to_hist, icut)
           if icut == 0: pass #cutflow = "ALL"
           if not cutflow: 
               log.debug( '%s no cut: %s'% (samplename,icut) )
               f.Close()
               return None
           path_to_hist = os.path.join(path_to_hist,cutflow)
          
        path_to_hist = os.path.join(path_to_hist,histname)

        h = f.Get(path_to_hist)

        if not h:
            f.Close()
            print 'failed retrieveing hist: %s:%s'%(path_to_file,path_to_hist)
            return None
        
        h = h.Clone()
        h.SetDirectory(0)
        f.Close()

        ## apply flat sys (if specified)
        if sys and sys.flat_err:
            if mode == 'up': h.Scale(1.+sys.flat_err)
            else:            h.Scale(1.-sys.flat_err)

        return h
          
    #____________________________________________________________
    def get_nevents(self,samplename,sys=None,mode=None):
        '''
        retrieves cutflow hist for given sample 
        and given systematic (which contains the 
        total events before skim)
        '''
        assert samplename, 'must provide samplename'
    
        nevents = None 
        path_to_file = self.get_file_path(samplename,sys,mode)
        f = ROOT.TFile.Open(path_to_file)
        if f: 
            h = f.Get(self.cutflow_histname)
            if h: nevents = h.GetBinContent(8)
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
    def hist(self,histname=None,region=None,icut=None,sys=None,mode=None):
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
class Estimator(BaseEstimator):
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
    def __hist__(self,histname=None,region=None,icut=None,sys=None,mode=None):
        """
        implemenation of nominal hist getter
        """
        h = self.hm.hist(histname=histname,
                         samplename=self.sample.name,
                         region=region,
                         icut=icut,
                         sys=sys,
                         mode=mode,
                         )
        if h and self.sample.type == 'mc': 
            lumi_frac = self.get_mc_lumi_frac(sys,mode)
            h.Scale(self.hm.target_lumi * lumi_frac)

        return h    
    #____________________________________________________________
    def get_mc_lumi_frac(self,sys,mode):
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
            Ntotal  = self.hm.get_nevents(self.sample.name,sys,mode)
            # there seems to be no need for feff and kfactor
            #self.mc_lumi_frac[sys] = (xsec * feff * kfactor) / Ntotal if Ntotal else 0.0
            self.mc_lumi_frac[sys] = xsec / Ntotal if Ntotal else 0.0
        return self.mc_lumi_frac[sys]


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
    def __hist__(self,histname=None,region=None,icut=None,sys=None,mode=None):
        h = self.data_sample.hist(histname=histname,region=region,icut=icut,sys=sys,mode=mode).Clone()
        if self.mc_samples: 
            for s in self.mc_samples: 
                hs = s.hist(histname=histname,region=region,icut=icut,sys=sys,mode=mode)
                mc_rescale = -1.0
                if self.mc_samples_rescales: 
                  if s in self.mc_samples_rescales.keys():
                    mc_rescale *= self.mc_samples_rescales[s]
                h.Add(hs, mc_rescale)
        return h
    #__________________________________________________________________________
    def is_affected_by_systematic(self, sys):
        """
        Override BaseEstimator implemenation.
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
#        self.rregions          = rregions 
#        self.kregions          = kregions 
        self.addon_regions     = addon_regions 
        self.print_info        = print_info
        
        assert self.rqcd_regions,  "ERROR: must provide rqcd regions"
        assert self.kf_regions,    "ERROR: must provide kf regions"
        #assert self.rregions,  "ERROR: must provide rqcd regions"
        #assert self.kregions,    "ERROR: must provide kf regions"
        assert self.addon_regions, "ERROR: must provide addon regions"

    #____________________________________________________________
    def __hist__(self,region=None,histname=None,icut=None,sys=None,mode=None):
        
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
           
           kf_OS[s]  = histutils.full_integral(data_sub.hist(region=kf_regions[s]["OS"],histname=histname,icut=kf_regions[s]["ncuts"],sys=sys,mode=mode))
           kf_OS[s] /= histutils.full_integral(s.hist(region=kf_regions[s]["OS"],histname=histname,icut=kf_regions[s]["ncuts"],sys=sys,mode=mode))
           kf_SS[s]  = histutils.full_integral(data_sub.hist(region=kf_regions[s]["SS"],histname=histname,icut=kf_regions[s]["ncuts"],sys=sys,mode=mode))

           x = histutils.full_integral(s.hist(region=kf_regions[s]["SS"],histname=histname,icut=kf_regions[s]["ncuts"],sys=sys,mode=mode))
           if x == 0:
	   	kf_SS[s] == 1.0
           else:
           	kf_SS[s] /= histutils.full_integral(s.hist(region=kf_regions[s]["SS"],histname=histname,icut=kf_regions[s]["ncuts"],sys=sys,mode=mode))
           

        # compute rqcd transfer factor
        # adding k_factors to the estimators
        self.data_minus_mc_num.mc_samples_rescales = kf_OS
        self.data_minus_mc_den.mc_samples_rescales = kf_SS
        
        rqcd_regions = self.rqcd_regions

        rqcd  = histutils.full_integral(self.data_minus_mc_num.hist(region=rqcd_regions[self.data_sample]["num"],histname=histname,icut=rqcd_regions[self.data_sample]["ncuts"],sys=sys,mode=mode))
        rqcd /= histutils.full_integral(self.data_minus_mc_den.hist(region=rqcd_regions[self.data_sample]["den"],histname=histname,icut=rqcd_regions[self.data_sample]["ncuts"],sys=sys,mode=mode))
        
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

        h_fakes = self.data_sample.hist(region=addon_regions[self.data_sample]["SS"],histname=histname,icut=addon_regions[self.data_sample]["ncuts"]) 
        h_fakes.Scale(rqcd) 
        
        h_addon = {} 
        h_addon[self.data_sample] = h_fakes.Clone()
        
        for s in addon_regions.keys():
           if s==self.data_sample: continue
           h_addon[s] = s.hist(region=addon_regions[s]["OS"],histname=histname,icut=addon_regions[s]["ncuts"],sys=sys,mode=mode).Clone()
           h_addon[s].Scale(kf_OS[s])
           h_addon[s].Add(s.hist(region=addon_regions[s]["SS"],histname=histname,icut=addon_regions[s]["ncuts"],sys=sys,mode=mode).Clone(), -1.0 * rqcd * kf_SS[s])
        
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
        Override BaseEstimator implemenation.
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
    def __hist__(self,region=None,icut=None,histname=None,sys=None,mode=None):
        hists = []
        for s in self.samples: 
            h = s.hist(region=region,icut=icut,histname=histname,sys=sys,mode=mode)
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
        Override BaseEstimator implemenation.
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
def load_base_estimator(hm,input_sample):
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
             #print 'sample %s, assigned MergeEstimator' % (input_sample.name)
             for d in input_sample.daughters:
                 load_base_estimator(hm,d)

        else: 
             #load estimators
             if input_sample.type in ["data","mc"]: 
                    input_sample.estimator = Estimator(hm=hm,sample=input_sample)
                    #print 'sample %s, assigned Estimator' % (input_sample.name)


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
