from hists import *


"""
This contains the histogram
configuration. Do not create
other config files !!!
"""


# -------
# event
# -------
h_n_vx = Hist1D( hname  = "h_n_vx",
                              xtitle = "NPV",
                              ytitle = "Events", 
                              nbins  = 35,
                              xmin   = 0.,
                              xmax   = 35.0,
                              dir    = "event",
                              vexpr  = "self.chain.n_vx",
                            )

h_dummy = Hist1D( hname  = "h_dummy",
                              xtitle = "DUMMY",
                              ytitle = "Events", 
                              nbins  = 2000,
                              xmin   = 0.,
                              xmax   = 2000.0,
                              dir    = "event",
                              vexpr  = "self.store['dummy']",
                            )



# -------
# jets
# -------
h_jet_0_pt  = Hist1D( hname  = "h_jet_0_pt",
                              xtitle = "p_{T}(jet_{lead}) [GeV]",
                              ytitle = "Events / (1 GeV)", 
                              nbins  = 2000,
                              xmin   = 0.0,
                              xmax   = 2000.0,
                              dir    = "jets",
                              vexpr  = "self.chain.jet_0_pt",
                            )


# -------
# MET
# -------
h_met_reco_et  = Hist1D( hname  = "h_met_reco_et",
                              xtitle = "E^{miss}_{T}(reco) [GeV]",
                              ytitle = "Events / (1 GeV)", 
                              nbins  = 2000,
                              xmin   = 0.,
                              xmax   = 2000.,
                              dir    = "met",
                              vexpr  = "self.chain.met_reco_et",

                              )
"""
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

"""
# EOF
