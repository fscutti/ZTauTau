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
#lumi =  3193.68 #2015
lumi = 7980 #2016

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
mc_backgrounds.append(samples.top)

## signals
mc_signals = []
mc_signals.append(samples.Zttjets)

# This is the sum of all addons
fakes = samples.fakes.copy()

sub_ztt = samples.sub_ztt.copy()
sub_ztt.tlatex = "Ztt (subtraction)"
sub_ztt_25med = samples.sub_ztt_25med.copy()
sub_ztt_25med.tlatex = "Ztt_25med (subtraction)"
sub_ztt_35med = samples.sub_ztt_35med.copy()
sub_ztt_35med.tlatex = "Ztt_35med (subtraction)"

sub_ztt_1Track = samples.sub_ztt_1Track.copy()
sub_ztt_1Track.tlatex = "Ztt_1Track (subtraction)"
sub_ztt_25med_1Track = samples.sub_ztt_25med_1Track.copy()
sub_ztt_25med_1Track.tlatex = "Ztt_25med_1Track (subtraction)"
sub_ztt_35med_1Track = samples.sub_ztt_35med_1Track.copy()
sub_ztt_35med_1Track.tlatex = "Ztt_35med_1Track (subtraction)"

sub_ztt_3Track = samples.sub_ztt_3Track.copy()
sub_ztt_3Track.tlatex = "Ztt_3Track (subtraction)"
sub_ztt_25med_3Track = samples.sub_ztt_25med_3Track.copy()
sub_ztt_25med_3Track.tlatex = "Ztt_25med_3Track (subtraction)"
sub_ztt_35med_3Track = samples.sub_ztt_35med_3Track.copy()
sub_ztt_35med_3Track.tlatex = "Ztt_35med_3Track (subtraction)"

# These are the components

#-----------------------------------
# BOTH TRACKS
#-----------------------------------

addon_data    = samples.addon_data.copy()
addon_Wjets   = samples.addon_Wjets.copy()
addon_Zlljets = samples.addon_Zlljets.copy()
addon_top     = samples.addon_top.copy()

addon_data_lowPT    = samples.addon_data_lowPT.copy()
addon_Wjets_lowPT   = samples.addon_Wjets_lowPT.copy()
addon_Zlljets_lowPT = samples.addon_Zlljets_lowPT.copy()
addon_top_lowPT     = samples.addon_top_lowPT.copy()

addon_data_highPT     = samples.addon_data_highPT.copy()
addon_Wjets_highPT   = samples.addon_Wjets_highPT.copy()
addon_Zlljets_highPT = samples.addon_Zlljets_highPT.copy()
addon_top_highPT     = samples.addon_top_highPT.copy()

addon_data_25med    = samples.addon_data_25med.copy()
addon_Wjets_25med   = samples.addon_Wjets_25med.copy()
addon_Zlljets_25med = samples.addon_Zlljets_25med.copy()
addon_top_25med     = samples.addon_top_25med.copy()

addon_data_25med_lowPT    = samples.addon_data_25med_lowPT.copy()
addon_Wjets_25med_lowPT   = samples.addon_Wjets_25med_lowPT.copy()
addon_Zlljets_25med_lowPT = samples.addon_Zlljets_25med_lowPT.copy()
addon_top_25med_lowPT     = samples.addon_top_25med_lowPT.copy()

addon_data_25med_highPT    = samples.addon_data_25med_highPT.copy()
addon_Wjets_25med_highPT   = samples.addon_Wjets_25med_highPT.copy()
addon_Zlljets_25med_highPT = samples.addon_Zlljets_25med_highPT.copy()
addon_top_25med_highPT     = samples.addon_top_25med_highPT.copy()

addon_data_35med    = samples.addon_data_25med.copy()
addon_Wjets_35med   = samples.addon_Wjets_25med.copy()
addon_Zlljets_35med = samples.addon_Zlljets_25med.copy()
addon_top_35med     = samples.addon_top_25med.copy()

addon_data_35med_lowPT    = samples.addon_data_35med_lowPT.copy()
addon_Wjets_35med_lowPT   = samples.addon_Wjets_35med_lowPT.copy()
addon_Zlljets_35med_lowPT = samples.addon_Zlljets_35med_lowPT.copy()
addon_top_35med_lowPT     = samples.addon_top_35med_lowPT.copy()

addon_data_35med_highPT    = samples.addon_data_35med_highPT.copy()
addon_Wjets_35med_highPT   = samples.addon_Wjets_35med_highPT.copy()
addon_Zlljets_35med_highPT = samples.addon_Zlljets_35med_highPT.copy()
addon_top_35med_highPT     = samples.addon_top_35med_highPT.copy()


#-----------------------------------
# ONE TRACK
#-----------------------------------

addon_data_1Track    = samples.addon_data_1Track.copy()
addon_Wjets_1Track   = samples.addon_Wjets_1Track.copy()
addon_Zlljets_1Track = samples.addon_Zlljets_1Track.copy()
addon_top_1Track     = samples.addon_top_1Track.copy()

addon_data_lowPT_1Track    = samples.addon_data_lowPT_1Track.copy()
addon_Wjets_lowPT_1Track   = samples.addon_Wjets_lowPT_1Track.copy()
addon_Zlljets_lowPT_1Track = samples.addon_Zlljets_lowPT_1Track.copy()
addon_top_lowPT_1Track     = samples.addon_top_lowPT_1Track.copy()

addon_data_highPT_1Track     = samples.addon_data_highPT_1Track.copy()
addon_Wjets_highPT_1Track   = samples.addon_Wjets_highPT_1Track.copy()
addon_Zlljets_highPT_1Track = samples.addon_Zlljets_highPT_1Track.copy()
addon_top_highPT_1Track     = samples.addon_top_highPT_1Track.copy()

addon_data_25med_1Track    = samples.addon_data_25med_1Track.copy()
addon_Wjets_25med_1Track   = samples.addon_Wjets_25med_1Track.copy()
addon_Zlljets_25med_1Track = samples.addon_Zlljets_25med_1Track.copy()
addon_top_25med_1Track     = samples.addon_top_25med_1Track.copy()

addon_data_25med_lowPT_1Track    = samples.addon_data_25med_lowPT_1Track.copy()
addon_Wjets_25med_lowPT_1Track   = samples.addon_Wjets_25med_lowPT_1Track.copy()
addon_Zlljets_25med_lowPT_1Track = samples.addon_Zlljets_25med_lowPT_1Track.copy()
addon_top_25med_lowPT_1Track     = samples.addon_top_25med_lowPT_1Track.copy()

addon_data_25med_highPT_1Track    = samples.addon_data_25med_highPT_1Track.copy()
addon_Wjets_25med_highPT_1Track   = samples.addon_Wjets_25med_highPT_1Track.copy()
addon_Zlljets_25med_highPT_1Track = samples.addon_Zlljets_25med_highPT_1Track.copy()
addon_top_25med_highPT_1Track     = samples.addon_top_25med_highPT_1Track.copy()

addon_data_35med_1Track    = samples.addon_data_35med_1Track.copy()
addon_Wjets_35med_1Track   = samples.addon_Wjets_35med_1Track.copy()
addon_Zlljets_35med_1Track = samples.addon_Zlljets_35med_1Track.copy()
addon_top_35med_1Track     = samples.addon_top_35med_1Track.copy()

addon_data_35med_lowPT_1Track    = samples.addon_data_35med_lowPT_1Track.copy()
addon_Wjets_35med_lowPT_1Track   = samples.addon_Wjets_35med_lowPT_1Track.copy()
addon_Zlljets_35med_lowPT_1Track = samples.addon_Zlljets_35med_lowPT_1Track.copy()
addon_top_35med_lowPT_1Track     = samples.addon_top_35med_lowPT_1Track.copy()

addon_data_35med_highPT_1Track    = samples.addon_data_35med_highPT_1Track.copy()
addon_Wjets_35med_highPT_1Track   = samples.addon_Wjets_35med_highPT_1Track.copy()
addon_Zlljets_35med_highPT_1Track = samples.addon_Zlljets_35med_highPT_1Track.copy()
addon_top_35med_highPT_1Track     = samples.addon_top_35med_highPT_1Track.copy()


#-----------------------------------
# THREE TRACKS
#-----------------------------------

addon_data_3Track    = samples.addon_data_3Track.copy()
addon_Wjets_3Track   = samples.addon_Wjets_3Track.copy()
addon_Zlljets_3Track = samples.addon_Zlljets_3Track.copy()
addon_top_3Track     = samples.addon_top_3Track.copy()

addon_data_lowPT_3Track    = samples.addon_data_lowPT_3Track.copy()
addon_Wjets_lowPT_3Track   = samples.addon_Wjets_lowPT_3Track.copy()
addon_Zlljets_lowPT_3Track = samples.addon_Zlljets_lowPT_3Track.copy()
addon_top_lowPT_3Track     = samples.addon_top_lowPT_3Track.copy()

addon_data_highPT_3Track     = samples.addon_data_highPT_3Track.copy()
addon_Wjets_highPT_3Track   = samples.addon_Wjets_highPT_3Track.copy()
addon_Zlljets_highPT_3Track = samples.addon_Zlljets_highPT_3Track.copy()
addon_top_highPT_3Track     = samples.addon_top_highPT_3Track.copy()

addon_data_25med_3Track    = samples.addon_data_25med_3Track.copy()
addon_Wjets_25med_3Track   = samples.addon_Wjets_25med_3Track.copy()
addon_Zlljets_25med_3Track = samples.addon_Zlljets_25med_3Track.copy()
addon_top_25med_3Track     = samples.addon_top_25med_3Track.copy()

