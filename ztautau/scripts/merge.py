## modules
import ROOT

import histmgr
import funcs
import os

from ztautau.samples import samples
from ztautau.plots   import vars
from systematics     import *

from optparse import OptionParser

ptbinning_y_or_n = "y"
#ptbinning_y_or_n = "n"

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
parser.add_option('-t', '--toposys', dest='toposys',
                  help='topo rqcd sys',metavar='TOPOSYS',default=None)
parser.add_option('-s', '--sysptvar', dest='sysptvar',
                  help='ptvar rqcd sys',metavar='SYSPTVAR',default=None)
parser.add_option('-k', '--kwsys', dest='kwsys',
		  help='kwsys', metavar='KWSYS',default=None)

(options, args) = parser.parse_args()

#-----------------
# Configuration
#-----------------
#lumi =  3193.68 #2015 v12
#lumi = 3212.72 #2015 v19
#lumi = 9966.815 #2016 v17

#lumi = 11473.88 #2016 v19
lumi = 24799 #2016 v22

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


trax = [1,3]
triggers = [25,35,"50L1TAU12", 80, "80L1TAU60", 125, 160]#, "L1TAU12IMmed"]

#-----------------
# Samples        
#-----------------

## data
data = samples.data
print len(data.daughters)

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

sub_ztt_1Track = samples.sub_ztt_1Track.copy()
sub_ztt_1Track.tlatex = "Ztt_1Track (subtraction)"

sub_ztt_3Track = samples.sub_ztt_3Track.copy()
sub_ztt_3Track.tlatex = "Ztt_3Track (subtraction)"

# Triggers

sub_ztt_25med = samples.sub_ztt_25med.copy()
sub_ztt_25med.tlatex = "Ztt_25med (subtraction)"
sub_ztt_35med = samples.sub_ztt_35med.copy()
sub_ztt_35med.tlatex = "Ztt_35med (subtraction)"
sub_ztt_50L1TAU12med = samples.sub_ztt_50L1TAU12med.copy()
sub_ztt_50L1TAU12med.tlatex = "Ztt_50L1TAU12med (subtraction)"
sub_ztt_80med = samples.sub_ztt_80med.copy()
sub_ztt_80med.tlatex = "Ztt_80med (subtraction)"
sub_ztt_80L1TAU60med = samples.sub_ztt_80L1TAU60med.copy()
sub_ztt_80L1TAU60med.tlatex = "Ztt_80L1TAU60med (subtraction)"
sub_ztt_125med = samples.sub_ztt_125med.copy()
sub_ztt_125med.tlatex = "Ztt_125med (subtraction)"
sub_ztt_160med = samples.sub_ztt_160med.copy()
sub_ztt_160med.tlatex = "Ztt_160med (subtraction)"
sub_ztt_L1TAU12IMmed = samples.sub_ztt_L1TAU12IMmed.copy()
sub_ztt_L1TAU12IMmed.tlatex = "Ztt_L1TAU12IMmed (subtraction)"


sub_ztt_ptonly = samples.sub_ztt_ptonly.copy()
sub_ztt_ptonly.tlatex = "Ztt_ptonly (subtraction)"
sub_ztt_tracktwo = samples.sub_ztt_tracktwo.copy()
sub_ztt_tracktwo.tlatex = "Ztt_tracktwo (subtraction)"

sub_ztt_25med_1Track = samples.sub_ztt_25med_1Track.copy()
sub_ztt_25med_1Track.tlatex = "Ztt_25med_1Track (subtraction)"
sub_ztt_35med_1Track = samples.sub_ztt_35med_1Track.copy()
sub_ztt_35med_1Track.tlatex = "Ztt_35med_1Track (subtraction)"
sub_ztt_50L1TAU12med_1Track = samples.sub_ztt_50L1TAU12med_1Track.copy()
sub_ztt_50L1TAU12med_1Track.tlatex = "Ztt_50L1TAU12med_1Track (subtraction)"
sub_ztt_80med_1Track = samples.sub_ztt_80med_1Track.copy()
sub_ztt_80med_1Track.tlatex = "Ztt_80med_1Track (subtraction)"
sub_ztt_80L1TAU60med_1Track = samples.sub_ztt_80L1TAU60med_1Track.copy()
sub_ztt_80L1TAU60med_1Track.tlatex = "Ztt_80L1TAU60med_1Track (subtraction)"
sub_ztt_125med_1Track = samples.sub_ztt_125med_1Track.copy()
sub_ztt_125med_1Track.tlatex = "Ztt_125med_1Track (subtraction)"
sub_ztt_160med_1Track = samples.sub_ztt_160med_1Track.copy()
sub_ztt_160med_1Track.tlatex = "Ztt_160med_1Track (subtraction)"
sub_ztt_L1TAU12IMmed_1Track = samples.sub_ztt_L1TAU12IMmed_1Track.copy()
sub_ztt_L1TAU12IMmed_1Track.tlatex = "Ztt_L1TAU12IMmed_1Track (subtraction)"

sub_ztt_ptonly_1Track = samples.sub_ztt_ptonly_1Track.copy()
sub_ztt_ptonly_1Track.tlatex = "Ztt_ptonly_1Track (subtraction)"
sub_ztt_tracktwo_1Track = samples.sub_ztt_tracktwo_1Track.copy()
sub_ztt_tracktwo_1Track.tlatex = "Ztt_tracktwo_1Track (subtraction)"

sub_ztt_25med_3Track = samples.sub_ztt_25med_3Track.copy()
sub_ztt_25med_3Track.tlatex = "Ztt_25med_3Track (subtraction)"
sub_ztt_35med_3Track = samples.sub_ztt_35med_3Track.copy()
sub_ztt_35med_3Track.tlatex = "Ztt_35med_3Track (subtraction)"
sub_ztt_50L1TAU12med_3Track = samples.sub_ztt_50L1TAU12med_3Track.copy()
sub_ztt_50L1TAU12med_3Track.tlatex = "Ztt_50L1TAU12med_3Track (subtraction)"
sub_ztt_80med_3Track = samples.sub_ztt_80med_3Track.copy()
sub_ztt_80med_3Track.tlatex = "Ztt_80med_3Track (subtraction)"
sub_ztt_80L1TAU60med_3Track = samples.sub_ztt_80L1TAU60med_3Track.copy()
sub_ztt_80L1TAU60med_3Track.tlatex = "Ztt_80L1TAU60med_3Track (subtraction)"
sub_ztt_125med_3Track = samples.sub_ztt_125med_3Track.copy()
sub_ztt_125med_3Track.tlatex = "Ztt_125med_3Track (subtraction)"
sub_ztt_160med_3Track = samples.sub_ztt_160med_3Track.copy()
sub_ztt_160med_3Track.tlatex = "Ztt_160med_3Track (subtraction)"
sub_ztt_L1TAU12IMmed_3Track = samples.sub_ztt_L1TAU12IMmed_3Track.copy()
sub_ztt_L1TAU12IMmed_3Track.tlatex = "Ztt_L1TAU12IMmed_3Track (subtraction)"

sub_ztt_ptonly_3Track = samples.sub_ztt_ptonly_3Track.copy()
sub_ztt_ptonly_3Track.tlatex = "Ztt_ptonly_3Track (subtraction)"
sub_ztt_tracktwo_3Track = samples.sub_ztt_tracktwo_3Track.copy()
sub_ztt_tracktwo_3Track.tlatex = "Ztt_track_3Track (subtraction)"

#-----------------------------------
# BOTH TRACKS
#-----------------------------------

# ADDITIONAL REGIONS

addon_data_OS_no_cuts    = samples.addon_data.copy()
addon_Wjets_OS_no_cuts   = samples.addon_Wjets.copy()
addon_Zlljets_OS_no_cuts = samples.addon_Zlljets.copy()
addon_top_OS_no_cuts     = samples.addon_top.copy()

addon_data_highSCDP_highMT    = samples.addon_data.copy()
addon_Wjets_highSCDP_highMT   = samples.addon_Wjets.copy()
addon_Zlljets_highSCDP_highMT = samples.addon_Zlljets.copy()
addon_top_highSCDP_highMT     = samples.addon_top.copy()

addon_data_lowSCDP_highMT    = samples.addon_data.copy()
addon_Wjets_lowSCDP_highMT   = samples.addon_Wjets.copy()
addon_Zlljets_lowSCDP_highMT = samples.addon_Zlljets.copy()
addon_top_lowSCDP_highMT     = samples.addon_top.copy()

addon_data_lowSCDP_lowMT    = samples.addon_data.copy()
addon_Wjets_lowSCDP_lowMT   = samples.addon_Wjets.copy()
addon_Zlljets_lowSCDP_lowMT = samples.addon_Zlljets.copy()
addon_top_lowSCDP_lowMT     = samples.addon_top.copy()

addon_data_lowSCDP    = samples.addon_data.copy()
addon_Wjets_lowSCDP   = samples.addon_Wjets.copy()
addon_Zlljets_lowSCDP = samples.addon_Zlljets.copy()
addon_top_lowSCDP     = samples.addon_top.copy()

addon_data_highSCDP    = samples.addon_data.copy()
addon_Wjets_highSCDP   = samples.addon_Wjets.copy()
addon_Zlljets_highSCDP = samples.addon_Zlljets.copy()
addon_top_highSCDP     = samples.addon_top.copy()

# ADDON FOR SR

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

addon_data_50L1TAU12med    = samples.addon_data_25med.copy()
addon_Wjets_50L1TAU12med   = samples.addon_Wjets_25med.copy()
addon_Zlljets_50L1TAU12med = samples.addon_Zlljets_25med.copy()
addon_top_50L1TAU12med     = samples.addon_top_25med.copy()

addon_data_50L1TAU12med_lowPT    = samples.addon_data_35med_lowPT.copy()
addon_Wjets_50L1TAU12med_lowPT   = samples.addon_Wjets_35med_lowPT.copy()
addon_Zlljets_50L1TAU12med_lowPT = samples.addon_Zlljets_35med_lowPT.copy()
addon_top_50L1TAU12med_lowPT     = samples.addon_top_35med_lowPT.copy()

addon_data_50L1TAU12med_highPT    = samples.addon_data_35med_highPT.copy()
addon_Wjets_50L1TAU12med_highPT   = samples.addon_Wjets_35med_highPT.copy()
addon_Zlljets_50L1TAU12med_highPT = samples.addon_Zlljets_35med_highPT.copy()
addon_top_50L1TAU12med_highPT     = samples.addon_top_35med_highPT.copy()

addon_data_80med    = samples.addon_data_25med.copy()
addon_Wjets_80med   = samples.addon_Wjets_25med.copy()
addon_Zlljets_80med = samples.addon_Zlljets_25med.copy()
addon_top_80med     = samples.addon_top_25med.copy()

addon_data_80med_lowPT    = samples.addon_data_35med_lowPT.copy()
addon_Wjets_80med_lowPT   = samples.addon_Wjets_35med_lowPT.copy()
addon_Zlljets_80med_lowPT = samples.addon_Zlljets_35med_lowPT.copy()
addon_top_80med_lowPT     = samples.addon_top_35med_lowPT.copy()

addon_data_80med_highPT    = samples.addon_data_35med_highPT.copy()
addon_Wjets_80med_highPT   = samples.addon_Wjets_35med_highPT.copy()
addon_Zlljets_80med_highPT = samples.addon_Zlljets_35med_highPT.copy()
addon_top_80med_highPT     = samples.addon_top_35med_highPT.copy()

addon_data_80L1TAU60med    = samples.addon_data_25med.copy()
addon_Wjets_80L1TAU60med   = samples.addon_Wjets_25med.copy()
addon_Zlljets_80L1TAU60med = samples.addon_Zlljets_25med.copy()
addon_top_80L1TAU60med     = samples.addon_top_25med.copy()

addon_data_80L1TAU60med_lowPT    = samples.addon_data_35med_lowPT.copy()
addon_Wjets_80L1TAU60med_lowPT   = samples.addon_Wjets_35med_lowPT.copy()
addon_Zlljets_80L1TAU60med_lowPT = samples.addon_Zlljets_35med_lowPT.copy()
addon_top_80L1TAU60med_lowPT     = samples.addon_top_35med_lowPT.copy()

addon_data_80L1TAU60med_highPT    = samples.addon_data_35med_highPT.copy()
addon_Wjets_80L1TAU60med_highPT   = samples.addon_Wjets_35med_highPT.copy()
addon_Zlljets_80L1TAU60med_highPT = samples.addon_Zlljets_35med_highPT.copy()
addon_top_80L1TAU60med_highPT     = samples.addon_top_35med_highPT.copy()

addon_data_125med    = samples.addon_data_25med.copy()
addon_Wjets_125med   = samples.addon_Wjets_25med.copy()
addon_Zlljets_125med = samples.addon_Zlljets_25med.copy()
addon_top_125med     = samples.addon_top_25med.copy()

addon_data_125med_lowPT    = samples.addon_data_35med_lowPT.copy()
addon_Wjets_125med_lowPT   = samples.addon_Wjets_35med_lowPT.copy()
addon_Zlljets_125med_lowPT = samples.addon_Zlljets_35med_lowPT.copy()
addon_top_125med_lowPT     = samples.addon_top_35med_lowPT.copy()

addon_data_125med_highPT    = samples.addon_data_35med_highPT.copy()
addon_Wjets_125med_highPT   = samples.addon_Wjets_35med_highPT.copy()
addon_Zlljets_125med_highPT = samples.addon_Zlljets_35med_highPT.copy()
addon_top_125med_highPT     = samples.addon_top_35med_highPT.copy()

addon_data_160med    = samples.addon_data_25med.copy()
addon_Wjets_160med   = samples.addon_Wjets_25med.copy()
addon_Zlljets_160med = samples.addon_Zlljets_25med.copy()
addon_top_160med     = samples.addon_top_25med.copy()

addon_data_L1TAU12IMmed    = samples.addon_data_25med.copy()
addon_Wjets_L1TAU12IMmed   = samples.addon_Wjets_25med.copy()
addon_Zlljets_L1TAU12IMmed = samples.addon_Zlljets_25med.copy()
addon_top_L1TAU12IMmed     = samples.addon_top_25med.copy()

addon_data_160med_lowPT    = samples.addon_data_35med_lowPT.copy()
addon_Wjets_160med_lowPT   = samples.addon_Wjets_35med_lowPT.copy()
addon_Zlljets_160med_lowPT = samples.addon_Zlljets_35med_lowPT.copy()
addon_top_160med_lowPT     = samples.addon_top_35med_lowPT.copy()

addon_data_160med_highPT    = samples.addon_data_35med_highPT.copy()
addon_Wjets_160med_highPT   = samples.addon_Wjets_35med_highPT.copy()
addon_Zlljets_160med_highPT = samples.addon_Zlljets_35med_highPT.copy()
addon_top_160med_highPT     = samples.addon_top_35med_highPT.copy()

addon_data_L1TAU12IMmed_lowPT    = samples.addon_data_35med_lowPT.copy()
addon_Wjets_L1TAU12IMmed_lowPT   = samples.addon_Wjets_35med_lowPT.copy()
addon_Zlljets_L1TAU12IMmed_lowPT = samples.addon_Zlljets_35med_lowPT.copy()
addon_top_L1TAU12IMmed_lowPT     = samples.addon_top_35med_lowPT.copy()

addon_data_L1TAU12IMmed_highPT    = samples.addon_data_35med_highPT.copy()
addon_Wjets_L1TAU12IMmed_highPT   = samples.addon_Wjets_35med_highPT.copy()
addon_Zlljets_L1TAU12IMmed_highPT = samples.addon_Zlljets_35med_highPT.copy()
addon_top_L1TAU12IMmed_highPT     = samples.addon_top_35med_highPT.copy()

addon_data_ptonly    = samples.addon_data_25med.copy()
addon_Wjets_ptonly   = samples.addon_Wjets_25med.copy()
addon_Zlljets_ptonly = samples.addon_Zlljets_25med.copy()
addon_top_ptonly     = samples.addon_top_25med.copy()

addon_data_ptonly_lowPT    = samples.addon_data_35med_lowPT.copy()
addon_Wjets_ptonly_lowPT   = samples.addon_Wjets_35med_lowPT.copy()
addon_Zlljets_ptonly_lowPT = samples.addon_Zlljets_35med_lowPT.copy()
addon_top_ptonly_lowPT     = samples.addon_top_35med_lowPT.copy()

addon_data_ptonly_highPT    = samples.addon_data_35med_highPT.copy()
addon_Wjets_ptonly_highPT   = samples.addon_Wjets_35med_highPT.copy()
addon_Zlljets_ptonly_highPT = samples.addon_Zlljets_35med_highPT.copy()
addon_top_ptonly_highPT     = samples.addon_top_35med_highPT.copy()

addon_data_tracktwo    = samples.addon_data_25med.copy()
addon_Wjets_tracktwo   = samples.addon_Wjets_25med.copy()
addon_Zlljets_tracktwo = samples.addon_Zlljets_25med.copy()
addon_top_tracktwo     = samples.addon_top_25med.copy()

addon_data_tracktwo_lowPT    = samples.addon_data_35med_lowPT.copy()
addon_Wjets_tracktwo_lowPT   = samples.addon_Wjets_35med_lowPT.copy()
addon_Zlljets_tracktwo_lowPT = samples.addon_Zlljets_35med_lowPT.copy()
addon_top_tracktwo_lowPT     = samples.addon_top_35med_lowPT.copy()

addon_data_tracktwo_highPT    = samples.addon_data_35med_highPT.copy()
addon_Wjets_tracktwo_highPT   = samples.addon_Wjets_35med_highPT.copy()
addon_Zlljets_tracktwo_highPT = samples.addon_Zlljets_35med_highPT.copy()
addon_top_tracktwo_highPT     = samples.addon_top_35med_highPT.copy()

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

addon_data_50L1TAU12med_1Track    = samples.addon_data_25med_1Track.copy()
addon_Wjets_50L1TAU12med_1Track   = samples.addon_Wjets_25med_1Track.copy()
addon_Zlljets_50L1TAU12med_1Track = samples.addon_Zlljets_25med_1Track.copy()
addon_top_50L1TAU12med_1Track     = samples.addon_top_25med_1Track.copy()

addon_data_50L1TAU12med_lowPT_1Track    = samples.addon_data_35med_lowPT_1Track.copy()
addon_Wjets_50L1TAU12med_lowPT_1Track   = samples.addon_Wjets_35med_lowPT_1Track.copy()
addon_Zlljets_50L1TAU12med_lowPT_1Track = samples.addon_Zlljets_35med_lowPT_1Track.copy()
addon_top_50L1TAU12med_lowPT_1Track     = samples.addon_top_35med_lowPT_1Track.copy()

addon_data_50L1TAU12med_highPT_1Track    = samples.addon_data_35med_highPT_1Track.copy()
addon_Wjets_50L1TAU12med_highPT_1Track   = samples.addon_Wjets_35med_highPT_1Track.copy()
addon_Zlljets_50L1TAU12med_highPT_1Track = samples.addon_Zlljets_35med_highPT_1Track.copy()
addon_top_50L1TAU12med_highPT_1Track     = samples.addon_top_35med_highPT_1Track.copy()

addon_data_80med_1Track    = samples.addon_data_25med_1Track.copy()
addon_Wjets_80med_1Track   = samples.addon_Wjets_25med_1Track.copy()
addon_Zlljets_80med_1Track = samples.addon_Zlljets_25med_1Track.copy()
addon_top_80med_1Track     = samples.addon_top_25med_1Track.copy()

addon_data_80med_lowPT_1Track    = samples.addon_data_35med_lowPT_1Track.copy()
addon_Wjets_80med_lowPT_1Track   = samples.addon_Wjets_35med_lowPT_1Track.copy()
addon_Zlljets_80med_lowPT_1Track = samples.addon_Zlljets_35med_lowPT_1Track.copy()
addon_top_80med_lowPT_1Track     = samples.addon_top_35med_lowPT_1Track.copy()

addon_data_80med_highPT_1Track    = samples.addon_data_35med_highPT_1Track.copy()
addon_Wjets_80med_highPT_1Track   = samples.addon_Wjets_35med_highPT_1Track.copy()
addon_Zlljets_80med_highPT_1Track = samples.addon_Zlljets_35med_highPT_1Track.copy()
addon_top_80med_highPT_1Track     = samples.addon_top_35med_highPT_1Track.copy()

addon_data_80L1TAU60med_1Track    = samples.addon_data_25med_1Track.copy()
addon_Wjets_80L1TAU60med_1Track   = samples.addon_Wjets_25med_1Track.copy()
addon_Zlljets_80L1TAU60med_1Track = samples.addon_Zlljets_25med_1Track.copy()
addon_top_80L1TAU60med_1Track     = samples.addon_top_25med_1Track.copy()

addon_data_80L1TAU60med_lowPT_1Track    = samples.addon_data_35med_lowPT_1Track.copy()
addon_Wjets_80L1TAU60med_lowPT_1Track   = samples.addon_Wjets_35med_lowPT_1Track.copy()
addon_Zlljets_80L1TAU60med_lowPT_1Track = samples.addon_Zlljets_35med_lowPT_1Track.copy()
addon_top_80L1TAU60med_lowPT_1Track     = samples.addon_top_35med_lowPT_1Track.copy()

addon_data_80L1TAU60med_highPT_1Track    = samples.addon_data_35med_highPT_1Track.copy()
addon_Wjets_80L1TAU60med_highPT_1Track   = samples.addon_Wjets_35med_highPT_1Track.copy()
addon_Zlljets_80L1TAU60med_highPT_1Track = samples.addon_Zlljets_35med_highPT_1Track.copy()
addon_top_80L1TAU60med_highPT_1Track     = samples.addon_top_35med_highPT_1Track.copy()

addon_data_125med_1Track    = samples.addon_data_25med_1Track.copy()
addon_Wjets_125med_1Track   = samples.addon_Wjets_25med_1Track.copy()
addon_Zlljets_125med_1Track = samples.addon_Zlljets_25med_1Track.copy()
addon_top_125med_1Track     = samples.addon_top_25med_1Track.copy()

addon_data_125med_lowPT_1Track    = samples.addon_data_35med_lowPT_1Track.copy()
addon_Wjets_125med_lowPT_1Track   = samples.addon_Wjets_35med_lowPT_1Track.copy()
addon_Zlljets_125med_lowPT_1Track = samples.addon_Zlljets_35med_lowPT_1Track.copy()
addon_top_125med_lowPT_1Track     = samples.addon_top_35med_lowPT_1Track.copy()

addon_data_125med_highPT_1Track    = samples.addon_data_35med_highPT_1Track.copy()
addon_Wjets_125med_highPT_1Track   = samples.addon_Wjets_35med_highPT_1Track.copy()
addon_Zlljets_125med_highPT_1Track = samples.addon_Zlljets_35med_highPT_1Track.copy()
addon_top_125med_highPT_1Track     = samples.addon_top_35med_highPT_1Track.copy()

addon_data_160med_1Track    = samples.addon_data_25med_1Track.copy()
addon_Wjets_160med_1Track   = samples.addon_Wjets_25med_1Track.copy()
addon_Zlljets_160med_1Track = samples.addon_Zlljets_25med_1Track.copy()
addon_top_160med_1Track     = samples.addon_top_25med_1Track.copy()

addon_data_160med_lowPT_1Track    = samples.addon_data_35med_lowPT_1Track.copy()
addon_Wjets_160med_lowPT_1Track   = samples.addon_Wjets_35med_lowPT_1Track.copy()
addon_Zlljets_160med_lowPT_1Track = samples.addon_Zlljets_35med_lowPT_1Track.copy()
addon_top_160med_lowPT_1Track     = samples.addon_top_35med_lowPT_1Track.copy()

addon_data_160med_highPT_1Track    = samples.addon_data_35med_highPT_1Track.copy()
addon_Wjets_160med_highPT_1Track   = samples.addon_Wjets_35med_highPT_1Track.copy()
addon_Zlljets_160med_highPT_1Track = samples.addon_Zlljets_35med_highPT_1Track.copy()
addon_top_160med_highPT_1Track     = samples.addon_top_35med_highPT_1Track.copy()

addon_data_L1TAU12IMmed_1Track    = samples.addon_data_25med_1Track.copy()
addon_Wjets_L1TAU12IMmed_1Track   = samples.addon_Wjets_25med_1Track.copy()
addon_Zlljets_L1TAU12IMmed_1Track = samples.addon_Zlljets_25med_1Track.copy()
addon_top_L1TAU12IMmed_1Track     = samples.addon_top_25med_1Track.copy()

addon_data_L1TAU12IMmed_lowPT_1Track    = samples.addon_data_35med_lowPT_1Track.copy()
addon_Wjets_L1TAU12IMmed_lowPT_1Track   = samples.addon_Wjets_35med_lowPT_1Track.copy()
addon_Zlljets_L1TAU12IMmed_lowPT_1Track = samples.addon_Zlljets_35med_lowPT_1Track.copy()
addon_top_L1TAU12IMmed_lowPT_1Track     = samples.addon_top_35med_lowPT_1Track.copy()

addon_data_L1TAU12IMmed_highPT_1Track    = samples.addon_data_35med_highPT_1Track.copy()
addon_Wjets_L1TAU12IMmed_highPT_1Track   = samples.addon_Wjets_35med_highPT_1Track.copy()
addon_Zlljets_L1TAU12IMmed_highPT_1Track = samples.addon_Zlljets_35med_highPT_1Track.copy()
addon_top_L1TAU12IMmed_highPT_1Track     = samples.addon_top_35med_highPT_1Track.copy()

addon_data_ptonly_1Track    = samples.addon_data_25med_1Track.copy()
addon_Wjets_ptonly_1Track   = samples.addon_Wjets_25med_1Track.copy()
addon_Zlljets_ptonly_1Track = samples.addon_Zlljets_25med_1Track.copy()
addon_top_ptonly_1Track     = samples.addon_top_25med_1Track.copy()

addon_data_ptonly_lowPT_1Track    = samples.addon_data_35med_lowPT_1Track.copy()
addon_Wjets_ptonly_lowPT_1Track   = samples.addon_Wjets_35med_lowPT_1Track.copy()
addon_Zlljets_ptonly_lowPT_1Track = samples.addon_Zlljets_35med_lowPT_1Track.copy()
addon_top_ptonly_lowPT_1Track     = samples.addon_top_35med_lowPT_1Track.copy()

addon_data_ptonly_highPT_1Track    = samples.addon_data_35med_highPT_1Track.copy()
addon_Wjets_ptonly_highPT_1Track   = samples.addon_Wjets_35med_highPT_1Track.copy()
addon_Zlljets_ptonly_highPT_1Track = samples.addon_Zlljets_35med_highPT_1Track.copy()
addon_top_ptonly_highPT_1Track     = samples.addon_top_35med_highPT_1Track.copy()

addon_data_tracktwo_1Track    = samples.addon_data_25med_1Track.copy()
addon_Wjets_tracktwo_1Track   = samples.addon_Wjets_25med_1Track.copy()
addon_Zlljets_tracktwo_1Track = samples.addon_Zlljets_25med_1Track.copy()
addon_top_tracktwo_1Track     = samples.addon_top_25med_1Track.copy()

addon_data_tracktwo_lowPT_1Track    = samples.addon_data_35med_lowPT_1Track.copy()
addon_Wjets_tracktwo_lowPT_1Track   = samples.addon_Wjets_35med_lowPT_1Track.copy()
addon_Zlljets_tracktwo_lowPT_1Track = samples.addon_Zlljets_35med_lowPT_1Track.copy()
addon_top_tracktwo_lowPT_1Track     = samples.addon_top_35med_lowPT_1Track.copy()

addon_data_tracktwo_highPT_1Track    = samples.addon_data_35med_highPT_1Track.copy()
addon_Wjets_tracktwo_highPT_1Track   = samples.addon_Wjets_35med_highPT_1Track.copy()
addon_Zlljets_tracktwo_highPT_1Track = samples.addon_Zlljets_35med_highPT_1Track.copy()
addon_top_tracktwo_highPT_1Track     = samples.addon_top_35med_highPT_1Track.copy()

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

addon_data_50L1TAU12med_3Track    = samples.addon_data_25med_3Track.copy()
addon_Wjets_50L1TAU12med_3Track   = samples.addon_Wjets_25med_3Track.copy()
addon_Zlljets_50L1TAU12med_3Track = samples.addon_Zlljets_25med_3Track.copy()
addon_top_50L1TAU12med_3Track     = samples.addon_top_25med_3Track.copy()

addon_data_50L1TAU12med_lowPT_3Track    = samples.addon_data_35med_lowPT_3Track.copy()
addon_Wjets_50L1TAU12med_lowPT_3Track   = samples.addon_Wjets_35med_lowPT_3Track.copy()
addon_Zlljets_50L1TAU12med_lowPT_3Track = samples.addon_Zlljets_35med_lowPT_3Track.copy()
addon_top_50L1TAU12med_lowPT_3Track     = samples.addon_top_35med_lowPT_3Track.copy()

addon_data_50L1TAU12med_highPT_3Track    = samples.addon_data_35med_highPT_3Track.copy()
addon_Wjets_50L1TAU12med_highPT_3Track   = samples.addon_Wjets_35med_highPT_3Track.copy()
addon_Zlljets_50L1TAU12med_highPT_3Track = samples.addon_Zlljets_35med_highPT_3Track.copy()
addon_top_50L1TAU12med_highPT_3Track     = samples.addon_top_35med_highPT_3Track.copy()

addon_data_80med_3Track    = samples.addon_data_25med_3Track.copy()
addon_Wjets_80med_3Track   = samples.addon_Wjets_25med_3Track.copy()
addon_Zlljets_80med_3Track = samples.addon_Zlljets_25med_3Track.copy()
addon_top_80med_3Track     = samples.addon_top_25med_3Track.copy()

addon_data_80med_lowPT_3Track    = samples.addon_data_35med_lowPT_3Track.copy()
addon_Wjets_80med_lowPT_3Track   = samples.addon_Wjets_35med_lowPT_3Track.copy()
addon_Zlljets_80med_lowPT_3Track = samples.addon_Zlljets_35med_lowPT_3Track.copy()
addon_top_80med_lowPT_3Track     = samples.addon_top_35med_lowPT_3Track.copy()

addon_data_80med_highPT_3Track    = samples.addon_data_35med_highPT_3Track.copy()
addon_Wjets_80med_highPT_3Track   = samples.addon_Wjets_35med_highPT_3Track.copy()
addon_Zlljets_80med_highPT_3Track = samples.addon_Zlljets_35med_highPT_3Track.copy()
addon_top_80med_highPT_3Track     = samples.addon_top_35med_highPT_3Track.copy()

addon_data_80L1TAU60med_3Track    = samples.addon_data_25med_3Track.copy()
addon_Wjets_80L1TAU60med_3Track   = samples.addon_Wjets_25med_3Track.copy()
addon_Zlljets_80L1TAU60med_3Track = samples.addon_Zlljets_25med_3Track.copy()
addon_top_80L1TAU60med_3Track     = samples.addon_top_25med_3Track.copy()

addon_data_80L1TAU60med_lowPT_3Track    = samples.addon_data_35med_lowPT_3Track.copy()
addon_Wjets_80L1TAU60med_lowPT_3Track   = samples.addon_Wjets_35med_lowPT_3Track.copy()
addon_Zlljets_80L1TAU60med_lowPT_3Track = samples.addon_Zlljets_35med_lowPT_3Track.copy()
addon_top_80L1TAU60med_lowPT_3Track     = samples.addon_top_35med_lowPT_3Track.copy()

addon_data_80L1TAU60med_highPT_3Track    = samples.addon_data_35med_highPT_3Track.copy()
addon_Wjets_80L1TAU60med_highPT_3Track   = samples.addon_Wjets_35med_highPT_3Track.copy()
addon_Zlljets_80L1TAU60med_highPT_3Track = samples.addon_Zlljets_35med_highPT_3Track.copy()
addon_top_80L1TAU60med_highPT_3Track     = samples.addon_top_35med_highPT_3Track.copy()

addon_data_125med_3Track    = samples.addon_data_25med_3Track.copy()
addon_Wjets_125med_3Track   = samples.addon_Wjets_25med_3Track.copy()
addon_Zlljets_125med_3Track = samples.addon_Zlljets_25med_3Track.copy()
addon_top_125med_3Track     = samples.addon_top_25med_3Track.copy()

addon_data_125med_lowPT_3Track    = samples.addon_data_35med_lowPT_3Track.copy()
addon_Wjets_125med_lowPT_3Track   = samples.addon_Wjets_35med_lowPT_3Track.copy()
addon_Zlljets_125med_lowPT_3Track = samples.addon_Zlljets_35med_lowPT_3Track.copy()
addon_top_125med_lowPT_3Track     = samples.addon_top_35med_lowPT_3Track.copy()

addon_data_125med_highPT_3Track    = samples.addon_data_35med_highPT_3Track.copy()
addon_Wjets_125med_highPT_3Track   = samples.addon_Wjets_35med_highPT_3Track.copy()
addon_Zlljets_125med_highPT_3Track = samples.addon_Zlljets_35med_highPT_3Track.copy()
addon_top_125med_highPT_3Track     = samples.addon_top_35med_highPT_3Track.copy()

addon_data_160med_3Track    = samples.addon_data_25med_3Track.copy()
addon_Wjets_160med_3Track   = samples.addon_Wjets_25med_3Track.copy()
addon_Zlljets_160med_3Track = samples.addon_Zlljets_25med_3Track.copy()
addon_top_160med_3Track     = samples.addon_top_25med_3Track.copy()

addon_data_160med_lowPT_3Track    = samples.addon_data_35med_lowPT_3Track.copy()
addon_Wjets_160med_lowPT_3Track   = samples.addon_Wjets_35med_lowPT_3Track.copy()
addon_Zlljets_160med_lowPT_3Track = samples.addon_Zlljets_35med_lowPT_3Track.copy()
addon_top_160med_lowPT_3Track     = samples.addon_top_35med_lowPT_3Track.copy()

addon_data_160med_highPT_3Track    = samples.addon_data_35med_highPT_3Track.copy()
addon_Wjets_160med_highPT_3Track   = samples.addon_Wjets_35med_highPT_3Track.copy()
addon_Zlljets_160med_highPT_3Track = samples.addon_Zlljets_35med_highPT_3Track.copy()
addon_top_160med_highPT_3Track     = samples.addon_top_35med_highPT_3Track.copy()

addon_data_L1TAU12IMmed_3Track    = samples.addon_data_25med_3Track.copy()
addon_Wjets_L1TAU12IMmed_3Track   = samples.addon_Wjets_25med_3Track.copy()
addon_Zlljets_L1TAU12IMmed_3Track = samples.addon_Zlljets_25med_3Track.copy()
addon_top_L1TAU12IMmed_3Track     = samples.addon_top_25med_3Track.copy()

addon_data_L1TAU12IMmed_3Track    = samples.addon_data_25med_3Track.copy()
addon_Wjets_L1TAU12IMmed_3Track   = samples.addon_Wjets_25med_3Track.copy()
addon_Zlljets_L1TAU12IMmed_3Track = samples.addon_Zlljets_25med_3Track.copy()
addon_top_L1TAU12IMmed_3Track     = samples.addon_top_25med_3Track.copy()

addon_data_L1TAU12IMmed_lowPT_3Track    = samples.addon_data_35med_lowPT_3Track.copy()
addon_Wjets_L1TAU12IMmed_lowPT_3Track   = samples.addon_Wjets_35med_lowPT_3Track.copy()
addon_Zlljets_L1TAU12IMmed_lowPT_3Track = samples.addon_Zlljets_35med_lowPT_3Track.copy()
addon_top_L1TAU12IMmed_lowPT_3Track     = samples.addon_top_35med_lowPT_3Track.copy()

addon_data_L1TAU12IMmed_highPT_3Track    = samples.addon_data_35med_highPT_3Track.copy()
addon_Wjets_L1TAU12IMmed_highPT_3Track   = samples.addon_Wjets_35med_highPT_3Track.copy()
addon_Zlljets_L1TAU12IMmed_highPT_3Track = samples.addon_Zlljets_35med_highPT_3Track.copy()
addon_top_L1TAU12IMmed_highPT_3Track     = samples.addon_top_35med_highPT_3Track.copy()

addon_data_ptonly_3Track    = samples.addon_data_25med_3Track.copy()
addon_Wjets_ptonly_3Track   = samples.addon_Wjets_25med_3Track.copy()
addon_Zlljets_ptonly_3Track = samples.addon_Zlljets_25med_3Track.copy()
addon_top_ptonly_3Track     = samples.addon_top_25med_3Track.copy()

addon_data_ptonly_lowPT_3Track    = samples.addon_data_35med_lowPT_3Track.copy()
addon_Wjets_ptonly_lowPT_3Track   = samples.addon_Wjets_35med_lowPT_3Track.copy()
addon_Zlljets_ptonly_lowPT_3Track = samples.addon_Zlljets_35med_lowPT_3Track.copy()
addon_top_ptonly_lowPT_3Track     = samples.addon_top_35med_lowPT_3Track.copy()

addon_data_ptonly_highPT_3Track    = samples.addon_data_35med_highPT_3Track.copy()
addon_Wjets_ptonly_highPT_3Track   = samples.addon_Wjets_35med_highPT_3Track.copy()
addon_Zlljets_ptonly_highPT_3Track = samples.addon_Zlljets_35med_highPT_3Track.copy()
addon_top_ptonly_highPT_3Track     = samples.addon_top_35med_highPT_3Track.copy()

addon_data_tracktwo_3Track    = samples.addon_data_25med_3Track.copy()
addon_Wjets_tracktwo_3Track   = samples.addon_Wjets_25med_3Track.copy()
addon_Zlljets_tracktwo_3Track = samples.addon_Zlljets_25med_3Track.copy()
addon_top_tracktwo_3Track     = samples.addon_top_25med_3Track.copy()

addon_data_tracktwo_lowPT_3Track    = samples.addon_data_35med_lowPT_3Track.copy()
addon_Wjets_tracktwo_lowPT_3Track   = samples.addon_Wjets_35med_lowPT_3Track.copy()
addon_Zlljets_tracktwo_lowPT_3Track = samples.addon_Zlljets_35med_lowPT_3Track.copy()
addon_top_tracktwo_lowPT_3Track     = samples.addon_top_35med_lowPT_3Track.copy()

addon_data_tracktwo_highPT_3Track    = samples.addon_data_35med_highPT_3Track.copy()
addon_Wjets_tracktwo_highPT_3Track   = samples.addon_Wjets_35med_highPT_3Track.copy()
addon_Zlljets_tracktwo_highPT_3Track = samples.addon_Zlljets_35med_highPT_3Track.copy()
addon_top_tracktwo_highPT_3Track     = samples.addon_top_35med_highPT_3Track.copy()


#-----------------------------
#-----------------------------

# ADDITIONAL REGIONS

addon_backgrounds_highSCDP = []
addon_backgrounds_highSCDP.append(addon_data_highSCDP)
addon_backgrounds_highSCDP.append(addon_Wjets_highSCDP)
addon_backgrounds_highSCDP.append(addon_Zlljets_highSCDP)
addon_backgrounds_highSCDP.append(addon_top_highSCDP)

addon_backgrounds_lowSCDP = []
addon_backgrounds_lowSCDP.append(addon_data_lowSCDP)
addon_backgrounds_lowSCDP.append(addon_Wjets_lowSCDP)
addon_backgrounds_lowSCDP.append(addon_Zlljets_lowSCDP)
addon_backgrounds_lowSCDP.append(addon_top_lowSCDP)

addon_backgrounds_lowSCDP_lowMT = []
addon_backgrounds_lowSCDP_lowMT.append(addon_data_lowSCDP_lowMT)
addon_backgrounds_lowSCDP_lowMT.append(addon_Wjets_lowSCDP_lowMT)
addon_backgrounds_lowSCDP_lowMT.append(addon_Zlljets_lowSCDP_lowMT)
addon_backgrounds_lowSCDP_lowMT.append(addon_top_lowSCDP_lowMT)

addon_backgrounds_lowSCDP_highMT = []
addon_backgrounds_lowSCDP_highMT.append(addon_data_lowSCDP_highMT)
addon_backgrounds_lowSCDP_highMT.append(addon_Wjets_lowSCDP_highMT)
addon_backgrounds_lowSCDP_highMT.append(addon_Zlljets_lowSCDP_highMT)
addon_backgrounds_lowSCDP_highMT.append(addon_top_lowSCDP_highMT)

addon_backgrounds_highSCDP_highMT = []
addon_backgrounds_highSCDP_highMT.append(addon_data_highSCDP_highMT)
addon_backgrounds_highSCDP_highMT.append(addon_Wjets_highSCDP_highMT)
addon_backgrounds_highSCDP_highMT.append(addon_Zlljets_highSCDP_highMT)
addon_backgrounds_highSCDP_highMT.append(addon_top_highSCDP_highMT)

addon_backgrounds_OS_no_cuts = []
addon_backgrounds_OS_no_cuts.append(addon_data_OS_no_cuts)
addon_backgrounds_OS_no_cuts.append(addon_Wjets_OS_no_cuts)
addon_backgrounds_OS_no_cuts.append(addon_Zlljets_OS_no_cuts)
addon_backgrounds_OS_no_cuts.append(addon_top_OS_no_cuts)

# SIGNAL REGIONS

addon_backgrounds = []
addon_backgrounds.append(addon_data)
addon_backgrounds.append(addon_Wjets)
addon_backgrounds.append(addon_Zlljets)
addon_backgrounds.append(addon_top)

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

addon_backgrounds_50L1TAU12med = []
addon_backgrounds_50L1TAU12med.append(addon_data_50L1TAU12med)
addon_backgrounds_50L1TAU12med.append(addon_Wjets_50L1TAU12med)
addon_backgrounds_50L1TAU12med.append(addon_Zlljets_50L1TAU12med)
addon_backgrounds_50L1TAU12med.append(addon_top_50L1TAU12med)

addon_backgrounds_50L1TAU12med_lowPT = []
addon_backgrounds_50L1TAU12med_lowPT.append(addon_data_50L1TAU12med_lowPT)
addon_backgrounds_50L1TAU12med_lowPT.append(addon_Wjets_50L1TAU12med_lowPT)
addon_backgrounds_50L1TAU12med_lowPT.append(addon_Zlljets_50L1TAU12med_lowPT)
addon_backgrounds_50L1TAU12med_lowPT.append(addon_top_50L1TAU12med_lowPT)

addon_backgrounds_50L1TAU12med_highPT = []
addon_backgrounds_50L1TAU12med_highPT.append(addon_data_50L1TAU12med_highPT)
addon_backgrounds_50L1TAU12med_highPT.append(addon_Wjets_50L1TAU12med_highPT)
addon_backgrounds_50L1TAU12med_highPT.append(addon_Zlljets_50L1TAU12med_highPT)
addon_backgrounds_50L1TAU12med_highPT.append(addon_top_50L1TAU12med_highPT)

addon_backgrounds_80med = []
addon_backgrounds_80med.append(addon_data_80med)
addon_backgrounds_80med.append(addon_Wjets_80med)
addon_backgrounds_80med.append(addon_Zlljets_80med)
addon_backgrounds_80med.append(addon_top_80med)

addon_backgrounds_80med_lowPT = []
addon_backgrounds_80med_lowPT.append(addon_data_80med_lowPT)
addon_backgrounds_80med_lowPT.append(addon_Wjets_80med_lowPT)
addon_backgrounds_80med_lowPT.append(addon_Zlljets_80med_lowPT)
addon_backgrounds_80med_lowPT.append(addon_top_80med_lowPT)

addon_backgrounds_80med_highPT = []
addon_backgrounds_80med_highPT.append(addon_data_80med_highPT)
addon_backgrounds_80med_highPT.append(addon_Wjets_80med_highPT)
addon_backgrounds_80med_highPT.append(addon_Zlljets_80med_highPT)
addon_backgrounds_80med_highPT.append(addon_top_80med_highPT)

addon_backgrounds_80L1TAU60med = []
addon_backgrounds_80L1TAU60med.append(addon_data_80L1TAU60med)
addon_backgrounds_80L1TAU60med.append(addon_Wjets_80L1TAU60med)
addon_backgrounds_80L1TAU60med.append(addon_Zlljets_80L1TAU60med)
addon_backgrounds_80L1TAU60med.append(addon_top_80L1TAU60med)

addon_backgrounds_80L1TAU60med_lowPT = []
addon_backgrounds_80L1TAU60med_lowPT.append(addon_data_80L1TAU60med_lowPT)
addon_backgrounds_80L1TAU60med_lowPT.append(addon_Wjets_80L1TAU60med_lowPT)
addon_backgrounds_80L1TAU60med_lowPT.append(addon_Zlljets_80L1TAU60med_lowPT)
addon_backgrounds_80L1TAU60med_lowPT.append(addon_top_80L1TAU60med_lowPT)

addon_backgrounds_80L1TAU60med_highPT = []
addon_backgrounds_80L1TAU60med_highPT.append(addon_data_80L1TAU60med_highPT)
addon_backgrounds_80L1TAU60med_highPT.append(addon_Wjets_80L1TAU60med_highPT)
addon_backgrounds_80L1TAU60med_highPT.append(addon_Zlljets_80L1TAU60med_highPT)
addon_backgrounds_80L1TAU60med_highPT.append(addon_top_80L1TAU60med_highPT)

addon_backgrounds_125med = []
addon_backgrounds_125med.append(addon_data_125med)
addon_backgrounds_125med.append(addon_Wjets_125med)
addon_backgrounds_125med.append(addon_Zlljets_125med)
addon_backgrounds_125med.append(addon_top_125med)

addon_backgrounds_125med_lowPT = []
addon_backgrounds_125med_lowPT.append(addon_data_125med_lowPT)
addon_backgrounds_125med_lowPT.append(addon_Wjets_125med_lowPT)
addon_backgrounds_125med_lowPT.append(addon_Zlljets_125med_lowPT)
addon_backgrounds_125med_lowPT.append(addon_top_125med_lowPT)

addon_backgrounds_125med_highPT = []
addon_backgrounds_125med_highPT.append(addon_data_125med_highPT)
addon_backgrounds_125med_highPT.append(addon_Wjets_125med_highPT)
addon_backgrounds_125med_highPT.append(addon_Zlljets_125med_highPT)
addon_backgrounds_125med_highPT.append(addon_top_125med_highPT)

addon_backgrounds_160med = []
addon_backgrounds_160med.append(addon_data_160med)
addon_backgrounds_160med.append(addon_Wjets_160med)
addon_backgrounds_160med.append(addon_Zlljets_160med)
addon_backgrounds_160med.append(addon_top_160med)

addon_backgrounds_160med_lowPT = []
addon_backgrounds_160med_lowPT.append(addon_data_160med_lowPT)
addon_backgrounds_160med_lowPT.append(addon_Wjets_160med_lowPT)
addon_backgrounds_160med_lowPT.append(addon_Zlljets_160med_lowPT)
addon_backgrounds_160med_lowPT.append(addon_top_160med_lowPT)

addon_backgrounds_160med_highPT = []
addon_backgrounds_160med_highPT.append(addon_data_160med_highPT)
addon_backgrounds_160med_highPT.append(addon_Wjets_160med_highPT)
addon_backgrounds_160med_highPT.append(addon_Zlljets_160med_highPT)
addon_backgrounds_160med_highPT.append(addon_top_160med_highPT)

addon_backgrounds_L1TAU12IMmed = []
addon_backgrounds_L1TAU12IMmed.append(addon_data_L1TAU12IMmed)
addon_backgrounds_L1TAU12IMmed.append(addon_Wjets_L1TAU12IMmed)
addon_backgrounds_L1TAU12IMmed.append(addon_Zlljets_L1TAU12IMmed)
addon_backgrounds_L1TAU12IMmed.append(addon_top_L1TAU12IMmed)

addon_backgrounds_L1TAU12IMmed_lowPT = []
addon_backgrounds_L1TAU12IMmed_lowPT.append(addon_data_L1TAU12IMmed_lowPT)
addon_backgrounds_L1TAU12IMmed_lowPT.append(addon_Wjets_L1TAU12IMmed_lowPT)
addon_backgrounds_L1TAU12IMmed_lowPT.append(addon_Zlljets_L1TAU12IMmed_lowPT)
addon_backgrounds_L1TAU12IMmed_lowPT.append(addon_top_L1TAU12IMmed_lowPT)

addon_backgrounds_L1TAU12IMmed_highPT = []
addon_backgrounds_L1TAU12IMmed_highPT.append(addon_data_L1TAU12IMmed_highPT)
addon_backgrounds_L1TAU12IMmed_highPT.append(addon_Wjets_L1TAU12IMmed_highPT)
addon_backgrounds_L1TAU12IMmed_highPT.append(addon_Zlljets_L1TAU12IMmed_highPT)
addon_backgrounds_L1TAU12IMmed_highPT.append(addon_top_L1TAU12IMmed_highPT)

addon_backgrounds_ptonly = []
addon_backgrounds_ptonly.append(addon_data_ptonly)
addon_backgrounds_ptonly.append(addon_Wjets_ptonly)
addon_backgrounds_ptonly.append(addon_Zlljets_ptonly)
addon_backgrounds_ptonly.append(addon_top_ptonly)

addon_backgrounds_ptonly_lowPT = []
addon_backgrounds_ptonly_lowPT.append(addon_data_ptonly_lowPT)
addon_backgrounds_ptonly_lowPT.append(addon_Wjets_ptonly_lowPT)
addon_backgrounds_ptonly_lowPT.append(addon_Zlljets_ptonly_lowPT)
addon_backgrounds_ptonly_lowPT.append(addon_top_ptonly_lowPT)

addon_backgrounds_ptonly_highPT = []
addon_backgrounds_ptonly_highPT.append(addon_data_ptonly_highPT)
addon_backgrounds_ptonly_highPT.append(addon_Wjets_ptonly_highPT)
addon_backgrounds_ptonly_highPT.append(addon_Zlljets_ptonly_highPT)
addon_backgrounds_ptonly_highPT.append(addon_top_ptonly_highPT)

addon_backgrounds_tracktwo = []
addon_backgrounds_tracktwo.append(addon_data_tracktwo)
addon_backgrounds_tracktwo.append(addon_Wjets_tracktwo)
addon_backgrounds_tracktwo.append(addon_Zlljets_tracktwo)
addon_backgrounds_tracktwo.append(addon_top_tracktwo)

addon_backgrounds_tracktwo_lowPT = []
addon_backgrounds_tracktwo_lowPT.append(addon_data_tracktwo_lowPT)
addon_backgrounds_tracktwo_lowPT.append(addon_Wjets_tracktwo_lowPT)
addon_backgrounds_tracktwo_lowPT.append(addon_Zlljets_tracktwo_lowPT)
addon_backgrounds_tracktwo_lowPT.append(addon_top_tracktwo_lowPT)

addon_backgrounds_tracktwo_highPT = []
addon_backgrounds_tracktwo_highPT.append(addon_data_tracktwo_highPT)
addon_backgrounds_tracktwo_highPT.append(addon_Wjets_tracktwo_highPT)
addon_backgrounds_tracktwo_highPT.append(addon_Zlljets_tracktwo_highPT)
addon_backgrounds_tracktwo_highPT.append(addon_top_tracktwo_highPT)

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

addon_backgrounds_50L1TAU12med_1Track = []
addon_backgrounds_50L1TAU12med_1Track.append(addon_data_50L1TAU12med_1Track)
addon_backgrounds_50L1TAU12med_1Track.append(addon_Wjets_50L1TAU12med_1Track)
addon_backgrounds_50L1TAU12med_1Track.append(addon_Zlljets_50L1TAU12med_1Track)
addon_backgrounds_50L1TAU12med_1Track.append(addon_top_50L1TAU12med_1Track)

addon_backgrounds_50L1TAU12med_lowPT_1Track = []
addon_backgrounds_50L1TAU12med_lowPT_1Track.append(addon_data_50L1TAU12med_lowPT_1Track)
addon_backgrounds_50L1TAU12med_lowPT_1Track.append(addon_Wjets_50L1TAU12med_lowPT_1Track)
addon_backgrounds_50L1TAU12med_lowPT_1Track.append(addon_Zlljets_50L1TAU12med_lowPT_1Track)
addon_backgrounds_50L1TAU12med_lowPT_1Track.append(addon_top_50L1TAU12med_lowPT_1Track)

addon_backgrounds_50L1TAU12med_highPT_1Track = []
addon_backgrounds_50L1TAU12med_highPT_1Track.append(addon_data_50L1TAU12med_highPT_1Track)
addon_backgrounds_50L1TAU12med_highPT_1Track.append(addon_Wjets_50L1TAU12med_highPT_1Track)
addon_backgrounds_50L1TAU12med_highPT_1Track.append(addon_Zlljets_50L1TAU12med_highPT_1Track)
addon_backgrounds_50L1TAU12med_highPT_1Track.append(addon_top_50L1TAU12med_highPT_1Track)

addon_backgrounds_80med_1Track = []
addon_backgrounds_80med_1Track.append(addon_data_80med_1Track)
addon_backgrounds_80med_1Track.append(addon_Wjets_80med_1Track)
addon_backgrounds_80med_1Track.append(addon_Zlljets_80med_1Track)
addon_backgrounds_80med_1Track.append(addon_top_80med_1Track)

addon_backgrounds_80med_lowPT_1Track = []
addon_backgrounds_80med_lowPT_1Track.append(addon_data_80med_lowPT_1Track)
addon_backgrounds_80med_lowPT_1Track.append(addon_Wjets_80med_lowPT_1Track)
addon_backgrounds_80med_lowPT_1Track.append(addon_Zlljets_80med_lowPT_1Track)
addon_backgrounds_80med_lowPT_1Track.append(addon_top_80med_lowPT_1Track)

addon_backgrounds_80med_highPT_1Track = []
addon_backgrounds_80med_highPT_1Track.append(addon_data_80med_highPT_1Track)
addon_backgrounds_80med_highPT_1Track.append(addon_Wjets_80med_highPT_1Track)
addon_backgrounds_80med_highPT_1Track.append(addon_Zlljets_80med_highPT_1Track)
addon_backgrounds_80med_highPT_1Track.append(addon_top_80med_highPT_1Track)

addon_backgrounds_80L1TAU60med_1Track = []
addon_backgrounds_80L1TAU60med_1Track.append(addon_data_80L1TAU60med_1Track)
addon_backgrounds_80L1TAU60med_1Track.append(addon_Wjets_80L1TAU60med_1Track)
addon_backgrounds_80L1TAU60med_1Track.append(addon_Zlljets_80L1TAU60med_1Track)
addon_backgrounds_80L1TAU60med_1Track.append(addon_top_80L1TAU60med_1Track)

addon_backgrounds_80L1TAU60med_lowPT_1Track = []
addon_backgrounds_80L1TAU60med_lowPT_1Track.append(addon_data_80L1TAU60med_lowPT_1Track)
addon_backgrounds_80L1TAU60med_lowPT_1Track.append(addon_Wjets_80L1TAU60med_lowPT_1Track)
addon_backgrounds_80L1TAU60med_lowPT_1Track.append(addon_Zlljets_80L1TAU60med_lowPT_1Track)
addon_backgrounds_80L1TAU60med_lowPT_1Track.append(addon_top_80L1TAU60med_lowPT_1Track)

addon_backgrounds_80L1TAU60med_highPT_1Track = []
addon_backgrounds_80L1TAU60med_highPT_1Track.append(addon_data_80L1TAU60med_highPT_1Track)
addon_backgrounds_80L1TAU60med_highPT_1Track.append(addon_Wjets_80L1TAU60med_highPT_1Track)
addon_backgrounds_80L1TAU60med_highPT_1Track.append(addon_Zlljets_80L1TAU60med_highPT_1Track)
addon_backgrounds_80L1TAU60med_highPT_1Track.append(addon_top_80L1TAU60med_highPT_1Track)

addon_backgrounds_125med_1Track = []
addon_backgrounds_125med_1Track.append(addon_data_125med_1Track)
addon_backgrounds_125med_1Track.append(addon_Wjets_125med_1Track)
addon_backgrounds_125med_1Track.append(addon_Zlljets_125med_1Track)
addon_backgrounds_125med_1Track.append(addon_top_125med_1Track)

addon_backgrounds_125med_lowPT_1Track = []
addon_backgrounds_125med_lowPT_1Track.append(addon_data_125med_lowPT_1Track)
addon_backgrounds_125med_lowPT_1Track.append(addon_Wjets_125med_lowPT_1Track)
addon_backgrounds_125med_lowPT_1Track.append(addon_Zlljets_125med_lowPT_1Track)
addon_backgrounds_125med_lowPT_1Track.append(addon_top_125med_lowPT_1Track)

addon_backgrounds_125med_highPT_1Track = []
addon_backgrounds_125med_highPT_1Track.append(addon_data_125med_highPT_1Track)
addon_backgrounds_125med_highPT_1Track.append(addon_Wjets_125med_highPT_1Track)
addon_backgrounds_125med_highPT_1Track.append(addon_Zlljets_125med_highPT_1Track)
addon_backgrounds_125med_highPT_1Track.append(addon_top_125med_highPT_1Track)

addon_backgrounds_160med_1Track = []
addon_backgrounds_160med_1Track.append(addon_data_160med_1Track)
addon_backgrounds_160med_1Track.append(addon_Wjets_160med_1Track)
addon_backgrounds_160med_1Track.append(addon_Zlljets_160med_1Track)
addon_backgrounds_160med_1Track.append(addon_top_160med_1Track)

addon_backgrounds_L1TAU12IMmed_1Track = []
addon_backgrounds_L1TAU12IMmed_1Track.append(addon_data_L1TAU12IMmed_1Track)
addon_backgrounds_L1TAU12IMmed_1Track.append(addon_Wjets_L1TAU12IMmed_1Track)
addon_backgrounds_L1TAU12IMmed_1Track.append(addon_Zlljets_L1TAU12IMmed_1Track)
addon_backgrounds_L1TAU12IMmed_1Track.append(addon_top_L1TAU12IMmed_1Track)

addon_backgrounds_160med_lowPT_1Track = []
addon_backgrounds_160med_lowPT_1Track.append(addon_data_160med_lowPT_1Track)
addon_backgrounds_160med_lowPT_1Track.append(addon_Wjets_160med_lowPT_1Track)
addon_backgrounds_160med_lowPT_1Track.append(addon_Zlljets_160med_lowPT_1Track)
addon_backgrounds_160med_lowPT_1Track.append(addon_top_160med_lowPT_1Track)

addon_backgrounds_160med_highPT_1Track = []
addon_backgrounds_160med_highPT_1Track.append(addon_data_160med_highPT_1Track)
addon_backgrounds_160med_highPT_1Track.append(addon_Wjets_160med_highPT_1Track)
addon_backgrounds_160med_highPT_1Track.append(addon_Zlljets_160med_highPT_1Track)
addon_backgrounds_160med_highPT_1Track.append(addon_top_160med_highPT_1Track)

addon_backgrounds_L1TAU12IMmed_lowPT_1Track = []
addon_backgrounds_L1TAU12IMmed_lowPT_1Track.append(addon_data_L1TAU12IMmed_lowPT_1Track)
addon_backgrounds_L1TAU12IMmed_lowPT_1Track.append(addon_Wjets_L1TAU12IMmed_lowPT_1Track)
addon_backgrounds_L1TAU12IMmed_lowPT_1Track.append(addon_Zlljets_L1TAU12IMmed_lowPT_1Track)
addon_backgrounds_L1TAU12IMmed_lowPT_1Track.append(addon_top_L1TAU12IMmed_lowPT_1Track)

addon_backgrounds_L1TAU12IMmed_highPT_1Track = []
addon_backgrounds_L1TAU12IMmed_highPT_1Track.append(addon_data_L1TAU12IMmed_highPT_1Track)
addon_backgrounds_L1TAU12IMmed_highPT_1Track.append(addon_Wjets_L1TAU12IMmed_highPT_1Track)
addon_backgrounds_L1TAU12IMmed_highPT_1Track.append(addon_Zlljets_L1TAU12IMmed_highPT_1Track)
addon_backgrounds_L1TAU12IMmed_highPT_1Track.append(addon_top_L1TAU12IMmed_highPT_1Track)

addon_backgrounds_ptonly_1Track = []
addon_backgrounds_ptonly_1Track.append(addon_data_ptonly_1Track)
addon_backgrounds_ptonly_1Track.append(addon_Wjets_ptonly_1Track)
addon_backgrounds_ptonly_1Track.append(addon_Zlljets_ptonly_1Track)
addon_backgrounds_ptonly_1Track.append(addon_top_ptonly_1Track)

addon_backgrounds_ptonly_lowPT_1Track = []
addon_backgrounds_ptonly_lowPT_1Track.append(addon_data_ptonly_lowPT_1Track)
addon_backgrounds_ptonly_lowPT_1Track.append(addon_Wjets_ptonly_lowPT_1Track)
addon_backgrounds_ptonly_lowPT_1Track.append(addon_Zlljets_ptonly_lowPT_1Track)
addon_backgrounds_ptonly_lowPT_1Track.append(addon_top_ptonly_lowPT_1Track)

addon_backgrounds_ptonly_highPT_1Track = []
addon_backgrounds_ptonly_highPT_1Track.append(addon_data_ptonly_highPT_1Track)
addon_backgrounds_ptonly_highPT_1Track.append(addon_Wjets_ptonly_highPT_1Track)
addon_backgrounds_ptonly_highPT_1Track.append(addon_Zlljets_ptonly_highPT_1Track)
addon_backgrounds_ptonly_highPT_1Track.append(addon_top_ptonly_highPT_1Track)

addon_backgrounds_tracktwo_1Track = []
addon_backgrounds_tracktwo_1Track.append(addon_data_tracktwo_1Track)
addon_backgrounds_tracktwo_1Track.append(addon_Wjets_tracktwo_1Track)
addon_backgrounds_tracktwo_1Track.append(addon_Zlljets_tracktwo_1Track)
addon_backgrounds_tracktwo_1Track.append(addon_top_tracktwo_1Track)

addon_backgrounds_tracktwo_lowPT_1Track = []
addon_backgrounds_tracktwo_lowPT_1Track.append(addon_data_tracktwo_lowPT_1Track)
addon_backgrounds_tracktwo_lowPT_1Track.append(addon_Wjets_tracktwo_lowPT_1Track)
addon_backgrounds_tracktwo_lowPT_1Track.append(addon_Zlljets_tracktwo_lowPT_1Track)
addon_backgrounds_tracktwo_lowPT_1Track.append(addon_top_tracktwo_lowPT_1Track)

addon_backgrounds_tracktwo_highPT_1Track = []
addon_backgrounds_tracktwo_highPT_1Track.append(addon_data_tracktwo_highPT_1Track)
addon_backgrounds_tracktwo_highPT_1Track.append(addon_Wjets_tracktwo_highPT_1Track)
addon_backgrounds_tracktwo_highPT_1Track.append(addon_Zlljets_tracktwo_highPT_1Track)
addon_backgrounds_tracktwo_highPT_1Track.append(addon_top_tracktwo_highPT_1Track)

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

addon_backgrounds_50L1TAU12med_3Track = []
addon_backgrounds_50L1TAU12med_3Track.append(addon_data_50L1TAU12med_3Track)
addon_backgrounds_50L1TAU12med_3Track.append(addon_Wjets_50L1TAU12med_3Track)
addon_backgrounds_50L1TAU12med_3Track.append(addon_Zlljets_50L1TAU12med_3Track)
addon_backgrounds_50L1TAU12med_3Track.append(addon_top_50L1TAU12med_3Track)

addon_backgrounds_50L1TAU12med_lowPT_3Track = []
addon_backgrounds_50L1TAU12med_lowPT_3Track.append(addon_data_50L1TAU12med_lowPT_3Track)
addon_backgrounds_50L1TAU12med_lowPT_3Track.append(addon_Wjets_50L1TAU12med_lowPT_3Track)
addon_backgrounds_50L1TAU12med_lowPT_3Track.append(addon_Zlljets_50L1TAU12med_lowPT_3Track)
addon_backgrounds_50L1TAU12med_lowPT_3Track.append(addon_top_50L1TAU12med_lowPT_3Track)

addon_backgrounds_50L1TAU12med_highPT_3Track = []
addon_backgrounds_50L1TAU12med_highPT_3Track.append(addon_data_50L1TAU12med_highPT_3Track)
addon_backgrounds_50L1TAU12med_highPT_3Track.append(addon_Wjets_50L1TAU12med_highPT_3Track)
addon_backgrounds_50L1TAU12med_highPT_3Track.append(addon_Zlljets_50L1TAU12med_highPT_3Track)
addon_backgrounds_50L1TAU12med_highPT_3Track.append(addon_top_50L1TAU12med_highPT_3Track)

addon_backgrounds_80med_3Track = []
addon_backgrounds_80med_3Track.append(addon_data_80med_3Track)
addon_backgrounds_80med_3Track.append(addon_Wjets_80med_3Track)
addon_backgrounds_80med_3Track.append(addon_Zlljets_80med_3Track)
addon_backgrounds_80med_3Track.append(addon_top_80med_3Track)

addon_backgrounds_80med_lowPT_3Track = []
addon_backgrounds_80med_lowPT_3Track.append(addon_data_80med_lowPT_3Track)
addon_backgrounds_80med_lowPT_3Track.append(addon_Wjets_80med_lowPT_3Track)
addon_backgrounds_80med_lowPT_3Track.append(addon_Zlljets_80med_lowPT_3Track)
addon_backgrounds_80med_lowPT_3Track.append(addon_top_80med_lowPT_3Track)

addon_backgrounds_80med_highPT_3Track = []
addon_backgrounds_80med_highPT_3Track.append(addon_data_80med_highPT_3Track)
addon_backgrounds_80med_highPT_3Track.append(addon_Wjets_80med_highPT_3Track)
addon_backgrounds_80med_highPT_3Track.append(addon_Zlljets_80med_highPT_3Track)
addon_backgrounds_80med_highPT_3Track.append(addon_top_80med_highPT_3Track)

addon_backgrounds_80L1TAU60med_3Track = []
addon_backgrounds_80L1TAU60med_3Track.append(addon_data_80L1TAU60med_3Track)
addon_backgrounds_80L1TAU60med_3Track.append(addon_Wjets_80L1TAU60med_3Track)
addon_backgrounds_80L1TAU60med_3Track.append(addon_Zlljets_80L1TAU60med_3Track)
addon_backgrounds_80L1TAU60med_3Track.append(addon_top_80L1TAU60med_3Track)

addon_backgrounds_80L1TAU60med_lowPT_3Track = []
addon_backgrounds_80L1TAU60med_lowPT_3Track.append(addon_data_80L1TAU60med_lowPT_3Track)
addon_backgrounds_80L1TAU60med_lowPT_3Track.append(addon_Wjets_80L1TAU60med_lowPT_3Track)
addon_backgrounds_80L1TAU60med_lowPT_3Track.append(addon_Zlljets_80L1TAU60med_lowPT_3Track)
addon_backgrounds_80L1TAU60med_lowPT_3Track.append(addon_top_80L1TAU60med_lowPT_3Track)

addon_backgrounds_80L1TAU60med_highPT_3Track = []
addon_backgrounds_80L1TAU60med_highPT_3Track.append(addon_data_80L1TAU60med_highPT_3Track)
addon_backgrounds_80L1TAU60med_highPT_3Track.append(addon_Wjets_80L1TAU60med_highPT_3Track)
addon_backgrounds_80L1TAU60med_highPT_3Track.append(addon_Zlljets_80L1TAU60med_highPT_3Track)
addon_backgrounds_80L1TAU60med_highPT_3Track.append(addon_top_80L1TAU60med_highPT_3Track)

addon_backgrounds_125med_3Track = []
addon_backgrounds_125med_3Track.append(addon_data_125med_3Track)
addon_backgrounds_125med_3Track.append(addon_Wjets_125med_3Track)
addon_backgrounds_125med_3Track.append(addon_Zlljets_125med_3Track)
addon_backgrounds_125med_3Track.append(addon_top_125med_3Track)

addon_backgrounds_125med_lowPT_3Track = []
addon_backgrounds_125med_lowPT_3Track.append(addon_data_125med_lowPT_3Track)
addon_backgrounds_125med_lowPT_3Track.append(addon_Wjets_125med_lowPT_3Track)
addon_backgrounds_125med_lowPT_3Track.append(addon_Zlljets_125med_lowPT_3Track)
addon_backgrounds_125med_lowPT_3Track.append(addon_top_125med_lowPT_3Track)

addon_backgrounds_125med_highPT_3Track = []
addon_backgrounds_125med_highPT_3Track.append(addon_data_125med_highPT_3Track)
addon_backgrounds_125med_highPT_3Track.append(addon_Wjets_125med_highPT_3Track)
addon_backgrounds_125med_highPT_3Track.append(addon_Zlljets_125med_highPT_3Track)
addon_backgrounds_125med_highPT_3Track.append(addon_top_125med_highPT_3Track)

addon_backgrounds_160med_3Track = []
addon_backgrounds_160med_3Track.append(addon_data_160med_3Track)
addon_backgrounds_160med_3Track.append(addon_Wjets_160med_3Track)
addon_backgrounds_160med_3Track.append(addon_Zlljets_160med_3Track)
addon_backgrounds_160med_3Track.append(addon_top_160med_3Track)

addon_backgrounds_160med_lowPT_3Track = []
addon_backgrounds_160med_lowPT_3Track.append(addon_data_160med_lowPT_3Track)
addon_backgrounds_160med_lowPT_3Track.append(addon_Wjets_160med_lowPT_3Track)
addon_backgrounds_160med_lowPT_3Track.append(addon_Zlljets_160med_lowPT_3Track)
addon_backgrounds_160med_lowPT_3Track.append(addon_top_160med_lowPT_3Track)

addon_backgrounds_160med_highPT_3Track = []
addon_backgrounds_160med_highPT_3Track.append(addon_data_160med_highPT_3Track)
addon_backgrounds_160med_highPT_3Track.append(addon_Wjets_160med_highPT_3Track)
addon_backgrounds_160med_highPT_3Track.append(addon_Zlljets_160med_highPT_3Track)
addon_backgrounds_160med_highPT_3Track.append(addon_top_160med_highPT_3Track)

addon_backgrounds_L1TAU12IMmed_3Track = []
addon_backgrounds_L1TAU12IMmed_3Track.append(addon_data_L1TAU12IMmed_3Track)
addon_backgrounds_L1TAU12IMmed_3Track.append(addon_Wjets_L1TAU12IMmed_3Track)
addon_backgrounds_L1TAU12IMmed_3Track.append(addon_Zlljets_L1TAU12IMmed_3Track)
addon_backgrounds_L1TAU12IMmed_3Track.append(addon_top_L1TAU12IMmed_3Track)

addon_backgrounds_L1TAU12IMmed_lowPT_3Track = []
addon_backgrounds_L1TAU12IMmed_lowPT_3Track.append(addon_data_L1TAU12IMmed_lowPT_3Track)
addon_backgrounds_L1TAU12IMmed_lowPT_3Track.append(addon_Wjets_L1TAU12IMmed_lowPT_3Track)
addon_backgrounds_L1TAU12IMmed_lowPT_3Track.append(addon_Zlljets_L1TAU12IMmed_lowPT_3Track)
addon_backgrounds_L1TAU12IMmed_lowPT_3Track.append(addon_top_L1TAU12IMmed_lowPT_3Track)

addon_backgrounds_L1TAU12IMmed_highPT_3Track = []
addon_backgrounds_L1TAU12IMmed_highPT_3Track.append(addon_data_L1TAU12IMmed_highPT_3Track)
addon_backgrounds_L1TAU12IMmed_highPT_3Track.append(addon_Wjets_L1TAU12IMmed_highPT_3Track)
addon_backgrounds_L1TAU12IMmed_highPT_3Track.append(addon_Zlljets_L1TAU12IMmed_highPT_3Track)
addon_backgrounds_L1TAU12IMmed_highPT_3Track.append(addon_top_L1TAU12IMmed_highPT_3Track)

addon_backgrounds_ptonly_3Track = []
addon_backgrounds_ptonly_3Track.append(addon_data_ptonly_3Track)
addon_backgrounds_ptonly_3Track.append(addon_Wjets_ptonly_3Track)
addon_backgrounds_ptonly_3Track.append(addon_Zlljets_ptonly_3Track)
addon_backgrounds_ptonly_3Track.append(addon_top_ptonly_3Track)

addon_backgrounds_ptonly_lowPT_3Track = []
addon_backgrounds_ptonly_lowPT_3Track.append(addon_data_ptonly_lowPT_3Track)
addon_backgrounds_ptonly_lowPT_3Track.append(addon_Wjets_ptonly_lowPT_3Track)
addon_backgrounds_ptonly_lowPT_3Track.append(addon_Zlljets_ptonly_lowPT_3Track)
addon_backgrounds_ptonly_lowPT_3Track.append(addon_top_ptonly_lowPT_3Track)

addon_backgrounds_ptonly_highPT_3Track = []
addon_backgrounds_ptonly_highPT_3Track.append(addon_data_ptonly_highPT_3Track)
addon_backgrounds_ptonly_highPT_3Track.append(addon_Wjets_ptonly_highPT_3Track)
addon_backgrounds_ptonly_highPT_3Track.append(addon_Zlljets_ptonly_highPT_3Track)
addon_backgrounds_ptonly_highPT_3Track.append(addon_top_ptonly_highPT_3Track)

addon_backgrounds_tracktwo_3Track = []
addon_backgrounds_tracktwo_3Track.append(addon_data_tracktwo_3Track)
addon_backgrounds_tracktwo_3Track.append(addon_Wjets_tracktwo_3Track)
addon_backgrounds_tracktwo_3Track.append(addon_Zlljets_tracktwo_3Track)
addon_backgrounds_tracktwo_3Track.append(addon_top_tracktwo_3Track)

addon_backgrounds_tracktwo_lowPT_3Track = []
addon_backgrounds_tracktwo_lowPT_3Track.append(addon_data_tracktwo_lowPT_3Track)
addon_backgrounds_tracktwo_lowPT_3Track.append(addon_Wjets_tracktwo_lowPT_3Track)
addon_backgrounds_tracktwo_lowPT_3Track.append(addon_Zlljets_tracktwo_lowPT_3Track)
addon_backgrounds_tracktwo_lowPT_3Track.append(addon_top_tracktwo_lowPT_3Track)

addon_backgrounds_tracktwo_highPT_3Track = []
addon_backgrounds_tracktwo_highPT_3Track.append(addon_data_tracktwo_highPT_3Track)
addon_backgrounds_tracktwo_highPT_3Track.append(addon_Wjets_tracktwo_highPT_3Track)
addon_backgrounds_tracktwo_highPT_3Track.append(addon_Zlljets_tracktwo_highPT_3Track)
addon_backgrounds_tracktwo_highPT_3Track.append(addon_top_tracktwo_highPT_3Track)


#---------------------------
# Regions for bkg estimation
#---------------------------

# k-factors

kf_regions = {}
kf_regions_highPT = {}
kf_regions_lowPT = {}
kf_regions_OS_no_cuts = {}

# Triggers

kf_regions_25med = {}
kf_regions_25med_lowPT = {}
kf_regions_25med_highPT = {}

kf_regions_35med = {}
kf_regions_35med_lowPT = {}
kf_regions_35med_highPT = {}

kf_regions_50L1TAU12med = {}
kf_regions_50L1TAU12med_lowPT = {}
kf_regions_50L1TAU12med_highPT = {}

kf_regions_80med = {}
kf_regions_80med_lowPT = {}
kf_regions_80med_highPT = {}

kf_regions_80L1TAU60med = {}
kf_regions_80L1TAU60med_lowPT = {}
kf_regions_80L1TAU60med_highPT = {}

kf_regions_125med = {}
kf_regions_125med_lowPT = {}
kf_regions_125med_highPT = {}

kf_regions_160med = {}
kf_regions_160med_lowPT = {}
kf_regions_160med_highPT = {}

kf_regions_L1TAU12IMmed = {}
kf_regions_L1TAU12IMmed_lowPT = {}
kf_regions_L1TAU12IMmed_highPT = {}

kf_regions_ptonly = {}
kf_regions_ptonly_lowPT = {}
kf_regions_ptonly_highPT = {}

kf_regions_tracktwo = {}
kf_regions_tracktwo_lowPT = {}
kf_regions_tracktwo_highPT = {}

kf_regions[samples.Wjets]	= {"OS":"Wjets_OS", "SS":"Wjets_SS","ncuts":3}
kf_regions_highPT[samples.Wjets]  = {"OS":"Wjets_OS_highPT", "SS":"Wjets_SS_highPT", "ncuts":4}
kf_regions_lowPT[samples.Wjets]   = {"OS":"Wjets_OS_lowPT", "SS":"Wjets_SS_lowPT", "ncuts":4}

kf_regions_OS_no_cuts[samples.Wjets] = {"OS":"Wjets_OS", "SS":"Wjets_SS","ncuts":3}

kf_regions_25med[samples.Wjets]	= {"OS":"Wjets_OS_25med", "SS":"Wjets_SS_25med","ncuts":4}
kf_regions_25med_lowPT[samples.Wjets]	= {"OS":"Wjets_OS_25med_lowPT", "SS":"Wjets_SS_25med_lowPT","ncuts":5}
kf_regions_25med_highPT[samples.Wjets]	= {"OS":"Wjets_OS_25med_highPT", "SS":"Wjets_SS_25med_highPT","ncuts":5}

kf_regions_35med[samples.Wjets]	= {"OS":"Wjets_OS_35med", "SS":"Wjets_SS_35med","ncuts":4}
kf_regions_35med_lowPT[samples.Wjets]	= {"OS":"Wjets_OS_35med_lowPT", "SS":"Wjets_SS_35med_lowPT","ncuts":5}
kf_regions_35med_highPT[samples.Wjets]	= {"OS":"Wjets_OS_35med_highPT", "SS":"Wjets_SS_35med_highPT","ncuts":5}

kf_regions_50L1TAU12med[samples.Wjets]	= {"OS":"Wjets_OS_50L1TAU12med", "SS":"Wjets_SS_50L1TAU12med","ncuts":4}
kf_regions_50L1TAU12med_lowPT[samples.Wjets]	= {"OS":"Wjets_OS_50L1TAU12med_lowPT", "SS":"Wjets_SS_50L1TAU12med_lowPT","ncuts":5}
kf_regions_50L1TAU12med_highPT[samples.Wjets]	= {"OS":"Wjets_OS_50L1TAU12med_highPT", "SS":"Wjets_SS_50L1TAU12med_highPT","ncuts":5}

kf_regions_80med[samples.Wjets]	= {"OS":"Wjets_OS_80med", "SS":"Wjets_SS_80med","ncuts":4}
kf_regions_80med_lowPT[samples.Wjets]	= {"OS":"Wjets_OS_80med_lowPT", "SS":"Wjets_SS_80med_lowPT","ncuts":5}
kf_regions_80med_highPT[samples.Wjets]	= {"OS":"Wjets_OS_80med_highPT", "SS":"Wjets_SS_80med_highPT","ncuts":5}

kf_regions_80L1TAU60med[samples.Wjets]	= {"OS":"Wjets_OS_80L1TAU60med", "SS":"Wjets_SS_80L1TAU60med","ncuts":4}
kf_regions_80L1TAU60med_lowPT[samples.Wjets]	= {"OS":"Wjets_OS_80L1TAU60med_lowPT", "SS":"Wjets_SS_80L1TAU60med_lowPT","ncuts":5}
kf_regions_80L1TAU60med_highPT[samples.Wjets]	= {"OS":"Wjets_OS_80L1TAU60med_highPT", "SS":"Wjets_SS_80L1TAU60med_highPT","ncuts":5}

kf_regions_125med[samples.Wjets]	= {"OS":"Wjets_OS_125med", "SS":"Wjets_SS_125med","ncuts":4}
kf_regions_125med_lowPT[samples.Wjets]	= {"OS":"Wjets_OS_125med_lowPT", "SS":"Wjets_SS_125med_lowPT","ncuts":5}
kf_regions_125med_highPT[samples.Wjets]	= {"OS":"Wjets_OS_125med_highPT", "SS":"Wjets_SS_125med_highPT","ncuts":5}

kf_regions_160med[samples.Wjets]	= {"OS":"Wjets_OS_160med", "SS":"Wjets_SS_160med","ncuts":4}
kf_regions_160med_lowPT[samples.Wjets]	= {"OS":"Wjets_OS_160med_lowPT", "SS":"Wjets_SS_160med_lowPT","ncuts":5}
kf_regions_160med_highPT[samples.Wjets]	= {"OS":"Wjets_OS_160med_highPT", "SS":"Wjets_SS_160med_highPT","ncuts":5}

kf_regions_L1TAU12IMmed[samples.Wjets]	= {"OS":"Wjets_OS_L1TAU12IMmed", "SS":"Wjets_SS_L1TAU12IMmed","ncuts":4}
kf_regions_L1TAU12IMmed_lowPT[samples.Wjets]	= {"OS":"Wjets_OS_L1TAU12IMmed_lowPT", "SS":"Wjets_SS_L1TAU12IMmed_lowPT","ncuts":5}
kf_regions_L1TAU12IMmed_highPT[samples.Wjets]	= {"OS":"Wjets_OS_L1TAU12IMmed_highPT", "SS":"Wjets_SS_L1TAU12IMmed_highPT","ncuts":5}

kf_regions_ptonly[samples.Wjets]	= {"OS":"Wjets_OS_ptonly", "SS":"Wjets_SS_ptonly","ncuts":4}
kf_regions_ptonly_lowPT[samples.Wjets]	= {"OS":"Wjets_OS_ptonly_lowPT", "SS":"Wjets_SS_ptonly_lowPT","ncuts":5}
kf_regions_ptonly_highPT[samples.Wjets]	= {"OS":"Wjets_OS_ptonly_highPT", "SS":"Wjets_SS_ptonly_highPT","ncuts":5}


kf_regions_tracktwo[samples.Wjets]	= {"OS":"Wjets_OS_tracktwo", "SS":"Wjets_SS_tracktwo","ncuts":4}
kf_regions_tracktwo_lowPT[samples.Wjets]	= {"OS":"Wjets_OS_tracktwo_lowPT", "SS":"Wjets_SS_tracktwo_lowPT","ncuts":5}
kf_regions_tracktwo_highPT[samples.Wjets]	= {"OS":"Wjets_OS_tracktwo_highPT", "SS":"Wjets_SS_tracktwo_highPT","ncuts":5}

#SYSTEMATICS

if options.kwsys:
	print "*****************************************"
        print "*********** kw sys", options.kwsys
        print "*****************************************" 

	#kf_regions[samples.Wjets]	= {"OS":"Wjets_OS_MTrans"+str(options.kwsys)+"_MTrans"+str(options.kwsys), "SS":"Wjets_SS"_MTrans+str(options.kwsys),"ncuts":4}
	#kf_regions_OS_no_cuts[samples.Wjets] = {"OS":"Wjets_OS_MTrans"+str(options.kwsys)+"_MTrans"+str(options.kwsys), "SS":"Wjets_SS_MTrans"+str(options.kwsys)+"_MTrans"+str(options.kwsys),"ncuts":4}
	#kf_regions_25med[samples.Wjets]	= {"OS":"Wjets_OS_MTrans"+str(options.kwsys)+"_25med", "SS":"Wjets_SS_MTrans"+str(options.kwsys)+"_25med","ncuts":5}
	#kf_regions_35med[samples.Wjets]	= {"OS":"Wjets_OS_MTrans"+str(options.kwsys)+"_35med", "SS":"Wjets_SS_MTrans"+str(options.kwsys)+"_35med","ncuts":5}

	kf_regions_25med_lowPT[samples.Wjets]	= {"OS":"Wjets_OS_MTrans"+str(options.kwsys)+"_25med_lowPT", "SS":"Wjets_SS_MTrans"+str(options.kwsys)+"_25med_lowPT","ncuts":6}
	kf_regions_25med_highPT[samples.Wjets]	= {"OS":"Wjets_OS_MTrans"+str(options.kwsys)+"_25med_highPT", "SS":"Wjets_SS_MTrans"+str(options.kwsys)+"_25med_highPT","ncuts":6}
	#kf_regions_35med_lowPT[samples.Wjets]	= {"OS":"Wjets_OS_MTrans"+str(options.kwsys)+"_35med_lowPT", "SS":"Wjets_SS_MTrans"+str(options.kwsys)+"_35med_lowPT","ncuts":6}
	#kf_regions_35med_highPT[samples.Wjets]	= {"OS":"Wjets_OS_MTrans"+str(options.kwsys)+"_35med_highPT", "SS":"Wjets_SS_MTrans"+str(options.kwsys)+"_35med_highPT","ncuts":6}

	kf_regions_highPT[samples.Wjets]  = {"OS":"Wjets_OS_MTrans"+str(options.kwsys)+"_highPT", "SS":"Wjets_SS_MTrans"+str(options.kwsys)+"_highPT", "ncuts":5}
	kf_regions_lowPT[samples.Wjets]   = {"OS":"Wjets_OS_MTrans"+str(options.kwsys)+"_lowPT", "SS":"Wjets_SS_MTrans"+str(options.kwsys)+"_lowPT", "ncuts":5}

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

kf_regions_50L1TAU12med_1Track = {}
kf_regions_50L1TAU12med_lowPT_1Track  = {}
kf_regions_50L1TAU12med_highPT_1Track  = {}

kf_regions_80med_1Track = {}
kf_regions_80med_lowPT_1Track  = {}
kf_regions_80med_highPT_1Track  = {}

kf_regions_80L1TAU60med_1Track = {}
kf_regions_80L1TAU60med_lowPT_1Track  = {}
kf_regions_80L1TAU60med_highPT_1Track  = {}

kf_regions_125med_1Track = {}
kf_regions_125med_lowPT_1Track  = {}
kf_regions_125med_highPT_1Track  = {}

kf_regions_160med_1Track = {}
kf_regions_160med_lowPT_1Track  = {}
kf_regions_160med_highPT_1Track  = {}

kf_regions_L1TAU12IMmed_1Track = {}
kf_regions_L1TAU12IMmed_lowPT_1Track  = {}
kf_regions_L1TAU12IMmed_highPT_1Track  = {}

kf_regions_ptonly_1Track = {}
kf_regions_ptonly_lowPT_1Track  = {}
kf_regions_ptonly_highPT_1Track  = {}

kf_regions_tracktwo_1Track = {}
kf_regions_tracktwo_lowPT_1Track  = {}
kf_regions_tracktwo_highPT_1Track  = {}

kf_regions_1Track[samples.Wjets]	= {"OS":"Wjets_OS_Tau1Track", "SS":"Wjets_SS_Tau1Track","ncuts":4}
kf_regions_highPT_1Track[samples.Wjets]  = {"OS":"Wjets_OS_highPT_Tau1Track", "SS":"Wjets_SS_highPT_Tau1Track", "ncuts":5}
kf_regions_lowPT_1Track[samples.Wjets]   = {"OS":"Wjets_OS_lowPT_Tau1Track", "SS":"Wjets_SS_lowPT_Tau1Track", "ncuts":5}

kf_regions_25med_1Track[samples.Wjets]	= {"OS":"Wjets_OS_25med_Tau1Track", "SS":"Wjets_SS_25med_Tau1Track","ncuts":5}
kf_regions_25med_lowPT_1Track[samples.Wjets]	= {"OS":"Wjets_OS_25med_lowPT_Tau1Track", "SS":"Wjets_SS_25med_lowPT_Tau1Track","ncuts":6}
kf_regions_25med_highPT_1Track[samples.Wjets]	= {"OS":"Wjets_OS_25med_highPT_Tau1Track", "SS":"Wjets_SS_25med_highPT_Tau1Track","ncuts":6}

kf_regions_35med_1Track[samples.Wjets]	= {"OS":"Wjets_OS_35med_Tau1Track", "SS":"Wjets_SS_35med_Tau1Track","ncuts":5}
kf_regions_35med_lowPT_1Track[samples.Wjets]	= {"OS":"Wjets_OS_35med_lowPT_Tau1Track", "SS":"Wjets_SS_35med_lowPT_Tau1Track","ncuts":6}
kf_regions_35med_highPT_1Track[samples.Wjets]	= {"OS":"Wjets_OS_35med_highPT_Tau1Track", "SS":"Wjets_SS_35med_highPT_Tau1Track","ncuts":6}

kf_regions_50L1TAU12med_1Track[samples.Wjets]	= {"OS":"Wjets_OS_50L1TAU12med_Tau1Track", "SS":"Wjets_SS_50L1TAU12med_Tau1Track","ncuts":5}
kf_regions_50L1TAU12med_lowPT_1Track[samples.Wjets]	= {"OS":"Wjets_OS_50L1TAU12med_lowPT_Tau1Track", "SS":"Wjets_SS_50L1TAU12med_lowPT_Tau1Track","ncuts":6}
kf_regions_50L1TAU12med_highPT_1Track[samples.Wjets]	= {"OS":"Wjets_OS_50L1TAU12med_highPT_Tau1Track", "SS":"Wjets_SS_50L1TAU12med_highPT_Tau1Track","ncuts":6}

kf_regions_80med_1Track[samples.Wjets]	= {"OS":"Wjets_OS_80med_Tau1Track", "SS":"Wjets_SS_80med_Tau1Track","ncuts":5}
kf_regions_80med_lowPT_1Track[samples.Wjets]	= {"OS":"Wjets_OS_80med_lowPT_Tau1Track", "SS":"Wjets_SS_80med_lowPT_Tau1Track","ncuts":6}
kf_regions_80med_highPT_1Track[samples.Wjets]	= {"OS":"Wjets_OS_80med_highPT_Tau1Track", "SS":"Wjets_SS_80med_highPT_Tau1Track","ncuts":6}

kf_regions_80L1TAU60med_1Track[samples.Wjets]	= {"OS":"Wjets_OS_80L1TAU60med_Tau1Track", "SS":"Wjets_SS_80L1TAU60med_Tau1Track","ncuts":5}
kf_regions_80L1TAU60med_lowPT_1Track[samples.Wjets]	= {"OS":"Wjets_OS_80L1TAU60med_lowPT_Tau1Track", "SS":"Wjets_SS_80L1TAU60med_lowPT_Tau1Track","ncuts":6}
kf_regions_80L1TAU60med_highPT_1Track[samples.Wjets]	= {"OS":"Wjets_OS_80L1TAU60med_highPT_Tau1Track", "SS":"Wjets_SS_80L1TAU60med_highPT_Tau1Track","ncuts":6}

kf_regions_125med_1Track[samples.Wjets]	= {"OS":"Wjets_OS_125med_Tau1Track", "SS":"Wjets_SS_125med_Tau1Track","ncuts":5}
kf_regions_125med_lowPT_1Track[samples.Wjets]	= {"OS":"Wjets_OS_125med_lowPT_Tau1Track", "SS":"Wjets_SS_125med_lowPT_Tau1Track","ncuts":6}
kf_regions_125med_highPT_1Track[samples.Wjets]	= {"OS":"Wjets_OS_125med_highPT_Tau1Track", "SS":"Wjets_SS_125med_highPT_Tau1Track","ncuts":6}

kf_regions_160med_1Track[samples.Wjets]	= {"OS":"Wjets_OS_160med_Tau1Track", "SS":"Wjets_SS_160med_Tau1Track","ncuts":5}
kf_regions_160med_lowPT_1Track[samples.Wjets]	= {"OS":"Wjets_OS_160med_lowPT_Tau1Track", "SS":"Wjets_SS_160med_lowPT_Tau1Track","ncuts":6}
kf_regions_160med_highPT_1Track[samples.Wjets]	= {"OS":"Wjets_OS_160med_highPT_Tau1Track", "SS":"Wjets_SS_160med_highPT_Tau1Track","ncuts":6}

kf_regions_L1TAU12IMmed_1Track[samples.Wjets]	= {"OS":"Wjets_OS_L1TAU12IMmed_Tau1Track", "SS":"Wjets_SS_L1TAU12IMmed_Tau1Track","ncuts":5}
kf_regions_L1TAU12IMmed_lowPT_1Track[samples.Wjets]	= {"OS":"Wjets_OS_L1TAU12IMmed_lowPT_Tau1Track", "SS":"Wjets_SS_L1TAU12IMmed_lowPT_Tau1Track","ncuts":6}
kf_regions_L1TAU12IMmed_highPT_1Track[samples.Wjets]	= {"OS":"Wjets_OS_L1TAU12IMmed_highPT_Tau1Track", "SS":"Wjets_SS_L1TAU12IMmed_highPT_Tau1Track","ncuts":6}

kf_regions_ptonly_1Track[samples.Wjets]	= {"OS":"Wjets_OS_ptonly_Tau1Track", "SS":"Wjets_SS_ptonly_Tau1Track","ncuts":5}
kf_regions_ptonly_lowPT_1Track[samples.Wjets]	= {"OS":"Wjets_OS_ptonly_lowPT_Tau1Track", "SS":"Wjets_SS_ptonly_lowPT_Tau1Track","ncuts":6}
kf_regions_ptonly_highPT_1Track[samples.Wjets]	= {"OS":"Wjets_OS_ptonly_highPT_Tau1Track", "SS":"Wjets_SS_ptonly_highPT_Tau1Track","ncuts":6}

kf_regions_tracktwo_1Track[samples.Wjets]	= {"OS":"Wjets_OS_tracktwo_Tau1Track", "SS":"Wjets_SS_tracktwo_Tau1Track","ncuts":5}
kf_regions_tracktwo_lowPT_1Track[samples.Wjets]	= {"OS":"Wjets_OS_tracktwo_lowPT_Tau1Track", "SS":"Wjets_SS_tracktwo_lowPT_Tau1Track","ncuts":6}
kf_regions_tracktwo_highPT_1Track[samples.Wjets]	= {"OS":"Wjets_OS_tracktwo_highPT_Tau1Track", "SS":"Wjets_SS_tracktwo_highPT_Tau1Track","ncuts":6}

if options.kwsys:
        print "*****************************************"
        print "*********** kw sys", options.kwsys
        print "*****************************************" 
	
	kf_regions_25med_lowPT_1Track[samples.Wjets]    = {"OS":"Wjets_OS_MTrans"+str(options.kwsys)+"_25med_lowPT_Tau1Track", "SS":"Wjets_SS_MTrans"+str(options.kwsys)+"_25med_lowPT_Tau1Track","ncuts":7}
	kf_regions_25med_highPT_1Track[samples.Wjets]   = {"OS":"Wjets_OS_MTrans"+str(options.kwsys)+"_25med_highPT_Tau1Track", "SS":"Wjets_SS_MTrans"+str(options.kwsys)+"_25med_highPT_Tau1Track","ncuts":7}

	kf_regions_35med_lowPT_1Track[samples.Wjets]    = {"OS":"Wjets_OS_MTrans"+str(options.kwsys)+"_35med_lowPT_Tau1Track", "SS":"Wjets_SS_MTrans"+str(options.kwsys)+"_35med_lowPT_Tau1Track","ncuts":7}
	kf_regions_35med_highPT_1Track[samples.Wjets]   = {"OS":"Wjets_OS_MTrans"+str(options.kwsys)+"_35med_highPT_Tau1Track", "SS":"Wjets_SS_MTrans"+str(options.kwsys)+"_35med_highPT_Tau1Track","ncuts":7}

	kf_regions_50L1TAU12med_lowPT_1Track[samples.Wjets]    = {"OS":"Wjets_OS_MTrans"+str(options.kwsys)+"_50L1TAU12med_lowPT_Tau1Track", "SS":"Wjets_SS_MTrans"+str(options.kwsys)+"_50L1TAU12med_lowPT_Tau1Track","ncuts":7}
	kf_regions_50L1TAU12med_highPT_1Track[samples.Wjets]   = {"OS":"Wjets_OS_MTrans"+str(options.kwsys)+"_50L1TAU12med_highPT_Tau1Track", "SS":"Wjets_SS_MTrans"+str(options.kwsys)+"_50L1TAU12med_highPT_Tau1Track","ncuts":7}

	kf_regions_80med_lowPT_1Track[samples.Wjets]    = {"OS":"Wjets_OS_MTrans"+str(options.kwsys)+"_80med_lowPT_Tau1Track", "SS":"Wjets_SS_MTrans"+str(options.kwsys)+"_80med_lowPT_Tau1Track","ncuts":7}
	kf_regions_80med_highPT_1Track[samples.Wjets]   = {"OS":"Wjets_OS_MTrans"+str(options.kwsys)+"_80med_highPT_Tau1Track", "SS":"Wjets_SS_MTrans"+str(options.kwsys)+"_80med_highPT_Tau1Track","ncuts":7}

	kf_regions_80L1TAU60med_lowPT_1Track[samples.Wjets]    = {"OS":"Wjets_OS_MTrans"+str(options.kwsys)+"_80L1TAU60med_lowPT_Tau1Track", "SS":"Wjets_SS_MTrans"+str(options.kwsys)+"_80L1TAU60med_lowPT_Tau1Track","ncuts":7}
	kf_regions_80L1TAU60med_highPT_1Track[samples.Wjets]   = {"OS":"Wjets_OS_MTrans"+str(options.kwsys)+"_80L1TAU60med_highPT_Tau1Track", "SS":"Wjets_SS_MTrans"+str(options.kwsys)+"_80L1TAU60med_highPT_Tau1Track","ncuts":7}

	kf_regions_125med_lowPT_1Track[samples.Wjets]    = {"OS":"Wjets_OS_MTrans"+str(options.kwsys)+"_125med_lowPT_Tau1Track", "SS":"Wjets_SS_MTrans"+str(options.kwsys)+"_125med_lowPT_Tau1Track","ncuts":7}
	kf_regions_125med_highPT_1Track[samples.Wjets]   = {"OS":"Wjets_OS_MTrans"+str(options.kwsys)+"_125med_highPT_Tau1Track", "SS":"Wjets_SS_MTrans"+str(options.kwsys)+"_125med_highPT_Tau1Track","ncuts":7}

	kf_regions_160med_lowPT_1Track[samples.Wjets]    = {"OS":"Wjets_OS_MTrans"+str(options.kwsys)+"_160med_lowPT_Tau1Track", "SS":"Wjets_SS_MTrans"+str(options.kwsys)+"_160med_lowPT_Tau1Track","ncuts":7}
	kf_regions_160med_highPT_1Track[samples.Wjets]   = {"OS":"Wjets_OS_MTrans"+str(options.kwsys)+"_160med_highPT_Tau1Track", "SS":"Wjets_SS_MTrans"+str(options.kwsys)+"_160med_highPT_Tau1Track","ncuts":7}

	kf_regions_L1TAU12IMmed_lowPT_1Track[samples.Wjets]    = {"OS":"Wjets_OS_MTrans"+str(options.kwsys)+"_L1TAU12IMmed_lowPT_Tau1Track", "SS":"Wjets_SS_MTrans"+str(options.kwsys)+"_L1TAU12IMmed_lowPT_Tau1Track","ncuts":7}
	kf_regions_L1TAU12IMmed_highPT_1Track[samples.Wjets]   = {"OS":"Wjets_OS_MTrans"+str(options.kwsys)+"_L1TAU12IMmed_highPT_Tau1Track", "SS":"Wjets_SS_MTrans"+str(options.kwsys)+"_L1TAU12IMmed_highPT_Tau1Track","ncuts":7}

	kf_regions_highPT_1Track[samples.Wjets]  = {"OS":"Wjets_OS_MTrans"+str(options.kwsys)+"_highPT_Tau1Track", "SS":"Wjets_SS_MTrans"+str(options.kwsys)+"_highPT_Tau1Track", "ncuts":6}
	kf_regions_lowPT_1Track[samples.Wjets]   = {"OS":"Wjets_OS_MTrans"+str(options.kwsys)+"_lowPT_Tau1Track", "SS":"Wjets_SS_MTrans"+str(options.kwsys)+"_lowPT_Tau1Track", "ncuts":6}
	print "Wjets_OS_MTrans"+str(options.kwsys)+"_highPT_Tau1Track", "Wjets_SS_MTrans"+str(options.kwsys)+"_highPT_Tau1Track"

	kf_regions_ptonly_lowPT_1Track[samples.Wjets]    = {"OS":"Wjets_OS_MTrans"+str(options.kwsys)+"_ptonlymed_lowPT1Track", "SS":"Wjets_SS_MTrans"+str(options.kwsys)+"_ptonlymed_lowPT1Track","ncuts":7}
	kf_regions_ptonly_highPT_1Track[samples.Wjets]   = {"OS":"Wjets_OS_MTrans"+str(options.kwsys)+"_ptonlymed_highPT1Track", "SS":"Wjets_SS_MTrans"+str(options.kwsys)+"_ptonlymed_highPT1Track","ncuts":7}

	kf_regions_tracktwo_lowPT_1Track[samples.Wjets]    = {"OS":"Wjets_OS_MTrans"+str(options.kwsys)+"_tracktwomed_lowPT1Track", "SS":"Wjets_SS_MTrans"+str(options.kwsys)+"_tracktwomed_lowPT1Track","ncuts":7}
	kf_regions_tracktwo_highPT_1Track[samples.Wjets]   = {"OS":"Wjets_OS_MTrans"+str(options.kwsys)+"_tracktwomed_highPT1Track", "SS":"Wjets_SS_MTrans"+str(options.kwsys)+"_tracktwomed_highPT1Track","ncuts":7}

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

kf_regions_50L1TAU12med_3Track = {}
kf_regions_50L1TAU12med_lowPT_3Track  = {}
kf_regions_50L1TAU12med_highPT_3Track  = {}

kf_regions_80med_3Track = {}
kf_regions_80med_lowPT_3Track  = {}
kf_regions_80med_highPT_3Track  = {}

kf_regions_80L1TAU60med_3Track = {}
kf_regions_80L1TAU60med_lowPT_3Track  = {}
kf_regions_80L1TAU60med_highPT_3Track  = {}

kf_regions_125med_3Track = {}
kf_regions_125med_lowPT_3Track  = {}
kf_regions_125med_highPT_3Track  = {}

kf_regions_160med_3Track = {}
kf_regions_160med_lowPT_3Track  = {}
kf_regions_160med_highPT_3Track  = {}

kf_regions_L1TAU12IMmed_3Track = {}
kf_regions_L1TAU12IMmed_lowPT_3Track  = {}
kf_regions_L1TAU12IMmed_highPT_3Track  = {}

kf_regions_ptonly_3Track = {}
kf_regions_ptonly_lowPT_3Track  = {}
kf_regions_ptonly_highPT_3Track  = {}

kf_regions_tracktwo_3Track = {}
kf_regions_tracktwo_lowPT_3Track  = {}
kf_regions_tracktwo_highPT_3Track  = {}


kf_regions_3Track[samples.Wjets]	= {"OS":"Wjets_OS_Tau3Track", "SS":"Wjets_SS_Tau3Track","ncuts":4}
kf_regions_highPT_3Track[samples.Wjets]  = {"OS":"Wjets_OS_highPT_Tau3Track", "SS":"Wjets_SS_highPT_Tau3Track", "ncuts":5}
kf_regions_lowPT_3Track[samples.Wjets]   = {"OS":"Wjets_OS_lowPT_Tau3Track", "SS":"Wjets_SS_lowPT_Tau3Track", "ncuts":5}

kf_regions_25med_3Track[samples.Wjets]	= {"OS":"Wjets_OS_25med_Tau3Track", "SS":"Wjets_SS_25med_Tau3Track","ncuts":5}
kf_regions_25med_lowPT_3Track[samples.Wjets]	= {"OS":"Wjets_OS_25med_lowPT_Tau3Track", "SS":"Wjets_SS_25med_lowPT_Tau3Track","ncuts":6}
kf_regions_25med_highPT_3Track[samples.Wjets]	= {"OS":"Wjets_OS_25med_highPT_Tau3Track", "SS":"Wjets_SS_25med_highPT_Tau3Track","ncuts":6}

kf_regions_35med_3Track[samples.Wjets]	= {"OS":"Wjets_OS_35med_Tau3Track", "SS":"Wjets_SS_35med_Tau3Track","ncuts":5}
kf_regions_35med_lowPT_3Track[samples.Wjets]	= {"OS":"Wjets_OS_35med_lowPT_Tau3Track", "SS":"Wjets_SS_35med_lowPT_Tau3Track","ncuts":6}
kf_regions_35med_highPT_3Track[samples.Wjets]	= {"OS":"Wjets_OS_35med_highPT_Tau3Track", "SS":"Wjets_SS_35med_highPT_Tau3Track","ncuts":6}

kf_regions_50L1TAU12med_3Track[samples.Wjets]	= {"OS":"Wjets_OS_50L1TAU12med_Tau3Track", "SS":"Wjets_SS_50L1TAU12med_Tau3Track","ncuts":5}
kf_regions_50L1TAU12med_lowPT_3Track[samples.Wjets]	= {"OS":"Wjets_OS_50L1TAU12med_lowPT_Tau3Track", "SS":"Wjets_SS_50L1TAU12med_lowPT_Tau3Track","ncuts":6}
kf_regions_50L1TAU12med_highPT_3Track[samples.Wjets]	= {"OS":"Wjets_OS_50L1TAU12med_highPT_Tau3Track", "SS":"Wjets_SS_50L1TAU12med_highPT_Tau3Track","ncuts":6}

kf_regions_80med_3Track[samples.Wjets]	= {"OS":"Wjets_OS_80med_Tau3Track", "SS":"Wjets_SS_80med_Tau3Track","ncuts":5}
kf_regions_80med_lowPT_3Track[samples.Wjets]	= {"OS":"Wjets_OS_80med_lowPT_Tau3Track", "SS":"Wjets_SS_80med_lowPT_Tau3Track","ncuts":6}
kf_regions_80med_highPT_3Track[samples.Wjets]	= {"OS":"Wjets_OS_80med_highPT_Tau3Track", "SS":"Wjets_SS_80med_highPT_Tau3Track","ncuts":6}

kf_regions_80L1TAU60med_3Track[samples.Wjets]	= {"OS":"Wjets_OS_80L1TAU60med_Tau3Track", "SS":"Wjets_SS_80L1TAU60med_Tau3Track","ncuts":5}
kf_regions_80L1TAU60med_lowPT_3Track[samples.Wjets]	= {"OS":"Wjets_OS_80L1TAU60med_lowPT_Tau3Track", "SS":"Wjets_SS_80L1TAU60med_lowPT_Tau3Track","ncuts":6}
kf_regions_80L1TAU60med_highPT_3Track[samples.Wjets]	= {"OS":"Wjets_OS_80L1TAU60med_highPT_Tau3Track", "SS":"Wjets_SS_80L1TAU60med_highPT_Tau3Track","ncuts":6}

kf_regions_125med_3Track[samples.Wjets]	= {"OS":"Wjets_OS_125med_Tau3Track", "SS":"Wjets_SS_125med_Tau3Track","ncuts":5}
kf_regions_125med_lowPT_3Track[samples.Wjets]	= {"OS":"Wjets_OS_125med_lowPT_Tau3Track", "SS":"Wjets_SS_125med_lowPT_Tau3Track","ncuts":6}
kf_regions_125med_highPT_3Track[samples.Wjets]	= {"OS":"Wjets_OS_125med_highPT_Tau3Track", "SS":"Wjets_SS_125med_highPT_Tau3Track","ncuts":6}

kf_regions_160med_3Track[samples.Wjets]	= {"OS":"Wjets_OS_160med_Tau3Track", "SS":"Wjets_SS_160med_Tau3Track","ncuts":5}
kf_regions_160med_lowPT_3Track[samples.Wjets]	= {"OS":"Wjets_OS_160med_lowPT_Tau3Track", "SS":"Wjets_SS_160med_lowPT_Tau3Track","ncuts":6}
kf_regions_160med_highPT_3Track[samples.Wjets]	= {"OS":"Wjets_OS_160med_highPT_Tau3Track", "SS":"Wjets_SS_160med_highPT_Tau3Track","ncuts":6}

kf_regions_L1TAU12IMmed_3Track[samples.Wjets]	= {"OS":"Wjets_OS_L1TAU12IMmed_Tau3Track", "SS":"Wjets_SS_L1TAU12IMmed_Tau3Track","ncuts":5}
kf_regions_L1TAU12IMmed_lowPT_3Track[samples.Wjets]	= {"OS":"Wjets_OS_L1TAU12IMmed_lowPT_Tau3Track", "SS":"Wjets_SS_L1TAU12IMmed_lowPT_Tau3Track","ncuts":6}
kf_regions_L1TAU12IMmed_highPT_3Track[samples.Wjets]	= {"OS":"Wjets_OS_L1TAU12IMmed_highPT_Tau3Track", "SS":"Wjets_SS_L1TAU12IMmed_highPT_Tau3Track","ncuts":6}

kf_regions_ptonly_3Track[samples.Wjets]	= {"OS":"Wjets_OS_ptonly_Tau3Track", "SS":"Wjets_SS_ptonly_Tau3Track","ncuts":5}
kf_regions_ptonly_lowPT_3Track[samples.Wjets]	= {"OS":"Wjets_OS_ptonly_lowPT_Tau3Track", "SS":"Wjets_SS_ptonly_lowPT_Tau3Track","ncuts":6}
kf_regions_ptonly_highPT_3Track[samples.Wjets]	= {"OS":"Wjets_OS_ptonly_highPT_Tau3Track", "SS":"Wjets_SS_ptonly_highPT_Tau3Track","ncuts":6}

kf_regions_tracktwo_3Track[samples.Wjets]	= {"OS":"Wjets_OS_tracktwo_Tau3Track", "SS":"Wjets_SS_tracktwo_Tau3Track","ncuts":5}
kf_regions_tracktwo_lowPT_3Track[samples.Wjets]	= {"OS":"Wjets_OS_tracktwo_lowPT_Tau3Track", "SS":"Wjets_SS_tracktwo_lowPT_Tau3Track","ncuts":6}
kf_regions_tracktwo_highPT_3Track[samples.Wjets]	= {"OS":"Wjets_OS_tracktwo_highPT_Tau3Track", "SS":"Wjets_SS_tracktwo_highPT_Tau3Track","ncuts":6}


if options.kwsys:
        print "*****************************************"
        print "*********** kw sys", options.kwsys
        print "*****************************************"


	kf_regions_25med_lowPT_3Track[samples.Wjets]    = {"OS":"Wjets_OS_MTrans"+str(options.kwsys)+"_25med_lowPT_Tau3Track", "SS":"Wjets_SS_MTrans"+str(options.kwsys)+"_25med_lowPT_Tau3Track","ncuts":7}
	kf_regions_25med_highPT_3Track[samples.Wjets]   = {"OS":"Wjets_OS_MTrans"+str(options.kwsys)+"_25med_highPT_Tau3Track", "SS":"Wjets_SS_MTrans"+str(options.kwsys)+"_25med_highPT_Tau3Track","ncuts":7}
	kf_regions_35med_lowPT_3Track[samples.Wjets]    = {"OS":"Wjets_OS_MTrans"+str(options.kwsys)+"_35med_lowPT_Tau3Track", "SS":"Wjets_SS_MTrans"+str(options.kwsys)+"_35med_lowPT_Tau3Track","ncuts":7}
	kf_regions_35med_highPT_3Track[samples.Wjets]   = {"OS":"Wjets_OS_MTrans"+str(options.kwsys)+"_35med_highPT_Tau3Track", "SS":"Wjets_SS_MTrans"+str(options.kwsys)+"_35med_highPT_Tau3Track","ncuts":7}

	kf_regions_50L1TAU12med_lowPT_3Track[samples.Wjets]    = {"OS":"Wjets_OS_MTrans"+str(options.kwsys)+"_50L1TAU12med_lowPT_Tau3Track", "SS":"Wjets_SS_MTrans"+str(options.kwsys)+"_50L1TAU12med_lowPT_Tau3Track","ncuts":7}
	kf_regions_50L1TAU12med_highPT_3Track[samples.Wjets]   = {"OS":"Wjets_OS_MTrans"+str(options.kwsys)+"_50L1TAU12med_highPT_Tau3Track", "SS":"Wjets_SS_MTrans"+str(options.kwsys)+"_50L1TAU12med_highPT_Tau3Track","ncuts":7}

	kf_regions_80med_lowPT_3Track[samples.Wjets]    = {"OS":"Wjets_OS_MTrans"+str(options.kwsys)+"_80med_lowPT_Tau3Track", "SS":"Wjets_SS_MTrans"+str(options.kwsys)+"_80med_lowPT_Tau3Track","ncuts":7}
	kf_regions_80med_highPT_3Track[samples.Wjets]   = {"OS":"Wjets_OS_MTrans"+str(options.kwsys)+"_80med_highPT_Tau3Track", "SS":"Wjets_SS_MTrans"+str(options.kwsys)+"_80med_highPT_Tau3Track","ncuts":7}

	kf_regions_80L1TAU60med_lowPT_3Track[samples.Wjets]    = {"OS":"Wjets_OS_MTrans"+str(options.kwsys)+"_80L1TAU60med_lowPT_Tau3Track", "SS":"Wjets_SS_MTrans"+str(options.kwsys)+"_80L1TAU60med_lowPT_Tau3Track","ncuts":7}
	kf_regions_80L1TAU60med_highPT_3Track[samples.Wjets]   = {"OS":"Wjets_OS_MTrans"+str(options.kwsys)+"_80L1TAU60med_highPT_Tau3Track", "SS":"Wjets_SS_MTrans"+str(options.kwsys)+"_80L1TAU60med_highPT_Tau3Track","ncuts":7}

	kf_regions_125med_lowPT_3Track[samples.Wjets]    = {"OS":"Wjets_OS_MTrans"+str(options.kwsys)+"_125med_lowPT_Tau3Track", "SS":"Wjets_SS_MTrans"+str(options.kwsys)+"_125med_lowPT_Tau3Track","ncuts":7}
	kf_regions_125med_highPT_3Track[samples.Wjets]   = {"OS":"Wjets_OS_MTrans"+str(options.kwsys)+"_125med_highPT_Tau3Track", "SS":"Wjets_SS_MTrans"+str(options.kwsys)+"_125med_highPT_Tau3Track","ncuts":7}

	kf_regions_160med_lowPT_3Track[samples.Wjets]    = {"OS":"Wjets_OS_MTrans"+str(options.kwsys)+"_160med_lowPT_Tau3Track", "SS":"Wjets_SS_MTrans"+str(options.kwsys)+"_160med_lowPT_Tau3Track","ncuts":7}
	kf_regions_160med_highPT_3Track[samples.Wjets]   = {"OS":"Wjets_OS_MTrans"+str(options.kwsys)+"_160med_highPT_Tau3Track", "SS":"Wjets_SS_MTrans"+str(options.kwsys)+"_160med_highPT_Tau3Track","ncuts":7}

	kf_regions_L1TAU12IMmed_lowPT_3Track[samples.Wjets]    = {"OS":"Wjets_OS_MTrans"+str(options.kwsys)+"_L1TAU12IMmed_lowPT_Tau3Track", "SS":"Wjets_SS_MTrans"+str(options.kwsys)+"_L1TAU12IMmed_lowPT_Tau3Track","ncuts":7}
	kf_regions_L1TAU12IMmed_highPT_3Track[samples.Wjets]   = {"OS":"Wjets_OS_MTrans"+str(options.kwsys)+"_L1TAU12IMmed_highPT_Tau3Track", "SS":"Wjets_SS_MTrans"+str(options.kwsys)+"_L1TAU12IMmed_highPT_Tau3Track","ncuts":7}

	kf_regions_highPT_3Track[samples.Wjets]  = {"OS":"Wjets_OS_MTrans"+str(options.kwsys)+"_highPT_Tau3Track", "SS":"Wjets_SS_MTrans"+str(options.kwsys)+"_highPT_Tau3Track", "ncuts":6}
	kf_regions_lowPT_3Track[samples.Wjets]   = {"OS":"Wjets_OS_MTrans"+str(options.kwsys)+"_lowPT_Tau3Track", "SS":"Wjets_SS_MTrans"+str(options.kwsys)+"_lowPT_Tau3Track", "ncuts":6}

	kf_regions_ptonly_lowPT_3Track[samples.Wjets]    = {"OS":"Wjets_OS_MTrans"+str(options.kwsys)+"_ptonlymed_lowPT3Track", "SS":"Wjets_SS_MTrans"+str(options.kwsys)+"_ptonlymed_lowPT3Track","ncuts":7}
	kf_regions_ptonly_highPT_3Track[samples.Wjets]   = {"OS":"Wjets_OS_MTrans"+str(options.kwsys)+"_ptonlymed_highPT3Track", "SS":"Wjets_SS_MTrans"+str(options.kwsys)+"_ptonlymed_highPT3Track","ncuts":7}

	kf_regions_tracktwo_lowPT_3Track[samples.Wjets]    = {"OS":"Wjets_OS_MTrans"+str(options.kwsys)+"_tracktwomed_lowPT3Track", "SS":"Wjets_SS_MTrans"+str(options.kwsys)+"_tracktwomed_lowPT3Track","ncuts":7}
	kf_regions_tracktwo_highPT_3Track[samples.Wjets]   = {"OS":"Wjets_OS_MTrans"+str(options.kwsys)+"_tracktwomed_highPT3Track", "SS":"Wjets_SS_MTrans"+str(options.kwsys)+"_tracktwomed_highPT3Track","ncuts":7}

	kf_regions_highPT_3Track[samples.Wjets]  = {"OS":"Wjets_OS_MTrans"+str(options.kwsys)+"_highPT_Tau3Track", "SS":"Wjets_SS_MTrans"+str(options.kwsys)+"_highPT_Tau3Track", "ncuts":6}
	kf_regions_lowPT_3Track[samples.Wjets]   = {"OS":"Wjets_OS_MTrans"+str(options.kwsys)+"_lowPT_Tau3Track", "SS":"Wjets_SS_MTrans"+str(options.kwsys)+"_lowPT_Tau3Track", "ncuts":6}
###############################################
     
# Rqcd

rqcd_regions_OS_no_cuts = {}

rqcd_regions = {}
rqcd_regions_lowPT = {}
rqcd_regions_highPT = {}

rqcd_regions_25med = {}
rqcd_regions_25med_lowPT = {}
rqcd_regions_25med_highPT = {}

rqcd_regions_35med = {}
rqcd_regions_35med_lowPT = {}
rqcd_regions_35med_highPT = {}

rqcd_regions_50L1TAU12med = {}
rqcd_regions_50L1TAU12med_lowPT = {}
rqcd_regions_50L1TAU12med_highPT = {}

rqcd_regions_80med = {}
rqcd_regions_80med_lowPT = {}
rqcd_regions_80med_highPT = {}

rqcd_regions_80L1TAU60med = {}
rqcd_regions_80L1TAU60med_lowPT = {}
rqcd_regions_80L1TAU60med_highPT = {}

rqcd_regions_125med = {}
rqcd_regions_125med_lowPT = {}
rqcd_regions_125med_highPT = {}

rqcd_regions_160med = {}
rqcd_regions_160med_lowPT = {}
rqcd_regions_160med_highPT = {}

rqcd_regions_L1TAU12IMmed = {}
rqcd_regions_L1TAU12IMmed_lowPT = {}
rqcd_regions_L1TAU12IMmed_highPT = {}

rqcd_regions_ptonly = {}
rqcd_regions_ptonly_lowPT = {}
rqcd_regions_ptonly_highPT = {}

rqcd_regions_tracktwo = {}
rqcd_regions_tracktwo_lowPT = {}
rqcd_regions_tracktwo_highPT = {}

rqcd_regions_OS_no_cuts[data] = {"num":"AntiIsoCR_OS","den":"AntiIsoCR_SS","ncuts":3}

rqcd_regions[data] 	= {"num":"AntiIsoCR_OS","den":"AntiIsoCR_SS","ncuts":3}
rqcd_regions_highPT[data]  = {"num":"AntiIsoCR_OS_highPT", "den":"AntiIsoCR_SS_highPT", "ncuts":4}
rqcd_regions_lowPT[data] = {"num":"AntiIsoCR_OS_lowPT", "den":"AntiIsoCR_SS_lowPT", "ncuts":4}

rqcd_regions_25med[data]  = {"num":"AntiIsoCR_OS_25med", "den":"AntiIsoCR_SS_25med", "ncuts":4}
rqcd_regions_25med_lowPT[data]  = {"num":"AntiIsoCR_OS_25med_lowPT", "den":"AntiIsoCR_SS_25med_lowPT", "ncuts":5}
rqcd_regions_25med_highPT[data]  = {"num":"AntiIsoCR_OS_25med_highPT", "den":"AntiIsoCR_SS_25med_highPT", "ncuts":5}

rqcd_regions_35med[data]  = {"num":"AntiIsoCR_OS_35med", "den":"AntiIsoCR_SS_35med", "ncuts":4}
rqcd_regions_35med_lowPT[data]  = {"num":"AntiIsoCR_OS_35med_lowPT", "den":"AntiIsoCR_SS_35med_lowPT", "ncuts":5}
rqcd_regions_35med_highPT[data]  = {"num":"AntiIsoCR_OS_35med_highPT", "den":"AntiIsoCR_SS_35med_highPT", "ncuts":5}

rqcd_regions_50L1TAU12med[data]  = {"num":"AntiIsoCR_OS_50L1TAU12med", "den":"AntiIsoCR_SS_50L1TAU12med", "ncuts":4}
rqcd_regions_50L1TAU12med_lowPT[data]  = {"num":"AntiIsoCR_OS_50L1TAU12med_lowPT", "den":"AntiIsoCR_SS_50L1TAU12med_lowPT", "ncuts":5}
rqcd_regions_50L1TAU12med_highPT[data]  = {"num":"AntiIsoCR_OS_50L1TAU12med_highPT", "den":"AntiIsoCR_SS_50L1TAU12med_highPT", "ncuts":5}

rqcd_regions_80med[data]  = {"num":"AntiIsoCR_OS_80med", "den":"AntiIsoCR_SS_80med", "ncuts":4}
rqcd_regions_80med_lowPT[data]  = {"num":"AntiIsoCR_OS_80med_lowPT", "den":"AntiIsoCR_SS_80med_lowPT", "ncuts":5}
rqcd_regions_80med_highPT[data]  = {"num":"AntiIsoCR_OS_80med_highPT", "den":"AntiIsoCR_SS_80med_highPT", "ncuts":5}

rqcd_regions_80L1TAU60med[data]  = {"num":"AntiIsoCR_OS_80L1TAU60med", "den":"AntiIsoCR_SS_80L1TAU60med", "ncuts":4}
rqcd_regions_80L1TAU60med_lowPT[data]  = {"num":"AntiIsoCR_OS_80L1TAU60med_lowPT", "den":"AntiIsoCR_SS_80L1TAU60med_lowPT", "ncuts":5}
rqcd_regions_80L1TAU60med_highPT[data]  = {"num":"AntiIsoCR_OS_80L1TAU60med_highPT", "den":"AntiIsoCR_SS_80L1TAU60med_highPT", "ncuts":5}

rqcd_regions_125med[data]  = {"num":"AntiIsoCR_OS_125med", "den":"AntiIsoCR_SS_125med", "ncuts":4}
rqcd_regions_125med_lowPT[data]  = {"num":"AntiIsoCR_OS_125med_lowPT", "den":"AntiIsoCR_SS_125med_lowPT", "ncuts":5}
rqcd_regions_125med_highPT[data]  = {"num":"AntiIsoCR_OS_125med_highPT", "den":"AntiIsoCR_SS_125med_highPT", "ncuts":5}

rqcd_regions_160med[data]  = {"num":"AntiIsoCR_OS_160med", "den":"AntiIsoCR_SS_160med", "ncuts":4}
rqcd_regions_160med_lowPT[data]  = {"num":"AntiIsoCR_OS_160med_lowPT", "den":"AntiIsoCR_SS_160med_lowPT", "ncuts":5}
rqcd_regions_160med_highPT[data]  = {"num":"AntiIsoCR_OS_160med_highPT", "den":"AntiIsoCR_SS_160med_highPT", "ncuts":5}

rqcd_regions_L1TAU12IMmed[data]  = {"num":"AntiIsoCR_OS_L1TAU12IMmed", "den":"AntiIsoCR_SS_L1TAU12IMmed", "ncuts":4}
rqcd_regions_L1TAU12IMmed_lowPT[data]  = {"num":"AntiIsoCR_OS_L1TAU12IMmed_lowPT", "den":"AntiIsoCR_SS_L1TAU12IMmed_lowPT", "ncuts":5}
rqcd_regions_L1TAU12IMmed_highPT[data]  = {"num":"AntiIsoCR_OS_L1TAU12IMmed_highPT", "den":"AntiIsoCR_SS_L1TAU12IMmed_highPT", "ncuts":5}

rqcd_regions_ptonly[data]  = {"num":"AntiIsoCR_OS_ptonly", "den":"AntiIsoCR_SS_ptonly", "ncuts":4}
rqcd_regions_ptonly_lowPT[data]  = {"num":"AntiIsoCR_OS_ptonly_lowPT", "den":"AntiIsoCR_SS_ptonly_lowPT", "ncuts":5}
rqcd_regions_ptonly_highPT[data]  = {"num":"AntiIsoCR_OS_ptonly_highPT", "den":"AntiIsoCR_SS_ptonly_highPT", "ncuts":5}

rqcd_regions_tracktwo[data]  = {"num":"AntiIsoCR_OS_tracktwo", "den":"AntiIsoCR_SS_tracktwo", "ncuts":4}
rqcd_regions_tracktwo_lowPT[data]  = {"num":"AntiIsoCR_OS_tracktwo_lowPT", "den":"AntiIsoCR_SS_tracktwo_lowPT", "ncuts":5}
rqcd_regions_tracktwo_highPT[data]  = {"num":"AntiIsoCR_OS_tracktwo_highPT", "den":"AntiIsoCR_SS_tracktwo_highPT", "ncuts":5}

if options.toposys:
        print "*****************************************"
        print "*********** incl topo sys", options.toposys
        print "*****************************************"

	# SYSTEMATICS
	# DONE #rqcd_regions[data]      = {"num":"AntiIsoCR_OS_Topoetcone20pt0"+str(options.toposys),"den":"AntiIsoCR_SS_Topoetcone20pt0"+str(options.toposys),"ncuts":4}
	rqcd_regions_highPT[data]  = {"num":"AntiIsoCR_OS_highPT_Topoetcone20pt0"+str(options.toposys), "den":"AntiIsoCR_SS_highPT_Topoetcone20pt0"+str(options.toposys), "ncuts":5}
	rqcd_regions_lowPT[data] = {"num":"AntiIsoCR_OS_lowPT_Topoetcone20pt0"+str(options.toposys), "den":"AntiIsoCR_SS_lowPT_Topoetcone20pt0"+str(options.toposys), "ncuts":5}
	# DONE #rqcd_regions_25med[data]  = {"num":"AntiIsoCR_OS_25med_Topoetcone20pt0"+str(options.toposys), "den":"AntiIsoCR_SS_25med_Topoetcone20pt0"+str(options.toposys), "ncuts":5}
	rqcd_regions_25med_lowPT[data]  = {"num":"AntiIsoCR_OS_25med_lowPT_Topoetcone20pt0"+str(options.toposys), "den":"AntiIsoCR_SS_25med_lowPT_Topoetcone20pt0"+str(options.toposys), "ncuts":6}
	rqcd_regions_25med_highPT[data]  = {"num":"AntiIsoCR_OS_25med_highPT_Topoetcone20pt0"+str(options.toposys), "den":"AntiIsoCR_SS_25med_highPT_Topoetcone20pt0"+str(options.toposys), "ncuts":6}
	#rqcd_regions_35med[data]  = {"num":"AntiIsoCR_OS_35med_Topoetcone20pt0"+str(options.toposys), "den":"AntiIsoCR_SS_35med_Topoetcone20pt0"+str(options.toposys), "ncuts":5}
	rqcd_regions_35med_lowPT[data]  = {"num":"AntiIsoCR_OS_35med_lowPT_Topoetcone20pt0"+str(options.toposys), "den":"AntiIsoCR_SS_35med_lowPT_Topoetcone20pt0"+str(options.toposys), "ncuts":6}
	rqcd_regions_35med_highPT[data]  = {"num":"AntiIsoCR_OS_35med_highPT_Topoetcone20pt0"+str(options.toposys), "den":"AntiIsoCR_SS_35med_highPT_Topoetcone20pt0"+str(options.toposys), "ncuts":6}

	rqcd_regions_L1TAU12IMmed_lowPT[data]  = {"num":"AntiIsoCR_OS_L1TAU12IMmed_lowPT_Topoetcone20pt0"+str(options.toposys), "den":"AntiIsoCR_SS_L1TAU12IMmed_lowPT_Topoetcone20pt0"+str(options.toposys), "ncuts":6}
	rqcd_regions_L1TAU12IMmed_highPT[data]  = {"num":"AntiIsoCR_OS_L1TAU12IMmed_highPT_Topoetcone20pt0"+str(options.toposys), "den":"AntiIsoCR_SS_L1TAU12IMmed_highPT_Topoetcone20pt0"+str(options.toposys), "ncuts":6}

	rqcd_regions_ptonly_lowPT[data]  = {"num":"AntiIsoCR_OS_ptonlymed_lowPT_Topoetcone20pt0"+str(options.toposys), "den":"AntiIsoCR_SS_ptonlymed_lowPT_Topoetcone20pt0"+str(options.toposys), "ncuts":6}
	rqcd_regions_ptonly_highPT[data]  = {"num":"AntiIsoCR_OS_ptonlymed_highPT_Topoetcone20pt0"+str(options.toposys), "den":"AntiIsoCR_SS_ptonlymed_highPT_Topoetcone20pt0"+str(options.toposys), "ncuts":6}

	rqcd_regions_tracktwo_lowPT[data]  = {"num":"AntiIsoCR_OS_tracktwomed_lowPT_Topoetcone20pt0"+str(options.toposys), "den":"AntiIsoCR_SS_tracktwomed_lowPT_Topoetcone20pt0"+str(options.toposys), "ncuts":6}
	rqcd_regions_tracktwo_highPT[data]  = {"num":"AntiIsoCR_OS_tracktwomed_highPT_Topoetcone20pt0"+str(options.toposys), "den":"AntiIsoCR_SS_tracktwomed_highPT_Topoetcone20pt0"+str(options.toposys), "ncuts":6}


if options.sysptvar:
        print "*****************************************"
        print "*********** ptvar sys", options.sysptvar
        print "*****************************************"

	rqcd_regions_highPT[data]  = {"num":"AntiIsoCR_OS_highPT_Ptvarcone30pt0"+str(options.sysptvar), "den":"AntiIsoCR_SS_highPT_Ptvarcone30pt0"+str(options.sysptvar), "ncuts":5}
	rqcd_regions_lowPT[data] = {"num":"AntiIsoCR_OS_lowPT_Ptvarcone30pt0"+str(options.sysptvar), "den":"AntiIsoCR_SS_lowPT_Ptvarcone30pt0"+str(options.sysptvar), "ncuts":5}

	rqcd_regions_25med_lowPT[data]  = {"num":"AntiIsoCR_OS_25med_lowPT_Ptvarcone30pt0"+str(options.sysptvar), "den":"AntiIsoCR_SS_25med_lowPT_Ptvarcone30pt0"+str(options.sysptvar), "ncuts":6}
	rqcd_regions_25med_highPT[data]  = {"num":"AntiIsoCR_OS_25med_highPT_Ptvarcone30pt0"+str(options.sysptvar), "den":"AntiIsoCR_SS_25med_highPT_Ptvarcone30pt0"+str(options.sysptvar), "ncuts":6}

	rqcd_regions_35med_lowPT[data]  = {"num":"AntiIsoCR_OS_35med_lowPT_Ptvarcone30pt0"+str(options.sysptvar), "den":"AntiIsoCR_SS_35med_lowPT_Ptvarcone30pt0"+str(options.sysptvar), "ncuts":6}
	rqcd_regions_35med_highPT[data]  = {"num":"AntiIsoCR_OS_35med_highPT_Ptvarcone30pt0"+str(options.sysptvar), "den":"AntiIsoCR_SS_35med_highPT_Ptvarcone30pt0"+str(options.sysptvar), "ncuts":6}

	rqcd_regions_L1TAU12IMmed_lowPT[data]  = {"num":"AntiIsoCR_OS_L1TAU12IMmed_lowPT_Ptvarcone30pt0"+str(options.sysptvar), "den":"AntiIsoCR_SS_L1TAU12IMmed_lowPT_Ptvarcone30pt0"+str(options.sysptvar), "ncuts":6}
	rqcd_regions_L1TAU12IMmed_highPT[data]  = {"num":"AntiIsoCR_OS_L1TAU12IMmed_highPT_Ptvarcone30pt0"+str(options.sysptvar), "den":"AntiIsoCR_SS_L1TAU12IMmed_highPT_Ptvarcone30pt0"+str(options.sysptvar), "ncuts":6}

	rqcd_regions_ptonly_lowPT[data]  = {"num":"AntiIsoCR_OS_ptonlymed_lowPT_Ptvarcone30pt0"+str(options.sysptvar), "den":"AntiIsoCR_SS_ptonlymed_lowPT_Ptvarcone30pt0"+str(options.sysptvar), "ncuts":6}
	rqcd_regions_ptonly_highPT[data]  = {"num":"AntiIsoCR_OS_ptonlymed_highPT_Ptvarcone30pt0"+str(options.sysptvar), "den":"AntiIsoCR_SS_ptonlymed_highPT_Ptvarcone30pt0"+str(options.sysptvar), "ncuts":6}

	rqcd_regions_tracktwo_lowPT[data]  = {"num":"AntiIsoCR_OS_tracktwomed_lowPT_Ptvarcone30pt0"+str(options.sysptvar), "den":"AntiIsoCR_SS_tracktwomed_lowPT_Ptvarcone30pt0"+str(options.sysptvar), "ncuts":6}
	rqcd_regions_tracktwo_highPT[data]  = {"num":"AntiIsoCR_OS_tracktwomed_highPT_Ptvarcone30pt0"+str(options.sysptvar), "den":"AntiIsoCR_SS_tracktwomed_highPT_Ptvarcone30pt0"+str(options.sysptvar), "ncuts":6}

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

rqcd_regions_50L1TAU12med_1Track= {}
rqcd_regions_50L1TAU12med_lowPT_1Track = {}
rqcd_regions_50L1TAU12med_highPT_1Track = {}

rqcd_regions_80med_1Track= {}
rqcd_regions_80med_lowPT_1Track = {}
rqcd_regions_80med_highPT_1Track = {}

rqcd_regions_80L1TAU60med_1Track= {}
rqcd_regions_80L1TAU60med_lowPT_1Track = {}
rqcd_regions_80L1TAU60med_highPT_1Track = {}

rqcd_regions_125med_1Track= {}
rqcd_regions_125med_lowPT_1Track = {}
rqcd_regions_125med_highPT_1Track = {}

rqcd_regions_160med_1Track= {}
rqcd_regions_160med_lowPT_1Track = {}
rqcd_regions_160med_highPT_1Track = {}

rqcd_regions_L1TAU12IMmed_1Track= {}
rqcd_regions_L1TAU12IMmed_lowPT_1Track = {}
rqcd_regions_L1TAU12IMmed_highPT_1Track = {}

rqcd_regions_ptonly_1Track= {}
rqcd_regions_ptonly_lowPT_1Track = {}
rqcd_regions_ptonly_highPT_1Track = {}

rqcd_regions_tracktwo_1Track= {}
rqcd_regions_tracktwo_lowPT_1Track = {}
rqcd_regions_tracktwo_highPT_1Track = {}

rqcd_regions_1Track[data] 	= {"num":"AntiIsoCR_OS_Tau1Track","den":"AntiIsoCR_SS_Tau1Track","ncuts":4}
rqcd_regions_highPT_1Track[data]  = {"num":"AntiIsoCR_OS_highPT_Tau1Track", "den":"AntiIsoCR_SS_highPT_Tau1Track", "ncuts":5}
rqcd_regions_lowPT_1Track[data] = {"num":"AntiIsoCR_OS_lowPT_Tau1Track", "den":"AntiIsoCR_SS_lowPT_Tau1Track", "ncuts":5}

rqcd_regions_25med_1Track[data]  = {"num":"AntiIsoCR_OS_25med_Tau1Track", "den":"AntiIsoCR_SS_25med_Tau1Track", "ncuts":5}
rqcd_regions_25med_lowPT_1Track[data]  = {"num":"AntiIsoCR_OS_25med_lowPT_Tau1Track", "den":"AntiIsoCR_SS_25med_lowPT_Tau1Track", "ncuts":6}
rqcd_regions_25med_highPT_1Track[data]  = {"num":"AntiIsoCR_OS_25med_highPT_Tau1Track", "den":"AntiIsoCR_SS_25med_highPT_Tau1Track", "ncuts":6}

rqcd_regions_35med_1Track[data]  = {"num":"AntiIsoCR_OS_35med_Tau1Track", "den":"AntiIsoCR_SS_35med_Tau1Track", "ncuts":5}
rqcd_regions_35med_lowPT_1Track[data]  = {"num":"AntiIsoCR_OS_35med_lowPT_Tau1Track", "den":"AntiIsoCR_SS_35med_lowPT_Tau1Track", "ncuts":6}
rqcd_regions_35med_highPT_1Track[data]  = {"num":"AntiIsoCR_OS_35med_highPT_Tau1Track", "den":"AntiIsoCR_SS_35med_highPT_Tau1Track", "ncuts":6}

rqcd_regions_50L1TAU12med_1Track[data]  = {"num":"AntiIsoCR_OS_50L1TAU12med_Tau1Track", "den":"AntiIsoCR_SS_50L1TAU12med_Tau1Track", "ncuts":5}
rqcd_regions_50L1TAU12med_lowPT_1Track[data]  = {"num":"AntiIsoCR_OS_50L1TAU12med_lowPT_Tau1Track", "den":"AntiIsoCR_SS_50L1TAU12med_lowPT_Tau1Track", "ncuts":6}
rqcd_regions_50L1TAU12med_highPT_1Track[data]  = {"num":"AntiIsoCR_OS_50L1TAU12med_highPT_Tau1Track", "den":"AntiIsoCR_SS_50L1TAU12med_highPT_Tau1Track", "ncuts":6}

rqcd_regions_80med_1Track[data]  = {"num":"AntiIsoCR_OS_80med_Tau1Track", "den":"AntiIsoCR_SS_80med_Tau1Track", "ncuts":5}
rqcd_regions_80med_lowPT_1Track[data]  = {"num":"AntiIsoCR_OS_80med_lowPT_Tau1Track", "den":"AntiIsoCR_SS_80med_lowPT_Tau1Track", "ncuts":6}
rqcd_regions_80med_highPT_1Track[data]  = {"num":"AntiIsoCR_OS_80med_highPT_Tau1Track", "den":"AntiIsoCR_SS_80med_highPT_Tau1Track", "ncuts":6}

rqcd_regions_80L1TAU60med_1Track[data]  = {"num":"AntiIsoCR_OS_80L1TAU60med_Tau1Track", "den":"AntiIsoCR_SS_80L1TAU60med_Tau1Track", "ncuts":5}
rqcd_regions_80L1TAU60med_lowPT_1Track[data]  = {"num":"AntiIsoCR_OS_80L1TAU60med_lowPT_Tau1Track", "den":"AntiIsoCR_SS_80L1TAU60med_lowPT_Tau1Track", "ncuts":6}
rqcd_regions_80L1TAU60med_highPT_1Track[data]  = {"num":"AntiIsoCR_OS_80L1TAU60med_highPT_Tau1Track", "den":"AntiIsoCR_SS_80L1TAU60med_highPT_Tau1Track", "ncuts":6}

rqcd_regions_125med_1Track[data]  = {"num":"AntiIsoCR_OS_125med_Tau1Track", "den":"AntiIsoCR_SS_125med_Tau1Track", "ncuts":5}
rqcd_regions_125med_lowPT_1Track[data]  = {"num":"AntiIsoCR_OS_125med_lowPT_Tau1Track", "den":"AntiIsoCR_SS_125med_lowPT_Tau1Track", "ncuts":6}
rqcd_regions_125med_highPT_1Track[data]  = {"num":"AntiIsoCR_OS_125med_highPT_Tau1Track", "den":"AntiIsoCR_SS_125med_highPT_Tau1Track", "ncuts":6}

rqcd_regions_160med_1Track[data]  = {"num":"AntiIsoCR_OS_160med_Tau1Track", "den":"AntiIsoCR_SS_160med_Tau1Track", "ncuts":5}
rqcd_regions_160med_lowPT_1Track[data]  = {"num":"AntiIsoCR_OS_160med_lowPT_Tau1Track", "den":"AntiIsoCR_SS_160med_lowPT_Tau1Track", "ncuts":6}
rqcd_regions_160med_highPT_1Track[data]  = {"num":"AntiIsoCR_OS_160med_highPT_Tau1Track", "den":"AntiIsoCR_SS_160med_highPT_Tau1Track", "ncuts":6}

rqcd_regions_L1TAU12IMmed_1Track[data]  = {"num":"AntiIsoCR_OS_L1TAU12IMmed_Tau1Track", "den":"AntiIsoCR_SS_L1TAU12IMmed_Tau1Track", "ncuts":5}
rqcd_regions_L1TAU12IMmed_lowPT_1Track[data]  = {"num":"AntiIsoCR_OS_L1TAU12IMmed_lowPT_Tau1Track", "den":"AntiIsoCR_SS_L1TAU12IMmed_lowPT_Tau1Track", "ncuts":6}
rqcd_regions_L1TAU12IMmed_highPT_1Track[data]  = {"num":"AntiIsoCR_OS_L1TAU12IMmed_highPT_Tau1Track", "den":"AntiIsoCR_SS_L1TAU12IMmed_highPT_Tau1Track", "ncuts":6}

rqcd_regions_ptonly_1Track[data]  = {"num":"AntiIsoCR_OS_ptonly_Tau1Track", "den":"AntiIsoCR_SS_ptonly_Tau1Track", "ncuts":5}
rqcd_regions_ptonly_lowPT_1Track[data]  = {"num":"AntiIsoCR_OS_ptonly_lowPT_Tau1Track", "den":"AntiIsoCR_SS_ptonly_lowPT_Tau1Track", "ncuts":6}
rqcd_regions_ptonly_highPT_1Track[data]  = {"num":"AntiIsoCR_OS_ptonly_highPT_Tau1Track", "den":"AntiIsoCR_SS_ptonly_highPT_Tau1Track", "ncuts":6}

rqcd_regions_tracktwo_1Track[data]  = {"num":"AntiIsoCR_OS_tracktwo_Tau1Track", "den":"AntiIsoCR_SS_tracktwo_Tau1Track", "ncuts":5}
rqcd_regions_tracktwo_lowPT_1Track[data]  = {"num":"AntiIsoCR_OS_tracktwo_lowPT_Tau1Track", "den":"AntiIsoCR_SS_tracktwo_lowPT_Tau1Track", "ncuts":6}
rqcd_regions_tracktwo_highPT_1Track[data]  = {"num":"AntiIsoCR_OS_tracktwo_highPT_Tau1Track", "den":"AntiIsoCR_SS_tracktwo_highPT_Tau1Track", "ncuts":6}


if options.toposys:
	print "*****************************************"
	print "*********** 1 track topo sys", options.toposys
        print "*****************************************"

	rqcd_regions_highPT_1Track[data]  = {"num":"AntiIsoCR_OS_highPT_Tau1Track_Topoetcone20pt0"+str(options.toposys), "den":"AntiIsoCR_SS_highPT_Tau1Track_Topoetcone20pt0"+str(options.toposys), "ncuts":6}
	rqcd_regions_lowPT_1Track[data] = {"num":"AntiIsoCR_OS_lowPT_Tau1Track_Topoetcone20pt0"+str(options.toposys), "den":"AntiIsoCR_SS_lowPT_Tau1Track_Topoetcone20pt0"+str(options.toposys), "ncuts":6}

	rqcd_regions_25med_lowPT_1Track[data]  = {"num":"AntiIsoCR_OS_25med_lowPT_Tau1Track_Topoetcone20pt0"+str(options.toposys), "den":"AntiIsoCR_SS_25med_lowPT_Tau1Track_Topoetcone20pt0"+str(options.toposys), "ncuts":7}
	rqcd_regions_25med_highPT_1Track[data]  = {"num":"AntiIsoCR_OS_25med_highPT_Tau1Track_Topoetcone20pt0"+str(options.toposys), "den":"AntiIsoCR_SS_25med_highPT_Tau1Track_Topoetcone20pt0"+str(options.toposys), "ncuts":7}

	rqcd_regions_35med_lowPT_1Track[data]  = {"num":"AntiIsoCR_OS_35med_lowPT_Tau1Track_Topoetcone20pt0"+str(options.toposys), "den":"AntiIsoCR_SS_35med_lowPT_Tau1Track_Topoetcone20pt0"+str(options.toposys), "ncuts":7}
	rqcd_regions_35med_highPT_1Track[data]  = {"num":"AntiIsoCR_OS_35med_highPT_Tau1Track_Topoetcone20pt0"+str(options.toposys), "den":"AntiIsoCR_SS_35med_highPT_Tau1Track_Topoetcone20pt0"+str(options.toposys), "ncuts":7}

	rqcd_regions_50L1TAU12med_lowPT_1Track[data]  = {"num":"AntiIsoCR_OS_50L1TAU12med_lowPT_Tau1Track_Topoetcone20pt0"+str(options.toposys), "den":"AntiIsoCR_SS_50L1TAU12med_lowPT_Tau1Track_Topoetcone20pt0"+str(options.toposys), "ncuts":7}
	rqcd_regions_50L1TAU12med_highPT_1Track[data]  = {"num":"AntiIsoCR_OS_50L1TAU12med_highPT_Tau1Track_Topoetcone20pt0"+str(options.toposys), "den":"AntiIsoCR_SS_50L1TAU12med_highPT_Tau1Track_Topoetcone20pt0"+str(options.toposys), "ncuts":7}

	rqcd_regions_80med_lowPT_1Track[data]  = {"num":"AntiIsoCR_OS_80med_lowPT_Tau1Track_Topoetcone20pt0"+str(options.toposys), "den":"AntiIsoCR_SS_80med_lowPT_Tau1Track_Topoetcone20pt0"+str(options.toposys), "ncuts":7}
	rqcd_regions_80med_highPT_1Track[data]  = {"num":"AntiIsoCR_OS_80med_highPT_Tau1Track_Topoetcone20pt0"+str(options.toposys), "den":"AntiIsoCR_SS_80med_highPT_Tau1Track_Topoetcone20pt0"+str(options.toposys), "ncuts":7}

	rqcd_regions_80L1TAU60med_lowPT_1Track[data]  = {"num":"AntiIsoCR_OS_80L1TAU60med_lowPT_Tau1Track_Topoetcone20pt0"+str(options.toposys), "den":"AntiIsoCR_SS_80L1TAU60med_lowPT_Tau1Track_Topoetcone20pt0"+str(options.toposys), "ncuts":7}
	rqcd_regions_80L1TAU60med_highPT_1Track[data]  = {"num":"AntiIsoCR_OS_80L1TAU60med_highPT_Tau1Track_Topoetcone20pt0"+str(options.toposys), "den":"AntiIsoCR_SS_80L1TAU60med_highPT_Tau1Track_Topoetcone20pt0"+str(options.toposys), "ncuts":7}

	rqcd_regions_125med_lowPT_1Track[data]  = {"num":"AntiIsoCR_OS_125med_lowPT_Tau1Track_Topoetcone20pt0"+str(options.toposys), "den":"AntiIsoCR_SS_125med_lowPT_Tau1Track_Topoetcone20pt0"+str(options.toposys), "ncuts":7}
	rqcd_regions_125med_highPT_1Track[data]  = {"num":"AntiIsoCR_OS_125med_highPT_Tau1Track_Topoetcone20pt0"+str(options.toposys), "den":"AntiIsoCR_SS_125med_highPT_Tau1Track_Topoetcone20pt0"+str(options.toposys), "ncuts":7}

	rqcd_regions_160med_lowPT_1Track[data]  = {"num":"AntiIsoCR_OS_160med_lowPT_Tau1Track_Topoetcone20pt0"+str(options.toposys), "den":"AntiIsoCR_SS_160med_lowPT_Tau1Track_Topoetcone20pt0"+str(options.toposys), "ncuts":7}
	rqcd_regions_160med_highPT_1Track[data]  = {"num":"AntiIsoCR_OS_160med_highPT_Tau1Track_Topoetcone20pt0"+str(options.toposys), "den":"AntiIsoCR_SS_160med_highPT_Tau1Track_Topoetcone20pt0"+str(options.toposys), "ncuts":7}

	rqcd_regions_L1TAU12IMmed_lowPT_1Track[data]  = {"num":"AntiIsoCR_OS_L1TAU12IMmed_lowPT_Tau1Track_Topoetcone20pt0"+str(options.toposys), "den":"AntiIsoCR_SS_L1TAU12IMmed_lowPT_Tau1Track_Topoetcone20pt0"+str(options.toposys), "ncuts":7}
	rqcd_regions_L1TAU12IMmed_highPT_1Track[data]  = {"num":"AntiIsoCR_OS_L1TAU12IMmed_highPT_Tau1Track_Topoetcone20pt0"+str(options.toposys), "den":"AntiIsoCR_SS_L1TAU12IMmed_highPT_Tau1Track_Topoetcone20pt0"+str(options.toposys), "ncuts":7}

	rqcd_regions_ptonly_lowPT_1Track[data]  = {"num":"AntiIsoCR_OS_ptonlymed_lowPT_Tau1Track_Topoetcone20pt0"+str(options.toposys), "den":"AntiIsoCR_SS_ptonlymed_lowPT_Tau1Track_Topoetcone20pt0"+str(options.toposys), "ncuts":7}
	rqcd_regions_ptonly_highPT_1Track[data]  = {"num":"AntiIsoCR_OS_ptonlymed_highPT_Tau1Track_Topoetcone20pt0"+str(options.toposys), "den":"AntiIsoCR_SS_ptonlymed_highPT_Tau1Track_Topoetcone20pt0"+str(options.toposys), "ncuts":7}

	rqcd_regions_tracktwo_lowPT_1Track[data]  = {"num":"AntiIsoCR_OS_tracktwomed_lowPT_Tau1Track_Topoetcone20pt0"+str(options.toposys), "den":"AntiIsoCR_SS_tracktwomed_lowPT_Tau1Track_Topoetcone20pt0"+str(options.toposys), "ncuts":7}
	rqcd_regions_tracktwo_highPT_1Track[data]  = {"num":"AntiIsoCR_OS_tracktwomed_highPT_Tau1Track_Topoetcone20pt0"+str(options.toposys), "den":"AntiIsoCR_SS_tracktwomed_highPT_Tau1Track_Topoetcone20pt0"+str(options.toposys), "ncuts":7}




if options.sysptvar:
        print "*****************************************"
        print "*********** ptvar sys", options.sysptvar
        print "*****************************************"

	rqcd_regions_highPT_1Track[data]  = {"num":"AntiIsoCR_OS_highPT_Tau1Track_Ptvarcone30pt0"+str(options.sysptvar), "den":"AntiIsoCR_SS_highPT_Tau1Track_Ptvarcone30pt0"+str(options.sysptvar), "ncuts":6}
	rqcd_regions_lowPT_1Track[data] = {"num":"AntiIsoCR_OS_lowPT_Tau1Track_Ptvarcone30pt0"+str(options.sysptvar), "den":"AntiIsoCR_SS_lowPT_Tau1Track_Ptvarcone30pt0"+str(options.sysptvar), "ncuts":6}

	rqcd_regions_25med_lowPT_1Track[data]  = {"num":"AntiIsoCR_OS_25med_lowPT_Tau1Track_Ptvarcone30pt0"+str(options.sysptvar), "den":"AntiIsoCR_SS_25med_lowPT_Tau1Track_Ptvarcone30pt0"+str(options.sysptvar), "ncuts":7}
	rqcd_regions_25med_highPT_1Track[data]  = {"num":"AntiIsoCR_OS_25med_highPT_Tau1Track_Ptvarcone30pt0"+str(options.sysptvar), "den":"AntiIsoCR_SS_25med_highPT_Tau1Track_Ptvarcone30pt0"+str(options.sysptvar), "ncuts":7}

	rqcd_regions_35med_lowPT_1Track[data]  = {"num":"AntiIsoCR_OS_35med_lowPT_Tau1Track_Ptvarcone30pt0"+str(options.sysptvar), "den":"AntiIsoCR_SS_35med_lowPT_Tau1Track_Ptvarcone30pt0"+str(options.sysptvar), "ncuts":7}
	rqcd_regions_35med_highPT_1Track[data]  = {"num":"AntiIsoCR_OS_35med_highPT_Tau1Track_Ptvarcone30pt0"+str(options.sysptvar), "den":"AntiIsoCR_SS_35med_highPT_Tau1Track_Ptvarcone30pt0"+str(options.sysptvar), "ncuts":7}

	rqcd_regions_50L1TAU12med_lowPT_1Track[data]  = {"num":"AntiIsoCR_OS_50L1TAU12med_lowPT_Tau1Track_Ptvarcone30pt0"+str(options.sysptvar), "den":"AntiIsoCR_SS_50L1TAU12med_lowPT_Tau1Track_Ptvarcone30pt0"+str(options.sysptvar), "ncuts":7}
	rqcd_regions_50L1TAU12med_highPT_1Track[data]  = {"num":"AntiIsoCR_OS_50L1TAU12med_highPT_Tau1Track_Ptvarcone30pt0"+str(options.sysptvar), "den":"AntiIsoCR_SS_50L1TAU12med_highPT_Tau1Track_Ptvarcone30pt0"+str(options.sysptvar), "ncuts":7}

	rqcd_regions_80med_lowPT_1Track[data]  = {"num":"AntiIsoCR_OS_80med_lowPT_Tau1Track_Ptvarcone30pt0"+str(options.sysptvar), "den":"AntiIsoCR_SS_80med_lowPT_Tau1Track_Ptvarcone30pt0"+str(options.sysptvar), "ncuts":7}
	rqcd_regions_80med_highPT_1Track[data]  = {"num":"AntiIsoCR_OS_80med_highPT_Tau1Track_Ptvarcone30pt0"+str(options.sysptvar), "den":"AntiIsoCR_SS_80med_highPT_Tau1Track_Ptvarcone30pt0"+str(options.sysptvar), "ncuts":7}

	rqcd_regions_80L1TAU60med_lowPT_1Track[data]  = {"num":"AntiIsoCR_OS_80L1TAU60med_lowPT_Tau1Track_Ptvarcone30pt0"+str(options.sysptvar), "den":"AntiIsoCR_SS_80L1TAU60med_lowPT_Tau1Track_Ptvarcone30pt0"+str(options.sysptvar), "ncuts":7}
	rqcd_regions_80L1TAU60med_highPT_1Track[data]  = {"num":"AntiIsoCR_OS_80L1TAU60med_highPT_Tau1Track_Ptvarcone30pt0"+str(options.sysptvar), "den":"AntiIsoCR_SS_80L1TAU60med_highPT_Tau1Track_Ptvarcone30pt0"+str(options.sysptvar), "ncuts":7}

	rqcd_regions_125med_1Track[data]  = {"num":"AntiIsoCR_OS_125med_Tau1Track_Ptvarcone30pt0"+str(options.sysptvar), "den":"AntiIsoCR_SS_125med_Tau1Track_Ptvarcone30pt0"+str(options.sysptvar), "ncuts":5}
	rqcd_regions_125med_lowPT_1Track[data]  = {"num":"AntiIsoCR_OS_125med_lowPT_Tau1Track_Ptvarcone30pt0"+str(options.sysptvar), "den":"AntiIsoCR_SS_125med_lowPT_Tau1Track_Ptvarcone30pt0"+str(options.sysptvar), "ncuts":7}
	rqcd_regions_125med_highPT_1Track[data]  = {"num":"AntiIsoCR_OS_125med_highPT_Tau1Track_Ptvarcone30pt0"+str(options.sysptvar), "den":"AntiIsoCR_SS_125med_highPT_Tau1Track_Ptvarcone30pt0"+str(options.sysptvar), "ncuts":7}

	rqcd_regions_160med_1Track[data]  = {"num":"AntiIsoCR_OS_160med_Tau1Track_Ptvarcone30pt0"+str(options.sysptvar), "den":"AntiIsoCR_SS_160med_Tau1Track_Ptvarcone30pt0"+str(options.sysptvar), "ncuts":5}
	rqcd_regions_160med_lowPT_1Track[data]  = {"num":"AntiIsoCR_OS_160med_lowPT_Tau1Track_Ptvarcone30pt0"+str(options.sysptvar), "den":"AntiIsoCR_SS_160med_lowPT_Tau1Track_Ptvarcone30pt0"+str(options.sysptvar), "ncuts":7}

	rqcd_regions_160med_highPT_1Track[data]  = {"num":"AntiIsoCR_OS_160med_highPT_Tau1Track_Ptvarcone30pt0"+str(options.sysptvar), "den":"AntiIsoCR_SS_160med_highPT_Tau1Track_Ptvarcone30pt0"+str(options.sysptvar), "ncuts":7}

	rqcd_regions_L1TAU12IMmed_lowPT_1Track[data]  = {"num":"AntiIsoCR_OS_L1TAU12IMmed_lowPT_Tau1Track_Ptvarcone30pt0"+str(options.sysptvar), "den":"AntiIsoCR_SS_L1TAU12IMmed_lowPT_Tau1Track_Ptvarcone30pt0"+str(options.sysptvar), "ncuts":7}
	rqcd_regions_L1TAU12IMmed_highPT_1Track[data]  = {"num":"AntiIsoCR_OS_L1TAU12IMmed_highPT_Tau1Track_Ptvarcone30pt0"+str(options.sysptvar), "den":"AntiIsoCR_SS_L1TAU12IMmed_highPT_Tau1Track_Ptvarcone30pt0"+str(options.sysptvar), "ncuts":7}

	rqcd_regions_ptonly_lowPT_1Track[data]  = {"num":"AntiIsoCR_OS_ptonlymed_lowPT_Tau1Track_Ptvarcone30pt0"+str(options.sysptvar), "den":"AntiIsoCR_SS_ptonlymed_lowPT_Tau1Track_Ptvarcone30pt0"+str(options.sysptvar), "ncuts":7}
	rqcd_regions_ptonly_highPT_1Track[data]  = {"num":"AntiIsoCR_OS_ptonlymed_highPT_Tau1Track_Ptvarcone30pt0"+str(options.sysptvar), "den":"AntiIsoCR_SS_ptonlymed_highPT_Tau1Track_Ptvarcone30pt0"+str(options.sysptvar), "ncuts":7}

	rqcd_regions_tracktwo_lowPT_1Track[data]  = {"num":"AntiIsoCR_OS_tracktwomed_lowPT_Tau1Track_Ptvarcone30pt0"+str(options.sysptvar), "den":"AntiIsoCR_SS_tracktwomed_lowPT_Tau1Track_Ptvarcone30pt0"+str(options.sysptvar), "ncuts":7}
	rqcd_regions_tracktwo_highPT_1Track[data]  = {"num":"AntiIsoCR_OS_tracktwomed_highPT_Tau1Track_Ptvarcone30pt0"+str(options.sysptvar), "den":"AntiIsoCR_SS_tracktwomed_highPT_Tau1Track_Ptvarcone30pt0"+str(options.sysptvar), "ncuts":7}





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

rqcd_regions_50L1TAU12med_3Track= {}
rqcd_regions_50L1TAU12med_lowPT_3Track = {}
rqcd_regions_50L1TAU12med_highPT_3Track = {}

rqcd_regions_80med_3Track= {}
rqcd_regions_80med_lowPT_3Track = {}
rqcd_regions_80med_highPT_3Track = {}

rqcd_regions_80L1TAU60med_3Track= {}
rqcd_regions_80L1TAU60med_lowPT_3Track = {}
rqcd_regions_80L1TAU60med_highPT_3Track = {}

rqcd_regions_125med_3Track= {}
rqcd_regions_125med_lowPT_3Track = {}
rqcd_regions_125med_highPT_3Track = {}

rqcd_regions_160med_3Track= {}
rqcd_regions_160med_lowPT_3Track = {}
rqcd_regions_160med_highPT_3Track = {}

rqcd_regions_L1TAU12IMmed_3Track= {}
rqcd_regions_L1TAU12IMmed_lowPT_3Track = {}
rqcd_regions_L1TAU12IMmed_highPT_3Track = {}

rqcd_regions_ptonly_3Track= {}
rqcd_regions_ptonly_lowPT_3Track = {}
rqcd_regions_ptonly_highPT_3Track = {}

rqcd_regions_tracktwo_3Track= {}
rqcd_regions_tracktwo_lowPT_3Track = {}
rqcd_regions_tracktwo_highPT_3Track = {}

rqcd_regions_3Track[data] 	= {"num":"AntiIsoCR_OS_Tau3Track","den":"AntiIsoCR_SS_Tau3Track","ncuts":4}
rqcd_regions_highPT_3Track[data]  = {"num":"AntiIsoCR_OS_highPT_Tau3Track", "den":"AntiIsoCR_SS_highPT_Tau3Track", "ncuts":5}
rqcd_regions_lowPT_3Track[data] = {"num":"AntiIsoCR_OS_lowPT_Tau3Track", "den":"AntiIsoCR_SS_lowPT_Tau3Track", "ncuts":5}

rqcd_regions_25med_3Track[data]  = {"num":"AntiIsoCR_OS_25med_Tau3Track", "den":"AntiIsoCR_SS_25med_Tau3Track", "ncuts":5}
rqcd_regions_25med_lowPT_3Track[data]  = {"num":"AntiIsoCR_OS_25med_lowPT_Tau3Track", "den":"AntiIsoCR_SS_25med_lowPT_Tau3Track", "ncuts":6}
rqcd_regions_25med_highPT_3Track[data]  = {"num":"AntiIsoCR_OS_25med_highPT_Tau3Track", "den":"AntiIsoCR_SS_25med_highPT_Tau3Track", "ncuts":6}

rqcd_regions_35med_3Track[data]  = {"num":"AntiIsoCR_OS_35med_Tau3Track", "den":"AntiIsoCR_SS_35med_Tau3Track", "ncuts":5}
rqcd_regions_35med_lowPT_3Track[data]  = {"num":"AntiIsoCR_OS_35med_lowPT_Tau3Track", "den":"AntiIsoCR_SS_35med_lowPT_Tau3Track", "ncuts":6}
rqcd_regions_35med_highPT_3Track[data]  = {"num":"AntiIsoCR_OS_35med_highPT_Tau3Track", "den":"AntiIsoCR_SS_35med_highPT_Tau3Track", "ncuts":6}

rqcd_regions_50L1TAU12med_3Track[data]  = {"num":"AntiIsoCR_OS_50L1TAU12med_Tau3Track", "den":"AntiIsoCR_SS_50L1TAU12med_Tau3Track", "ncuts":5}
rqcd_regions_50L1TAU12med_lowPT_3Track[data]  = {"num":"AntiIsoCR_OS_50L1TAU12med_lowPT_Tau3Track", "den":"AntiIsoCR_SS_50L1TAU12med_lowPT_Tau3Track", "ncuts":6}
rqcd_regions_50L1TAU12med_highPT_3Track[data]  = {"num":"AntiIsoCR_OS_50L1TAU12med_highPT_Tau3Track", "den":"AntiIsoCR_SS_50L1TAU12med_highPT_Tau3Track", "ncuts":6}

rqcd_regions_80med_3Track[data]  = {"num":"AntiIsoCR_OS_80med_Tau3Track", "den":"AntiIsoCR_SS_80med_Tau3Track", "ncuts":5}
rqcd_regions_80med_lowPT_3Track[data]  = {"num":"AntiIsoCR_OS_80med_lowPT_Tau3Track", "den":"AntiIsoCR_SS_80med_lowPT_Tau3Track", "ncuts":6}
rqcd_regions_80med_highPT_3Track[data]  = {"num":"AntiIsoCR_OS_80med_highPT_Tau3Track", "den":"AntiIsoCR_SS_80med_highPT_Tau3Track", "ncuts":6}

rqcd_regions_80L1TAU60med_3Track[data]  = {"num":"AntiIsoCR_OS_80L1TAU60med_Tau3Track", "den":"AntiIsoCR_SS_80L1TAU60med_Tau3Track", "ncuts":5}
rqcd_regions_80L1TAU60med_lowPT_3Track[data]  = {"num":"AntiIsoCR_OS_80L1TAU60med_lowPT_Tau3Track", "den":"AntiIsoCR_SS_80L1TAU60med_lowPT_Tau3Track", "ncuts":6}
rqcd_regions_80L1TAU60med_highPT_3Track[data]  = {"num":"AntiIsoCR_OS_80L1TAU60med_highPT_Tau3Track", "den":"AntiIsoCR_SS_80L1TAU60med_highPT_Tau3Track", "ncuts":6}

rqcd_regions_125med_3Track[data]  = {"num":"AntiIsoCR_OS_125med_Tau3Track", "den":"AntiIsoCR_SS_125med_Tau3Track", "ncuts":5}
rqcd_regions_125med_lowPT_3Track[data]  = {"num":"AntiIsoCR_OS_125med_lowPT_Tau3Track", "den":"AntiIsoCR_SS_125med_lowPT_Tau3Track", "ncuts":6}
rqcd_regions_125med_highPT_3Track[data]  = {"num":"AntiIsoCR_OS_125med_highPT_Tau3Track", "den":"AntiIsoCR_SS_125med_highPT_Tau3Track", "ncuts":6}

rqcd_regions_160med_3Track[data]  = {"num":"AntiIsoCR_OS_160med_Tau3Track", "den":"AntiIsoCR_SS_160med_Tau3Track", "ncuts":5}
rqcd_regions_160med_lowPT_3Track[data]  = {"num":"AntiIsoCR_OS_160med_lowPT_Tau3Track", "den":"AntiIsoCR_SS_160med_lowPT_Tau3Track", "ncuts":6}
rqcd_regions_160med_highPT_3Track[data]  = {"num":"AntiIsoCR_OS_160med_highPT_Tau3Track", "den":"AntiIsoCR_SS_160med_highPT_Tau3Track", "ncuts":6}

rqcd_regions_L1TAU12IMmed_3Track[data]  = {"num":"AntiIsoCR_OS_L1TAU12IMmed_Tau3Track", "den":"AntiIsoCR_SS_L1TAU12IMmed_Tau3Track", "ncuts":5}
rqcd_regions_L1TAU12IMmed_lowPT_3Track[data]  = {"num":"AntiIsoCR_OS_L1TAU12IMmed_lowPT_Tau3Track", "den":"AntiIsoCR_SS_L1TAU12IMmed_lowPT_Tau3Track", "ncuts":6}
rqcd_regions_L1TAU12IMmed_highPT_3Track[data]  = {"num":"AntiIsoCR_OS_L1TAU12IMmed_highPT_Tau3Track", "den":"AntiIsoCR_SS_L1TAU12IMmed_highPT_Tau3Track", "ncuts":6}

rqcd_regions_ptonly_3Track[data]  = {"num":"AntiIsoCR_OS_ptonly_Tau3Track", "den":"AntiIsoCR_SS_ptonly_Tau3Track", "ncuts":5}
rqcd_regions_ptonly_lowPT_3Track[data]  = {"num":"AntiIsoCR_OS_ptonly_lowPT_Tau3Track", "den":"AntiIsoCR_SS_ptonly_lowPT_Tau3Track", "ncuts":6}
rqcd_regions_ptonly_highPT_3Track[data]  = {"num":"AntiIsoCR_OS_ptonly_highPT_Tau3Track", "den":"AntiIsoCR_SS_ptonly_highPT_Tau3Track", "ncuts":6}

rqcd_regions_tracktwo_3Track[data]  = {"num":"AntiIsoCR_OS_tracktwo_Tau3Track", "den":"AntiIsoCR_SS_tracktwo_Tau3Track", "ncuts":5}
rqcd_regions_tracktwo_lowPT_3Track[data]  = {"num":"AntiIsoCR_OS_tracktwo_lowPT_Tau3Track", "den":"AntiIsoCR_SS_tracktwo_lowPT_Tau3Track", "ncuts":6}
rqcd_regions_tracktwo_highPT_3Track[data]  = {"num":"AntiIsoCR_OS_tracktwo_highPT_Tau3Track", "den":"AntiIsoCR_SS_tracktwo_highPT_Tau3Track", "ncuts":6}


if options.toposys:
        print "*****************************************"
        print "*********** 3 track topo sys", options.toposys
        print "*****************************************"

	rqcd_regions_highPT_3Track[data]  = {"num":"AntiIsoCR_OS_highPT_Tau3Track_Topoetcone20pt0"+str(options.toposys), "den":"AntiIsoCR_SS_highPT_Tau3Track_Topoetcone20pt0"+str(options.toposys), "ncuts":6}
	rqcd_regions_lowPT_3Track[data] = {"num":"AntiIsoCR_OS_lowPT_Tau3Track_Topoetcone20pt0"+str(options.toposys), "den":"AntiIsoCR_SS_lowPT_Tau3Track_Topoetcone20pt0"+str(options.toposys), "ncuts":6}
	#rqcd_regions_3Track[data] 	= {"num":"AntiIsoCR_OS_Tau3Track_Topoetcone20pt0"+str(options.toposys),"den":"AntiIsoCR_SS_Tau3Track_Topoetcone20pt0"+str(options.toposys),"ncuts":5}
	#rqcd_regions_25med_3Track[data]  = {"num":"AntiIsoCR_OS_25med_Tau3Track_Topoetcone20pt0"+str(options.toposys), "den":"AntiIsoCR_SS_25med_Tau3Track_Topoetcone20pt0"+str(options.toposys), "ncuts":6}
	rqcd_regions_25med_lowPT_3Track[data]  = {"num":"AntiIsoCR_OS_25med_lowPT_Tau3Track_Topoetcone20pt0"+str(options.toposys), "den":"AntiIsoCR_SS_25med_lowPT_Tau3Track_Topoetcone20pt0"+str(options.toposys), "ncuts":7}
	rqcd_regions_25med_highPT_3Track[data]  = {"num":"AntiIsoCR_OS_25med_highPT_Tau3Track_Topoetcone20pt0"+str(options.toposys), "den":"AntiIsoCR_SS_25med_highPT_Tau3Track_Topoetcone20pt0"+str(options.toposys), "ncuts":7}
	#rqcd_regions_35med_3Track[data]  = {"num":"AntiIsoCR_OS_35med_Tau3Track_Topoetcone20pt0"+str(options.toposys), "den":"AntiIsoCR_SS_35med_Tau3Track_Topoetcone20pt0"+str(options.toposys), "ncuts":6}
	rqcd_regions_35med_lowPT_3Track[data]  = {"num":"AntiIsoCR_OS_35med_lowPT_Tau3Track_Topoetcone20pt0"+str(options.toposys), "den":"AntiIsoCR_SS_35med_lowPT_Tau3Track_Topoetcone20pt0"+str(options.toposys), "ncuts":7}
	rqcd_regions_35med_highPT_3Track[data]  = {"num":"AntiIsoCR_OS_35med_highPT_Tau3Track_Topoetcone20pt0"+str(options.toposys), "den":"AntiIsoCR_SS_35med_highPT_Tau3Track_Topoetcone20pt0"+str(options.toposys), "ncuts":7}

	rqcd_regions_50L1TAU12med_lowPT_3Track[data]  = {"num":"AntiIsoCR_OS_50L1TAU12med_lowPT_Tau3Track_Topoetcone20pt0"+str(options.toposys), "den":"AntiIsoCR_SS_50L1TAU12med_lowPT_Tau3Track_Topoetcone20pt0"+str(options.toposys), "ncuts":7}
	rqcd_regions_50L1TAU12med_highPT_3Track[data]  = {"num":"AntiIsoCR_OS_50L1TAU12med_highPT_Tau3Track_Topoetcone20pt0"+str(options.toposys), "den":"AntiIsoCR_SS_50L1TAU12med_highPT_Tau3Track_Topoetcone20pt0"+str(options.toposys), "ncuts":7}

	rqcd_regions_80L1TAU60med_lowPT_3Track[data]  = {"num":"AntiIsoCR_OS_80L1TAU60med_lowPT_Tau3Track_Topoetcone20pt0"+str(options.toposys), "den":"AntiIsoCR_SS_80L1TAU60med_lowPT_Tau3Track_Topoetcone20pt0"+str(options.toposys), "ncuts":7}
	rqcd_regions_80L1TAU60med_highPT_3Track[data]  = {"num":"AntiIsoCR_OS_80L1TAU60med_highPT_Tau3Track_Topoetcone20pt0"+str(options.toposys), "den":"AntiIsoCR_SS_80L1TAU60med_highPT_Tau3Track_Topoetcone20pt0"+str(options.toposys), "ncuts":7}

	rqcd_regions_125med_lowPT_3Track[data]  = {"num":"AntiIsoCR_OS_125med_lowPT_Tau3Track_Topoetcone20pt0"+str(options.toposys), "den":"AntiIsoCR_SS_125med_lowPT_Tau3Track_Topoetcone20pt0"+str(options.toposys), "ncuts":7}
	rqcd_regions_125med_highPT_3Track[data]  = {"num":"AntiIsoCR_OS_125med_highPT_Tau3Track_Topoetcone20pt0"+str(options.toposys), "den":"AntiIsoCR_SS_125med_highPT_Tau3Track_Topoetcone20pt0"+str(options.toposys), "ncuts":7}

	rqcd_regions_160med_lowPT_3Track[data]  = {"num":"AntiIsoCR_OS_160med_lowPT_Tau3Track_Topoetcone20pt0"+str(options.toposys), "den":"AntiIsoCR_SS_160med_lowPT_Tau3Track_Topoetcone20pt0"+str(options.toposys), "ncuts":7}
	rqcd_regions_160med_highPT_3Track[data]  = {"num":"AntiIsoCR_OS_160med_highPT_Tau3Track_Topoetcone20pt0"+str(options.toposys), "den":"AntiIsoCR_SS_160med_highPT_Tau3Track_Topoetcone20pt0"+str(options.toposys), "ncuts":7}

	rqcd_regions_L1TAU12IMmed_lowPT_3Track[data]  = {"num":"AntiIsoCR_OS_L1TAU12IMmed_lowPT_Tau3Track_Topoetcone20pt0"+str(options.toposys), "den":"AntiIsoCR_SS_L1TAU12IMmed_lowPT_Tau3Track_Topoetcone20pt0"+str(options.toposys), "ncuts":7}
	rqcd_regions_L1TAU12IMmed_highPT_3Track[data]  = {"num":"AntiIsoCR_OS_L1TAU12IMmed_highPT_Tau3Track_Topoetcone20pt0"+str(options.toposys), "den":"AntiIsoCR_SS_L1TAU12IMmed_highPT_Tau3Track_Topoetcone20pt0"+str(options.toposys), "ncuts":7}

	rqcd_regions_ptonly_lowPT_3Track[data]  = {"num":"AntiIsoCR_OS_ptonlymed_lowPT_Tau3Track_Topoetcone20pt0"+str(options.toposys), "den":"AntiIsoCR_SS_ptonlymed_lowPT_Tau3Track_Topoetcone20pt0"+str(options.toposys), "ncuts":7}
	rqcd_regions_ptonly_highPT_3Track[data]  = {"num":"AntiIsoCR_OS_ptonlymed_highPT_Tau3Track_Topoetcone20pt0"+str(options.toposys), "den":"AntiIsoCR_SS_ptonlymed_highPT_Tau3Track_Topoetcone20pt0"+str(options.toposys), "ncuts":7}

	rqcd_regions_tracktwo_lowPT_3Track[data]  = {"num":"AntiIsoCR_OS_tracktwomed_lowPT_Tau3Track_Topoetcone20pt0"+str(options.toposys), "den":"AntiIsoCR_SS_tracktwomed_lowPT_Tau3Track_Topoetcone20pt0"+str(options.toposys), "ncuts":7}
	rqcd_regions_tracktwo_highPT_3Track[data]  = {"num":"AntiIsoCR_OS_tracktwomed_highPT_Tau3Track_Topoetcone20pt0"+str(options.toposys), "den":"AntiIsoCR_SS_tracktwomed_highPT_Tau3Track_Topoetcone20pt0"+str(options.toposys), "ncuts":7}

	rqcd_regions_80med_lowPT_3Track[data]  = {"num":"AntiIsoCR_OS_80med_lowPT_Tau3Track_Topoetcone20pt0"+str(options.toposys), "den":"AntiIsoCR_SS_80med_lowPT_Tau3Track_Topoetcone20pt0"+str(options.toposys), "ncuts":7}
	rqcd_regions_80med_highPT_3Track[data]  = {"num":"AntiIsoCR_OS_80med_highPT_Tau3Track_Topoetcone20pt0"+str(options.toposys), "den":"AntiIsoCR_SS_80med_highPT_Tau3Track_Topoetcone20pt0"+str(options.toposys), "ncuts":7}


if options.sysptvar:
        print "*****************************************"
        print "*********** ptvar sys", options.sysptvar
        print "*****************************************"

	rqcd_regions_highPT_3Track[data]  = {"num":"AntiIsoCR_OS_highPT_Tau3Track_Ptvarcone30pt0"+str(options.sysptvar), "den":"AntiIsoCR_SS_highPT_Tau3Track_Ptvarcone30pt0"+str(options.sysptvar), "ncuts":6}
	rqcd_regions_lowPT_3Track[data] = {"num":"AntiIsoCR_OS_lowPT_Tau3Track_Ptvarcone30pt0"+str(options.sysptvar), "den":"AntiIsoCR_SS_lowPT_Tau3Track_Ptvarcone30pt0"+str(options.sysptvar), "ncuts":6}
	#rqcd_regions_3Track[data] 	= {"num":"AntiIsoCR_OS_Tau3Track_Ptvarcone30pt0"+str(options.sysptvar),"den":"AntiIsoCR_SS_Tau3Track_Ptvarcone30pt0"+str(options.sysptvar),"ncuts":5}
	rqcd_regions_25med_3Track[data]  = {"num":"AntiIsoCR_OS_25med_Tau3Track_Ptvarcone30pt0"+str(options.sysptvar), "den":"AntiIsoCR_SS_25med_Tau3Track_Ptvarcone30pt0"+str(options.sysptvar), "ncuts":6}
	rqcd_regions_25med_lowPT_3Track[data]  = {"num":"AntiIsoCR_OS_25med_lowPT_Tau3Track_Ptvarcone30pt0"+str(options.sysptvar), "den":"AntiIsoCR_SS_25med_lowPT_Tau3Track_Ptvarcone30pt0"+str(options.sysptvar), "ncuts":7}
	rqcd_regions_25med_highPT_3Track[data]  = {"num":"AntiIsoCR_OS_25med_highPT_Tau3Track_Ptvarcone30pt0"+str(options.sysptvar), "den":"AntiIsoCR_SS_25med_highPT_Tau3Track_Ptvarcone30pt0"+str(options.sysptvar), "ncuts":7}
	#rqcd_regions_35med_3Track[data]  = {"num":"AntiIsoCR_OS_35med_Tau3Track_Ptvarcone30pt0"+str(options.sysptvar), "den":"AntiIsoCR_SS_35med_Tau3Track_Ptvarcone30pt0"+str(options.sysptvar), "ncuts":6}
	rqcd_regions_35med_lowPT_3Track[data]  = {"num":"AntiIsoCR_OS_35med_lowPT_Tau3Track_Ptvarcone30pt0"+str(options.sysptvar), "den":"AntiIsoCR_SS_35med_lowPT_Tau3Track_Ptvarcone30pt0"+str(options.sysptvar), "ncuts":7}
	rqcd_regions_35med_highPT_3Track[data]  = {"num":"AntiIsoCR_OS_35med_highPT_Tau3Track_Ptvarcone30pt0"+str(options.sysptvar), "den":"AntiIsoCR_SS_35med_highPT_Tau3Track_Ptvarcone30pt0"+str(options.sysptvar), "ncuts":7}
	  
	rqcd_regions_50L1TAU12med_lowPT_3Track[data]  = {"num":"AntiIsoCR_OS_50L1TAU12med_lowPT_Tau3Track_Ptvarcone30pt0"+str(options.sysptvar), "den":"AntiIsoCR_SS_50L1TAU12med_lowPT_Tau3Track_Ptvarcone30pt0"+str(options.sysptvar), "ncuts":7}
	rqcd_regions_50L1TAU12med_highPT_3Track[data]  = {"num":"AntiIsoCR_OS_50L1TAU12med_highPT_Tau3Track_Ptvarcone30pt0"+str(options.sysptvar), "den":"AntiIsoCR_SS_50L1TAU12med_highPT_Tau3Track_Ptvarcone30pt0"+str(options.sysptvar), "ncuts":7}

	rqcd_regions_80L1TAU60med_lowPT_3Track[data]  = {"num":"AntiIsoCR_OS_80L1TAU60med_lowPT_Tau3Track_Ptvarcone30pt0"+str(options.sysptvar), "den":"AntiIsoCR_SS_80L1TAU60med_lowPT_Tau3Track_Ptvarcone30pt0"+str(options.sysptvar), "ncuts":7}
	rqcd_regions_80L1TAU60med_highPT_3Track[data]  = {"num":"AntiIsoCR_OS_80L1TAU60med_highPT_Tau3Track_Ptvarcone30pt0"+str(options.sysptvar), "den":"AntiIsoCR_SS_80L1TAU60med_highPT_Tau3Track_Ptvarcone30pt0"+str(options.sysptvar), "ncuts":7}

	rqcd_regions_L1TAU12IMmed_lowPT_3Track[data]  = {"num":"AntiIsoCR_OS_L1TAU12IMmed_lowPT_Tau3Track_Ptvarcone30pt0"+str(options.sysptvar), "den":"AntiIsoCR_SS_L1TAU12IMmed_lowPT_Tau3Track_Ptvarcone30pt0"+str(options.sysptvar), "ncuts":7}
	rqcd_regions_L1TAU12IMmed_highPT_3Track[data]  = {"num":"AntiIsoCR_OS_L1TAU12IMmed_highPT_Tau3Track_Ptvarcone30pt0"+str(options.sysptvar), "den":"AntiIsoCR_SS_L1TAU12IMmed_highPT_Tau3Track_Ptvarcone30pt0"+str(options.sysptvar), "ncuts":7}

	rqcd_regions_125med_lowPT_3Track[data]  = {"num":"AntiIsoCR_OS_125med_lowPT_Tau3Track_Ptvarcone30pt0"+str(options.sysptvar), "den":"AntiIsoCR_SS_125med_lowPT_Tau3Track_Ptvarcone30pt0"+str(options.sysptvar), "ncuts":7}
	rqcd_regions_125med_highPT_3Track[data]  = {"num":"AntiIsoCR_OS_125med_highPT_Tau3Track_Ptvarcone30pt0"+str(options.sysptvar), "den":"AntiIsoCR_SS_125med_highPT_Tau3Track_Ptvarcone30pt0"+str(options.sysptvar), "ncuts":7}

	rqcd_regions_160med_lowPT_3Track[data]  = {"num":"AntiIsoCR_OS_160med_lowPT_Tau3Track_Ptvarcone30pt0"+str(options.sysptvar), "den":"AntiIsoCR_SS_160med_lowPT_Tau3Track_Ptvarcone30pt0"+str(options.sysptvar), "ncuts":7}
	rqcd_regions_160med_highPT_3Track[data]  = {"num":"AntiIsoCR_OS_160med_highPT_Tau3Track_Ptvarcone30pt0"+str(options.sysptvar), "den":"AntiIsoCR_SS_160med_highPT_Tau3Track_Ptvarcone30pt0"+str(options.sysptvar), "ncuts":7}

	rqcd_regions_ptonly_lowPT_3Track[data]  = {"num":"AntiIsoCR_OS_ptonlymed_lowPT_Tau3Track_Ptvarcone30pt0"+str(options.sysptvar), "den":"AntiIsoCR_SS_ptonlymed_lowPT_Tau3Track_Ptvarcone30pt0"+str(options.sysptvar), "ncuts":7}
	rqcd_regions_ptonly_highPT_3Track[data]  = {"num":"AntiIsoCR_OS_ptonlymed_highPT_Tau3Track_Ptvarcone30pt0"+str(options.sysptvar), "den":"AntiIsoCR_SS_ptonlymed_highPT_Tau3Track_Ptvarcone30pt0"+str(options.sysptvar), "ncuts":7}

	rqcd_regions_tracktwo_lowPT_3Track[data]  = {"num":"AntiIsoCR_OS_tracktwomed_lowPT_Tau3Track_Ptvarcone30pt0"+str(options.sysptvar), "den":"AntiIsoCR_SS_tracktwomed_lowPT_Tau3Track_Ptvarcone30pt0"+str(options.sysptvar), "ncuts":7}
	rqcd_regions_tracktwo_highPT_3Track[data]  = {"num":"AntiIsoCR_OS_tracktwomed_highPT_Tau3Track_Ptvarcone30pt0"+str(options.sysptvar), "den":"AntiIsoCR_SS_tracktwomed_highPT_Tau3Track_Ptvarcone30pt0"+str(options.sysptvar), "ncuts":7}

	rqcd_regions_80med_lowPT_3Track[data]  = {"num":"AntiIsoCR_OS_80med_lowPT_Tau3Track_Ptvarcone30pt0"+str(options.sysptvar), "den":"AntiIsoCR_SS_80med_lowPT_Tau3Track_Ptvarcone30pt0"+str(options.sysptvar), "ncuts":7}
	rqcd_regions_80med_highPT_3Track[data]  = {"num":"AntiIsoCR_OS_80med_highPT_Tau3Track_Ptvarcone30pt0"+str(options.sysptvar), "den":"AntiIsoCR_SS_80med_highPT_Tau3Track_Ptvarcone30pt0"+str(options.sysptvar), "ncuts":7}




################################################### 
# Add-On

# ADDITIONAL REGIONS

addon_regions_OS_no_cuts = {}
addon_regions_OS_no_cuts[data]  = {"SS":"SR_SS_no_cuts_forvismass", "OS":"SR_OS_no_cuts_forvismass", "SS_lscdp":"SR_SS_lowSCDP_nomtcut_forvismass", "OS_lscdp":"SR_lowSCDP_nomtcut_forvismass", "ncuts":3}  
addon_regions_OS_no_cuts[samples.Wjets]   = {"OS":"SR_OS_no_cuts_forvismass", "SS":"SR_SS_no_cuts_forvismass", "ncuts":3}
addon_regions_OS_no_cuts[samples.Zlljets] = {"OS":"SR_OS_no_cuts_forvismass", "SS":"SR_SS_no_cuts_forvismass", "ncuts":3}
addon_regions_OS_no_cuts[samples.top]     = {"OS":"SR_OS_no_cuts_forvismass", "SS":"SR_SS_no_cuts_forvismass", "ncuts":3}

addon_regions_lowSCDP = {}
addon_regions_lowSCDP[data]            = {"SS":"SR_SS_lowSCDP", "ncuts":3}
addon_regions_lowSCDP[samples.Wjets]   = {"OS":"SR_lowSCDP", "SS":"SR_SS_lowSCDP", "ncuts":3}
addon_regions_lowSCDP[samples.Zlljets] = {"OS":"SR_lowSCDP", "SS":"SR_SS_lowSCDP", "ncuts":3}
addon_regions_lowSCDP[samples.top]     = {"OS":"SR_lowSCDP", "SS":"SR_SS_lowSCDP", "ncuts":3}

addon_regions_highSCDP = {}
addon_regions_highSCDP[data]            = {"SS":"SR_SS_highSCDP", "ncuts":3}
addon_regions_highSCDP[samples.Wjets]   = {"OS":"SR_highSCDP", "SS":"SR_SS_highSCDP", "ncuts":3}
addon_regions_highSCDP[samples.Zlljets] = {"OS":"SR_highSCDP", "SS":"SR_SS_highSCDP", "ncuts":3}
addon_regions_highSCDP[samples.top]     = {"OS":"SR_highSCDP", "SS":"SR_SS_highSCDP", "ncuts":3}

addon_regions_lowSCDP_highMT = {}
addon_regions_lowSCDP_highMT[data]            = {"SS":"SR_lowSCDP_highMT_SS", "ncuts":4}
addon_regions_lowSCDP_highMT[samples.Wjets]   = {"OS":"SR_lowSCDP_highMT", "SS":"SR_lowSCDP_highMT_SS", "ncuts":4}
addon_regions_lowSCDP_highMT[samples.Zlljets] = {"OS":"SR_lowSCDP_highMT", "SS":"SR_lowSCDP_highMT_SS", "ncuts":4}
addon_regions_lowSCDP_highMT[samples.top]     = {"OS":"SR_lowSCDP_highMT", "SS":"SR_lowSCDP_highMT_SS", "ncuts":4}

addon_regions_highSCDP_highMT = {}
addon_regions_highSCDP_highMT[data]            = {"SS":"SR_highSCDP_highMT_SS", "ncuts":4}
addon_regions_highSCDP_highMT[samples.Wjets]   = {"OS":"SR_highSCDP_highMT", "SS":"SR_highSCDP_highMT_SS", "ncuts":4}
addon_regions_highSCDP_highMT[samples.Zlljets] = {"OS":"SR_highSCDP_highMT", "SS":"SR_highSCDP_highMT_SS", "ncuts":4}
addon_regions_highSCDP_highMT[samples.top]     = {"OS":"SR_highSCDP_highMT", "SS":"SR_highSCDP_highMT_SS", "ncuts":4}

addon_regions_lowSCDP_lowMT = {}
addon_regions_lowSCDP_lowMT[data]            = {"SS":"SR_lowSCDP_lowMT_SS", "ncuts":4}
addon_regions_lowSCDP_lowMT[samples.Wjets]   = {"OS":"SR_lowSCDP_lowMT", "SS":"SR_lowSCDP_lowMT_SS", "ncuts":4}
addon_regions_lowSCDP_lowMT[samples.Zlljets] = {"OS":"SR_lowSCDP_lowMT", "SS":"SR_lowSCDP_lowMT_SS", "ncuts":4}
addon_regions_lowSCDP_lowMT[samples.top]     = {"OS":"SR_lowSCDP_lowMT", "SS":"SR_lowSCDP_lowMT_SS", "ncuts":4}

# SIGNAL REGIONS

addon_regions = {}
addon_regions[data]            ={"OS":"SR", "SS":"SR_SS", "OS_lscdp":"SR_lowSCDP", "SS_lscdp":"SR_lowSCDP_SS", "ncuts":4}# {"SS":"SR_SS", "ncuts":4}  
addon_regions[samples.Wjets]   = {"OS":"SR", "SS":"SR_SS", "ncuts":4}
addon_regions[samples.Zlljets] = {"OS":"SR", "SS":"SR_SS", "ncuts":4}
addon_regions[samples.top]     = {"OS":"SR", "SS":"SR_SS", "ncuts":4}

addon_regions_highPT = {}
addon_regions_highPT[data]            = {"OS":"SR_highPT", "SS":"SR_SS_highPT", "OS_lscdp":"SR_lowSCDP_highPT", "SS_lscdp":"SR_lowSCDP_SS_highPT", "ncuts":5}# {"SS":"SR_SS_highPT", "ncuts":5}  
addon_regions_highPT[samples.Wjets]   = {"OS":"SR_highPT", "SS":"SR_SS_highPT", "ncuts":5}
addon_regions_highPT[samples.Zlljets] = {"OS":"SR_highPT", "SS":"SR_SS_highPT", "ncuts":5}#{"OS":"SR_highPT", "SS":"SR_SS_highPT", "ncuts":5}
addon_regions_highPT[samples.top]     = {"OS":"SR_highPT", "SS":"SR_SS_highPT", "ncuts":5}#{"OS":"SR_highPT", "SS":"SR_SS_highPT", "ncuts":5}

addon_regions_lowPT = {}
addon_regions_lowPT[data]            = {"OS":"SR_lowPT", "SS":"SR_SS_lowPT", "OS_lscdp":"SR_lowSCDP_lowPT", "SS_lscdp":"SR_lowSCDP_SS_lowPT","ncuts":5} # {"SS":"SR_SS_lowPT", "ncuts":5}  
addon_regions_lowPT[samples.Wjets]   = {"OS":"SR_lowPT", "SS":"SR_SS_lowPT", "ncuts":5}
addon_regions_lowPT[samples.Zlljets] = {"OS":"SR_lowPT", "SS":"SR_SS_lowPT", "ncuts":5}#{"OS":"SR_lowPT", "SS":"SR_SS_lowPT", "ncuts":5}
addon_regions_lowPT[samples.top]     = {"OS":"SR_lowPT", "SS":"SR_SS_lowPT", "ncuts":5}#{"OS":"SR_lowPT", "SS":"SR_SS_lowPT", "ncuts":5}

addon_regions_25med = {}
addon_regions_25med[data]            = {"OS":"SR_25med", "SS":"SR_SS25med", "OS_lscdp":"SR_lowSCDP_25med", "SS_lscdp":"SR_lowSCDP_SS25med", "ncuts":5}#{"SS":"SR_SS25med", "ncuts":5}  
addon_regions_25med[samples.Wjets]   = {"OS":"SR_25med", "SS":"SR_SS25med", "ncuts":5}#{"OS":"SR_25med", "SS":"SR_SS25med", "ncuts":5}
addon_regions_25med[samples.Zlljets] = {"OS":"SR_25med", "SS":"SR_SS25med", "ncuts":5}#{"OS":"SR_25med", "SS":"SR_SS25med", "ncuts":5}
addon_regions_25med[samples.top]     = {"OS":"SR_25med", "SS":"SR_SS25med", "ncuts":5}#{"OS":"SR_25med", "SS":"SR_SS25med", "ncuts":5}

addon_regions_25med_lowPT = {}
addon_regions_25med_lowPT[data]            = {"OS":"SR_25med_lowPT", "SS":"SR_SS25med_lowPT", "OS_lscdp":"SR_lowSCDP_25med_lowPT", "SS_lscdp":"SR_lowSCDP_SS25med_lowPT", "ncuts":6}  
addon_regions_25med_lowPT[samples.Wjets]   = {"OS":"SR_25med_lowPT", "SS":"SR_SS25med_lowPT", "ncuts":6}
addon_regions_25med_lowPT[samples.Zlljets] = {"OS":"SR_25med_lowPT", "SS":"SR_SS25med_lowPT", "ncuts":6}
addon_regions_25med_lowPT[samples.top]     = {"OS":"SR_25med_lowPT", "SS":"SR_SS25med_lowPT", "ncuts":6}#{"OS":"SR_25med_lowPT", "SS":"SR_SS25med_lowPT", "ncuts":6}

addon_regions_25med_highPT = {}
addon_regions_25med_highPT[data]            = {"OS":"SR_25med_highPT", "SS":"SR_SS25med_highPT", "OS_lscdp":"SR_lowSCDP_25med_highPT", "SS_lscdp":"SR_lowSCDP_SS25med_highPT", "ncuts":6}#{"SS":"SR_SS25med_highPT", "ncuts":6}  
addon_regions_25med_highPT[samples.Wjets]   = {"OS":"SR_25med_highPT", "SS":"SR_SS25med_highPT", "ncuts":6}#{"OS":"SR_25med_highPT", "SS":"SR_SS25med_highPT", "ncuts":6}
addon_regions_25med_highPT[samples.Zlljets] = {"OS":"SR_25med_highPT", "SS":"SR_SS25med_highPT", "ncuts":6}#"OS":"SR_25med_highPT", "SS":"SR_SS25med_highPT", "ncuts":6}
addon_regions_25med_highPT[samples.top]     = {"OS":"SR_25med_highPT", "SS":"SR_SS25med_highPT", "ncuts":6}#{"OS":"SR_25med_highPT", "SS":"SR_SS25med_highPT", "ncuts":6}

addon_regions_35med = {}
addon_regions_35med[data]            = {"OS":"SR_35med", "OS_lscdp":"SR_lowSCDP_35med", "SS_lscdp":"SR_lowSCDP_SS35med","SS":"SR_SS35med", "ncuts":5}  
addon_regions_35med[samples.Wjets]   = {"OS":"SR_35med", "SS":"SR_SS35med", "ncuts":5}
addon_regions_35med[samples.Zlljets] = {"OS":"SR_35med", "SS":"SR_SS_35med", "ncuts":5}
addon_regions_35med[samples.top]     = {"OS":"SR_35med", "SS":"SR_SS_35med", "ncuts":5}

addon_regions_35med_lowPT = {}
addon_regions_35med_lowPT[data]            = {"SS":"SR_SS35med_lowPT", "OS_lscdp":"SR_lowSCDP_35med_lowPT", "SS_lscdp":"SR_lowSCDP_SS35med_lowPT", "OS":"SR_35med_lowPT", "ncuts":6}  
addon_regions_35med_lowPT[samples.Wjets]   = {"OS":"SR_35med_lowPT", "SS":"SR_SS35med_lowPT", "ncuts":6}
addon_regions_35med_lowPT[samples.Zlljets] = {"OS":"SR_35med_lowPT", "SS":"SR_SS35med_lowPT", "ncuts":6}
addon_regions_35med_lowPT[samples.top]     = {"OS":"SR_35med_lowPT", "SS":"SR_SS35med_lowPT", "ncuts":6}

addon_regions_35med_highPT = {}
addon_regions_35med_highPT[data]            = {"SS":"SR_SS35med_highPT",  "OS_lscdp":"SR_lowSCDP_35med_highPT", "SS_lscdp":"SR_lowSCDP_SS35med_highPT","OS":"SR_35med_highPT", "ncuts":6}  
addon_regions_35med_highPT[samples.Wjets]   = {"OS":"SR_35med_highPT", "SS":"SR_SS35med_highPT", "ncuts":6}
addon_regions_35med_highPT[samples.Zlljets] = {"OS":"SR_35med_highPT", "SS":"SR_SS35med_highPT", "ncuts":6}
addon_regions_35med_highPT[samples.top]     = {"OS":"SR_35med_highPT", "SS":"SR_SS35med_highPT", "ncuts":6}

addon_regions_50L1TAU12med = {}
addon_regions_50L1TAU12med[data]            = {"OS":"SR_50L1TAU12med", "OS_lscdp":"SR_lowSCDP_50L1TAU12med", "SS_lscdp":"SR_lowSCDP_SS50L1TAU12med", "SS":"SR_SS50L1TAU12med", "ncuts":5}  
addon_regions_50L1TAU12med[samples.Wjets]   = {"OS":"SR_50L1TAU12med", "SS":"SR_SS50L1TAU12med", "ncuts":5}
addon_regions_50L1TAU12med[samples.Zlljets] = {"OS":"SR_50L1TAU12med", "SS":"SR_SS_50L1TAU12med", "ncuts":5}
addon_regions_50L1TAU12med[samples.top]     = {"OS":"SR_50L1TAU12med", "SS":"SR_SS_50L1TAU12med", "ncuts":5}

addon_regions_50L1TAU12med_lowPT = {}
addon_regions_50L1TAU12med_lowPT[data]            = {"SS":"SR_SS50L1TAU12med_lowPT", "OS_lscdp":"SR_lowSCDP_50L1TAU12med_lowPT", "SS_lscdp":"SR_lowSCDP_SS50L1TAU12med_lowPT", "OS":"SR_50L1TAU12med_lowPT", "ncuts":6}  
addon_regions_50L1TAU12med_lowPT[samples.Wjets]   = {"OS":"SR_50L1TAU12med_lowPT", "SS":"SR_SS50L1TAU12med_lowPT", "ncuts":6}
addon_regions_50L1TAU12med_lowPT[samples.Zlljets] = {"OS":"SR_50L1TAU12med_lowPT", "SS":"SR_SS50L1TAU12med_lowPT", "ncuts":6}
addon_regions_50L1TAU12med_lowPT[samples.top]     = {"OS":"SR_50L1TAU12med_lowPT", "SS":"SR_SS50L1TAU12med_lowPT", "ncuts":6}

addon_regions_50L1TAU12med_highPT = {}
addon_regions_50L1TAU12med_highPT[data]            = {"SS":"SR_SS50L1TAU12med_highPT",  "OS_lscdp":"SR_lowSCDP_50L1TAU12med_highPT", "SS_lscdp":"SR_lowSCDP_SS50L1TAU12med_highPT", "OS":"SR_50L1TAU12med_highPT", "ncuts":6}  
addon_regions_50L1TAU12med_highPT[samples.Wjets]   = {"OS":"SR_50L1TAU12med_highPT", "SS":"SR_SS50L1TAU12med_highPT", "ncuts":6}
addon_regions_50L1TAU12med_highPT[samples.Zlljets] = {"OS":"SR_50L1TAU12med_highPT", "SS":"SR_SS50L1TAU12med_highPT", "ncuts":6}
addon_regions_50L1TAU12med_highPT[samples.top]     = {"OS":"SR_50L1TAU12med_highPT", "SS":"SR_SS50L1TAU12med_highPT", "ncuts":6}

addon_regions_80med = {}
addon_regions_80med[data]            = {"OS":"SR_80med", "OS_lscdp":"SR_lowSCDP_80med", "SS_lscdp":"SR_lowSCDP_SS80med", "SS":"SR_SS80med", "ncuts":5}  
addon_regions_80med[samples.Wjets]   = {"OS":"SR_80med", "SS":"SR_SS80med", "ncuts":5}
addon_regions_80med[samples.Zlljets] = {"OS":"SR_80med", "SS":"SR_SS_80med", "ncuts":5}
addon_regions_80med[samples.top]     = {"OS":"SR_80med", "SS":"SR_SS_80med", "ncuts":5}

addon_regions_80med_lowPT = {}
addon_regions_80med_lowPT[data]            = {"SS":"SR_SS80med_lowPT", "OS_lscdp":"SR_lowSCDP_80med_lowPT", "SS_lscdp":"SR_lowSCDP_SS80med_lowPT","OS":"SR_80med_lowPT", "ncuts":6}  
addon_regions_80med_lowPT[samples.Wjets]   = {"OS":"SR_80med_lowPT", "SS":"SR_SS80med_lowPT", "ncuts":6}
addon_regions_80med_lowPT[samples.Zlljets] = {"OS":"SR_80med_lowPT", "SS":"SR_SS80med_lowPT", "ncuts":6}
addon_regions_80med_lowPT[samples.top]     = {"OS":"SR_80med_lowPT", "SS":"SR_SS80med_lowPT", "ncuts":6}

addon_regions_80med_highPT = {}
addon_regions_80med_highPT[data]            = {"SS":"SR_SS80med_highPT",  "OS_lscdp":"SR_lowSCDP_80med_highPT", "SS_lscdp":"SR_lowSCDP_SS80med_highPT","OS":"SR_80med_highPT", "ncuts":6}  
addon_regions_80med_highPT[samples.Wjets]   = {"OS":"SR_80med_highPT", "SS":"SR_SS80med_highPT", "ncuts":6}
addon_regions_80med_highPT[samples.Zlljets] = {"OS":"SR_80med_highPT", "SS":"SR_SS80med_highPT", "ncuts":6}
addon_regions_80med_highPT[samples.top]     = {"OS":"SR_80med_highPT", "SS":"SR_SS80med_highPT", "ncuts":6}

addon_regions_80L1TAU60med = {}
addon_regions_80L1TAU60med[data]            = {"OS":"SR_80L1TAU60med", "OS_lscdp":"SR_lowSCDP_80L1TAU60med", "SS_lscdp":"SR_lowSCDP_SS80L1TAU60med", "SS":"SR_SS80L1TAU60med", "ncuts":5}  
addon_regions_80L1TAU60med[samples.Wjets]   = {"OS":"SR_80L1TAU60med", "SS":"SR_SS80L1TAU60med", "ncuts":5}
addon_regions_80L1TAU60med[samples.Zlljets] = {"OS":"SR_80L1TAU60med", "SS":"SR_SS_80L1TAU60med", "ncuts":5}
addon_regions_80L1TAU60med[samples.top]     = {"OS":"SR_80L1TAU60med", "SS":"SR_SS_80L1TAU60med", "ncuts":5}

addon_regions_80L1TAU60med_lowPT = {}
addon_regions_80L1TAU60med_lowPT[data]            = {"SS":"SR_SS80L1TAU60med_lowPT", "OS_lscdp":"SR_lowSCDP_80L1TAU60med_lowPT", "SS_lscdp":"SR_lowSCDP_SS80L1TAU60med_lowPT", "OS":"SR_80L1TAU60med_lowPT", "ncuts":6}  
addon_regions_80L1TAU60med_lowPT[samples.Wjets]   = {"OS":"SR_80L1TAU60med_lowPT", "SS":"SR_SS80L1TAU60med_lowPT", "ncuts":6}
addon_regions_80L1TAU60med_lowPT[samples.Zlljets] = {"OS":"SR_80L1TAU60med_lowPT", "SS":"SR_SS80L1TAU60med_lowPT", "ncuts":6}
addon_regions_80L1TAU60med_lowPT[samples.top]     = {"OS":"SR_80L1TAU60med_lowPT", "SS":"SR_SS80L1TAU60med_lowPT", "ncuts":6}

addon_regions_80L1TAU60med_highPT = {}
addon_regions_80L1TAU60med_highPT[data]            = {"SS":"SR_SS80L1TAU60med_highPT",  "OS_lscdp":"SR_lowSCDP_80L1TAU60med_highPT", "SS_lscdp":"SR_lowSCDP_SS80L1TAU60med_highPT","OS":"SR_80L1TAU60med_highPT", "ncuts":6}  
addon_regions_80L1TAU60med_highPT[samples.Wjets]   = {"OS":"SR_80L1TAU60med_highPT", "SS":"SR_SS80L1TAU60med_highPT", "ncuts":6}
addon_regions_80L1TAU60med_highPT[samples.Zlljets] = {"OS":"SR_80L1TAU60med_highPT", "SS":"SR_SS80L1TAU60med_highPT", "ncuts":6}
addon_regions_80L1TAU60med_highPT[samples.top]     = {"OS":"SR_80L1TAU60med_highPT", "SS":"SR_SS80L1TAU60med_highPT", "ncuts":6}

addon_regions_125med = {}
addon_regions_125med[data]            = {"OS":"SR_125med", "OS_lscdp":"SR_lowSCDP_125med", "SS_lscdp":"SR_lowSCDP_SS125med", "SS":"SR_SS125med", "ncuts":5}  
addon_regions_125med[samples.Wjets]   = {"OS":"SR_125med", "SS":"SR_SS125med", "ncuts":5}
addon_regions_125med[samples.Zlljets] = {"OS":"SR_125med", "SS":"SR_SS_125med", "ncuts":5}
addon_regions_125med[samples.top]     = {"OS":"SR_125med", "SS":"SR_SS_125med", "ncuts":5}

addon_regions_125med_lowPT = {}
addon_regions_125med_lowPT[data]            = {"SS":"SR_SS125med_lowPT", "OS_lscdp":"SR_lowSCDP_125med_lowPT", "SS_lscdp":"SR_lowSCDP_SS125med_lowPT", "OS":"SR_125med_lowPT", "ncuts":6}  
addon_regions_125med_lowPT[samples.Wjets]   = {"OS":"SR_125med_lowPT", "SS":"SR_SS125med_lowPT", "ncuts":6}
addon_regions_125med_lowPT[samples.Zlljets] = {"OS":"SR_125med_lowPT", "SS":"SR_SS125med_lowPT", "ncuts":6}
addon_regions_125med_lowPT[samples.top]     = {"OS":"SR_125med_lowPT", "SS":"SR_SS125med_lowPT", "ncuts":6}

addon_regions_125med_highPT = {}
addon_regions_125med_highPT[data]            = {"SS":"SR_SS125med_highPT",  "OS_lscdp":"SR_lowSCDP_125med_highPT", "SS_lscdp":"SR_lowSCDP_SS125med_highPT", "OS":"SR_125med_highPT", "ncuts":6}  
addon_regions_125med_highPT[samples.Wjets]   = {"OS":"SR_125med_highPT", "SS":"SR_SS125med_highPT", "ncuts":6}
addon_regions_125med_highPT[samples.Zlljets] = {"OS":"SR_125med_highPT", "SS":"SR_SS125med_highPT", "ncuts":6}
addon_regions_125med_highPT[samples.top]     = {"OS":"SR_125med_highPT", "SS":"SR_SS125med_highPT", "ncuts":6}

addon_regions_160med = {}
addon_regions_160med[data]            = {"OS":"SR_160med", "OS_lscdp":"SR_lowSCDP_160med", "SS_lscdp":"SR_lowSCDP_SS160med", "SS":"SR_SS160med", "ncuts":5}  
addon_regions_160med[samples.Wjets]   = {"OS":"SR_160med", "SS":"SR_SS160med", "ncuts":5}
addon_regions_160med[samples.Zlljets] = {"OS":"SR_160med", "SS":"SR_SS_160med", "ncuts":5}
addon_regions_160med[samples.top]     = {"OS":"SR_160med", "SS":"SR_SS_160med", "ncuts":5}

addon_regions_160med_lowPT = {}
addon_regions_160med_lowPT[data]            = {"SS":"SR_SS160med_lowPT", "OS_lscdp":"SR_lowSCDP_160med_lowPT", "SS_lscdp":"SR_lowSCDP_SS160med_lowPT", "OS":"SR_160med_lowPT", "ncuts":6}  
addon_regions_160med_lowPT[samples.Wjets]   = {"OS":"SR_160med_lowPT", "SS":"SR_SS160med_lowPT", "ncuts":6}
addon_regions_160med_lowPT[samples.Zlljets] = {"OS":"SR_160med_lowPT", "SS":"SR_SS160med_lowPT", "ncuts":6}
addon_regions_160med_lowPT[samples.top]     = {"OS":"SR_160med_lowPT", "SS":"SR_SS160med_lowPT", "ncuts":6}

addon_regions_160med_highPT = {}
addon_regions_160med_highPT[data]            = {"SS":"SR_SS160med_highPT",  "OS_lscdp":"SR_lowSCDP_160med_highPT", "SS_lscdp":"SR_lowSCDP_SS160med_highPT", "OS":"SR_160med_highPT", "ncuts":6}  
addon_regions_160med_highPT[samples.Wjets]   = {"OS":"SR_160med_highPT", "SS":"SR_SS160med_highPT", "ncuts":6}
addon_regions_160med_highPT[samples.Zlljets] = {"OS":"SR_160med_highPT", "SS":"SR_SS160med_highPT", "ncuts":6}
addon_regions_160med_highPT[samples.top]     = {"OS":"SR_160med_highPT", "SS":"SR_SS160med_highPT", "ncuts":6}

addon_regions_L1TAU12IMmed = {}
addon_regions_L1TAU12IMmed[data]            = {"OS":"SR_L1TAU12IMmed", "OS_lscdp":"SR_lowSCDP_L1TAU12IMmed", "SS_lscdp":"SR_lowSCDP_SSL1TAU12IMmed", "SS":"SR_SSL1TAU12IMmed", "ncuts":5}  
addon_regions_L1TAU12IMmed[samples.Wjets]   = {"OS":"SR_L1TAU12IMmed", "SS":"SR_SSL1TAU12IMmed", "ncuts":5}
addon_regions_L1TAU12IMmed[samples.Zlljets] = {"OS":"SR_L1TAU12IMmed", "SS":"SR_SS_L1TAU12IMmed", "ncuts":5}
addon_regions_L1TAU12IMmed[samples.top]     = {"OS":"SR_L1TAU12IMmed", "SS":"SR_SS_L1TAU12IMmed", "ncuts":5}

addon_regions_L1TAU12IMmed_lowPT = {}
addon_regions_L1TAU12IMmed_lowPT[data]            = {"SS":"SR_SSL1TAU12IMmed_lowPT", "OS_lscdp":"SR_lowSCDP_L1TAU12IMmed_lowPT", "SS_lscdp":"SR_lowSCDP_SSL1TAU12IMmed_lowPT", "OS":"SR_L1TAU12IMmed_lowPT", "ncuts":6}  
addon_regions_L1TAU12IMmed_lowPT[samples.Wjets]   = {"OS":"SR_L1TAU12IMmed_lowPT", "SS":"SR_SSL1TAU12IMmed_lowPT", "ncuts":6}
addon_regions_L1TAU12IMmed_lowPT[samples.Zlljets] = {"OS":"SR_L1TAU12IMmed_lowPT", "SS":"SR_SSL1TAU12IMmed_lowPT", "ncuts":6}
addon_regions_L1TAU12IMmed_lowPT[samples.top]     = {"OS":"SR_L1TAU12IMmed_lowPT", "SS":"SR_SSL1TAU12IMmed_lowPT", "ncuts":6}

addon_regions_L1TAU12IMmed_highPT = {}
addon_regions_L1TAU12IMmed_highPT[data]            = {"SS":"SR_SSL1TAU12IMmed_highPT",  "OS_lscdp":"SR_lowSCDP_L1TAU12IMmed_highPT", "SS_lscdp":"SR_lowSCDP_SSL1TAU12IMmed_highPT", "OS":"SR_L1TAU12IMmed_highPT", "ncuts":6}  
addon_regions_L1TAU12IMmed_highPT[samples.Wjets]   = {"OS":"SR_L1TAU12IMmed_highPT", "SS":"SR_SSL1TAU12IMmed_highPT", "ncuts":6}
addon_regions_L1TAU12IMmed_highPT[samples.Zlljets] = {"OS":"SR_L1TAU12IMmed_highPT", "SS":"SR_SSL1TAU12IMmed_highPT", "ncuts":6}
addon_regions_L1TAU12IMmed_highPT[samples.top]     = {"OS":"SR_L1TAU12IMmed_highPT", "SS":"SR_SSL1TAU12IMmed_highPT", "ncuts":6}

addon_regions_ptonly = {}
addon_regions_ptonly[data]            = {"OS":"SR_ptonly", "OS_lscdp":"SR_lowSCDP_ptonly", "SS_lscdp":"SR_lowSCDP_SSptonly", "SS":"SR_SSptonly", "ncuts":5}  
addon_regions_ptonly[samples.Wjets]   = {"OS":"SR_ptonly", "SS":"SR_SSptonly", "ncuts":5}
addon_regions_ptonly[samples.Zlljets] = {"OS":"SR_ptonly", "SS":"SR_SS_ptonly", "ncuts":5}
addon_regions_ptonly[samples.top]     = {"OS":"SR_ptonly", "SS":"SR_SS_ptonly", "ncuts":5}

addon_regions_ptonly_lowPT = {}
addon_regions_ptonly_lowPT[data]            = {"SS":"SR_SSptonly_lowPT", "OS_lscdp":"SR_lowSCDP_ptonly_lowPT", "SS_lscdp":"SR_lowSCDP_SSptonly_lowPT", "OS":"SR_ptonly_lowPT", "ncuts":6}  
addon_regions_ptonly_lowPT[samples.Wjets]   = {"OS":"SR_ptonly_lowPT", "SS":"SR_SSptonly_lowPT", "ncuts":6}
addon_regions_ptonly_lowPT[samples.Zlljets] = {"OS":"SR_ptonly_lowPT", "SS":"SR_SSptonly_lowPT", "ncuts":6}
addon_regions_ptonly_lowPT[samples.top]     = {"OS":"SR_ptonly_lowPT", "SS":"SR_SSptonly_lowPT", "ncuts":6}

addon_regions_ptonly_highPT = {}
addon_regions_ptonly_highPT[data]            = {"SS":"SR_SSptonly_highPT",  "OS_lscdp":"SR_lowSCDP_ptonly_highPT", "SS_lscdp":"SR_lowSCDP_SSptonly_highPT", "OS":"SR_ptonly_highPT", "ncuts":6}  
addon_regions_ptonly_highPT[samples.Wjets]   = {"OS":"SR_ptonly_highPT", "SS":"SR_SSptonly_highPT", "ncuts":6}
addon_regions_ptonly_highPT[samples.Zlljets] = {"OS":"SR_ptonly_highPT", "SS":"SR_SSptonly_highPT", "ncuts":6}
addon_regions_ptonly_highPT[samples.top]     = {"OS":"SR_ptonly_highPT", "SS":"SR_SSptonly_highPT", "ncuts":6}

addon_regions_tracktwo = {}
addon_regions_tracktwo[data]            = {"OS":"SR_tracktwo", "OS_lscdp":"SR_lowSCDP_tracktwo", "SS_lscdp":"SR_lowSCDP_SStracktwo", "SS":"SR_SStracktwo", "ncuts":5}  
addon_regions_tracktwo[samples.Wjets]   = {"OS":"SR_tracktwo", "SS":"SR_SStracktwo", "ncuts":5}
addon_regions_tracktwo[samples.Zlljets] = {"OS":"SR_tracktwo", "SS":"SR_SS_tracktwo", "ncuts":5}
addon_regions_tracktwo[samples.top]     = {"OS":"SR_tracktwo", "SS":"SR_SS_tracktwo", "ncuts":5}

addon_regions_tracktwo_lowPT = {}
addon_regions_tracktwo_lowPT[data]            = {"SS":"SR_SStracktwo_lowPT", "OS_lscdp":"SR_lowSCDP_tracktwo_lowPT", "SS_lscdp":"SR_lowSCDP_tracktwo_lowPT", "OS":"SR_tracktwo_lowPT", "ncuts":6}  
addon_regions_tracktwo_lowPT[samples.Wjets]   = {"OS":"SR_tracktwo_lowPT", "SS":"SR_SStracktwo_lowPT", "ncuts":6}
addon_regions_tracktwo_lowPT[samples.Zlljets] = {"OS":"SR_tracktwo_lowPT", "SS":"SR_SStracktwo_lowPT", "ncuts":6}
addon_regions_tracktwo_lowPT[samples.top]     = {"OS":"SR_tracktwo_lowPT", "SS":"SR_SStracktwo_lowPT", "ncuts":6}

addon_regions_tracktwo_highPT = {}
addon_regions_tracktwo_highPT[data]            = {"SS":"SR_SStracktwo_highPT",  "OS_lscdp":"SR_lowSCDP_tracktwo_highPT", "SS_lscdp":"SR_lowSCDP_tracktwo_highPT", "OS":"SR_tracktwo_highPT", "ncuts":6}  
addon_regions_tracktwo_highPT[samples.Wjets]   = {"OS":"SR_tracktwo_highPT", "SS":"SR_SStracktwo_highPT", "ncuts":6}
addon_regions_tracktwo_highPT[samples.Zlljets] = {"OS":"SR_tracktwo_highPT", "SS":"SR_SStracktwo_highPT", "ncuts":6}
addon_regions_tracktwo_highPT[samples.top]     = {"OS":"SR_tracktwo_highPT", "SS":"SR_SStracktwo_highPT", "ncuts":6}

#--------------------
# one track
#--------------------

addon_regions_1Track = {}
addon_regions_1Track[data]            = {"OS":"SR_Tau1Track", "SS":"SR_SS_Tau1Track", "OS_lscdp":"SR_lowSCDP_Tau1Track", "SS_lscdp":"SR_lowSCDP_SS_Tau1Track","ncuts":5}#{"SS":"SR_SS_Tau1Track", "ncuts":5}  
addon_regions_1Track[samples.Wjets]   = {"OS":"SR_Tau1Track", "SS":"SR_SS_Tau1Track", "ncuts":5}#{"OS":"SR_Tau1Track", "SS":"SR_SS_Tau1Track", "ncuts":5}
addon_regions_1Track[samples.Zlljets] = {"OS":"SR_Tau1Track", "SS":"SR_SS_Tau1Track", "ncuts":5}#{"OS":"SR_Tau1Track", "SS":"SR_SS_Tau1Track", "ncuts":5}
addon_regions_1Track[samples.top]     = {"OS":"SR_Tau1Track", "SS":"SR_SS_Tau1Track", "ncuts":5}#{"OS":"SR_Tau1Track", "SS":"SR_SS_Tau1Track", "ncuts":5}

addon_regions_highPT_1Track = {}
addon_regions_highPT_1Track[data]            = {"OS":"SR_highPT_Tau1Track", "SS":"SR_SS_highPT_Tau1Track", "OS_lscdp":"SR_lowSCDP_highPT_Tau1Track", "SS_lscdp":"SR_lowSCDP_SS_highPT_Tau1Track", "ncuts":6}#{"SS":"SR_SS_highPT_Tau1Track", "ncuts":6}  
addon_regions_highPT_1Track[samples.Wjets]   = {"OS":"SR_highPT_Tau1Track", "SS":"SR_SS_highPT_Tau1Track","ncuts":6}#{"OS":"SR_highPT_Tau1Track", "SS":"SR_SS_highPT_Tau1Track", "ncuts":6}
addon_regions_highPT_1Track[samples.Zlljets] = {"OS":"SR_highPT_Tau1Track", "SS":"SR_SS_highPT_Tau1Track","ncuts":6}#{"OS":"SR_highPT_Tau1Track", "SS":"SR_SS_highPT_Tau1Track", "ncuts":6}
addon_regions_highPT_1Track[samples.top]     = {"OS":"SR_highPT_Tau1Track", "SS":"SR_SS_highPT_Tau1Track","ncuts":6}

addon_regions_lowPT_1Track = {}
addon_regions_lowPT_1Track[data]            = {"OS":"SR_lowPT_Tau1Track", "SS":"SR_SS_lowPT_Tau1Track", "OS_lscdp":"SR_lowSCDP_lowPT_Tau1Track", "SS_lscdp":"SR_lowSCDP_SS_lowPT_Tau1Track","ncuts":6}#{"SS":"SR_SS_lowPT_Tau1Track", "ncuts":6}  
addon_regions_lowPT_1Track[samples.Wjets]   = {"OS":"SR_lowPT_Tau1Track", "SS":"SR_SS_lowPT_Tau1Track", "ncuts":6}#{"OS":"SR_lowPT_Tau1Track", "SS":"SR_SS_lowPT_Tau1Track", "ncuts":6}
addon_regions_lowPT_1Track[samples.Zlljets] = {"OS":"SR_lowPT_Tau1Track", "SS":"SR_SS_lowPT_Tau1Track", "ncuts":6}#{"OS":"SR_lowPT_Tau1Track", "SS":"SR_SS_lowPT_Tau1Track", "ncuts":6}
addon_regions_lowPT_1Track[samples.top]     = {"OS":"SR_lowPT_Tau1Track", "SS":"SR_SS_lowPT_Tau1Track", "ncuts":6}


addon_regions_25med_1Track = {}
addon_regions_25med_1Track[data]            = {"OS":"SR_25med_Tau1Track", "SS":"SR_SS25med_Tau1Track", "OS_lscdp":"SR_lowSCDP_25med_Tau1Track", "SS_lscdp":"SR_lowSCDP_SS25med_Tau1Track","ncuts":6}#'SR_lowSCDP_'+str(triggers[i])+'med_Tau'+str(trax[j])+'Track',{"SS":"SR_SS25med_Tau1Track", "ncuts":6}  
addon_regions_25med_1Track[samples.Wjets]   = {"OS":"SR_25med_Tau1Track", "SS":"SR_SS25med_Tau1Track","ncuts":6}
addon_regions_25med_1Track[samples.Zlljets] = {"OS":"SR_25med_Tau1Track", "SS":"SR_SS25med_Tau1Track", "ncuts":6}
addon_regions_25med_1Track[samples.top]     = {"OS":"SR_25med_Tau1Track", "SS":"SR_SS25med_Tau1Track","ncuts":6}

addon_regions_25med_lowPT_1Track = {}
addon_regions_25med_lowPT_1Track[data]            = {"OS":"SR_25med_lowPT_Tau1Track", "SS":"SR_SS25med_lowPT_Tau1Track", "OS_lscdp":"SR_lowSCDP_25med_lowPT_Tau1Track", "SS_lscdp":"SR_lowSCDP_SS25med_lowPT_Tau1Track", "ncuts":7}#{"SS":"SR_SS25med_lowPT_Tau1Track", "ncuts":7}  
addon_regions_25med_lowPT_1Track[samples.Wjets]   = {"OS":"SR_25med_lowPT_Tau1Track", "SS":"SR_SS25med_lowPT_Tau1Track", "ncuts":7}
addon_regions_25med_lowPT_1Track[samples.Zlljets] = {"OS":"SR_25med_lowPT_Tau1Track", "SS":"SR_SS25med_lowPT_Tau1Track", "ncuts":7}
addon_regions_25med_lowPT_1Track[samples.top]     = {"OS":"SR_25med_lowPT_Tau1Track", "SS":"SR_SS25med_lowPT_Tau1Track", "ncuts":7}

addon_regions_25med_highPT_1Track = {}
addon_regions_25med_highPT_1Track[data]            = {"OS":"SR_25med_highPT_Tau1Track", "SS":"SR_SS25med_highPT_Tau1Track", "OS_lscdp":"SR_lowSCDP_25med_highPT_Tau1Track", "SS_lscdp":"SR_lowSCDP_SS25med_highPT_Tau1Track", "ncuts":7}#{"SS":"SR_SS25med_highPT_Tau1Track", "ncuts":7}  
addon_regions_25med_highPT_1Track[samples.Wjets]   = {"OS":"SR_25med_highPT_Tau1Track", "SS":"SR_SS25med_highPT_Tau1Track","ncuts":7}
addon_regions_25med_highPT_1Track[samples.Zlljets] = {"OS":"SR_25med_highPT_Tau1Track", "SS":"SR_SS25med_highPT_Tau1Track", "ncuts":7}
addon_regions_25med_highPT_1Track[samples.top]     = {"OS":"SR_25med_highPT_Tau1Track", "SS":"SR_SS25med_highPT_Tau1Track", "ncuts":7}

addon_regions_35med_1Track = {}
addon_regions_35med_1Track[data]            = {"OS_lscdp":"SR_lowSCDP_35med_Tau1Track", "SS_lscdp":"SR_lowSCDP_SS35med_Tau1Track","OS":"SR_35med_Tau1Track", "SS":"SR_SS35med_Tau1Track", "ncuts":6}  
addon_regions_35med_1Track[samples.Wjets]   = {"OS":"SR_35med_Tau1Track", "SS":"SR_SS35med_Tau1Track", "ncuts":6}
addon_regions_35med_1Track[samples.Zlljets] = {"OS":"SR_35med_Tau1Track", "SS":"SR_SS35med_Tau1Track", "ncuts":6}
addon_regions_35med_1Track[samples.top]     = {"OS":"SR_35med_Tau1Track", "SS":"SR_SS35med_Tau1Track", "ncuts":6}

addon_regions_35med_lowPT_1Track = {}
addon_regions_35med_lowPT_1Track[data]            = {"SS":"SR_SS35med_lowPT_Tau1Track", "OS_lscdp":"SR_lowSCDP_35med_lowPT_Tau1Track", "SS_lscdp":"SR_lowSCDP_SS35med_lowPT_Tau1Track", "OS":"SR_35med_lowPT_Tau1Track", "ncuts":7}  
addon_regions_35med_lowPT_1Track[samples.Wjets]   = {"OS":"SR_35med_lowPT_Tau1Track", "SS":"SR_SS35med_lowPT_Tau1Track", "ncuts":7}
addon_regions_35med_lowPT_1Track[samples.Zlljets] = {"OS":"SR_35med_lowPT_Tau1Track", "SS":"SR_SS35med_lowPT_Tau1Track", "ncuts":7}
addon_regions_35med_lowPT_1Track[samples.top]     = {"OS":"SR_35med_lowPT_Tau1Track", "SS":"SR_SS35med_lowPT_Tau1Track", "ncuts":7}

addon_regions_35med_highPT_1Track = {}
addon_regions_35med_highPT_1Track[data]            = {"SS":"SR_SS35med_highPT_Tau1Track", "OS_lscdp":"SR_lowSCDP_35med_highPT_Tau1Track", "SS_lscdp":"SR_lowSCDP_SS35med_highPT_Tau1Track", "OS":"SR_35med_highPT_Tau1Track","ncuts":7}  
addon_regions_35med_highPT_1Track[samples.Wjets]   = {"OS":"SR_35med_highPT_Tau1Track", "SS":"SR_SS35med_highPT_Tau1Track", "ncuts":7}
addon_regions_35med_highPT_1Track[samples.Zlljets] = {"OS":"SR_35med_highPT_Tau1Track", "SS":"SR_SS35med_highPT_Tau1Track", "ncuts":7}
addon_regions_35med_highPT_1Track[samples.top]     = {"OS":"SR_35med_highPT_Tau1Track", "SS":"SR_SS35med_highPT_Tau1Track", "ncuts":7}

addon_regions_50L1TAU12med_1Track = {}
addon_regions_50L1TAU12med_1Track[data]            = {"OS_lscdp":"SR_lowSCDP_50L1TAU12med_Tau1Track", "SS_lscdp":"SR_lowSCDP_SS50L1TAU12med_Tau1Track", "OS":"SR_50L1TAU12med_Tau1Track", "SS":"SR_SS50L1TAU12med_Tau1Track", "ncuts":6}  
addon_regions_50L1TAU12med_1Track[samples.Wjets]   = {"OS":"SR_50L1TAU12med_Tau1Track", "SS":"SR_SS50L1TAU12med_Tau1Track", "ncuts":6}
addon_regions_50L1TAU12med_1Track[samples.Zlljets] = {"OS":"SR_50L1TAU12med_Tau1Track", "SS":"SR_SS50L1TAU12med_Tau1Track", "ncuts":6}
addon_regions_50L1TAU12med_1Track[samples.top]     = {"OS":"SR_50L1TAU12med_Tau1Track", "SS":"SR_SS50L1TAU12med_Tau1Track", "ncuts":6}

addon_regions_50L1TAU12med_lowPT_1Track = {}
addon_regions_50L1TAU12med_lowPT_1Track[data]            = {"SS":"SR_SS50L1TAU12med_lowPT_Tau1Track", "OS_lscdp":"SR_lowSCDP_50L1TAU12med_lowPT_Tau1Track", "SS_lscdp":"SR_lowSCDP_SS50L1TAU12med_lowPT_Tau1Track", "OS":"SR_50L1TAU12med_lowPT_Tau1Track", "ncuts":7}  
addon_regions_50L1TAU12med_lowPT_1Track[samples.Wjets]   = {"OS":"SR_50L1TAU12med_lowPT_Tau1Track", "SS":"SR_SS50L1TAU12med_lowPT_Tau1Track", "ncuts":7}
addon_regions_50L1TAU12med_lowPT_1Track[samples.Zlljets] = {"OS":"SR_50L1TAU12med_lowPT_Tau1Track", "SS":"SR_SS50L1TAU12med_lowPT_Tau1Track", "ncuts":7}
addon_regions_50L1TAU12med_lowPT_1Track[samples.top]     = {"OS":"SR_50L1TAU12med_lowPT_Tau1Track", "SS":"SR_SS50L1TAU12med_lowPT_Tau1Track", "ncuts":7}

addon_regions_50L1TAU12med_highPT_1Track = {}
addon_regions_50L1TAU12med_highPT_1Track[data]            = {"SS":"SR_SS50L1TAU12med_highPT_Tau1Track", "OS_lscdp":"SR_lowSCDP_50L1TAU12med_highPT_Tau1Track", "SS_lscdp":"SR_lowSCDP_SS50L1TAU12med_highPT_Tau1Track", "OS":"SR_50L1TAU12med_highPT_Tau1Track","ncuts":7}  
addon_regions_50L1TAU12med_highPT_1Track[samples.Wjets]   = {"OS":"SR_50L1TAU12med_highPT_Tau1Track", "SS":"SR_SS50L1TAU12med_highPT_Tau1Track", "ncuts":7}
addon_regions_50L1TAU12med_highPT_1Track[samples.Zlljets] = {"OS":"SR_50L1TAU12med_highPT_Tau1Track", "SS":"SR_SS50L1TAU12med_highPT_Tau1Track", "ncuts":7}
addon_regions_50L1TAU12med_highPT_1Track[samples.top]     = {"OS":"SR_50L1TAU12med_highPT_Tau1Track", "SS":"SR_SS50L1TAU12med_highPT_Tau1Track", "ncuts":7}

addon_regions_80med_1Track = {}
addon_regions_80med_1Track[data]            = {"OS_lscdp":"SR_lowSCDP_80med_Tau1Track", "SS_lscdp":"SR_lowSCDP_SS80med_Tau1Track", "OS":"SR_80med_Tau1Track", "SS":"SR_SS80med_Tau1Track", "ncuts":6}  
addon_regions_80med_1Track[samples.Wjets]   = {"OS":"SR_80med_Tau1Track", "SS":"SR_SS80med_Tau1Track", "ncuts":6}
addon_regions_80med_1Track[samples.Zlljets] = {"OS":"SR_80med_Tau1Track", "SS":"SR_SS80med_Tau1Track", "ncuts":6}
addon_regions_80med_1Track[samples.top]     = {"OS":"SR_80med_Tau1Track", "SS":"SR_SS80med_Tau1Track", "ncuts":6}

addon_regions_80med_lowPT_1Track = {}
addon_regions_80med_lowPT_1Track[data]            = {"SS":"SR_SS80med_lowPT_Tau1Track", "OS_lscdp":"SR_lowSCDP_80med_lowPT_Tau1Track", "SS_lscdp":"SR_lowSCDP_SS80med_lowPT_Tau1Track", "OS":"SR_80med_lowPT_Tau1Track", "ncuts":7}  
addon_regions_80med_lowPT_1Track[samples.Wjets]   = {"OS":"SR_80med_lowPT_Tau1Track", "SS":"SR_SS80med_lowPT_Tau1Track", "ncuts":7}
addon_regions_80med_lowPT_1Track[samples.Zlljets] = {"OS":"SR_80med_lowPT_Tau1Track", "SS":"SR_SS80med_lowPT_Tau1Track", "ncuts":7}
addon_regions_80med_lowPT_1Track[samples.top]     = {"OS":"SR_80med_lowPT_Tau1Track", "SS":"SR_SS80med_lowPT_Tau1Track", "ncuts":7}

addon_regions_80med_highPT_1Track = {}
addon_regions_80med_highPT_1Track[data]            = {"SS":"SR_SS80med_highPT_Tau1Track", "OS_lscdp":"SR_lowSCDP_80med_highPT_Tau1Track", "SS_lscdp":"SR_lowSCDP_SS80med_highPT_Tau1Track","OS":"SR_80med_highPT_Tau1Track","ncuts":7}  
addon_regions_80med_highPT_1Track[samples.Wjets]   = {"OS":"SR_80med_highPT_Tau1Track", "SS":"SR_SS80med_highPT_Tau1Track", "ncuts":7}
addon_regions_80med_highPT_1Track[samples.Zlljets] = {"OS":"SR_80med_highPT_Tau1Track", "SS":"SR_SS80med_highPT_Tau1Track", "ncuts":7}
addon_regions_80med_highPT_1Track[samples.top]     = {"OS":"SR_80med_highPT_Tau1Track", "SS":"SR_SS80med_highPT_Tau1Track", "ncuts":7}

addon_regions_80L1TAU60med_1Track = {}
addon_regions_80L1TAU60med_1Track[data]            = {"OS_lscdp":"SR_lowSCDP_80L1TAU60med_Tau1Track", "SS_lscdp":"SR_lowSCDP_SS80L1TAU60med_Tau1Track","OS":"SR_80L1TAU60med_Tau1Track", "SS":"SR_SS80L1TAU60med_Tau1Track", "ncuts":6}  
addon_regions_80L1TAU60med_1Track[samples.Wjets]   = {"OS":"SR_80L1TAU60med_Tau1Track", "SS":"SR_SS80L1TAU60med_Tau1Track", "ncuts":6}
addon_regions_80L1TAU60med_1Track[samples.Zlljets] = {"OS":"SR_80L1TAU60med_Tau1Track", "SS":"SR_SS80L1TAU60med_Tau1Track", "ncuts":6}
addon_regions_80L1TAU60med_1Track[samples.top]     = {"OS":"SR_80L1TAU60med_Tau1Track", "SS":"SR_SS80L1TAU60med_Tau1Track", "ncuts":6}

addon_regions_80L1TAU60med_lowPT_1Track = {}
addon_regions_80L1TAU60med_lowPT_1Track[data]            = {"SS":"SR_SS80L1TAU60med_lowPT_Tau1Track", "OS_lscdp":"SR_lowSCDP_80L1TAU60med_lowPT_Tau1Track", "SS_lscdp":"SR_lowSCDP_SS80L1TAU60med_lowPT_Tau1Track","OS":"SR_80L1TAU60med_lowPT_Tau1Track", "ncuts":7}  
addon_regions_80L1TAU60med_lowPT_1Track[samples.Wjets]   = {"OS":"SR_80L1TAU60med_lowPT_Tau1Track", "SS":"SR_SS80L1TAU60med_lowPT_Tau1Track", "ncuts":7}
addon_regions_80L1TAU60med_lowPT_1Track[samples.Zlljets] = {"OS":"SR_80L1TAU60med_lowPT_Tau1Track", "SS":"SR_SS80L1TAU60med_lowPT_Tau1Track", "ncuts":7}
addon_regions_80L1TAU60med_lowPT_1Track[samples.top]     = {"OS":"SR_80L1TAU60med_lowPT_Tau1Track", "SS":"SR_SS80L1TAU60med_lowPT_Tau1Track", "ncuts":7}

addon_regions_80L1TAU60med_highPT_1Track = {}
addon_regions_80L1TAU60med_highPT_1Track[data]            = {"SS":"SR_SS80L1TAU60med_highPT_Tau1Track", "OS_lscdp":"SR_lowSCDP_80L1TAU60med_highPT_Tau1Track", "SS_lscdp":"SR_lowSCDP_SS80L1TAU60med_highPT_Tau1Track", "OS":"SR_80L1TAU60med_highPT_Tau1Track","ncuts":7}  
addon_regions_80L1TAU60med_highPT_1Track[samples.Wjets]   = {"OS":"SR_80L1TAU60med_highPT_Tau1Track", "SS":"SR_SS80L1TAU60med_highPT_Tau1Track", "ncuts":7}
addon_regions_80L1TAU60med_highPT_1Track[samples.Zlljets] = {"OS":"SR_80L1TAU60med_highPT_Tau1Track", "SS":"SR_SS80L1TAU60med_highPT_Tau1Track", "ncuts":7}
addon_regions_80L1TAU60med_highPT_1Track[samples.top]     = {"OS":"SR_80L1TAU60med_highPT_Tau1Track", "SS":"SR_SS80L1TAU60med_highPT_Tau1Track", "ncuts":7}

addon_regions_125med_1Track = {}
addon_regions_125med_1Track[data]            = {"OS_lscdp":"SR_lowSCDP_125med_Tau1Track", "SS_lscdp":"SR_lowSCDP_SS125med_Tau1Track","OS":"SR_125med_Tau1Track", "SS":"SR_SS125med_Tau1Track", "ncuts":6}  
addon_regions_125med_1Track[samples.Wjets]   = {"OS":"SR_125med_Tau1Track", "SS":"SR_SS125med_Tau1Track", "ncuts":6}
addon_regions_125med_1Track[samples.Zlljets] = {"OS":"SR_125med_Tau1Track", "SS":"SR_SS125med_Tau1Track", "ncuts":6}
addon_regions_125med_1Track[samples.top]     = {"OS":"SR_125med_Tau1Track", "SS":"SR_SS125med_Tau1Track", "ncuts":6}

addon_regions_125med_lowPT_1Track = {}
addon_regions_125med_lowPT_1Track[data]            = {"SS":"SR_SS125med_lowPT_Tau1Track", "OS_lscdp":"SR_lowSCDP_125med_lowPT_Tau1Track", "SS_lscdp":"SR_lowSCDP_SS125med_lowPT_Tau1Track", "OS":"SR_125med_lowPT_Tau1Track", "ncuts":7}  
addon_regions_125med_lowPT_1Track[samples.Wjets]   = {"OS":"SR_125med_lowPT_Tau1Track", "SS":"SR_SS125med_lowPT_Tau1Track", "ncuts":7}
addon_regions_125med_lowPT_1Track[samples.Zlljets] = {"OS":"SR_125med_lowPT_Tau1Track", "SS":"SR_SS125med_lowPT_Tau1Track", "ncuts":7}
addon_regions_125med_lowPT_1Track[samples.top]     = {"OS":"SR_125med_lowPT_Tau1Track", "SS":"SR_SS125med_lowPT_Tau1Track", "ncuts":7}

addon_regions_125med_highPT_1Track = {}
addon_regions_125med_highPT_1Track[data]            = {"SS":"SR_SS125med_highPT_Tau1Track", "OS_lscdp":"SR_lowSCDP_125med_highPT_Tau1Track", "SS_lscdp":"SR_lowSCDP_SS125med_highPT_Tau1Track", "OS":"SR_125med_highPT_Tau1Track","ncuts":7}  
addon_regions_125med_highPT_1Track[samples.Wjets]   = {"OS":"SR_125med_highPT_Tau1Track", "SS":"SR_SS125med_highPT_Tau1Track", "ncuts":7}
addon_regions_125med_highPT_1Track[samples.Zlljets] = {"OS":"SR_125med_highPT_Tau1Track", "SS":"SR_SS125med_highPT_Tau1Track", "ncuts":7}
addon_regions_125med_highPT_1Track[samples.top]     = {"OS":"SR_125med_highPT_Tau1Track", "SS":"SR_SS125med_highPT_Tau1Track", "ncuts":7}

addon_regions_160med_1Track = {}
addon_regions_160med_1Track[data]            = {"OS_lscdp":"SR_lowSCDP_160med_Tau1Track", "SS_lscdp":"SR_lowSCDP_SS160med_Tau1Track", "OS":"SR_160med_Tau1Track", "SS":"SR_SS160med_Tau1Track", "ncuts":6}  
addon_regions_160med_1Track[samples.Wjets]   = {"OS":"SR_160med_Tau1Track", "SS":"SR_SS160med_Tau1Track", "ncuts":6}
addon_regions_160med_1Track[samples.Zlljets] = {"OS":"SR_160med_Tau1Track", "SS":"SR_SS160med_Tau1Track", "ncuts":6}
addon_regions_160med_1Track[samples.top]     = {"OS":"SR_160med_Tau1Track", "SS":"SR_SS160med_Tau1Track", "ncuts":6}

addon_regions_160med_lowPT_1Track = {}
addon_regions_160med_lowPT_1Track[data]            = {"SS":"SR_SS160med_lowPT_Tau1Track", "OS_lscdp":"SR_lowSCDP_160med_lowPT_Tau1Track", "SS_lscdp":"SR_lowSCDP_SS160med_lowPT_Tau1Track", "OS":"SR_160med_lowPT_Tau1Track", "ncuts":7}  
addon_regions_160med_lowPT_1Track[samples.Wjets]   = {"OS":"SR_160med_lowPT_Tau1Track", "SS":"SR_SS160med_lowPT_Tau1Track", "ncuts":7}
addon_regions_160med_lowPT_1Track[samples.Zlljets] = {"OS":"SR_160med_lowPT_Tau1Track", "SS":"SR_SS160med_lowPT_Tau1Track", "ncuts":7}
addon_regions_160med_lowPT_1Track[samples.top]     = {"OS":"SR_160med_lowPT_Tau1Track", "SS":"SR_SS160med_lowPT_Tau1Track", "ncuts":7}

addon_regions_160med_highPT_1Track = {}
addon_regions_160med_highPT_1Track[data]            = {"SS":"SR_SS160med_highPT_Tau1Track", "OS_lscdp":"SR_lowSCDP_160med_highPT_Tau1Track", "SS_lscdp":"SR_lowSCDP_SS160med_highPT_Tau1Track", "OS":"SR_160med_highPT_Tau1Track","ncuts":7}  
addon_regions_160med_highPT_1Track[samples.Wjets]   = {"OS":"SR_160med_highPT_Tau1Track", "SS":"SR_SS160med_highPT_Tau1Track", "ncuts":7}
addon_regions_160med_highPT_1Track[samples.Zlljets] = {"OS":"SR_160med_highPT_Tau1Track", "SS":"SR_SS160med_highPT_Tau1Track", "ncuts":7}
addon_regions_160med_highPT_1Track[samples.top]     = {"OS":"SR_160med_highPT_Tau1Track", "SS":"SR_SS160med_highPT_Tau1Track", "ncuts":7}

addon_regions_L1TAU12IMmed_1Track = {}
addon_regions_L1TAU12IMmed_1Track[data]            = {"OS_lscdp":"SR_lowSCDP_L1TAU12IMmed_Tau1Track", "SS_lscdp":"SR_lowSCDP_SSL1TAU12IMmed_Tau1Track", "OS":"SR_L1TAU12IMmed_Tau1Track", "SS":"SR_SSL1TAU12IMmed_Tau1Track", "ncuts":6}  
addon_regions_L1TAU12IMmed_1Track[samples.Wjets]   = {"OS":"SR_L1TAU12IMmed_Tau1Track", "SS":"SR_SSL1TAU12IMmed_Tau1Track", "ncuts":6}
addon_regions_L1TAU12IMmed_1Track[samples.Zlljets] = {"OS":"SR_L1TAU12IMmed_Tau1Track", "SS":"SR_SSL1TAU12IMmed_Tau1Track", "ncuts":6}
addon_regions_L1TAU12IMmed_1Track[samples.top]     = {"OS":"SR_L1TAU12IMmed_Tau1Track", "SS":"SR_SSL1TAU12IMmed_Tau1Track", "ncuts":6}

addon_regions_L1TAU12IMmed_lowPT_1Track = {}
addon_regions_L1TAU12IMmed_lowPT_1Track[data]            = {"SS":"SR_SSL1TAU12IMmed_lowPT_Tau1Track", "OS_lscdp":"SR_lowSCDP_L1TAU12IMmed_lowPT_Tau1Track", "SS_lscdp":"SR_lowSCDP_SSL1TAU12IMmed_lowPT_Tau1Track", "OS":"SR_L1TAU12IMmed_lowPT_Tau1Track", "ncuts":7}  
addon_regions_L1TAU12IMmed_lowPT_1Track[samples.Wjets]   = {"OS":"SR_L1TAU12IMmed_lowPT_Tau1Track", "SS":"SR_SSL1TAU12IMmed_lowPT_Tau1Track", "ncuts":7}
addon_regions_L1TAU12IMmed_lowPT_1Track[samples.Zlljets] = {"OS":"SR_L1TAU12IMmed_lowPT_Tau1Track", "SS":"SR_SSL1TAU12IMmed_lowPT_Tau1Track", "ncuts":7}
addon_regions_L1TAU12IMmed_lowPT_1Track[samples.top]     = {"OS":"SR_L1TAU12IMmed_lowPT_Tau1Track", "SS":"SR_SSL1TAU12IMmed_lowPT_Tau1Track", "ncuts":7}

addon_regions_L1TAU12IMmed_highPT_1Track = {}
addon_regions_L1TAU12IMmed_highPT_1Track[data]            = {"SS":"SR_SSL1TAU12IMmed_highPT_Tau1Track", "OS_lscdp":"SR_lowSCDP_L1TAU12IMmed_highPT_Tau1Track", "SS_lscdp":"SR_lowSCDP_SSL1TAU12IMmed_highPT_Tau1Track", "OS":"SR_L1TAU12IMmed_highPT_Tau1Track","ncuts":7}  
addon_regions_L1TAU12IMmed_highPT_1Track[samples.Wjets]   = {"OS":"SR_L1TAU12IMmed_highPT_Tau1Track", "SS":"SR_SSL1TAU12IMmed_highPT_Tau1Track", "ncuts":7}
addon_regions_L1TAU12IMmed_highPT_1Track[samples.Zlljets] = {"OS":"SR_L1TAU12IMmed_highPT_Tau1Track", "SS":"SR_SSL1TAU12IMmed_highPT_Tau1Track", "ncuts":7}
addon_regions_L1TAU12IMmed_highPT_1Track[samples.top]     = {"OS":"SR_L1TAU12IMmed_highPT_Tau1Track", "SS":"SR_SSL1TAU12IMmed_highPT_Tau1Track", "ncuts":7}

addon_regions_ptonly_1Track = {}
addon_regions_ptonly_1Track[data]            = {"OS_lscdp":"SR_lowSCDP_ptonly_Tau1Track", "SS_lscdp":"SR_lowSCDP_SSptonly_Tau1Track", "OS":"SR_ptonly_Tau1Track", "SS":"SR_SSptonly_Tau1Track", "ncuts":6}  
addon_regions_ptonly_1Track[samples.Wjets]   = {"OS":"SR_ptonly_Tau1Track", "SS":"SR_SSptonly_Tau1Track", "ncuts":6}
addon_regions_ptonly_1Track[samples.Zlljets] = {"OS":"SR_ptonly_Tau1Track", "SS":"SR_SSptonly_Tau1Track", "ncuts":6}
addon_regions_ptonly_1Track[samples.top]     = {"OS":"SR_ptonly_Tau1Track", "SS":"SR_SSptonly_Tau1Track", "ncuts":6}

addon_regions_ptonly_lowPT_1Track = {}
addon_regions_ptonly_lowPT_1Track[data]            = {"SS":"SR_SSptonly_lowPT_Tau1Track", "OS_lscdp":"SR_lowSCDP_ptonly_lowPT_Tau1Track", "SS_lscdp":"SR_lowSCDP_SSptonly_lowPT_Tau1Track", "OS":"SR_ptonly_lowPT_Tau1Track", "ncuts":7}  
addon_regions_ptonly_lowPT_1Track[samples.Wjets]   = {"OS":"SR_ptonly_lowPT_Tau1Track", "SS":"SR_SSptonly_lowPT_Tau1Track", "ncuts":7}
addon_regions_ptonly_lowPT_1Track[samples.Zlljets] = {"OS":"SR_ptonly_lowPT_Tau1Track", "SS":"SR_SSptonly_lowPT_Tau1Track", "ncuts":7}
addon_regions_ptonly_lowPT_1Track[samples.top]     = {"OS":"SR_ptonly_lowPT_Tau1Track", "SS":"SR_SSptonly_lowPT_Tau1Track", "ncuts":7}

addon_regions_ptonly_highPT_1Track = {}
addon_regions_ptonly_highPT_1Track[data]            = {"SS":"SR_SSptonly_highPT_Tau1Track", "OS_lscdp":"SR_lowSCDP_ptonly_highPT_Tau1Track", "SS_lscdp":"SR_lowSCDP_SSptonly_highPT_Tau1Track", "OS":"SR_ptonly_highPT_Tau1Track","ncuts":7}  
addon_regions_ptonly_highPT_1Track[samples.Wjets]   = {"OS":"SR_ptonly_highPT_Tau1Track", "SS":"SR_SSptonly_highPT_Tau1Track", "ncuts":7}
addon_regions_ptonly_highPT_1Track[samples.Zlljets] = {"OS":"SR_ptonly_highPT_Tau1Track", "SS":"SR_SSptonly_highPT_Tau1Track", "ncuts":7}
addon_regions_ptonly_highPT_1Track[samples.top]     = {"OS":"SR_ptonly_highPT_Tau1Track", "SS":"SR_SSptonly_highPT_Tau1Track", "ncuts":7}

addon_regions_tracktwo_1Track = {}
addon_regions_tracktwo_1Track[data]            = {"OS_lscdp":"SR_lowSCDP_tracktwo_Tau1Track", "SS_lscdp":"SR_lowSCDP_SStracktwo_Tau1Track", "OS":"SR_tracktwo_Tau1Track", "SS":"SR_SStracktwo_Tau1Track", "ncuts":6}  
addon_regions_tracktwo_1Track[samples.Wjets]   = {"OS":"SR_tracktwo_Tau1Track", "SS":"SR_SStracktwo_Tau1Track", "ncuts":6}
addon_regions_tracktwo_1Track[samples.Zlljets] = {"OS":"SR_tracktwo_Tau1Track", "SS":"SR_SStracktwo_Tau1Track", "ncuts":6}
addon_regions_tracktwo_1Track[samples.top]     = {"OS":"SR_tracktwo_Tau1Track", "SS":"SR_SStracktwo_Tau1Track", "ncuts":6}

addon_regions_tracktwo_lowPT_1Track = {}
addon_regions_tracktwo_lowPT_1Track[data]            = {"SS":"SR_SStracktwo_lowPT_Tau1Track", "OS_lscdp":"SR_lowSCDP_tracktwo_lowPT_Tau1Track", "SS_lscdp":"SR_lowSCDP_SStracktwo_lowPT_Tau1Track", "OS":"SR_tracktwo_lowPT_Tau1Track", "ncuts":7}  
addon_regions_tracktwo_lowPT_1Track[samples.Wjets]   = {"OS":"SR_tracktwo_lowPT_Tau1Track", "SS":"SR_SStracktwo_lowPT_Tau1Track", "ncuts":7}
addon_regions_tracktwo_lowPT_1Track[samples.Zlljets] = {"OS":"SR_tracktwo_lowPT_Tau1Track", "SS":"SR_SStracktwo_lowPT_Tau1Track", "ncuts":7}
addon_regions_tracktwo_lowPT_1Track[samples.top]     = {"OS":"SR_tracktwo_lowPT_Tau1Track", "SS":"SR_SStracktwo_lowPT_Tau1Track", "ncuts":7}

addon_regions_tracktwo_highPT_1Track = {}
addon_regions_tracktwo_highPT_1Track[data]            = {"SS":"SR_SStracktwo_highPT_Tau1Track", "OS_lscdp":"SR_lowSCDP_tracktwo_highPT_Tau1Track", "SS_lscdp":"SR_lowSCDP_SStracktwo_highPT_Tau1Track", "OS":"SR_tracktwo_highPT_Tau1Track","ncuts":7}  
addon_regions_tracktwo_highPT_1Track[samples.Wjets]   = {"OS":"SR_tracktwo_highPT_Tau1Track", "SS":"SR_SStracktwo_highPT_Tau1Track", "ncuts":7}
addon_regions_tracktwo_highPT_1Track[samples.Zlljets] = {"OS":"SR_tracktwo_highPT_Tau1Track", "SS":"SR_SStracktwo_highPT_Tau1Track", "ncuts":7}
addon_regions_tracktwo_highPT_1Track[samples.top]     = {"OS":"SR_tracktwo_highPT_Tau1Track", "SS":"SR_SStracktwo_highPT_Tau1Track", "ncuts":7}


#--------------------
# three tracks
#--------------------

addon_regions_3Track = {}
addon_regions_3Track[data]            = {"OS":"SR_Tau3Track", "SS":"SR_SS_Tau3Track", "OS_lscdp":"SR_lowSCDP_Tau3Track", "SS_lscdp":"SR_lowSCDP_SS_Tau3Track", "ncuts":5}#{"SS":"SR_SS_Tau3Track", "ncuts":5}  
addon_regions_3Track[samples.Wjets]   = {"OS":"SR_Tau3Track", "SS":"SR_SS_Tau3Track", "ncuts":5}
addon_regions_3Track[samples.Zlljets] = {"OS":"SR_Tau3Track", "SS":"SR_SS_Tau3Track", "ncuts":5}
addon_regions_3Track[samples.top]     = {"OS":"SR_Tau3Track", "SS":"SR_SS_Tau3Track", "ncuts":5}

addon_regions_highPT_3Track = {}
addon_regions_highPT_3Track[data]            = {"OS":"SR_highPT_Tau3Track", "SS":"SR_SS_highPT_Tau3Track", "OS_lscdp":"SR_lowSCDP_highPT_Tau3Track", "SS_lscdp":"SR_lowSCDP_SS_highPT_Tau3Track", "ncuts":6}  
addon_regions_highPT_3Track[samples.Wjets]   = {"OS":"SR_highPT_Tau3Track", "SS":"SR_SS_highPT_Tau3Track", "ncuts":6}
addon_regions_highPT_3Track[samples.Zlljets] = {"OS":"SR_highPT_Tau3Track", "SS":"SR_SS_highPT_Tau3Track", "ncuts":6}
addon_regions_highPT_3Track[samples.top]     = {"OS":"SR_highPT_Tau3Track", "SS":"SR_SS_highPT_Tau3Track", "ncuts":6}

addon_regions_lowPT_3Track = {}
addon_regions_lowPT_3Track[data]            = {"OS":"SR_lowPT_Tau3Track", "SS":"SR_SS_lowPT_Tau3Track", "OS_lscdp":"SR_lowSCDP_lowPT_Tau3Track", "SS_lscdp":"SR_lowSCDP_SS_lowPT_Tau3Track", "ncuts":6}#{"SS":"SR_SS_lowPT_Tau3Track", "ncuts":6}  
addon_regions_lowPT_3Track[samples.Wjets]   = {"OS":"SR_lowPT_Tau3Track", "SS":"SR_SS_lowPT_Tau3Track", "ncuts":6}
addon_regions_lowPT_3Track[samples.Zlljets] = {"OS":"SR_lowPT_Tau3Track", "SS":"SR_SS_lowPT_Tau3Track", "ncuts":6}
addon_regions_lowPT_3Track[samples.top]     = {"OS":"SR_lowPT_Tau3Track", "SS":"SR_SS_lowPT_Tau3Track", "ncuts":6}

addon_regions_25med_3Track = {}
addon_regions_25med_3Track[data]            = {"OS":"SR_25med_Tau3Track", "SS":"SR_SS25med_Tau3Track", "OS_lscdp":"SR_lowSCDP_25med_Tau3Track", "SS_lscdp":"SR_lowSCDP_SS25med_Tau3Track", "ncuts":6}#'SR_lowSCDP_'+str(triggers[i])+'med_Tau'+str(trax[j])+'Track',{"SS":"SR_SS25med_Tau3Track", "ncuts":6}  
addon_regions_25med_3Track[samples.Wjets]   = {"OS":"SR_25med_Tau3Track", "SS":"SR_SS25med_Tau3Track", "ncuts":6}
addon_regions_25med_3Track[samples.Zlljets] = {"OS":"SR_25med_Tau3Track", "SS":"SR_SS25med_Tau3Track", "ncuts":6}
addon_regions_25med_3Track[samples.top]     = {"OS":"SR_25med_Tau3Track", "SS":"SR_SS25med_Tau3Track", "ncuts":6}

addon_regions_25med_lowPT_3Track = {}
addon_regions_25med_lowPT_3Track[data]            = {"OS":"SR_25med_lowPT_Tau3Track", "SS":"SR_SS25med_lowPT_Tau3Track", "OS_lscdp":"SR_lowSCDP_25med_lowPT_Tau3Track", "SS_lscdp":"SR_lowSCDP_SS25med_lowPT_Tau3Track", "ncuts":7}  
addon_regions_25med_lowPT_3Track[samples.Wjets]   = {"OS":"SR_25med_lowPT_Tau3Track", "SS":"SR_SS25med_lowPT_Tau3Track", "ncuts":7}
addon_regions_25med_lowPT_3Track[samples.Zlljets] = {"OS":"SR_25med_lowPT_Tau3Track", "SS":"SR_SS25med_lowPT_Tau3Track", "ncuts":7}
addon_regions_25med_lowPT_3Track[samples.top]     = {"OS":"SR_25med_lowPT_Tau3Track", "SS":"SR_SS25med_lowPT_Tau3Track", "ncuts":7}

addon_regions_25med_highPT_3Track = {}
addon_regions_25med_highPT_3Track[data]            = {"OS":"SR_25med_highPT_Tau3Track", "SS":"SR_SS25med_highPT_Tau3Track", "OS_lscdp":"SR_lowSCDP_25med_highPT_Tau3Track", "SS_lscdp":"SR_lowSCDP_SS25med_highPT_Tau3Track","ncuts":7}#{"SS":"SR_SS25med_highPT_Tau3Track", "ncuts":7}  
addon_regions_25med_highPT_3Track[samples.Wjets]   = {"OS":"SR_25med_highPT_Tau3Track", "SS":"SR_SS25med_highPT_Tau3Track", "ncuts":7}
addon_regions_25med_highPT_3Track[samples.Zlljets] = {"OS":"SR_25med_highPT_Tau3Track", "SS":"SR_SS25med_highPT_Tau3Track", "ncuts":7}
addon_regions_25med_highPT_3Track[samples.top]     = {"OS":"SR_25med_highPT_Tau3Track", "SS":"SR_SS25med_highPT_Tau3Track", "ncuts":7}

addon_regions_35med_3Track = {}
addon_regions_35med_3Track[data]            = {"OS_lscdp":"SR_lowSCDP_35med_Tau3Track", "SS_lscdp":"SR_lowSCDP_SS35med_Tau3Track", "OS":"SR_35med_Tau3Track", "SS":"SR_SS35med_Tau3Track", "ncuts":6}  
addon_regions_35med_3Track[samples.Wjets]   = {"OS":"SR_35med_Tau3Track", "SS":"SR_SS35med_Tau3Track", "ncuts":6}
addon_regions_35med_3Track[samples.Zlljets] = {"OS":"SR_35med_Tau3Track", "SS":"SR_SS35med_Tau3Track", "ncuts":6}
addon_regions_35med_3Track[samples.top]     = {"OS":"SR_35med_Tau3Track", "SS":"SR_SS35med_Tau3Track", "ncuts":6}

addon_regions_35med_lowPT_3Track = {}
addon_regions_35med_lowPT_3Track[data]            = {"SS":"SR_SS35med_lowPT_Tau3Track", "OS_lscdp":"SR_lowSCDP_35med_lowPT_Tau3Track", "SS_lscdp":"SR_lowSCDP_SS35med_lowPT_Tau3Track", "OS":"SR_35med_lowPT_Tau3Track", "ncuts":7}  
addon_regions_35med_lowPT_3Track[samples.Wjets]   = {"OS":"SR_35med_lowPT_Tau3Track", "SS":"SR_SS35med_lowPT_Tau3Track", "ncuts":7}
addon_regions_35med_lowPT_3Track[samples.Zlljets] = {"OS":"SR_35med_lowPT_Tau3Track", "SS":"SR_SS35med_lowPT_Tau3Track", "ncuts":7}
addon_regions_35med_lowPT_3Track[samples.top]     = {"OS":"SR_35med_lowPT_Tau3Track", "SS":"SR_SS35med_lowPT_Tau3Track", "ncuts":7}

addon_regions_35med_highPT_3Track = {}
addon_regions_35med_highPT_3Track[data]            = {"SS":"SR_SS35med_highPT_Tau3Track", "OS_lscdp":"SR_lowSCDP_35med_highPT_Tau3Track", "SS_lscdp":"SR_lowSCDP_SS35med_highPT_Tau3Track", "OS":"SR_35med_highPT_Tau3Track","ncuts":7}  
addon_regions_35med_highPT_3Track[samples.Wjets]   = {"OS":"SR_35med_highPT_Tau3Track", "SS":"SR_SS35med_highPT_Tau3Track", "ncuts":7}
addon_regions_35med_highPT_3Track[samples.Zlljets] = {"OS":"SR_35med_highPT_Tau3Track", "SS":"SR_SS35med_highPT_Tau3Track", "ncuts":7}
addon_regions_35med_highPT_3Track[samples.top]     = {"OS":"SR_35med_highPT_Tau3Track", "SS":"SR_SS35med_highPT_Tau3Track", "ncuts":7}

addon_regions_50L1TAU12med_3Track = {}
addon_regions_50L1TAU12med_3Track[data]            = {"OS_lscdp":"SR_lowSCDP_50L1TAU12med_Tau3Track", "SS_lscdp":"SR_lowSCDP_SS50L1TAU12med_Tau3Track","OS":"SR_50L1TAU12med_Tau3Track", "SS":"SR_SS50L1TAU12med_Tau3Track", "ncuts":6}  
addon_regions_50L1TAU12med_3Track[samples.Wjets]   = {"OS":"SR_50L1TAU12med_Tau3Track", "SS":"SR_SS50L1TAU12med_Tau3Track", "ncuts":6}
addon_regions_50L1TAU12med_3Track[samples.Zlljets] = {"OS":"SR_50L1TAU12med_Tau3Track", "SS":"SR_SS50L1TAU12med_Tau3Track", "ncuts":6}
addon_regions_50L1TAU12med_3Track[samples.top]     = {"OS":"SR_50L1TAU12med_Tau3Track", "SS":"SR_SS50L1TAU12med_Tau3Track", "ncuts":6}

addon_regions_50L1TAU12med_lowPT_3Track = {}
addon_regions_50L1TAU12med_lowPT_3Track[data]            = {"SS":"SR_SS50L1TAU12med_lowPT_Tau3Track", "OS_lscdp":"SR_lowSCDP_50L1TAU12med_lowPT_Tau3Track", "SS_lscdp":"SR_lowSCDP_SS50L1TAU12med_lowPT_Tau3Track", "OS":"SR_50L1TAU12med_lowPT_Tau3Track", "ncuts":7}  
addon_regions_50L1TAU12med_lowPT_3Track[samples.Wjets]   = {"OS":"SR_50L1TAU12med_lowPT_Tau3Track", "SS":"SR_SS50L1TAU12med_lowPT_Tau3Track", "ncuts":7}
addon_regions_50L1TAU12med_lowPT_3Track[samples.Zlljets] = {"OS":"SR_50L1TAU12med_lowPT_Tau3Track", "SS":"SR_SS50L1TAU12med_lowPT_Tau3Track", "ncuts":7}
addon_regions_50L1TAU12med_lowPT_3Track[samples.top]     = {"OS":"SR_50L1TAU12med_lowPT_Tau3Track", "SS":"SR_SS50L1TAU12med_lowPT_Tau3Track", "ncuts":7}

addon_regions_50L1TAU12med_highPT_3Track = {}
addon_regions_50L1TAU12med_highPT_3Track[data]            = {"SS":"SR_SS50L1TAU12med_highPT_Tau3Track", "OS_lscdp":"SR_lowSCDP_50L1TAU12med_highPT_Tau3Track", "SS_lscdp":"SR_lowSCDP_SS50L1TAU12med_highPT_Tau3Track",  "OS":"SR_50L1TAU12med_highPT_Tau3Track","ncuts":7}  
addon_regions_50L1TAU12med_highPT_3Track[samples.Wjets]   = {"OS":"SR_50L1TAU12med_highPT_Tau3Track", "SS":"SR_SS50L1TAU12med_highPT_Tau3Track", "ncuts":7}
addon_regions_50L1TAU12med_highPT_3Track[samples.Zlljets] = {"OS":"SR_50L1TAU12med_highPT_Tau3Track", "SS":"SR_SS50L1TAU12med_highPT_Tau3Track", "ncuts":7}
addon_regions_50L1TAU12med_highPT_3Track[samples.top]     = {"OS":"SR_50L1TAU12med_highPT_Tau3Track", "SS":"SR_SS50L1TAU12med_highPT_Tau3Track", "ncuts":7}

addon_regions_80med_3Track = {}
addon_regions_80med_3Track[data]            = {"OS_lscdp":"SR_lowSCDP_80med_Tau3Track", "SS_lscdp":"SR_lowSCDP_SS80med_Tau3Track","OS":"SR_80med_Tau3Track", "SS":"SR_SS80med_Tau3Track", "ncuts":6}  
addon_regions_80med_3Track[samples.Wjets]   = {"OS":"SR_80med_Tau3Track", "SS":"SR_SS80med_Tau3Track", "ncuts":6}
addon_regions_80med_3Track[samples.Zlljets] = {"OS":"SR_80med_Tau3Track", "SS":"SR_SS80med_Tau3Track", "ncuts":6}
addon_regions_80med_3Track[samples.top]     = {"OS":"SR_80med_Tau3Track", "SS":"SR_SS80med_Tau3Track", "ncuts":6}

addon_regions_80med_lowPT_3Track = {}
addon_regions_80med_lowPT_3Track[data]            = {"SS":"SR_SS80med_lowPT_Tau3Track", "OS_lscdp":"SR_lowSCDP_80med_lowPT_Tau3Track", "SS_lscdp":"SR_lowSCDP_SS80med_lowPT_Tau3Track", "OS":"SR_80med_lowPT_Tau3Track", "ncuts":7}  
addon_regions_80med_lowPT_3Track[samples.Wjets]   = {"OS":"SR_80med_lowPT_Tau3Track", "SS":"SR_SS80med_lowPT_Tau3Track", "ncuts":7}
addon_regions_80med_lowPT_3Track[samples.Zlljets] = {"OS":"SR_80med_lowPT_Tau3Track", "SS":"SR_SS80med_lowPT_Tau3Track", "ncuts":7}
addon_regions_80med_lowPT_3Track[samples.top]     = {"OS":"SR_80med_lowPT_Tau3Track", "SS":"SR_SS80med_lowPT_Tau3Track", "ncuts":7}

addon_regions_80med_highPT_3Track = {}
addon_regions_80med_highPT_3Track[data]            = {"SS":"SR_SS80med_highPT_Tau3Track", "OS_lscdp":"SR_lowSCDP_80med_highPT_Tau3Track", "SS_lscdp":"SR_lowSCDP_SS80med_highPT_Tau3Track", "OS":"SR_80med_highPT_Tau3Track","ncuts":7}  
addon_regions_80med_highPT_3Track[samples.Wjets]   = {"OS":"SR_80med_highPT_Tau3Track", "SS":"SR_SS80med_highPT_Tau3Track", "ncuts":7}
addon_regions_80med_highPT_3Track[samples.Zlljets] = {"OS":"SR_80med_highPT_Tau3Track", "SS":"SR_SS80med_highPT_Tau3Track", "ncuts":7}
addon_regions_80med_highPT_3Track[samples.top]     = {"OS":"SR_80med_highPT_Tau3Track", "SS":"SR_SS80med_highPT_Tau3Track", "ncuts":7}

addon_regions_80L1TAU60med_3Track = {}
addon_regions_80L1TAU60med_3Track[data]            = {"OS_lscdp":"SR_lowSCDP_80L1TAU60med_Tau3Track", "SS_lscdp":"SR_lowSCDP_SS80L1TAU60med_Tau3Track", "OS":"SR_80L1TAU60med_Tau3Track", "SS":"SR_SS80L1TAU60med_Tau3Track", "ncuts":6}  
addon_regions_80L1TAU60med_3Track[samples.Wjets]   = {"OS":"SR_80L1TAU60med_Tau3Track", "SS":"SR_SS80L1TAU60med_Tau3Track", "ncuts":6}
addon_regions_80L1TAU60med_3Track[samples.Zlljets] = {"OS":"SR_80L1TAU60med_Tau3Track", "SS":"SR_SS80L1TAU60med_Tau3Track", "ncuts":6}
addon_regions_80L1TAU60med_3Track[samples.top]     = {"OS":"SR_80L1TAU60med_Tau3Track", "SS":"SR_SS80L1TAU60med_Tau3Track", "ncuts":6}

addon_regions_80L1TAU60med_lowPT_3Track = {}
addon_regions_80L1TAU60med_lowPT_3Track[data]            = {"SS":"SR_SS80L1TAU60med_lowPT_Tau3Track", "OS_lscdp":"SR_lowSCDP_80L1TAU60med_lowPT_Tau3Track", "SS_lscdp":"SR_lowSCDP_SS80L1TAU60med_lowPT_Tau3Track", "OS":"SR_80L1TAU60med_lowPT_Tau3Track", "ncuts":7}  
addon_regions_80L1TAU60med_lowPT_3Track[samples.Wjets]   = {"OS":"SR_80L1TAU60med_lowPT_Tau3Track", "SS":"SR_SS80L1TAU60med_lowPT_Tau3Track", "ncuts":7}
addon_regions_80L1TAU60med_lowPT_3Track[samples.Zlljets] = {"OS":"SR_80L1TAU60med_lowPT_Tau3Track", "SS":"SR_SS80L1TAU60med_lowPT_Tau3Track", "ncuts":7}
addon_regions_80L1TAU60med_lowPT_3Track[samples.top]     = {"OS":"SR_80L1TAU60med_lowPT_Tau3Track", "SS":"SR_SS80L1TAU60med_lowPT_Tau3Track", "ncuts":7}

addon_regions_80L1TAU60med_highPT_3Track = {}
addon_regions_80L1TAU60med_highPT_3Track[data]            = {"SS":"SR_SS80L1TAU60med_highPT_Tau3Track", "OS_lscdp":"SR_lowSCDP_80L1TAU60med_highPT_Tau3Track", "SS_lscdp":"SR_lowSCDP_SS80L1TAU60med_highPT_Tau3Track", "OS":"SR_80L1TAU60med_highPT_Tau3Track","ncuts":7}  
addon_regions_80L1TAU60med_highPT_3Track[samples.Wjets]   = {"OS":"SR_80L1TAU60med_highPT_Tau3Track", "SS":"SR_SS80L1TAU60med_highPT_Tau3Track", "ncuts":7}
addon_regions_80L1TAU60med_highPT_3Track[samples.Zlljets] = {"OS":"SR_80L1TAU60med_highPT_Tau3Track", "SS":"SR_SS80L1TAU60med_highPT_Tau3Track", "ncuts":7}
addon_regions_80L1TAU60med_highPT_3Track[samples.top]     = {"OS":"SR_80L1TAU60med_highPT_Tau3Track", "SS":"SR_SS80L1TAU60med_highPT_Tau3Track", "ncuts":7}

addon_regions_125med_3Track = {}
addon_regions_125med_3Track[data]            = {"OS_lscdp":"SR_lowSCDP_125med_Tau3Track", "SS_lscdp":"SR_lowSCDP_SS125med_Tau3Track", "OS":"SR_125med_Tau3Track", "SS":"SR_SS125med_Tau3Track", "ncuts":6}  
addon_regions_125med_3Track[samples.Wjets]   = {"OS":"SR_125med_Tau3Track", "SS":"SR_SS125med_Tau3Track", "ncuts":6}
addon_regions_125med_3Track[samples.Zlljets] = {"OS":"SR_125med_Tau3Track", "SS":"SR_SS125med_Tau3Track", "ncuts":6}
addon_regions_125med_3Track[samples.top]     = {"OS":"SR_125med_Tau3Track", "SS":"SR_SS125med_Tau3Track", "ncuts":6}

addon_regions_125med_lowPT_3Track = {}
addon_regions_125med_lowPT_3Track[data]            = {"SS":"SR_SS125med_lowPT_Tau3Track", "OS_lscdp":"SR_lowSCDP_125med_lowPT_Tau3Track", "SS_lscdp":"SR_lowSCDP_SS125med_lowPT_Tau3Track", "OS":"SR_125med_lowPT_Tau3Track", "ncuts":7}  
addon_regions_125med_lowPT_3Track[samples.Wjets]   = {"OS":"SR_125med_lowPT_Tau3Track", "SS":"SR_SS125med_lowPT_Tau3Track", "ncuts":7}
addon_regions_125med_lowPT_3Track[samples.Zlljets] = {"OS":"SR_125med_lowPT_Tau3Track", "SS":"SR_SS125med_lowPT_Tau3Track", "ncuts":7}
addon_regions_125med_lowPT_3Track[samples.top]     = {"OS":"SR_125med_lowPT_Tau3Track", "SS":"SR_SS125med_lowPT_Tau3Track", "ncuts":7}

addon_regions_125med_highPT_3Track = {}
addon_regions_125med_highPT_3Track[data]            = {"SS":"SR_SS125med_highPT_Tau3Track", "OS_lscdp":"SR_lowSCDP_125med_highPT_Tau3Track", "SS_lscdp":"SR_lowSCDP_SS125med_highPT_Tau3Track", "OS":"SR_125med_highPT_Tau3Track","ncuts":7}  
addon_regions_125med_highPT_3Track[samples.Wjets]   = {"OS":"SR_125med_highPT_Tau3Track", "SS":"SR_SS125med_highPT_Tau3Track", "ncuts":7}
addon_regions_125med_highPT_3Track[samples.Zlljets] = {"OS":"SR_125med_highPT_Tau3Track", "SS":"SR_SS125med_highPT_Tau3Track", "ncuts":7}
addon_regions_125med_highPT_3Track[samples.top]     = {"OS":"SR_125med_highPT_Tau3Track", "SS":"SR_SS125med_highPT_Tau3Track", "ncuts":7}

addon_regions_160med_3Track = {}
addon_regions_160med_3Track[data]            = {"OS_lscdp":"SR_lowSCDP_160med_Tau3Track", "SS_lscdp":"SR_lowSCDP_SS160med_Tau3Track","OS":"SR_160med_Tau3Track", "SS":"SR_SS160med_Tau3Track", "ncuts":6}  
addon_regions_160med_3Track[samples.Wjets]   = {"OS":"SR_160med_Tau3Track", "SS":"SR_SS160med_Tau3Track", "ncuts":6}
addon_regions_160med_3Track[samples.Zlljets] = {"OS":"SR_160med_Tau3Track", "SS":"SR_SS160med_Tau3Track", "ncuts":6}
addon_regions_160med_3Track[samples.top]     = {"OS":"SR_160med_Tau3Track", "SS":"SR_SS160med_Tau3Track", "ncuts":6}

addon_regions_160med_lowPT_3Track = {}
addon_regions_160med_lowPT_3Track[data]            = {"SS":"SR_SS160med_lowPT_Tau3Track", "OS_lscdp":"SR_lowSCDP_160med_lowPT_Tau3Track", "SS_lscdp":"SR_lowSCDP_SS160med_lowPT_Tau3Track", "OS":"SR_160med_lowPT_Tau3Track", "ncuts":7}  
addon_regions_160med_lowPT_3Track[samples.Wjets]   = {"OS":"SR_160med_lowPT_Tau3Track", "SS":"SR_SS160med_lowPT_Tau3Track", "ncuts":7}
addon_regions_160med_lowPT_3Track[samples.Zlljets] = {"OS":"SR_160med_lowPT_Tau3Track", "SS":"SR_SS160med_lowPT_Tau3Track", "ncuts":7}
addon_regions_160med_lowPT_3Track[samples.top]     = {"OS":"SR_160med_lowPT_Tau3Track", "SS":"SR_SS160med_lowPT_Tau3Track", "ncuts":7}

addon_regions_160med_highPT_3Track = {}
addon_regions_160med_highPT_3Track[data]            = {"SS":"SR_SS160med_highPT_Tau3Track", "OS_lscdp":"SR_lowSCDP_160med_highPT_Tau3Track", "SS_lscdp":"SR_lowSCDP_SS160med_highPT_Tau3Track", "OS":"SR_160med_highPT_Tau3Track","ncuts":7}  
addon_regions_160med_highPT_3Track[samples.Wjets]   = {"OS":"SR_160med_highPT_Tau3Track", "SS":"SR_SS160med_highPT_Tau3Track", "ncuts":7}
addon_regions_160med_highPT_3Track[samples.Zlljets] = {"OS":"SR_160med_highPT_Tau3Track", "SS":"SR_SS160med_highPT_Tau3Track", "ncuts":7}
addon_regions_160med_highPT_3Track[samples.top]     = {"OS":"SR_160med_highPT_Tau3Track", "SS":"SR_SS160med_highPT_Tau3Track", "ncuts":7}

addon_regions_L1TAU12IMmed_3Track = {}
addon_regions_L1TAU12IMmed_3Track[data]            = {"OS_lscdp":"SR_lowSCDP_L1TAU12IMmed_Tau3Track", "SS_lscdp":"SR_lowSCDP_SSL1TAU12IMmed_Tau3Track","OS":"SR_L1TAU12IMmed_Tau3Track", "SS":"SR_SSL1TAU12IMmed_Tau3Track", "ncuts":6}  
addon_regions_L1TAU12IMmed_3Track[samples.Wjets]   = {"OS":"SR_L1TAU12IMmed_Tau3Track", "SS":"SR_SSL1TAU12IMmed_Tau3Track", "ncuts":6}
addon_regions_L1TAU12IMmed_3Track[samples.Zlljets] = {"OS":"SR_L1TAU12IMmed_Tau3Track", "SS":"SR_SSL1TAU12IMmed_Tau3Track", "ncuts":6}
addon_regions_L1TAU12IMmed_3Track[samples.top]     = {"OS":"SR_L1TAU12IMmed_Tau3Track", "SS":"SR_SSL1TAU12IMmed_Tau3Track", "ncuts":6}

addon_regions_L1TAU12IMmed_lowPT_3Track = {}
addon_regions_L1TAU12IMmed_lowPT_3Track[data]            = {"SS":"SR_SSL1TAU12IMmed_lowPT_Tau3Track", "OS_lscdp":"SR_lowSCDP_L1TAU12IMmed_lowPT_Tau3Track", "SS_lscdp":"SR_lowSCDP_SSL1TAU12IMmed_lowPT_Tau3Track", "OS":"SR_L1TAU12IMmed_lowPT_Tau3Track", "ncuts":7}  
addon_regions_L1TAU12IMmed_lowPT_3Track[samples.Wjets]   = {"OS":"SR_L1TAU12IMmed_lowPT_Tau3Track", "SS":"SR_SSL1TAU12IMmed_lowPT_Tau3Track", "ncuts":7}
addon_regions_L1TAU12IMmed_lowPT_3Track[samples.Zlljets] = {"OS":"SR_L1TAU12IMmed_lowPT_Tau3Track", "SS":"SR_SSL1TAU12IMmed_lowPT_Tau3Track", "ncuts":7}
addon_regions_L1TAU12IMmed_lowPT_3Track[samples.top]     = {"OS":"SR_L1TAU12IMmed_lowPT_Tau3Track", "SS":"SR_SSL1TAU12IMmed_lowPT_Tau3Track", "ncuts":7}

addon_regions_L1TAU12IMmed_highPT_3Track = {}
addon_regions_L1TAU12IMmed_highPT_3Track[data]            = {"SS":"SR_SSL1TAU12IMmed_highPT_Tau3Track", "OS_lscdp":"SR_lowSCDP_L1TAU12IMmed_highPT_Tau3Track", "SS_lscdp":"SR_lowSCDP_SSL1TAU12IMmed_highPT_Tau3Track", "OS":"SR_L1TAU12IMmed_highPT_Tau3Track","ncuts":7}  
addon_regions_L1TAU12IMmed_highPT_3Track[samples.Wjets]   = {"OS":"SR_L1TAU12IMmed_highPT_Tau3Track", "SS":"SR_SSL1TAU12IMmed_highPT_Tau3Track", "ncuts":7}
addon_regions_L1TAU12IMmed_highPT_3Track[samples.Zlljets] = {"OS":"SR_L1TAU12IMmed_highPT_Tau3Track", "SS":"SR_SSL1TAU12IMmed_highPT_Tau3Track", "ncuts":7}
addon_regions_L1TAU12IMmed_highPT_3Track[samples.top]     = {"OS":"SR_L1TAU12IMmed_highPT_Tau3Track", "SS":"SR_SSL1TAU12IMmed_highPT_Tau3Track", "ncuts":7}

addon_regions_ptonly_3Track = {}
addon_regions_ptonly_3Track[data]            = {"OS_lscdp":"SR_lowSCDP_ptonly_Tau3Track", "SS_lscdp":"SR_lowSCDP_SSptonly_Tau3Track", "OS":"SR_ptonly_Tau3Track", "SS":"SR_SSptonly_Tau3Track", "ncuts":6}  
addon_regions_ptonly_3Track[samples.Wjets]   = {"OS":"SR_ptonly_Tau3Track", "SS":"SR_SSptonly_Tau3Track", "ncuts":6}
addon_regions_ptonly_3Track[samples.Zlljets] = {"OS":"SR_ptonly_Tau3Track", "SS":"SR_SSptonly_Tau3Track", "ncuts":6}
addon_regions_ptonly_3Track[samples.top]     = {"OS":"SR_ptonly_Tau3Track", "SS":"SR_SSptonly_Tau3Track", "ncuts":6}

addon_regions_ptonly_lowPT_3Track = {}
addon_regions_ptonly_lowPT_3Track[data]            = {"SS":"SR_SSptonly_lowPT_Tau3Track", "OS_lscdp":"SR_lowSCDP_ptonly_lowPT_Tau3Track", "SS_lscdp":"SR_lowSCDP_SSptonly_lowPT_Tau3Track", "OS":"SR_ptonly_lowPT_Tau3Track", "ncuts":7}  
addon_regions_ptonly_lowPT_3Track[samples.Wjets]   = {"OS":"SR_ptonly_lowPT_Tau3Track", "SS":"SR_SSptonly_lowPT_Tau3Track", "ncuts":7}
addon_regions_ptonly_lowPT_3Track[samples.Zlljets] = {"OS":"SR_ptonly_lowPT_Tau3Track", "SS":"SR_SSptonly_lowPT_Tau3Track", "ncuts":7}
addon_regions_ptonly_lowPT_3Track[samples.top]     = {"OS":"SR_ptonly_lowPT_Tau3Track", "SS":"SR_SSptonly_lowPT_Tau3Track", "ncuts":7}

addon_regions_ptonly_highPT_3Track = {}
addon_regions_ptonly_highPT_3Track[data]            = {"SS":"SR_SSptonly_highPT_Tau3Track", "OS_lscdp":"SR_lowSCDP_ptonly_highPT_Tau3Track", "SS_lscdp":"SR_lowSCDP_SSptonly_highPT_Tau3Track", "OS":"SR_ptonly_highPT_Tau3Track","ncuts":7}  
addon_regions_ptonly_highPT_3Track[samples.Wjets]   = {"OS":"SR_ptonly_highPT_Tau3Track", "SS":"SR_SSptonly_highPT_Tau3Track", "ncuts":7}
addon_regions_ptonly_highPT_3Track[samples.Zlljets] = {"OS":"SR_ptonly_highPT_Tau3Track", "SS":"SR_SSptonly_highPT_Tau3Track", "ncuts":7}
addon_regions_ptonly_highPT_3Track[samples.top]     = {"OS":"SR_ptonly_highPT_Tau3Track", "SS":"SR_SSptonly_highPT_Tau3Track", "ncuts":7}

addon_regions_tracktwo_3Track = {}
addon_regions_tracktwo_3Track[data]            = {"OS_lscdp":"SR_lowSCDP_tracktwo_Tau3Track", "SS_lscdp":"SR_lowSCDP_SStracktwo_Tau3Track", "OS":"SR_tracktwo_Tau3Track", "SS":"SR_SStracktwo_Tau3Track", "ncuts":6}  
addon_regions_tracktwo_3Track[samples.Wjets]   = {"OS":"SR_tracktwo_Tau3Track", "SS":"SR_SStracktwo_Tau3Track", "ncuts":6}
addon_regions_tracktwo_3Track[samples.Zlljets] = {"OS":"SR_tracktwo_Tau3Track", "SS":"SR_SStracktwo_Tau3Track", "ncuts":6}
addon_regions_tracktwo_3Track[samples.top]     = {"OS":"SR_tracktwo_Tau3Track", "SS":"SR_SStracktwo_Tau3Track", "ncuts":6}

addon_regions_tracktwo_lowPT_3Track = {}
addon_regions_tracktwo_lowPT_3Track[data]            = {"SS":"SR_SStracktwo_lowPT_Tau3Track", "OS_lscdp":"SR_lowSCDP_tracktwo_lowPT_Tau3Track", "SS_lscdp":"SR_lowSCDP_SStracktwo_lowPT_Tau3Track", "OS":"SR_tracktwo_lowPT_Tau3Track", "ncuts":7}  
addon_regions_tracktwo_lowPT_3Track[samples.Wjets]   = {"OS":"SR_tracktwo_lowPT_Tau3Track", "SS":"SR_SStracktwo_lowPT_Tau3Track", "ncuts":7}
addon_regions_tracktwo_lowPT_3Track[samples.Zlljets] = {"OS":"SR_tracktwo_lowPT_Tau3Track", "SS":"SR_SStracktwo_lowPT_Tau3Track", "ncuts":7}
addon_regions_tracktwo_lowPT_3Track[samples.top]     = {"OS":"SR_tracktwo_lowPT_Tau3Track", "SS":"SR_SStracktwo_lowPT_Tau3Track", "ncuts":7}

addon_regions_tracktwo_highPT_3Track = {}
addon_regions_tracktwo_highPT_3Track[data]            = {"SS":"SR_SStracktwo_highPT_Tau3Track", "OS_lscdp":"SR_lowSCDP_tracktwo_highPT_Tau3Track", "SS_lscdp":"SR_lowSCDP_SStracktwo_highPT_Tau3Track", "OS":"SR_tracktwo_highPT_Tau3Track","ncuts":7}  
addon_regions_tracktwo_highPT_3Track[samples.Wjets]   = {"OS":"SR_tracktwo_highPT_Tau3Track", "SS":"SR_SStracktwo_highPT_Tau3Track", "ncuts":7}
addon_regions_tracktwo_highPT_3Track[samples.Zlljets] = {"OS":"SR_tracktwo_highPT_Tau3Track", "SS":"SR_SStracktwo_highPT_Tau3Track", "ncuts":7}
addon_regions_tracktwo_highPT_3Track[samples.top]     = {"OS":"SR_tracktwo_highPT_Tau3Track", "SS":"SR_SStracktwo_highPT_Tau3Track", "ncuts":7}


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

if ptbinning_y_or_n == "y":

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


	for b in addon_backgrounds_50L1TAU12med_lowPT:
	 b.estimator = histmgr.AddOnEstimator(
	       hm            = hm,
	       sample        = b,
	       data_sample   = data,
	       mc_samples    = mc_backgrounds + mc_signals,
	       rqcd_regions  = rqcd_regions_50L1TAU12med_lowPT,
	       kf_regions    = kf_regions_50L1TAU12med_lowPT,
	       addon_regions = addon_regions_50L1TAU12med_lowPT,
	       print_info    = True,
	       )

	for b in addon_backgrounds_50L1TAU12med_highPT:
	 b.estimator = histmgr.AddOnEstimator(
	       hm            = hm,
	       sample        = b,
	       data_sample   = data,
	       mc_samples    = mc_backgrounds + mc_signals,
	       rqcd_regions  = rqcd_regions_50L1TAU12med_highPT,
	       kf_regions    = kf_regions_50L1TAU12med_highPT,
	       addon_regions = addon_regions_50L1TAU12med_highPT,
	       print_info    = True,
	       )


	for b in addon_backgrounds_80med_lowPT:
	 b.estimator = histmgr.AddOnEstimator(
	       hm            = hm,
	       sample        = b,
	       data_sample   = data,
	       mc_samples    = mc_backgrounds + mc_signals,
	       rqcd_regions  = rqcd_regions_80med_lowPT,
	       kf_regions    = kf_regions_80med_lowPT,
	       addon_regions = addon_regions_80med_lowPT,
	       print_info    = True,
	       )

	for b in addon_backgrounds_80med_highPT:
	 b.estimator = histmgr.AddOnEstimator(
	       hm            = hm,
	       sample        = b,
	       data_sample   = data,
	       mc_samples    = mc_backgrounds + mc_signals,
	       rqcd_regions  = rqcd_regions_80med_highPT,
	       kf_regions    = kf_regions_80med_highPT,
	       addon_regions = addon_regions_80med_highPT,
	       print_info    = True,
	       )


	for b in addon_backgrounds_80L1TAU60med_lowPT:
	 b.estimator = histmgr.AddOnEstimator(
	       hm            = hm,
	       sample        = b,
	       data_sample   = data,
	       mc_samples    = mc_backgrounds + mc_signals,
	       rqcd_regions  = rqcd_regions_80L1TAU60med_lowPT,
	       kf_regions    = kf_regions_80L1TAU60med_lowPT,
	       addon_regions = addon_regions_80L1TAU60med_lowPT,
	       print_info    = True,
	       )

	for b in addon_backgrounds_80L1TAU60med_highPT:
	 b.estimator = histmgr.AddOnEstimator(
	       hm            = hm,
	       sample        = b,
	       data_sample   = data,
	       mc_samples    = mc_backgrounds + mc_signals,
	       rqcd_regions  = rqcd_regions_80L1TAU60med_highPT,
	       kf_regions    = kf_regions_80L1TAU60med_highPT,
	       addon_regions = addon_regions_80L1TAU60med_highPT,
	       print_info    = True,
	       )


	for b in addon_backgrounds_125med_lowPT:
	 b.estimator = histmgr.AddOnEstimator(
	       hm            = hm,
	       sample        = b,
	       data_sample   = data,
	       mc_samples    = mc_backgrounds + mc_signals,
	       rqcd_regions  = rqcd_regions_125med_lowPT,
	       kf_regions    = kf_regions_125med_lowPT,
	       addon_regions = addon_regions_125med_lowPT,
	       print_info    = True,
	       )

	for b in addon_backgrounds_125med_highPT:
	 b.estimator = histmgr.AddOnEstimator(
	       hm            = hm,
	       sample        = b,
	       data_sample   = data,
	       mc_samples    = mc_backgrounds + mc_signals,
	       rqcd_regions  = rqcd_regions_125med_highPT,
	       kf_regions    = kf_regions_125med_highPT,
	       addon_regions = addon_regions_125med_highPT,
	       print_info    = True,
	       )


	for b in addon_backgrounds_160med_lowPT:
	 b.estimator = histmgr.AddOnEstimator(
	       hm            = hm,
	       sample        = b,
	       data_sample   = data,
	       mc_samples    = mc_backgrounds + mc_signals,
	       rqcd_regions  = rqcd_regions_160med_lowPT,
	       kf_regions    = kf_regions_160med_lowPT,
	       addon_regions = addon_regions_160med_lowPT,
	       print_info    = True,
	       )

	for b in addon_backgrounds_160med_highPT:
	 b.estimator = histmgr.AddOnEstimator(
	       hm            = hm,
	       sample        = b,
	       data_sample   = data,
	       mc_samples    = mc_backgrounds + mc_signals,
	       rqcd_regions  = rqcd_regions_160med_highPT,
	       kf_regions    = kf_regions_160med_highPT,
	       addon_regions = addon_regions_160med_highPT,
	       print_info    = True,
	       )
       
	for b in addon_backgrounds_L1TAU12IMmed_lowPT:
	 b.estimator = histmgr.AddOnEstimator(
	       hm            = hm,
	       sample        = b,
	       data_sample   = data,
	       mc_samples    = mc_backgrounds + mc_signals,
	       rqcd_regions  = rqcd_regions_L1TAU12IMmed_lowPT,
	       kf_regions    = kf_regions_L1TAU12IMmed_lowPT,
	       addon_regions = addon_regions_L1TAU12IMmed_lowPT,
	       print_info    = True,
	       )

	for b in addon_backgrounds_L1TAU12IMmed_highPT:
	 b.estimator = histmgr.AddOnEstimator(
	       hm            = hm,
	       sample        = b,
	       data_sample   = data,
	       mc_samples    = mc_backgrounds + mc_signals,
	       rqcd_regions  = rqcd_regions_L1TAU12IMmed_highPT,
	       kf_regions    = kf_regions_L1TAU12IMmed_highPT,
	       addon_regions = addon_regions_L1TAU12IMmed_highPT,
	       print_info    = True,
	       )
        
	for b in addon_backgrounds_ptonly_lowPT:
	 b.estimator = histmgr.AddOnEstimator(
	       hm            = hm,
	       sample        = b,
	       data_sample   = data,
	       mc_samples    = mc_backgrounds + mc_signals,
	       rqcd_regions  = rqcd_regions_ptonly_lowPT,
	       kf_regions    = kf_regions_ptonly_lowPT,
	       addon_regions = addon_regions_ptonly_lowPT,
	       print_info    = True,
	       )

	for b in addon_backgrounds_ptonly_highPT:
	 b.estimator = histmgr.AddOnEstimator(
	       hm            = hm,
	       sample        = b,
	       data_sample   = data,
	       mc_samples    = mc_backgrounds + mc_signals,
	       rqcd_regions  = rqcd_regions_ptonly_highPT,
	       kf_regions    = kf_regions_ptonly_highPT,
	       addon_regions = addon_regions_ptonly_highPT,
	       print_info    = True,
	       )
        
	for b in addon_backgrounds_tracktwo_lowPT:
	 b.estimator = histmgr.AddOnEstimator(
	       hm            = hm,
	       sample        = b,
	       data_sample   = data,
	       mc_samples    = mc_backgrounds + mc_signals,
	       rqcd_regions  = rqcd_regions_tracktwo_lowPT,
	       kf_regions    = kf_regions_tracktwo_lowPT,
	       addon_regions = addon_regions_tracktwo_lowPT,
	       print_info    = True,
	       )

	for b in addon_backgrounds_tracktwo_highPT:
	 b.estimator = histmgr.AddOnEstimator(
	       hm            = hm,
	       sample        = b,
	       data_sample   = data,
	       mc_samples    = mc_backgrounds + mc_signals,
	       rqcd_regions  = rqcd_regions_tracktwo_highPT,
	       kf_regions    = kf_regions_tracktwo_highPT,
	       addon_regions = addon_regions_tracktwo_highPT,
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


	for b in addon_backgrounds_50L1TAU12med_lowPT_1Track:
	 b.estimator = histmgr.AddOnEstimator(
	       hm            = hm,
	       sample        = b,
	       data_sample   = data,
	       mc_samples    = mc_backgrounds + mc_signals,
	       rqcd_regions  = rqcd_regions_50L1TAU12med_lowPT_1Track,
	       kf_regions    = kf_regions_50L1TAU12med_lowPT_1Track,
	       addon_regions = addon_regions_50L1TAU12med_lowPT_1Track,
	       print_info    = True,
	       )

	for b in addon_backgrounds_50L1TAU12med_highPT_1Track:
	 b.estimator = histmgr.AddOnEstimator(
	       hm            = hm,
	       sample        = b,
	       data_sample   = data,
	       mc_samples    = mc_backgrounds + mc_signals,
	       rqcd_regions  = rqcd_regions_50L1TAU12med_highPT_1Track,
	       kf_regions    = kf_regions_50L1TAU12med_highPT_1Track,
	       addon_regions = addon_regions_50L1TAU12med_highPT_1Track,
	       print_info    = True,
	       )


	for b in addon_backgrounds_80med_lowPT_1Track:
	 b.estimator = histmgr.AddOnEstimator(
	       hm            = hm,
	       sample        = b,
	       data_sample   = data,
	       mc_samples    = mc_backgrounds + mc_signals,
	       rqcd_regions  = rqcd_regions_80med_lowPT_1Track,
	       kf_regions    = kf_regions_80med_lowPT_1Track,
	       addon_regions = addon_regions_80med_lowPT_1Track,
	       print_info    = True,
	       )

	for b in addon_backgrounds_80med_highPT_1Track:
	 b.estimator = histmgr.AddOnEstimator(
	       hm            = hm,
	       sample        = b,
	       data_sample   = data,
	       mc_samples    = mc_backgrounds + mc_signals,
	       rqcd_regions  = rqcd_regions_80med_highPT_1Track,
	       kf_regions    = kf_regions_80med_highPT_1Track,
	       addon_regions = addon_regions_80med_highPT_1Track,
	       print_info    = True,
	       )


	for b in addon_backgrounds_80L1TAU60med_lowPT_1Track:
	 b.estimator = histmgr.AddOnEstimator(
	       hm            = hm,
	       sample        = b,
	       data_sample   = data,
	       mc_samples    = mc_backgrounds + mc_signals,
	       rqcd_regions  = rqcd_regions_80L1TAU60med_lowPT_1Track,
	       kf_regions    = kf_regions_80L1TAU60med_lowPT_1Track,
	       addon_regions = addon_regions_80L1TAU60med_lowPT_1Track,
	       print_info    = True,
	       )

	for b in addon_backgrounds_80L1TAU60med_highPT_1Track:
	 b.estimator = histmgr.AddOnEstimator(
	       hm            = hm,
	       sample        = b,
	       data_sample   = data,
	       mc_samples    = mc_backgrounds + mc_signals,
	       rqcd_regions  = rqcd_regions_80L1TAU60med_highPT_1Track,
	       kf_regions    = kf_regions_80L1TAU60med_highPT_1Track,
	       addon_regions = addon_regions_80L1TAU60med_highPT_1Track,
	       print_info    = True,
	       )


	for b in addon_backgrounds_125med_lowPT_1Track:
	 b.estimator = histmgr.AddOnEstimator(
	       hm            = hm,
	       sample        = b,
	       data_sample   = data,
	       mc_samples    = mc_backgrounds + mc_signals,
	       rqcd_regions  = rqcd_regions_125med_lowPT_1Track,
	       kf_regions    = kf_regions_125med_lowPT_1Track,
	       addon_regions = addon_regions_125med_lowPT_1Track,
	       print_info    = True,
	       )

	for b in addon_backgrounds_125med_highPT_1Track:
	 b.estimator = histmgr.AddOnEstimator(
	       hm            = hm,
	       sample        = b,
	       data_sample   = data,
	       mc_samples    = mc_backgrounds + mc_signals,
	       rqcd_regions  = rqcd_regions_125med_highPT_1Track,
	       kf_regions    = kf_regions_125med_highPT_1Track,
	       addon_regions = addon_regions_125med_highPT_1Track,
	       print_info    = True,
	       )


	for b in addon_backgrounds_160med_lowPT_1Track:
	 b.estimator = histmgr.AddOnEstimator(
	       hm            = hm,
	       sample        = b,
	       data_sample   = data,
	       mc_samples    = mc_backgrounds + mc_signals,
	       rqcd_regions  = rqcd_regions_160med_lowPT_1Track,
	       kf_regions    = kf_regions_160med_lowPT_1Track,
	       addon_regions = addon_regions_160med_lowPT_1Track,
	       print_info    = True,
	       )

	for b in addon_backgrounds_160med_highPT_1Track:
	 b.estimator = histmgr.AddOnEstimator(
	       hm            = hm,
	       sample        = b,
	       data_sample   = data,
	       mc_samples    = mc_backgrounds + mc_signals,
	       rqcd_regions  = rqcd_regions_160med_highPT_1Track,
	       kf_regions    = kf_regions_160med_highPT_1Track,
	       addon_regions = addon_regions_160med_highPT_1Track,
	       print_info    = True,
	       )
        
	
	for b in addon_backgrounds_L1TAU12IMmed_lowPT_1Track:
	 b.estimator = histmgr.AddOnEstimator(
	       hm            = hm,
	       sample        = b,
	       data_sample   = data,
	       mc_samples    = mc_backgrounds + mc_signals,
	       rqcd_regions  = rqcd_regions_L1TAU12IMmed_lowPT_1Track,
	       kf_regions    = kf_regions_L1TAU12IMmed_lowPT_1Track,
	       addon_regions = addon_regions_L1TAU12IMmed_lowPT_1Track,
	       print_info    = True,
	       )

	for b in addon_backgrounds_L1TAU12IMmed_highPT_1Track:
	 b.estimator = histmgr.AddOnEstimator(
	       hm            = hm,
	       sample        = b,
	       data_sample   = data,
	       mc_samples    = mc_backgrounds + mc_signals,
	       rqcd_regions  = rqcd_regions_L1TAU12IMmed_highPT_1Track,
	       kf_regions    = kf_regions_L1TAU12IMmed_highPT_1Track,
	       addon_regions = addon_regions_L1TAU12IMmed_highPT_1Track,
	       print_info    = True,
	       )
       
	for b in addon_backgrounds_ptonly_lowPT_1Track:
	 b.estimator = histmgr.AddOnEstimator(
	       hm            = hm,
	       sample        = b,
	       data_sample   = data,
	       mc_samples    = mc_backgrounds + mc_signals,
	       rqcd_regions  = rqcd_regions_ptonly_lowPT_1Track,
	       kf_regions    = kf_regions_ptonly_lowPT_1Track,
	       addon_regions = addon_regions_ptonly_lowPT_1Track,
	       print_info    = True,
	       )

	for b in addon_backgrounds_ptonly_highPT_1Track:
	 b.estimator = histmgr.AddOnEstimator(
	       hm            = hm,
	       sample        = b,
	       data_sample   = data,
	       mc_samples    = mc_backgrounds + mc_signals,
	       rqcd_regions  = rqcd_regions_ptonly_highPT_1Track,
	       kf_regions    = kf_regions_ptonly_highPT_1Track,
	       addon_regions = addon_regions_ptonly_highPT_1Track,
	       print_info    = True,
	       )
        

	for b in addon_backgrounds_tracktwo_lowPT_1Track:
	 b.estimator = histmgr.AddOnEstimator(
	       hm            = hm,
	       sample        = b,
	       data_sample   = data,
	       mc_samples    = mc_backgrounds + mc_signals,
	       rqcd_regions  = rqcd_regions_tracktwo_lowPT_1Track,
	       kf_regions    = kf_regions_tracktwo_lowPT_1Track,
	       addon_regions = addon_regions_tracktwo_lowPT_1Track,
	       print_info    = True,
	       )

	for b in addon_backgrounds_tracktwo_highPT_1Track:
	 b.estimator = histmgr.AddOnEstimator(
	       hm            = hm,
	       sample        = b,
	       data_sample   = data,
	       mc_samples    = mc_backgrounds + mc_signals,
	       rqcd_regions  = rqcd_regions_tracktwo_highPT_1Track,
	       kf_regions    = kf_regions_tracktwo_highPT_1Track,
	       addon_regions = addon_regions_tracktwo_highPT_1Track,
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

	for b in addon_backgrounds_50L1TAU12med_lowPT_3Track:
	 b.estimator = histmgr.AddOnEstimator(
	       hm            = hm,
	       sample        = b,
	       data_sample   = data,
	       mc_samples    = mc_backgrounds + mc_signals,
	       rqcd_regions  = rqcd_regions_50L1TAU12med_lowPT_3Track,
	       kf_regions    = kf_regions_50L1TAU12med_lowPT_3Track,
	       addon_regions = addon_regions_50L1TAU12med_lowPT_3Track,
	       print_info    = True,
	       )

	for b in addon_backgrounds_50L1TAU12med_highPT_3Track:
	 b.estimator = histmgr.AddOnEstimator(
	       hm            = hm,
	       sample        = b,
	       data_sample   = data,
	       mc_samples    = mc_backgrounds + mc_signals,
	       rqcd_regions  = rqcd_regions_50L1TAU12med_highPT_3Track,
	       kf_regions    = kf_regions_50L1TAU12med_highPT_3Track,
	       addon_regions = addon_regions_50L1TAU12med_highPT_3Track,
	       print_info    = True,
	       )


	for b in addon_backgrounds_80med_lowPT_3Track:
	 b.estimator = histmgr.AddOnEstimator(
	       hm            = hm,
	       sample        = b,
	       data_sample   = data,
	       mc_samples    = mc_backgrounds + mc_signals,
	       rqcd_regions  = rqcd_regions_80med_lowPT_3Track,
	       kf_regions    = kf_regions_80med_lowPT_3Track,
	       addon_regions = addon_regions_80med_lowPT_3Track,
	       print_info    = True,
	       )

	for b in addon_backgrounds_80med_highPT_3Track:
	 b.estimator = histmgr.AddOnEstimator(
	       hm            = hm,
	       sample        = b,
	       data_sample   = data,
	       mc_samples    = mc_backgrounds + mc_signals,
	       rqcd_regions  = rqcd_regions_80med_highPT_3Track,
	       kf_regions    = kf_regions_80med_highPT_3Track,
	       addon_regions = addon_regions_80med_highPT_3Track,
	       print_info    = True,
	       )


	for b in addon_backgrounds_80L1TAU60med_lowPT_3Track:
	 b.estimator = histmgr.AddOnEstimator(
	       hm            = hm,
	       sample        = b,
	       data_sample   = data,
	       mc_samples    = mc_backgrounds + mc_signals,
	       rqcd_regions  = rqcd_regions_80L1TAU60med_lowPT_3Track,
	       kf_regions    = kf_regions_80L1TAU60med_lowPT_3Track,
	       addon_regions = addon_regions_80L1TAU60med_lowPT_3Track,
	       print_info    = True,
	       )

	for b in addon_backgrounds_80L1TAU60med_highPT_3Track:
	 b.estimator = histmgr.AddOnEstimator(
	       hm            = hm,
	       sample        = b,
	       data_sample   = data,
	       mc_samples    = mc_backgrounds + mc_signals,
	       rqcd_regions  = rqcd_regions_80L1TAU60med_highPT_3Track,
	       kf_regions    = kf_regions_80L1TAU60med_highPT_3Track,
	       addon_regions = addon_regions_80L1TAU60med_highPT_3Track,
	       print_info    = True,
	       )


	for b in addon_backgrounds_125med_lowPT_3Track:
	 b.estimator = histmgr.AddOnEstimator(
	       hm            = hm,
	       sample        = b,
	       data_sample   = data,
	       mc_samples    = mc_backgrounds + mc_signals,
	       rqcd_regions  = rqcd_regions_125med_lowPT_3Track,
	       kf_regions    = kf_regions_125med_lowPT_3Track,
	       addon_regions = addon_regions_125med_lowPT_3Track,
	       print_info    = True,
	       )

	for b in addon_backgrounds_125med_highPT_3Track:
	 b.estimator = histmgr.AddOnEstimator(
	       hm            = hm,
	       sample        = b,
	       data_sample   = data,
	       mc_samples    = mc_backgrounds + mc_signals,
	       rqcd_regions  = rqcd_regions_125med_highPT_3Track,
	       kf_regions    = kf_regions_125med_highPT_3Track,
	       addon_regions = addon_regions_125med_highPT_3Track,
	       print_info    = True,
	       )


	for b in addon_backgrounds_160med_lowPT_3Track:
	 b.estimator = histmgr.AddOnEstimator(
	       hm            = hm,
	       sample        = b,
	       data_sample   = data,
	       mc_samples    = mc_backgrounds + mc_signals,
	       rqcd_regions  = rqcd_regions_160med_lowPT_3Track,
	       kf_regions    = kf_regions_160med_lowPT_3Track,
	       addon_regions = addon_regions_160med_lowPT_3Track,
	       print_info    = True,
	       )

	for b in addon_backgrounds_160med_highPT_3Track:
	 b.estimator = histmgr.AddOnEstimator(
	       hm            = hm,
	       sample        = b,
	       data_sample   = data,
	       mc_samples    = mc_backgrounds + mc_signals,
	       rqcd_regions  = rqcd_regions_160med_highPT_3Track,
	       kf_regions    = kf_regions_160med_highPT_3Track,
	       addon_regions = addon_regions_160med_highPT_3Track,
	       print_info    = True,
	       )
	
	for b in addon_backgrounds_L1TAU12IMmed_lowPT_3Track:
	 b.estimator = histmgr.AddOnEstimator(
	       hm            = hm,
	       sample        = b,
	       data_sample   = data,
	       mc_samples    = mc_backgrounds + mc_signals,
	       rqcd_regions  = rqcd_regions_L1TAU12IMmed_lowPT_3Track,
	       kf_regions    = kf_regions_L1TAU12IMmed_lowPT_3Track,
	       addon_regions = addon_regions_L1TAU12IMmed_lowPT_3Track,
	       print_info    = True,
	       )

	for b in addon_backgrounds_L1TAU12IMmed_highPT_3Track:
	 b.estimator = histmgr.AddOnEstimator(
	       hm            = hm,
	       sample        = b,
	       data_sample   = data,
	       mc_samples    = mc_backgrounds + mc_signals,
	       rqcd_regions  = rqcd_regions_L1TAU12IMmed_highPT_3Track,
	       kf_regions    = kf_regions_L1TAU12IMmed_highPT_3Track,
	       addon_regions = addon_regions_L1TAU12IMmed_highPT_3Track,
	       print_info    = True,
	       )
 
	for b in addon_backgrounds_ptonly_lowPT_3Track:
	 b.estimator = histmgr.AddOnEstimator(
	       hm            = hm,
	       sample        = b,
	       data_sample   = data,
	       mc_samples    = mc_backgrounds + mc_signals,
	       rqcd_regions  = rqcd_regions_ptonly_lowPT_3Track,
	       kf_regions    = kf_regions_ptonly_lowPT_3Track,
	       addon_regions = addon_regions_ptonly_lowPT_3Track,
	       print_info    = True,
	       )

	for b in addon_backgrounds_ptonly_highPT_3Track:
	 b.estimator = histmgr.AddOnEstimator(
	       hm            = hm,
	       sample        = b,
	       data_sample   = data,
	       mc_samples    = mc_backgrounds + mc_signals,
	       rqcd_regions  = rqcd_regions_ptonly_highPT_3Track,
	       kf_regions    = kf_regions_ptonly_highPT_3Track,
	       addon_regions = addon_regions_ptonly_highPT_3Track,
	       print_info    = True,
	       )
        

	for b in addon_backgrounds_tracktwo_lowPT_3Track:
	 b.estimator = histmgr.AddOnEstimator(
	       hm            = hm,
	       sample        = b,
	       data_sample   = data,
	       mc_samples    = mc_backgrounds + mc_signals,
	       rqcd_regions  = rqcd_regions_tracktwo_lowPT_3Track,
	       kf_regions    = kf_regions_tracktwo_lowPT_3Track,
	       addon_regions = addon_regions_tracktwo_lowPT_3Track,
	       print_info    = True,
	       )

	for b in addon_backgrounds_tracktwo_highPT_3Track:
	 b.estimator = histmgr.AddOnEstimator(
	       hm            = hm,
	       sample        = b,
	       data_sample   = data,
	       mc_samples    = mc_backgrounds + mc_signals,
	       rqcd_regions  = rqcd_regions_tracktwo_highPT_3Track,
	       kf_regions    = kf_regions_tracktwo_highPT_3Track,
	       addon_regions = addon_regions_tracktwo_highPT_3Track,
	       print_info    = True,
	       )
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

	for i in range(len(addon_backgrounds_80med)):
	 m = addon_backgrounds_80med[i]
	 m.estimator = histmgr.MergeEstimator(
		hm = hm,
		sample = m,
		samples = [addon_backgrounds_80med_lowPT[i],addon_backgrounds_80med_highPT[i]]
		)

	for i in range(len(addon_backgrounds_50L1TAU12med)):
	 m = addon_backgrounds_50L1TAU12med[i]
	 m.estimator = histmgr.MergeEstimator(
		hm = hm,
		sample = m,
		samples = [addon_backgrounds_50L1TAU12med_lowPT[i],addon_backgrounds_50L1TAU12med_highPT[i]]
		)

	for i in range(len(addon_backgrounds_80L1TAU60med)):
	 m = addon_backgrounds_80L1TAU60med[i]
	 m.estimator = histmgr.MergeEstimator(
		hm = hm,
		sample = m,
		samples = [addon_backgrounds_80L1TAU60med_lowPT[i],addon_backgrounds_80L1TAU60med_highPT[i]]
		)

	for i in range(len(addon_backgrounds_125med)):
	 m = addon_backgrounds_125med[i]
	 m.estimator = histmgr.MergeEstimator(
		hm = hm,
		sample = m,
		samples = [addon_backgrounds_125med_lowPT[i],addon_backgrounds_125med_highPT[i]]
		)

	for i in range(len(addon_backgrounds_160med)):
	 m = addon_backgrounds_160med[i]
	 m.estimator = histmgr.MergeEstimator(
		hm = hm,
		sample = m,
		samples = [addon_backgrounds_160med_lowPT[i],addon_backgrounds_160med_highPT[i]]
		)
	
	for i in range(len(addon_backgrounds_L1TAU12IMmed)):
	 m = addon_backgrounds_L1TAU12IMmed[i]
	 m.estimator = histmgr.MergeEstimator(
		hm = hm,
		sample = m,
		samples = [addon_backgrounds_L1TAU12IMmed_lowPT[i],addon_backgrounds_L1TAU12IMmed_highPT[i]]
		)

	for i in range(len(addon_backgrounds_ptonly)):
	 m = addon_backgrounds_ptonly[i]
	 m.estimator = histmgr.MergeEstimator(
		hm = hm,
		sample = m,
		samples = [addon_backgrounds_ptonly_lowPT[i],addon_backgrounds_ptonly_highPT[i]]
		)
	
	for i in range(len(addon_backgrounds_tracktwo)):
	 m = addon_backgrounds_tracktwo[i]
	 m.estimator = histmgr.MergeEstimator(
		hm = hm,
		sample = m,
		samples = [addon_backgrounds_tracktwo_lowPT[i],addon_backgrounds_tracktwo_highPT[i]]
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

	for i in range(len(addon_backgrounds_50L1TAU12med_1Track)):
	 m = addon_backgrounds_50L1TAU12med_1Track[i]
	 m.estimator = histmgr.MergeEstimator(
		hm = hm,
		sample = m,
		samples = [addon_backgrounds_50L1TAU12med_lowPT_1Track[i],addon_backgrounds_50L1TAU12med_highPT_1Track[i]]
		)

	for i in range(len(addon_backgrounds_80med_1Track)):
	 m = addon_backgrounds_80med_1Track[i]
	 m.estimator = histmgr.MergeEstimator(
		hm = hm,
		sample = m,
		samples = [addon_backgrounds_80med_lowPT_1Track[i],addon_backgrounds_80med_highPT_1Track[i]]
		)

	for i in range(len(addon_backgrounds_80L1TAU60med_1Track)):
	 m = addon_backgrounds_80L1TAU60med_1Track[i]
	 m.estimator = histmgr.MergeEstimator(
		hm = hm,
		sample = m,
		samples = [addon_backgrounds_80L1TAU60med_lowPT_1Track[i],addon_backgrounds_80L1TAU60med_highPT_1Track[i]]
		)

	for i in range(len(addon_backgrounds_125med_1Track)):
	 m = addon_backgrounds_125med_1Track[i]
	 m.estimator = histmgr.MergeEstimator(
		hm = hm,
		sample = m,
		samples = [addon_backgrounds_125med_lowPT_1Track[i],addon_backgrounds_125med_highPT_1Track[i]]
		)

	for i in range(len(addon_backgrounds_160med_1Track)):
	 m = addon_backgrounds_160med_1Track[i]
	 m.estimator = histmgr.MergeEstimator(
		hm = hm,
		sample = m,
		samples = [addon_backgrounds_160med_lowPT_1Track[i],addon_backgrounds_160med_highPT_1Track[i]]
		)
	
	for i in range(len(addon_backgrounds_L1TAU12IMmed_1Track)):
	 m = addon_backgrounds_L1TAU12IMmed_1Track[i]
	 m.estimator = histmgr.MergeEstimator(
		hm = hm,
		sample = m,
		samples = [addon_backgrounds_L1TAU12IMmed_lowPT_1Track[i],addon_backgrounds_L1TAU12IMmed_highPT_1Track[i]]
		)

	for i in range(len(addon_backgrounds_ptonly_1Track)):
	 m = addon_backgrounds_ptonly_1Track[i]
	 m.estimator = histmgr.MergeEstimator(
		hm = hm,
		sample = m,
		samples = [addon_backgrounds_ptonly_lowPT_1Track[i],addon_backgrounds_ptonly_highPT_1Track[i]]
		)

	for i in range(len(addon_backgrounds_tracktwo_1Track)):
	 m = addon_backgrounds_tracktwo_1Track[i]
	 m.estimator = histmgr.MergeEstimator(
		hm = hm,
		sample = m,
		samples = [addon_backgrounds_tracktwo_lowPT_1Track[i],addon_backgrounds_tracktwo_highPT_1Track[i]]
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

	for i in range(len(addon_backgrounds_50L1TAU12med_3Track)):
	 m = addon_backgrounds_50L1TAU12med_3Track[i]
	 m.estimator = histmgr.MergeEstimator(
		hm = hm,
		sample = m,
		samples = [addon_backgrounds_50L1TAU12med_lowPT_3Track[i],addon_backgrounds_50L1TAU12med_highPT_3Track[i]]
		)

	for i in range(len(addon_backgrounds_80med_3Track)):
	 m = addon_backgrounds_80med_3Track[i]
	 m.estimator = histmgr.MergeEstimator(
		hm = hm,
		sample = m,
		samples = [addon_backgrounds_80med_lowPT_3Track[i],addon_backgrounds_80med_highPT_3Track[i]]
		)

	for i in range(len(addon_backgrounds_80L1TAU60med_3Track)):
	 m = addon_backgrounds_80L1TAU60med_3Track[i]
	 m.estimator = histmgr.MergeEstimator(
		hm = hm,
		sample = m,
		samples = [addon_backgrounds_80L1TAU60med_lowPT_3Track[i],addon_backgrounds_80L1TAU60med_highPT_3Track[i]]
		)

	for i in range(len(addon_backgrounds_125med_3Track)):
	 m = addon_backgrounds_125med_3Track[i]
	 m.estimator = histmgr.MergeEstimator(
		hm = hm,
		sample = m,
		samples = [addon_backgrounds_125med_lowPT_3Track[i],addon_backgrounds_125med_highPT_3Track[i]]
		)

	for i in range(len(addon_backgrounds_160med_3Track)):
	 m = addon_backgrounds_160med_3Track[i]
	 m.estimator = histmgr.MergeEstimator(
		hm = hm,
		sample = m,
		samples = [addon_backgrounds_160med_lowPT_3Track[i],addon_backgrounds_160med_highPT_3Track[i]]
		)
	
	for i in range(len(addon_backgrounds_L1TAU12IMmed_3Track)):
	 m = addon_backgrounds_L1TAU12IMmed_3Track[i]
	 m.estimator = histmgr.MergeEstimator(
		hm = hm,
		sample = m,
		samples = [addon_backgrounds_L1TAU12IMmed_lowPT_3Track[i],addon_backgrounds_L1TAU12IMmed_highPT_3Track[i]]
		)

	for i in range(len(addon_backgrounds_ptonly_3Track)):
	 m = addon_backgrounds_ptonly_3Track[i]
	 m.estimator = histmgr.MergeEstimator(
		hm = hm,
		sample = m,
		samples = [addon_backgrounds_ptonly_lowPT_3Track[i],addon_backgrounds_ptonly_highPT_3Track[i]]
		)

	for i in range(len(addon_backgrounds_tracktwo_3Track)):
	 m = addon_backgrounds_tracktwo_3Track[i]
	 m.estimator = histmgr.MergeEstimator(
		hm = hm,
		sample = m,
		samples = [addon_backgrounds_tracktwo_lowPT_3Track[i],addon_backgrounds_tracktwo_highPT_3Track[i]]
		)

	
	for b in addon_backgrounds_OS_no_cuts:
	 b.estimator = histmgr.AddOnEstimator(
	       hm            = hm,
	       sample        = b,
	       data_sample   = data,
	       mc_samples    = mc_backgrounds + mc_signals,
	       rqcd_regions  = rqcd_regions_OS_no_cuts,
	       kf_regions    = kf_regions_OS_no_cuts,
	       addon_regions = addon_regions_OS_no_cuts,
	       print_info    = True,
	       )
	
if ptbinning_y_or_n == "n":

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

	
	for b in addon_backgrounds_OS_no_cuts:
	 b.estimator = histmgr.AddOnEstimator(
	       hm            = hm,
	       sample        = b,
	       data_sample   = data,
	       mc_samples    = mc_backgrounds + mc_signals,
	       rqcd_regions  = rqcd_regions_OS_no_cuts,
	       kf_regions    = kf_regions_OS_no_cuts,
	       addon_regions = addon_regions_OS_no_cuts,
	       print_info    = True,
	       )
	
        for b in addon_backgrounds_lowSCDP_lowMT:
         b.estimator = histmgr.AddOnEstimator(
               hm            = hm,
               sample        = b,
               data_sample   = data,
               mc_samples    = mc_backgrounds + mc_signals,
               rqcd_regions  = rqcd_regions,
               kf_regions    = kf_regions,
               addon_regions = addon_regions_lowSCDP_lowMT,
               print_info    = True,
               )

        for b in addon_backgrounds_lowSCDP_highMT:
         b.estimator = histmgr.AddOnEstimator(
               hm            = hm,
               sample        = b,
               data_sample   = data,
               mc_samples    = mc_backgrounds + mc_signals,
               rqcd_regions  = rqcd_regions,
               kf_regions    = kf_regions,
               addon_regions = addon_regions_lowSCDP_highMT,
               print_info    = True,
               )

        for b in addon_backgrounds_highSCDP_highMT:
         b.estimator = histmgr.AddOnEstimator(
               hm            = hm,
               sample        = b,
               data_sample   = data,
               mc_samples    = mc_backgrounds + mc_signals,
               rqcd_regions  = rqcd_regions,
               kf_regions    = kf_regions,
               addon_regions = addon_regions_highSCDP_highMT,
               print_info    = True,
               )

        for b in addon_backgrounds_lowSCDP:
         b.estimator = histmgr.AddOnEstimator(
               hm            = hm,
               sample        = b,
               data_sample   = data,
               mc_samples    = mc_backgrounds + mc_signals,
               rqcd_regions  = rqcd_regions,
               kf_regions    = kf_regions,
               addon_regions = addon_regions_lowSCDP,
               print_info    = True,
               )

        for b in addon_backgrounds_highSCDP:
         b.estimator = histmgr.AddOnEstimator(
               hm            = hm,
               sample        = b,
               data_sample   = data,
               mc_samples    = mc_backgrounds + mc_signals,
               rqcd_regions  = rqcd_regions,
               kf_regions    = kf_regions,
               addon_regions = addon_regions_highSCDP,
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

	for b in addon_backgrounds_50L1TAU12med:
	 b.estimator = histmgr.AddOnEstimator(
	       hm            = hm,
	       sample        = b,
	       data_sample   = data,
	       mc_samples    = mc_backgrounds + mc_signals,
	       rqcd_regions  = rqcd_regions_50L1TAU12med,
	       kf_regions    = kf_regions_50L1TAU12med,
	       addon_regions = addon_regions_50L1TAU12med,
	       print_info    = True,
	       )

	for b in addon_backgrounds_80med:
	 b.estimator = histmgr.AddOnEstimator(
	       hm            = hm,
	       sample        = b,
	       data_sample   = data,
	       mc_samples    = mc_backgrounds + mc_signals,
	       rqcd_regions  = rqcd_regions_80med,
	       kf_regions    = kf_regions_80med,
	       addon_regions = addon_regions_80med,
	       print_info    = True,
	       )

	for b in addon_backgrounds_80L1TAU60med:
	 b.estimator = histmgr.AddOnEstimator(
	       hm            = hm,
	       sample        = b,
	       data_sample   = data,
	       mc_samples    = mc_backgrounds + mc_signals,
	       rqcd_regions  = rqcd_regions_80L1TAU60med,
	       kf_regions    = kf_regions_80L1TAU60med,
	       addon_regions = addon_regions_80L1TAU60med,
	       print_info    = True,
	       )

	for b in addon_backgrounds_125med:
	 b.estimator = histmgr.AddOnEstimator(
	       hm            = hm,
	       sample        = b,
	       data_sample   = data,
	       mc_samples    = mc_backgrounds + mc_signals,
	       rqcd_regions  = rqcd_regions_125med,
	       kf_regions    = kf_regions_125med,
	       addon_regions = addon_regions_125med,
	       print_info    = True,
	       )

	for b in addon_backgrounds_160med:
	 b.estimator = histmgr.AddOnEstimator(
	       hm            = hm,
	       sample        = b,
	       data_sample   = data,
	       mc_samples    = mc_backgrounds + mc_signals,
	       rqcd_regions  = rqcd_regions_160med,
	       kf_regions    = kf_regions_160med,
	       addon_regions = addon_regions_160med,
	       print_info    = True,
	       )

	for b in addon_backgrounds_L1TAU12IMmed:
	 b.estimator = histmgr.AddOnEstimator(
	       hm            = hm,
	       sample        = b,
	       data_sample   = data,
	       mc_samples    = mc_backgrounds + mc_signals,
	       rqcd_regions  = rqcd_regions_L1TAU12IMmed,
	       kf_regions    = kf_regions_L1TAU12IMmed,
	       addon_regions = addon_regions_L1TAU12IMmed,
	       print_info    = True,
	       )

	for b in addon_backgrounds_ptonly:
	 b.estimator = histmgr.AddOnEstimator(
	       hm            = hm,
	       sample        = b,
	       data_sample   = data,
	       mc_samples    = mc_backgrounds + mc_signals,
	       rqcd_regions  = rqcd_regions_ptonly,
	       kf_regions    = kf_regions_ptonly,
	       addon_regions = addon_regions_ptonly,
	       print_info    = True,
	       )

	for b in addon_backgrounds_tracktwo:
	 b.estimator = histmgr.AddOnEstimator(
	       hm            = hm,
	       sample        = b,
	       data_sample   = data,
	       mc_samples    = mc_backgrounds + mc_signals,
	       rqcd_regions  = rqcd_regions_tracktwo,
	       kf_regions    = kf_regions_tracktwo,
	       addon_regions = addon_regions_tracktwo,
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

	for b in addon_backgrounds_50L1TAU12med_1Track:
	 b.estimator = histmgr.AddOnEstimator(
	       hm            = hm,
	       sample        = b,
	       data_sample   = data,
	       mc_samples    = mc_backgrounds + mc_signals,
	       rqcd_regions  = rqcd_regions_50L1TAU12med_1Track,
	       kf_regions    = kf_regions_50L1TAU12med_1Track,
	       addon_regions = addon_regions_50L1TAU12med_1Track,
	       print_info    = True,
	       )

	for b in addon_backgrounds_80med_1Track:
	 b.estimator = histmgr.AddOnEstimator(
	       hm            = hm,
	       sample        = b,
	       data_sample   = data,
	       mc_samples    = mc_backgrounds + mc_signals,
	       rqcd_regions  = rqcd_regions_80med_1Track,
	       kf_regions    = kf_regions_80med_1Track,
	       addon_regions = addon_regions_80med_1Track,
	       print_info    = True,
	       )

	for b in addon_backgrounds_80L1TAU60med_1Track:
	 b.estimator = histmgr.AddOnEstimator(
	       hm            = hm,
	       sample        = b,
	       data_sample   = data,
	       mc_samples    = mc_backgrounds + mc_signals,
	       rqcd_regions  = rqcd_regions_80L1TAU60med_1Track,
	       kf_regions    = kf_regions_80L1TAU60med_1Track,
	       addon_regions = addon_regions_80L1TAU60med_1Track,
	       print_info    = True,
	       )

	for b in addon_backgrounds_125med_1Track:
	 b.estimator = histmgr.AddOnEstimator(
	       hm            = hm,
	       sample        = b,
	       data_sample   = data,
	       mc_samples    = mc_backgrounds + mc_signals,
	       rqcd_regions  = rqcd_regions_125med_1Track,
	       kf_regions    = kf_regions_125med_1Track,
	       addon_regions = addon_regions_125med_1Track,
	       print_info    = True,
	       )

	for b in addon_backgrounds_160med_1Track:
	 b.estimator = histmgr.AddOnEstimator(
	       hm            = hm,
	       sample        = b,
	       data_sample   = data,
	       mc_samples    = mc_backgrounds + mc_signals,
	       rqcd_regions  = rqcd_regions_160med_1Track,
	       kf_regions    = kf_regions_160med_1Track,
	       addon_regions = addon_regions_160med_1Track,
	       print_info    = True,
	       )
	
	for b in addon_backgrounds_L1TAU12IMmed_1Track:
	 b.estimator = histmgr.AddOnEstimator(
	       hm            = hm,
	       sample        = b,
	       data_sample   = data,
	       mc_samples    = mc_backgrounds + mc_signals,
	       rqcd_regions  = rqcd_regions_L1TAU12IMmed_1Track,
	       kf_regions    = kf_regions_L1TAU12IMmed_1Track,
	       addon_regions = addon_regions_L1TAU12IMmed_1Track,
	       print_info    = True,
	       )

	for b in addon_backgrounds_ptonly_1Track:
	 b.estimator = histmgr.AddOnEstimator(
	       hm            = hm,
	       sample        = b,
	       data_sample   = data,
	       mc_samples    = mc_backgrounds + mc_signals,
	       rqcd_regions  = rqcd_regions_ptonly_1Track,
	       kf_regions    = kf_regions_ptonly_1Track,
	       addon_regions = addon_regions_ptonly_1Track,
	       print_info    = True,
	       )

	for b in addon_backgrounds_tracktwo_1Track:
	 b.estimator = histmgr.AddOnEstimator(
	       hm            = hm,
	       sample        = b,
	       data_sample   = data,
	       mc_samples    = mc_backgrounds + mc_signals,
	       rqcd_regions  = rqcd_regions_tracktwo_1Track,
	       kf_regions    = kf_regions_tracktwo_1Track,
	       addon_regions = addon_regions_tracktwo_1Track,
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
	
	for b in addon_backgrounds_50L1TAU12med_3Track:
	 b.estimator = histmgr.AddOnEstimator(
	       hm            = hm,
	       sample        = b,
	       data_sample   = data,
	       mc_samples    = mc_backgrounds + mc_signals,
	       rqcd_regions  = rqcd_regions_50L1TAU12med_3Track,
	       kf_regions    = kf_regions_50L1TAU12med_3Track,
	       addon_regions = addon_regions_50L1TAU12med_3Track,
	       print_info    = True,
	       )

	for b in addon_backgrounds_80med_3Track:
	 b.estimator = histmgr.AddOnEstimator(
	       hm            = hm,
	       sample        = b,
	       data_sample   = data,
	       mc_samples    = mc_backgrounds + mc_signals,
	       rqcd_regions  = rqcd_regions_80med_3Track,
	       kf_regions    = kf_regions_80med_3Track,
	       addon_regions = addon_regions_80med_3Track,
	       print_info    = True,
	       )

	for b in addon_backgrounds_80L1TAU60med_3Track:
	 b.estimator = histmgr.AddOnEstimator(
	       hm            = hm,
	       sample        = b,
	       data_sample   = data,
	       mc_samples    = mc_backgrounds + mc_signals,
	       rqcd_regions  = rqcd_regions_80L1TAU60med_3Track,
	       kf_regions    = kf_regions_80L1TAU60med_3Track,
	       addon_regions = addon_regions_80L1TAU60med_3Track,
	       print_info    = True,
	       )

	for b in addon_backgrounds_125med_3Track:
	 b.estimator = histmgr.AddOnEstimator(
	       hm            = hm,
	       sample        = b,
	       data_sample   = data,
	       mc_samples    = mc_backgrounds + mc_signals,
	       rqcd_regions  = rqcd_regions_125med_3Track,
	       kf_regions    = kf_regions_125med_3Track,
	       addon_regions = addon_regions_125med_3Track,
	       print_info    = True,
	       )

	for b in addon_backgrounds_160med_3Track:
	 b.estimator = histmgr.AddOnEstimator(
	       hm            = hm,
	       sample        = b,
	       data_sample   = data,
	       mc_samples    = mc_backgrounds + mc_signals,
	       rqcd_regions  = rqcd_regions_160med_3Track,
	       kf_regions    = kf_regions_160med_3Track,
	       addon_regions = addon_regions_160med_3Track,
	       print_info    = True,
	       )
	
	for b in addon_backgrounds_L1TAU12IMmed_3Track:
	 b.estimator = histmgr.AddOnEstimator(
	       hm            = hm,
	       sample        = b,
	       data_sample   = data,
	       mc_samples    = mc_backgrounds + mc_signals,
	       rqcd_regions  = rqcd_regions_L1TAU12IMmed_3Track,
	       kf_regions    = kf_regions_L1TAU12IMmed_3Track,
	       addon_regions = addon_regions_L1TAU12IMmed_3Track,
	       print_info    = True,
	       )

	for b in addon_backgrounds_ptonly_3Track:
	 b.estimator = histmgr.AddOnEstimator(
	       hm            = hm,
	       sample        = b,
	       data_sample   = data,
	       mc_samples    = mc_backgrounds + mc_signals,
	       rqcd_regions  = rqcd_regions_ptonly_3Track,
	       kf_regions    = kf_regions_ptonly_3Track,
	       addon_regions = addon_regions_ptonly_3Track,
	       print_info    = True,
	       )

	for b in addon_backgrounds_tracktwo_3Track:
	 b.estimator = histmgr.AddOnEstimator(
	       hm            = hm,
	       sample        = b,
	       data_sample   = data,
	       mc_samples    = mc_backgrounds + mc_signals,
	       rqcd_regions  = rqcd_regions_tracktwo_3Track,
	       kf_regions    = kf_regions_tracktwo_3Track,
	       addon_regions = addon_regions_tracktwo_3Track,
	       print_info    = True,
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

sub_ztt_50L1TAU12med.estimator = histmgr.DataBkgSubEstimator(
	hm = hm,
	sample = sub_ztt_50L1TAU12med,
	data_sample = data,
	mc_samples = addon_backgrounds_50L1TAU12med,
	mc_samples_rescales = None,
	) 

sub_ztt_80med.estimator = histmgr.DataBkgSubEstimator(
	hm = hm,
	sample = sub_ztt_80med,
	data_sample = data,
	mc_samples = addon_backgrounds_80med,
	mc_samples_rescales = None,
	) 

sub_ztt_80L1TAU60med.estimator = histmgr.DataBkgSubEstimator(
	hm = hm,
	sample = sub_ztt_80L1TAU60med,
	data_sample = data,
	mc_samples = addon_backgrounds_80L1TAU60med,
	mc_samples_rescales = None,
	) 

sub_ztt_125med.estimator = histmgr.DataBkgSubEstimator(
	hm = hm,
	sample = sub_ztt_125med,
	data_sample = data,
	mc_samples = addon_backgrounds_125med,
	mc_samples_rescales = None,
	) 

sub_ztt_160med.estimator = histmgr.DataBkgSubEstimator(
	hm = hm,
	sample = sub_ztt_160med,
	data_sample = data,
	mc_samples = addon_backgrounds_160med,
	mc_samples_rescales = None,
	) 

sub_ztt_L1TAU12IMmed.estimator = histmgr.DataBkgSubEstimator(
	hm = hm,
	sample = sub_ztt_L1TAU12IMmed,
	data_sample = data,
	mc_samples = addon_backgrounds_L1TAU12IMmed,
	mc_samples_rescales = None,
	) 


sub_ztt_ptonly.estimator = histmgr.DataBkgSubEstimator(
	hm = hm,
	sample = sub_ztt_ptonly,
	data_sample = data,
	mc_samples = addon_backgrounds_ptonly,
	mc_samples_rescales = None,
	) 


sub_ztt_tracktwo.estimator = histmgr.DataBkgSubEstimator(
	hm = hm,
	sample = sub_ztt_tracktwo,
	data_sample = data,
	mc_samples = addon_backgrounds_tracktwo,
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

sub_ztt_50L1TAU12med_1Track.estimator = histmgr.DataBkgSubEstimator(
	hm = hm,
	sample = sub_ztt_50L1TAU12med_1Track,
	data_sample = data,
	mc_samples = addon_backgrounds_50L1TAU12med_1Track,
	mc_samples_rescales = None,
	) 

sub_ztt_80med_1Track.estimator = histmgr.DataBkgSubEstimator(
	hm = hm,
	sample = sub_ztt_80med_1Track,
	data_sample = data,
	mc_samples = addon_backgrounds_80med_1Track,
	mc_samples_rescales = None,
	) 

sub_ztt_80L1TAU60med_1Track.estimator = histmgr.DataBkgSubEstimator(
	hm = hm,
	sample = sub_ztt_80L1TAU60med_1Track,
	data_sample = data,
	mc_samples = addon_backgrounds_80L1TAU60med_1Track,
	mc_samples_rescales = None,
	) 

sub_ztt_125med_1Track.estimator = histmgr.DataBkgSubEstimator(
	hm = hm,
	sample = sub_ztt_125med_1Track,
	data_sample = data,
	mc_samples = addon_backgrounds_125med_1Track,
	mc_samples_rescales = None,
	) 

sub_ztt_160med_1Track.estimator = histmgr.DataBkgSubEstimator(
	hm = hm,
	sample = sub_ztt_160med_1Track,
	data_sample = data,
	mc_samples = addon_backgrounds_160med_1Track,
	mc_samples_rescales = None,
	) 

sub_ztt_L1TAU12IMmed_1Track.estimator = histmgr.DataBkgSubEstimator(
	hm = hm,
	sample = sub_ztt_L1TAU12IMmed_1Track,
	data_sample = data,
	mc_samples = addon_backgrounds_L1TAU12IMmed_1Track,
	mc_samples_rescales = None,
	) 

sub_ztt_ptonly_1Track.estimator = histmgr.DataBkgSubEstimator(
	hm = hm,
	sample = sub_ztt_ptonly_1Track,
	data_sample = data,
	mc_samples = addon_backgrounds_ptonly_1Track,
	mc_samples_rescales = None,
	) 

sub_ztt_tracktwo_1Track.estimator = histmgr.DataBkgSubEstimator(
	hm = hm,
	sample = sub_ztt_tracktwo_1Track,
	data_sample = data,
	mc_samples = addon_backgrounds_tracktwo_1Track,
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

sub_ztt_50L1TAU12med_3Track.estimator = histmgr.DataBkgSubEstimator(
	hm = hm,
	sample = sub_ztt_50L1TAU12med_3Track,
	data_sample = data,
	mc_samples = addon_backgrounds_50L1TAU12med_3Track,
	mc_samples_rescales = None,
	) 

sub_ztt_80med_3Track.estimator = histmgr.DataBkgSubEstimator(
	hm = hm,
	sample = sub_ztt_80med_3Track,
	data_sample = data,
	mc_samples = addon_backgrounds_80med_3Track,
	mc_samples_rescales = None,
	) 

sub_ztt_80L1TAU60med_3Track.estimator = histmgr.DataBkgSubEstimator(
	hm = hm,
	sample = sub_ztt_80L1TAU60med_3Track,
	data_sample = data,
	mc_samples = addon_backgrounds_80L1TAU60med_3Track,
	mc_samples_rescales = None,
	) 

sub_ztt_125med_3Track.estimator = histmgr.DataBkgSubEstimator(
	hm = hm,
	sample = sub_ztt_125med_3Track,
	data_sample = data,
	mc_samples = addon_backgrounds_125med_3Track,
	mc_samples_rescales = None,
	) 

sub_ztt_160med_3Track.estimator = histmgr.DataBkgSubEstimator(
	hm = hm,
	sample = sub_ztt_160med_3Track,
	data_sample = data,
	mc_samples = addon_backgrounds_160med_3Track,
	mc_samples_rescales = None,
	) 

sub_ztt_L1TAU12IMmed_3Track.estimator = histmgr.DataBkgSubEstimator(
	hm = hm,
	sample = sub_ztt_L1TAU12IMmed_3Track,
	data_sample = data,
	mc_samples = addon_backgrounds_L1TAU12IMmed_3Track,
	mc_samples_rescales = None,
	) 

sub_ztt_ptonly_3Track.estimator = histmgr.DataBkgSubEstimator(
	hm = hm,
	sample = sub_ztt_ptonly_3Track,
	data_sample = data,
	mc_samples = addon_backgrounds_ptonly_3Track,
	mc_samples_rescales = None,
	) 

sub_ztt_tracktwo_3Track.estimator = histmgr.DataBkgSubEstimator(
	hm = hm,
	sample = sub_ztt_tracktwo_3Track,
	data_sample = data,
	mc_samples = addon_backgrounds_tracktwo_3Track,
	mc_samples_rescales = None,
	) 

#-----------------
# Systematics       
#-----------------

for s in mc_signals:
    s.estimator.add_systematics(MUID)
    s.estimator.add_systematics(MUMS)
    s.estimator.add_systematics(MUSCALE)
    s.estimator.add_systematics(TAUSF_SYS)
    s.estimator.add_systematics(MUSF_SYS)
    s.estimator.add_systematics(MUSF_STAT)
    s.estimator.add_systematics(METSCALE)
    s.estimator.add_systematics(PILEUP)


if ptbinning_y_or_n == "n":
	
	# NO PT BINNING
	"""
	for s in addon_backgrounds:
            #s.estimator.add_systematics(kW)
	    s.estimator.add_systematics(RQCD_AntiIsoCR_highPT)
	    s.estimator.add_systematics(RQCD_AntiIsoCR_lowPT)
	    s.estimator.add_systematics(MUID)
	    s.estimator.add_systematics(MUMS)
	    s.estimator.add_systematics(MUSCALE)
	    s.estimator.add_systematics(TAUSF_SYS)
	    s.estimator.add_systematics(MUSF_SYS)
	    s.estimator.add_systematics(MUSF_STAT)
	    s.estimator.add_systematics(METSCALE)
	
	for t in addon_backgrounds_25med:
                #t.estimator.add_systematics(kW_25med)
		t.estimator.add_systematics(RQCD_AntiIsoCR_25med)
		t.estimator.add_systematics(MUID)
		t.estimator.add_systematics(MUMS)
		t.estimator.add_systematics(MUSCALE)
		t.estimator.add_systematics(TAUSF_SYS)
		t.estimator.add_systematics(MUSF_SYS)
		t.estimator.add_systematics(MUSF_STAT)
		t.estimator.add_systematics(METSCALE)
	"""
	for t in addon_backgrounds_35med:
                #t.estimator.add_systematics(kW_35med)
		t.estimator.add_systematics(RQCD_AntiIsoCR_35med_highPT)
		t.estimator.add_systematics(RQCD_AntiIsoCR_35med_lowPT)
		t.estimator.add_systematics(MUID)
		t.estimator.add_systematics(MUMS)
		t.estimator.add_systematics(MUSCALE)
		t.estimator.add_systematics(TAUSF_SYS)
		t.estimator.add_systematics(MUSF_SYS)
		t.estimator.add_systematics(MUSF_STAT)
		t.estimator.add_systematics(METSCALE)


	for t in addon_backgrounds_50L1TAU12med:
                #t.estimator.add_systematics(kW_50L1TAU12med)
		t.estimator.add_systematics(RQCD_AntiIsoCR_50L1TAU12med_highPT)
		t.estimator.add_systematics(MUID)
		t.estimator.add_systematics(RQCD_AntiIsoCR_50L1TAU12med_lowPT)
		t.estimator.add_systematics(MUMS)
		t.estimator.add_systematics(MUSCALE)
		t.estimator.add_systematics(TAUSF_SYS)
		t.estimator.add_systematics(MUSF_SYS)
		t.estimator.add_systematics(MUSF_STAT)
		t.estimator.add_systematics(METSCALE)


	for t in addon_backgrounds_80med:
                #t.estimator.add_systematics(kW_80med)
		t.estimator.add_systematics(RQCD_AntiIsoCR_80med_highPT)
		t.estimator.add_systematics(MUID)
		t.estimator.add_systematics(RQCD_AntiIsoCR_80med_lowPT)
		t.estimator.add_systematics(MUMS)
		t.estimator.add_systematics(MUSCALE)
		t.estimator.add_systematics(TAUSF_SYS)
		t.estimator.add_systematics(MUSF_SYS)
		t.estimator.add_systematics(MUSF_STAT)
		t.estimator.add_systematics(METSCALE)


	for t in addon_backgrounds_80L1TAU60med:
                #t.estimator.add_systematics(kW_80L1TAU60med)
		t.estimator.add_systematics(RQCD_AntiIsoCR_80L1TAU60med_highPT)
		t.estimator.add_systematics(MUID)
		t.estimator.add_systematics(RQCD_AntiIsoCR_80L1TAU60med_lowPT)
		t.estimator.add_systematics(MUMS)
		t.estimator.add_systematics(MUSCALE)
		t.estimator.add_systematics(TAUSF_SYS)
		t.estimator.add_systematics(MUSF_SYS)
		t.estimator.add_systematics(MUSF_STAT)
		t.estimator.add_systematics(METSCALE)


	for t in addon_backgrounds_125med:
                #t.estimator.add_systematics(kW_125med)
		t.estimator.add_systematics(RQCD_AntiIsoCR_125med_lowPT)
		t.estimator.add_systematics(RQCD_AntiIsoCR_125med_highPT)
		t.estimator.add_systematics(MUID)
		t.estimator.add_systematics(MUMS)
		t.estimator.add_systematics(MUSCALE)
		t.estimator.add_systematics(TAUSF_SYS)
		t.estimator.add_systematics(MUSF_SYS)
		t.estimator.add_systematics(MUSF_STAT)
		t.estimator.add_systematics(METSCALE)


	for t in addon_backgrounds_160med:
                #t.estimator.add_systematics(kW_160med)
		t.estimator.add_systematics(RQCD_AntiIsoCR_160med_highPT)
		t.estimator.add_systematics(RQCD_AntiIsoCR_160med_lowPT)
		t.estimator.add_systematics(MUID)
		t.estimator.add_systematics(MUMS)
		t.estimator.add_systematics(MUSCALE)
		t.estimator.add_systematics(TAUSF_SYS)
		t.estimator.add_systematics(MUSF_SYS)
		t.estimator.add_systematics(MUSF_STAT)
		t.estimator.add_systematics(METSCALE)
	
	for v in addon_backgrounds_1Track:
            #v.estimator.add_systematics(kW_highPT_Tau1Track)
	    v.estimator.add_systematics(RQCD_AntiIsoCR_highPT_Tau1Track)
	    v.estimator.add_systematics(RQCD_AntiIsoCR_lowPT_Tau1Track)
	    v.estimator.add_systematics(MUID)
	    v.estimator.add_systematics(MUMS)
	    v.estimator.add_systematics(MUSCALE)
	    v.estimator.add_systematics(TAUSF_SYS)
	    v.estimator.add_systematics(MUSF_SYS)
	    v.estimator.add_systematics(MUSF_STAT)
	    v.estimator.add_systematics(METSCALE)
	    v.estimator.add_systematics(PILEUP)
            v.estimator.add_systematics(fw_highPT_1Track)
            v.estimator.add_systematics(fw_lowPT_1Track)

	for v in addon_backgrounds_3Track:
            #v.estimator.add_systematics(kW_highPT_Tau3Track)
	    v.estimator.add_systematics(RQCD_AntiIsoCR_highPT_Tau3Track)
	    v.estimator.add_systematics(RQCD_AntiIsoCR_highPT_Tau3Track)
	    v.estimator.add_systematics(MUID)
	    v.estimator.add_systematics(MUMS)
	    v.estimator.add_systematics(MUSCALE)
	    v.estimator.add_systematics(TAUSF_SYS)
	    v.estimator.add_systematics(MUSF_SYS)
	    v.estimator.add_systematics(MUSF_STAT)
	    v.estimator.add_systematics(METSCALE)
	    v.estimator.add_systematics(PILEUP)
            v.estimator.add_systematics(fw_highPT_3Track)
            v.estimator.add_systematics(fw_lowPT_3Track)

	for v in addon_backgrounds_35med_3Track:
            #v.estimator.add_systematics(kW_35med_highPT_Tau3Track)
	    v.estimator.add_systematics(RQCD_AntiIsoCR_35med_highPT_Tau3Track)
	    v.estimator.add_systematics(RQCD_AntiIsoCR_35med_highPT_Tau3Track)
	    v.estimator.add_systematics(MUID)
	    v.estimator.add_systematics(MUMS)
	    v.estimator.add_systematics(MUSCALE)
	    v.estimator.add_systematics(TAUSF_SYS)
	    v.estimator.add_systematics(MUSF_SYS)
	    v.estimator.add_systematics(MUSF_STAT)
	    v.estimator.add_systematics(METSCALE)
	    v.estimator.add_systematics(PILEUP)
            v.estimator.add_systematics(fw_highPT_3Track_35med)
            v.estimator.add_systematics(fw_highPT_3Track_35med)

	for u in addon_backgrounds_50L1TAU12med_3Track:
            #u.estimator.add_systematics(kW_50L1TAU12med_lowPT_Tau3Track)
	    u.estimator.add_systematics(RQCD_AntiIsoCR_50L1TAU12med_lowPT_Tau3Track) 
	    u.estimator.add_systematics(RQCD_AntiIsoCR_50L1TAU12med_highPT_Tau3Track) 
	    u.estimator.add_systematics(MUID)
	    u.estimator.add_systematics(MUMS)
	    u.estimator.add_systematics(MUSCALE)
	    u.estimator.add_systematics(TAUSF_SYS)
	    u.estimator.add_systematics(MUSF_SYS)
	    u.estimator.add_systematics(MUSF_STAT)
	    u.estimator.add_systematics(METSCALE)
	    u.estimator.add_systematics(PILEUP)
	    u.estimator.add_systematics(fw_lowPT_3Track_50L1TAU12med)
	    u.estimator.add_systematics(fw_highPT_3Track_50L1TAU12med)

	for u in addon_backgrounds_80med_3Track:
            #u.estimator.add_systematics(kW_80med_lowPT_Tau3Track)
	    u.estimator.add_systematics(RQCD_AntiIsoCR_80med_lowPT_Tau3Track) 
	    u.estimator.add_systematics(RQCD_AntiIsoCR_80med_highPT_Tau3Track) 
	    u.estimator.add_systematics(MUID)
	    u.estimator.add_systematics(MUMS)
	    u.estimator.add_systematics(MUSCALE)
	    u.estimator.add_systematics(TAUSF_SYS)
	    u.estimator.add_systematics(MUSF_SYS)
	    u.estimator.add_systematics(MUSF_STAT)
	    u.estimator.add_systematics(METSCALE)
	    u.estimator.add_systematics(PILEUP)
            u.estimator.add_systematics(fw_lowPT_3Track_80med)
            u.estimator.add_systematics(fw_highPT_3Track_80med)

	for u in addon_backgrounds_80L1TAU60med_3Track:
            #u.estimator.add_systematics(kW_80L1TAU60med_lowPT_Tau3Track)
	    u.estimator.add_systematics(RQCD_AntiIsoCR_80L1TAU60med_lowPT_Tau3Track) 
	    u.estimator.add_systematics(RQCD_AntiIsoCR_80L1TAU60med_highPT_Tau3Track) 
	    u.estimator.add_systematics(MUID)
	    u.estimator.add_systematics(MUMS)
	    u.estimator.add_systematics(MUSCALE)
	    u.estimator.add_systematics(TAUSF_SYS)
	    u.estimator.add_systematics(MUSF_SYS)
	    u.estimator.add_systematics(MUSF_STAT)
	    u.estimator.add_systematics(METSCALE)
	    u.estimator.add_systematics(PILEUP)
            u.estimator.add_systematics(fw_lowPT_3Track_80L1TAU60med)
            u.estimator.add_systematics(fw_highPT_3Track_80L1TAU60med)

	for u in addon_backgrounds_125med_3Track:
            #u.estimator.add_systematics(kW_125med_lowPT_Tau3Track)
	    u.estimator.add_systematics(RQCD_AntiIsoCR_125med_lowPT_Tau3Track) 
	    u.estimator.add_systematics(RQCD_AntiIsoCR_125med_highPT_Tau3Track) 
	    u.estimator.add_systematics(MUID)
	    u.estimator.add_systematics(MUMS)
	    u.estimator.add_systematics(MUSCALE)
	    u.estimator.add_systematics(TAUSF_SYS)
	    u.estimator.add_systematics(MUSF_SYS)
	    u.estimator.add_systematics(MUSF_STAT)
	    u.estimator.add_systematics(METSCALE)
	    u.estimator.add_systematics(PILEUP)
            u.estimator.add_systematics(fw_lowPT_3Track_125med)
            u.estimator.add_systematics(fw_highPT_3Track_125med)

	for u in addon_backgrounds_160med_3Track:
            #u.estimator.add_systematics(kW_160med_lowPT_Tau3Track)
	    u.estimator.add_systematics(RQCD_AntiIsoCR_160med_lowPT_Tau3Track) 
	    u.estimator.add_systematics(RQCD_AntiIsoCR_160med_highPT_Tau3Track) 
	    u.estimator.add_systematics(MUID)
	    u.estimator.add_systematics(MUMS)
	    u.estimator.add_systematics(MUSCALE)
	    u.estimator.add_systematics(TAUSF_SYS)
	    u.estimator.add_systematics(MUSF_SYS)
	    u.estimator.add_systematics(MUSF_STAT)
	    u.estimator.add_systematics(METSCALE)
	    u.estimator.add_systematics(PILEUP)
            u.estimator.add_systematics(fw_lowPT_3Track_160med)
            u.estimator.add_systematics(fw_highPT_3Track_160med)

	for v in addon_backgrounds_35med_1Track:
            #v.estimator.add_systematics(kW_35med_highPT_Tau1Track)
	    v.estimator.add_systematics(RQCD_AntiIsoCR_35med_highPT_Tau1Track)
	    v.estimator.add_systematics(RQCD_AntiIsoCR_35med_highPT_Tau1Track)
	    v.estimator.add_systematics(MUID)
	    v.estimator.add_systematics(MUMS)
	    v.estimator.add_systematics(MUSCALE)
	    v.estimator.add_systematics(TAUSF_SYS)
	    v.estimator.add_systematics(MUSF_SYS)
	    v.estimator.add_systematics(MUSF_STAT)
	    v.estimator.add_systematics(METSCALE)
	    v.estimator.add_systematics(PILEUP)
            v.estimator.add_systematics(fw_highPT_1Track_35med)
            v.estimator.add_systematics(fw_highPT_1Track_35med)

	for u in addon_backgrounds_50L1TAU12med_1Track:
            #u.estimator.add_systematics(kW_50L1TAU12med_lowPT_Tau1Track)
	    u.estimator.add_systematics(RQCD_AntiIsoCR_50L1TAU12med_lowPT_Tau1Track) 
	    u.estimator.add_systematics(RQCD_AntiIsoCR_50L1TAU12med_highPT_Tau1Track) 
	    u.estimator.add_systematics(MUID)
	    u.estimator.add_systematics(MUMS)
	    u.estimator.add_systematics(MUSCALE)
	    u.estimator.add_systematics(TAUSF_SYS)
	    u.estimator.add_systematics(MUSF_SYS)
	    u.estimator.add_systematics(MUSF_STAT)
	    u.estimator.add_systematics(METSCALE)
	    u.estimator.add_systematics(PILEUP)
	    u.estimator.add_systematics(fw_lowPT_1Track_50L1TAU12med)
	    u.estimator.add_systematics(fw_highPT_1Track_50L1TAU12med)

	for u in addon_backgrounds_80med_1Track:
            #u.estimator.add_systematics(kW_80med_lowPT_Tau1Track)
	    u.estimator.add_systematics(RQCD_AntiIsoCR_80med_lowPT_Tau1Track) 
	    u.estimator.add_systematics(RQCD_AntiIsoCR_80med_highPT_Tau1Track) 
	    u.estimator.add_systematics(MUID)
	    u.estimator.add_systematics(MUMS)
	    u.estimator.add_systematics(MUSCALE)
	    u.estimator.add_systematics(TAUSF_SYS)
	    u.estimator.add_systematics(MUSF_SYS)
	    u.estimator.add_systematics(MUSF_STAT)
	    u.estimator.add_systematics(METSCALE)
	    u.estimator.add_systematics(PILEUP)
            u.estimator.add_systematics(fw_lowPT_1Track_80med)
            u.estimator.add_systematics(fw_highPT_1Track_80med)

	for u in addon_backgrounds_80L1TAU60med_1Track:
            #u.estimator.add_systematics(kW_80L1TAU60med_lowPT_Tau1Track)
	    u.estimator.add_systematics(RQCD_AntiIsoCR_80L1TAU60med_lowPT_Tau1Track) 
	    u.estimator.add_systematics(RQCD_AntiIsoCR_80L1TAU60med_highPT_Tau1Track) 
	    u.estimator.add_systematics(MUID)
	    u.estimator.add_systematics(MUMS)
	    u.estimator.add_systematics(MUSCALE)
	    u.estimator.add_systematics(TAUSF_SYS)
	    u.estimator.add_systematics(MUSF_SYS)
	    u.estimator.add_systematics(MUSF_STAT)
	    u.estimator.add_systematics(METSCALE)
	    u.estimator.add_systematics(PILEUP)
            u.estimator.add_systematics(fw_lowPT_1Track_80L1TAU60med)
            u.estimator.add_systematics(fw_highPT_1Track_80L1TAU60med)

	for u in addon_backgrounds_125med_1Track:
            #u.estimator.add_systematics(kW_125med_lowPT_Tau1Track)
	    u.estimator.add_systematics(RQCD_AntiIsoCR_125med_lowPT_Tau1Track) 
	    u.estimator.add_systematics(RQCD_AntiIsoCR_125med_highPT_Tau1Track) 
	    u.estimator.add_systematics(MUID)
	    u.estimator.add_systematics(MUMS)
	    u.estimator.add_systematics(MUSCALE)
	    u.estimator.add_systematics(TAUSF_SYS)
	    u.estimator.add_systematics(MUSF_SYS)
	    u.estimator.add_systematics(MUSF_STAT)
	    u.estimator.add_systematics(METSCALE)
	    u.estimator.add_systematics(PILEUP)
            u.estimator.add_systematics(fw_lowPT_1Track_125med)
            u.estimator.add_systematics(fw_highPT_1Track_125med)

	for u in addon_backgrounds_160med_1Track:
            #u.estimator.add_systematics(kW_160med_lowPT_Tau1Track)
	    u.estimator.add_systematics(RQCD_AntiIsoCR_160med_lowPT_Tau1Track) 
	    u.estimator.add_systematics(RQCD_AntiIsoCR_160med_highPT_Tau1Track) 
	    u.estimator.add_systematics(MUID)
	    u.estimator.add_systematics(MUMS)
	    u.estimator.add_systematics(MUSCALE)
	    u.estimator.add_systematics(TAUSF_SYS)
	    u.estimator.add_systematics(MUSF_SYS)
	    u.estimator.add_systematics(MUSF_STAT)
	    u.estimator.add_systematics(METSCALE)
	    u.estimator.add_systematics(PILEUP)
            u.estimator.add_systematics(fw_lowPT_1Track_160med)
            u.estimator.add_systematics(fw_highPT_1Track_160med)

if ptbinning_y_or_n == "y":

	# PT BINNING
	for s in addon_backgrounds_lowPT:
            s.estimator.add_systematics(kW_SS_lowPT)
            s.estimator.add_systematics(kW_OS_lowPT)
	    s.estimator.add_systematics(RQCD_AntiIsoCR_lowPT) 
	    s.estimator.add_systematics(MUID)
	    s.estimator.add_systematics(MUMS)
	    s.estimator.add_systematics(MUSCALE)
	    s.estimator.add_systematics(TAUSF_SYS)
	    s.estimator.add_systematics(MUSF_SYS)
	    s.estimator.add_systematics(MUSF_STAT)
	    s.estimator.add_systematics(METSCALE)
	    s.estimator.add_systematics(PILEUP)
            s.estimator.add_systematics(fw_lowPT_incl)
	    
	for t in addon_backgrounds_highPT:
            t.estimator.add_systematics(kW_SS_highPT)
            t.estimator.add_systematics(kW_OS_highPT)
	    t.estimator.add_systematics(RQCD_AntiIsoCR_highPT)  
	    t.estimator.add_systematics(MUID)
	    t.estimator.add_systematics(MUMS)
	    t.estimator.add_systematics(MUSCALE)
	    t.estimator.add_systematics(TAUSF_SYS)
	    t.estimator.add_systematics(MUSF_SYS)
	    t.estimator.add_systematics(MUSF_STAT)
	    t.estimator.add_systematics(METSCALE)
	    t.estimator.add_systematics(PILEUP)
            t.estimator.add_systematics(fw_highPT_incl)

	for u in addon_backgrounds_25med_lowPT:
            u.estimator.add_systematics(kW_OS_25med_lowPT)
            u.estimator.add_systematics(kW_SS_25med_lowPT)
	    u.estimator.add_systematics(RQCD_AntiIsoCR_25med_lowPT) 
	    u.estimator.add_systematics(MUID)
	    u.estimator.add_systematics(MUMS)
	    u.estimator.add_systematics(MUSCALE)
	    u.estimator.add_systematics(TAUSF_SYS)
	    u.estimator.add_systematics(MUSF_SYS)
	    u.estimator.add_systematics(MUSF_STAT)
	    u.estimator.add_systematics(METSCALE)
	    u.estimator.add_systematics(PILEUP)
	    u.estimator.add_systematics(fw_lowPT_25med)

	for v in addon_backgrounds_25med_highPT:
            v.estimator.add_systematics(kW_OS_25med_highPT)
            v.estimator.add_systematics(kW_SS_25med_highPT)
	    v.estimator.add_systematics(RQCD_AntiIsoCR_25med_highPT)
	    v.estimator.add_systematics(MUID)
	    v.estimator.add_systematics(MUMS)
	    v.estimator.add_systematics(MUSCALE)
	    v.estimator.add_systematics(TAUSF_SYS)
	    v.estimator.add_systematics(MUSF_SYS)
	    v.estimator.add_systematics(MUSF_STAT)
	    v.estimator.add_systematics(METSCALE)
	    v.estimator.add_systematics(PILEUP)
            v.estimator.add_systematics(fw_highPT_25med)
  		
	for u in addon_backgrounds_35med_lowPT:
#            u.estimator.add_systematics(kW_OS_35med_lowPT)
#            u.estimator.add_systematics(kW_SS_35med_lowPT)
	    u.estimator.add_systematics(RQCD_AntiIsoCR_35med_lowPT) 
	    u.estimator.add_systematics(MUID)
	    u.estimator.add_systematics(MUMS)
	    u.estimator.add_systematics(MUSCALE)
	    u.estimator.add_systematics(TAUSF_SYS)
	    u.estimator.add_systematics(MUSF_SYS)
	    u.estimator.add_systematics(MUSF_STAT)
	    u.estimator.add_systematics(METSCALE)
	    u.estimator.add_systematics(PILEUP)
	
	for v in addon_backgrounds_35med_highPT:
            #v.estimator.add_systematics(kW_35med_highPT)
	    v.estimator.add_systematics(RQCD_AntiIsoCR_35med_highPT)
	    v.estimator.add_systematics(MUID)
	    v.estimator.add_systematics(MUMS)
	    v.estimator.add_systematics(MUSCALE)
	    v.estimator.add_systematics(TAUSF_SYS)
	    v.estimator.add_systematics(MUSF_SYS)
	    v.estimator.add_systematics(MUSF_STAT)
	    v.estimator.add_systematics(METSCALE)
	    v.estimator.add_systematics(PILEUP)

	for u in addon_backgrounds_50L1TAU12med_lowPT:
            #u.estimator.add_systematics(kW_50L1TAU12med_lowPT)
	    u.estimator.add_systematics(RQCD_AntiIsoCR_50L1TAU12med_lowPT) 
	    u.estimator.add_systematics(MUID)
	    u.estimator.add_systematics(MUMS)
	    u.estimator.add_systematics(MUSCALE)
	    u.estimator.add_systematics(TAUSF_SYS)
	    u.estimator.add_systematics(MUSF_SYS)
	    u.estimator.add_systematics(MUSF_STAT)
	    u.estimator.add_systematics(METSCALE)
	    u.estimator.add_systematics(PILEUP)

	for v in addon_backgrounds_50L1TAU12med_highPT:
            #v.estimator.add_systematics(kW_50L1TAU12med_highPT)
	    v.estimator.add_systematics(RQCD_AntiIsoCR_50L1TAU12med_highPT)
	    v.estimator.add_systematics(MUID)
	    v.estimator.add_systematics(MUMS)
	    v.estimator.add_systematics(MUSCALE)
	    v.estimator.add_systematics(TAUSF_SYS)
	    v.estimator.add_systematics(MUSF_SYS)
	    v.estimator.add_systematics(MUSF_STAT)
	    v.estimator.add_systematics(METSCALE)
	    v.estimator.add_systematics(PILEUP)


	for u in addon_backgrounds_80med_lowPT:
            #u.estimator.add_systematics(kW_80med_lowPT)
	    u.estimator.add_systematics(RQCD_AntiIsoCR_80med_lowPT) 
	    u.estimator.add_systematics(MUID)
	    u.estimator.add_systematics(MUMS)
	    u.estimator.add_systematics(MUSCALE)
	    u.estimator.add_systematics(TAUSF_SYS)
	    u.estimator.add_systematics(MUSF_SYS)
	    u.estimator.add_systematics(MUSF_STAT)
	    u.estimator.add_systematics(METSCALE)
	    u.estimator.add_systematics(PILEUP)

	for v in addon_backgrounds_80med_highPT:
            #v.estimator.add_systematics(kW_80med_highPT)
	    v.estimator.add_systematics(RQCD_AntiIsoCR_80med_highPT)
	    v.estimator.add_systematics(MUID)
	    v.estimator.add_systematics(MUMS)
	    v.estimator.add_systematics(MUSCALE)
	    v.estimator.add_systematics(TAUSF_SYS)
	    v.estimator.add_systematics(MUSF_SYS)
	    v.estimator.add_systematics(MUSF_STAT)
	    v.estimator.add_systematics(METSCALE)
	    v.estimator.add_systematics(PILEUP)


	for u in addon_backgrounds_80L1TAU60med_lowPT:
            #u.estimator.add_systematics(kW_80L1TAU60med_lowPT)
	    u.estimator.add_systematics(RQCD_AntiIsoCR_80L1TAU60med_lowPT) 
	    u.estimator.add_systematics(MUID)
	    u.estimator.add_systematics(MUMS)
	    u.estimator.add_systematics(MUSCALE)
	    u.estimator.add_systematics(TAUSF_SYS)
	    u.estimator.add_systematics(MUSF_SYS)
	    u.estimator.add_systematics(MUSF_STAT)
	    u.estimator.add_systematics(METSCALE)
	    u.estimator.add_systematics(PILEUP)

	for v in addon_backgrounds_80L1TAU60med_highPT:
            #v.estimator.add_systematics(kW_80L1TAU60med_highPT)
	    v.estimator.add_systematics(RQCD_AntiIsoCR_80L1TAU60med_highPT)
	    v.estimator.add_systematics(MUID)
	    v.estimator.add_systematics(MUMS)
	    v.estimator.add_systematics(MUSCALE)
	    v.estimator.add_systematics(TAUSF_SYS)
	    v.estimator.add_systematics(MUSF_SYS)
	    v.estimator.add_systematics(MUSF_STAT)
	    v.estimator.add_systematics(METSCALE)
	    v.estimator.add_systematics(PILEUP)


	for u in addon_backgrounds_125med_lowPT:
            #u.estimator.add_systematics(kW_125med_lowPT)
	    u.estimator.add_systematics(RQCD_AntiIsoCR_125med_lowPT) 
	    u.estimator.add_systematics(MUID)
	    u.estimator.add_systematics(MUMS)
	    u.estimator.add_systematics(MUSCALE)
	    u.estimator.add_systematics(TAUSF_SYS)
	    u.estimator.add_systematics(MUSF_SYS)
	    u.estimator.add_systematics(MUSF_STAT)
	    u.estimator.add_systematics(METSCALE)
	    u.estimator.add_systematics(PILEUP)

	for v in addon_backgrounds_125med_highPT:
            #v.estimator.add_systematics(kW_125med_highPT)
	    v.estimator.add_systematics(RQCD_AntiIsoCR_125med_highPT)
	    v.estimator.add_systematics(MUID)
	    v.estimator.add_systematics(MUMS)
	    v.estimator.add_systematics(MUSCALE)
	    v.estimator.add_systematics(TAUSF_SYS)
	    v.estimator.add_systematics(MUSF_SYS)
	    v.estimator.add_systematics(MUSF_STAT)
	    v.estimator.add_systematics(METSCALE)
	    v.estimator.add_systematics(PILEUP)


	for u in addon_backgrounds_160med_lowPT:
            #u.estimator.add_systematics(kW_160med_lowPT)
	    u.estimator.add_systematics(RQCD_AntiIsoCR_160med_lowPT) 
	    u.estimator.add_systematics(MUID)
	    u.estimator.add_systematics(MUMS)
	    u.estimator.add_systematics(MUSCALE)
	    u.estimator.add_systematics(TAUSF_SYS)
	    u.estimator.add_systematics(MUSF_SYS)
	    u.estimator.add_systematics(MUSF_STAT)
	    u.estimator.add_systematics(METSCALE)
	    u.estimator.add_systematics(PILEUP)

	for v in addon_backgrounds_160med_highPT:
            #v.estimator.add_systematics(kW_160med_highPT)
	    v.estimator.add_systematics(RQCD_AntiIsoCR_160med_highPT)
	    v.estimator.add_systematics(MUID)
	    v.estimator.add_systematics(MUMS)
	    v.estimator.add_systematics(MUSCALE)
	    v.estimator.add_systematics(TAUSF_SYS)
	    v.estimator.add_systematics(MUSF_SYS)
	    v.estimator.add_systematics(MUSF_STAT)
	    v.estimator.add_systematics(METSCALE)
	    v.estimator.add_systematics(PILEUP)
		
	for u in addon_backgrounds_L1TAU12IMmed_lowPT:
            #u.estimator.add_systematics(kW_L1TAU12IMmed_lowPT)
	    u.estimator.add_systematics(RQCD_AntiIsoCR_L1TAU12IMmed_lowPT) 
	    u.estimator.add_systematics(MUID)
	    u.estimator.add_systematics(MUMS)
	    u.estimator.add_systematics(MUSCALE)
	    u.estimator.add_systematics(TAUSF_SYS)
	    u.estimator.add_systematics(MUSF_SYS)
	    u.estimator.add_systematics(MUSF_STAT)
	    u.estimator.add_systematics(METSCALE)
	    u.estimator.add_systematics(PILEUP)

	for v in addon_backgrounds_L1TAU12IMmed_highPT:
            #v.estimator.add_systematics(kW_L1TAU12IMmed_highPT)
	    v.estimator.add_systematics(RQCD_AntiIsoCR_L1TAU12IMmed_highPT)
	    v.estimator.add_systematics(MUID)
	    v.estimator.add_systematics(MUMS)
	    v.estimator.add_systematics(MUSCALE)
	    v.estimator.add_systematics(TAUSF_SYS)
	    v.estimator.add_systematics(MUSF_SYS)
	    v.estimator.add_systematics(MUSF_STAT)
	    v.estimator.add_systematics(METSCALE)
	    v.estimator.add_systematics(PILEUP)
		
	for s in addon_backgrounds_lowPT_1Track:
            s.estimator.add_systematics(kW_OS_lowPT_Tau1Track)
            s.estimator.add_systematics(kW_SS_lowPT_Tau1Track)
	    s.estimator.add_systematics(RQCD_AntiIsoCR_lowPT_Tau1Track) 
	    s.estimator.add_systematics(MUID)
	    s.estimator.add_systematics(MUMS)
	    s.estimator.add_systematics(MUSCALE)
	    s.estimator.add_systematics(TAUSF_SYS)
	    s.estimator.add_systematics(MUSF_SYS)
	    s.estimator.add_systematics(MUSF_STAT)
	    s.estimator.add_systematics(METSCALE)
	    s.estimator.add_systematics(PILEUP)
	    s.estimator.add_systematics(fw_lowPT_1Track)

	for t in addon_backgrounds_highPT_1Track:
            t.estimator.add_systematics(kW_OS_highPT_Tau1Track)
            t.estimator.add_systematics(kW_SS_highPT_Tau1Track)
	    t.estimator.add_systematics(RQCD_AntiIsoCR_highPT_Tau1Track)
	    t.estimator.add_systematics(MUID)
	    t.estimator.add_systematics(MUMS)
	    t.estimator.add_systematics(MUSCALE)
	    t.estimator.add_systematics(TAUSF_SYS)
	    t.estimator.add_systematics(MUSF_SYS)
	    t.estimator.add_systematics(MUSF_STAT)
	    t.estimator.add_systematics(METSCALE)
	    t.estimator.add_systematics(PILEUP)
	    t.estimator.add_systematics(fw_highPT_1Track)

	for u in addon_backgrounds_25med_lowPT_1Track:
            u.estimator.add_systematics(kW_OS_25med_lowPT_Tau1Track)
            u.estimator.add_systematics(kW_SS_25med_lowPT_Tau1Track)
	    u.estimator.add_systematics(RQCD_AntiIsoCR_25med_lowPT_Tau1Track) 
	    u.estimator.add_systematics(MUID)
	    u.estimator.add_systematics(MUMS)
	    u.estimator.add_systematics(MUSCALE)
	    u.estimator.add_systematics(TAUSF_SYS)
	    u.estimator.add_systematics(MUSF_SYS)
	    u.estimator.add_systematics(MUSF_STAT)
	    u.estimator.add_systematics(METSCALE)
	    u.estimator.add_systematics(PILEUP)
	    u.estimator.add_systematics(fw_lowPT_1Track_25med)

	for v in addon_backgrounds_25med_highPT_1Track:
            v.estimator.add_systematics(kW_OS_25med_highPT_Tau1Track)
            v.estimator.add_systematics(kW_SS_25med_highPT_Tau1Track)
	    v.estimator.add_systematics(RQCD_AntiIsoCR_25med_highPT_Tau1Track)
	    v.estimator.add_systematics(MUID)
	    v.estimator.add_systematics(MUMS)
	    v.estimator.add_systematics(MUSCALE)
	    v.estimator.add_systematics(TAUSF_SYS)
	    v.estimator.add_systematics(MUSF_SYS)
	    v.estimator.add_systematics(MUSF_STAT)
	    v.estimator.add_systematics(METSCALE)
	    v.estimator.add_systematics(PILEUP)
	    v.estimator.add_systematics(fw_highPT_1Track_25med)
	
	for u in addon_backgrounds_35med_lowPT_1Track:
            u.estimator.add_systematics(kW_OS_35med_lowPT_Tau1Track)
            u.estimator.add_systematics(kW_SS_35med_lowPT_Tau1Track)
	    u.estimator.add_systematics(RQCD_AntiIsoCR_35med_lowPT_Tau1Track) 
	    u.estimator.add_systematics(MUID)
	    u.estimator.add_systematics(MUMS)
	    u.estimator.add_systematics(MUSCALE)
	    u.estimator.add_systematics(TAUSF_SYS)
	    u.estimator.add_systematics(MUSF_SYS)
	    u.estimator.add_systematics(MUSF_STAT)
	    u.estimator.add_systematics(METSCALE)
	    u.estimator.add_systematics(PILEUP)
            u.estimator.add_systematics(fw_lowPT_1Track_35med)

	for v in addon_backgrounds_35med_highPT_1Track:
            v.estimator.add_systematics(kW_OS_35med_highPT_Tau1Track)
            v.estimator.add_systematics(kW_SS_35med_highPT_Tau1Track)
	    v.estimator.add_systematics(RQCD_AntiIsoCR_35med_highPT_Tau1Track)
	    v.estimator.add_systematics(MUID)
	    v.estimator.add_systematics(MUMS)
	    v.estimator.add_systematics(MUSCALE)
	    v.estimator.add_systematics(TAUSF_SYS)
	    v.estimator.add_systematics(MUSF_SYS)
	    v.estimator.add_systematics(MUSF_STAT)
	    v.estimator.add_systematics(METSCALE)
	    v.estimator.add_systematics(PILEUP)
            v.estimator.add_systematics(fw_highPT_1Track_35med)

	for u in addon_backgrounds_50L1TAU12med_lowPT_1Track:
            u.estimator.add_systematics(kW_OS_50L1TAU12med_lowPT_Tau1Track)
            u.estimator.add_systematics(kW_SS_50L1TAU12med_lowPT_Tau1Track)
	    u.estimator.add_systematics(RQCD_AntiIsoCR_50L1TAU12med_lowPT_Tau1Track) 
	    u.estimator.add_systematics(MUID)
	    u.estimator.add_systematics(MUMS)
	    u.estimator.add_systematics(MUSCALE)
	    u.estimator.add_systematics(TAUSF_SYS)
	    u.estimator.add_systematics(MUSF_SYS)
	    u.estimator.add_systematics(MUSF_STAT)
	    u.estimator.add_systematics(METSCALE)
	    u.estimator.add_systematics(PILEUP)
	    u.estimator.add_systematics(fw_lowPT_1Track_50L1TAU12med)

	for v in addon_backgrounds_50L1TAU12med_highPT_1Track:
            v.estimator.add_systematics(kW_OS_50L1TAU12med_highPT_Tau1Track)
            v.estimator.add_systematics(kW_SS_50L1TAU12med_highPT_Tau1Track)
	    v.estimator.add_systematics(RQCD_AntiIsoCR_50L1TAU12med_highPT_Tau1Track)
	    v.estimator.add_systematics(MUID)
	    v.estimator.add_systematics(MUMS)
	    v.estimator.add_systematics(MUSCALE)
	    v.estimator.add_systematics(TAUSF_SYS)
	    v.estimator.add_systematics(MUSF_SYS)
	    v.estimator.add_systematics(MUSF_STAT)
	    v.estimator.add_systematics(METSCALE)
	    v.estimator.add_systematics(PILEUP)
            v.estimator.add_systematics(fw_highPT_1Track_50L1TAU12med)


	for u in addon_backgrounds_80med_lowPT_1Track:
            u.estimator.add_systematics(kW_OS_80med_lowPT_Tau1Track)
            u.estimator.add_systematics(kW_SS_80med_lowPT_Tau1Track)
	    u.estimator.add_systematics(RQCD_AntiIsoCR_80med_lowPT_Tau1Track) 
	    u.estimator.add_systematics(MUID)
	    u.estimator.add_systematics(MUMS)
	    u.estimator.add_systematics(MUSCALE)
	    u.estimator.add_systematics(TAUSF_SYS)
	    u.estimator.add_systematics(MUSF_SYS)
	    u.estimator.add_systematics(MUSF_STAT)
	    u.estimator.add_systematics(METSCALE)
	    u.estimator.add_systematics(PILEUP)
            u.estimator.add_systematics(fw_lowPT_1Track_80med)

	for v in addon_backgrounds_80med_highPT_1Track:
            v.estimator.add_systematics(kW_OS_80med_highPT_Tau1Track)
            v.estimator.add_systematics(kW_SS_80med_highPT_Tau1Track)
	    v.estimator.add_systematics(RQCD_AntiIsoCR_80med_highPT_Tau1Track)
	    v.estimator.add_systematics(MUID)
	    v.estimator.add_systematics(MUMS)
	    v.estimator.add_systematics(MUSCALE)
	    v.estimator.add_systematics(TAUSF_SYS)
	    v.estimator.add_systematics(MUSF_SYS)
	    v.estimator.add_systematics(MUSF_STAT)
	    v.estimator.add_systematics(METSCALE)
	    v.estimator.add_systematics(PILEUP)
	    v.estimator.add_systematics(fw_highPT_1Track_80med)


	for u in addon_backgrounds_80L1TAU60med_lowPT_1Track:
            u.estimator.add_systematics(kW_OS_80L1TAU60med_lowPT_Tau1Track)
            u.estimator.add_systematics(kW_SS_80L1TAU60med_lowPT_Tau1Track)
	    u.estimator.add_systematics(RQCD_AntiIsoCR_80L1TAU60med_lowPT_Tau1Track) 
	    u.estimator.add_systematics(MUID)
	    u.estimator.add_systematics(MUMS)
	    u.estimator.add_systematics(MUSCALE)
	    u.estimator.add_systematics(TAUSF_SYS)
	    u.estimator.add_systematics(MUSF_SYS)
	    u.estimator.add_systematics(MUSF_STAT)
	    u.estimator.add_systematics(METSCALE)
	    u.estimator.add_systematics(PILEUP)
            u.estimator.add_systematics(fw_lowPT_1Track_80L1TAU60med)

	for v in addon_backgrounds_80L1TAU60med_highPT_1Track:
            v.estimator.add_systematics(kW_OS_80L1TAU60med_highPT_Tau1Track)
            v.estimator.add_systematics(kW_SS_80L1TAU60med_highPT_Tau1Track)
	    v.estimator.add_systematics(RQCD_AntiIsoCR_80L1TAU60med_highPT_Tau1Track)
	    v.estimator.add_systematics(MUID)
	    v.estimator.add_systematics(MUMS)
	    v.estimator.add_systematics(MUSCALE)
	    v.estimator.add_systematics(TAUSF_SYS)
	    v.estimator.add_systematics(MUSF_SYS)
	    v.estimator.add_systematics(MUSF_STAT)
	    v.estimator.add_systematics(METSCALE)
	    v.estimator.add_systematics(PILEUP)
	    v.estimator.add_systematics(fw_highPT_1Track_80L1TAU60med)

	for u in addon_backgrounds_125med_lowPT_1Track:
            u.estimator.add_systematics(kW_OS_125med_lowPT_Tau1Track)
            u.estimator.add_systematics(kW_SS_125med_lowPT_Tau1Track)
	    u.estimator.add_systematics(RQCD_AntiIsoCR_125med_lowPT_Tau1Track) 
	    u.estimator.add_systematics(MUID)
	    u.estimator.add_systematics(MUMS)
	    u.estimator.add_systematics(MUSCALE)
	    u.estimator.add_systematics(TAUSF_SYS)
	    u.estimator.add_systematics(MUSF_SYS)
	    u.estimator.add_systematics(MUSF_STAT)
	    u.estimator.add_systematics(METSCALE)
	    u.estimator.add_systematics(PILEUP)
            u.estimator.add_systematics(fw_lowPT_1Track_125med)

	for v in addon_backgrounds_125med_highPT_1Track:
            v.estimator.add_systematics(kW_OS_125med_highPT_Tau1Track)
            v.estimator.add_systematics(kW_SS_125med_highPT_Tau1Track)
	    v.estimator.add_systematics(RQCD_AntiIsoCR_125med_highPT_Tau1Track)
	    v.estimator.add_systematics(MUID)
	    v.estimator.add_systematics(MUMS)
	    v.estimator.add_systematics(MUSCALE)
	    v.estimator.add_systematics(TAUSF_SYS)
	    v.estimator.add_systematics(MUSF_SYS)
	    v.estimator.add_systematics(MUSF_STAT)
	    v.estimator.add_systematics(METSCALE)
	    v.estimator.add_systematics(PILEUP)
            v.estimator.add_systematics(fw_highPT_1Track_125med)

	for u in addon_backgrounds_160med_lowPT_1Track:
            u.estimator.add_systematics(kW_OS_160med_lowPT_Tau1Track)
            u.estimator.add_systematics(kW_SS_160med_lowPT_Tau1Track)
	    u.estimator.add_systematics(RQCD_AntiIsoCR_160med_lowPT_Tau1Track) 
	    u.estimator.add_systematics(MUID)
	    u.estimator.add_systematics(MUMS)
	    u.estimator.add_systematics(MUSCALE)
	    u.estimator.add_systematics(TAUSF_SYS)
	    u.estimator.add_systematics(MUSF_SYS)
	    u.estimator.add_systematics(MUSF_STAT)
	    u.estimator.add_systematics(METSCALE)
	    u.estimator.add_systematics(PILEUP)
            u.estimator.add_systematics(fw_lowPT_1Track_160med)

	for v in addon_backgrounds_160med_highPT_1Track:
            v.estimator.add_systematics(kW_OS_160med_highPT_Tau1Track)
            v.estimator.add_systematics(kW_SS_160med_highPT_Tau1Track)
	    v.estimator.add_systematics(RQCD_AntiIsoCR_160med_highPT_Tau1Track)
	    v.estimator.add_systematics(MUID)
	    v.estimator.add_systematics(MUMS)
	    v.estimator.add_systematics(MUSCALE)
	    v.estimator.add_systematics(TAUSF_SYS)
	    v.estimator.add_systematics(MUSF_SYS)
	    v.estimator.add_systematics(MUSF_STAT)
	    v.estimator.add_systematics(METSCALE)
	    v.estimator.add_systematics(PILEUP)
            v.estimator.add_systematics(fw_highPT_1Track_160med)
        	
	for u in addon_backgrounds_L1TAU12IMmed_lowPT_1Track:
            u.estimator.add_systematics(kW_OS_L1TAU12IMmed_lowPT_Tau1Track)
            u.estimator.add_systematics(kW_SS_L1TAU12IMmed_lowPT_Tau1Track)
	    u.estimator.add_systematics(RQCD_AntiIsoCR_L1TAU12IMmed_lowPT_Tau1Track) 
	    u.estimator.add_systematics(MUID)
	    u.estimator.add_systematics(MUMS)
	    u.estimator.add_systematics(MUSCALE)
	    u.estimator.add_systematics(TAUSF_SYS)
	    u.estimator.add_systematics(MUSF_SYS)
	    u.estimator.add_systematics(MUSF_STAT)
	    u.estimator.add_systematics(METSCALE)
	    u.estimator.add_systematics(PILEUP)
            u.estimator.add_systematics(fw_lowPT_1Track_L1TAU12IMmed)

	for v in addon_backgrounds_L1TAU12IMmed_highPT_1Track:
            v.estimator.add_systematics(kW_OS_L1TAU12IMmed_highPT_Tau1Track)
            v.estimator.add_systematics(kW_SS_L1TAU12IMmed_highPT_Tau1Track)
	    v.estimator.add_systematics(RQCD_AntiIsoCR_L1TAU12IMmed_highPT_Tau1Track)
	    v.estimator.add_systematics(MUID)
	    v.estimator.add_systematics(MUMS)
	    v.estimator.add_systematics(MUSCALE)
	    v.estimator.add_systematics(TAUSF_SYS)
	    v.estimator.add_systematics(MUSF_SYS)
	    v.estimator.add_systematics(MUSF_STAT)
	    v.estimator.add_systematics(METSCALE)
	    v.estimator.add_systematics(PILEUP)
            v.estimator.add_systematics(fw_highPT_1Track_L1TAU12IMmed)
	
	for u in addon_backgrounds_tracktwo_lowPT_1Track:
            u.estimator.add_systematics(kW_OS_tracktwo_lowPT_Tau1Track)
            u.estimator.add_systematics(kW_SS_tracktwo_lowPT_Tau1Track)
	    u.estimator.add_systematics(RQCD_AntiIsoCR_tracktwo_lowPT_Tau1Track) 
	    u.estimator.add_systematics(MUID)
	    u.estimator.add_systematics(MUMS)
	    u.estimator.add_systematics(MUSCALE)
	    u.estimator.add_systematics(TAUSF_SYS)
	    u.estimator.add_systematics(MUSF_SYS)
	    u.estimator.add_systematics(MUSF_STAT)
	    u.estimator.add_systematics(METSCALE)
	    u.estimator.add_systematics(PILEUP)
            u.estimator.add_systematics(fw_lowPT_1Track_tracktwo)

	for v in addon_backgrounds_tracktwo_highPT_1Track:
            v.estimator.add_systematics(kW_OS_tracktwo_highPT_Tau1Track)
            v.estimator.add_systematics(kW_SS_tracktwo_highPT_Tau1Track)
	    v.estimator.add_systematics(RQCD_AntiIsoCR_tracktwo_highPT_Tau1Track)
	    v.estimator.add_systematics(MUID)
	    v.estimator.add_systematics(MUMS)
	    v.estimator.add_systematics(MUSCALE)
	    v.estimator.add_systematics(TAUSF_SYS)
	    v.estimator.add_systematics(MUSF_SYS)
	    v.estimator.add_systematics(MUSF_STAT)
	    v.estimator.add_systematics(METSCALE)
	    v.estimator.add_systematics(PILEUP)
 	    u.estimator.add_systematics(fw_highPT_1Track_tracktwo)

	for u in addon_backgrounds_ptonly_lowPT_1Track:
            u.estimator.add_systematics(kW_OS_ptonly_lowPT_Tau1Track)
            u.estimator.add_systematics(kW_SS_ptonly_lowPT_Tau1Track)
	    u.estimator.add_systematics(RQCD_AntiIsoCR_ptonly_lowPT_Tau1Track) 
	    u.estimator.add_systematics(MUID)
	    u.estimator.add_systematics(MUMS)
	    u.estimator.add_systematics(MUSCALE)
	    u.estimator.add_systematics(TAUSF_SYS)
	    u.estimator.add_systematics(MUSF_SYS)
	    u.estimator.add_systematics(MUSF_STAT)
	    u.estimator.add_systematics(METSCALE)
	    u.estimator.add_systematics(PILEUP)
            u.estimator.add_systematics(fw_lowPT_1Track_ptonly)

	for v in addon_backgrounds_ptonly_highPT_1Track:
            v.estimator.add_systematics(kW_OS_ptonly_highPT_Tau1Track)
            v.estimator.add_systematics(kW_SS_ptonly_highPT_Tau1Track)
	    v.estimator.add_systematics(RQCD_AntiIsoCR_ptonly_highPT_Tau1Track)
	    v.estimator.add_systematics(MUID)
	    v.estimator.add_systematics(MUMS)
	    v.estimator.add_systematics(MUSCALE)
	    v.estimator.add_systematics(TAUSF_SYS)
	    v.estimator.add_systematics(MUSF_SYS)
	    v.estimator.add_systematics(MUSF_STAT)
	    v.estimator.add_systematics(METSCALE)
	    v.estimator.add_systematics(PILEUP)
 	    u.estimator.add_systematics(fw_highPT_1Track_ptonly)

	for s in addon_backgrounds_lowPT_3Track:
            s.estimator.add_systematics(kW_OS_lowPT_Tau3Track)
            s.estimator.add_systematics(kW_SS_lowPT_Tau3Track)
	    s.estimator.add_systematics(RQCD_AntiIsoCR_lowPT_Tau3Track) 
	    s.estimator.add_systematics(MUID)
	    s.estimator.add_systematics(MUMS)
	    s.estimator.add_systematics(MUSCALE)
	    s.estimator.add_systematics(TAUSF_SYS)
	    s.estimator.add_systematics(MUSF_SYS)
	    s.estimator.add_systematics(MUSF_STAT)
	    s.estimator.add_systematics(METSCALE)
	    s.estimator.add_systematics(PILEUP)
	    s.estimator.add_systematics(fw_lowPT_3Track)

	for t in addon_backgrounds_highPT_3Track:
            t.estimator.add_systematics(kW_OS_highPT_Tau3Track)
            t.estimator.add_systematics(kW_SS_highPT_Tau3Track)
	    t.estimator.add_systematics(RQCD_AntiIsoCR_highPT_Tau3Track)
	    t.estimator.add_systematics(MUID)
	    t.estimator.add_systematics(MUMS)
	    t.estimator.add_systematics(MUSCALE)
	    t.estimator.add_systematics(TAUSF_SYS)
	    t.estimator.add_systematics(MUSF_SYS)
	    t.estimator.add_systematics(MUSF_STAT)
	    t.estimator.add_systematics(METSCALE)
	    t.estimator.add_systematics(PILEUP)
	    t.estimator.add_systematics(fw_highPT_3Track)

	for u in addon_backgrounds_25med_lowPT_3Track:
            u.estimator.add_systematics(kW_OS_25med_lowPT_Tau3Track)
            u.estimator.add_systematics(kW_SS_25med_lowPT_Tau3Track)
	    u.estimator.add_systematics(RQCD_AntiIsoCR_25med_lowPT_Tau3Track) 
	    u.estimator.add_systematics(MUID)
	    u.estimator.add_systematics(MUMS)
	    u.estimator.add_systematics(MUSCALE)
	    u.estimator.add_systematics(TAUSF_SYS)
	    u.estimator.add_systematics(MUSF_SYS)
	    u.estimator.add_systematics(MUSF_STAT)
	    u.estimator.add_systematics(METSCALE)
	    u.estimator.add_systematics(PILEUP)
	    u.estimator.add_systematics(fw_lowPT_3Track_25med)

	for v in addon_backgrounds_25med_highPT_3Track:
            v.estimator.add_systematics(kW_OS_25med_highPT_Tau3Track)
            v.estimator.add_systematics(kW_SS_25med_highPT_Tau3Track)
	    v.estimator.add_systematics(RQCD_AntiIsoCR_25med_highPT_Tau3Track)
	    v.estimator.add_systematics(MUID)
	    v.estimator.add_systematics(MUMS)
	    v.estimator.add_systematics(MUSCALE)
	    v.estimator.add_systematics(TAUSF_SYS)
	    v.estimator.add_systematics(MUSF_SYS)
	    v.estimator.add_systematics(MUSF_STAT)
	    v.estimator.add_systematics(METSCALE)
	    v.estimator.add_systematics(PILEUP)
	    v.estimator.add_systematics(fw_highPT_3Track_25med)    
	
	for u in addon_backgrounds_35med_lowPT_3Track:
            u.estimator.add_systematics(kW_OS_35med_lowPT_Tau3Track)
            u.estimator.add_systematics(kW_SS_35med_lowPT_Tau3Track)
	    u.estimator.add_systematics(RQCD_AntiIsoCR_35med_lowPT_Tau3Track) 
	    u.estimator.add_systematics(MUID)
	    u.estimator.add_systematics(MUMS)
	    u.estimator.add_systematics(MUSCALE)
	    u.estimator.add_systematics(TAUSF_SYS)
	    u.estimator.add_systematics(MUSF_SYS)
	    u.estimator.add_systematics(MUSF_STAT)
	    u.estimator.add_systematics(METSCALE)
	    u.estimator.add_systematics(PILEUP)
            u.estimator.add_systematics(fw_lowPT_3Track_35med)

	for v in addon_backgrounds_35med_highPT_3Track:
            v.estimator.add_systematics(kW_OS_35med_highPT_Tau3Track)
            v.estimator.add_systematics(kW_SS_35med_highPT_Tau3Track)
	    v.estimator.add_systematics(RQCD_AntiIsoCR_35med_highPT_Tau3Track)
	    v.estimator.add_systematics(MUID)
	    v.estimator.add_systematics(MUMS)
	    v.estimator.add_systematics(MUSCALE)
	    v.estimator.add_systematics(TAUSF_SYS)
	    v.estimator.add_systematics(MUSF_SYS)
	    v.estimator.add_systematics(MUSF_STAT)
	    v.estimator.add_systematics(METSCALE)
	    v.estimator.add_systematics(PILEUP)
            v.estimator.add_systematics(fw_highPT_3Track_35med)
	
	for u in addon_backgrounds_50L1TAU12med_lowPT_3Track:
            u.estimator.add_systematics(kW_OS_50L1TAU12med_lowPT_Tau3Track)
            u.estimator.add_systematics(kW_SS_50L1TAU12med_lowPT_Tau3Track)
	    u.estimator.add_systematics(RQCD_AntiIsoCR_50L1TAU12med_lowPT_Tau3Track) 
	    u.estimator.add_systematics(MUID)
	    u.estimator.add_systematics(MUMS)
	    u.estimator.add_systematics(MUSCALE)
	    u.estimator.add_systematics(TAUSF_SYS)
	    u.estimator.add_systematics(MUSF_SYS)
	    u.estimator.add_systematics(MUSF_STAT)
	    u.estimator.add_systematics(METSCALE)
	    u.estimator.add_systematics(PILEUP)
            u.estimator.add_systematics(fw_lowPT_3Track_50L1TAU12med)

	for v in addon_backgrounds_50L1TAU12med_highPT_3Track:
            v.estimator.add_systematics(kW_OS_50L1TAU12med_highPT_Tau3Track)
            v.estimator.add_systematics(kW_SS_50L1TAU12med_highPT_Tau3Track)
	    v.estimator.add_systematics(RQCD_AntiIsoCR_50L1TAU12med_highPT_Tau3Track)
	    v.estimator.add_systematics(MUID)
	    v.estimator.add_systematics(MUMS)
	    v.estimator.add_systematics(MUSCALE)
	    v.estimator.add_systematics(TAUSF_SYS)
	    v.estimator.add_systematics(MUSF_SYS)
	    v.estimator.add_systematics(MUSF_STAT)
	    v.estimator.add_systematics(METSCALE)
	    v.estimator.add_systematics(PILEUP)
            v.estimator.add_systematics(fw_highPT_3Track_50L1TAU12med)


	for u in addon_backgrounds_80med_lowPT_3Track:
            u.estimator.add_systematics(kW_OS_80med_lowPT_Tau3Track)
            u.estimator.add_systematics(kW_SS_80med_lowPT_Tau3Track)
	    u.estimator.add_systematics(RQCD_AntiIsoCR_80med_lowPT_Tau3Track) 
	    u.estimator.add_systematics(MUID)
	    u.estimator.add_systematics(MUMS)
	    u.estimator.add_systematics(MUSCALE)
	    u.estimator.add_systematics(TAUSF_SYS)
	    u.estimator.add_systematics(MUSF_SYS)
	    u.estimator.add_systematics(MUSF_STAT)
	    u.estimator.add_systematics(METSCALE)
	    u.estimator.add_systematics(PILEUP)
            u.estimator.add_systematics(fw_lowPT_3Track_80med)

	for v in addon_backgrounds_80med_highPT_3Track:
            v.estimator.add_systematics(kW_OS_80med_highPT_Tau3Track)
            v.estimator.add_systematics(kW_SS_80med_highPT_Tau3Track)
	    v.estimator.add_systematics(RQCD_AntiIsoCR_80med_highPT_Tau3Track)
	    v.estimator.add_systematics(MUID)
	    v.estimator.add_systematics(MUMS)
	    v.estimator.add_systematics(MUSCALE)
	    v.estimator.add_systematics(TAUSF_SYS)
	    v.estimator.add_systematics(MUSF_SYS)
	    v.estimator.add_systematics(MUSF_STAT)
	    v.estimator.add_systematics(METSCALE)
	    v.estimator.add_systematics(PILEUP)
            v.estimator.add_systematics(fw_highPT_3Track_80med)

	for u in addon_backgrounds_80L1TAU60med_lowPT_3Track:
            u.estimator.add_systematics(kW_OS_80L1TAU60med_lowPT_Tau3Track)
            u.estimator.add_systematics(kW_SS_80L1TAU60med_lowPT_Tau3Track)
	    u.estimator.add_systematics(RQCD_AntiIsoCR_80L1TAU60med_lowPT_Tau3Track) 
	    u.estimator.add_systematics(MUID)
	    u.estimator.add_systematics(MUMS)
	    u.estimator.add_systematics(MUSCALE)
	    u.estimator.add_systematics(TAUSF_SYS)
	    u.estimator.add_systematics(MUSF_SYS)
	    u.estimator.add_systematics(MUSF_STAT)
	    u.estimator.add_systematics(METSCALE)
	    u.estimator.add_systematics(PILEUP)
            u.estimator.add_systematics(fw_lowPT_3Track_80L1TAU60med)

	for v in addon_backgrounds_80L1TAU60med_highPT_3Track:
            v.estimator.add_systematics(kW_OS_80L1TAU60med_highPT_Tau3Track)
            v.estimator.add_systematics(kW_SS_80L1TAU60med_highPT_Tau3Track)
	    v.estimator.add_systematics(RQCD_AntiIsoCR_80L1TAU60med_highPT_Tau3Track)
	    v.estimator.add_systematics(MUID)
	    v.estimator.add_systematics(MUMS)
	    v.estimator.add_systematics(MUSCALE)
	    v.estimator.add_systematics(TAUSF_SYS)
	    v.estimator.add_systematics(MUSF_SYS)
	    v.estimator.add_systematics(MUSF_STAT)
	    v.estimator.add_systematics(METSCALE)
	    v.estimator.add_systematics(PILEUP)
            v.estimator.add_systematics(fw_highPT_3Track_80L1TAU60med)

	for u in addon_backgrounds_125med_lowPT_3Track:
            u.estimator.add_systematics(kW_OS_125med_lowPT_Tau3Track)
            u.estimator.add_systematics(kW_SS_125med_lowPT_Tau3Track)
	    u.estimator.add_systematics(RQCD_AntiIsoCR_125med_lowPT_Tau3Track) 
	    u.estimator.add_systematics(MUID)
	    u.estimator.add_systematics(MUMS)
	    u.estimator.add_systematics(MUSCALE)
	    u.estimator.add_systematics(TAUSF_SYS)
	    u.estimator.add_systematics(MUSF_SYS)
	    u.estimator.add_systematics(MUSF_STAT)
	    u.estimator.add_systematics(METSCALE)
	    u.estimator.add_systematics(PILEUP)
            u.estimator.add_systematics(fw_lowPT_3Track_125med)

	for v in addon_backgrounds_125med_highPT_3Track:
            v.estimator.add_systematics(kW_OS_125med_highPT_Tau3Track)
            v.estimator.add_systematics(kW_SS_125med_highPT_Tau3Track)
	    v.estimator.add_systematics(RQCD_AntiIsoCR_125med_highPT_Tau3Track)
	    v.estimator.add_systematics(MUID)
	    v.estimator.add_systematics(MUMS)
	    v.estimator.add_systematics(MUSCALE)
	    v.estimator.add_systematics(TAUSF_SYS)
	    v.estimator.add_systematics(MUSF_SYS)
	    v.estimator.add_systematics(MUSF_STAT)
	    v.estimator.add_systematics(METSCALE)
	    v.estimator.add_systematics(PILEUP)
            v.estimator.add_systematics(fw_highPT_3Track_125med)

	for u in addon_backgrounds_160med_lowPT_3Track:
            u.estimator.add_systematics(kW_OS_160med_lowPT_Tau3Track)
            u.estimator.add_systematics(kW_SS_160med_lowPT_Tau3Track)
	    u.estimator.add_systematics(RQCD_AntiIsoCR_160med_lowPT_Tau3Track) 
	    u.estimator.add_systematics(MUID)
	    u.estimator.add_systematics(MUMS)
	    u.estimator.add_systematics(MUSCALE)
	    u.estimator.add_systematics(TAUSF_SYS)
	    u.estimator.add_systematics(MUSF_SYS)
	    u.estimator.add_systematics(MUSF_STAT)
	    u.estimator.add_systematics(METSCALE)
	    u.estimator.add_systematics(PILEUP)
            u.estimator.add_systematics(fw_lowPT_3Track_160med)

	for v in addon_backgrounds_160med_highPT_3Track:
            v.estimator.add_systematics(kW_OS_160med_highPT_Tau3Track)
            v.estimator.add_systematics(kW_SS_160med_highPT_Tau3Track)
	    v.estimator.add_systematics(RQCD_AntiIsoCR_160med_highPT_Tau3Track)
	    v.estimator.add_systematics(MUID)
	    v.estimator.add_systematics(MUMS)
	    v.estimator.add_systematics(MUSCALE)
	    v.estimator.add_systematics(TAUSF_SYS)
	    v.estimator.add_systematics(MUSF_SYS)
	    v.estimator.add_systematics(MUSF_STAT)
	    v.estimator.add_systematics(METSCALE)
	    v.estimator.add_systematics(PILEUP)
            v.estimator.add_systematics(fw_highPT_3Track_160med)	

	for u in addon_backgrounds_L1TAU12IMmed_lowPT_3Track:
            u.estimator.add_systematics(kW_OS_L1TAU12IMmed_lowPT_Tau3Track)
            u.estimator.add_systematics(kW_SS_L1TAU12IMmed_lowPT_Tau3Track)
	    u.estimator.add_systematics(RQCD_AntiIsoCR_L1TAU12IMmed_lowPT_Tau3Track) 
	    u.estimator.add_systematics(MUID)
	    u.estimator.add_systematics(MUMS)
	    u.estimator.add_systematics(MUSCALE)
	    u.estimator.add_systematics(TAUSF_SYS)
	    u.estimator.add_systematics(MUSF_SYS)
	    u.estimator.add_systematics(MUSF_STAT)
	    u.estimator.add_systematics(METSCALE)
	    u.estimator.add_systematics(PILEUP)
            u.estimator.add_systematics(fw_lowPT_3Track_L1TAU12IMmed)

	for v in addon_backgrounds_L1TAU12IMmed_highPT_3Track:
            v.estimator.add_systematics(kW_OS_L1TAU12IMmed_highPT_Tau3Track)
            v.estimator.add_systematics(kW_SS_L1TAU12IMmed_highPT_Tau3Track)
	    v.estimator.add_systematics(RQCD_AntiIsoCR_L1TAU12IMmed_highPT_Tau3Track)
	    v.estimator.add_systematics(MUID)
	    v.estimator.add_systematics(MUMS)
	    v.estimator.add_systematics(MUSCALE)
	    v.estimator.add_systematics(TAUSF_SYS)
	    v.estimator.add_systematics(MUSF_SYS)
	    v.estimator.add_systematics(MUSF_STAT)
	    v.estimator.add_systematics(METSCALE)
	    v.estimator.add_systematics(PILEUP)
            v.estimator.add_systematics(fw_highPT_3Track_L1TAU12IMmed)	

	for u in addon_backgrounds_tracktwo_lowPT_3Track:
            u.estimator.add_systematics(kW_OS_tracktwo_lowPT_Tau3Track)
            u.estimator.add_systematics(kW_SS_tracktwo_lowPT_Tau3Track)
	    u.estimator.add_systematics(RQCD_AntiIsoCR_tracktwo_lowPT_Tau3Track) 
	    u.estimator.add_systematics(MUID)
	    u.estimator.add_systematics(MUMS)
	    u.estimator.add_systematics(MUSCALE)
	    u.estimator.add_systematics(TAUSF_SYS)
	    u.estimator.add_systematics(MUSF_SYS)
	    u.estimator.add_systematics(MUSF_STAT)
	    u.estimator.add_systematics(METSCALE)
	    u.estimator.add_systematics(PILEUP)
            u.estimator.add_systematics(fw_lowPT_3Track_tracktwo)

	for v in addon_backgrounds_tracktwo_highPT_3Track:
            v.estimator.add_systematics(kW_OS_tracktwo_highPT_Tau3Track)
            v.estimator.add_systematics(kW_SS_tracktwo_highPT_Tau3Track)
	    v.estimator.add_systematics(RQCD_AntiIsoCR_tracktwo_highPT_Tau3Track)
	    v.estimator.add_systematics(MUID)
	    v.estimator.add_systematics(MUMS)
	    v.estimator.add_systematics(MUSCALE)
	    v.estimator.add_systematics(TAUSF_SYS)
	    v.estimator.add_systematics(MUSF_SYS)
	    v.estimator.add_systematics(MUSF_STAT)
	    v.estimator.add_systematics(METSCALE)
	    v.estimator.add_systematics(PILEUP)
            v.estimator.add_systematics(fw_highPT_3Track_tracktwo)	

	for u in addon_backgrounds_ptonly_lowPT_3Track:
            u.estimator.add_systematics(kW_OS_ptonly_lowPT_Tau3Track)
            u.estimator.add_systematics(kW_SS_ptonly_lowPT_Tau3Track)
	    u.estimator.add_systematics(RQCD_AntiIsoCR_ptonly_lowPT_Tau3Track) 
	    u.estimator.add_systematics(MUID)
	    u.estimator.add_systematics(MUMS)
	    u.estimator.add_systematics(MUSCALE)
	    u.estimator.add_systematics(TAUSF_SYS)
	    u.estimator.add_systematics(MUSF_SYS)
	    u.estimator.add_systematics(MUSF_STAT)
	    u.estimator.add_systematics(METSCALE)
	    u.estimator.add_systematics(PILEUP)
            u.estimator.add_systematics(fw_lowPT_3Track_ptonly)

	for v in addon_backgrounds_ptonly_highPT_3Track:
            v.estimator.add_systematics(kW_OS_ptonly_highPT_Tau3Track)
            v.estimator.add_systematics(kW_SS_ptonly_highPT_Tau3Track)
	    v.estimator.add_systematics(RQCD_AntiIsoCR_ptonly_highPT_Tau3Track)
	    v.estimator.add_systematics(MUID)
	    v.estimator.add_systematics(MUMS)
	    v.estimator.add_systematics(MUSCALE)
	    v.estimator.add_systematics(TAUSF_SYS)
	    v.estimator.add_systematics(MUSF_SYS)
	    v.estimator.add_systematics(MUSF_STAT)
	    v.estimator.add_systematics(METSCALE)
	    v.estimator.add_systematics(PILEUP)
            v.estimator.add_systematics(fw_highPT_3Track_ptonly)	

vdict  = vars.vars_dict

#-----------------
# Plotting 
#-----------------

# NB it does not make sense to plot fakes and addons on the same plot!
# NB when plotting same sign regions, you can only plot MC scaled by kfactor. ADDON is purely OS background!!

## backgrounds 
plot_backgrounds = []
plot_signals = []

if "SR" == options.region:  

	print "signal region"
	
	plot_backgrounds.append(addon_data)
	plot_backgrounds.append(addon_Wjets)
	plot_backgrounds.append(addon_Zlljets)
	plot_backgrounds.append(addon_top)

 	#plot_signals.append(samples.Wjets)
        
	plot_signals.append(samples.Zttjets)
        #plot_signals.append(sub_ztt) 

elif "SR_Tau1Track" == options.region:  

	print "signal region 1 prong"

	plot_backgrounds.append(addon_data_1Track)
	plot_backgrounds.append(addon_Wjets_1Track)
	plot_backgrounds.append(addon_Zlljets_1Track)
	plot_backgrounds.append(addon_top_1Track)
	
        plot_signals.append(samples.Zttjets)
        plot_signals.append(sub_ztt_1Track) 
	
elif "SR_25med_Tau1Track" == options.region:
 
	print "signal region _25med 1 prong"

	plot_backgrounds.append(addon_data_25med_1Track)
	plot_backgrounds.append(addon_Wjets_25med_1Track)
	plot_backgrounds.append(addon_Zlljets_25med_1Track)
	plot_backgrounds.append(addon_top_25med_1Track)

        plot_signals.append(samples.Zttjets)
        plot_signals.append(sub_ztt_25med_1Track)  

elif "SR_35med_Tau1Track" == options.region:
 
	print "signal region _35med 1 prong"

	plot_backgrounds.append(addon_data_35med_1Track)
	plot_backgrounds.append(addon_Wjets_35med_1Track)
	plot_backgrounds.append(addon_Zlljets_35med_1Track)
	plot_backgrounds.append(addon_top_35med_1Track)

        plot_signals.append(samples.Zttjets)
        plot_signals.append(sub_ztt_35med_1Track)  


elif "SR_50L1TAU12med_Tau1Track" == options.region:
 
	print "signal region _50L1TAU12med 1 prong"

	plot_backgrounds.append(addon_data_50L1TAU12med_1Track)
	plot_backgrounds.append(addon_Wjets_50L1TAU12med_1Track)
	plot_backgrounds.append(addon_Zlljets_50L1TAU12med_1Track)
	plot_backgrounds.append(addon_top_50L1TAU12med_1Track)

        plot_signals.append(samples.Zttjets)
        plot_signals.append(sub_ztt_50L1TAU12med_1Track)  

elif "SR_80med_Tau1Track" == options.region:
 
	print "signal region _80med 1 prong"

	plot_backgrounds.append(addon_data_80med_1Track)
	plot_backgrounds.append(addon_Wjets_80med_1Track)
	plot_backgrounds.append(addon_Zlljets_80med_1Track)
	plot_backgrounds.append(addon_top_80med_1Track)

        plot_signals.append(samples.Zttjets)
        plot_signals.append(sub_ztt_80med_1Track)  

elif "SR_80L1TAU60med_Tau1Track" == options.region:
 
	print "signal region _80L1TAU60med 1 prong"

	plot_backgrounds.append(addon_data_80L1TAU60med_1Track)
	plot_backgrounds.append(addon_Wjets_80L1TAU60med_1Track)
	plot_backgrounds.append(addon_Zlljets_80L1TAU60med_1Track)
	plot_backgrounds.append(addon_top_80L1TAU60med_1Track)

        plot_signals.append(samples.Zttjets)
        plot_signals.append(sub_ztt_80L1TAU60med_1Track)  

elif "SR_125med_Tau1Track" == options.region:
 
	print "signal region _125med 1 prong"

	plot_backgrounds.append(addon_data_125med_1Track)
	plot_backgrounds.append(addon_Wjets_125med_1Track)
	plot_backgrounds.append(addon_Zlljets_125med_1Track)
	plot_backgrounds.append(addon_top_125med_1Track)

        plot_signals.append(samples.Zttjets)
        plot_signals.append(sub_ztt_125med_1Track)  

elif "SR_160med_Tau1Track" == options.region:
 
	print "signal region _160med 1 prong"

	plot_backgrounds.append(addon_data_160med_1Track)
	plot_backgrounds.append(addon_Wjets_160med_1Track)
	plot_backgrounds.append(addon_Zlljets_160med_1Track)
	plot_backgrounds.append(addon_top_160med_1Track)

        plot_signals.append(samples.Zttjets)
        plot_signals.append(sub_ztt_160med_1Track)  

elif "SR_L1TAU12IMmed_Tau1Track" == options.region:
 
	print "signal region _L1TAU12IMmed 1 prong"

	plot_backgrounds.append(addon_data_L1TAU12IMmed_1Track)
	plot_backgrounds.append(addon_Wjets_L1TAU12IMmed_1Track)
	plot_backgrounds.append(addon_Zlljets_L1TAU12IMmed_1Track)
	plot_backgrounds.append(addon_top_L1TAU12IMmed_1Track)

        plot_signals.append(samples.Zttjets)
        plot_signals.append(sub_ztt_L1TAU12IMmed_1Track)  

elif "SR_ptonly_Tau1Track" == options.region:
 
	print "signal region _ptonly 1 prong"

	plot_backgrounds.append(addon_data_ptonly_1Track)
	plot_backgrounds.append(addon_Wjets_ptonly_1Track)
	plot_backgrounds.append(addon_Zlljets_ptonly_1Track)
	plot_backgrounds.append(addon_top_ptonly_1Track)

        plot_signals.append(samples.Zttjets)
        plot_signals.append(sub_ztt_ptonly_1Track)  

elif "SR_tracktwo_Tau1Track" == options.region:
 
	print "signal region _tracktwo 1 prong"

	plot_backgrounds.append(addon_data_tracktwo_1Track)
	plot_backgrounds.append(addon_Wjets_tracktwo_1Track)
	plot_backgrounds.append(addon_Zlljets_tracktwo_1Track)
	plot_backgrounds.append(addon_top_tracktwo_1Track)

        plot_signals.append(samples.Zttjets)
        plot_signals.append(sub_ztt_tracktwo_1Track)  

elif "SR_Tau3Track" == options.region:  

	print "signal region 3 prong"

	
	plot_backgrounds.append(addon_data_3Track)
	plot_backgrounds.append(addon_Wjets_3Track)
	plot_backgrounds.append(addon_Zlljets_3Track)
	plot_backgrounds.append(addon_top_3Track)

        plot_signals.append(samples.Zttjets)
        plot_signals.append(sub_ztt_3Track) 
	
elif "SR_25med_Tau3Track" == options.region:
 
	print "signal region _25med 3 prong"

	plot_backgrounds.append(addon_data_25med_3Track)
	plot_backgrounds.append(addon_Wjets_25med_3Track)
	plot_backgrounds.append(addon_Zlljets_25med_3Track)
	plot_backgrounds.append(addon_top_25med_3Track)

        plot_signals.append(samples.Zttjets)
        plot_signals.append(sub_ztt_25med_3Track)  
		
elif "SR_35med_Tau3Track" == options.region:
 
	print "signal region _35med 3 prong"

	plot_backgrounds.append(addon_data_35med_3Track)
	plot_backgrounds.append(addon_Wjets_35med_3Track)
	plot_backgrounds.append(addon_Zlljets_35med_3Track)
	plot_backgrounds.append(addon_top_35med_3Track)

        plot_signals.append(samples.Zttjets)
        plot_signals.append(sub_ztt_35med_3Track)  
	
elif "SR_50L1TAU12med_Tau3Track" == options.region:
 
	print "signal region _50L1TAU12med 3 prong"

	plot_backgrounds.append(addon_data_50L1TAU12med_3Track)
	plot_backgrounds.append(addon_Wjets_50L1TAU12med_3Track)
	plot_backgrounds.append(addon_Zlljets_50L1TAU12med_3Track)
	plot_backgrounds.append(addon_top_50L1TAU12med_3Track)

        plot_signals.append(samples.Zttjets)
        plot_signals.append(sub_ztt_50L1TAU12med_3Track)  

elif "SR_80med_Tau3Track" == options.region:
 
	print "signal region _80med 3 prong"

	plot_backgrounds.append(addon_data_80med_3Track)
	plot_backgrounds.append(addon_Wjets_80med_3Track)
	plot_backgrounds.append(addon_Zlljets_80med_3Track)
	plot_backgrounds.append(addon_top_80med_3Track)

        plot_signals.append(samples.Zttjets)
        plot_signals.append(sub_ztt_80med_3Track)  

elif "SR_80L1TAU60med_Tau3Track" == options.region:
 
	print "signal region _80L1TAU60med 3 prong"

	plot_backgrounds.append(addon_data_80L1TAU60med_3Track)
	plot_backgrounds.append(addon_Wjets_80L1TAU60med_3Track)
	plot_backgrounds.append(addon_Zlljets_80L1TAU60med_3Track)
	plot_backgrounds.append(addon_top_80L1TAU60med_3Track)

        plot_signals.append(samples.Zttjets)
        plot_signals.append(sub_ztt_80L1TAU60med_3Track)  

elif "SR_125med_Tau3Track" == options.region:
 
	print "signal region _125med 3 prong"

	plot_backgrounds.append(addon_data_125med_3Track)
	plot_backgrounds.append(addon_Wjets_125med_3Track)
	plot_backgrounds.append(addon_Zlljets_125med_3Track)
	plot_backgrounds.append(addon_top_125med_3Track)

        plot_signals.append(samples.Zttjets)
        plot_signals.append(sub_ztt_125med_3Track)  

elif "SR_ptonly_Tau3Track" == options.region:
 
	print "signal region _ptonly 3 prong"

	plot_backgrounds.append(addon_data_ptonly_3Track)
	plot_backgrounds.append(addon_Wjets_ptonly_3Track)
	plot_backgrounds.append(addon_Zlljets_ptonly_3Track)
	plot_backgrounds.append(addon_top_ptonly_3Track)

        plot_signals.append(samples.Zttjets)
        plot_signals.append(sub_ztt_ptonly_3Track)  

elif "SR_tracktwo_Tau3Track" == options.region:
 
	print "signal region _tracktwo 3 prong"

	plot_backgrounds.append(addon_data_tracktwo_3Track)
	plot_backgrounds.append(addon_Wjets_tracktwo_3Track)
	plot_backgrounds.append(addon_Zlljets_tracktwo_3Track)
	plot_backgrounds.append(addon_top_tracktwo_3Track)

        plot_signals.append(samples.Zttjets)
        plot_signals.append(sub_ztt_tracktwo_3Track)  


elif "SR_160med_Tau3Track" == options.region:
 
	print "signal region _160med 3 prong"

	plot_backgrounds.append(addon_data_160med_3Track)
	plot_backgrounds.append(addon_Wjets_160med_3Track)
	plot_backgrounds.append(addon_Zlljets_160med_3Track)
	plot_backgrounds.append(addon_top_160med_3Track)

        plot_signals.append(samples.Zttjets)
        plot_signals.append(sub_ztt_160med_3Track)  


elif "SR_L1TAU12IMmed_Tau3Track" == options.region:
 
	print "signal region _L1TAU12IMmed 3 prong"

	plot_backgrounds.append(addon_data_L1TAU12IMmed_3Track)
	plot_backgrounds.append(addon_Wjets_L1TAU12IMmed_3Track)
	plot_backgrounds.append(addon_Zlljets_L1TAU12IMmed_3Track)
	plot_backgrounds.append(addon_top_L1TAU12IMmed_3Track)

        plot_signals.append(samples.Zttjets)
        plot_signals.append(sub_ztt_L1TAU12IMmed_3Track)  


elif "SR_L1TAU12IMmed" == options.region:
 
	print "signal region _L1TAU12IMmed "

	plot_backgrounds.append(addon_data_L1TAU12IMmed)
	plot_backgrounds.append(addon_Wjets_L1TAU12IMmed)
	plot_backgrounds.append(addon_Zlljets_L1TAU12IMmed)
	plot_backgrounds.append(addon_top_L1TAU12IMmed)

        plot_signals.append(samples.Zttjets)
        #plot_signals.append(sub_ztt_L1TAU12IMmed)  

#------------ HIGH?LOW SCDP REGIONS------------------#

elif "SR_highSCDP_highMT" == options.region:
        
        #plot_backgrounds.append(addon_data_highSCDP_highMT)
        plot_backgrounds.append(addon_Wjets_highSCDP_highMT)
        plot_backgrounds.append(addon_Zlljets_highSCDP_highMT)
        plot_backgrounds.append(addon_top_highSCDP_highMT)
	
        #plot_backgrounds.append(samples.Wjets)
        #plot_backgrounds.append(samples.Zlljets)
        #plot_backgrounds.append(samples.top)

        plot_signals.append(samples.Zttjets)

elif "SR_lowSCDP_highMT"== options.region:
	
        #plot_backgrounds.append(addon_data_lowSCDP_highMT)
        plot_backgrounds.append(addon_Wjets_lowSCDP_highMT)
        plot_backgrounds.append(addon_Zlljets_lowSCDP_highMT)
        plot_backgrounds.append(addon_top_lowSCDP_highMT)
	
        #plot_backgrounds.append(samples.Wjets)
        #plot_backgrounds.append(samples.Zlljets)
        #plot_backgrounds.append(samples.top)

        plot_signals.append(samples.Zttjets)

elif "SR_highSCDP_highMT_SS" == options.region:

        #plot_backgrounds.append(addon_data_highSCDP_highMT)
        plot_backgrounds.append(addon_Wjets_highSCDP_highMT)
        plot_backgrounds.append(addon_Zlljets_highSCDP_highMT)
        plot_backgrounds.append(addon_top_highSCDP_highMT)

        #plot_backgrounds.append(samples.Wjets)
        #plot_backgrounds.append(samples.Zlljets)
        #plot_backgrounds.append(samples.top)

        plot_signals.append(samples.Zttjets)
        
elif "SR_lowSCDP_highMT_SS"== options.region:

        plot_backgrounds.append(addon_Wjets_lowSCDP_highMT)
        plot_backgrounds.append(addon_Zlljets_lowSCDP_highMT)
        plot_backgrounds.append(addon_top_lowSCDP_highMT)
        
        #plot_backgrounds.append(samples.Wjets)
        #plot_backgrounds.append(samples.Zlljets)
        #plot_backgrounds.append(samples.top)

        plot_signals.append(samples.Zttjets)

elif "SR_lowSCDP_lowMT" == options.region:
	
        #plot_backgrounds.append(addon_data_lowSCDP_lowMT)
        #plot_backgrounds.append(addon_Wjets_lowSCDP_lowMT)
        #plot_backgrounds.append(addon_Zlljets_lowSCDP_lowMT)
        #plot_backgrounds.append(addon_top_lowSCDP_lowMT)
	
        plot_backgrounds.append(samples.Wjets)
        #plot_backgrounds.append(samples.Zlljets)
        #plot_backgrounds.append(samples.top)
       
	#plot_signals.append(samples.Zttjets)
        #plot_signals.append(sub_ztt) 

elif "SR_lowSCDP_lowMT_SS" == options.region:

        #plot_backgrounds.append(addon_Wjets_lowSCDP_lowMT)
        #plot_backgrounds.append(addon_Zlljets_lowSCDP_lowMT)
        #plot_backgrounds.append(addon_top_lowSCDP_lowMT)

        #plot_backgrounds.append(samples.Wjets)
        #plot_backgrounds.append(samples.Zlljets)
        #plot_backgrounds.append(samples.top)

        plot_signals.append(samples.Wjets)
        #plot_signals.append(samples.Zttjets)
        #plot_signals.append(sub_ztt) 

elif "SR_SS_lowSCDP" == options.region:
        #plot_backgrounds.append(addon_Wjets)
        plot_signals.append(samples.Wjets)
        #plot_signals.append(samples.Zttjets)
        #plot_backgrounds.append(samples.Zlljets)
        #plot_backgrounds.append(samples.top)

elif "SR_highSCDP" == options.region:

	plot_signals.append(samples.Zttjets)
	plot_backgrounds.append(addon_data_highSCDP)
        plot_backgrounds.append(addon_Wjets_highSCDP)
        plot_backgrounds.append(addon_Zlljets_highSCDP)
        plot_backgrounds.append(addon_top_highSCDP)
        #plot_signals.append(samples.Wjets)
        #plot_backgrounds.append(samples.Zlljets)
        #plot_backgrounds.append(samples.top)

elif "SR_OS_no_cuts_for2D" == options.region:

	plot_backgrounds.append(samples.Wjets)

elif "SR_SS_no_cuts_2D" == options.region:

	plot_backgrounds.append(samples.Wjets)

elif "SR_lowSCDP" == options.region:

	#plot_signals.append(samples.Zttjets)
	#plot_backgrounds.append(addon_data_lowSCDP)
        #plot_backgrounds.append(addon_Wjets_lowSCDP)
        #plot_backgrounds.append(addon_Zlljets_lowSCDP)
        #plot_backgrounds.append(addon_top_lowSCDP)
        plot_signals.append(samples.Wjets)
        #plot_backgrounds.append(samples.Zlljets)
        #plot_backgrounds.append(samples.top)


elif "SR_lowSCDP_SS25med" == options.region:

	#plot_signals.append(samples.Zttjets)
	#plot_backgrounds.append(addon_data_lowSCDP)
        #plot_backgrounds.append(addon_Wjets_lowSCDP)
        #plot_backgrounds.append(addon_Zlljets_lowSCDP)
        #plot_backgrounds.append(addon_top_lowSCDP)
        plot_signals.append(samples.Wjets)
        #plot_backgrounds.append(samples.Zlljets)
        #plot_backgrounds.append(samples.top)


elif "SR_lowSCDP_25med" == options.region:

	#plot_signals.append(samples.Zttjets)
	#plot_backgrounds.append(addon_data_lowSCDP)
        #plot_backgrounds.append(addon_Wjets_lowSCDP)
        #plot_backgrounds.append(addon_Zlljets_lowSCDP)
        #plot_backgrounds.append(addon_top_lowSCDP)
        plot_signals.append(samples.Wjets)
        #plot_backgrounds.append(samples.Zlljets)
        #plot_backgrounds.append(samples.top)

#------------------------------------------------------#

elif "SR_SS" == options.region:

        print "signal region"

        plot_signals.append(samples.Wjets)
        #plot_signals.append(samples.Zttjets)

elif "SR_SS_Tau1Track" == options.region:
        plot_signals.append(samples.Wjets)

elif "SR_SS_Tau3Track" == options.region:
        plot_signals.append(samples.Wjets)


elif "AntiIsoCR_OS" == options.region:

        plot_signals.append(samples.Zttjets)
        plot_backgrounds.append(addon_data)
	plot_backgrounds.append(addon_Wjets)
        plot_backgrounds.append(addon_Zlljets)
        plot_backgrounds.append(addon_top)

elif "SR_OS_no_cuts_forvismass" == options.region:  

#	print "signal region"
        #plot_backgrounds.append(samples.Wjets)
        #plot_backgrounds.append(samples.Zlljets)
        #plot_backgrounds.append(samples.top)

	plot_backgrounds.append(addon_data_OS_no_cuts)
	plot_backgrounds.append(addon_Wjets_OS_no_cuts)
	plot_backgrounds.append(addon_Zlljets_OS_no_cuts)
	plot_backgrounds.append(addon_top_OS_no_cuts)

        plot_signals.append(samples.Zttjets)


elif "SR_25med" == options.region:
 
	print "signal region _25med"

	plot_backgrounds.append(addon_data_25med)
	plot_backgrounds.append(addon_Wjets_25med)
	plot_backgrounds.append(addon_Zlljets_25med)
	plot_backgrounds.append(addon_top_25med)

        plot_signals.append(samples.Zttjets)
        #plot_signals.append(sub_ztt_25med)  


	#plot_signals.append(samples.Wjets)

elif "SR_SS25med" == options.region:

        print "signal region _25med"

        #plot_backgrounds.append(addon_data_25med)
        #plot_backgrounds.append(addon_Wjets_25med)
        #plot_backgrounds.append(addon_Zlljets_25med)
        #plot_backgrounds.append(addon_top_25med)

        #plot_signals.append(samples.Zttjets)
        #plot_signals.append(sub_ztt_25med)  


        plot_signals.append(samples.Wjets)

elif "SR_35med" == options.region:
 
	print "signal region _35med"

	plot_backgrounds.append(addon_data_35med)
	plot_backgrounds.append(addon_Wjets_35med)
	plot_backgrounds.append(addon_Zlljets_35med)
	plot_backgrounds.append(addon_top_35med)

        plot_signals.append(samples.Zttjets)
        plot_signals.append(sub_ztt_35med)  

elif "SR_tracktwo" == options.region:
 

	plot_backgrounds.append(addon_data_tracktwo)
	plot_backgrounds.append(addon_Wjets_tracktwo)
	plot_backgrounds.append(addon_Zlljets_tracktwo)
	plot_backgrounds.append(addon_top_tracktwo)

        plot_signals.append(samples.Zttjets)

elif "SR_ptonly" == options.region:
 
	plot_backgrounds.append(addon_data_ptonly)
	plot_backgrounds.append(addon_Wjets_ptonly)
	plot_backgrounds.append(addon_Zlljets_ptonly)
	plot_backgrounds.append(addon_top_ptonly)

        plot_signals.append(samples.Zttjets)

elif "SR_50L1TAU12med" == options.region:

        print "signal region _50L1TAU12med "

        plot_backgrounds.append(addon_data_50L1TAU12med)
        plot_backgrounds.append(addon_Wjets_50L1TAU12med)
        plot_backgrounds.append(addon_Zlljets_50L1TAU12med)
        plot_backgrounds.append(addon_top_50L1TAU12med)

        plot_signals.append(samples.Zttjets)
        plot_signals.append(sub_ztt_50L1TAU12med)


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
    xmin2          = vdict[options.vname]['xmin2'],
    xmax2          = vdict[options.vname]['xmax2'],
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
        sys_dict    = sys_dict,
        outname     = plotsfile
        )	

## EOF



