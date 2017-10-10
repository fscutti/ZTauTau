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
            hname    = None,
            xtitle   = None,
            ytitle   = None,
            nbinsx   = None,
            nbinsy   = None,
            xmin     = None,
            xmax     = None,
            ymin     = None,
            ymax     = None,
            dir      = None,
            instance = None,
            vexpr    = None,
            **kw):
       
       self.hname    = hname
       self.xtitle   = xtitle
       self.ytitle   = ytitle
       self.nbinsx   = nbinsx
       self.nbinsy   = nbinsy
       self.xmin     = xmin
       self.xmax     = xmax
       self.ymin     = ymin
       self.ymax     = ymax
       self.dir      = dir
       self.instance = instance
       self.vexpr    = vexpr

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
      # Rebin histograms with a dictionary, reset name to remove 'h_'
      if 'rebin_dict' in kw.keys():
          if 'xmin' in self.rebin_dict: 
              self.xmin  = self.rebin_dict['xmin']
          if 'xmax' in self.rebin_dict: 
              self.xmax  = self.rebin_dict['xmax']
          if 'nbinsx' in self.rebin_dict: 
              self.nbins = self.rebin_dict['nbinsx']
          if 'ymin' in self.rebin_dict: 
              self.ymin  = self.rebin_dict['ymin']
          if 'ymax' in self.rebin_dict: 
              self.ymax  = self.rebin_dict['ymax']
          if 'nbinsy' in self.rebin_dict: 
              self.nbins = self.rebin_dict['nbinsy']
          if 'log' in self.rebin_dict.keys():
              self.log = self.rebin_dict['log']
          self.hname = self.hname[2:]
      elif rebin_dict:
          if 'xmin' in rebin_dict: 
              self.xmin  = rebin_dict['xmin']
          if 'xmax' in rebin_dict: 
              self.xmax  = rebin_dict['xmax']
          if 'nbinsx' in rebin_dict: 
              self.nbins = rebin_dict['nbinsx']
          if 'ymin' in rebin_dict: 
              self.ymin  = rebin_dict['ymin']
          if 'ymax' in rebin_dict: 
              self.ymax  = rebin_dict['ymax']
          if 'nbinsy' in rebin_dict: 
              self.nbins = rebin_dict['nbinsy']
          if 'log' in rebin_dict.keys():
              self.log = rebin_dict['log']
          self.hname = hname[2:]
      else:
          print "No dictionary provided!"
    
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