addon_data_25med_lowPT_3Track    = samples.addon_data_25med_lowPT_3Track.copy()
addon_Wjets_25med_lowPT_3Track   = samples.addon_Wjets_25med_lowPT_3Track.copy()
addon_Zlljets_25med_lowPT_3Track = samples.addon_Zlljets_25med_lowPT_3Track.copy()
addon_top_25med_lowPT_3Track     = samples.addon_top_25med_lowPT_3Track.copy()

addon_data_25med_highPT_3Track    = samples.addon_data_25med_highPT_3Track.copy()
addon_Wjets_25med_highPT_3Track   = samples.addon_Wjets_25med_highPT_3Track.copy()
addon_Zlljets_25med_highPT_3Track = samples.addon_Zlljets_25med_highPT_3Track.copy()
addon_top_25med_highPT_3Track     = samples.addon_top_25med_highPT_3Track.copy()

addon_data_35med_3Track    = samples.addon_data_35med_3Track.copy()
addon_Wjets_35med_3Track   = samples.addon_Wjets_35med_3Track.copy()
addon_Zlljets_35med_3Track = samples.addon_Zlljets_35med_3Track.copy()
addon_top_35med_3Track     = samples.addon_top_35med_3Track.copy()

addon_data_35med_lowPT_3Track    = samples.addon_data_35med_lowPT_3Track.copy()
addon_Wjets_35med_lowPT_3Track   = samples.addon_Wjets_35med_lowPT_3Track.copy()
addon_Zlljets_35med_lowPT_3Track = samples.addon_Zlljets_35med_lowPT_3Track.copy()
addon_top_35med_lowPT_3Track     = samples.addon_top_35med_lowPT_3Track.copy()

addon_data_35med_highPT_3Track    = samples.addon_data_35med_highPT_3Track.copy()
addon_Wjets_35med_highPT_3Track   = samples.addon_Wjets_35med_highPT_3Track.copy()
addon_Zlljets_35med_highPT_3Track = samples.addon_Zlljets_35med_highPT_3Track.copy()
addon_top_35med_highPT_3Track     = samples.addon_top_35med_highPT_3Track.copy()



#-----------------------------
#-----------------------------

addon_backgrounds_lowPT = []
addon_backgrounds_lowPT.append(addon_data_lowPT)
addon_backgrounds_lowPT.append(addon_Wjets_lowPT)
addon_backgrounds_lowPT.append(addon_Zlljets_lowPT)
addon_backgrounds_lowPT.append(addon_top_lowPT)

addon_backgrounds_highPT = []
addon_backgrounds_highPT.append(addon_data_highPT)
addon_backgrounds_highPT.append(addon_Wjets_highPT)
addon_backgrounds_highPT.append(addon_Zlljets_highPT)
addon_backgrounds_highPT.append(addon_top_highPT)

addon_backgrounds = []
addon_backgrounds.append(addon_data)
addon_backgrounds.append(addon_Wjets)
addon_backgrounds.append(addon_Zlljets)
addon_backgrounds.append(addon_top)

addon_backgrounds_25med = []
addon_backgrounds_25med.append(addon_data_25med)
addon_backgrounds_25med.append(addon_Wjets_25med)
addon_backgrounds_25med.append(addon_Zlljets_25med)
addon_backgrounds_25med.append(addon_top_25med)

addon_backgrounds_25med_lowPT = []
addon_backgrounds_25med_lowPT.append(addon_data_25med_lowPT)
addon_backgrounds_25med_lowPT.append(addon_Wjets_25med_lowPT)
addon_backgrounds_25med_lowPT.append(addon_Zlljets_25med_lowPT)
addon_backgrounds_25med_lowPT.append(addon_top_25med_lowPT)

addon_backgrounds_25med_highPT = []
addon_backgrounds_25med_highPT.append(addon_data_25med_highPT)
addon_backgrounds_25med_highPT.append(addon_Wjets_25med_highPT)
addon_backgrounds_25med_highPT.append(addon_Zlljets_25med_highPT)
addon_backgrounds_25med_highPT.append(addon_top_25med_highPT)

addon_backgrounds_35med = []
addon_backgrounds_35med.append(addon_data_35med)
addon_backgrounds_35med.append(addon_Wjets_35med)
addon_backgrounds_35med.append(addon_Zlljets_35med)
addon_backgrounds_35med.append(addon_top_35med)

addon_backgrounds_35med_lowPT = []
addon_backgrounds_35med_lowPT.append(addon_data_35med_lowPT)
addon_backgrounds_35med_lowPT.append(addon_Wjets_35med_lowPT)
addon_backgrounds_35med_lowPT.append(addon_Zlljets_35med_lowPT)
addon_backgrounds_35med_lowPT.append(addon_top_35med_lowPT)

addon_backgrounds_35med_highPT = []
addon_backgrounds_35med_highPT.append(addon_data_35med_highPT)
addon_backgrounds_35med_highPT.append(addon_Wjets_35med_highPT)
addon_backgrounds_35med_highPT.append(addon_Zlljets_35med_highPT)
addon_backgrounds_35med_highPT.append(addon_top_35med_highPT)


#--------------------------
# one track
#--------------------------

addon_backgrounds_lowPT_1Track = []
addon_backgrounds_lowPT_1Track.append(addon_data_lowPT_1Track)
addon_backgrounds_lowPT_1Track.append(addon_Wjets_lowPT_1Track)
addon_backgrounds_lowPT_1Track.append(addon_Zlljets_lowPT_1Track)
addon_backgrounds_lowPT_1Track.append(addon_top_lowPT_1Track)

addon_backgrounds_highPT_1Track = []
addon_backgrounds_highPT_1Track.append(addon_data_highPT_1Track)
addon_backgrounds_highPT_1Track.append(addon_Wjets_highPT_1Track)
addon_backgrounds_highPT_1Track.append(addon_Zlljets_highPT_1Track)
addon_backgrounds_highPT_1Track.append(addon_top_highPT_1Track)

addon_backgrounds_1Track = []
addon_backgrounds_1Track.append(addon_data_1Track)
addon_backgrounds_1Track.append(addon_Wjets_1Track)
addon_backgrounds_1Track.append(addon_Zlljets_1Track)
addon_backgrounds_1Track.append(addon_top_1Track)

addon_backgrounds_25med_1Track = []
addon_backgrounds_25med_1Track.append(addon_data_25med_1Track)
addon_backgrounds_25med_1Track.append(addon_Wjets_25med_1Track)
addon_backgrounds_25med_1Track.append(addon_Zlljets_25med_1Track)
addon_backgrounds_25med_1Track.append(addon_top_25med_1Track)

addon_backgrounds_25med_lowPT_1Track = []
addon_backgrounds_25med_lowPT_1Track.append(addon_data_25med_lowPT_1Track)
addon_backgrounds_25med_lowPT_1Track.append(addon_Wjets_25med_lowPT_1Track)
addon_backgrounds_25med_lowPT_1Track.append(addon_Zlljets_25med_lowPT_1Track)
addon_backgrounds_25med_lowPT_1Track.append(addon_top_25med_lowPT_1Track)

addon_backgrounds_25med_highPT_1Track = []
addon_backgrounds_25med_highPT_1Track.append(addon_data_25med_highPT_1Track)
addon_backgrounds_25med_highPT_1Track.append(addon_Wjets_25med_highPT_1Track)
addon_backgrounds_25med_highPT_1Track.append(addon_Zlljets_25med_highPT_1Track)
addon_backgrounds_25med_highPT_1Track.append(addon_top_25med_highPT_1Track)

addon_backgrounds_35med_1Track = []
addon_backgrounds_35med_1Track.append(addon_data_35med_1Track)
addon_backgrounds_35med_1Track.append(addon_Wjets_35med_1Track)
addon_backgrounds_35med_1Track.append(addon_Zlljets_35med_1Track)
addon_backgrounds_35med_1Track.append(addon_top_35med_1Track)

addon_backgrounds_35med_lowPT_1Track = []
addon_backgrounds_35med_lowPT_1Track.append(addon_data_35med_lowPT_1Track)
addon_backgrounds_35med_lowPT_1Track.append(addon_Wjets_35med_lowPT_1Track)
addon_backgrounds_35med_lowPT_1Track.append(addon_Zlljets_35med_lowPT_1Track)
addon_backgrounds_35med_lowPT_1Track.append(addon_top_35med_lowPT_1Track)

addon_backgrounds_35med_highPT_1Track = []
addon_backgrounds_35med_highPT_1Track.append(addon_data_35med_highPT_1Track)
addon_backgrounds_35med_highPT_1Track.append(addon_Wjets_35med_highPT_1Track)
addon_backgrounds_35med_highPT_1Track.append(addon_Zlljets_35med_highPT_1Track)
addon_backgrounds_35med_highPT_1Track.append(addon_top_35med_highPT_1Track)

#--------------------------
# three tracks
#--------------------------

addon_backgrounds_lowPT_3Track = []
addon_backgrounds_lowPT_3Track.append(addon_data_lowPT_3Track)
addon_backgrounds_lowPT_3Track.append(addon_Wjets_lowPT_3Track)
addon_backgrounds_lowPT_3Track.append(addon_Zlljets_lowPT_3Track)
addon_backgrounds_lowPT_3Track.append(addon_top_lowPT_3Track)

addon_backgrounds_highPT_3Track = []
addon_backgrounds_highPT_3Track.append(addon_data_highPT_3Track)
addon_backgrounds_highPT_3Track.append(addon_Wjets_highPT_3Track)
addon_backgrounds_highPT_3Track.append(addon_Zlljets_highPT_3Track)
addon_backgrounds_highPT_3Track.append(addon_top_highPT_3Track)

