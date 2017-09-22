from hists import *


"""
This contains the histogram
configuration. Do not create
other config files !!!
"""


###############
# TAU RELATED #
###############
h_tau0_eta         = Hist1D( 'tau_0_eta',                
                             title = '#eta(#tau)',                   
                             nbins = 1000, 
                             xmin = -6.0, 
                             xmax = 6.0, 
                             dir='tau', 
                             vexpr = 'self.chain.tau_0_eta',               
                             )

h_tau0_phi         = Hist1D( 'tau_0_phi',                
                             title = '#phi(#tau)',                   
                             nbins = 1000, 
                             xmin = -3.2, 
                             xmax = 3.2, 
                             dir='tau', 
                             vexpr = 'self.chain.tau_0_phi',               
                             )

h_tau0_pt          = Hist1D( 'tau_0_pt',                 
                             title = 'p_{T}(#tau)',                  
                             nbins = 1000, 
                             xmin = 0., 
                             xmax = 1000.0, 
                             dir='tau', 
                             vexpr = 'self.chain.tau_0_pt',                
                             )

###############
# LEP RELATED #
###############
h_lep0_eta         = Hist1D( 'lep_0_eta',                
                             title = '#eta(l)',                      
                             nbins = 1000, 
                             xmin = -6.0, 
                             xmax = 6.0, 
                             dir='lep', 
                             vexpr = 'self.chain.lep_0_eta',               
                             )

h_lep0_phi         = Hist1D( 'lep_0_phi',                
                             title = '#phi(l)',                      
                             nbins = 1000, 
                             xmin = -3.2, 
                             xmax = 3.2, 
                             dir='lep', 
                             vexpr = 'self.chain.lep_0_phi',               
                             )

h_lep0_pt          = Hist1D( 'lep_0_pt',                 
                             title = 'p_{T}(l)',                     
                             nbins = 1000, 
                             xmin = 0., 
                             xmax = 1000.0, 
                             dir='lep', 
                             vexpr = 'self.chain.lep_0_pt',                
                             )

##################
# LEPHAD RELATED #
##################
h_lh_vis_m         = Hist1D( 'lephad_vis_m', 
                             title = 'm_{vis}(#tau,l)',
                             nbins = 1000, 
                             xmin = 0., 
                             xmax = 1000.0, 
                             dir='lephad', 
                             vexpr = 'self.chain.lephad_vis_mass',         
                             )

h_lh_mmc_mlm_m     = Hist1D( 'lephad_lfv_mmc_mlm_m',
                             title = 'm^{mlm}_{MMC}(#tau,l)',
                             nbins = 1000, 
                             xmin = 0., 
                             xmax = 1000.0, 
                             dir='lephad', 
                             vexpr = 'self.chain.lephad_lfv_mmc_mlm_m', 
                             )

h_lh_mmc_maxw_m    = Hist1D( 'lephad_lfv_mmc_maxw_m', 
                             title = 'm^{maxw}_{MMC}(#tau,l)',
                             nbins = 1000, 
                             xmin = 0., 
                             xmax = 1000.0, 
                             dir='lephad', 
                             vexpr = 'self.chain.lephad_lfv_mmc_maxw_m',
                             )

h_lh_mmc_mlnu3p    = Hist1D( 'lephad_mmc_mlnu3p_m',
                             title = 'm^{mlnu3p}_{MMC}(#tau,l)',
                             nbins = 1000, 
                             xmin = 0., 
                             xmax = 1000.0, 
                             dir='lephad', 
                             vexpr = 'self.chain.lephad_mmc_mlnu3p_m',  
                             )

h_lh_coll_m        = Hist1D( 'coll_approx_lfv_m',
                             title = 'm_{Coll}(#tau,l)',
                             nbins = 1000, 
                             xmin = 0., 
                             xmax = 1000.0, 
                             dir='lephad', 
                             vexpr = 'self.chain.coll_approx_lfv_m',    
                             )

h_lh_coll_x0       = Hist1D( 'lephad_coll_approx_x0',
                             title = 'x0',
                             nbins = 1000, 
                             xmin = -2.0,
                             xmax = 2.0, 
                             dir='lephad', 
                             vexpr = 'self.chain.lephad_coll_approx_x0',   
                             )

h_lh_coll_x1 	   = Hist1D( 'lephad_coll_approx_x1',    
                             title = 'x1',                           
                             nbins = 1000, 
                             xmin = -2.0,
                             xmax = 2.0, 
                             dir='lephad', 
                             vexpr = 'self.chain.lephad_coll_approx_x1',   
                             )

h_lh_scdp          = Hist1D( 'lephad_met_sum_cos_dphi',  
                             title = '#Sigma cos(#Delta#phi)',       
                             nbins = 1000, 
                             xmin = -4.0, 
                             xmax = 4.0, 
                             dir='lephad', 
                             vexpr = 'self.chain.lephad_met_sum_cos_dphi', 
                             )

h_lh_lep_mt        = Hist1D( 'lephad_mt_lep_0_met',      
                             title = 'm_{T}(#l,MET)',                
                             nbins = 1000, 
                             xmin = 0., 
                             xmax = 1000.0, 
                             dir='lephad', 
                             vexpr = 'self.chain.lephad_mt_lep0_met',     
                             )

