# encoding: utf-8
'''
samples.py

description:

'''

#------------------------------------------------------------------------------
# All MC xsections can be found here:
# https://twiki.cern.ch/twiki/bin/viewauth/AtlasProtected/CentralMC15ProductionList
#------------------------------------------------------------------------------

## modules
from sample import Sample
import ROOT


## colors
black = ROOT.kBlack
white = ROOT.kWhite
red   = ROOT.kRed
green = ROOT.kGreen+1



#-------------------------------------------------------------------------------
# data
#-------------------------------------------------------------------------------
GRL = []


# ----- 2015 -----
"""
# v19 2015
GRL += ["276262", "276329",  "276330",  "276336",  "276416",  "276511",
	"276689", "276731",  "276778",  "276790",  "276952",  "276954",
	"278727", "278748",  "278880",  "278912",  "278968",  "278970",
	"279169", "279259",  "279279",  "279284",  "279345",  "279515",
	"279598", "279685",  "279764",  "279813",  "279867",  "279928",
	"279932", "279984",  "280231",  "280273",  "280319",  "280368",
	"280423", "280464",  "280500",  "280520",  "280614",  "280673",
	"280753", "280853",  "280862",  "280950",  "280977",  "281070",
	"281074", "281075",  "281130",  "281143",  "281317",  "281381",
	"281385", "281411",  "282625",  "282631",  "282712",  "282784",
	"282992", "283074",  "283155",  "283270",  "283429",  "283608",
	"283780", "284006",  "284154",  "284213",  "284285",  "284420",
	"284427", "284473",  "284484"]
"""
"""
# v25 2015
GRL += ["276262", "276329",  "276336",  "276416",  "276511",  "276689",
        "276778", "276790",  "276952",  "276954",  "278880",  "278912",
        "278968", "279169",  "279259",  "279279",  "279284",  "279345",
        "279515", "279598",  "279685",  "279813",  "279867",  "279928",
        "279932", "279984",  "280231",  "280273",  "280319",  "280368",
        "280423", "280464",  "280500",  "280520",  "280614",  "280673",
        "280753", "280853",  "280862",  "280950",  "280977",  "281070",
        "281074", "281075",  "281317",  "281385",  "281411",  "282625",
        "282631", "282712",  "282784",  "282992",  "283074",  "283155",
        "283270", "283429",  "283608",  "283780",  "284006",  "284154",
        "284213", "284285",  "284420",  "284427",  "284484"]

#---------- 2016 ---------
"""
GRL += ["297730", "298595",  "298609",  "298633",  "298687",  "298690",
        "298771", "298773",  "298862",  "298967",  "299055",  "299144",
        "299147", "299184",  "299243",  "299584",  "300279",  "300345",
        "300415", "300418",  "300487",  "300540",  "300571",  "300600",
        "300655", "300687",  "300784",  "300800",  "300863",  "300908",
        "301912", "301918",  "301932",  "301973",  "302053",  "302137",
        "302265", "302269",  "302300",  "302347",  "302380",  "302391",
        "302393", "302737",  "302831",  "302872",  "302919",  "302925",
        "302956", "303079",  "303201",  "303208",  "303264",  "303266",
        "303291", "303304",  "303338",  "303421",  "303499",  "303560",
        "303638", "303832",  "303846",  "303943",  "304006",  "304008",
        "304128", "304178",  "304198",  "304211",  "304243",  "304308",
        "304337", "304409",  "304431",  "304494",  "305380",  "305543",
        "305571", "305618",  "305671",  "305674",  "305723",  "305727",
        "305735", "305777",  "305811",  "305920",  "306269",  "306278",
        "306310", "306384",  "306419",  "306448",  "306451",  "307126",
        "307195", "307259",  "307306",  "307354",  "307358",  "307394",
        "307454", "307514",  "307539",  "307569",  "307601",  "307619",
        "307656", "307710",  "307732",  "307861",  "307935",  "308047",
        "308084", "309390",  "309440",  "309516",  "309640",  "309674",
        "309759", "310015",  "310247",  "310249",  "310341",  "310370",
        "310405", "310468",  "310473",  "310634",  "310691",  "310738",
        "310809", "310863",  "310872",  "310969",  "311071",  "311244",
        "311287", "311321",  "311365",  "311402",  "311473",  "311481",
        "303007", "307716",  "311170",  "303892","306442"]

ds_name = 'physics_Main_00%s'

for run in GRL:
    name = ds_name % run
    globals()[name] = Sample(
            name = name,
            type = "data"
            )

list_runs =[globals()[ds_name%(run)] for run in GRL]
"""
data = Sample(name         = "data",
              tlatex       = "Data 2015",
              fill_color   = white,
              fill_style   = 0,
              line_color   = black,
              line_style   = 1,
              marker_color = black,
              marker_style = 20,
              daughters    = list_runs,
              marker_color = black,
              marker_style = 20,
              daughters    = list_runs,
              )
"""
data = Sample(name         = "data",
              tlatex       = "Data",
              fill_color   = white,
              fill_style   = 0,
              line_color   = black,
              line_style   = 1,
              marker_color = black,
              marker_style = 20,
              daughters    = list_runs,
              )

#-----------------------------------------------------------------------------
# W + jets (Powheg+Pythia8)
# Notes:
#     * cross sections: https://twiki.cern.ch/twiki/bin/view/AtlasProtected/XsecSummaryWjetsPowPy8Incl
#-----------------------------------------------------------------------------

PoPy8_Wminusenu   = Sample( name =  "PoPy8_Wminusenu",    xsec = 8579.00109999)
PoPy8_Wminusmunu  = Sample( name =  "PoPy8_Wminusmunu",   xsec = 8579.00109999)
PoPy8_Wminustaunu = Sample( name =  "PoPy8_Wminustaunu",  xsec = 8579.00109999)
PoPy8_Wplusenu    = Sample( name =  "PoPy8_Wplusenu",     xsec = 11500.9154)
PoPy8_Wplusmunu   = Sample( name =  "PoPy8_Wplusmunu",    xsec = 11500.9154)
PoPy8_Wplustaunu  = Sample( name =  "PoPy8_Wplustaunu",   xsec = 11500.9154)

Wenujets = Sample( name =   'Wenujets',
                  tlatex = 'W #rightarrow e#nu+jets',
                  fill_color = ROOT.kCyan+1,
                  line_color =  ROOT.kCyan+2,
                  marker_color =  ROOT.kCyan+2,
                  daughters = [
                               PoPy8_Wminusenu,
			       PoPy8_Wplusenu,
                              ],
                )
Wmunujets = Sample( name =   'Wmunujets',
                  tlatex = 'W #rightarrow #mu #nu+jets',
                  fill_color = ROOT.kAzure+6,
                  line_color =  ROOT.kAzure+2,
                  marker_color =  ROOT.kAzure+2,
                  daughters = [
                               PoPy8_Wminusmunu,
                               PoPy8_Wplusmunu,
                              ],
                )
Wtaujets = Sample( name =   'Wtaujets',
                  tlatex = 'W #rightarrow #tau#nu+jets',
                  fill_color = ROOT.kGreen+1,
                  line_color =  ROOT.kGreen+2,
                  marker_color =  ROOT.kGreen+2,
                  daughters = [
                               PoPy8_Wminustaunu,
                               PoPy8_Wplustaunu,
                              ],
                )

# merge all W+jets samples
Wjets = Sample( name =   'Wjets',
                  tlatex = 'W #rightarrow #mu#nu+jets (OS-SS)',
                  fill_color = ROOT.kYellow-3,
                  line_color =  ROOT.kBlack,
                  marker_color =  ROOT.kYellow-3,
                  daughters = [Wenujets,
                               Wmunujets,
                               Wtaujets,
                              ],
                )



#-----------------------------------------------------------------------------
# Z + jets (Powheg+Pythia8)
# Notes:
#     * cross sections: https://twiki.cern.ch/twiki/bin/view/AtlasProtected/XsecSummaryZjetsPowPy8Incl
#-----------------------------------------------------------------------------

PoPy8_Zee   = Sample( name =  "PoPy8_Zee",    xsec = 1950.63210001)
PoPy8_Zmumu = Sample( name =  "PoPy8_Zmumu",  xsec = 1950.63210001)
PoPy8_Ztt   = Sample( name =  "PoPy8_Ztt",    xsec = 1950.63210001)
PoPy8_Ztt_truth   = Sample( name =  "PoPy8_Ztt_truth", type = "mcTruth",  xsec = 1950.63210001)
PoPy8_Ztt_antitruth   = Sample( name =  "PoPy8_Ztt_antitruth", type = "mcAntiTruth", xsec = 1950.63210001)

Zmumujets = Sample( name =   'Zmumujets',
                  tlatex = 'Z #rightarrow #mu#mu+jets',
                  fill_color = ROOT.kSpring-2,
                  line_color =  ROOT.kSpring-3,
                  marker_color =  ROOT.kSpring-3,
                  daughters = [
			       PoPy8_Zmumu,
                              ],
                )


Zeejets = Sample( name =   'Zeejets',
                  tlatex = 'Z #rightarrow ee+jets',
                  fill_color = ROOT.kBlue+1,
                  line_color =  ROOT.kBlue+2,
                  marker_color =  ROOT.kBlue+2,
                  daughters = [
                               PoPy8_Zee,
                              ],
                )

