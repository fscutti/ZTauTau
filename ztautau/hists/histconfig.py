from hists import *


"""
This contains the histogram
configuration. Do not create
other config files !!!
"""


# -------
# event
# -------
h_NPV = Hist1D( hname  = "h_NPV",
                              xtitle = "NPV",
                              ytitle = "Events", 
                              nbins  = 35,
                              xmin   = 0.,
                              xmax   = 35.0,
                              dir    = "event",
                              vexpr  = "self.chain.NPV",
                            )

# -------
# jets
# -------
h_jetlead_pt  = Hist1D( hname  = "h_jetlead_pt",
                              xtitle = "p_{T}(jet_{lead}) [GeV]",
                              ytitle = "Events / (1 GeV)", 
                              nbins  = 2000,
                              xmin   = 0.0,
                              xmax   = 2000.0,
                              dir    = "jets",
                              vexpr  = "self.store['jets'][0].tlv.Pt()/GeV",
                            )


# -------
# muons
# -------

# mulead
# ------
h_mulead_pt = Hist1D( hname  = "h_mulead_pt",
                              xtitle = "p_{T}(#mu_{lead}) [GeV]",
                              ytitle = "Events / (1 GeV)", 
                              nbins  = 2000,
                              xmin   = 0.0,
                              xmax   = 2000.0,
                              dir    = "muons",
                              vexpr  = "self.store['muons'][0].tlv.Pt() / GeV",
                            )


# -------------
# tag and probe
# -------------
h_tag_pt = Hist1D( hname  = "h_tag_pt",
                              xtitle = "p_{T}(#mu_{tag}) [GeV]",
                              ytitle = "Events / (1 GeV)", 
                              nbins  = 2000,
                              xmin   = 0.0,
                              xmax   = 2000.0,
                              dir    = "muons",
                              vexpr  = "self.store['tag'].tlv.Pt() / GeV",
                            )


# -------
# MET
# -------
h_met_clus_et  = Hist1D( hname  = "h_met_clus_et",
                              xtitle = "E^{miss}_{T}(clus) [GeV]",
                              ytitle = "Events / (1 GeV)", 
                              nbins  = 2000,
                              xmin   = 0.,
                              xmax   = 2000.,
                              dir    = "met",
                              vexpr  = "self.store['met_clus'].tlv.Pt()/GeV",
                            )

# --------
# 2D hists
# --------
h_mulead_pt_jetlead_pt  = Hist2D( hname      = "h_mulead_pt_jetlead_pt",
                              xtitle  = "p_{T}(#mu_{lead}) [GeV]",
                              ytitle  = "p_{T}(jet_{lead}) [GeV]", 
                              nbinsx  = 1000,
                              xmin    = 0.,
                              xmax    = 1000.,
                              nbinsy  = 1000,
                              ymin    = 0.,
                              ymax    = 1000.,
                              dir     = "event",
                              vexpr   = " self.store['muons'][0].tlv.Pt() / GeV , self.store['jets'][0].tlv.Pt() / GeV",
                          )

# EOF
