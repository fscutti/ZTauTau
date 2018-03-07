# encoding: utf-8
'''
hist.py
description: histogram class for plotting algorithm
'''

## modules

from array import array
dtype = {type(1.0):'d',type(1):'i'}



# - - - - - - - - - - - class defs  - - - - - - - - - - - - #
#------------------------------------------------------------
class Hist1D(object):
    '''
    class to hold histogram info for plotting
    '''
    #________________________________________________________
    def __init__(self,
            hname      = None,
            xtitle     = None,
            ytitle     = "Events",
            nbins      = None,
            xmin       = None,
            xmax       = None,
            dir        = None,
            instance   = None,
            vexpr      = None,
            log        = False,
            rebin_dict = False,
            **kw):
       
       self.hname      = hname
       self.xtitle     = xtitle
       self.ytitle     = ytitle
       self.nbins      = nbins
       self.xmin       = xmin
       self.xmax       = xmax
       self.dir        = dir
       self.instance   = instance
       self.vexpr      = vexpr
       self.log        = log
       self.rebin_dict = rebin_dict
        
       ## set additional key-word args
       # -------------------------------------------------------
       for k,w in kw.iteritems():
           setattr(self, k, w)
    
    #________________________________________________________
    def get_name(self):
      return self.__class__.__name__
    
    #________________________________________________________
    def apply_final_binning(self, rebin_dict=None):

      if not self.rebin_dict:
        self.rebin_dict = rebin_dict
      assert self.rebin_dict, "ERROR: no rebin dictionary provided for %s"%self.hname
      for k,v in self.rebin_dict.iteritems(): setattr(self,k,v)

      if not 'rebin' in self.rebin_dict.keys():
        self.rebin_dict['rebin'] = array(dtype[type(self.xmin)])
        wb = (self.xmax - self.xmin) / self.nbins
        for ib in xrange(self.nbins):
          self.rebin_dict['rebin'].append(self.xmin + wb * ib)
        self.rebin_dict['rebin'].append(self.xmax) 
      
      # Rebin histograms with a dictionary, reset name to remove 'h_'
      if self.hname.startswith("h_"):
         self.hname = self.hname[2:]

    #________________________________________________________
    def fill(self,var,weight):
      if self.instance:
        self.instance.Fill(var,weight)
      return
    
    #________________________________________________________
    def varcheck(self):
      if self.vexpr:
        if "store" in self.vexpr:
          var = self.vexpr.split("'")[1]
          return  "bool('%s' in self.store.keys())" % var 
          #return  "bool(len(self.store['%s'])>=1)" % var 
        if "chain" in self.vexpr:
          pref,mid,var = self.vexpr.split(".")
          return "bool(hasattr(self.chain, '%s'))" % var 


#------------------------------------------------------------
class Hist2D(object):
    '''
    class to hold histogram info for plotting
    '''
    #________________________________________________________
    def __init__(self,
            hname      = None,
            xtitle     = None,
            ytitle     = None,
            nbinsx     = None,
            nbinsy     = None,
            xmin       = None,
            xmax       = None,
            ymin       = None,
            ymax       = None,
            dir        = None,
            instance   = None,
            vexpr      = None,
            log        = False,
            rebin_dict = None,
            **kw):
       
       self.hname      = hname
       self.xtitle     = xtitle
       self.ytitle     = ytitle
       self.nbinsx     = nbinsx
       self.nbinsy     = nbinsy
       self.xmin       = xmin
       self.xmax       = xmax
       self.ymin       = ymin
       self.ymax       = ymax
       self.dir        = dir
       self.instance   = instance
       self.vexpr      = vexpr
       self.kw         = kw
       self.rebin_dict = rebin_dict 
       self.log        = log

       ## set additional key-word args
       # -------------------------------------------------------
       for k,w in kw.iteritems():
           setattr(self, k, w)

    #________________________________________________________
    def get_name(self):
      return self.__class__.__name__
    
    #________________________________________________________
    def apply_final_binning(self, rebin_dict=False):

      # Rebin histograms with a dictionary, reset name to remove 'h_'
      if not self.rebin_dict:
        self.rebin_dict = rebin_dict
      assert self.rebin_dict, "ERROR: no rebin dictionary provided for %s"%self.hname
      for k,v in self.rebin_dict.iteritems(): setattr(self,k,v)

      if not 'rebin' in self.rebin_dict.keys():
        self.rebin_dict['rebin'] = {}
        self.rebin_dict['rebin']['rebinx'] = array(dtype[type(self.xmin)])
        wb = (self.xmax - self.xmin) / self.nbinsx
        for ib in xrange(self.nbinsx):
          self.rebin_dict['rebin']['rebinx'].append(self.xmin + wb * ib)
        self.rebin_dict['rebin']['rebinx'].append(self.xmax) 
      
        self.rebin_dict['rebin']['rebiny'] = array(dtype[type(self.ymin)])
        wb = (self.ymax - self.ymin) / self.nbinsy
        for ib in xrange(self.nbinsy):
          self.rebin_dict['rebin']['rebiny'].append(self.ymin + wb * ib)
        self.rebin_dict['rebin']['rebiny'].append(self.ymax) 
      
      # Rebin histograms with a dictionary, reset name to remove 'h_'
      if self.hname.startswith("h_"):
         self.hname = self.hname[2:]

    #________________________________________________________
    def set_axis_titles(self):
      if self.instance:
        self.instance.GetXaxis().SetTitle(self.xtitle)
        self.instance.GetYaxis().SetTitle(self.ytitle)
      return
    
    #________________________________________________________
    def fill(self,varx,vary,weight):
      if self.instance:
        self.instance.Fill(varx,vary,weight)
      return

    #________________________________________________________
    def varcheck(self):
      return "True"