addon_backgrounds_3Track = []
addon_backgrounds_3Track.append(addon_data_3Track)
addon_backgrounds_3Track.append(addon_Wjets_3Track)
addon_backgrounds_3Track.append(addon_Zlljets_3Track)
addon_backgrounds_3Track.append(addon_top_3Track)

addon_backgrounds_25med_3Track = []
addon_backgrounds_25med_3Track.append(addon_data_25med_3Track)
addon_backgrounds_25med_3Track.append(addon_Wjets_25med_3Track)
addon_backgrounds_25med_3Track.append(addon_Zlljets_25med_3Track)
addon_backgrounds_25med_3Track.append(addon_top_25med_3Track)

addon_backgrounds_25med_lowPT_3Track = []
addon_backgrounds_25med_lowPT_3Track.append(addon_data_25med_lowPT_3Track)
addon_backgrounds_25med_lowPT_3Track.append(addon_Wjets_25med_lowPT_3Track)
addon_backgrounds_25med_lowPT_3Track.append(addon_Zlljets_25med_lowPT_3Track)
addon_backgrounds_25med_lowPT_3Track.append(addon_top_25med_lowPT_3Track)

addon_backgrounds_25med_highPT_3Track = []
addon_backgrounds_25med_highPT_3Track.append(addon_data_25med_highPT_3Track)
addon_backgrounds_25med_highPT_3Track.append(addon_Wjets_25med_highPT_3Track)
addon_backgrounds_25med_highPT_3Track.append(addon_Zlljets_25med_highPT_3Track)
addon_backgrounds_25med_highPT_3Track.append(addon_top_25med_highPT_3Track)

addon_backgrounds_35med_3Track = []
addon_backgrounds_35med_3Track.append(addon_data_35med_3Track)
addon_backgrounds_35med_3Track.append(addon_Wjets_35med_3Track)
addon_backgrounds_35med_3Track.append(addon_Zlljets_35med_3Track)
addon_backgrounds_35med_3Track.append(addon_top_35med_3Track)

addon_backgrounds_35med_lowPT_3Track = []
addon_backgrounds_35med_lowPT_3Track.append(addon_data_35med_lowPT_3Track)
addon_backgrounds_35med_lowPT_3Track.append(addon_Wjets_35med_lowPT_3Track)
addon_backgrounds_35med_lowPT_3Track.append(addon_Zlljets_35med_lowPT_3Track)
addon_backgrounds_35med_lowPT_3Track.append(addon_top_35med_lowPT_3Track)

addon_backgrounds_35med_highPT_3Track = []
addon_backgrounds_35med_highPT_3Track.append(addon_data_35med_highPT_3Track)
addon_backgrounds_35med_highPT_3Track.append(addon_Wjets_35med_highPT_3Track)
addon_backgrounds_35med_highPT_3Track.append(addon_Zlljets_35med_highPT_3Track)
addon_backgrounds_35med_highPT_3Track.append(addon_top_35med_highPT_3Track)

#---------------------------
# Regions for bkg estimation
#---------------------------

# k-factors

kf_regions = {}
kf_regions_highPT = {}
kf_regions_lowPT = {}

kf_regions_25med = {}
kf_regions_25med_lowPT = {}
kf_regions_25med_highPT = {}

kf_regions_35med = {}
kf_regions_35med_lowPT = {}
kf_regions_35med_highPT = {}

kf_regions[samples.Wjets]	= {"OS":"Wjets_OS", "SS":"Wjets_SS","ncuts":3}
kf_regions_25med[samples.Wjets]	= {"OS":"Wjets_OS_25med", "SS":"Wjets_SS_25med","ncuts":4}
kf_regions_35med[samples.Wjets]	= {"OS":"Wjets_OS_35med", "SS":"Wjets_SS_35med","ncuts":4}

kf_regions_25med_lowPT[samples.Wjets]	= {"OS":"Wjets_OS_25med_lowPT", "SS":"Wjets_SS_25med_lowPT","ncuts":5}
kf_regions_25med_highPT[samples.Wjets]	= {"OS":"Wjets_OS_25med_highPT", "SS":"Wjets_SS_25med_highPT","ncuts":5}
kf_regions_35med_lowPT[samples.Wjets]	= {"OS":"Wjets_OS_35med_lowPT", "SS":"Wjets_SS_35med_lowPT","ncuts":5}
kf_regions_35med_highPT[samples.Wjets]	= {"OS":"Wjets_OS_35med_highPT", "SS":"Wjets_SS_35med_highPT","ncuts":5}

kf_regions_highPT[samples.Wjets]  = {"OS":"Wjets_OS_highPT", "SS":"Wjets_SS_highPT", "ncuts":4}
kf_regions_lowPT[samples.Wjets]   = {"OS":"Wjets_OS_lowPT", "SS":"Wjets_SS_lowPT", "ncuts":4}

#-----------
# one track
#-----------

kf_regions_1Track = {}
kf_regions_highPT_1Track = {}
kf_regions_lowPT_1Track = {}

kf_regions_25med_1Track = {}
kf_regions_25med_lowPT_1Track = {}
kf_regions_25med_highPT_1Track = {}
kf_regions_35med_1Track = {}
kf_regions_35med_lowPT_1Track = {}
kf_regions_35med_highPT_1Track = {}

kf_regions_1Track[samples.Wjets]	= {"OS":"Wjets_OS_Tau1Track", "SS":"Wjets_SS_Tau1Track","ncuts":4}
kf_regions_25med_1Track[samples.Wjets]	= {"OS":"Wjets_OS_25med_Tau1Track", "SS":"Wjets_SS_25med_Tau1Track","ncuts":5}
kf_regions_35med_1Track[samples.Wjets]	= {"OS":"Wjets_OS_35med_Tau1Track", "SS":"Wjets_SS_35med_Tau1Track","ncuts":5}

kf_regions_25med_lowPT_1Track[samples.Wjets]	= {"OS":"Wjets_OS_25med_lowPT_Tau1Track", "SS":"Wjets_SS_25med_lowPT_Tau1Track","ncuts":6}
kf_regions_25med_highPT_1Track[samples.Wjets]	= {"OS":"Wjets_OS_25med_highPT_Tau1Track", "SS":"Wjets_SS_25med_highPT_Tau1Track","ncuts":6}
kf_regions_35med_lowPT_1Track[samples.Wjets]	= {"OS":"Wjets_OS_35med_lowPT_Tau1Track", "SS":"Wjets_SS_35med_lowPT_Tau1Track","ncuts":6}
kf_regions_35med_highPT_1Track[samples.Wjets]	= {"OS":"Wjets_OS_35med_highPT_Tau1Track", "SS":"Wjets_SS_35med_highPT_Tau1Track","ncuts":6}

kf_regions_highPT_1Track[samples.Wjets]  = {"OS":"Wjets_OS_highPT_Tau1Track", "SS":"Wjets_SS_highPT_Tau1Track", "ncuts":5}
kf_regions_lowPT_1Track[samples.Wjets]   = {"OS":"Wjets_OS_lowPT_Tau1Track", "SS":"Wjets_SS_lowPT_Tau1Track", "ncuts":5}

#------------
# three tracks
#------------

kf_regions_3Track = {}
kf_regions_highPT_3Track = {}
kf_regions_lowPT_3Track = {}

kf_regions_25med_3Track = {}
kf_regions_25med_lowPT_3Track = {}
kf_regions_25med_highPT_3Track = {}
kf_regions_35med_3Track = {}
kf_regions_35med_lowPT_3Track = {}
kf_regions_35med_highPT_3Track = {}

kf_regions_3Track[samples.Wjets]	= {"OS":"Wjets_OS_Tau3Track", "SS":"Wjets_SS_Tau3Track","ncuts":4}
kf_regions_25med_3Track[samples.Wjets]	= {"OS":"Wjets_OS_25med_Tau3Track", "SS":"Wjets_SS_25med_Tau3Track","ncuts":5}
kf_regions_35med_3Track[samples.Wjets]	= {"OS":"Wjets_OS_35med_Tau3Track", "SS":"Wjets_SS_35med_Tau3Track","ncuts":5}

kf_regions_25med_lowPT_3Track[samples.Wjets]	= {"OS":"Wjets_OS_25med_lowPT_Tau3Track", "SS":"Wjets_SS_25med_lowPT_Tau3Track","ncuts":6}
kf_regions_25med_highPT_3Track[samples.Wjets]	= {"OS":"Wjets_OS_25med_highPT_Tau3Track", "SS":"Wjets_SS_25med_highPT_Tau3Track","ncuts":6}
kf_regions_35med_lowPT_3Track[samples.Wjets]	= {"OS":"Wjets_OS_35med_lowPT_Tau3Track", "SS":"Wjets_SS_35med_lowPT_Tau3Track","ncuts":6}
kf_regions_35med_highPT_3Track[samples.Wjets]	= {"OS":"Wjets_OS_35med_highPT_Tau3Track", "SS":"Wjets_SS_35med_highPT_Tau3Track","ncuts":6}

kf_regions_highPT_3Track[samples.Wjets]  = {"OS":"Wjets_OS_highPT_Tau3Track", "SS":"Wjets_SS_highPT_Tau3Track", "ncuts":5}
kf_regions_lowPT_3Track[samples.Wjets]   = {"OS":"Wjets_OS_lowPT_Tau3Track", "SS":"Wjets_SS_lowPT_Tau3Track", "ncuts":5}

#kf_regions[samples.Wjets]   = {"OS":"Wjets_OS", "SS":"Wjets_SS", "ncuts":3}
#kkf_regions[samples.top]     = {"OS":"","SS":"","ncuts"}
#kf_regions[samples.Zlljets] = {"OS":"","SS":"","ncuts"}

