## modules
import ROOT
from ztautau.samples import samples
import histmgr
#import systematics
from systematics import *
import tools
from pyplot import core
import os

#-----------------
# Configuration
#-----------------
lumi = 3209.05

basepath = '/data/fscutti/ztautau'
baserun  = "HistTEST"

basedir = os.path.join(basepath,baserun) 

core.setup(batch_mode=True)
hm = histmgr.HistMgr(basedir=basedir,target_lumi=lumi)

#-----------------
# Samples        
#-----------------

## data
data = samples.data

fakes = samples.fakes.copy()

## backgrounds 
mc_backgrounds = [
    samples.Wenu,
    samples.Wmunu,
    samples.Wtaunu,
    samples.Zee,
    samples.Zmumu,
    samples.Ztautau,
    samples.top,
   ]

## order backgrounds for plots
plot_backgrounds = [
    samples.Wenu,
    samples.Wmunu,
    samples.Wtaunu,
    samples.Zee,
    samples.Zmumu,
    samples.Ztautau,
    samples.top,
    #fakes,
    ]

## signals
plot_signals = []

#--------------
# Estimators
#--------------
for s in mc_backgrounds:# + signals + [data]: 
    histmgr.load_base_estimator(hm,s)


"""
fakes.estimator = histmgr.DataBkgSubEstimator(
    hm=hm,
    sample=fakes,
    data_sample=data,
    background_samples=mc_backgrounds,
    )
"""

#-----------------
# Systematics       
#-----------------
mc_sys = [
    SYS1, 
    SYS2,
    ]

## set mc systematics
#for s in mc_backgrounds + mumu_signals:
#    s.estimator.add_systematics(mc_sys)

## set r_qcd systematics
#fakes.estimator.add_systematics(RQCD)

#-----------------
# Write on file 
# (limits input)
#-----------------
"""
tools.write_plain_hists(
        backgrounds = plot_backgrounds,
        signals     = plot_signals,
        #data        = data,
        region      = "TEST",
        icut        = 1,
        histname    = 'muons/h_mu_pt',
        rebin       = 10,
        sys_dict    = None,
        )
"""

tools.plot_hist(
     plot_backgrounds,
     plot_signals, 
     #data       = data, 
     region     = "TEST",
     region_tag = "TEST tag",
     histname   = "muons/h_mu_pt",
     xmin       = 0.,
     xmax       = 150.,
     rebin      = 10,
     log        = False,
     icut       = 1,
     do_ratio_plot=False,
     plotsfile="test.root",
     )

## EOF