Zttjets = Sample( name =   'Zttjets',
                  tlatex = 'Z #rightarrow #tau#tau+jets',
                  fill_color = ROOT.kAzure+7,
                  line_color =  ROOT.kBlack,
                  marker_color =  ROOT.kAzure+7,
                  daughters = [
                               PoPy8_Ztt_truth,
                              ],
                )

# merge light leptons ones
Zlljets = Sample( name =   'Zlljets',
                  tlatex = 'Z #rightarrow #mu#mu+jets (OS-SS)',
                  fill_color = ROOT.kCyan+2,
                  line_color =  ROOT.kBlack,
                  marker_color =  ROOT.kCyan+2,
                  daughters = [
                               Zmumujets,
                               Zeejets,
                              ],
                )

#-----------------------------------------------------------------------------
# Top
# Notes:
#     * single-top cross section: https://twiki.cern.ch/twiki/bin/view/AtlasProtected/XsecSummarySingleTop
#     * ttbar cross section: https://twiki.cern.ch/twiki/bin/view/AtlasProtected/XsecSummaryTTbar
#-----------------------------------------------------------------------------


#-----------
# single-top
#-----------
PoPy_P2012_STSchan_noAllHad_atop = Sample( name =  "PoPy_P2012_STSchan_noAllHad_atop",   xsec = 1.2615) #susy
PoPy_P2012_STSchan_noAllHad_top  = Sample( name =  "PoPy_P2012_STSchan_noAllHad_top",    xsec = 2.0517) #susy
PoPy_P2012_st_tchan_lept_atop    = Sample( name =  "PoPy_P2012_st_tchan_lept_atop",      xsec = 25.778) #susy
PoPy_P2012_st_tchan_lept_top     = Sample( name =  "PoPy_P2012_st_tchan_lept_top",       xsec = 43.739) #susy
PoPy_P2012_Wt_incl_atop          = Sample( name =  "PoPy_P2012_Wt_incl_atop",            xsec = 33.989) #susy
PoPy_P2012_Wt_incl_top           = Sample( name =  "PoPy_P2012_Wt_incl_top",             xsec = 34.009) #susy

PoPy_P2012_STSchan_noAllHad_atop_truth = Sample( name =  "PoPy_P2012_STSchan_noAllHad_atop_truth", type = "mcTruth",  xsec = 1.2615) #susy
PoPy_P2012_STSchan_noAllHad_top_truth  = Sample( name =  "PoPy_P2012_STSchan_noAllHad_top_truth",  type = "mcTruth",  xsec = 2.0517) #susy
PoPy_P2012_st_tchan_lept_atop_truth    = Sample( name =  "PoPy_P2012_st_tchan_lept_atop_truth",    type = "mcTruth",  xsec = 25.778) #susy
PoPy_P2012_st_tchan_lept_top_truth     = Sample( name =  "PoPy_P2012_st_tchan_lept_top_truth",     type = "mcTruth",  xsec = 43.739) #susy
PoPy_P2012_Wt_incl_atop_truth          = Sample( name =  "PoPy_P2012_Wt_incl_atop_truth",          type = "mcTruth",  xsec = 33.989) #susy
PoPy_P2012_Wt_incl_top_truth           = Sample( name =  "PoPy_P2012_Wt_incl_top_truth",           type = "mcTruth",  xsec = 34.009) #susy

PoPy_P2012_STSchan_noAllHad_atop_antitruth = Sample( name =  "PoPy_P2012_STSchan_noAllHad_atop_antitruth", type = "mcAntiTruth",  xsec = 1.2615) #susy
PoPy_P2012_STSchan_noAllHad_top_antitruth  = Sample( name =  "PoPy_P2012_STSchan_noAllHad_top_antitruth",  type = "mcAntiTruth",  xsec = 2.0517) #susy
PoPy_P2012_st_tchan_lept_atop_antitruth    = Sample( name =  "PoPy_P2012_st_tchan_lept_atop_antitruth",    type = "mcAntiTruth",  xsec = 25.778) #susy
PoPy_P2012_st_tchan_lept_top_antitruth     = Sample( name =  "PoPy_P2012_st_tchan_lept_top_antitruth",     type = "mcAntiTruth",  xsec = 43.739) #susy
PoPy_P2012_Wt_incl_atop_antitruth          = Sample( name =  "PoPy_P2012_Wt_incl_atop_antitruth",          type = "mcAntiTruth",  xsec = 33.989) #susy
PoPy_P2012_Wt_incl_top_antitruth           = Sample( name =  "PoPy_P2012_Wt_incl_top_antitruth",           type = "mcAntiTruth",  xsec = 34.009) #susy

#-----------
# ttbar
#-----------
PoPy_P2012_ttb_nonallh           = Sample( name =  "PoPy_P2012_ttb_nonallh",             xsec = 696.11) #susy

PoPy_P2012_ttb_nonallh_truth           = Sample( name =  "PoPy_P2012_ttb_nonallh_truth",  type = "mcTruth",  xsec = 696.11) #susy

PoPy_P2012_ttb_nonallh_antitruth           = Sample( name =  "PoPy_P2012_ttb_nonallh_antitruth",  type = "mcAntiTruth",  xsec = 696.11) #susy

top = Sample( name =   'top',
              tlatex = 'Top (OS-SS)',
              fill_color = ROOT.kOrange+6,
              line_color =  ROOT.kBlack,
              marker_color =  ROOT.kOrange+6,
              daughters = [
                           PoPy_P2012_STSchan_noAllHad_atop,
                           PoPy_P2012_STSchan_noAllHad_top,
                           PoPy_P2012_st_tchan_lept_atop,
                           PoPy_P2012_st_tchan_lept_top,
                           PoPy_P2012_Wt_incl_atop,
                           PoPy_P2012_Wt_incl_top,
                           PoPy_P2012_ttb_nonallh,
                          ],
            )

#-------------------------------------------------------------------------------
# truth vs antitruth
#-------------------------------------------------------------------------------

Zttjets_truth = Sample( name =   'Zttjets_truth',
                  tlatex = 'Z #rightarrow #tau#tau+jets',
                  fill_color = ROOT.kAzure+7,
                  line_color =  ROOT.kBlack,
                  marker_color =  ROOT.kAzure+7,
		  type = "mcTruth",
                  daughters = [
                               PoPy8_Ztt_truth,
                              ],
                )

Zttjets_antitruth = Sample( name =   'Zttjets_antitruth',
                  tlatex = 'Z #rightarrow #tau#tau+jets',
                  fill_color = ROOT.kAzure+7,
                  line_color =  ROOT.kBlack,
                  marker_color =  ROOT.kAzure+7,
		  type = "mcAntiTruth",
                  daughters = [
                               PoPy8_Ztt_antitruth,
                              ],
                )


top_truth = Sample( name =   'top_truth',
              tlatex = 'Top',
              fill_color = ROOT.kOrange+6,
              line_color =  ROOT.kBlack,
              marker_color =  ROOT.kOrange+6,
	      type = "mcTruth",
              daughters = [
                           PoPy_P2012_STSchan_noAllHad_atop_truth,
                           PoPy_P2012_STSchan_noAllHad_top_truth,
                           PoPy_P2012_st_tchan_lept_atop_truth,
                           PoPy_P2012_st_tchan_lept_top_truth,
                           PoPy_P2012_Wt_incl_atop_truth,
                           PoPy_P2012_Wt_incl_top_truth,
                           PoPy_P2012_ttb_nonallh_truth,
                          ],
            )
top_antitruth = Sample( name =   'top_antitruth',
              tlatex = 'Top (OS-SS)',
              fill_color = ROOT.kOrange+6,
              line_color =  ROOT.kBlack,
	      type = "mcAntiTruth",
              marker_color =  ROOT.kOrange+6,
              daughters = [
                           PoPy_P2012_STSchan_noAllHad_atop_antitruth,
                           PoPy_P2012_STSchan_noAllHad_top_antitruth,
                           PoPy_P2012_st_tchan_lept_atop_antitruth,
                           PoPy_P2012_st_tchan_lept_top_antitruth,
                           PoPy_P2012_Wt_incl_atop_antitruth,
                           PoPy_P2012_Wt_incl_top_antitruth,
                           PoPy_P2012_ttb_nonallh_antitruth,
                          ],
            )




#-------------------------------------------------------------------------------
# data-driven backgrounds
#-------------------------------------------------------------------------------
addon_Zttjets_antitruth = Sample( name  = Zttjets_antitruth.name,
                 tlatex       = Zttjets_antitruth.tlatex,
                 fill_color   = Zttjets_antitruth.fill_color,
                 line_color   = Zttjets_antitruth.line_color,
                 marker_color = Zttjets_antitruth.marker_color,
                 )

addon_Zttjets_truth = Sample( name  = Zttjets_truth.name,
                 tlatex       = Zttjets_truth.tlatex,
                 fill_color   = Zttjets_truth.fill_color,
                 line_color   = Zttjets_truth.line_color,
                 marker_color = Zttjets_truth.marker_color,
                 )