###############################################
     
# Rqcd
rqcd_regions_lowPT = {}
rqcd_regions_highPT = {}
rqcd_regions = {}

rqcd_regions_25med = {}
rqcd_regions_25med_lowPT = {}
rqcd_regions_25med_highPT = {}
rqcd_regions_35med = {}
rqcd_regions_35med_lowPT = {}
rqcd_regions_35med_highPT = {}

rqcd_regions_highPT[data]  = {"num":"AntiIsoCR_OS_highPT", "den":"AntiIsoCR_SS_highPT", "ncuts":3}
rqcd_regions_lowPT[data] = {"num":"AntiIsoCR_OS_lowPT", "den":"AntiIsoCR_SS_lowPT", "ncuts":3}
rqcd_regions[data] 	= {"num":"AntiIsoCR_OS","den":"AntiIsoCR_SS","ncuts":2}

rqcd_regions_25med[data]  = {"num":"AntiIsoCR_OS_25med", "den":"AntiIsoCR_SS_25med", "ncuts":3}
rqcd_regions_25med_lowPT[data]  = {"num":"AntiIsoCR_OS_25med_lowPT", "den":"AntiIsoCR_SS_25med_lowPT", "ncuts":4}
rqcd_regions_25med_highPT[data]  = {"num":"AntiIsoCR_OS_25med_highPT", "den":"AntiIsoCR_SS_25med_highPT", "ncuts":4}
rqcd_regions_35med[data]  = {"num":"AntiIsoCR_OS_35med", "den":"AntiIsoCR_SS_35med", "ncuts":3}
rqcd_regions_35med_lowPT[data]  = {"num":"AntiIsoCR_OS_35med_lowPT", "den":"AntiIsoCR_SS_35med_lowPT", "ncuts":4}
rqcd_regions_35med_highPT[data]  = {"num":"AntiIsoCR_OS_35med_highPT", "den":"AntiIsoCR_SS_35med_highPT", "ncuts":4}


#-------------
# one track
#-------------

rqcd_regions_lowPT_1Track = {}
rqcd_regions_highPT_1Track = {}
rqcd_regions_1Track = {}

rqcd_regions_25med_1Track = {}
rqcd_regions_25med_lowPT_1Track = {}
rqcd_regions_25med_highPT_1Track = {}
rqcd_regions_35med_1Track = {}
rqcd_regions_35med_lowPT_1Track = {}
rqcd_regions_35med_highPT_1Track = {}

rqcd_regions_highPT_1Track[data]  = {"num":"AntiIsoCR_OS_highPT_Tau1Track", "den":"AntiIsoCR_SS_highPT_Tau1Track", "ncuts":4}
rqcd_regions_lowPT_1Track[data] = {"num":"AntiIsoCR_OS_lowPT_Tau1Track", "den":"AntiIsoCR_SS_lowPT_Tau1Track", "ncuts":4}
rqcd_regions_1Track[data] 	= {"num":"AntiIsoCR_OS_Tau1Track","den":"AntiIsoCR_SS_Tau1Track","ncuts":3}

rqcd_regions_25med_1Track[data]  = {"num":"AntiIsoCR_OS_25med_Tau1Track", "den":"AntiIsoCR_SS_25med_Tau1Track", "ncuts":4}
rqcd_regions_25med_lowPT_1Track[data]  = {"num":"AntiIsoCR_OS_25med_lowPT_Tau1Track", "den":"AntiIsoCR_SS_25med_lowPT_Tau1Track", "ncuts":5}
rqcd_regions_25med_highPT_1Track[data]  = {"num":"AntiIsoCR_OS_25med_highPT_Tau1Track", "den":"AntiIsoCR_SS_25med_highPT_Tau1Track", "ncuts":5}
rqcd_regions_35med_1Track[data]  = {"num":"AntiIsoCR_OS_35med_Tau1Track", "den":"AntiIsoCR_SS_35med_Tau1Track", "ncuts":4}
rqcd_regions_35med_lowPT_1Track[data]  = {"num":"AntiIsoCR_OS_35med_lowPT_Tau1Track", "den":"AntiIsoCR_SS_35med_lowPT_Tau1Track", "ncuts":5}
rqcd_regions_35med_highPT_1Track[data]  = {"num":"AntiIsoCR_OS_35med_highPT_Tau1Track", "den":"AntiIsoCR_SS_35med_highPT_Tau1Track", "ncuts":5}

#--------------
# three tracks
#--------------

rqcd_regions_lowPT_3Track = {}
rqcd_regions_highPT_3Track = {}
rqcd_regions_3Track = {}

rqcd_regions_25med_3Track = {}
rqcd_regions_25med_lowPT_3Track = {}
rqcd_regions_25med_highPT_3Track = {}
rqcd_regions_35med_3Track = {}
rqcd_regions_35med_lowPT_3Track = {}
rqcd_regions_35med_highPT_3Track = {}

rqcd_regions_highPT_3Track[data]  = {"num":"AntiIsoCR_OS_highPT_Tau3Track", "den":"AntiIsoCR_SS_highPT_Tau3Track", "ncuts":4}
rqcd_regions_lowPT_3Track[data] = {"num":"AntiIsoCR_OS_lowPT_Tau3Track", "den":"AntiIsoCR_SS_lowPT_Tau3Track", "ncuts":4}
rqcd_regions_3Track[data] 	= {"num":"AntiIsoCR_OS_Tau3Track","den":"AntiIsoCR_SS_Tau3Track","ncuts":3}

rqcd_regions_25med_3Track[data]  = {"num":"AntiIsoCR_OS_25med_Tau3Track", "den":"AntiIsoCR_SS_25med_Tau3Track", "ncuts":4}
rqcd_regions_25med_lowPT_3Track[data]  = {"num":"AntiIsoCR_OS_25med_lowPT_Tau3Track", "den":"AntiIsoCR_SS_25med_lowPT_Tau3Track", "ncuts":5}
rqcd_regions_25med_highPT_3Track[data]  = {"num":"AntiIsoCR_OS_25med_highPT_Tau3Track", "den":"AntiIsoCR_SS_25med_highPT_Tau3Track", "ncuts":5}
rqcd_regions_35med_3Track[data]  = {"num":"AntiIsoCR_OS_35med_Tau3Track", "den":"AntiIsoCR_SS_35med_Tau3Track", "ncuts":4}
rqcd_regions_35med_lowPT_3Track[data]  = {"num":"AntiIsoCR_OS_35med_lowPT_Tau3Track", "den":"AntiIsoCR_SS_35med_lowPT_Tau3Track", "ncuts":5}
rqcd_regions_35med_highPT_3Track[data]  = {"num":"AntiIsoCR_OS_35med_highPT_Tau3Track", "den":"AntiIsoCR_SS_35med_highPT_Tau3Track", "ncuts":5}
  
################################################### 
# Add-On

addon_regions = {}
addon_regions[data]            = {"SS":"SR_SS", "ncuts":4} # don't really need OS for data do you?
addon_regions[samples.Wjets]   = {"OS":"SR", "SS":"SR_SS", "ncuts":4}
addon_regions[samples.Zlljets] = {"OS":"SR", "SS":"SR_SS", "ncuts":4}
addon_regions[samples.top]     = {"OS":"SR", "SS":"SR_SS", "ncuts":4}

addon_regions_25med = {}
addon_regions_25med[data]            = {"SS":"SR_SS_25med", "ncuts":5} # don't really need OS for data do you?
addon_regions_25med[samples.Wjets]   = {"OS":"SR_25med", "SS":"SR_SS_25med", "ncuts":5}
addon_regions_25med[samples.Zlljets] = {"OS":"SR_25med", "SS":"SR_SS_25med", "ncuts":5}
addon_regions_25med[samples.top]     = {"OS":"SR_25med", "SS":"SR_SS_25med", "ncuts":5}

addon_regions_35med = {}
addon_regions_35med[data]            = {"SS":"SR_SS_35med", "ncuts":5} # don't really need OS for data do you?
addon_regions_35med[samples.Wjets]   = {"OS":"SR_35med", "SS":"SR_SS_35med", "ncuts":5}
addon_regions_35med[samples.Zlljets] = {"OS":"SR_35med", "SS":"SR_SS_35med", "ncuts":5}
addon_regions_35med[samples.top]     = {"OS":"SR_35med", "SS":"SR_SS_35med", "ncuts":5}

addon_regions_highPT = {}
addon_regions_highPT[data]            = {"SS":"SR_SS_highPT", "ncuts":5} # don't really need OS for data do you?
addon_regions_highPT[samples.Wjets]   = {"OS":"SR_highPT", "SS":"SR_SS_highPT", "ncuts":5}
addon_regions_highPT[samples.Zlljets] = {"OS":"SR_highPT", "SS":"SR_SS_highPT", "ncuts":5}
addon_regions_highPT[samples.top]     = {"OS":"SR_highPT", "SS":"SR_SS_highPT", "ncuts":5}

addon_regions_lowPT = {}
addon_regions_lowPT[data]            = {"SS":"SR_SS_lowPT", "ncuts":5} # don't really need OS for data do you?
addon_regions_lowPT[samples.Wjets]   = {"OS":"SR_lowPT", "SS":"SR_SS_lowPT", "ncuts":5}
addon_regions_lowPT[samples.Zlljets] = {"OS":"SR_lowPT", "SS":"SR_SS_lowPT", "ncuts":5}
addon_regions_lowPT[samples.top]     = {"OS":"SR_lowPT", "SS":"SR_SS_lowPT", "ncuts":5}

