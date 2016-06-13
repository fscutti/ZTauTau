## modules
import ROOT

import histmgr
import tools
import os

from ztautau.samples import samples
from ztautau.plots   import vars
from systematics     import *

from optparse import OptionParser

labels = {}
labels["TEST"] =    ["TEST REGION"]


#-----------------
# input
#-----------------
parser = OptionParser()
parser.add_option('-v', '--var', dest='vname',
                  help='varable name',metavar='VAR',default=None)
parser.add_option('-r', '--reg', dest='region',
                  help='region name',metavar='REG',default=None)
parser.add_option('-i', '--input', dest='indir',
                  help='input directory',metavar='INDIR',default=None)
parser.add_option('-o', '--output', dest='outdir',
                  help='output directory',metavar='OUTDIR',default=None)


(options, args) = parser.parse_args()

#-----------------
# Configuration
#-----------------
lumi = 3209.05

# Control regions
region = options.region

plotsfile = [options.vname,region]
plotsfile = "_".join(plotsfile)+".root"

plotsfile = os.path.join(options.outdir,plotsfile)

ROOT.gROOT.SetBatch(True)
hm = histmgr.HistMgr(basedir=options.indir,target_lumi=lumi)

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

fakes = samples.fakes.copy()


## signals
plot_signals = []

#--------------
# Estimators
#--------------
for s in mc_backgrounds: #+ plot_signals + [data] + [fakes]: 
    histmgr.load_base_estimator(hm,s)


"""
fakes.estimator = histmgr.FakeEstimator(
    hm=hm, 
    sample=fakes,
    data_sample = fakes,
    mc_samples = mc_backgrounds )
"""


#-----------------
# Systematics       
#-----------------
mc_sys = [
    SYS1, 
    SYS2,
    ]

## set mc systematics
#for s in mc_backgrounds:# + mumu_signals:
#    s.estimator.add_systematics(mc_sys)

vdict  = vars.vars_dict

#-----------------
# Plotting 
#-----------------

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


if "TEST" in options.region:
  tools.plot_hist(
     plot_backgrounds,
     plot_signals, 
     #data       = data, 
     region     = options.region,
     region_tag = labels[region],
     histname   = os.path.join(vdict[options.vname]['path'], vdict[options.vname]['hname']),
     xmin       = vdict[options.vname]['xmin'],
     xmax       = vdict[options.vname]['xmax'],
     rebin      = vdict[options.vname]['rebin'],
     log        = vdict[options.vname]['log'],
     icut       = 1,
     sys_dict=None,
     #sys_dict=sys_dict,
     do_ratio_plot=False,
     plotsfile=plotsfile,
     )

## EOF



