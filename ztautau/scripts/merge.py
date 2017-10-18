## modules
import ROOT

import histmgr
import funcs
import os

from ztautau.samples import samples
from ztautau.hists   import final_binning_hists
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


norm_factors_path = "/coepp/cephfs/share/atlas/LFV/ligang"


(options, args) = parser.parse_args()

#-----------------
# Configuration
#-----------------
lumi = 3212.96 if '15' in options.region else 32861.2 if '16' in options.region else 3212.96+32861.2

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
dataest = samples.data.copy() # sample to be used for dd estimation
data = samples.data.copy()    # sample for plotting

## backgrounds 
mc_backgrounds = []
mc_backgrounds.append(samples.Wtaunu)
mc_backgrounds.append(samples.Wlepnu)
mc_backgrounds.append(samples.Zleplep)
mc_backgrounds.append(samples.Ztautau)
mc_backgrounds.append(samples.top)

## signals
mc_signals = []
mc_signals.append(samples.lfvh)


# -----------------------
# Load estimators
# -----------------------

# proxy estimator 
# for fundamental samples
# -----------------------
for s in mc_backgrounds + mc_signals + [data,dataest]: 
    histmgr.load_proxy_estimator(hm,s)


# data driven backgrounds
# -----------------------
Wjets_dd = samples.Wjets_dd
Multijet_dd = samples.Multijet_dd

Wjets_dd.estimator    = histmgr.SimpleEstimator(hm=hm,
                                                sample=Wjets_dd,
                                                data_sample=dataest,
                                                ext_hist_path=norm_factors_path
                                                )

Multijet_dd.estimator = histmgr.SimpleEstimator(hm=hm,
                                                sample=Multijet_dd,
                                                data_sample=dataest,
                                                ext_hist_path=norm_factors_path
                                                )

data.estimator = histmgr.SimpleEstimator(hm=hm,
                                             pathmod="NN_allregions_v2_data_main", # force the estimator to read from this path
                                             sample=data.copy()
                                             )

# rest of samples
# -----------------------
for s in mc_signals + mc_backgrounds:
  s.estimator = histmgr.SimpleEstimator(hm=hm,
                                        pathmod="NN_allregions_v2_mc", # force the estimator to read from this path
                                        sample=s.copy())



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


hdict  = final_binning_hists.hist_dict


#-----------------
# Plotting 
#-----------------

## backgrounds 
plot_backgrounds = []
plot_backgrounds.append(Wjets_dd)
plot_backgrounds.append(Multijet_dd)
plot_backgrounds.append(samples.Ztautau)
plot_backgrounds.append(samples.Zleplep)
plot_backgrounds.append(samples.top)

## signals
plot_signals = []
plot_signals.append(samples.lfvh)

if options.makeplot == "True":
 funcs.plot_hist(
    backgrounds   = plot_backgrounds,
    signal        = plot_signals, 
    data          = data,
    region        = options.region,
    label         = options.label,
    histname      = os.path.join(hdict[options.vname]['dir'],hdict[options.vname]['hname']),
    rebin         = hdict[options.vname]['rebin_dict']['rebin'],
    log           = hdict[options.vname]['log'],
    icut          = int(options.icut),
    sys_dict      = None,
    do_ratio_plot = False,
    plotsfile     = plotsfile,
    )

else:
 funcs.write_hist(
         backgrounds = plot_backgrounds,
         signal      = plot_signals,      
         data        = data,
         region      = options.region,
         icut        = int(options.icut),
         histname    = os.path.join(hdict[options.vname]['dir'],hdict[options.vname]['hname']),
         rebin       = hdict[options.vname]['rebin_dict']['rebin'],
         sys_dict    = None,
         outname     = plotsfile
         )
 ## EOF