addon_regions_25med_lowPT = {}
addon_regions_25med_lowPT[data]            = {"SS":"SR_SS_25med_lowPT", "ncuts":6} # don't really need OS for data do you?
addon_regions_25med_lowPT[samples.Wjets]   = {"OS":"SR_25med_lowPT", "SS":"SR_SS_25med_lowPT", "ncuts":6}
addon_regions_25med_lowPT[samples.Zlljets] = {"OS":"SR_25med_lowPT", "SS":"SR_SS_25med_lowPT", "ncuts":6}
addon_regions_25med_lowPT[samples.top]     = {"OS":"SR_25med_lowPT", "SS":"SR_SS_25med_lowPT", "ncuts":6}

addon_regions_25med_highPT = {}
addon_regions_25med_highPT[data]            = {"SS":"SR_SS_25med_highPT", "ncuts":6} # don't really need OS for data do you?
addon_regions_25med_highPT[samples.Wjets]   = {"OS":"SR_25med_highPT", "SS":"SR_SS_25med_highPT", "ncuts":6}
addon_regions_25med_highPT[samples.Zlljets] = {"OS":"SR_25med_highPT", "SS":"SR_SS_25med_highPT", "ncuts":6}
addon_regions_25med_highPT[samples.top]     = {"OS":"SR_25med_highPT", "SS":"SR_SS_25med_highPT", "ncuts":6}

addon_regions_35med_lowPT = {}
addon_regions_35med_lowPT[data]            = {"SS":"SR_SS_35med_lowPT", "ncuts":6} # don't really need OS for data do you?
addon_regions_35med_lowPT[samples.Wjets]   = {"OS":"SR_35med_lowPT", "SS":"SR_SS_35med_lowPT", "ncuts":6}
addon_regions_35med_lowPT[samples.Zlljets] = {"OS":"SR_35med_lowPT", "SS":"SR_SS_35med_lowPT", "ncuts":6}
addon_regions_35med_lowPT[samples.top]     = {"OS":"SR_35med_lowPT", "SS":"SR_SS_35med_lowPT", "ncuts":6}

addon_regions_35med_highPT = {}
addon_regions_35med_highPT[data]            = {"SS":"SR_SS_35med_highPT", "ncuts":6} # don't really need OS for data do you?
addon_regions_35med_highPT[samples.Wjets]   = {"OS":"SR_35med_highPT", "SS":"SR_SS_35med_highPT", "ncuts":6}
addon_regions_35med_highPT[samples.Zlljets] = {"OS":"SR_35med_highPT", "SS":"SR_SS_35med_highPT", "ncuts":6}
addon_regions_35med_highPT[samples.top]     = {"OS":"SR_35med_highPT", "SS":"SR_SS_35med_highPT", "ncuts":6}

#--------------------
# one track
#--------------------

addon_regions_1Track = {}
addon_regions_1Track[data]            = {"SS":"SR_SS_Tau1Track", "ncuts":5} # don't really need OS for data do you?
addon_regions_1Track[samples.Wjets]   = {"OS":"SR_Tau1Track", "SS":"SR_SS_Tau1Track", "ncuts":5}
addon_regions_1Track[samples.Zlljets] = {"OS":"SR_Tau1Track", "SS":"SR_SS_Tau1Track", "ncuts":5}
addon_regions_1Track[samples.top]     = {"OS":"SR_Tau1Track", "SS":"SR_SS_Tau1Track", "ncuts":5}

addon_regions_25med_1Track = {}
addon_regions_25med_1Track[data]            = {"SS":"SR_SS_25med_Tau1Track", "ncuts":6} # don't really need OS for data do you?
addon_regions_25med_1Track[samples.Wjets]   = {"OS":"SR_25med_Tau1Track", "SS":"SR_SS_25med_Tau1Track", "ncuts":6}
addon_regions_25med_1Track[samples.Zlljets] = {"OS":"SR_25med_Tau1Track", "SS":"SR_SS_25med_Tau1Track", "ncuts":6}
addon_regions_25med_1Track[samples.top]     = {"OS":"SR_25med_Tau1Track", "SS":"SR_SS_25med_Tau1Track", "ncuts":6}

addon_regions_35med_1Track = {}
addon_regions_35med_1Track[data]            = {"SS":"SR_SS_35med_Tau1Track", "ncuts":6} # don't really need OS for data do you?
addon_regions_35med_1Track[samples.Wjets]   = {"OS":"SR_35med_Tau1Track", "SS":"SR_SS_35med_Tau1Track", "ncuts":6}
addon_regions_35med_1Track[samples.Zlljets] = {"OS":"SR_35med_Tau1Track", "SS":"SR_SS_35med_Tau1Track", "ncuts":6}
addon_regions_35med_1Track[samples.top]     = {"OS":"SR_35med_Tau1Track", "SS":"SR_SS_35med_Tau1Track", "ncuts":6}

addon_regions_highPT_1Track = {}
addon_regions_highPT_1Track[data]            = {"SS":"SR_SS_highPT_Tau1Track", "ncuts":6} # don't really need OS for data do you?
addon_regions_highPT_1Track[samples.Wjets]   = {"OS":"SR_highPT_Tau1Track", "SS":"SR_SS_highPT_Tau1Track", "ncuts":6}
addon_regions_highPT_1Track[samples.Zlljets] = {"OS":"SR_highPT_Tau1Track", "SS":"SR_SS_highPT_Tau1Track", "ncuts":6}
addon_regions_highPT_1Track[samples.top]     = {"OS":"SR_highPT_Tau1Track", "SS":"SR_SS_highPT_Tau1Track", "ncuts":6}

addon_regions_lowPT_1Track = {}
addon_regions_lowPT_1Track[data]            = {"SS":"SR_SS_lowPT_Tau1Track", "ncuts":6} # don't really need OS for data do you?
addon_regions_lowPT_1Track[samples.Wjets]   = {"OS":"SR_lowPT_Tau1Track", "SS":"SR_SS_lowPT_Tau1Track", "ncuts":6}
addon_regions_lowPT_1Track[samples.Zlljets] = {"OS":"SR_lowPT_Tau1Track", "SS":"SR_SS_lowPT_Tau1Track", "ncuts":6}
addon_regions_lowPT_1Track[samples.top]     = {"OS":"SR_lowPT_Tau1Track", "SS":"SR_SS_lowPT_Tau1Track", "ncuts":6}

addon_regions_25med_lowPT_1Track = {}
addon_regions_25med_lowPT_1Track[data]            = {"SS":"SR_SS_25med_lowPT_Tau1Track", "ncuts":7} # don't really need OS for data do you?
addon_regions_25med_lowPT_1Track[samples.Wjets]   = {"OS":"SR_25med_lowPT_Tau1Track", "SS":"SR_SS_25med_lowPT_Tau1Track", "ncuts":7}
addon_regions_25med_lowPT_1Track[samples.Zlljets] = {"OS":"SR_25med_lowPT_Tau1Track", "SS":"SR_SS_25med_lowPT_Tau1Track", "ncuts":7}
addon_regions_25med_lowPT_1Track[samples.top]     = {"OS":"SR_25med_lowPT_Tau1Track", "SS":"SR_SS_25med_lowPT_Tau1Track", "ncuts":7}

addon_regions_25med_highPT_1Track = {}
addon_regions_25med_highPT_1Track[data]            = {"SS":"SR_SS_25med_highPT_Tau1Track", "ncuts":7} # don't really need OS for data do you?
addon_regions_25med_highPT_1Track[samples.Wjets]   = {"OS":"SR_25med_highPT_Tau1Track", "SS":"SR_SS_25med_highPT_Tau1Track", "ncuts":7}
addon_regions_25med_highPT_1Track[samples.Zlljets] = {"OS":"SR_25med_highPT_Tau1Track", "SS":"SR_SS_25med_highPT_Tau1Track", "ncuts":7}
addon_regions_25med_highPT_1Track[samples.top]     = {"OS":"SR_25med_highPT_Tau1Track", "SS":"SR_SS_25med_highPT_Tau1Track", "ncuts":7}

addon_regions_35med_lowPT_1Track = {}
addon_regions_35med_lowPT_1Track[data]            = {"SS":"SR_SS_35med_lowPT_Tau1Track", "ncuts":7} # don't really need OS for data do you?
addon_regions_35med_lowPT_1Track[samples.Wjets]   = {"OS":"SR_35med_lowPT_Tau1Track", "SS":"SR_SS_35med_lowPT_Tau1Track", "ncuts":7}
addon_regions_35med_lowPT_1Track[samples.Zlljets] = {"OS":"SR_35med_lowPT_Tau1Track", "SS":"SR_SS_35med_lowPT_Tau1Track", "ncuts":7}
addon_regions_35med_lowPT_1Track[samples.top]     = {"OS":"SR_35med_lowPT_Tau1Track", "SS":"SR_SS_35med_lowPT_Tau1Track", "ncuts":7}

addon_regions_35med_highPT_1Track = {}
addon_regions_35med_highPT_1Track[data]            = {"SS":"SR_SS_35med_highPT_Tau1Track", "ncuts":7} # don't really need OS for data do you?
addon_regions_35med_highPT_1Track[samples.Wjets]   = {"OS":"SR_35med_highPT_Tau1Track", "SS":"SR_SS_35med_highPT_Tau1Track", "ncuts":7}
addon_regions_35med_highPT_1Track[samples.Zlljets] = {"OS":"SR_35med_highPT_Tau1Track", "SS":"SR_SS_35med_highPT_Tau1Track", "ncuts":7}
addon_regions_35med_highPT_1Track[samples.top]     = {"OS":"SR_35med_highPT_Tau1Track", "SS":"SR_SS_35med_highPT_Tau1Track", "ncuts":7}

#--------------------
# three tracks
#--------------------

