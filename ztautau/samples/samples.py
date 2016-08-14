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
# v12 2015
"""
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
# v15 2015

GRL += ["276073", "276778",  "279345",  "280423",  "281130",  "283608",
        "276147", "276790",  "279515",  "280464",  "281143",  "283780",
        "276161", "276952",  "279598",  "280500",  "281317",  "284006",
        "276183", "276954",  "279685",  "280520",  "281381",  "284154",
        "276189", "278727",  "279764",  "280614",  "281385",  "284213",
        "276212", "278748",  "279813",  "280673",  "281411",  "284285",
        "276245", "278880",  "279867",  "280753",  "282625",  "284420",
        "276262", "278912",  "279928",  "280853",  "282712",  "284427",
        "276329", "278968",  "279932",  "280862",  "282784",  "284473",
        "276330", "278970",  "279984",  "280950",  "282992",  "284484",
        "276336", "279169",  "280231",  "280977",  "283074",  "276416",
        "279259", "280273",  "281070",  "283155",  "276511",  "279279",
        "280319", "281074",  "283270",  "276689",  "279284",  "280368",
        "281075", "283429",  "276731",  "282631"]
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


#---------- 2016 ---------
"""
# v17 2016
GRL += ["297730", "298591",  "298595",  "298609",  "298633",  "298687",
        "298690", "298771",  "298773",  "298862",  "298967",  "299055",
        "299144", "299147",  "299184",  "299241",  "299243",  "299288",
        "299315", "299340",  "299343",  "299390",  "299584",  "300279",
        "300287", "300345",  "300415",  "300418",  "300487",  "300540",
        "300571", "300600",  "300655",  "300687",  "300784",  "300800",
        "300863", "300908",  "301912",  "301915",  "301918",  "301932",
        "301973", "302053",  "302137",  "302265",  "302269",  "302300",
        "302347", "302380",  "302391",  "302393",  "302737",  "302829",
        "302831", "302872",  "302919",  "302925",  "302956",  "303007",
        "303059", "303079",  "303201",  "303208",  "303264",  "303266",
        "303291", "303304",  "303338",  "303421",  "303499",  "303560"]

"""
"""
# v19 2016
GRL += ["297730", "298591",  "298595",  "298609",  "298633",  "298687",
        "298690", "298771",  "298773",  "298862",  "298967",  "299055",
        "299144", "299147",  "299184",  "299241",  "299243",  "299288",
        "299315", "299340",  "299343",  "299390",  "299584",  "300279",
        "300287", "300345",  "300415",  "300418",  "300487",  "300540",
        "300571", "300600",  "300655",  "300687",  "300784",  "300800",
        "300863", "300908",  "301912",  "301915",  "301918",  "301932",
        "301973", "302053",  "302137",  "302265",  "302269",  "302300",
        "302347", "302380",  "302391",  "302393",  "302737",  "302829",
        "302831", "302872",  "302919",  "302925",  "302956",  "303007",
        "303059", "303079",  "303201",  "303208",  "303264",  "303266",
        "303291", "303304",  "303338",  "303421",  "303499",  "303560",
	"303638", "303726",  "303811",  "303817",  "303819",  "303832",
	"303846", "303892"]