addon_top_antitruth = Sample( name  = top_antitruth.name,
                 tlatex       = top_antitruth.tlatex,
                 fill_color   = top_antitruth.fill_color,
                 line_color   = top_antitruth.line_color,
                 marker_color = top_antitruth.marker_color,
                 )

addon_top_truth = Sample( name  = top_antitruth.name,
                 tlatex       = top_antitruth.tlatex,
                 fill_color   = top_antitruth.fill_color,
                 line_color   = top_antitruth.line_color,
                 marker_color = Zttjets.marker_color,
                 )

truth_taus = Sample(  name = 'truth_taus',
				tlatex = 'True #tau',
				fill_color = Zttjets.fill_color,
				line_color = ROOT.kBlack,
				marker_color = Zttjets.marker_color,
                                  )

all_fake_backgrounds = Sample(  name = 'all_fake_backgrounds',
				tlatex = 'Fakes',
				fill_color = ROOT.kAzure+6,
				line_color = ROOT.kBlack,
				marker_color = ROOT.kAzure+6,
				type = "datadriven",
				#daughters = [
        	                #             addon_Zlljets,
				#	     addon_top,
                               	#	     addon_Wjets,
				#	     addon_data,
				#	     ]
                                  )

fakes  = Sample( name         = "fakes",
                 tlatex       = "Fakes",
                 fill_color   = ROOT.kGreen+1,
                 line_color   = ROOT.kGreen+2,
                 marker_color = ROOT.kGreen+2,
                 type         = "datadriven",
                 )

sub_ztt = Sample( name 	      = "sub_ztt",
		 tlatex       = "Ztt (data - add ons)",
		 fill_color   = ROOT.kMagenta-7,
		 line_color   = ROOT.kBlack,
		 marker_color = ROOT.kMagenta-7,
		 type	      = "datadriven",
		 )

sub_ztt_1Track = Sample( name = "sub_ztt_1Track",
		 tlatex       = "Ztt (data - add ons)",
		 fill_color   = ROOT.kMagenta-7,
		 line_color   = ROOT.kBlack,
		 marker_color = ROOT.kMagenta-7,
		 type	      = "datadriven",
		 )

sub_ztt_3Track = Sample( name = "sub_ztt_3Track",
		 tlatex       = "Ztt (data - add ons)",
		 fill_color   = ROOT.kMagenta-7,
		 line_color   = ROOT.kBlack,
		 marker_color = ROOT.kMagenta-7,
		 type	      = "datadriven",
		 )

sub_ztt_25med = Sample( name 	      = "sub_ztt_25med",
		 tlatex       = "Ztt (data - add ons)",
		 fill_color   = ROOT.kMagenta-7,
		 line_color   = ROOT.kBlack,
		 marker_color = ROOT.kMagenta-7,
		 type	      = "datadriven",
		 )

sub_ztt_25med_1Track = Sample( name 	      = "sub_ztt_25med_1Track",
		 tlatex       = "Ztt (data - add ons)",
		 fill_color   = ROOT.kMagenta-7,
		 line_color   = ROOT.kBlack,
		 marker_color = ROOT.kMagenta-7,
		 type	      = "datadriven",
		 )

sub_ztt_25med_3Track = Sample( name 	      = "sub_ztt_25med_3Track",
		 tlatex       = "Ztt (data - add ons)",
		 fill_color   = ROOT.kMagenta-7,
		 line_color   = ROOT.kBlack,
		 marker_color = ROOT.kMagenta-7,
		 type	      = "datadriven",
		 )

sub_ztt_35med = Sample( name 	      = "sub_ztt_35med",
		 tlatex       = "Ztt (data - add ons)",
		 fill_color   = ROOT.kMagenta-7,
		 line_color   = ROOT.kBlack,
		 marker_color = ROOT.kMagenta-7,
		 type	      = "datadriven",
		 )

sub_ztt_35med_1Track = Sample( name 	      = "sub_ztt_35med_1Track",
		 tlatex       = "Ztt (data - add ons)",
		 fill_color   = ROOT.kMagenta-7,
		 line_color   = ROOT.kBlack,
		 marker_color = ROOT.kMagenta-7,
		 type	      = "datadriven",
		 )

sub_ztt_35med_3Track = Sample( name 	      = "sub_ztt_35med_3Track",
		 tlatex       = "Ztt (data - add ons)",
		 fill_color   = ROOT.kMagenta-7,
		 line_color   = ROOT.kBlack,
		 marker_color = ROOT.kMagenta-7,
		 type	      = "datadriven",
		 )


sub_ztt_50L1TAU12med = Sample( name 	      = "sub_ztt_50L1TAU12med",
		 tlatex       = "Ztt (data - add ons)",
		 fill_color   = ROOT.kMagenta-7,
		 line_color   = ROOT.kBlack,
		 marker_color = ROOT.kMagenta-7,
		 type	      = "datadriven",
		 )

sub_ztt_50L1TAU12med_1Track = Sample( name 	      = "sub_ztt_50L1TAU12med_1Track",
		 tlatex       = "Ztt (data - add ons)",
		 fill_color   = ROOT.kMagenta-7,
		 line_color   = ROOT.kBlack,
		 marker_color = ROOT.kMagenta-7,
		 type	      = "datadriven",
		 )

sub_ztt_50L1TAU12med_3Track = Sample( name 	      = "sub_ztt_50L1TAU12med_3Track",
		 tlatex       = "Ztt (data - add ons)",
		 fill_color   = ROOT.kMagenta-7,
		 line_color   = ROOT.kBlack,
		 marker_color = ROOT.kMagenta-7,
		 type	      = "datadriven",
		 )


sub_ztt_80med = Sample( name 	      = "sub_ztt_80med",
		 tlatex       = "Ztt (data - add ons)",
		 fill_color   = ROOT.kMagenta-7,
		 line_color   = ROOT.kBlack,
		 marker_color = ROOT.kMagenta-7,
		 type	      = "datadriven",
		 )

sub_ztt_80med_1Track = Sample( name 	      = "sub_ztt_80med_1Track",
		 tlatex       = "Ztt (data - add ons)",
		 fill_color   = ROOT.kMagenta-7,
		 line_color   = ROOT.kBlack,
		 marker_color = ROOT.kMagenta-7,
		 type	      = "datadriven",
		 )

sub_ztt_80med_3Track = Sample( name 	      = "sub_ztt_80med_3Track",
		 tlatex       = "Ztt (data - add ons)",
		 fill_color   = ROOT.kMagenta-7,
		 line_color   = ROOT.kBlack,
		 marker_color = ROOT.kMagenta-7,
		 type	      = "datadriven",
		 )


sub_ztt_80L1TAU60med = Sample( name 	      = "sub_ztt_80L1TAU60med",
		 tlatex       = "Ztt (data - add ons)",
		 fill_color   = ROOT.kMagenta-7,
		 line_color   = ROOT.kBlack,
		 marker_color = ROOT.kMagenta-7,
		 type	      = "datadriven",
		 )

sub_ztt_80L1TAU60med_1Track = Sample( name 	      = "sub_ztt_80L1TAU60med_1Track",
		 tlatex       = "Ztt (data - add ons)",
		 fill_color   = ROOT.kMagenta-7,
		 line_color   = ROOT.kBlack,
		 marker_color = ROOT.kMagenta-7,
		 type	      = "datadriven",
		 )

sub_ztt_80L1TAU60med_3Track = Sample( name 	      = "sub_ztt_80L1TAU60med_3Track",
		 tlatex       = "Ztt (data - add ons)",
		 fill_color   = ROOT.kMagenta-7,
		 line_color   = ROOT.kBlack,
		 marker_color = ROOT.kMagenta-7,
		 type	      = "datadriven",
		 )


sub_ztt_125med = Sample( name 	      = "sub_ztt_125med",
		 tlatex       = "Ztt (data - add ons)",
		 fill_color   = ROOT.kMagenta-7,
		 line_color   = ROOT.kBlack,
		 marker_color = ROOT.kMagenta-7,
		 type	      = "datadriven",
		 )

sub_ztt_125med_1Track = Sample( name 	      = "sub_ztt_125med_1Track",
		 tlatex       = "Ztt (data - add ons)",
		 fill_color   = ROOT.kMagenta-7,
		 line_color   = ROOT.kBlack,
		 marker_color = ROOT.kMagenta-7,
		 type	      = "datadriven",
		 )

sub_ztt_125med_3Track = Sample( name 	      = "sub_ztt_125med_3Track",
		 tlatex       = "Ztt (data - add ons)",
		 fill_color   = ROOT.kMagenta-7,
		 line_color   = ROOT.kBlack,
		 marker_color = ROOT.kMagenta-7,
		 type	      = "datadriven",
		 )


sub_ztt_160med = Sample( name 	      = "sub_ztt_160med",
		 tlatex       = "Ztt (data - add ons)",
		 fill_color   = ROOT.kMagenta-7,
		 line_color   = ROOT.kBlack,
		 marker_color = ROOT.kMagenta-7,
		 type	      = "datadriven",
		 )