addon_regions_3Track = {}
addon_regions_3Track[data]            = {"SS":"SR_SS_Tau3Track", "ncuts":5} # don't really need OS for data do you?
addon_regions_3Track[samples.Wjets]   = {"OS":"SR_Tau3Track", "SS":"SR_SS_Tau3Track", "ncuts":5}
addon_regions_3Track[samples.Zlljets] = {"OS":"SR_Tau3Track", "SS":"SR_SS_Tau3Track", "ncuts":5}
addon_regions_3Track[samples.top]     = {"OS":"SR_Tau3Track", "SS":"SR_SS_Tau3Track", "ncuts":5}

addon_regions_25med_3Track = {}
addon_regions_25med_3Track[data]            = {"SS":"SR_SS_25med_Tau3Track", "ncuts":6} # don't really need OS for data do you?
addon_regions_25med_3Track[samples.Wjets]   = {"OS":"SR_25med_Tau3Track", "SS":"SR_SS_25med_Tau3Track", "ncuts":6}
addon_regions_25med_3Track[samples.Zlljets] = {"OS":"SR_25med_Tau3Track", "SS":"SR_SS_25med_Tau3Track", "ncuts":6}
addon_regions_25med_3Track[samples.top]     = {"OS":"SR_25med_Tau3Track", "SS":"SR_SS_25med_Tau3Track", "ncuts":6}

addon_regions_35med_3Track = {}
addon_regions_35med_3Track[data]            = {"SS":"SR_SS_35med_Tau3Track", "ncuts":6} # don't really need OS for data do you?
addon_regions_35med_3Track[samples.Wjets]   = {"OS":"SR_35med_Tau3Track", "SS":"SR_SS_35med_Tau3Track", "ncuts":6}
addon_regions_35med_3Track[samples.Zlljets] = {"OS":"SR_35med_Tau3Track", "SS":"SR_SS_35med_Tau3Track", "ncuts":6}
addon_regions_35med_3Track[samples.top]     = {"OS":"SR_35med_Tau3Track", "SS":"SR_SS_35med_Tau3Track", "ncuts":6}

addon_regions_highPT_3Track = {}
addon_regions_highPT_3Track[data]            = {"SS":"SR_SS_highPT_Tau3Track", "ncuts":6} # don't really need OS for data do you?
addon_regions_highPT_3Track[samples.Wjets]   = {"OS":"SR_highPT_Tau3Track", "SS":"SR_SS_highPT_Tau3Track", "ncuts":6}
addon_regions_highPT_3Track[samples.Zlljets] = {"OS":"SR_highPT_Tau3Track", "SS":"SR_SS_highPT_Tau3Track", "ncuts":6}
addon_regions_highPT_3Track[samples.top]     = {"OS":"SR_highPT_Tau3Track", "SS":"SR_SS_highPT_Tau3Track", "ncuts":6}

addon_regions_lowPT_3Track = {}
addon_regions_lowPT_3Track[data]            = {"SS":"SR_SS_lowPT_Tau3Track", "ncuts":6} # don't really need OS for data do you?
addon_regions_lowPT_3Track[samples.Wjets]   = {"OS":"SR_lowPT_Tau3Track", "SS":"SR_SS_lowPT_Tau3Track", "ncuts":6}
addon_regions_lowPT_3Track[samples.Zlljets] = {"OS":"SR_lowPT_Tau3Track", "SS":"SR_SS_lowPT_Tau3Track", "ncuts":6}
addon_regions_lowPT_3Track[samples.top]     = {"OS":"SR_lowPT_Tau3Track", "SS":"SR_SS_lowPT_Tau3Track", "ncuts":6}

addon_regions_25med_lowPT_3Track = {}
addon_regions_25med_lowPT_3Track[data]            = {"SS":"SR_SS_25med_lowPT_Tau3Track", "ncuts":7} # don't really need OS for data do you?
addon_regions_25med_lowPT_3Track[samples.Wjets]   = {"OS":"SR_25med_lowPT_Tau3Track", "SS":"SR_SS_25med_lowPT_Tau3Track", "ncuts":7}
addon_regions_25med_lowPT_3Track[samples.Zlljets] = {"OS":"SR_25med_lowPT_Tau3Track", "SS":"SR_SS_25med_lowPT_Tau3Track", "ncuts":7}
addon_regions_25med_lowPT_3Track[samples.top]     = {"OS":"SR_25med_lowPT_Tau3Track", "SS":"SR_SS_25med_lowPT_Tau3Track", "ncuts":7}

addon_regions_25med_highPT_3Track = {}
addon_regions_25med_highPT_3Track[data]            = {"SS":"SR_SS_25med_highPT_Tau3Track", "ncuts":7} # don't really need OS for data do you?
addon_regions_25med_highPT_3Track[samples.Wjets]   = {"OS":"SR_25med_highPT_Tau3Track", "SS":"SR_SS_25med_highPT_Tau3Track", "ncuts":7}
addon_regions_25med_highPT_3Track[samples.Zlljets] = {"OS":"SR_25med_highPT_Tau3Track", "SS":"SR_SS_25med_highPT_Tau3Track", "ncuts":7}
addon_regions_25med_highPT_3Track[samples.top]     = {"OS":"SR_25med_highPT_Tau3Track", "SS":"SR_SS_25med_highPT_Tau3Track", "ncuts":7}

addon_regions_35med_lowPT_3Track = {}
addon_regions_35med_lowPT_3Track[data]            = {"SS":"SR_SS_35med_lowPT_Tau3Track", "ncuts":7} # don't really need OS for data do you?
addon_regions_35med_lowPT_3Track[samples.Wjets]   = {"OS":"SR_35med_lowPT_Tau3Track", "SS":"SR_SS_35med_lowPT_Tau3Track", "ncuts":7}
addon_regions_35med_lowPT_3Track[samples.Zlljets] = {"OS":"SR_35med_lowPT_Tau3Track", "SS":"SR_SS_35med_lowPT_Tau3Track", "ncuts":7}
addon_regions_35med_lowPT_3Track[samples.top]     = {"OS":"SR_35med_lowPT_Tau3Track", "SS":"SR_SS_35med_lowPT_Tau3Track", "ncuts":7}

addon_regions_35med_highPT_3Track = {}
addon_regions_35med_highPT_3Track[data]            = {"SS":"SR_SS_35med_highPT_Tau3Track", "ncuts":7} # don't really need OS for data do you?
addon_regions_35med_highPT_3Track[samples.Wjets]   = {"OS":"SR_35med_highPT_Tau3Track", "SS":"SR_SS_35med_highPT_Tau3Track", "ncuts":7}
addon_regions_35med_highPT_3Track[samples.Zlljets] = {"OS":"SR_35med_highPT_Tau3Track", "SS":"SR_SS_35med_highPT_Tau3Track", "ncuts":7}
addon_regions_35med_highPT_3Track[samples.top]     = {"OS":"SR_35med_highPT_Tau3Track", "SS":"SR_SS_35med_highPT_Tau3Track", "ncuts":7}

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
#----------------------------------------------
# PT BINNING
#----------------------------------------------

for b in addon_backgrounds_lowPT:
 b.estimator = histmgr.AddOnEstimator(
       hm            = hm,
       sample        = b,
       data_sample   = data,
       mc_samples    = mc_backgrounds + mc_signals,
       rqcd_regions  = rqcd_regions_lowPT,
       kf_regions    = kf_regions_lowPT,
       addon_regions = addon_regions_lowPT,
       print_info    = True,
       )

for b in addon_backgrounds_highPT:
 b.estimator = histmgr.AddOnEstimator(
       hm            = hm,
       sample        = b,
       data_sample   = data,
       mc_samples    = mc_backgrounds + mc_signals,
       rqcd_regions  = rqcd_regions_highPT,
       kf_regions    = kf_regions_highPT,
       addon_regions = addon_regions_highPT,
       print_info    = True,
       )

for b in addon_backgrounds_25med_lowPT:
 b.estimator = histmgr.AddOnEstimator(
       hm            = hm,
       sample        = b,
       data_sample   = data,
       mc_samples    = mc_backgrounds + mc_signals,
       rqcd_regions  = rqcd_regions_25med_lowPT,
       kf_regions    = kf_regions_25med_lowPT,
       addon_regions = addon_regions_25med_lowPT,
       print_info    = True,
       )

for b in addon_backgrounds_25med_highPT:
 b.estimator = histmgr.AddOnEstimator(
       hm            = hm,
       sample        = b,
       data_sample   = data,
       mc_samples    = mc_backgrounds + mc_signals,
       rqcd_regions  = rqcd_regions_25med_highPT,
       kf_regions    = kf_regions_25med_highPT,
       addon_regions = addon_regions_25med_highPT,
       print_info    = True,
       )

for b in addon_backgrounds_35med_lowPT:
 b.estimator = histmgr.AddOnEstimator(
       hm            = hm,
       sample        = b,
       data_sample   = data,
       mc_samples    = mc_backgrounds + mc_signals,
       rqcd_regions  = rqcd_regions_35med_lowPT,
       kf_regions    = kf_regions_35med_lowPT,
       addon_regions = addon_regions_35med_lowPT,
       print_info    = True,
       )

for b in addon_backgrounds_35med_highPT:
 b.estimator = histmgr.AddOnEstimator(
       hm            = hm,
       sample        = b,
       data_sample   = data,
       mc_samples    = mc_backgrounds + mc_signals,
       rqcd_regions  = rqcd_regions_35med_highPT,
       kf_regions    = kf_regions_35med_highPT,
       addon_regions = addon_regions_35med_highPT,
       print_info    = True,
       )

#--------------------
# one track
#--------------------