"""
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
# W + jets (Madgraph+Pythia8)
# Notes:
#     * cross sections: https://twiki.cern.ch/twiki/bin/view/AtlasProtected/XsecSummaryWjetsMadgraph
#-----------------------------------------------------------------------------
"""
MadPy8_Wenu_Np0   = Sample( name =  "MadPy8_Wenu_Np0",    xsec = ) 
MadPy8_Wenu_Np1   = Sample( name =  "MadPy8_Wenu_Np1",    xsec = ) 
MadPy8_Wenu_Np2   = Sample( name =  "MadPy8_Wenu_Np2",    xsec = ) 
MadPy8_Wenu_Np3   = Sample( name =  "MadPy8_Wenu_Np3",    xsec = ) 
MadPy8_Wmunu_Np2  = Sample( name =  "MadPy8_Wmunu_Np2",   xsec = ) 
MadPy8_Wmunu_Np3  = Sample( name =  "MadPy8_Wmunu_Np3",   xsec = ) 
MadPy8_Wmunu_Np4  = Sample( name =  "MadPy8_Wmunu_Np4",   xsec = ) 
MadPy8_Wtaunu_Np0 = Sample( name =  "MadPy8_Wtaunu_Np0",  xsec = ) 
MadPy8_Wtaunu_Np1 = Sample( name =  "MadPy8_Wtaunu_Np1",  xsec = ) 
MadPy8_Wtaunu_Np2 = Sample( name =  "MadPy8_Wtaunu_Np2",  xsec = ) 
MadPy8_Wtaunu_Np3 = Sample( name =  "MadPy8_Wtaunu_Np3",  xsec = ) 
MadPy8_Wtaunu_Np4 = Sample( name =  "MadPy8_Wtaunu_Np4",  xsec = ) 
"""


#-----------------------------------------------------------------------------
# Z + jets (Madgraph+Pythia8)
# Notes:
#     * cross sections: https://twiki.cern.ch/twiki/bin/view/AtlasProtected/XsecSummaryZjetsMadgraph 
#-----------------------------------------------------------------------------
"""
MadPy8_Zee_lowMll_Np0    = Sample( name =  "MadPy8_Zee_lowMll_Np0",    xsec = )
MadPy8_Zee_lowMll_Np1    = Sample( name =  "MadPy8_Zee_lowMll_Np1",    xsec = )
MadPy8_Zee_lowMll_Np2    = Sample( name =  "MadPy8_Zee_lowMll_Np2",    xsec = )
MadPy8_Zee_lowMll_Np3    = Sample( name =  "MadPy8_Zee_lowMll_Np3",    xsec = )
MadPy8_Zee_Np0           = Sample( name =  "MadPy8_Zee_Np0",           xsec = )
MadPy8_Zee_Np1           = Sample( name =  "MadPy8_Zee_Np1",           xsec = )
MadPy8_Zee_Np2           = Sample( name =  "MadPy8_Zee_Np2",           xsec = )
MadPy8_Zee_Np3           = Sample( name =  "MadPy8_Zee_Np3",           xsec = )
MadPy8_Zee_Np4           = Sample( name =  "MadPy8_Zee_Np4",           xsec = )
MadPy8_Zmumu_lowMll_Np0  = Sample( name =  "MadPy8_Zmumu_lowMll_Np0",  xsec = )
MadPy8_Zmumu_lowMll_Np1  = Sample( name =  "MadPy8_Zmumu_lowMll_Np1",  xsec = )
MadPy8_Zmumu_lowMll_Np2  = Sample( name =  "MadPy8_Zmumu_lowMll_Np2",  xsec = )
MadPy8_Zmumu_lowMll_Np3  = Sample( name =  "MadPy8_Zmumu_lowMll_Np3",  xsec = )
MadPy8_Zmumu_lowMll_Np4  = Sample( name =  "MadPy8_Zmumu_lowMll_Np4",  xsec = )
MadPy8_Zmumu_Np0         = Sample( name =  "MadPy8_Zmumu_Np0",         xsec = )
MadPy8_Zmumu_Np1         = Sample( name =  "MadPy8_Zmumu_Np1",         xsec = )
MadPy8_Zmumu_Np2         = Sample( name =  "MadPy8_Zmumu_Np2",         xsec = )
MadPy8_Zmumu_Np3         = Sample( name =  "MadPy8_Zmumu_Np3",         xsec = )
MadPy8_Zmumu_Np4         = Sample( name =  "MadPy8_Zmumu_Np4",         xsec = )
MadPy8_Ztt_lowMll_Np0    = Sample( name =  "MadPy8_Ztt_lowMll_Np0",    xsec = )
MadPy8_Ztt_lowMll_Np1    = Sample( name =  "MadPy8_Ztt_lowMll_Np1",    xsec = )
MadPy8_Ztt_lowMll_Np2    = Sample( name =  "MadPy8_Ztt_lowMll_Np2",    xsec = )
MadPy8_Ztt_lowMll_Np3    = Sample( name =  "MadPy8_Ztt_lowMll_Np3",    xsec = )
MadPy8_Ztt_lowMll_Np4    = Sample( name =  "MadPy8_Ztt_lowMll_Np4",    xsec = )
MadPy8_Ztt_Np0           = Sample( name =  "MadPy8_Ztt_Np0",           xsec = )
MadPy8_Ztt_Np1           = Sample( name =  "MadPy8_Ztt_Np1",           xsec = )
MadPy8_Ztt_Np2           = Sample( name =  "MadPy8_Ztt_Np2",           xsec = )
MadPy8_Ztt_Np3           = Sample( name =  "MadPy8_Ztt_Np3",           xsec = )
MadPy8_Ztt_Np4           = Sample( name =  "MadPy8_Ztt_Np4",           xsec = )
"""


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
                  fill_color = ROOT.kAzure+1,
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
                  tlatex = 'W #rightarrow l#nu+jets',
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
                               PoPy8_Ztt,
                              ],
                )

# merge light leptons ones
Zlljets = Sample( name =   'Zlljets',
                  tlatex = 'Z #rightarrow ll+jets',
                  fill_color = ROOT.kCyan+2,
                  line_color =  ROOT.kBlack,
                  marker_color =  ROOT.kCyan+2,
                  daughters = [
                               Zmumujets,
                               Zeejets,
                              ],
                )


#-----------------------------------------------------------------------------
# W + jets (Sherpa)
# Notes:
#       * cross sections: https://twiki.cern.ch/twiki/bin/view/AtlasProtected/XsecSummaryWjetsSherpaLight (light filter)
#                         https://twiki.cern.ch/twiki/bin/view/AtlasProtected/XsecSummaryWjetsSherpaC     (C filter) 
#                         https://twiki.cern.ch/twiki/bin/view/AtlasProtected/XsecSummaryWjetsSherpaB     (B filter) 
#-----------------------------------------------------------------------------

#-----
# Wenu
#-----

Sh_NNPDF30NNLO_Wenu_Pt0_70_CVetoBVeto      = Sample( name =  "Sh_NNPDF30NNLO_Wenu_Pt0_70_CVetoBVeto",      xsec = 17217.7589809) 
Sh_NNPDF30NNLO_Wenu_Pt70_140_CVetoBVeto    = Sample( name =  "Sh_NNPDF30NNLO_Wenu_Pt70_140_CVetoBVeto",    xsec = 419.458902664)
Sh_NNPDF30NNLO_Wenu_Pt140_280_CVetoBVeto   = Sample( name =  "Sh_NNPDF30NNLO_Wenu_Pt140_280_CVetoBVeto",   xsec = 55.812213827 )
Sh_NNPDF30NNLO_Wenu_Pt280_500_CVetoBVeto   = Sample( name =  "Sh_NNPDF30NNLO_Wenu_Pt280_500_CVetoBVeto",   xsec = 3.415293894  )
Sh_NNPDF30NNLO_Wenu_Pt500_700_CVetoBVeto   = Sample( name =  "Sh_NNPDF30NNLO_Wenu_Pt500_700_CVetoBVeto",   xsec = 0.204156559  )
Sh_NNPDF30NNLO_Wenu_Pt700_1000_CVetoBVeto  = Sample( name =  "Sh_NNPDF30NNLO_Wenu_Pt700_1000_CVetoBVeto",  xsec = 0.033518757  )
Sh_NNPDF30NNLO_Wenu_Pt1000_2000_CVetoBVeto = Sample( name =  "Sh_NNPDF30NNLO_Wenu_Pt1000_2000_CVetoBVeto", xsec = 0.004526723  )
                                                                                                             
Sh_NNPDF30NNLO_Wenu_Pt0_70_CFiltBVet       = Sample( name =  "Sh_NNPDF30NNLO_Wenu_Pt0_70_CFiltBVet",       xsec = 957.166425598)
Sh_NNPDF30NNLO_Wenu_Pt70_140_CFiltBVet     = Sample( name =  "Sh_NNPDF30NNLO_Wenu_Pt70_140_CFiltBVet",     xsec = 101.537442087)
Sh_NNPDF30NNLO_Wenu_Pt140_280_CFiltBVet    = Sample( name =  "Sh_NNPDF30NNLO_Wenu_Pt140_280_CFiltBVet",    xsec = 16.838461137 )
Sh_NNPDF30NNLO_Wenu_Pt280_500_CFiltBVet    = Sample( name =  "Sh_NNPDF30NNLO_Wenu_Pt280_500_CFiltBVet",    xsec = 1.159086019  )
Sh_NNPDF30NNLO_Wenu_Pt500_700_CFiltBVet    = Sample( name =  "Sh_NNPDF30NNLO_Wenu_Pt500_700_CFiltBVet",    xsec = 0.076063692  )
Sh_NNPDF30NNLO_Wenu_Pt700_1000_CFiltBVet   = Sample( name =  "Sh_NNPDF30NNLO_Wenu_Pt700_1000_CFiltBVet",   xsec = 0.011205872  )
Sh_NNPDF30NNLO_Wenu_Pt1000_2000_CFiltBVet  = Sample( name =  "Sh_NNPDF30NNLO_Wenu_Pt1000_2000_CFiltBVet",  xsec = 0.001755119  )
                                                                                                             
Sh_NNPDF30NNLO_Wenu_Pt0_70_BFilter         = Sample( name =  "Sh_NNPDF30NNLO_Wenu_Pt0_70_BFilter",         xsec = 1161.20628355)
Sh_NNPDF30NNLO_Wenu_Pt70_140_BFilter       = Sample( name =  "Sh_NNPDF30NNLO_Wenu_Pt70_140_BFilter",       xsec = 55.459634594 )
Sh_NNPDF30NNLO_Wenu_Pt140_280_BFilter      = Sample( name =  "Sh_NNPDF30NNLO_Wenu_Pt140_280_BFilter",      xsec = 9.19142934   )
Sh_NNPDF30NNLO_Wenu_Pt280_500_BFilter      = Sample( name =  "Sh_NNPDF30NNLO_Wenu_Pt280_500_BFilter",      xsec = 0.679805485  )
Sh_NNPDF30NNLO_Wenu_Pt500_700_BFilter      = Sample( name =  "Sh_NNPDF30NNLO_Wenu_Pt500_700_BFilter",      xsec = 0.048845728  )
Sh_NNPDF30NNLO_Wenu_Pt700_1000_BFilter     = Sample( name =  "Sh_NNPDF30NNLO_Wenu_Pt700_1000_BFilter",     xsec = 0.00959807   )
Sh_NNPDF30NNLO_Wenu_Pt1000_2000_BFilter    = Sample( name =  "Sh_NNPDF30NNLO_Wenu_Pt1000_2000_BFilter",    xsec = 0.001258268  )

Wenu = Sample( name =   'Wenu',
                  tlatex = 'W #rightarrow e#nu+jets',
                  fill_color = ROOT.kRed+1,
                  line_color =  ROOT.kRed+2,
                  marker_color =  ROOT.kRed+2,
                  daughters = [
                               Sh_NNPDF30NNLO_Wenu_Pt0_70_CVetoBVeto,        
                               Sh_NNPDF30NNLO_Wenu_Pt70_140_CVetoBVeto,                                    
                               Sh_NNPDF30NNLO_Wenu_Pt140_280_CVetoBVeto,     
                               Sh_NNPDF30NNLO_Wenu_Pt280_500_CVetoBVeto,     
                               Sh_NNPDF30NNLO_Wenu_Pt500_700_CVetoBVeto,     
                               #Sh_NNPDF30NNLO_Wenu_Pt700_1000_CVetoBVeto,    missing!!!
                               #Sh_NNPDF30NNLO_Wenu_Pt1000_2000_CVetoBVeto,   missing!!!
                               Sh_NNPDF30NNLO_Wenu_Pt0_70_CFiltBVet,      
                               Sh_NNPDF30NNLO_Wenu_Pt70_140_CFiltBVet,    
                               Sh_NNPDF30NNLO_Wenu_Pt140_280_CFiltBVet,   
                               Sh_NNPDF30NNLO_Wenu_Pt280_500_CFiltBVet,   
                               Sh_NNPDF30NNLO_Wenu_Pt500_700_CFiltBVet,   
                               Sh_NNPDF30NNLO_Wenu_Pt700_1000_CFiltBVet,  
                               #Sh_NNPDF30NNLO_Wenu_Pt1000_2000_CFiltBVet,    missing!!! 
                               Sh_NNPDF30NNLO_Wenu_Pt0_70_BFilter,           
                               Sh_NNPDF30NNLO_Wenu_Pt70_140_BFilter,         
                               Sh_NNPDF30NNLO_Wenu_Pt140_280_BFilter,        
                               Sh_NNPDF30NNLO_Wenu_Pt280_500_BFilter,        
                               Sh_NNPDF30NNLO_Wenu_Pt500_700_BFilter,        
                               Sh_NNPDF30NNLO_Wenu_Pt700_1000_BFilter,       
                               Sh_NNPDF30NNLO_Wenu_Pt1000_2000_BFilter,      
                              ],
                ) 


#------
# Wmunu
#------

Sh_NNPDF30NNLO_Wmunu_Pt0_70_CVetoBVeto      = Sample( name =  "Sh_NNPDF30NNLO_Wmunu_Pt0_70_CVetoBVeto",      xsec = 17340.6393371)
Sh_NNPDF30NNLO_Wmunu_Pt70_140_CVetoBVeto    = Sample( name =  "Sh_NNPDF30NNLO_Wmunu_Pt70_140_CVetoBVeto",    xsec = 419.506840815) 
Sh_NNPDF30NNLO_Wmunu_Pt140_280_CVetoBVeto   = Sample( name =  "Sh_NNPDF30NNLO_Wmunu_Pt140_280_CVetoBVeto",   xsec = 55.841494484 )
Sh_NNPDF30NNLO_Wmunu_Pt280_500_CVetoBVeto   = Sample( name =  "Sh_NNPDF30NNLO_Wmunu_Pt280_500_CVetoBVeto",   xsec = 3.432031461  )
Sh_NNPDF30NNLO_Wmunu_Pt500_700_CVetoBVeto   = Sample( name =  "Sh_NNPDF30NNLO_Wmunu_Pt500_700_CVetoBVeto",   xsec = 0.202350513  )
Sh_NNPDF30NNLO_Wmunu_Pt700_1000_CVetoBVeto  = Sample( name =  "Sh_NNPDF30NNLO_Wmunu_Pt700_1000_CVetoBVeto",  xsec = 0.035335673  )
Sh_NNPDF30NNLO_Wmunu_Pt1000_2000_CVetoBVeto = Sample( name =  "Sh_NNPDF30NNLO_Wmunu_Pt1000_2000_CVetoBVeto", xsec = 0.004290787  )
                                                                                                                  
Sh_NNPDF30NNLO_Wmunu_Pt0_70_CFiltBVet       = Sample( name =  "Sh_NNPDF30NNLO_Wmunu_Pt0_70_CFiltBVet",       xsec = 919.838769744)
Sh_NNPDF30NNLO_Wmunu_Pt70_140_CFiltBVet     = Sample( name =  "Sh_NNPDF30NNLO_Wmunu_Pt70_140_CFiltBVet",     xsec = 100.564174092)
Sh_NNPDF30NNLO_Wmunu_Pt140_280_CFiltBVet    = Sample( name =  "Sh_NNPDF30NNLO_Wmunu_Pt140_280_CFiltBVet",    xsec = 16.649629005 )
Sh_NNPDF30NNLO_Wmunu_Pt280_500_CFiltBVet    = Sample( name =  "Sh_NNPDF30NNLO_Wmunu_Pt280_500_CFiltBVet",    xsec = 1.160810758  )
Sh_NNPDF30NNLO_Wmunu_Pt500_700_CFiltBVet    = Sample( name =  "Sh_NNPDF30NNLO_Wmunu_Pt500_700_CFiltBVet",    xsec = 0.075282837  )
Sh_NNPDF30NNLO_Wmunu_Pt700_1000_CFiltBVet   = Sample( name =  "Sh_NNPDF30NNLO_Wmunu_Pt700_1000_CFiltBVet",   xsec = 0.012748102  )
Sh_NNPDF30NNLO_Wmunu_Pt1000_2000_CFiltBVet  = Sample( name =  "Sh_NNPDF30NNLO_Wmunu_Pt1000_2000_CFiltBVet",  xsec = 0.001699121  )
                                                                                                                  
Sh_NNPDF30NNLO_Wmunu_Pt0_70_BFilter         = Sample( name =  "Sh_NNPDF30NNLO_Wmunu_Pt0_70_BFilter",         xsec = 1158.97092326)
Sh_NNPDF30NNLO_Wmunu_Pt70_140_BFilter       = Sample( name =  "Sh_NNPDF30NNLO_Wmunu_Pt70_140_BFilter",       xsec = 55.568454407 )
Sh_NNPDF30NNLO_Wmunu_Pt140_280_BFilter      = Sample( name =  "Sh_NNPDF30NNLO_Wmunu_Pt140_280_BFilter",      xsec = 9.22013311   )
Sh_NNPDF30NNLO_Wmunu_Pt280_500_BFilter      = Sample( name =  "Sh_NNPDF30NNLO_Wmunu_Pt280_500_BFilter",      xsec = 0.680142792  )
Sh_NNPDF30NNLO_Wmunu_Pt500_700_BFilter      = Sample( name =  "Sh_NNPDF30NNLO_Wmunu_Pt500_700_BFilter",      xsec = 0.051706999  )
Sh_NNPDF30NNLO_Wmunu_Pt700_1000_BFilter     = Sample( name =  "Sh_NNPDF30NNLO_Wmunu_Pt700_1000_BFilter",     xsec = 0.00874855   )
Sh_NNPDF30NNLO_Wmunu_Pt1000_2000_BFilter    = Sample( name =  "Sh_NNPDF30NNLO_Wmunu_Pt1000_2000_BFilter",    xsec = 0.001139207  )

Wmunu = Sample( name =   'Wmunu',
                  tlatex = 'W #rightarrow #mu#nu+jets',
                  fill_color = ROOT.kGreen+1,
                  line_color =  ROOT.kGreen+2,
                  marker_color =  ROOT.kGreen+2,
                  daughters = [
                               Sh_NNPDF30NNLO_Wmunu_Pt0_70_CVetoBVeto,        
                               Sh_NNPDF30NNLO_Wmunu_Pt70_140_CVetoBVeto,                                    
                               #Sh_NNPDF30NNLO_Wmunu_Pt140_280_CVetoBVeto,     missing !!!
                               #Sh_NNPDF30NNLO_Wmunu_Pt280_500_CVetoBVeto,     missing !!!
                               #Sh_NNPDF30NNLO_Wmunu_Pt500_700_CVetoBVeto,     missing !!!
                               #Sh_NNPDF30NNLO_Wmunu_Pt700_1000_CVetoBVeto,    missing !!!
                               #Sh_NNPDF30NNLO_Wmunu_Pt1000_2000_CVetoBVeto,   missing !!!
                               Sh_NNPDF30NNLO_Wmunu_Pt0_70_CFiltBVet,      
                               Sh_NNPDF30NNLO_Wmunu_Pt70_140_CFiltBVet,    
                               Sh_NNPDF30NNLO_Wmunu_Pt140_280_CFiltBVet,   
                               Sh_NNPDF30NNLO_Wmunu_Pt280_500_CFiltBVet,   
                               Sh_NNPDF30NNLO_Wmunu_Pt500_700_CFiltBVet,   
                               #Sh_NNPDF30NNLO_Wmunu_Pt700_1000_CFiltBVet,     missing !!!
                               #Sh_NNPDF30NNLO_Wmunu_Pt1000_2000_CFiltBVet,    missing !!!
                               Sh_NNPDF30NNLO_Wmunu_Pt0_70_BFilter,           
                               Sh_NNPDF30NNLO_Wmunu_Pt70_140_BFilter,         
                               Sh_NNPDF30NNLO_Wmunu_Pt140_280_BFilter,        
                               Sh_NNPDF30NNLO_Wmunu_Pt280_500_BFilter,        
                               Sh_NNPDF30NNLO_Wmunu_Pt500_700_BFilter,        
                               Sh_NNPDF30NNLO_Wmunu_Pt700_1000_BFilter,       
                               Sh_NNPDF30NNLO_Wmunu_Pt1000_2000_BFilter,      
                              ],
                ) 

#-------
# Wtaunu
#-------

Sh_NNPDF30NNLO_Wtaunu_Pt0_70_CVetoBVeto      = Sample( name =  "Sh_NNPDF30NNLO_Wtaunu_Pt0_70_CVetoBVeto",      xsec = 17314.4290983 )
Sh_NNPDF30NNLO_Wtaunu_Pt70_140_CVetoBVeto    = Sample( name =  "Sh_NNPDF30NNLO_Wtaunu_Pt70_140_CVetoBVeto",    xsec = 419.122578495 ) 
Sh_NNPDF30NNLO_Wtaunu_Pt140_280_CVetoBVeto   = Sample( name =  "Sh_NNPDF30NNLO_Wtaunu_Pt140_280_CVetoBVeto",   xsec = 55.916387347  )
Sh_NNPDF30NNLO_Wtaunu_Pt280_500_CVetoBVeto   = Sample( name =  "Sh_NNPDF30NNLO_Wtaunu_Pt280_500_CVetoBVeto",   xsec = 3.406527101   )
Sh_NNPDF30NNLO_Wtaunu_Pt500_700_CVetoBVeto   = Sample( name =  "Sh_NNPDF30NNLO_Wtaunu_Pt500_700_CVetoBVeto",   xsec = 0.197106496   )
Sh_NNPDF30NNLO_Wtaunu_Pt700_1000_CVetoBVeto  = Sample( name =  "Sh_NNPDF30NNLO_Wtaunu_Pt700_1000_CVetoBVeto",  xsec = 0.034681733   )
Sh_NNPDF30NNLO_Wtaunu_Pt1000_2000_CVetoBVeto = Sample( name =  "Sh_NNPDF30NNLO_Wtaunu_Pt1000_2000_CVetoBVeto", xsec = 0.004373938   )
                                                                                                                 
Sh_NNPDF30NNLO_Wtaunu_Pt0_70_CFiltBVet       = Sample( name =  "Sh_NNPDF30NNLO_Wtaunu_Pt0_70_CFiltBVet",       xsec =  945.692972992)
Sh_NNPDF30NNLO_Wtaunu_Pt70_140_CFiltBVet     = Sample( name =  "Sh_NNPDF30NNLO_Wtaunu_Pt70_140_CFiltBVet",     xsec =  101.503853138)
Sh_NNPDF30NNLO_Wtaunu_Pt140_280_CFiltBVet    = Sample( name =  "Sh_NNPDF30NNLO_Wtaunu_Pt140_280_CFiltBVet",    xsec =  16.794548709 )
Sh_NNPDF30NNLO_Wtaunu_Pt280_500_CFiltBVet    = Sample( name =  "Sh_NNPDF30NNLO_Wtaunu_Pt280_500_CFiltBVet",    xsec =  1.149628406  )
Sh_NNPDF30NNLO_Wtaunu_Pt500_700_CFiltBVet    = Sample( name =  "Sh_NNPDF30NNLO_Wtaunu_Pt500_700_CFiltBVet",    xsec =  0.074064213  )
Sh_NNPDF30NNLO_Wtaunu_Pt700_1000_CFiltBVet   = Sample( name =  "Sh_NNPDF30NNLO_Wtaunu_Pt700_1000_CFiltBVet",   xsec =  0.012089998  )
Sh_NNPDF30NNLO_Wtaunu_Pt1000_2000_CFiltBVet  = Sample( name =  "Sh_NNPDF30NNLO_Wtaunu_Pt1000_2000_CFiltBVet",  xsec =  0.001705245  )
                                                                                                                 
Sh_NNPDF30NNLO_Wtaunu_Pt0_70_BFilter         = Sample( name =  "Sh_NNPDF30NNLO_Wtaunu_Pt0_70_BFilter",         xsec =  1159.25995066)
Sh_NNPDF30NNLO_Wtaunu_Pt70_140_BFilter       = Sample( name =  "Sh_NNPDF30NNLO_Wtaunu_Pt70_140_BFilter",       xsec =  55.038425769 )
Sh_NNPDF30NNLO_Wtaunu_Pt140_280_BFilter      = Sample( name =  "Sh_NNPDF30NNLO_Wtaunu_Pt140_280_BFilter",      xsec =  9.259878116  )
Sh_NNPDF30NNLO_Wtaunu_Pt280_500_BFilter      = Sample( name =  "Sh_NNPDF30NNLO_Wtaunu_Pt280_500_BFilter",      xsec =  0.692107677  )
Sh_NNPDF30NNLO_Wtaunu_Pt500_700_BFilter      = Sample( name =  "Sh_NNPDF30NNLO_Wtaunu_Pt500_700_BFilter",      xsec =  0.05020675   )
Sh_NNPDF30NNLO_Wtaunu_Pt700_1000_BFilter     = Sample( name =  "Sh_NNPDF30NNLO_Wtaunu_Pt700_1000_BFilter",     xsec =  0.008573241  )
Sh_NNPDF30NNLO_Wtaunu_Pt1000_2000_BFilter    = Sample( name =  "Sh_NNPDF30NNLO_Wtaunu_Pt1000_2000_BFilter",    xsec =  0.001282272  )

Wtaunu = Sample( name =   'Wtaunu',
                  tlatex = 'W #rightarrow #tau#nu+jets',
                  fill_color = ROOT.kBlue+1,
                  line_color =  ROOT.kBlue+2,
                  marker_color =  ROOT.kBlue+2,
                  daughters = [
                               #Sh_NNPDF30NNLO_Wtaunu_Pt0_70_CVetoBVeto,     missing !!!
                               #Sh_NNPDF30NNLO_Wtaunu_Pt70_140_CVetoBVeto,                                    
                               #Sh_NNPDF30NNLO_Wtaunu_Pt140_280_CVetoBVeto,     
                               #Sh_NNPDF30NNLO_Wtaunu_Pt280_500_CVetoBVeto,     
                               #Sh_NNPDF30NNLO_Wtaunu_Pt500_700_CVetoBVeto,     
                               #Sh_NNPDF30NNLO_Wtaunu_Pt700_1000_CVetoBVeto,    
                               #Sh_NNPDF30NNLO_Wtaunu_Pt1000_2000_CVetoBVeto,   
                               #Sh_NNPDF30NNLO_Wtaunu_Pt0_70_CFiltBVet,      
                               #Sh_NNPDF30NNLO_Wtaunu_Pt70_140_CFiltBVet,    
                               #Sh_NNPDF30NNLO_Wtaunu_Pt140_280_CFiltBVet,   
                               #Sh_NNPDF30NNLO_Wtaunu_Pt280_500_CFiltBVet,   
                               #Sh_NNPDF30NNLO_Wtaunu_Pt500_700_CFiltBVet,   
                               #Sh_NNPDF30NNLO_Wtaunu_Pt700_1000_CFiltBVet,  
                               #Sh_NNPDF30NNLO_Wtaunu_Pt1000_2000_CFiltBVet, 
                               #Sh_NNPDF30NNLO_Wtaunu_Pt0_70_BFilter,           
                               Sh_NNPDF30NNLO_Wtaunu_Pt70_140_BFilter,         
                               Sh_NNPDF30NNLO_Wtaunu_Pt140_280_BFilter,        
                               Sh_NNPDF30NNLO_Wtaunu_Pt280_500_BFilter,        
                               Sh_NNPDF30NNLO_Wtaunu_Pt500_700_BFilter,        
                               Sh_NNPDF30NNLO_Wtaunu_Pt700_1000_BFilter,       
                               #Sh_NNPDF30NNLO_Wtaunu_Pt1000_2000_BFilter,      
                              ],
                ) 


#-----------------------------------------------------------------------------
# Z + jets (Sherpa)
# Notes:
#       * cross sections: https://twiki.cern.ch/twiki/bin/view/AtlasProtected/XsecSummaryZjetsSherpaLight (light filter)
#                         https://twiki.cern.ch/twiki/bin/view/AtlasProtected/XsecSummaryZjetsSherpaC     (C filter) 
#                         https://twiki.cern.ch/twiki/bin/view/AtlasProtected/XsecSummaryZjetsSherpaB     (B filter) 
#-----------------------------------------------------------------------------

#-----
# Zee
#-----

Sh_NNPDF30NNLO_Zee_Pt0_70_CVetoBVeto      = Sample( name =  "Sh_NNPDF30NNLO_Zee_Pt0_70_CVetoBVeto",      xsec = 1549.26000693) 
Sh_NNPDF30NNLO_Zee_Pt70_140_CVetoBVeto    = Sample( name =  "Sh_NNPDF30NNLO_Zee_Pt70_140_CVetoBVeto",    xsec = 44.22776987  )
Sh_NNPDF30NNLO_Zee_Pt140_280_CVetoBVeto   = Sample( name =  "Sh_NNPDF30NNLO_Zee_Pt140_280_CVetoBVeto",   xsec = 6.506584189  )
Sh_NNPDF30NNLO_Zee_Pt280_500_CVetoBVeto   = Sample( name =  "Sh_NNPDF30NNLO_Zee_Pt280_500_CVetoBVeto",   xsec = 0.407251422  )
Sh_NNPDF30NNLO_Zee_Pt500_700_CVetoBVeto   = Sample( name =  "Sh_NNPDF30NNLO_Zee_Pt500_700_CVetoBVeto",   xsec = 0.024016122  )
Sh_NNPDF30NNLO_Zee_Pt700_1000_CVetoBVeto  = Sample( name =  "Sh_NNPDF30NNLO_Zee_Pt700_1000_CVetoBVeto",  xsec = 0.004150103  )
Sh_NNPDF30NNLO_Zee_Pt1000_2000_CVetoBVeto = Sample( name =  "Sh_NNPDF30NNLO_Zee_Pt1000_2000_CVetoBVeto", xsec = 0.000504024  )
                                                                                                        
Sh_NNPDF30NNLO_Zee_Pt0_70_CFiltBVet       = Sample( name =  "Sh_NNPDF30NNLO_Zee_Pt0_70_CFiltBVet",       xsec = 282.772058138)
Sh_NNPDF30NNLO_Zee_Pt70_140_CFiltBVet     = Sample( name =  "Sh_NNPDF30NNLO_Zee_Pt70_140_CFiltBVet",     xsec = 14.952742932 )
Sh_NNPDF30NNLO_Zee_Pt140_280_CFiltBVet    = Sample( name =  "Sh_NNPDF30NNLO_Zee_Pt140_280_CFiltBVet",    xsec = 2.538900646  )
Sh_NNPDF30NNLO_Zee_Pt280_500_CFiltBVet    = Sample( name =  "Sh_NNPDF30NNLO_Zee_Pt280_500_CFiltBVet",    xsec = 0.17993672   )
Sh_NNPDF30NNLO_Zee_Pt500_700_CFiltBVet    = Sample( name =  "Sh_NNPDF30NNLO_Zee_Pt500_700_CFiltBVet",    xsec = 0.011351653  )
Sh_NNPDF30NNLO_Zee_Pt700_1000_CFiltBVet   = Sample( name =  "Sh_NNPDF30NNLO_Zee_Pt700_1000_CFiltBVet",   xsec = 0.002197952  )
Sh_NNPDF30NNLO_Zee_Pt1000_2000_CFiltBVet  = Sample( name =  "Sh_NNPDF30NNLO_Zee_Pt1000_2000_CFiltBVet",  xsec = 0.000296457  )
                                                                                                        
Sh_NNPDF30NNLO_Zee_Pt0_70_BFilter         = Sample( name =  "Sh_NNPDF30NNLO_Zee_Pt0_70_BFilter",         xsec = 158.396126791)
Sh_NNPDF30NNLO_Zee_Pt70_140_BFilter       = Sample( name =  "Sh_NNPDF30NNLO_Zee_Pt70_140_BFilter",       xsec = 8.994572804  )
Sh_NNPDF30NNLO_Zee_Pt140_280_BFilter      = Sample( name =  "Sh_NNPDF30NNLO_Zee_Pt140_280_BFilter",      xsec = 1.579281881  )
Sh_NNPDF30NNLO_Zee_Pt280_500_BFilter      = Sample( name =  "Sh_NNPDF30NNLO_Zee_Pt280_500_BFilter",      xsec = 0.107766448  )
Sh_NNPDF30NNLO_Zee_Pt500_700_BFilter      = Sample( name =  "Sh_NNPDF30NNLO_Zee_Pt500_700_BFilter",      xsec = 0.007056014  )
Sh_NNPDF30NNLO_Zee_Pt700_1000_BFilter     = Sample( name =  "Sh_NNPDF30NNLO_Zee_Pt700_1000_BFilter",     xsec = 0.001344726  )
Sh_NNPDF30NNLO_Zee_Pt1000_2000_BFilter    = Sample( name =  "Sh_NNPDF30NNLO_Zee_Pt1000_2000_BFilter",    xsec = 0.000183289  )

Zee = Sample( name =   'Zee',
                  tlatex = 'Z #rightarrow ee+jets',
                  fill_color = ROOT.kOrange+1,
                  line_color =  ROOT.kOrange+2,
                  marker_color =  ROOT.kOrange+2,
                  daughters = [
                               Sh_NNPDF30NNLO_Zee_Pt0_70_CVetoBVeto,        
                               Sh_NNPDF30NNLO_Zee_Pt70_140_CVetoBVeto,                                    
                               Sh_NNPDF30NNLO_Zee_Pt140_280_CVetoBVeto,     
                               Sh_NNPDF30NNLO_Zee_Pt280_500_CVetoBVeto,     
                               Sh_NNPDF30NNLO_Zee_Pt500_700_CVetoBVeto,     
                               Sh_NNPDF30NNLO_Zee_Pt700_1000_CVetoBVeto,    
                               #Sh_NNPDF30NNLO_Zee_Pt1000_2000_CVetoBVeto,   
                               Sh_NNPDF30NNLO_Zee_Pt0_70_CFiltBVet,      
                               Sh_NNPDF30NNLO_Zee_Pt70_140_CFiltBVet,    
                               Sh_NNPDF30NNLO_Zee_Pt140_280_CFiltBVet,   
                               Sh_NNPDF30NNLO_Zee_Pt280_500_CFiltBVet,   
                               Sh_NNPDF30NNLO_Zee_Pt500_700_CFiltBVet,   
                               Sh_NNPDF30NNLO_Zee_Pt700_1000_CFiltBVet,  
                               Sh_NNPDF30NNLO_Zee_Pt1000_2000_CFiltBVet, 
                               Sh_NNPDF30NNLO_Zee_Pt0_70_BFilter,           
                               Sh_NNPDF30NNLO_Zee_Pt70_140_BFilter,         
                               Sh_NNPDF30NNLO_Zee_Pt140_280_BFilter,        
                               Sh_NNPDF30NNLO_Zee_Pt280_500_BFilter,        
                               Sh_NNPDF30NNLO_Zee_Pt500_700_BFilter,        
                               Sh_NNPDF30NNLO_Zee_Pt700_1000_BFilter,       
                               Sh_NNPDF30NNLO_Zee_Pt1000_2000_BFilter,      
                              ],
                ) 


#-------
# Zmumu
#-------

Sh_NNPDF30NNLO_Zmumu_Pt0_70_CVetoBVeto      = Sample( name =  "Sh_NNPDF30NNLO_Zmumu_Pt0_70_CVetoBVeto",      xsec = 1545.03412569 )
Sh_NNPDF30NNLO_Zmumu_Pt70_140_CVetoBVeto    = Sample( name =  "Sh_NNPDF30NNLO_Zmumu_Pt70_140_CVetoBVeto",    xsec = 44.406818306  ) 
Sh_NNPDF30NNLO_Zmumu_Pt140_280_CVetoBVeto   = Sample( name =  "Sh_NNPDF30NNLO_Zmumu_Pt140_280_CVetoBVeto",   xsec = 6.403162188   )
Sh_NNPDF30NNLO_Zmumu_Pt280_500_CVetoBVeto   = Sample( name =  "Sh_NNPDF30NNLO_Zmumu_Pt280_500_CVetoBVeto",   xsec = 0.402575488   )
Sh_NNPDF30NNLO_Zmumu_Pt500_700_CVetoBVeto   = Sample( name =  "Sh_NNPDF30NNLO_Zmumu_Pt500_700_CVetoBVeto",   xsec = 0.023490348   )
Sh_NNPDF30NNLO_Zmumu_Pt700_1000_CVetoBVeto  = Sample( name =  "Sh_NNPDF30NNLO_Zmumu_Pt700_1000_CVetoBVeto",  xsec = 0.004066761   )
Sh_NNPDF30NNLO_Zmumu_Pt1000_2000_CVetoBVeto = Sample( name =  "Sh_NNPDF30NNLO_Zmumu_Pt1000_2000_CVetoBVeto", xsec = 0.000566401   )
                                                                                                        
Sh_NNPDF30NNLO_Zmumu_Pt0_70_CFiltBVet       = Sample( name =  "Sh_NNPDF30NNLO_Zmumu_Pt0_70_CFiltBVet",       xsec =  281.969546386)
Sh_NNPDF30NNLO_Zmumu_Pt70_140_CFiltBVet     = Sample( name =  "Sh_NNPDF30NNLO_Zmumu_Pt70_140_CFiltBVet",     xsec =  15.044569464 )
Sh_NNPDF30NNLO_Zmumu_Pt140_280_CFiltBVet    = Sample( name =  "Sh_NNPDF30NNLO_Zmumu_Pt140_280_CFiltBVet",    xsec =  2.535541296  )
Sh_NNPDF30NNLO_Zmumu_Pt280_500_CFiltBVet    = Sample( name =  "Sh_NNPDF30NNLO_Zmumu_Pt280_500_CFiltBVet",    xsec =  0.185533832  )
Sh_NNPDF30NNLO_Zmumu_Pt500_700_CFiltBVet    = Sample( name =  "Sh_NNPDF30NNLO_Zmumu_Pt500_700_CFiltBVet",    xsec =  0.011157277  )
Sh_NNPDF30NNLO_Zmumu_Pt700_1000_CFiltBVet   = Sample( name =  "Sh_NNPDF30NNLO_Zmumu_Pt700_1000_CFiltBVet",   xsec =  0.002053806  )
Sh_NNPDF30NNLO_Zmumu_Pt1000_2000_CFiltBVet  = Sample( name =  "Sh_NNPDF30NNLO_Zmumu_Pt1000_2000_CFiltBVet",  xsec =  0.000265446  )
                                                                                                        
Sh_NNPDF30NNLO_Zmumu_Pt0_70_BFilter         = Sample( name =  "Sh_NNPDF30NNLO_Zmumu_Pt0_70_BFilter",         xsec =  158.199011129)
Sh_NNPDF30NNLO_Zmumu_Pt70_140_BFilter       = Sample( name =  "Sh_NNPDF30NNLO_Zmumu_Pt70_140_BFilter",       xsec =  8.937479488  )
Sh_NNPDF30NNLO_Zmumu_Pt140_280_BFilter      = Sample( name =  "Sh_NNPDF30NNLO_Zmumu_Pt140_280_BFilter",      xsec =  1.554540292  )
Sh_NNPDF30NNLO_Zmumu_Pt280_500_BFilter      = Sample( name =  "Sh_NNPDF30NNLO_Zmumu_Pt280_500_BFilter",      xsec =  0.113373913  )
Sh_NNPDF30NNLO_Zmumu_Pt500_700_BFilter      = Sample( name =  "Sh_NNPDF30NNLO_Zmumu_Pt500_700_BFilter",      xsec =  0.007371738  )
Sh_NNPDF30NNLO_Zmumu_Pt700_1000_BFilter     = Sample( name =  "Sh_NNPDF30NNLO_Zmumu_Pt700_1000_BFilter",     xsec =  0.001297194  )
Sh_NNPDF30NNLO_Zmumu_Pt1000_2000_BFilter    = Sample( name =  "Sh_NNPDF30NNLO_Zmumu_Pt1000_2000_BFilter",    xsec =  0.000190262  )

Zmumu = Sample( name =   'Zmumu',
                  tlatex = 'Z #rightarrow #mu#mu+jets',
                  fill_color = ROOT.kSpring+1,
                  line_color =  ROOT.kSpring+2,
                  marker_color =  ROOT.kSpring+2,
                  daughters = [
                               Sh_NNPDF30NNLO_Zmumu_Pt0_70_CVetoBVeto,        
                               Sh_NNPDF30NNLO_Zmumu_Pt70_140_CVetoBVeto,                                    
                               #Sh_NNPDF30NNLO_Zmumu_Pt140_280_CVetoBVeto,     missing !!!
                               #Sh_NNPDF30NNLO_Zmumu_Pt280_500_CVetoBVeto,     
                               #Sh_NNPDF30NNLO_Zmumu_Pt500_700_CVetoBVeto,     
                               #Sh_NNPDF30NNLO_Zmumu_Pt700_1000_CVetoBVeto,    
                               #Sh_NNPDF30NNLO_Zmumu_Pt1000_2000_CVetoBVeto,   
                               #Sh_NNPDF30NNLO_Zmumu_Pt0_70_CFiltBVet,      
                               Sh_NNPDF30NNLO_Zmumu_Pt70_140_CFiltBVet,    
                               Sh_NNPDF30NNLO_Zmumu_Pt140_280_CFiltBVet,   
                               Sh_NNPDF30NNLO_Zmumu_Pt280_500_CFiltBVet,   
                               Sh_NNPDF30NNLO_Zmumu_Pt500_700_CFiltBVet,   
                               #Sh_NNPDF30NNLO_Zmumu_Pt700_1000_CFiltBVet,  
                               #Sh_NNPDF30NNLO_Zmumu_Pt1000_2000_CFiltBVet, 
                               Sh_NNPDF30NNLO_Zmumu_Pt0_70_BFilter,           
                               Sh_NNPDF30NNLO_Zmumu_Pt70_140_BFilter,         
                               Sh_NNPDF30NNLO_Zmumu_Pt140_280_BFilter,        
                               Sh_NNPDF30NNLO_Zmumu_Pt280_500_BFilter,        
                               Sh_NNPDF30NNLO_Zmumu_Pt500_700_BFilter,        
                               Sh_NNPDF30NNLO_Zmumu_Pt700_1000_BFilter,       
                               Sh_NNPDF30NNLO_Zmumu_Pt1000_2000_BFilter,      
                              ],
                ) 

#---------
# Ztautau
#---------

Sh_NNPDF30NNLO_Ztt_Pt0_70_CVetoBVeto      = Sample( name =  "Sh_NNPDF30NNLO_Ztt_Pt0_70_CVetoBVeto",      xsec = 1540.4178651 )
Sh_NNPDF30NNLO_Ztt_Pt70_140_CVetoBVeto    = Sample( name =  "Sh_NNPDF30NNLO_Ztt_Pt70_140_CVetoBVeto",    xsec = 44.65676361  ) 
Sh_NNPDF30NNLO_Ztt_Pt140_280_CVetoBVeto   = Sample( name =  "Sh_NNPDF30NNLO_Ztt_Pt140_280_CVetoBVeto",   xsec = 6.455693712  )
Sh_NNPDF30NNLO_Ztt_Pt280_500_CVetoBVeto   = Sample( name =  "Sh_NNPDF30NNLO_Ztt_Pt280_500_CVetoBVeto",   xsec = 0.401065     )
Sh_NNPDF30NNLO_Ztt_Pt500_700_CVetoBVeto   = Sample( name =  "Sh_NNPDF30NNLO_Ztt_Pt500_700_CVetoBVeto",   xsec = 0.02348807   )
Sh_NNPDF30NNLO_Ztt_Pt700_1000_CVetoBVeto  = Sample( name =  "Sh_NNPDF30NNLO_Ztt_Pt700_1000_CVetoBVeto",  xsec = 0.004107715  )
Sh_NNPDF30NNLO_Ztt_Pt1000_2000_CVetoBVeto = Sample( name =  "Sh_NNPDF30NNLO_Ztt_Pt1000_2000_CVetoBVeto", xsec = 0.000532212  )
                                                                                                        
Sh_NNPDF30NNLO_Ztt_Pt0_70_CFiltBVet       = Sample( name =  "Sh_NNPDF30NNLO_Ztt_Pt0_70_CFiltBVet",       xsec = 282.756352896)
Sh_NNPDF30NNLO_Ztt_Pt70_140_CFiltBVet     = Sample( name =  "Sh_NNPDF30NNLO_Ztt_Pt70_140_CFiltBVet",     xsec = 15.209340192 )
Sh_NNPDF30NNLO_Ztt_Pt140_280_CFiltBVet    = Sample( name =  "Sh_NNPDF30NNLO_Ztt_Pt140_280_CFiltBVet",    xsec = 2.529223599  )
Sh_NNPDF30NNLO_Ztt_Pt280_500_CFiltBVet    = Sample( name =  "Sh_NNPDF30NNLO_Ztt_Pt280_500_CFiltBVet",    xsec = 0.176406172  )
Sh_NNPDF30NNLO_Ztt_Pt500_700_CFiltBVet    = Sample( name =  "Sh_NNPDF30NNLO_Ztt_Pt500_700_CFiltBVet",    xsec = 0.011224933  )
Sh_NNPDF30NNLO_Ztt_Pt700_1000_CFiltBVet   = Sample( name =  "Sh_NNPDF30NNLO_Ztt_Pt700_1000_CFiltBVet",   xsec = 0.002156445  )
Sh_NNPDF30NNLO_Ztt_Pt1000_2000_CFiltBVet  = Sample( name =  "Sh_NNPDF30NNLO_Ztt_Pt1000_2000_CFiltBVet",  xsec = 0.000329597  )
                                                                                                        
Sh_NNPDF30NNLO_Ztt_Pt0_70_BFilter         = Sample( name =  "Sh_NNPDF30NNLO_Ztt_Pt0_70_BFilter",         xsec = 157.407818354)
Sh_NNPDF30NNLO_Ztt_Pt70_140_BFilter       = Sample( name =  "Sh_NNPDF30NNLO_Ztt_Pt70_140_BFilter",       xsec = 8.971250612  )
Sh_NNPDF30NNLO_Ztt_Pt140_280_BFilter      = Sample( name =  "Sh_NNPDF30NNLO_Ztt_Pt140_280_BFilter",      xsec = 1.494293679  )
Sh_NNPDF30NNLO_Ztt_Pt280_500_BFilter      = Sample( name =  "Sh_NNPDF30NNLO_Ztt_Pt280_500_BFilter",      xsec = 0.108832258  )
Sh_NNPDF30NNLO_Ztt_Pt500_700_BFilter      = Sample( name =  "Sh_NNPDF30NNLO_Ztt_Pt500_700_BFilter",      xsec = 0.007076053  )
Sh_NNPDF30NNLO_Ztt_Pt700_1000_BFilter     = Sample( name =  "Sh_NNPDF30NNLO_Ztt_Pt700_1000_BFilter",     xsec = 0.001318545  )
Sh_NNPDF30NNLO_Ztt_Pt1000_2000_BFilter    = Sample( name =  "Sh_NNPDF30NNLO_Ztt_Pt1000_2000_BFilter",    xsec = 0.000161628  )

Ztautau = Sample( name =   'Ztautau',
                  tlatex = 'Z #rightarrow #tau#tau+jets',
                  fill_color = ROOT.kAzure-4,
                  line_color =  ROOT.kAzure-5,
                  marker_color =  ROOT.kAzure-5,
                  daughters = [
                               Sh_NNPDF30NNLO_Ztt_Pt0_70_CVetoBVeto,        
                               Sh_NNPDF30NNLO_Ztt_Pt70_140_CVetoBVeto,                                    
                               #Sh_NNPDF30NNLO_Ztt_Pt140_280_CVetoBVeto,     
                               Sh_NNPDF30NNLO_Ztt_Pt280_500_CVetoBVeto,     
                               Sh_NNPDF30NNLO_Ztt_Pt500_700_CVetoBVeto,     
                               Sh_NNPDF30NNLO_Ztt_Pt700_1000_CVetoBVeto,    
                               #Sh_NNPDF30NNLO_Ztt_Pt1000_2000_CVetoBVeto,   
                               Sh_NNPDF30NNLO_Ztt_Pt0_70_CFiltBVet,      
                               Sh_NNPDF30NNLO_Ztt_Pt70_140_CFiltBVet,    
                               Sh_NNPDF30NNLO_Ztt_Pt140_280_CFiltBVet,   
                               Sh_NNPDF30NNLO_Ztt_Pt280_500_CFiltBVet,   
                               Sh_NNPDF30NNLO_Ztt_Pt500_700_CFiltBVet,   
                               Sh_NNPDF30NNLO_Ztt_Pt700_1000_CFiltBVet,  
                               Sh_NNPDF30NNLO_Ztt_Pt1000_2000_CFiltBVet, 
                               Sh_NNPDF30NNLO_Ztt_Pt0_70_BFilter,           
                               Sh_NNPDF30NNLO_Ztt_Pt70_140_BFilter,         
                               Sh_NNPDF30NNLO_Ztt_Pt140_280_BFilter,        
                               Sh_NNPDF30NNLO_Ztt_Pt280_500_BFilter, 
                               Sh_NNPDF30NNLO_Ztt_Pt500_700_BFilter,        
                               Sh_NNPDF30NNLO_Ztt_Pt700_1000_BFilter,       
                               Sh_NNPDF30NNLO_Ztt_Pt1000_2000_BFilter,      
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

#-----------
# ttbar
#-----------
PoPy_P2012_ttb_nonallh           = Sample( name =  "PoPy_P2012_ttb_nonallh",             xsec = 696.11) #susy

top = Sample( name =   'top',
              tlatex = 'Top',
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
# data-driven backgrounds
#-------------------------------------------------------------------------------
fakes  = Sample( name         = "fakes",
                 tlatex       = "Fakes",
                 fill_color   = ROOT.kGreen+1,
                 line_color   = ROOT.kGreen+2,
                 marker_color = ROOT.kGreen+2,
                 type         = "datadriven",
                 )

sub_ztt = Sample( name 	      = "sub_ztt",
		 tlatex       = "Ztt (data - add ons)",
		 fill_color   = ROOT.kAzure-9,
		 line_color   = ROOT.kBlack,
		 marker_color = ROOT.kAzure-9,
		 type	      = "datadriven",
		 )

sub_ztt_1Track = Sample( name = "sub_ztt_1Track",
		 tlatex       = "Ztt (data - add ons)",
		 fill_color   = ROOT.kAzure-9,
		 line_color   = ROOT.kBlack,
		 marker_color = ROOT.kAzure-9,
		 type	      = "datadriven",
		 )

sub_ztt_3Track = Sample( name = "sub_ztt_3Track",
		 tlatex       = "Ztt (data - add ons)",
		 fill_color   = ROOT.kAzure-9,
		 line_color   = ROOT.kBlack,
		 marker_color = ROOT.kAzure-9,
		 type	      = "datadriven",
		 )

sub_ztt_25med = Sample( name 	      = "sub_ztt_25med",
		 tlatex       = "Ztt (data - add ons)",
		 fill_color   = ROOT.kAzure-9,
		 line_color   = ROOT.kBlack,
		 marker_color = ROOT.kAzure-9,
		 type	      = "datadriven",
		 )

sub_ztt_25med_1Track = Sample( name 	      = "sub_ztt_25med_1Track",
		 tlatex       = "Ztt (data - add ons)",
		 fill_color   = ROOT.kAzure-9,
		 line_color   = ROOT.kBlack,
		 marker_color = ROOT.kAzure-9,
		 type	      = "datadriven",
		 )

sub_ztt_25med_3Track = Sample( name 	      = "sub_ztt_25med_3Track",
		 tlatex       = "Ztt (data - add ons)",
		 fill_color   = ROOT.kAzure-9,
		 line_color   = ROOT.kBlack,
		 marker_color = ROOT.kAzure-9,
		 type	      = "datadriven",
		 )

sub_ztt_35med = Sample( name 	      = "sub_ztt_35med",
		 tlatex       = "Ztt (data - add ons)",
		 fill_color   = ROOT.kAzure-9,
		 line_color   = ROOT.kBlack,
		 marker_color = ROOT.kAzure-9,
		 type	      = "datadriven",
		 )

sub_ztt_35med_1Track = Sample( name 	      = "sub_ztt_35med_1Track",
		 tlatex       = "Ztt (data - add ons)",
		 fill_color   = ROOT.kAzure-9,
		 line_color   = ROOT.kBlack,
		 marker_color = ROOT.kAzure-9,
		 type	      = "datadriven",
		 )

sub_ztt_35med_3Track = Sample( name 	      = "sub_ztt_35med_3Track",
		 tlatex       = "Ztt (data - add ons)",
		 fill_color   = ROOT.kAzure-9,
		 line_color   = ROOT.kBlack,
		 marker_color = ROOT.kAzure-9,
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
                 tlatex       = Wjets.tlatex+"(OS-SS)",
                 fill_color   = Wjets.fill_color,
                 line_color   = Wjets.line_color,
                 marker_color = Wjets.marker_color,
                 type         = "datadriven",
                 )

addon_Zlljets = Sample( name   = Zlljets.name,
                 tlatex       = Zlljets.tlatex+"(OS-SS)",
                 fill_color   = Zlljets.fill_color,
                 line_color   = Zlljets.line_color,
                 marker_color = Zlljets.marker_color,
                 type         = "datadriven",
                 )

addon_Zttjets = Sample( name   = Zttjets.name,
                 tlatex       = Zttjets.tlatex+"(OS-SS)",
                 fill_color   = Zttjets.fill_color,
                 line_color   = Zttjets.line_color,
                 marker_color = Zttjets.marker_color,
                 type         = "datadriven",
                 )

addon_top = Sample( name   = top.name,
                 tlatex       = top.tlatex+"(OS-SS)",
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
                 tlatex       = Wjets.tlatex+"(OS-SS)",
                 fill_color   = Wjets.fill_color,
                 line_color   = Wjets.line_color,
                 marker_color = Wjets.marker_color,
                 type         = "datadriven",
                 )

addon_Zlljets_25med = Sample( name   = Zlljets.name,
                 tlatex       = Zlljets.tlatex+"(OS-SS)",
                 fill_color   = Zlljets.fill_color,
                 line_color   = Zlljets.line_color,
                 marker_color = Zlljets.marker_color,
                 type         = "datadriven",
                 )

addon_Zttjets_25med = Sample( name   = Zttjets.name,
                 tlatex       = Zttjets.tlatex+"(OS-SS)",
                 fill_color   = Zttjets.fill_color,
                 line_color   = Zttjets.line_color,
                 marker_color = Zttjets.marker_color,
                 type         = "datadriven",
                 )

addon_top_25med = Sample( name   = top.name,
                 tlatex       = top.tlatex+"(OS-SS)",
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
                 tlatex       = Wjets.tlatex+"(OS-SS)",
                 fill_color   = Wjets.fill_color,
                 line_color   = Wjets.line_color,
                 marker_color = Wjets.marker_color,
                 type         = "datadriven",
                 )

addon_Zlljets_25med_lowPT = Sample( name   = Zlljets.name,
                 tlatex       = Zlljets.tlatex+"(OS-SS)",
                 fill_color   = Zlljets.fill_color,
                 line_color   = Zlljets.line_color,
                 marker_color = Zlljets.marker_color,
                 type         = "datadriven",
                 )

addon_Zttjets_25med_lowPT = Sample( name   = Zttjets.name,
                 tlatex       = Zttjets.tlatex+"(OS-SS)",
                 fill_color   = Zttjets.fill_color,
                 line_color   = Zttjets.line_color,
                 marker_color = Zttjets.marker_color,
                 type         = "datadriven",
                 )

addon_top_25med_lowPT = Sample( name   = top.name,
                 tlatex       = top.tlatex+"(OS-SS)",
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
                 tlatex       = Wjets.tlatex+"(OS-SS)",
                 fill_color   = Wjets.fill_color,
                 line_color   = Wjets.line_color,
                 marker_color = Wjets.marker_color,
                 type         = "datadriven",
                 )

addon_Zlljets_25med_highPT = Sample( name   = Zlljets.name,
                 tlatex       = Zlljets.tlatex+"(OS-SS)",
                 fill_color   = Zlljets.fill_color,
                 line_color   = Zlljets.line_color,
                 marker_color = Zlljets.marker_color,
                 type         = "datadriven",
                 )

addon_Zttjets_25med_highPT = Sample( name   = Zttjets.name,
                 tlatex       = Zttjets.tlatex+"(OS-SS)",
                 fill_color   = Zttjets.fill_color,
                 line_color   = Zttjets.line_color,
                 marker_color = Zttjets.marker_color,
                 type         = "datadriven",
                 )

addon_top_25med_highPT = Sample( name   = top.name,
                 tlatex       = top.tlatex+"(OS-SS)",
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
                 tlatex       = Wjets.tlatex+"(OS-SS)",
                 fill_color   = Wjets.fill_color,
                 line_color   = Wjets.line_color,
                 marker_color = Wjets.marker_color,
                 type         = "datadriven",
                 )

addon_Zlljets_35med = Sample( name   = Zlljets.name,
                 tlatex       = Zlljets.tlatex+"(OS-SS)",
                 fill_color   = Zlljets.fill_color,
                 line_color   = Zlljets.line_color,
                 marker_color = Zlljets.marker_color,
                 type         = "datadriven",
                 )

addon_Zttjets_35med = Sample( name   = Zttjets.name,
                 tlatex       = Zttjets.tlatex+"(OS-SS)",
                 fill_color   = Zttjets.fill_color,
                 line_color   = Zttjets.line_color,
                 marker_color = Zttjets.marker_color,
                 type         = "datadriven",
                 )

addon_top_35med = Sample( name   = top.name,
                 tlatex       = top.tlatex+"(OS-SS)",
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
                 tlatex       = Wjets.tlatex+"(OS-SS)",
                 fill_color   = Wjets.fill_color,
                 line_color   = Wjets.line_color,
                 marker_color = Wjets.marker_color,
                 type         = "datadriven",
                 )

addon_Zlljets_35med_lowPT = Sample( name   = Zlljets.name,
                 tlatex       = Zlljets.tlatex+"(OS-SS)",
                 fill_color   = Zlljets.fill_color,
                 line_color   = Zlljets.line_color,
                 marker_color = Zlljets.marker_color,
                 type         = "datadriven",
                 )

addon_Zttjets_35med_lowPT = Sample( name   = Zttjets.name,
                 tlatex       = Zttjets.tlatex+"(OS-SS)",
                 fill_color   = Zttjets.fill_color,
                 line_color   = Zttjets.line_color,
                 marker_color = Zttjets.marker_color,
                 type         = "datadriven",
                 )

addon_top_35med_lowPT = Sample( name   = top.name,
                 tlatex       = top.tlatex+"(OS-SS)",
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
                 tlatex       = Wjets.tlatex+"(OS-SS)",
                 fill_color   = Wjets.fill_color,
                 line_color   = Wjets.line_color,
                 marker_color = Wjets.marker_color,
                 type         = "datadriven",
                 )

addon_Zlljets_35med_highPT = Sample( name   = Zlljets.name,
                 tlatex       = Zlljets.tlatex+"(OS-SS)",
                 fill_color   = Zlljets.fill_color,
                 line_color   = Zlljets.line_color,
                 marker_color = Zlljets.marker_color,
                 type         = "datadriven",
                 )

addon_Zttjets_35med_highPT = Sample( name   = Zttjets.name,
                 tlatex       = Zttjets.tlatex+"(OS-SS)",
                 fill_color   = Zttjets.fill_color,
                 line_color   = Zttjets.line_color,
                 marker_color = Zttjets.marker_color,
                 type         = "datadriven",
                 )

addon_top_35med_highPT = Sample( name   = top.name,
                 tlatex       = top.tlatex+"(OS-SS)",
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
                 tlatex       = Wjets.tlatex+"(OS-SS)",
                 fill_color   = Wjets.fill_color,
                 line_color   = Wjets.line_color,
                 marker_color = Wjets.marker_color,
                 type         = "datadriven",
                 )

addon_Zlljets_1Track = Sample( name   = Zlljets.name,
                 tlatex       = Zlljets.tlatex+"(OS-SS)",
                 fill_color   = Zlljets.fill_color,
                 line_color   = Zlljets.line_color,
                 marker_color = Zlljets.marker_color,
                 type         = "datadriven",
                 )

addon_Zttjets_1Track = Sample( name   = Zttjets.name,
                 tlatex       = Zttjets.tlatex+"(OS-SS)",
                 fill_color   = Zttjets.fill_color,
                 line_color   = Zttjets.line_color,
                 marker_color = Zttjets.marker_color,
                 type         = "datadriven",
                 )

addon_top_1Track = Sample( name   = top.name,
                 tlatex       = top.tlatex+"(OS-SS)",
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
                 tlatex       = Wjets.tlatex+"(OS-SS)",
                 fill_color   = Wjets.fill_color,
                 line_color   = Wjets.line_color,
                 marker_color = Wjets.marker_color,
                 type         = "datadriven",
                 )

addon_Zlljets_25med_1Track = Sample( name   = Zlljets.name,
                 tlatex       = Zlljets.tlatex+"(OS-SS)",
                 fill_color   = Zlljets.fill_color,
                 line_color   = Zlljets.line_color,
                 marker_color = Zlljets.marker_color,
                 type         = "datadriven",
                 )

addon_Zttjets_25med_1Track = Sample( name   = Zttjets.name,
                 tlatex       = Zttjets.tlatex+"(OS-SS)",
                 fill_color   = Zttjets.fill_color,
                 line_color   = Zttjets.line_color,
                 marker_color = Zttjets.marker_color,
                 type         = "datadriven",
                 )

addon_top_25med_1Track = Sample( name   = top.name,
                 tlatex       = top.tlatex+"(OS-SS)",
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
                 tlatex       = Wjets.tlatex+"(OS-SS)",
                 fill_color   = Wjets.fill_color,
                 line_color   = Wjets.line_color,
                 marker_color = Wjets.marker_color,
                 type         = "datadriven",
                 )

addon_Zlljets_25med_lowPT_1Track = Sample( name   = Zlljets.name,
                 tlatex       = Zlljets.tlatex+"(OS-SS)",
                 fill_color   = Zlljets.fill_color,
                 line_color   = Zlljets.line_color,
                 marker_color = Zlljets.marker_color,
                 type         = "datadriven",
                 )

addon_Zttjets_25med_lowPT_1Track = Sample( name   = Zttjets.name,
                 tlatex       = Zttjets.tlatex+"(OS-SS)",
                 fill_color   = Zttjets.fill_color,
                 line_color   = Zttjets.line_color,
                 marker_color = Zttjets.marker_color,
                 type         = "datadriven",
                 )

addon_top_25med_lowPT_1Track = Sample( name   = top.name,
                 tlatex       = top.tlatex+"(OS-SS)",
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
                 tlatex       = Wjets.tlatex+"(OS-SS)",
                 fill_color   = Wjets.fill_color,
                 line_color   = Wjets.line_color,
                 marker_color = Wjets.marker_color,
                 type         = "datadriven",
                 )

addon_Zlljets_25med_highPT_1Track = Sample( name   = Zlljets.name,
                 tlatex       = Zlljets.tlatex+"(OS-SS)",
                 fill_color   = Zlljets.fill_color,
                 line_color   = Zlljets.line_color,
                 marker_color = Zlljets.marker_color,
                 type         = "datadriven",
                 )

addon_Zttjets_25med_highPT_1Track = Sample( name   = Zttjets.name,
                 tlatex       = Zttjets.tlatex+"(OS-SS)",
                 fill_color   = Zttjets.fill_color,
                 line_color   = Zttjets.line_color,
                 marker_color = Zttjets.marker_color,
                 type         = "datadriven",
                 )

addon_top_25med_highPT_1Track = Sample( name   = top.name,
                 tlatex       = top.tlatex+"(OS-SS)",
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
                 tlatex       = Wjets.tlatex+"(OS-SS)",
                 fill_color   = Wjets.fill_color,
                 line_color   = Wjets.line_color,
                 marker_color = Wjets.marker_color,
                 type         = "datadriven",
                 )

addon_Zlljets_35med_1Track = Sample( name   = Zlljets.name,
                 tlatex       = Zlljets.tlatex+"(OS-SS)",
                 fill_color   = Zlljets.fill_color,
                 line_color   = Zlljets.line_color,
                 marker_color = Zlljets.marker_color,
                 type         = "datadriven",
                 )

addon_Zttjets_35med_1Track = Sample( name   = Zttjets.name,
                 tlatex       = Zttjets.tlatex+"(OS-SS)",
                 fill_color   = Zttjets.fill_color,
                 line_color   = Zttjets.line_color,
                 marker_color = Zttjets.marker_color,
                 type         = "datadriven",
                 )

addon_top_35med_1Track = Sample( name   = top.name,
                 tlatex       = top.tlatex+"(OS-SS)",
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
                 tlatex       = Wjets.tlatex+"(OS-SS)",
                 fill_color   = Wjets.fill_color,
                 line_color   = Wjets.line_color,
                 marker_color = Wjets.marker_color,
                 type         = "datadriven",
                 )

addon_Zlljets_35med_lowPT_1Track = Sample( name   = Zlljets.name,
                 tlatex       = Zlljets.tlatex+"(OS-SS)",
                 fill_color   = Zlljets.fill_color,
                 line_color   = Zlljets.line_color,
                 marker_color = Zlljets.marker_color,
                 type         = "datadriven",
                 )

addon_Zttjets_35med_lowPT_1Track = Sample( name   = Zttjets.name,
                 tlatex       = Zttjets.tlatex+"(OS-SS)",
                 fill_color   = Zttjets.fill_color,
                 line_color   = Zttjets.line_color,
                 marker_color = Zttjets.marker_color,
                 type         = "datadriven",
                 )

addon_top_35med_lowPT_1Track = Sample( name   = top.name,
                 tlatex       = top.tlatex+"(OS-SS)",
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
                 tlatex       = Wjets.tlatex+"(OS-SS)",
                 fill_color   = Wjets.fill_color,
                 line_color   = Wjets.line_color,
                 marker_color = Wjets.marker_color,
                 type         = "datadriven",
                 )

addon_Zlljets_35med_highPT_1Track = Sample( name   = Zlljets.name,
                 tlatex       = Zlljets.tlatex+"(OS-SS)",
                 fill_color   = Zlljets.fill_color,
                 line_color   = Zlljets.line_color,
                 marker_color = Zlljets.marker_color,
                 type         = "datadriven",
                 )

addon_Zttjets_35med_highPT_1Track = Sample( name   = Zttjets.name,
                 tlatex       = Zttjets.tlatex+"(OS-SS)",
                 fill_color   = Zttjets.fill_color,
                 line_color   = Zttjets.line_color,
                 marker_color = Zttjets.marker_color,
                 type         = "datadriven",
                 )

addon_top_35med_highPT_1Track = Sample( name   = top.name,
                 tlatex       = top.tlatex+"(OS-SS)",
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
                 tlatex       = Wjets.tlatex+"(OS-SS)",
                 fill_color   = Wjets.fill_color,
                 line_color   = Wjets.line_color,
                 marker_color = Wjets.marker_color,
                 type         = "datadriven",
                 )

addon_Zlljets_3Track = Sample( name   = Zlljets.name,
                 tlatex       = Zlljets.tlatex+"(OS-SS)",
                 fill_color   = Zlljets.fill_color,
                 line_color   = Zlljets.line_color,
                 marker_color = Zlljets.marker_color,
                 type         = "datadriven",
                 )

addon_Zttjets_3Track = Sample( name   = Zttjets.name,
                 tlatex       = Zttjets.tlatex+"(OS-SS)",
                 fill_color   = Zttjets.fill_color,
                 line_color   = Zttjets.line_color,
                 marker_color = Zttjets.marker_color,
                 type         = "datadriven",
                 )

addon_top_3Track = Sample( name   = top.name,
                 tlatex       = top.tlatex+"(OS-SS)",
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
                 tlatex       = Wjets.tlatex+"(OS-SS)",
                 fill_color   = Wjets.fill_color,
                 line_color   = Wjets.line_color,
                 marker_color = Wjets.marker_color,
                 type         = "datadriven",
                 )

addon_Zlljets_25med_3Track = Sample( name   = Zlljets.name,
                 tlatex       = Zlljets.tlatex+"(OS-SS)",
                 fill_color   = Zlljets.fill_color,
                 line_color   = Zlljets.line_color,
                 marker_color = Zlljets.marker_color,
                 type         = "datadriven",
                 )

addon_Zttjets_25med_3Track = Sample( name   = Zttjets.name,
                 tlatex       = Zttjets.tlatex+"(OS-SS)",
                 fill_color   = Zttjets.fill_color,
                 line_color   = Zttjets.line_color,
                 marker_color = Zttjets.marker_color,
                 type         = "datadriven",
                 )

addon_top_25med_3Track = Sample( name   = top.name,
                 tlatex       = top.tlatex+"(OS-SS)",
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
                 tlatex       = Wjets.tlatex+"(OS-SS)",
                 fill_color   = Wjets.fill_color,
                 line_color   = Wjets.line_color,
                 marker_color = Wjets.marker_color,
                 type         = "datadriven",
                 )

addon_Zlljets_25med_lowPT_3Track = Sample( name   = Zlljets.name,
                 tlatex       = Zlljets.tlatex+"(OS-SS)",
                 fill_color   = Zlljets.fill_color,
                 line_color   = Zlljets.line_color,
                 marker_color = Zlljets.marker_color,
                 type         = "datadriven",
                 )

addon_Zttjets_25med_lowPT_3Track = Sample( name   = Zttjets.name,
                 tlatex       = Zttjets.tlatex+"(OS-SS)",
                 fill_color   = Zttjets.fill_color,
                 line_color   = Zttjets.line_color,
                 marker_color = Zttjets.marker_color,
                 type         = "datadriven",
                 )

addon_top_25med_lowPT_3Track = Sample( name   = top.name,
                 tlatex       = top.tlatex+"(OS-SS)",
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
                 tlatex       = Wjets.tlatex+"(OS-SS)",
                 fill_color   = Wjets.fill_color,
                 line_color   = Wjets.line_color,
                 marker_color = Wjets.marker_color,
                 type         = "datadriven",
                 )

addon_Zlljets_25med_highPT_3Track = Sample( name   = Zlljets.name,
                 tlatex       = Zlljets.tlatex+"(OS-SS)",
                 fill_color   = Zlljets.fill_color,
                 line_color   = Zlljets.line_color,
                 marker_color = Zlljets.marker_color,
                 type         = "datadriven",
                 )

addon_Zttjets_25med_highPT_3Track = Sample( name   = Zttjets.name,
                 tlatex       = Zttjets.tlatex+"(OS-SS)",
                 fill_color   = Zttjets.fill_color,
                 line_color   = Zttjets.line_color,
                 marker_color = Zttjets.marker_color,
                 type         = "datadriven",
                 )

addon_top_25med_highPT_3Track = Sample( name   = top.name,
                 tlatex       = top.tlatex+"(OS-SS)",
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
                 tlatex       = Wjets.tlatex+"(OS-SS)",
                 fill_color   = Wjets.fill_color,
                 line_color   = Wjets.line_color,
                 marker_color = Wjets.marker_color,
                 type         = "datadriven",
                 )

addon_Zlljets_35med_3Track = Sample( name   = Zlljets.name,
                 tlatex       = Zlljets.tlatex+"(OS-SS)",
                 fill_color   = Zlljets.fill_color,
                 line_color   = Zlljets.line_color,
                 marker_color = Zlljets.marker_color,
                 type         = "datadriven",
                 )

addon_Zttjets_35med_3Track = Sample( name   = Zttjets.name,
                 tlatex       = Zttjets.tlatex+"(OS-SS)",
                 fill_color   = Zttjets.fill_color,
                 line_color   = Zttjets.line_color,
                 marker_color = Zttjets.marker_color,
                 type         = "datadriven",
                 )

addon_top_35med_3Track = Sample( name   = top.name,
                 tlatex       = top.tlatex+"(OS-SS)",
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
                 tlatex       = Wjets.tlatex+"(OS-SS)",
                 fill_color   = Wjets.fill_color,
                 line_color   = Wjets.line_color,
                 marker_color = Wjets.marker_color,
                 type         = "datadriven",
                 )

addon_Zlljets_35med_lowPT_3Track = Sample( name   = Zlljets.name,
                 tlatex       = Zlljets.tlatex+"(OS-SS)",
                 fill_color   = Zlljets.fill_color,
                 line_color   = Zlljets.line_color,
                 marker_color = Zlljets.marker_color,
                 type         = "datadriven",
                 )

addon_Zttjets_35med_lowPT_3Track = Sample( name   = Zttjets.name,
                 tlatex       = Zttjets.tlatex+"(OS-SS)",
                 fill_color   = Zttjets.fill_color,
                 line_color   = Zttjets.line_color,
                 marker_color = Zttjets.marker_color,
                 type         = "datadriven",
                 )

addon_top_35med_lowPT_3Track = Sample( name   = top.name,
                 tlatex       = top.tlatex+"(OS-SS)",
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
                 tlatex       = Wjets.tlatex+"(OS-SS)",
                 fill_color   = Wjets.fill_color,
                 line_color   = Wjets.line_color,
                 marker_color = Wjets.marker_color,
                 type         = "datadriven",
                 )

addon_Zlljets_35med_highPT_3Track = Sample( name   = Zlljets.name,
                 tlatex       = Zlljets.tlatex+"(OS-SS)",
                 fill_color   = Zlljets.fill_color,
                 line_color   = Zlljets.line_color,
                 marker_color = Zlljets.marker_color,
                 type         = "datadriven",
                 )

addon_Zttjets_35med_highPT_3Track = Sample( name   = Zttjets.name,
                 tlatex       = Zttjets.tlatex+"(OS-SS)",
                 fill_color   = Zttjets.fill_color,
                 line_color   = Zttjets.line_color,
                 marker_color = Zttjets.marker_color,
                 type         = "datadriven",
                 )

addon_top_35med_highPT_3Track = Sample( name   = top.name,
                 tlatex       = top.tlatex+"(OS-SS)",
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

addon_Zttjets_highPT_3Track = Sample( name   = Zttjets.name,
                 tlatex       = Zttjets.tlatex+"(OS-SS)_highPT",
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
all_mc += top.daughters
all_mc += Wenujets.daughters
all_mc += Wmunujets.daughters
all_mc += Zeejets.daughters
all_mc += Zmumujets.daughters
all_mc += Zttjets.daughters

## EOF
