## modules
import ROOT

import histmgr
import funcs
import os

from ztautau.samples import samples
from ztautau.hists   import final_binning_hists
from systematics     import *

from optparse import OptionParser

ROOT.gErrorIgnoreLevel = ROOT.kError

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
parser.add_option('-b', '--background', dest='bkgd',
                  help='background estimation',metavar='BKGD',default=None)
parser.add_option('-u', '--printcutflow', dest='printcutflow',
                  help='prints cutflows',metavar='PRINTCUTFLOW',default=None)
parser.add_option('-t', '--regiontype', dest='regiontype', 
                  help='region type', metavar='REGTYPE',default=None)


(options, args) = parser.parse_args()

#-----------------
# Configuration
#-----------------
lumi = 3212.96 if '15' in options.region else 32861.2 if '16' in options.region else 3212.96+32861.2

# Control regions
plotsfile = ["out"]
if options.makeplot == "False":
  plotsfile.append("hists")
plotsfile.append(options.vname)  

#norm_factors_path = "/coepp/cephfs/share/atlas/LFV/ligang/171221"
#norm_factors_path = "/coepp/cephfs/share/atlas/LFV/ligang/180203"
norm_factors_path = "/coepp/cephfs/share/atlas/LFV/ligang/180217"
if options.region:
  plotsfile.append(options.region)  
  if 'sr' in options.region:
      norm_factors_path+='/sr/fake_norm_dir/'
  else:
      norm_factors_path+='/presel/fake_norm_dir/'
if 'tight' in options.regiontype:
    norm_factors_path += 'july_tight'
else:
    norm_factors_path += 'july_medium'

print norm_factors_path
plotsfile = "_".join(plotsfile)+".root"
plotsfile = os.path.join(options.outdir,plotsfile)


ROOT.gROOT.SetBatch(True)
sys_dict = None
from ztautau.hists.Systematics import sys_dict
hm = histmgr.HistMgr(basedir=options.indir,target_lumi=lumi)

#-----------------
# Samples        
#-----------------

## data
dataest = samples.data.copy()
data    = samples.data.copy()

## backgrounds 
mc_backgrounds = []
#mc_backgrounds.append(samples.Wtaunu)
#mc_backgrounds.append(samples.Wlepnu)
mc_backgrounds.append(samples.Wjets)
mc_backgrounds.append(samples.Zleplep)
mc_backgrounds.append(samples.Ztautau)
mc_backgrounds.append(samples.top)
mc_backgrounds.append(samples.diboson)
mc_backgrounds.append(samples.smh)


## signals
mc_signals = []
#mc_signals.append(samples.lfvh)
mc_signals.append(samples.lfvh_ggH)
mc_signals.append(samples.lfvh_VBF)


# -----------------------
# Load estimators
# -----------------------

# proxy estimator 
# for fundamental samples
# -----------------------
for s in mc_backgrounds + mc_signals + [data,dataest]: 
    histmgr.load_proxy_estimator(hm,s)

mcest = []
for s in mc_backgrounds:
    mcest.append(s.copy())

# data driven backgrounds

regiontype = 'tight' if 'tight' in options.regiontype else 'ac' if 'ac' in options.regiontype else 'presel'
print "NN_allregions_%s" % regiontype

FF_Fake = samples.FF_Fake
FF_Fake.estimator = histmgr.SimpleEstimator(hm=hm,
                                         sample=FF_Fake,
                                         pathmod_aux="NN_allregions_%s" % regiontype, # force the estimator to read from this path
                                         data_sample=dataest.copy(),
                                         mc_sample=mcest,
                                         ext_hist_path=norm_factors_path
                                         )

Fake = samples.Fake
Fake.estimator = histmgr.SimpleEstimator(hm=hm,
                                         sample=Fake,
                                         pathmod_aux="NN_allregions_%s" % regiontype, # force the estimator to read from this path
                                         data_sample=dataest.copy(),
                                         mc_sample=mcest,
                                         ext_hist_path=norm_factors_path
                                         )

Wjets_dd = samples.Wjets_dd
Wjets_dd.estimator = histmgr.SimpleEstimator(hm=hm,
                                         sample=Wjets_dd,
                                         pathmod_aux="NN_allregions_%s" % regiontype, # force the estimator to read from this path
                                         data_sample=dataest.copy(),
                                         mc_sample=mcest,
                                         ext_hist_path=norm_factors_path
                                         )

Multijet_dd = samples.Multijet_dd
Multijet_dd.estimator = histmgr.SimpleEstimator(hm=hm,
                                         sample=Multijet_dd,
                                         pathmod_aux="NN_allregions_%s" % regiontype, # force the estimator to read from this path
                                         data_sample=dataest.copy(),
                                         mc_sample=mcest,
                                         ext_hist_path=norm_factors_path
                                         )