sub_ztt_160med_1Track = Sample( name 	      = "sub_ztt_160med_1Track",
		 tlatex       = "Ztt (data - add ons)",
		 fill_color   = ROOT.kMagenta-7,
		 line_color   = ROOT.kBlack,
		 marker_color = ROOT.kMagenta-7,
		 type	      = "datadriven",
		 )

sub_ztt_160med_3Track = Sample( name 	      = "sub_ztt_160med_3Track",
		 tlatex       = "Ztt (data - add ons)",
		 fill_color   = ROOT.kMagenta-7,
		 line_color   = ROOT.kBlack,
		 marker_color = ROOT.kMagenta-7,
		 type	      = "datadriven",
		 )

sub_ztt_L1TAU12IMmed = Sample( name 	      = "sub_ztt_L1TAU12IMmed",
		 tlatex       = "Ztt (data - add ons)",
		 fill_color   = ROOT.kMagenta-7,
		 line_color   = ROOT.kBlack,
		 marker_color = ROOT.kMagenta-7,
		 type	      = "datadriven",
		 )

sub_ztt_L1TAU12IMmed_1Track = Sample( name 	      = "sub_ztt_L1TAU12IMmed_1Track",
		 tlatex       = "Ztt (data - add ons)",
		 fill_color   = ROOT.kMagenta-7,
		 line_color   = ROOT.kBlack,
		 marker_color = ROOT.kMagenta-7,
		 type	      = "datadriven",
		 )

sub_ztt_L1TAU12IMmed_3Track = Sample( name 	      = "sub_ztt_L1TAU12IMmed_3Track",
		 tlatex       = "Ztt (data - add ons)",
		 fill_color   = ROOT.kMagenta-7,
		 line_color   = ROOT.kBlack,
		 marker_color = ROOT.kMagenta-7,
		 type	      = "datadriven",
		 )

sub_ztt_ptonly = Sample( name 	      = "sub_ztt_ptonly",
		 tlatex       = "Ztt (data - add ons)",
		 fill_color   = ROOT.kMagenta-7,
		 line_color   = ROOT.kBlack,
		 marker_color = ROOT.kMagenta-7,
		 type	      = "datadriven",
		 )

sub_ztt_ptonly_1Track = Sample( name 	      = "sub_ztt_ptonly_1Track",
		 tlatex       = "Ztt (data - add ons)",
		 fill_color   = ROOT.kMagenta-7,
		 line_color   = ROOT.kBlack,
		 marker_color = ROOT.kMagenta-7,
		 type	      = "datadriven",
		 )

sub_ztt_ptonly_3Track = Sample( name 	      = "sub_ztt_ptonly_3Track",
		 tlatex       = "Ztt (data - add ons)",
		 fill_color   = ROOT.kMagenta-7,
		 line_color   = ROOT.kBlack,
		 marker_color = ROOT.kMagenta-7,
		 type	      = "datadriven",
		 )


sub_ztt_tracktwo = Sample( name 	      = "sub_ztt_tracktwo",
		 tlatex       = "Ztt (data - add ons)",
		 fill_color   = ROOT.kMagenta-7,
		 line_color   = ROOT.kBlack,
		 marker_color = ROOT.kMagenta-7,
		 type	      = "datadriven",
		 )

sub_ztt_tracktwo_1Track = Sample( name 	      = "sub_ztt_tracktwo_1Track",
		 tlatex       = "Ztt (data - add ons)",
		 fill_color   = ROOT.kMagenta-7,
		 line_color   = ROOT.kBlack,
		 marker_color = ROOT.kMagenta-7,
		 type	      = "datadriven",
		 )

sub_ztt_tracktwo_3Track = Sample( name 	      = "sub_ztt_tracktwo_3Track",
		 tlatex       = "Ztt (data - add ons)",
		 fill_color   = ROOT.kMagenta-7,
		 line_color   = ROOT.kBlack,
		 marker_color = ROOT.kMagenta-7,
		 type	      = "datadriven",
		 )

addon_data  = Sample( name   = "data",
                 tlatex       = "Same Sign",
                 fill_color   = ROOT.kRed-6,
                 line_color   = ROOT.kBlack,
                 marker_color = ROOT.kRed-6,
                 type         = "datadriven",
                 )

addon_Wjets = Sample( name   = Wjets.name,
                 tlatex       = Wjets.tlatex,
                 fill_color   = Wjets.fill_color,
                 line_color   = Wjets.line_color,
                 marker_color = Wjets.marker_color,
                 type         = "datadriven",
                 )

addon_Zlljets = Sample( name   = Zlljets.name,
                 tlatex       = Zlljets.tlatex,
                 fill_color   = Zlljets.fill_color,
                 line_color   = Zlljets.line_color,
                 marker_color = Zlljets.marker_color,
                 type         = "datadriven",
                 )

addon_Zttjets = Sample( name   = Zttjets.name,
                 tlatex       = Zttjets.tlatex,
                 fill_color   = Zttjets.fill_color,
                 line_color   = Zttjets.line_color,
                 marker_color = Zttjets.marker_color,
                 type         = "datadriven",
                 )

addon_top = Sample( name   = top.name,
                 tlatex       = top.tlatex,
                 fill_color   = top.fill_color,
                 line_color   = top.line_color,
                 marker_color = top.marker_color,
                 type         = "datadriven",
                 )

addon_data_OS_no_cuts  = Sample( name   = "data",
                 tlatex       = "Same Sign",
                 fill_color   = ROOT.kRed-6,
                 line_color   = ROOT.kBlack,
                 marker_color = ROOT.kRed-6,
                 type         = "datadriven",
                 )

addon_Wjets_OS_no_cuts = Sample( name   = Wjets.name,
                 tlatex       = Wjets.tlatex,
                 fill_color   = Wjets.fill_color,
                 line_color   = Wjets.line_color,
                 marker_color = Wjets.marker_color,
                 type         = "datadriven",
                 )

addon_Zlljets_OS_no_cuts = Sample( name   = Zlljets.name,
                 tlatex       = Zlljets.tlatex,
                 fill_color   = Zlljets.fill_color,
                 line_color   = Zlljets.line_color,
                 marker_color = Zlljets.marker_color,
                 type         = "datadriven",
                 )

addon_Zttjets_OS_no_cuts = Sample( name   = Zttjets.name,
                 tlatex       = Zttjets.tlatex,
                 fill_color   = Zttjets.fill_color,
                 line_color   = Zttjets.line_color,
                 marker_color = Zttjets.marker_color,
                 type         = "datadriven",
                 )

addon_top_OS_no_cuts = Sample( name   = top.name,
                 tlatex       = top.tlatex,
                 fill_color   = top.fill_color,
                 line_color   = top.line_color,
                 marker_color = top.marker_color,
                 type         = "datadriven",
                 )

addon_data_25med  = Sample( name   = "data",
                 tlatex       = "Same Sign",
                 fill_color   = ROOT.kRed-6,
                 line_color   = ROOT.kBlack,
                 marker_color = ROOT.kRed-6,
                 type         = "datadriven",
                 )

addon_Wjets_25med = Sample( name   = Wjets.name,
                 tlatex       = Wjets.tlatex,
                 fill_color   = Wjets.fill_color,
                 line_color   = Wjets.line_color,
                 marker_color = Wjets.marker_color,
                 type         = "datadriven",
                 )

addon_Zlljets_25med = Sample( name   = Zlljets.name,
                 tlatex       = Zlljets.tlatex,
                 fill_color   = Zlljets.fill_color,
                 line_color   = Zlljets.line_color,
                 marker_color = Zlljets.marker_color,
                 type         = "datadriven",
                 )

addon_Zttjets_25med = Sample( name   = Zttjets.name,
                 tlatex       = Zttjets.tlatex,
                 fill_color   = Zttjets.fill_color,
                 line_color   = Zttjets.line_color,
                 marker_color = Zttjets.marker_color,
                 type         = "datadriven",
                 )

addon_top_25med = Sample( name   = top.name,
                 tlatex       = top.tlatex,
                 fill_color   = top.fill_color,
                 line_color   = top.line_color,
                 marker_color = top.marker_color,
                 type         = "datadriven",
                 )

addon_data_25med_lowPT  = Sample( name   = "data",
                 tlatex       = "Same Sign",
                 fill_color   = ROOT.kRed-6,
                 line_color   = ROOT.kBlack,
                 marker_color = ROOT.kRed-6,
                 type         = "datadriven",
                 )

addon_Wjets_25med_lowPT = Sample( name   = Wjets.name,
                 tlatex       = Wjets.tlatex,
                 fill_color   = Wjets.fill_color,
                 line_color   = Wjets.line_color,
                 marker_color = Wjets.marker_color,
                 type         = "datadriven",
                 )

addon_Zlljets_25med_lowPT = Sample( name   = Zlljets.name,
                 tlatex       = Zlljets.tlatex,
                 fill_color   = Zlljets.fill_color,
                 line_color   = Zlljets.line_color,
                 marker_color = Zlljets.marker_color,
                 type         = "datadriven",
                 )

addon_Zttjets_25med_lowPT = Sample( name   = Zttjets.name,
                 tlatex       = Zttjets.tlatex,
                 fill_color   = Zttjets.fill_color,
                 line_color   = Zttjets.line_color,
                 marker_color = Zttjets.marker_color,
                 type         = "datadriven",
                 )

