## modules
import ROOT

import histmgr
import funcs
import os

from ztautau.samples import samples
from ztautau.plots   import vars
from systematics     import *

from optparse import OptionParser


#-----------------
# input
#-----------------
parser = OptionParser()
parser.add_option('-v', '--var', dest='vname',
                  help='varable name',metavar='VAR',default=None)
parser.add_option('-r', '--reg', dest='region',
                  help='region name',metavar='REG',default=None)
parser.add_option('-l', '--lab', dest='label',
                  help='region label',metavar='LAB',default=None)
parser.add_option('-c', '--icut', dest='icut',
                  help='number of cuts',metavar='ICUT',default=None)
parser.add_option('-p', '--makeplot', dest='makeplot',
                  help='make plot',metavar='MAKEPLOT',default=None)
parser.add_option('-i', '--input', dest='indir',
                  help='input directory',metavar='INDIR',default=None)
parser.add_option('-o', '--output', dest='outdir',
                  help='output directory',metavar='OUTDIR',default=None)


(options, args) = parser.parse_args()

#-----------------
# Configuration
#-----------------
lumi =  3158.13

# Control regions
plotsfile = []
if options.makeplot == "False":
  plotsfile.append("hists")
plotsfile.append(options.vname)  
plotsfile.append(options.region)  

plotsfile = "_".join(plotsfile)+".root"
plotsfile = os.path.join(options.outdir,plotsfile)


ROOT.gROOT.SetBatch(True)
hm = histmgr.HistMgr(basedir=options.indir,target_lumi=lumi)

#-----------------
# Samples        
#-----------------

## data
data = samples.data

## backgrounds 
mc_backgrounds = []
mc_backgrounds.append(samples.Wjets)
mc_backgrounds.append(samples.Zlljets)
#mc_backgrounds.append(samples.top)

## signals
mc_signals = []
mc_signals.append(samples.Zttjets)

# This is the sum of all addons
fakes = samples.fakes.copy()

# These are the components
addon_data    = samples.addon_data.copy()
addon_Wjets   = samples.addon_Wjets.copy()
addon_Zlljets = samples.addon_Zlljets.copy()
addon_Zttjets = samples.addon_Zttjets.copy()
#addon_top     = samples.addon_top.copy()

addon_backgrounds = []
addon_backgrounds.append(addon_data)
addon_backgrounds.append(addon_Wjets)
addon_backgrounds.append(addon_Zlljets)
addon_backgrounds.append(addon_Zttjets)
#addon_backgrounds.append(addon_top)



#---------------------------
# Regions for bkg estimation
#---------------------------

# k-factors
kf_regions = {}
kf_regions[samples.Wjets]   = {"OS":"Wjets_OS", "SS":"Wjets_SS", "ncuts":2}
#kf_regions[samples.top]     = {"OS":"","SS":"","ncuts"}
#kf_regions[samples.Zlljets] = {"OS":"","SS":"","ncuts"}
     
# Rqcd
rqcd_regions = {}
rqcd_regions[data]   = {"num":"AntiIsoCR_OS", "den":"AntiIsoCR_SS", "ncuts":3}
     
     
# Add-On
# always provide the full set of samples here
addon_regions = {}
addon_regions[data]            = {"SS":"SR_SS", "ncuts":4} # don't really need OS for data do you?
addon_regions[samples.Wjets]   = {"OS":"SR", "SS":"SR_SS", "ncuts":4}
addon_regions[samples.Zlljets] = {"OS":"SR", "SS":"SR_SS", "ncuts":4}
addon_regions[samples.Zttjets] = {"OS":"SR", "SS":"SR_SS", "ncuts":4}
#addon_regions[samples.top]     = {"OS":"SR", "SS":"Ztau", "ncuts":4}



#--------------
# Estimators
#--------------
for s in mc_backgrounds + mc_signals + [data]: 
    histmgr.load_base_estimator(hm,s)

"""
fakes.estimator = histmgr.DataBkgSubEstimator(
     hm=hm,
     sample=fakes,
     data_sample=data,
     mc_samples=mc_backgrounds+mc_signals,
     )
"""
for b in addon_backgrounds + [fakes]:

  b.estimator = histmgr.AddOnEstimator(
       hm            = hm,
       sample        = b,
       data_sample   = data,
       mc_samples    = mc_backgrounds + mc_signals,
       rqcd_regions  = rqcd_regions,
       kf_regions    = kf_regions,
       addon_regions = addon_regions,
       print_info    = True,
       )


#-----------------
# Systematics       
#-----------------
# just an example ...
mc_sys = [
    SYS1, 
    SYS2,
    ]

## set mc systematics
#for s in mc_backgrounds + mumu_signals:
#    s.estimator.add_systematics(mc_sys)

#fakes.estimator.add_systematics(RQCD)

vdict  = vars.vars_dict

#-----------------
# Plotting 
#-----------------

## order backgrounds for plots.
## different typologies of background
## can be mixed, e.g. semples.somecrap 
## with addon_somecrap. However, it does
## not make sense to plot fakes and addons
## on the same plot!

## backgrounds 
plot_backgrounds = []
#plot_backgrounds.append(fakes)

plot_backgrounds.append(addon_data)
plot_backgrounds.append(addon_Wjets)
plot_backgrounds.append(addon_Zlljets)
###plot_backgrounds.append(addon_top)

## signals
plot_signals = []
#plot_signals.append(addon_Zttjets)
plot_signals.append(samples.Zttjets)


if options.makeplot == "True":
 funcs.plot_hist(
    backgrounds   = plot_backgrounds,
    signal        = plot_signals, 
    data          = data,
    region        = options.region,
    label         = options.label,
    histname      = os.path.join(vdict[options.vname]['path'],vdict[options.vname]['hname']),
    xmin          = vdict[options.vname]['xmin'],
    xmax          = vdict[options.vname]['xmax'],
    rebin         = vdict[options.vname]['rebin'],
    log           = vdict[options.vname]['log'],
    icut          = int(options.icut),
    sys_dict      = sys_dict,
    do_ratio_plot = True,
    plotsfile     = plotsfile,
    )

else:
 funcs.write_hist(
         backgrounds = mc_backgrounds,
         signal      = mc_signals, # This can be a list
         data        = data,
         region      = options.region,
         icut        = int(options.icut),
         histname    = os.path.join(vdict[options.vname]['path'],vdict[options.vname]['hname']),
         rebin       = vdict[options.vname]['rebin'],
         sys_dict    = None,
         outname     = plotsfile
         )
 ## EOF