data.estimator = histmgr.SimpleEstimator(hm=hm,
                                         pathmod_main="NN_allregions_%s_main" % regiontype, # force the estimator to read from this path
                                         sample=data.copy(),
                                         )

# rest of samples
# -----------------------
for s in mc_signals + mc_backgrounds:
  s.estimator = histmgr.SimpleEstimator(hm=hm,
                                        pathmod_main="NN_allregions_%s_main" % regiontype, # force the estimator to read from this path
                                        sample=s.copy())
  s.estimator.add_systematics(sys_dict.keys())



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
#samples.Ztautau .add_systematics(sys_dict)
#samples.Zleplep .add_systematics(sys_dict)
#samples.Wjets   .add_systematics(sys_dict)
#samples.top     .add_systematics(sys_dict)
#samples.diboson .add_systematics(sys_dict)
#samples.smh     .add_systematics(sys_dict)
#samples.lfvh_ggH.add_systematics(sys_dict)
#samples.lfvh_VBF.add_systematics(sys_dict)

## backgrounds 
plot_backgrounds = []
#if options.bkgd == 'lg':
#    plot_backgrounds.append(Fake)
#elif options.bkgd == 'ff':
#    plot_backgrounds.append(FF_Fake)
#    pass
plot_backgrounds.append(samples.Ztautau)
plot_backgrounds.append(samples.Zleplep)
plot_backgrounds.append(samples.Wjets  )
plot_backgrounds.append(samples.top    )
plot_backgrounds.append(samples.diboson)
plot_backgrounds.append(samples.smh    )

#plot_backgrounds.append(Wjets_dd)
#plot_backgrounds.append(Multijet_dd)

## signals
plot_signals = []
#plot_signals.append(samples.lfvh)
plot_signals.append(samples.lfvh_ggH)
plot_signals.append(samples.lfvh_VBF)

#print hdict.keys()
#print options.vname
#if options.vname.startswith('h_'): options.vname = options.vname.replace('h_','')

if (options.printcutflow == "False" or not options.printcutflow):
    if hdict[options.vname]['dir'] == 'hist_2d': blind = False
    else:
        blind = hdict[options.vname]['rebin_dict']['blind_range']if 'blind_range' in hdict[options.vname]['rebin_dict'].keys() else False
    do_ratio_plot = False if hdict[options.vname]['dir'] == 'profile' else True
    do_profile    = True  if hdict[options.vname]['dir'] == 'profile' else False
    do_ratio_plot = False if hdict[options.vname]['dir'] == 'hist_2d' else True
    do_profile    = False#True  if hdict[options.vname]['dir'] == 'hist_2d' else False
    do_2d         = True  if hdict[options.vname]['dir'] == 'hist_2d' else False

    #print "do_profile", do_profile
    #print "do_ratio_plot", do_profile
    #print hdict[options.vname]['rebin_dict']

if options.makeplot == "True" and (options.printcutflow == "False" or not options.printcutflow):
 funcs.plot_hist(
    backgrounds   = plot_backgrounds,
    signal        = plot_signals,
    data          = data,#data,
    region        = options.region,
    label         = options.label,
    histname      = os.path.join(hdict[options.vname]['dir'],hdict[options.vname]['hname']),
    rebin         = hdict[options.vname]['rebin_dict'],
    blind         = blind,
    log           = hdict[options.vname]['log'] if 'log' in hdict[options.vname].keys() else False,
    icut          = int(options.icut),
    sys_dict      = None,
    do_ratio_plot = do_ratio_plot,
    do_profile    = do_profile,
    do_2d         = do_2d,#False,
    profile_2d    = True,
    plotsfile     = plotsfile,
    sig_rescale   = 10
    )

elif options.makeplot == "False" and (options.printcutflow == "False" or not options.printcutflow):
 funcs.write_hist(
         backgrounds = plot_backgrounds,
         signal      = plot_signals,
         data        = False,#data,
         region      = options.region,
         icut        = int(options.icut),
         histname    = os.path.join(hdict[options.vname]['dir'],hdict[options.vname]['hname']),
         rebin       = hdict[options.vname]['rebin_dict'],
         sys_dict    = sys_dict,
         outname     = plotsfile
         )

elif options.printcutflow == "True":
 funcs.print_cutflows(
         backgrounds = plot_backgrounds,
         signal      = plot_signals,
         data        = data,
         region      = options.region,
         histname    = os.path.join(hdict[options.vname+"_"+options.region]['dir'],hdict[options.vname+"_"+options.region]['hname']),
         sys_dict    = None,
         outname     = plotsfile
         )

 ## EOF