addon_top_25med_lowPT = Sample( name   = top.name,
                 tlatex       = top.tlatex,
                 fill_color   = top.fill_color,
                 line_color   = top.line_color,
                 marker_color = top.marker_color,
                 type         = "datadriven",
                 )

addon_data_25med_highPT  = Sample( name   = "data",
                 tlatex       = "Same Sign",
                 fill_color   = ROOT.kRed-6,
                 line_color   = ROOT.kBlack,
                 marker_color = ROOT.kRed-6,
                 type         = "datadriven",
                 )

addon_Wjets_25med_highPT = Sample( name   = Wjets.name,
                 tlatex       = Wjets.tlatex,
                 fill_color   = Wjets.fill_color,
                 line_color   = Wjets.line_color,
                 marker_color = Wjets.marker_color,
                 type         = "datadriven",
                 )

addon_Zlljets_25med_highPT = Sample( name   = Zlljets.name,
                 tlatex       = Zlljets.tlatex,
                 fill_color   = Zlljets.fill_color,
                 line_color   = Zlljets.line_color,
                 marker_color = Zlljets.marker_color,
                 type         = "datadriven",
                 )

addon_Zttjets_25med_highPT = Sample( name   = Zttjets.name,
                 tlatex       = Zttjets.tlatex,
                 fill_color   = Zttjets.fill_color,
                 line_color   = Zttjets.line_color,
                 marker_color = Zttjets.marker_color,
                 type         = "datadriven",
                 )

addon_top_25med_highPT = Sample( name   = top.name,
                 tlatex       = top.tlatex,
                 fill_color   = top.fill_color,
                 line_color   = top.line_color,
                 marker_color = top.marker_color,
                 type         = "datadriven",
                 )
########

addon_data_35med  = Sample( name   = "data",
                 tlatex       = "Same Sign",
                 fill_color   = ROOT.kRed-6,
                 line_color   = ROOT.kBlack,
                 marker_color = ROOT.kRed-6,
                 type         = "datadriven",
                 )

addon_Wjets_35med = Sample( name   = Wjets.name,
                 tlatex       = Wjets.tlatex,
                 fill_color   = Wjets.fill_color,
                 line_color   = Wjets.line_color,
                 marker_color = Wjets.marker_color,
                 type         = "datadriven",
                 )

addon_Zlljets_35med = Sample( name   = Zlljets.name,
                 tlatex       = Zlljets.tlatex,
                 fill_color   = Zlljets.fill_color,
                 line_color   = Zlljets.line_color,
                 marker_color = Zlljets.marker_color,
                 type         = "datadriven",
                 )

addon_Zttjets_35med = Sample( name   = Zttjets.name,
                 tlatex       = Zttjets.tlatex,
                 fill_color   = Zttjets.fill_color,
                 line_color   = Zttjets.line_color,
                 marker_color = Zttjets.marker_color,
                 type         = "datadriven",
                 )

addon_top_35med = Sample( name   = top.name,
                 tlatex       = top.tlatex,
                 fill_color   = top.fill_color,
                 line_color   = top.line_color,
                 marker_color = top.marker_color,
                 type         = "datadriven",
                 )

addon_data_35med_lowPT  = Sample( name   = "data",
                 tlatex       = "Same Sign",
                 fill_color   = ROOT.kRed-6,
                 line_color   = ROOT.kBlack,
                 marker_color = ROOT.kRed-6,
                 type         = "datadriven",
                 )

addon_Wjets_35med_lowPT = Sample( name   = Wjets.name,
                 tlatex       = Wjets.tlatex,
                 fill_color   = Wjets.fill_color,
                 line_color   = Wjets.line_color,
                 marker_color = Wjets.marker_color,
                 type         = "datadriven",
                 )

addon_Zlljets_35med_lowPT = Sample( name   = Zlljets.name,
                 tlatex       = Zlljets.tlatex,
                 fill_color   = Zlljets.fill_color,
                 line_color   = Zlljets.line_color,
                 marker_color = Zlljets.marker_color,
                 type         = "datadriven",
                 )

addon_Zttjets_35med_lowPT = Sample( name   = Zttjets.name,
                 tlatex       = Zttjets.tlatex,
                 fill_color   = Zttjets.fill_color,
                 line_color   = Zttjets.line_color,
                 marker_color = Zttjets.marker_color,
                 type         = "datadriven",
                 )

addon_top_35med_lowPT = Sample( name   = top.name,
                 tlatex       = top.tlatex,
                 fill_color   = top.fill_color,
                 line_color   = top.line_color,
                 marker_color = top.marker_color,
                 type         = "datadriven",
                 )

addon_data_35med_highPT  = Sample( name   = "data",
                 tlatex       = "Same Sign",
                 fill_color   = ROOT.kRed-6,
                 line_color   = ROOT.kBlack,
                 marker_color = ROOT.kRed-6,
                 type         = "datadriven",
                 )

addon_Wjets_35med_highPT = Sample( name   = Wjets.name,
                 tlatex       = Wjets.tlatex,
                 fill_color   = Wjets.fill_color,
                 line_color   = Wjets.line_color,
                 marker_color = Wjets.marker_color,
                 type         = "datadriven",
                 )

addon_Zlljets_35med_highPT = Sample( name   = Zlljets.name,
                 tlatex       = Zlljets.tlatex,
                 fill_color   = Zlljets.fill_color,
                 line_color   = Zlljets.line_color,
                 marker_color = Zlljets.marker_color,
                 type         = "datadriven",
                 )

addon_Zttjets_35med_highPT = Sample( name   = Zttjets.name,
                 tlatex       = Zttjets.tlatex,
                 fill_color   = Zttjets.fill_color,
                 line_color   = Zttjets.line_color,
                 marker_color = Zttjets.marker_color,
                 type         = "datadriven",
                 )

addon_top_35med_highPT = Sample( name   = top.name,
                 tlatex       = top.tlatex,
                 fill_color   = top.fill_color,
                 line_color   = top.line_color,
                 marker_color = top.marker_color,
                 type         = "datadriven",
                 )

##########

addon_data_lowPT  = Sample( name   = "data",
                 tlatex       = "Same Sign_lowPT",
                 fill_color   = ROOT.kRed-6,
                 line_color   = ROOT.kBlack,
                 marker_color = ROOT.kRed-6,
                 type         = "datadriven",
                 )

addon_Wjets_lowPT = Sample( name   = Wjets.name,
                 tlatex       = Wjets.tlatex+"(OS-SS)_lowPT",
                 fill_color   = Wjets.fill_color,
                 line_color   = Wjets.line_color,
                 marker_color = Wjets.marker_color,
                 type         = "datadriven",
                 )

addon_Zlljets_lowPT = Sample( name   = Zlljets.name,
                 tlatex       = Zlljets.tlatex+"(OS-SS)_lowPT",
                 fill_color   = Zlljets.fill_color,
                 line_color   = Zlljets.line_color,
                 marker_color = Zlljets.marker_color,
                 type         = "datadriven",
                 )

addon_Zttjets_lowPT = Sample( name   = Zttjets.name,
                 tlatex       = Zttjets.tlatex+"(OS-SS)_lowPT",
                 fill_color   = Zttjets.fill_color,
                 line_color   = Zttjets.line_color,
                 marker_color = Zttjets.marker_color,
                 type         = "datadriven",
                 )

addon_top_lowPT = Sample( name   = top.name,
                 tlatex       = top.tlatex+"(OS-SS)_lowPT",
                 fill_color   = top.fill_color,
                 line_color   = top.line_color,
                 marker_color = top.marker_color,
                 type         = "datadriven",
                 )

addon_data_highPT  = Sample( name   = "data",
                 tlatex       = "Same Sign_highPT",
                 fill_color   = ROOT.kRed-6,
                 line_color   = ROOT.kBlack,
                 marker_color = ROOT.kRed-6,
                 type         = "datadriven",
                 )

addon_Wjets_highPT = Sample( name   = Wjets.name,
                 tlatex       = Wjets.tlatex+"(OS-SS)_highPT",
                 fill_color   = Wjets.fill_color,
                 line_color   = Wjets.line_color,
                 marker_color = Wjets.marker_color,
                 type         = "datadriven",
                 )

addon_Zlljets_highPT = Sample( name   = Zlljets.name,
                 tlatex       = Zlljets.tlatex+"(OS-SS)_highPT",
                 fill_color   = Zlljets.fill_color,
                 line_color   = Zlljets.line_color,
                 marker_color = Zlljets.marker_color,
                 type         = "datadriven",
                 )

addon_Zttjets_highPT = Sample( name   = Zttjets.name,
                 tlatex       = Zttjets.tlatex+"(OS-SS)_highPT",
                 fill_color   = Zttjets.fill_color,
                 line_color   = Zttjets.line_color,
                 marker_color = Zttjets.marker_color,
                 type         = "datadriven",
                 )

addon_top_highPT = Sample( name   = top.name,
                 tlatex       = top.tlatex+"(OS-SS)_highPT",
                 fill_color   = top.fill_color,
                 line_color   = top.line_color,
                 marker_color = top.marker_color,
                 type         = "datadriven",
                 )


#------------------------
# 	one track
#------------------------