h_lh_tau_mt        = Hist1D( 'lephad_mt_tau_0_met',      
                             title = 'm_{T}(#tau,MET)',              
                             nbins = 1000, 
                             xmin = 0., 
                             xmax = 1000.0, 
                             dir='lephad', 
                             vexpr = 'self.chain.lephad_mt_lep1_met',     
                             )

h_lh_dR            = Hist1D( 'lephad_dr',                
                             title = '#Delta R(#tau,l)',             
                             nbins = 1000, 
                             xmin = 0., 
                             xmax = 6.0, 
                             dir='lephad', 
                             vexpr = 'self.chain.lephad_dr',               
                             )

h_lh_deta          = Hist1D( 'lephad_deta',              
                             title = '|#Delta #eta(#tau,l)|',        
                             nbins = 1000, 
                             xmin = 0., 
                             xmax = 6.0, 
                             dir='lephad', 
                             vexpr = 'self.chain.lephad_deta',             
                             )

h_lh_met_cent      = Hist1D( 'lephad_met_cent',          
                             title = 'E_{T}^{miss} #phi Centrality', 
                             nbins = 1000, 
                             xmin = -10.0, 
                             xmax = 10.0, 
                             dir='lephad', 
                             vexpr = 'self.chain.lephad_met_centrality',         
                             )

##################
# EVENTT RELATED #
##################
h_evt_nvx          = Hist1D( 'n_vx',
                             title = 'N_{vertex}',
                             nbins = 100, 
                             xmin = 0., 
                             xmax = 100.0, 
                             dir='event', 
                             vexpr = 'self.chain.n_vx',
                             )

h_evt_npvx         = Hist1D( 'n_pvx',
                             title = 'N_{Primary vertex}',
                             nbins = 100, 
                             xmin = 0., 
                             xmax = 100.0, 
                             dir='event', 
                             vexpr = 'self.chain.n_pvx',
                             )

h_evt_navgint      = Hist1D( 'n_avg_int',
                             title = '<#mu>',
                             nbins = 100, 
                             xmin = 0., 
                             xmax = 100.0, 
                             dir='event', 
                             vexpr = 'self.chain.n_avg_int',                   
                             )

h_evt_navgintcor   = Hist1D( 'n_avg_int_cor',
                             title = '<#mu>_{corrected}',
                             nbins = 100, 
                             xmin = 0., 
                             xmax = 100.0, 
                             dir='event', 
                             vexpr = 'self.chain.n_avg_int_cor',               
                             )

h_evt_n_jets       = Hist1D( 'n_jets',
                             title = 'N_{jets}',
                             nbins = 100, 
                             xmin = 0., 
                             xmax = 100.0, 
                             dir='event', 
                             vexpr = 'self.chain.n_jets',               
                             )

###############
# MET RELATED #
###############
h_met_reco_sumet   = Hist1D( 'met_reco_sumet',
                             title = 'MET #Sigma E_{t}',
                             nbins = 1000, 
                             xmin = 0., 
                             xmax = 1000.0, 
                             dir='met', 
                             vexpr = 'self.chain.met_reco_sumet',          
                             )

h_met_reco_etx     = Hist1D( 'met_reco_etx',
                             title = 'E_{x}^{miss}',
                             nbins = 1000, 
                             xmin = 0., 
                             xmax = 1000.0, 
                             dir='met', 
                             vexpr = 'self.chain.met_reco_etx',            
                             )

h_met_reco_ety     = Hist1D( 'met_reco_ety',
                             title = 'E_{y}^{miss}',
                             nbins = 1000, 
                             xmin = 0., 
                             xmax = 1000.0, 
                             dir='met', 
                             vexpr = 'self.chain.met_reco_ety',            
                             )

h_met_reco_et      = Hist1D( 'met_reco_et',
                             title = 'E_{T}^{miss}',
                             nbins = 1000, 
                             xmin = 0., 
                             xmax = 1000.0, 
                             dir='met', 
                             vexpr = 'self.chain.met_reco_et',             
                             )

h_met_reco_phi     = Hist1D( 'met_reco_phi',
                             title = 'E_{T}^{miss}(#phi)',
                             nbins = 1000, 
                             xmin = -3.2, 
                             xmax = 3.2, 
                             dir='met', 
                             vexpr = 'self.chain.met_reco_phi',            
                             )

# -------
# event
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
# --------
# 2D hists
# --------
h_lep_0_pt_tau_0_pt  = Hist2D( hname  = "h_lep_0_pt_tau_0_pt",
                              xtitle  = "p_{T}(l_{lead}) [GeV]",
                              ytitle  = "p_{T}(#tau_{lead}) [GeV]", 
                              nbinsx  = 1000,
                              xmin    = 0.,
                              xmax    = 1000.,
                              nbinsy  = 1000,
                              ymin    = 0.,
                              ymax    = 1000.,
                              dir     = "event",
                              vexpr   = " self.chain.lep_0_pt , self.chain.tau_0_pt",
                          )

# EOF