for b in addon_backgrounds_lowPT_1Track:
 b.estimator = histmgr.AddOnEstimator(
       hm            = hm,
       sample        = b,
       data_sample   = data,
       mc_samples    = mc_backgrounds + mc_signals,
       rqcd_regions  = rqcd_regions_lowPT_1Track,
       kf_regions    = kf_regions_lowPT_1Track,
       addon_regions = addon_regions_lowPT_1Track,
       print_info    = True,
       )

for b in addon_backgrounds_highPT_1Track:
 b.estimator = histmgr.AddOnEstimator(
       hm            = hm,
       sample        = b,
       data_sample   = data,
       mc_samples    = mc_backgrounds + mc_signals,
       rqcd_regions  = rqcd_regions_highPT_1Track,
       kf_regions    = kf_regions_highPT_1Track,
       addon_regions = addon_regions_highPT_1Track,
       print_info    = True,
       )

for b in addon_backgrounds_25med_lowPT_1Track:
 b.estimator = histmgr.AddOnEstimator(
       hm            = hm,
       sample        = b,
       data_sample   = data,
       mc_samples    = mc_backgrounds + mc_signals,
       rqcd_regions  = rqcd_regions_25med_lowPT_1Track,
       kf_regions    = kf_regions_25med_lowPT_1Track,
       addon_regions = addon_regions_25med_lowPT_1Track,
       print_info    = True,
       )

for b in addon_backgrounds_25med_highPT_1Track:
 b.estimator = histmgr.AddOnEstimator(
       hm            = hm,
       sample        = b,
       data_sample   = data,
       mc_samples    = mc_backgrounds + mc_signals,
       rqcd_regions  = rqcd_regions_25med_highPT_1Track,
       kf_regions    = kf_regions_25med_highPT_1Track,
       addon_regions = addon_regions_25med_highPT_1Track,
       print_info    = True,
       )

for b in addon_backgrounds_35med_lowPT_1Track:
 b.estimator = histmgr.AddOnEstimator(
       hm            = hm,
       sample        = b,
       data_sample   = data,
       mc_samples    = mc_backgrounds + mc_signals,
       rqcd_regions  = rqcd_regions_35med_lowPT_1Track,
       kf_regions    = kf_regions_35med_lowPT_1Track,
       addon_regions = addon_regions_35med_lowPT_1Track,
       print_info    = True,
       )

for b in addon_backgrounds_35med_highPT_1Track:
 b.estimator = histmgr.AddOnEstimator(
       hm            = hm,
       sample        = b,
       data_sample   = data,
       mc_samples    = mc_backgrounds + mc_signals,
       rqcd_regions  = rqcd_regions_35med_highPT_1Track,
       kf_regions    = kf_regions_35med_highPT_1Track,
       addon_regions = addon_regions_35med_highPT_1Track,
       print_info    = True,
       )

#----------------
# three tracks
#---------------

for b in addon_backgrounds_lowPT_3Track:
 b.estimator = histmgr.AddOnEstimator(
       hm            = hm,
       sample        = b,
       data_sample   = data,
       mc_samples    = mc_backgrounds + mc_signals,
       rqcd_regions  = rqcd_regions_lowPT_3Track,
       kf_regions    = kf_regions_lowPT_3Track,
       addon_regions = addon_regions_lowPT_3Track,
       print_info    = True,
       )

for b in addon_backgrounds_highPT_3Track:
 b.estimator = histmgr.AddOnEstimator(
       hm            = hm,
       sample        = b,
       data_sample   = data,
       mc_samples    = mc_backgrounds + mc_signals,
       rqcd_regions  = rqcd_regions_highPT_3Track,
       kf_regions    = kf_regions_highPT_3Track,
       addon_regions = addon_regions_highPT_3Track,
       print_info    = True,
       )

for b in addon_backgrounds_25med_lowPT_3Track:
 b.estimator = histmgr.AddOnEstimator(
       hm            = hm,
       sample        = b,
       data_sample   = data,
       mc_samples    = mc_backgrounds + mc_signals,
       rqcd_regions  = rqcd_regions_25med_lowPT_3Track,
       kf_regions    = kf_regions_25med_lowPT_3Track,
       addon_regions = addon_regions_25med_lowPT_3Track,
       print_info    = True,
       )

for b in addon_backgrounds_25med_highPT_3Track:
 b.estimator = histmgr.AddOnEstimator(
       hm            = hm,
       sample        = b,
       data_sample   = data,
       mc_samples    = mc_backgrounds + mc_signals,
       rqcd_regions  = rqcd_regions_25med_highPT_3Track,
       kf_regions    = kf_regions_25med_highPT_3Track,
       addon_regions = addon_regions_25med_highPT_3Track,
       print_info    = True,
       )

for b in addon_backgrounds_35med_lowPT_3Track:
 b.estimator = histmgr.AddOnEstimator(
       hm            = hm,
       sample        = b,
       data_sample   = data,
       mc_samples    = mc_backgrounds + mc_signals,
       rqcd_regions  = rqcd_regions_35med_lowPT_3Track,
       kf_regions    = kf_regions_35med_lowPT_3Track,
       addon_regions = addon_regions_35med_lowPT_3Track,
       print_info    = True,
       )

for b in addon_backgrounds_35med_highPT_3Track:
 b.estimator = histmgr.AddOnEstimator(
       hm            = hm,
       sample        = b,
       data_sample   = data,
       mc_samples    = mc_backgrounds + mc_signals,
       rqcd_regions  = rqcd_regions_35med_highPT_3Track,
       kf_regions    = kf_regions_35med_highPT_3Track,
       addon_regions = addon_regions_35med_highPT_3Track,
       print_info    = True,
       )

"""
#-----------------------------
# NO PT BINNING
#-----------------------------

for b in addon_backgrounds:
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

for b in addon_backgrounds_25med:
 b.estimator = histmgr.AddOnEstimator(
       hm            = hm,
       sample        = b,
       data_sample   = data,
       mc_samples    = mc_backgrounds + mc_signals,
       rqcd_regions  = rqcd_regions_25med,
       kf_regions    = kf_regions_25med,
       addon_regions = addon_regions_25med,
       print_info    = True,
       )

for b in addon_backgrounds_35med:
 b.estimator = histmgr.AddOnEstimator(
       hm            = hm,
       sample        = b,
       data_sample   = data,
       mc_samples    = mc_backgrounds + mc_signals,
       rqcd_regions  = rqcd_regions_35med,
       kf_regions    = kf_regions_35med,
       addon_regions = addon_regions_35med,
       print_info    = True,
       )

for b in addon_backgrounds_1Track:
 b.estimator = histmgr.AddOnEstimator(
       hm            = hm,
       sample        = b,
       data_sample   = data,
       mc_samples    = mc_backgrounds + mc_signals,
       rqcd_regions  = rqcd_regions_1Track,
       kf_regions    = kf_regions_1Track,
       addon_regions = addon_regions_1Track,
       print_info    = True,
       )

for b in addon_backgrounds_25med_1Track:
 b.estimator = histmgr.AddOnEstimator(
       hm            = hm,
       sample        = b,
       data_sample   = data,
       mc_samples    = mc_backgrounds + mc_signals,
       rqcd_regions  = rqcd_regions_25med_1Track,
       kf_regions    = kf_regions_25med_1Track,
       addon_regions = addon_regions_25med_1Track,
       print_info    = True,
       )

for b in addon_backgrounds_35med_1Track:
 b.estimator = histmgr.AddOnEstimator(
       hm            = hm,
       sample        = b,
       data_sample   = data,
       mc_samples    = mc_backgrounds + mc_signals,
       rqcd_regions  = rqcd_regions_35med_1Track,
       kf_regions    = kf_regions_35med_1Track,
       addon_regions = addon_regions_35med_1Track,
       print_info    = True,
       )

for b in addon_backgrounds_3Track:
 b.estimator = histmgr.AddOnEstimator(
       hm            = hm,
       sample        = b,
       data_sample   = data,
       mc_samples    = mc_backgrounds + mc_signals,
       rqcd_regions  = rqcd_regions_3Track,
       kf_regions    = kf_regions_3Track,
       addon_regions = addon_regions_3Track,
       print_info    = True,
       )

for b in addon_backgrounds_25med_3Track:
 b.estimator = histmgr.AddOnEstimator(
       hm            = hm,
       sample        = b,
       data_sample   = data,
       mc_samples    = mc_backgrounds + mc_signals,
       rqcd_regions  = rqcd_regions_25med_3Track,
       kf_regions    = kf_regions_25med_3Track,
       addon_regions = addon_regions_25med_3Track,
       print_info    = True,
       )

for b in addon_backgrounds_35med_3Track:
 b.estimator = histmgr.AddOnEstimator(
       hm            = hm,
       sample        = b,
       data_sample   = data,
       mc_samples    = mc_backgrounds + mc_signals,
       rqcd_regions  = rqcd_regions_35med_3Track,
       kf_regions    = kf_regions_35med_3Track,
       addon_regions = addon_regions_35med_3Track,
       print_info    = True,
       )

"""
#----------------------
# MERGE
#----------------------

for i in range(len(addon_backgrounds)):
 m = addon_backgrounds[i]
 m.estimator = histmgr.MergeEstimator(
	hm = hm,
	sample = m,
        samples = [addon_backgrounds_lowPT[i],addon_backgrounds_highPT[i]]
 	)

for i in range(len(addon_backgrounds_25med)):
 m = addon_backgrounds_25med[i]
 m.estimator = histmgr.MergeEstimator(
	hm = hm,
	sample = m,
        samples = [addon_backgrounds_25med_lowPT[i],addon_backgrounds_25med_highPT[i]]
 	)