class Profile(object):
    '''
    class to hold histogram info for plotting
    '''
    #________________________________________________________
    def __init__(self,
            hname      = None,
            xtitle     = None,
            ytitle     = None,
            nbinsx     = None,
            nbinsy     = None,
            xmin       = None,
            xmax       = None,
            ymin       = None,
            ymax       = None,
            dir        = None,
            instance   = None,
            vexpr      = None,
            rebin_dict = None,
            **kw):
       
       self.hname      = hname
       self.xtitle     = xtitle
       self.ytitle     = ytitle
       self.nbinsx     = nbinsx
       self.nbinsy     = nbinsy
       self.xmin       = xmin
       self.xmax       = xmax
       self.ymin       = ymin
       self.ymax       = ymax
       self.dir        = dir
       self.instance   = instance
       self.vexpr      = vexpr
       self.rebin_dict = rebin_dict 

       ## set additional key-word args
       # -------------------------------------------------------
       for k,w in kw.iteritems():
           setattr(self, k, w)

    #________________________________________________________
    def get_name(self):
      return self.__class__.__name__
    
    #________________________________________________________
    def apply_final_binning(self, rebin_dict=False):
      # Rebin histograms with a dictionary, reset name to remove 'h_'
      if not self.rebin_dict:
        self.rebin_dict = rebin_dict
      assert self.rebin_dict, "ERROR: no rebin dictionary provided for %s"%self.hname
      for k,v in self.rebin_dict.iteritems(): setattr(self,k,v)

      if not 'rebin' in self.rebin_dict.keys():
        self.rebin_dict['rebin'] = {}
        self.rebin_dict['rebin']['rebinx'] = array(dtype[type(self.xmin)])
        wb = (self.xmax - self.xmin) / self.nbinsx
        for ib in xrange(self.nbinsx):
          self.rebin_dict['rebin']['rebinx'].append(self.xmin + wb * ib)
        self.rebin_dict['rebin']['rebinx'].append(self.xmax) 
      
        self.rebin_dict['rebin']['rebiny'] = array(dtype[type(self.ymin)])
        wb = (self.ymax - self.ymin) / self.nbinsy
        for ib in xrange(self.nbinsy):
          self.rebin_dict['rebin']['rebiny'].append(self.ymin + wb * ib)
        self.rebin_dict['rebin']['rebiny'].append(self.ymax) 
      
      # Rebin histograms with a dictionary, reset name to remove 'h_'
      if self.hname.startswith("h_"):
         self.hname = self.hname[2:]
    
    #________________________________________________________
    def set_axis_titles(self):
      if self.instance:
        self.instance.GetXaxis().SetTitle(self.xtitle)
        self.instance.GetYaxis().SetTitle(self.ytitle)
      return
    
    #________________________________________________________
    def fill(self,varx,vary,weight):
      if self.instance:
        self.instance.Fill(varx,vary,weight)
      return

    #________________________________________________________
    def varcheck(self):
      return "True"


## EOF