addon_data_1Track  = Sample( name   = "data",
                 tlatex       = "Same Sign",
                 fill_color   = ROOT.kRed-6,
                 line_color   = ROOT.kBlack,
                 marker_color = ROOT.kRed-6,
                 type         = "datadriven",
                 )

addon_Wjets_1Track = Sample( name   = Wjets.name,
                 tlatex       = Wjets.tlatex,
                 fill_color   = Wjets.fill_color,
                 line_color   = Wjets.line_color,
                 marker_color = Wjets.marker_color,
                 type         = "datadriven",
                 )

addon_Zlljets_1Track = Sample( name   = Zlljets.name,
                 tlatex       = Zlljets.tlatex,
                 fill_color   = Zlljets.fill_color,
                 line_color   = Zlljets.line_color,
                 marker_color = Zlljets.marker_color,
                 type         = "datadriven",
                 )

addon_Zttjets_1Track = Sample( name   = Zttjets.name,
                 tlatex       = Zttjets.tlatex,
                 fill_color   = Zttjets.fill_color,
                 line_color   = Zttjets.line_color,
                 marker_color = Zttjets.marker_color,
                 type         = "datadriven",
                 )

addon_top_1Track = Sample( name   = top.name,
                 tlatex       = top.tlatex,
                 fill_color   = top.fill_color,
                 line_color   = top.line_color,
                 marker_color = top.marker_color,
                 type         = "datadriven",
                 )

#############

addon_data_25med_1Track  = Sample( name   = "data",
                 tlatex       = "Same Sign",
                 fill_color   = ROOT.kRed-6,
                 line_color   = ROOT.kBlack,
                 marker_color = ROOT.kRed-6,
                 type         = "datadriven",
                 )

addon_Wjets_25med_1Track = Sample( name   = Wjets.name,
                 tlatex       = Wjets.tlatex,
                 fill_color   = Wjets.fill_color,
                 line_color   = Wjets.line_color,
                 marker_color = Wjets.marker_color,
                 type         = "datadriven",
                 )

addon_Zlljets_25med_1Track = Sample( name   = Zlljets.name,
                 tlatex       = Zlljets.tlatex,
                 fill_color   = Zlljets.fill_color,
                 line_color   = Zlljets.line_color,
                 marker_color = Zlljets.marker_color,
                 type         = "datadriven",
                 )

addon_Zttjets_25med_1Track = Sample( name   = Zttjets.name,
                 tlatex       = Zttjets.tlatex,
                 fill_color   = Zttjets.fill_color,
                 line_color   = Zttjets.line_color,
                 marker_color = Zttjets.marker_color,
                 type         = "datadriven",
                 )

addon_top_25med_1Track = Sample( name   = top.name,
                 tlatex       = top.tlatex,
                 fill_color   = top.fill_color,
                 line_color   = top.line_color,
                 marker_color = top.marker_color,
                 type         = "datadriven",
                 )

addon_data_25med_lowPT_1Track  = Sample( name   = "data",
                 tlatex       = "Same Sign",
                 fill_color   = ROOT.kRed-6,
                 line_color   = ROOT.kBlack,
                 marker_color = ROOT.kRed-6,
                 type         = "datadriven",
                 )

addon_Wjets_25med_lowPT_1Track = Sample( name   = Wjets.name,
                 tlatex       = Wjets.tlatex,
                 fill_color   = Wjets.fill_color,
                 line_color   = Wjets.line_color,
                 marker_color = Wjets.marker_color,
                 type         = "datadriven",
                 )

addon_Zlljets_25med_lowPT_1Track = Sample( name   = Zlljets.name,
                 tlatex       = Zlljets.tlatex,
                 fill_color   = Zlljets.fill_color,
                 line_color   = Zlljets.line_color,
                 marker_color = Zlljets.marker_color,
                 type         = "datadriven",
                 )

addon_Zttjets_25med_lowPT_1Track = Sample( name   = Zttjets.name,
                 tlatex       = Zttjets.tlatex,
                 fill_color   = Zttjets.fill_color,
                 line_color   = Zttjets.line_color,
                 marker_color = Zttjets.marker_color,
                 type         = "datadriven",
                 )

addon_top_25med_lowPT_1Track = Sample( name   = top.name,
                 tlatex       = top.tlatex,
                 fill_color   = top.fill_color,
                 line_color   = top.line_color,
                 marker_color = top.marker_color,
                 type         = "datadriven",
                 )

addon_data_25med_highPT_1Track  = Sample( name   = "data",
                 tlatex       = "Same Sign",
                 fill_color   = ROOT.kRed-6,
                 line_color   = ROOT.kBlack,
                 marker_color = ROOT.kRed-6,
                 type         = "datadriven",
                 )

addon_Wjets_25med_highPT_1Track = Sample( name   = Wjets.name,
                 tlatex       = Wjets.tlatex,
                 fill_color   = Wjets.fill_color,
                 line_color   = Wjets.line_color,
                 marker_color = Wjets.marker_color,
                 type         = "datadriven",
                 )

addon_Zlljets_25med_highPT_1Track = Sample( name   = Zlljets.name,
                 tlatex       = Zlljets.tlatex,
                 fill_color   = Zlljets.fill_color,
                 line_color   = Zlljets.line_color,
                 marker_color = Zlljets.marker_color,
                 type         = "datadriven",
                 )

addon_Zttjets_25med_highPT_1Track = Sample( name   = Zttjets.name,
                 tlatex       = Zttjets.tlatex,
                 fill_color   = Zttjets.fill_color,
                 line_color   = Zttjets.line_color,
                 marker_color = Zttjets.marker_color,
                 type         = "datadriven",
                 )

addon_top_25med_highPT_1Track = Sample( name   = top.name,
                 tlatex       = top.tlatex,
                 fill_color   = top.fill_color,
                 line_color   = top.line_color,
                 marker_color = top.marker_color,
                 type         = "datadriven",
                 )
#############

addon_data_35med_1Track  = Sample( name   = "data",
                 tlatex       = "Same Sign",
                 fill_color   = ROOT.kRed-6,
                 line_color   = ROOT.kBlack,
                 marker_color = ROOT.kRed-6,
                 type         = "datadriven",
                 )

addon_Wjets_35med_1Track = Sample( name   = Wjets.name,
                 tlatex       = Wjets.tlatex,
                 fill_color   = Wjets.fill_color,
                 line_color   = Wjets.line_color,
                 marker_color = Wjets.marker_color,
                 type         = "datadriven",
                 )

addon_Zlljets_35med_1Track = Sample( name   = Zlljets.name,
                 tlatex       = Zlljets.tlatex,
                 fill_color   = Zlljets.fill_color,
                 line_color   = Zlljets.line_color,
                 marker_color = Zlljets.marker_color,
                 type         = "datadriven",
                 )

addon_Zttjets_35med_1Track = Sample( name   = Zttjets.name,
                 tlatex       = Zttjets.tlatex,
                 fill_color   = Zttjets.fill_color,
                 line_color   = Zttjets.line_color,
                 marker_color = Zttjets.marker_color,
                 type         = "datadriven",
                 )

addon_top_35med_1Track = Sample( name   = top.name,
                 tlatex       = top.tlatex,
                 fill_color   = top.fill_color,
                 line_color   = top.line_color,
                 marker_color = top.marker_color,
                 type         = "datadriven",
                 )

addon_data_35med_lowPT_1Track  = Sample( name   = "data",
                 tlatex       = "Same Sign",
                 fill_color   = ROOT.kRed-6,
                 line_color   = ROOT.kBlack,
                 marker_color = ROOT.kRed-6,
                 type         = "datadriven",
                 )

addon_Wjets_35med_lowPT_1Track = Sample( name   = Wjets.name,
                 tlatex       = Wjets.tlatex,
                 fill_color   = Wjets.fill_color,
                 line_color   = Wjets.line_color,
                 marker_color = Wjets.marker_color,
                 type         = "datadriven",
                 )

addon_Zlljets_35med_lowPT_1Track = Sample( name   = Zlljets.name,
                 tlatex       = Zlljets.tlatex,
                 fill_color   = Zlljets.fill_color,
                 line_color   = Zlljets.line_color,
                 marker_color = Zlljets.marker_color,
                 type         = "datadriven",
                 )

addon_Zttjets_35med_lowPT_1Track = Sample( name   = Zttjets.name,
                 tlatex       = Zttjets.tlatex,
                 fill_color   = Zttjets.fill_color,
                 line_color   = Zttjets.line_color,
                 marker_color = Zttjets.marker_color,
                 type         = "datadriven",
                 )

addon_top_35med_lowPT_1Track = Sample( name   = top.name,
                 tlatex       = top.tlatex,
                 fill_color   = top.fill_color,
                 line_color   = top.line_color,
                 marker_color = top.marker_color,
                 type         = "datadriven",
                 )

addon_data_35med_highPT_1Track  = Sample( name   = "data",
                 tlatex       = "Same Sign",
                 fill_color   = ROOT.kRed-6,
                 line_color   = ROOT.kBlack,
                 marker_color = ROOT.kRed-6,
                 type         = "datadriven",
                 )