for i in range(len(addon_backgrounds_35med)):
 m = addon_backgrounds_35med[i]
 m.estimator = histmgr.MergeEstimator(
	hm = hm,
	sample = m,
        samples = [addon_backgrounds_35med_lowPT[i],addon_backgrounds_35med_highPT[i]]
 	)

for i in range(len(addon_backgrounds_1Track)):
 m = addon_backgrounds_1Track[i]
 m.estimator = histmgr.MergeEstimator(
	hm = hm,
	sample = m,
        samples = [addon_backgrounds_lowPT_1Track[i],addon_backgrounds_highPT_1Track[i]]
 	)

for i in range(len(addon_backgrounds_25med_1Track)):
 m = addon_backgrounds_25med_1Track[i]
 m.estimator = histmgr.MergeEstimator(
	hm = hm,
	sample = m,
        samples = [addon_backgrounds_25med_lowPT_1Track[i],addon_backgrounds_25med_highPT_1Track[i]]
 	)

for i in range(len(addon_backgrounds_35med_1Track)):
 m = addon_backgrounds_35med_1Track[i]
 m.estimator = histmgr.MergeEstimator(
	hm = hm,
	sample = m,
        samples = [addon_backgrounds_35med_lowPT_1Track[i],addon_backgrounds_35med_highPT_1Track[i]]
 	)

for i in range(len(addon_backgrounds_3Track)):
 m = addon_backgrounds_3Track[i]
 m.estimator = histmgr.MergeEstimator(
	hm = hm,
	sample = m,
        samples = [addon_backgrounds_lowPT_3Track[i],addon_backgrounds_highPT_3Track[i]]
 	)

for i in range(len(addon_backgrounds_25med_3Track)):
 m = addon_backgrounds_25med_3Track[i]
 m.estimator = histmgr.MergeEstimator(
	hm = hm,
	sample = m,
        samples = [addon_backgrounds_25med_lowPT_3Track[i],addon_backgrounds_25med_highPT_3Track[i]]
 	)

for i in range(len(addon_backgrounds_35med_3Track)):
 m = addon_backgrounds_35med_3Track[i]
 m.estimator = histmgr.MergeEstimator(
	hm = hm,
	sample = m,
        samples = [addon_backgrounds_35med_lowPT_3Track[i],addon_backgrounds_35med_highPT_3Track[i]]
 	)

#############################

sub_ztt.estimator = histmgr.DataBkgSubEstimator(
	hm = hm,
	sample = sub_ztt,
	data_sample = data,
	mc_samples = addon_backgrounds,
	mc_samples_rescales = None,
	) 

sub_ztt_25med.estimator = histmgr.DataBkgSubEstimator(
	hm = hm,
	sample = sub_ztt_25med,
	data_sample = data,
	mc_samples = addon_backgrounds_25med,
	mc_samples_rescales = None,
	) 

sub_ztt_35med.estimator = histmgr.DataBkgSubEstimator(
	hm = hm,
	sample = sub_ztt_35med,
	data_sample = data,
	mc_samples = addon_backgrounds_35med,
	mc_samples_rescales = None,
	) 

sub_ztt_1Track.estimator = histmgr.DataBkgSubEstimator(
	hm = hm,
	sample = sub_ztt_1Track,
	data_sample = data,
	mc_samples = addon_backgrounds_1Track,
	mc_samples_rescales = None,
	) 

sub_ztt_25med_1Track.estimator = histmgr.DataBkgSubEstimator(
	hm = hm,
	sample = sub_ztt_25med_1Track,
	data_sample = data,
	mc_samples = addon_backgrounds_25med_1Track,
	mc_samples_rescales = None,
	) 

sub_ztt_35med_1Track.estimator = histmgr.DataBkgSubEstimator(
	hm = hm,
	sample = sub_ztt_35med_1Track,
	data_sample = data,
	mc_samples = addon_backgrounds_35med_1Track,
	mc_samples_rescales = None,
	) 

sub_ztt_3Track.estimator = histmgr.DataBkgSubEstimator(
	hm = hm,
	sample = sub_ztt_3Track,
	data_sample = data,
	mc_samples = addon_backgrounds_3Track,
	mc_samples_rescales = None,
	) 

sub_ztt_25med_3Track.estimator = histmgr.DataBkgSubEstimator(
	hm = hm,
	sample = sub_ztt_25med_3Track,
	data_sample = data,
	mc_samples = addon_backgrounds_25med_3Track,
	mc_samples_rescales = None,
	) 

sub_ztt_35med_3Track.estimator = histmgr.DataBkgSubEstimator(
	hm = hm,
	sample = sub_ztt_35med_3Track,
	data_sample = data,
	mc_samples = addon_backgrounds_35med_3Track,
	mc_samples_rescales = None,
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
plot_signals = []

if "SR" == options.region: #add-ons only make sense in the signal region

	print "signal region"

	plot_backgrounds.append(addon_data)
	plot_backgrounds.append(addon_Wjets)
	plot_backgrounds.append(addon_Zlljets)
	plot_backgrounds.append(addon_top)

        plot_signals.append(samples.Zttjets)
        #plot_signals.append(sub_ztt) 


elif "SR_25med" == options.region:
 
	print "signal region _25med"

	plot_backgrounds.append(addon_data_25med)
	plot_backgrounds.append(addon_Wjets_25med)
	plot_backgrounds.append(addon_Zlljets_25med)
	plot_backgrounds.append(addon_top_25med)

        plot_signals.append(samples.Zttjets)
        #plot_signals.append(sub_ztt_25med) #remember to comment addon_backgrounds ztt

elif "SR_35med" == options.region:
 
	print "signal region _35med"

	plot_backgrounds.append(addon_data_35med)
	plot_backgrounds.append(addon_Wjets_35med)
	plot_backgrounds.append(addon_Zlljets_35med)
	plot_backgrounds.append(addon_top_35med)

        plot_signals.append(samples.Zttjets)
        #plot_signals.append(sub_ztt_35med) #remember to comment addon_backgrounds ztt

elif "SR_Tau1Track" == options.region: #add-ons only make sense in the signal region

	print "signal region 1 prong"

	plot_backgrounds.append(addon_data_1Track)
	plot_backgrounds.append(addon_Wjets_1Track)
	plot_backgrounds.append(addon_Zlljets_1Track)
	plot_backgrounds.append(addon_top_1Track)

        plot_signals.append(samples.Zttjets)
        #plot_signals.append(sub_ztt_1Track) 
	
elif "SR_25med_Tau1Track" == options.region:
 
	print "signal region _25med 1 prong"

	plot_backgrounds.append(addon_data_25med_1Track)
	plot_backgrounds.append(addon_Wjets_25med_1Track)
	plot_backgrounds.append(addon_Zlljets_25med_1Track)
	plot_backgrounds.append(addon_top_25med_1Track)

        #plot_signals.append(samples.Zttjets)
        plot_signals.append(sub_ztt_25med_1Track) #remember to comment addon_backgrounds ztt

elif "SR_35med_Tau1Track" == options.region:
 
	print "signal region _35med 1 prong"

	plot_backgrounds.append(addon_data_35med_1Track)
	plot_backgrounds.append(addon_Wjets_35med_1Track)
	plot_backgrounds.append(addon_Zlljets_35med_1Track)
	plot_backgrounds.append(addon_top_35med_1Track)

        plot_signals.append(samples.Zttjets)
        #plot_signals.append(sub_ztt_35med_1Track) #remember to comment addon_backgrounds ztt

elif "SR_Tau3Track" == options.region: #add-ons only make sense in the signal region

	print "signal region 3 prong"

	plot_backgrounds.append(addon_data_3Track)
	plot_backgrounds.append(addon_Wjets_3Track)
	plot_backgrounds.append(addon_Zlljets_3Track)
	plot_backgrounds.append(addon_top_3Track)

        #plot_signals.append(samples.Zttjets)
        plot_signals.append(sub_ztt_3Track) 
	
elif "SR_25med_Tau3Track" == options.region:
 
	print "signal region _25med 3 prong"

	plot_backgrounds.append(addon_data_25med_3Track)
	plot_backgrounds.append(addon_Wjets_25med_3Track)
	plot_backgrounds.append(addon_Zlljets_25med_3Track)
	plot_backgrounds.append(addon_top_25med_3Track)

        #plot_signals.append(samples.Zttjets)
        plot_signals.append(sub_ztt_25med_3Track) #remember to comment addon_backgrounds ztt
		
elif "SR_35med_Tau3Track" == options.region:
 
	print "signal region _35med 3 prong"

	plot_backgrounds.append(addon_data_35med_3Track)
	plot_backgrounds.append(addon_Wjets_35med_3Track)
	plot_backgrounds.append(addon_Zlljets_35med_3Track)
	plot_backgrounds.append(addon_top_35med_3Track)

        plot_signals.append(samples.Zttjets)
        #plot_signals.append(sub_ztt_35med_3Track) #remember to comment addon_backgrounds ztt
	
else: #MC as background
	plot_signals.append(samples.Zttjets)
        plot_backgrounds.append(samples.Wjets)
        plot_backgrounds.append(samples.Zlljets)
        plot_backgrounds.append(samples.top)


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
 print "Writing a nice hist for you.."
 funcs.write_hist(
#	backgrounds = mc_backgrounds,
	backgrounds = plot_backgrounds,
	signal 	    = plot_signals,
#	signal      = mc_signals, # This can be a list
        data        = data,
        region      = options.region,
        icut        = int(options.icut),
        histname    = os.path.join(vdict[options.vname]['path'],vdict[options.vname]['hname']),
        #rebin       = vdict[options.vname]['rebin'],
        sys_dict    = None,
        outname     = plotsfile
        )	

## EOF