addon_Wjets_35med_highPT_1Track = Sample( name   = Wjets.name,
                 tlatex       = Wjets.tlatex,
                 fill_color   = Wjets.fill_color,
                 line_color   = Wjets.line_color,
                 marker_color = Wjets.marker_color,
                 type         = "datadriven",
                 )

addon_Zlljets_35med_highPT_1Track = Sample( name   = Zlljets.name,
                 tlatex       = Zlljets.tlatex,
                 fill_color   = Zlljets.fill_color,
                 line_color   = Zlljets.line_color,
                 marker_color = Zlljets.marker_color,
                 type         = "datadriven",
                 )

addon_Zttjets_35med_highPT_1Track = Sample( name   = Zttjets.name,
                 tlatex       = Zttjets.tlatex,
                 fill_color   = Zttjets.fill_color,
                 line_color   = Zttjets.line_color,
                 marker_color = Zttjets.marker_color,
                 type         = "datadriven",
                 )

addon_top_35med_highPT_1Track = Sample( name   = top.name,
                 tlatex       = top.tlatex,
                 fill_color   = top.fill_color,
                 line_color   = top.line_color,
                 marker_color = top.marker_color,
                 type         = "datadriven",
                 )

#############

addon_data_lowPT_1Track  = Sample( name   = "data",
                 tlatex       = "Same Sign_lowPT",
                 fill_color   = ROOT.kRed-6,
                 line_color   = ROOT.kBlack,
                 marker_color = ROOT.kRed-6,
                 type         = "datadriven",
                 )

addon_Wjets_lowPT_1Track = Sample( name   = Wjets.name,
                 tlatex       = Wjets.tlatex+"(OS-SS)_lowPT",
                 fill_color   = Wjets.fill_color,
                 line_color   = Wjets.line_color,
                 marker_color = Wjets.marker_color,
                 type         = "datadriven",
                 )

addon_Zlljets_lowPT_1Track = Sample( name   = Zlljets.name,
                 tlatex       = Zlljets.tlatex+"(OS-SS)_lowPT",
                 fill_color   = Zlljets.fill_color,
                 line_color   = Zlljets.line_color,
                 marker_color = Zlljets.marker_color,
                 type         = "datadriven",
                 )

addon_Zttjets_lowPT_1Track = Sample( name   = Zttjets.name,
                 tlatex       = Zttjets.tlatex+"(OS-SS)_lowPT",
                 fill_color   = Zttjets.fill_color,
                 line_color   = Zttjets.line_color,
                 marker_color = Zttjets.marker_color,
                 type         = "datadriven",
                 )

addon_top_lowPT_1Track = Sample( name   = top.name,
                 tlatex       = top.tlatex+"(OS-SS)_lowPT",
                 fill_color   = top.fill_color,
                 line_color   = top.line_color,
                 marker_color = top.marker_color,
                 type         = "datadriven",
                 )

addon_data_highPT_1Track  = Sample( name   = "data",
                 tlatex       = "Same Sign_highPT",
                 fill_color   = ROOT.kRed-6,
                 line_color   = ROOT.kBlack,
                 marker_color = ROOT.kRed-6,
                 type         = "datadriven",
                 )

addon_Wjets_highPT_1Track = Sample( name   = Wjets.name,
                 tlatex       = Wjets.tlatex+"(OS-SS)_highPT",
                 fill_color   = Wjets.fill_color,
                 line_color   = Wjets.line_color,
                 marker_color = Wjets.marker_color,
                 type         = "datadriven",
                 )

addon_Zlljets_highPT_1Track = Sample( name   = Zlljets.name,
                 tlatex       = Zlljets.tlatex+"(OS-SS)_highPT",
                 fill_color   = Zlljets.fill_color,
                 line_color   = Zlljets.line_color,
                 marker_color = Zlljets.marker_color,
                 type         = "datadriven",
                 )

addon_Zttjets_highPT_1Track = Sample( name   = Zttjets.name,
                 tlatex       = Zttjets.tlatex+"(OS-SS)_highPT",
                 fill_color   = Zttjets.fill_color,
                 line_color   = Zttjets.line_color,
                 marker_color = Zttjets.marker_color,
                 type         = "datadriven",
                 )

addon_top_highPT_1Track = Sample( name   = top.name,
                 tlatex       = top.tlatex+"(OS-SS)_highPT",
                 fill_color   = top.fill_color,
                 line_color   = top.line_color,
                 marker_color = top.marker_color,
                 type         = "datadriven",
                 )

#------------------------
# 	three tracks
#------------------------

addon_data_3Track  = Sample( name   = "data",
                 tlatex       = "Same Sign",
                 fill_color   = ROOT.kRed-6,
                 line_color   = ROOT.kBlack,
                 marker_color = ROOT.kRed-6,
                 type         = "datadriven",
                 )

addon_Wjets_3Track = Sample( name   = Wjets.name,
                 tlatex       = Wjets.tlatex,
                 fill_color   = Wjets.fill_color,
                 line_color   = Wjets.line_color,
                 marker_color = Wjets.marker_color,
                 type         = "datadriven",
                 )

addon_Zlljets_3Track = Sample( name   = Zlljets.name,
                 tlatex       = Zlljets.tlatex,
                 fill_color   = Zlljets.fill_color,
                 line_color   = Zlljets.line_color,
                 marker_color = Zlljets.marker_color,
                 type         = "datadriven",
                 )

addon_Zttjets_3Track = Sample( name   = Zttjets.name,
                 tlatex       = Zttjets.tlatex,
                 fill_color   = Zttjets.fill_color,
                 line_color   = Zttjets.line_color,
                 marker_color = Zttjets.marker_color,
                 type         = "datadriven",
                 )

addon_top_3Track = Sample( name   = top.name,
                 tlatex       = top.tlatex,
                 fill_color   = top.fill_color,
                 line_color   = top.line_color,
                 marker_color = top.marker_color,
                 type         = "datadriven",
                 )

addon_data_25med_3Track  = Sample( name   = "data",
                 tlatex       = "Same Sign",
                 fill_color   = ROOT.kRed-6,
                 line_color   = ROOT.kBlack,
                 marker_color = ROOT.kRed-6,
                 type         = "datadriven",
                 )

addon_Wjets_25med_3Track = Sample( name   = Wjets.name,
                 tlatex       = Wjets.tlatex,
                 fill_color   = Wjets.fill_color,
                 line_color   = Wjets.line_color,
                 marker_color = Wjets.marker_color,
                 type         = "datadriven",
                 )

addon_Zlljets_25med_3Track = Sample( name   = Zlljets.name,
                 tlatex       = Zlljets.tlatex,
                 fill_color   = Zlljets.fill_color,
                 line_color   = Zlljets.line_color,
                 marker_color = Zlljets.marker_color,
                 type         = "datadriven",
                 )

addon_Zttjets_25med_3Track = Sample( name   = Zttjets.name,
                 tlatex       = Zttjets.tlatex,
                 fill_color   = Zttjets.fill_color,
                 line_color   = Zttjets.line_color,
                 marker_color = Zttjets.marker_color,
                 type         = "datadriven",
                 )

addon_top_25med_3Track = Sample( name   = top.name,
                 tlatex       = top.tlatex,
                 fill_color   = top.fill_color,
                 line_color   = top.line_color,
                 marker_color = top.marker_color,
                 type         = "datadriven",
                 )

addon_data_25med_lowPT_3Track  = Sample( name   = "data",
                 tlatex       = "Same Sign",
                 fill_color   = ROOT.kRed-6,
                 line_color   = ROOT.kBlack,
                 marker_color = ROOT.kRed-6,
                 type         = "datadriven",
                 )

addon_Wjets_25med_lowPT_3Track = Sample( name   = Wjets.name,
                 tlatex       = Wjets.tlatex,
                 fill_color   = Wjets.fill_color,
                 line_color   = Wjets.line_color,
                 marker_color = Wjets.marker_color,
                 type         = "datadriven",
                 )

addon_Zlljets_25med_lowPT_3Track = Sample( name   = Zlljets.name,
                 tlatex       = Zlljets.tlatex,
                 fill_color   = Zlljets.fill_color,
                 line_color   = Zlljets.line_color,
                 marker_color = Zlljets.marker_color,
                 type         = "datadriven",
                 )

addon_Zttjets_25med_lowPT_3Track = Sample( name   = Zttjets.name,
                 tlatex       = Zttjets.tlatex,
                 fill_color   = Zttjets.fill_color,
                 line_color   = Zttjets.line_color,
                 marker_color = Zttjets.marker_color,
                 type         = "datadriven",
                 )

addon_top_25med_lowPT_3Track = Sample( name   = top.name,
                 tlatex       = top.tlatex,
                 fill_color   = top.fill_color,
                 line_color   = top.line_color,
                 marker_color = top.marker_color,
                 type         = "datadriven",
                 )

addon_data_25med_highPT_3Track  = Sample( name   = "data",
                 tlatex       = "Same Sign",
                 fill_color   = ROOT.kRed-6,
                 line_color   = ROOT.kBlack,
                 marker_color = ROOT.kRed-6,
                 type         = "datadriven",
                 )

addon_Wjets_25med_highPT_3Track = Sample( name   = Wjets.name,
                 tlatex       = Wjets.tlatex,
                 fill_color   = Wjets.fill_color,
                 line_color   = Wjets.line_color,
                 marker_color = Wjets.marker_color,
                 type         = "datadriven",
                 )

addon_Zlljets_25med_highPT_3Track = Sample( name   = Zlljets.name,
                 tlatex       = Zlljets.tlatex,
                 fill_color   = Zlljets.fill_color,
                 line_color   = Zlljets.line_color,
                 marker_color = Zlljets.marker_color,
                 type         = "datadriven",
                 )

addon_Zttjets_25med_highPT_3Track = Sample( name   = Zttjets.name,
                 tlatex       = Zttjets.tlatex,
                 fill_color   = Zttjets.fill_color,
                 line_color   = Zttjets.line_color,
                 marker_color = Zttjets.marker_color,
                 type         = "datadriven",
                 )

addon_top_25med_highPT_3Track = Sample( name   = top.name,
                 tlatex       = top.tlatex,
                 fill_color   = top.fill_color,
                 line_color   = top.line_color,
                 marker_color = top.marker_color,
                 type         = "datadriven",
                 )
##############

addon_data_35med_3Track  = Sample( name   = "data",
                 tlatex       = "Same Sign",
                 fill_color   = ROOT.kRed-6,
                 line_color   = ROOT.kBlack,
                 marker_color = ROOT.kRed-6,
                 type         = "datadriven",
                 )

addon_Wjets_35med_3Track = Sample( name   = Wjets.name,
                 tlatex       = Wjets.tlatex,
                 fill_color   = Wjets.fill_color,
                 line_color   = Wjets.line_color,
                 marker_color = Wjets.marker_color,
                 type         = "datadriven",
                 )

addon_Zlljets_35med_3Track = Sample( name   = Zlljets.name,
                 tlatex       = Zlljets.tlatex,
                 fill_color   = Zlljets.fill_color,
                 line_color   = Zlljets.line_color,
                 marker_color = Zlljets.marker_color,
                 type         = "datadriven",
                 )

addon_Zttjets_35med_3Track = Sample( name   = Zttjets.name,
                 tlatex       = Zttjets.tlatex,
                 fill_color   = Zttjets.fill_color,
                 line_color   = Zttjets.line_color,
                 marker_color = Zttjets.marker_color,
                 type         = "datadriven",
                 )

addon_top_35med_3Track = Sample( name   = top.name,
                 tlatex       = top.tlatex,
                 fill_color   = top.fill_color,
                 line_color   = top.line_color,
                 marker_color = top.marker_color,
                 type         = "datadriven",
                 )

addon_data_35med_lowPT_3Track  = Sample( name   = "data",
                 tlatex       = "Same Sign",
                 fill_color   = ROOT.kRed-6,
                 line_color   = ROOT.kBlack,
                 marker_color = ROOT.kRed-6,
                 type         = "datadriven",
                 )

addon_Wjets_35med_lowPT_3Track = Sample( name   = Wjets.name,
                 tlatex       = Wjets.tlatex,
                 fill_color   = Wjets.fill_color,
                 line_color   = Wjets.line_color,
                 marker_color = Wjets.marker_color,
                 type         = "datadriven",
                 )

addon_Zlljets_35med_lowPT_3Track = Sample( name   = Zlljets.name,
                 tlatex       = Zlljets.tlatex,
                 fill_color   = Zlljets.fill_color,
                 line_color   = Zlljets.line_color,
                 marker_color = Zlljets.marker_color,
                 type         = "datadriven",
                 )

addon_Zttjets_35med_lowPT_3Track = Sample( name   = Zttjets.name,
                 tlatex       = Zttjets.tlatex,
                 fill_color   = Zttjets.fill_color,
                 line_color   = Zttjets.line_color,
                 marker_color = Zttjets.marker_color,
                 type         = "datadriven",
                 )

addon_top_35med_lowPT_3Track = Sample( name   = top.name,
                 tlatex       = top.tlatex,
                 fill_color   = top.fill_color,
                 line_color   = top.line_color,
                 marker_color = top.marker_color,
                 type         = "datadriven",
                 )

addon_data_35med_highPT_3Track  = Sample( name   = "data",
                 tlatex       = "Same Sign",
                 fill_color   = ROOT.kRed-6,
                 line_color   = ROOT.kBlack,
                 marker_color = ROOT.kRed-6,
                 type         = "datadriven",
                 )

addon_Wjets_35med_highPT_3Track = Sample( name   = Wjets.name,
                 tlatex       = Wjets.tlatex,
                 fill_color   = Wjets.fill_color,
                 line_color   = Wjets.line_color,
                 marker_color = Wjets.marker_color,
                 type         = "datadriven",
                 )

addon_Zlljets_35med_highPT_3Track = Sample( name   = Zlljets.name,
                 tlatex       = Zlljets.tlatex,
                 fill_color   = Zlljets.fill_color,
                 line_color   = Zlljets.line_color,
                 marker_color = Zlljets.marker_color,
                 type         = "datadriven",
                 )

addon_Zttjets_35med_highPT_3Track = Sample( name   = Zttjets.name,
                 tlatex       = Zttjets.tlatex,
                 fill_color   = Zttjets.fill_color,
                 line_color   = Zttjets.line_color,
                 marker_color = Zttjets.marker_color,
                 type         = "datadriven",
                 )

addon_top_35med_highPT_3Track = Sample( name   = top.name,
                 tlatex       = top.tlatex,
                 fill_color   = top.fill_color,
                 line_color   = top.line_color,
                 marker_color = top.marker_color,
                 type         = "datadriven",
                 )

#############

addon_data_lowPT_3Track  = Sample( name   = "data",
                 tlatex       = "Same Sign_lowPT",
                 fill_color   = ROOT.kRed-6,
                 line_color   = ROOT.kBlack,
                 marker_color = ROOT.kRed-6,
                 type         = "datadriven",
                 )

addon_Wjets_lowPT_3Track = Sample( name   = Wjets.name,
                 tlatex       = Wjets.tlatex+"(OS-SS)_lowPT",
                 fill_color   = Wjets.fill_color,
                 line_color   = Wjets.line_color,
                 marker_color = Wjets.marker_color,
                 type         = "datadriven",
                 )

addon_Zlljets_lowPT_3Track = Sample( name   = Zlljets.name,
                 tlatex       = Zlljets.tlatex+"(OS-SS)_lowPT",
                 fill_color   = Zlljets.fill_color,
                 line_color   = Zlljets.line_color,
                 marker_color = Zlljets.marker_color,
                 type         = "datadriven",
                 )

addon_Zttjets_lowPT_3Track = Sample( name   = Zttjets.name,
                 tlatex       = Zttjets.tlatex+"(OS-SS)_lowPT",
                 fill_color   = Zttjets.fill_color,
                 line_color   = Zttjets.line_color,
                 marker_color = Zttjets.marker_color,
                 type         = "datadriven",
                 )

addon_top_lowPT_3Track = Sample( name   = top.name,
                 tlatex       = top.tlatex+"(OS-SS)_lowPT",
                 fill_color   = top.fill_color,
                 line_color   = top.line_color,
                 marker_color = top.marker_color,
                 type         = "datadriven",
                 )

addon_data_highPT_3Track  = Sample( name   = "data",
                 tlatex       = "Same Sign_highPT",
                 fill_color   = ROOT.kRed-6,
                 line_color   = ROOT.kBlack,
                 marker_color = ROOT.kRed-6,
                 type         = "datadriven",
                 )

addon_Wjets_highPT_3Track = Sample( name   = Wjets.name,
                 tlatex       = Wjets.tlatex+"(OS-SS)_highPT",
                 fill_color   = Wjets.fill_color,
                 line_color   = Wjets.line_color,
                 marker_color = Wjets.marker_color,
                 type         = "datadriven",
                 )

addon_Zlljets_highPT_3Track = Sample( name   = Zlljets.name,
                 tlatex       = Zlljets.tlatex+"(OS-SS)_highPT",
                 fill_color   = Zlljets.fill_color,
                 line_color   = Zlljets.line_color,
                 marker_color = Zlljets.marker_color,
                 type         = "datadriven",
                 )

addon_Zttjets_highPT_3Track = Sample( name =Zttjets.name,
                 fill_color   = Zttjets.fill_color,
                 line_color   = Zttjets.line_color,
                 marker_color = Zttjets.marker_color,
                 type         = "datadriven",
                 )

addon_top_highPT_3Track = Sample( name   = top.name,
                 tlatex       = top.tlatex+"(OS-SS)_highPT",
                 fill_color   = top.fill_color,
                 line_color   = top.line_color,
                 marker_color = top.marker_color,
                 type         = "datadriven",
                 )

#-------------------------------------------------------------------------------
# Collections
#-------------------------------------------------------------------------------

all_data = data.daughters

all_mc = []

all_mc += Wtaujets.daughters
all_mc += Wenujets.daughters
all_mc += Wmunujets.daughters
all_mc += Zeejets.daughters
all_mc += Zmumujets.daughters
all_mc += Zttjets_truth.daughters
all_mc += Zttjets_antitruth.daughters
all_mc += top_truth.daughters
all_mc += top_antitruth.daughters

## EOF
