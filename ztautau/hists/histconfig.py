from hists import *


"""
This contains the histogram
configuration. Do not create
other config files !!!
"""




h_cutflow_presel_mu161p = Hist1D('cutflow_presel_mu161p',dir="")
h_cutflow_presel_mu163p = Hist1D('cutflow_presel_mu163p',dir="")
h_cutflow_presel_mu16inc = Hist1D('cutflow_presel_mu16inc',dir="")


###############
# TAU RELATED #
###############
h_tau0_eta         = Hist1D( 'tau_0_eta',                
                             xtitle = '#eta(#tau)',                   
                             nbins = 1000, 
                             xmin = -6.0, 
                             xmax = 6.0, 
                             dir='tau', 
                             vexpr = 'self.chain.tau_0_eta',               
                             )

h_tau0_phi         = Hist1D( 'tau_0_phi',                
                             xtitle = '#phi(#tau)',                   
                             nbins = 1000, 
                             xmin = -3.2, 
                             xmax = 3.2, 
                             dir='tau', 
                             vexpr = 'self.chain.tau_0_phi',               
                             )

h_tau0_pt          = Hist1D( 'tau_0_pt',                 
                             xtitle = 'p_{T}(#tau)',                  
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
                             xtitle = '#eta(l)',                      
                             nbins = 1000, 
                             xmin = -6.0, 
                             xmax = 6.0, 
                             dir='lep', 
                             vexpr = 'self.chain.lep_0_eta',               
                             )

h_lep0_phi         = Hist1D( 'lep_0_phi',                
                             xtitle = '#phi(l)',                      
                             nbins = 1000, 
                             xmin = -3.2, 
                             xmax = 3.2, 
                             dir='lep', 
                             vexpr = 'self.chain.lep_0_phi',               
                             )

h_lep0_pt          = Hist1D( 'lep_0_pt',                 
                             xtitle = 'p_{T}(l)',                     
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
                             xtitle = 'm_{vis}(#tau,l)',
                             nbins = 1000, 
                             xmin = 0., 
                             xmax = 1000.0, 
                             dir='lephad', 
                             vexpr = 'self.chain.lephad_vis_mass',         
                             )

h_lh_mmc_mlm_m     = Hist1D( 'lephad_lfv_mmc_mlm_m',
                             xtitle = 'm^{mlm}_{MMC}(#tau,l)',
                             nbins = 1000, 
                             xmin = 0., 
                             xmax = 1000.0, 
                             dir='lephad', 
                             vexpr = 'self.chain.lephad_lfv_mmc_mlm_m', 
                             )

h_lh_mmc_maxw_m    = Hist1D( 'lephad_lfv_mmc_maxw_m', 
                             xtitle = 'm^{maxw}_{MMC}(#tau,l)',
                             nbins = 1000, 
                             xmin = 0., 
                             xmax = 1000.0, 
                             dir='lephad', 
                             vexpr = 'self.chain.lephad_lfv_mmc_maxw_m',
                             )

h_lh_mmc_mlnu3p    = Hist1D( 'lephad_mmc_mlnu3p_m',
                             xtitle = 'm^{mlnu3p}_{MMC}(#tau,l)',
                             nbins = 1000, 
                             xmin = 0., 
                             xmax = 1000.0, 
                             dir='lephad', 
                             vexpr = 'self.chain.lephad_mmc_mlnu3p_m',  
                             )

h_lh_coll_m        = Hist1D( 'coll_approx_lfv_m',
                             xtitle = 'm_{Coll}(#tau,l)',
                             nbins = 1000, 
                             xmin = 0., 
                             xmax = 1000.0, 
                             dir='lephad', 
                             vexpr = 'self.chain.coll_approx_lfv_m',    
                             )

h_lh_coll_x0       = Hist1D( 'lephad_coll_approx_x0',
                             xtitle = 'x0',
                             nbins = 1000, 
                             xmin = -2.0,
                             xmax = 2.0, 
                             dir='lephad', 
                             vexpr = 'self.chain.lephad_coll_approx_x0',   
                             )

h_lh_coll_x1 	   = Hist1D( 'lephad_coll_approx_x1',    
                             xtitle = 'x1',                           
                             nbins = 1000, 
                             xmin = -2.0,
                             xmax = 2.0, 
                             dir='lephad', 
                             vexpr = 'self.chain.lephad_coll_approx_x1',   
                             )

h_lh_scdp          = Hist1D( 'lephad_met_sum_cos_dphi',  
                             xtitle = '#Sigma cos(#Delta#phi)',       
                             nbins = 1000, 
                             xmin = -4.0, 
                             xmax = 4.0, 
                             dir='lephad', 
                             vexpr = 'self.chain.lephad_met_sum_cos_dphi', 
                             )

h_lh_lep_mt        = Hist1D( 'lephad_mt_lep_0_met',      
                             xtitle = 'm_{T}(#l,MET)',                
                             nbins = 1000, 
                             xmin = 0., 
                             xmax = 1000.0, 
                             dir='lephad', 
                             vexpr = 'self.chain.lephad_mt_lep0_met',     
                             )

h_lh_tau_mt        = Hist1D( 'lephad_mt_tau_0_met',      
                             xtitle = 'm_{T}(#tau,MET)',              
                             nbins = 1000, 
                             xmin = 0., 
                             xmax = 1000.0, 
                             dir='lephad', 
                             vexpr = 'self.chain.lephad_mt_lep1_met',     
                             )

h_lh_dR            = Hist1D( 'lephad_dr',                
                             xtitle = '#Delta R(#tau,l)',             
                             nbins = 1000, 
                             xmin = 0., 
                             xmax = 6.0, 
                             dir='lephad', 
                             vexpr = 'self.chain.lephad_dr',               
                             )

h_lh_deta          = Hist1D( 'lephad_deta',              
                             xtitle = '|#Delta #eta(#tau,l)|',        
                             nbins = 1000, 
                             xmin = 0., 
                             xmax = 6.0, 
                             dir='lephad', 
                             vexpr = 'self.chain.lephad_deta',             
                             )

h_lh_met_cent      = Hist1D( 'lephad_met_cent',          
                             xtitle = 'E_{T}^{miss} #phi Centrality', 
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
                             xtitle = 'N_{vertex}',
                             nbins = 100, 
                             xmin = 0., 
                             xmax = 100.0, 
                             dir='event', 
                             vexpr = 'self.chain.n_vx',
                             )

h_evt_npvx         = Hist1D( 'n_pvx',
                             xtitle = 'N_{Primary vertex}',
                             nbins = 100, 
                             xmin = 0., 
                             xmax = 100.0, 
                             dir='event', 
                             vexpr = 'self.chain.n_pvx',
                             )

h_evt_navgint      = Hist1D( 'n_avg_int',
                             xtitle = '<#mu>',
                             nbins = 100, 
                             xmin = 0., 
                             xmax = 100.0, 
                             dir='event', 
                             vexpr = 'self.chain.n_avg_int',                   
                             )

h_evt_navgintcor   = Hist1D( 'n_avg_int_cor',
                             xtitle = '<#mu>_{corrected}',
                             nbins = 100, 
                             xmin = 0., 
                             xmax = 100.0, 
                             dir='event', 
                             vexpr = 'self.chain.n_avg_int_cor',               
                             )

h_evt_n_jets       = Hist1D( 'n_jets',
                             xtitle = 'N_{jets}',
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
                             xtitle = 'MET #Sigma E_{t}',
                             nbins = 1000, 
                             xmin = 0., 
                             xmax = 1000.0, 
                             dir='met', 
                             vexpr = 'self.chain.met_reco_sumet',          
                             )

h_met_reco_etx     = Hist1D( 'met_reco_etx',
                             xtitle = 'E_{x}^{miss}',
                             nbins = 1000, 
                             xmin = 0., 
                             xmax = 1000.0, 
                             dir='met', 
                             vexpr = 'self.chain.met_reco_etx',            
                             )

h_met_reco_ety     = Hist1D( 'met_reco_ety',
                             xtitle = 'E_{y}^{miss}',
                             nbins = 1000, 
                             xmin = 0., 
                             xmax = 1000.0, 
                             dir='met', 
                             vexpr = 'self.chain.met_reco_ety',            
                             )

h_met_reco_et      = Hist1D( 'met_reco_et',
                             xtitle = 'E_{T}^{miss}',
                             nbins = 1000, 
                             xmin = 0., 
                             xmax = 1000.0, 
                             dir='met', 
                             vexpr = 'self.chain.met_reco_et',             
                             )

h_met_reco_phi     = Hist1D( 'met_reco_phi',
                             xtitle = 'E_{T}^{miss}(#phi)',
                             nbins = 1000, 
                             xmin = -3.2, 
                             xmax = 3.2, 
                             dir='met', 
                             vexpr = 'self.chain.met_reco_phi',            
                             )

h_met_reco_phi     = Hist1D( 'met_reco_phi',
                             xtitle = 'E_{T}^{miss}(#phi)',
                             nbins = 1000, 
                             xmin = -3.2, 
                             xmax = 3.2, 
                             dir='met', 
                             vexpr = 'self.chain.met_reco_phi',            
                             )

###############
# MET RELATED #
###############
h_NN_W_output      = Hist1D( 'output_W',
                             xtitle = 'NN (LFV vs W) score',
                             nbins = 1000, 
                             xmin = 0., 
                             xmax = 1.0, 
                             dir='nn', 
                             vexpr = 'self.chain.output_W',
                             )

h_NN_Z_output      = Hist1D( 'output_Z',
                             xtitle = 'NN (LFV vs Z) score',
                             nbins = 1000, 
                             xmin = 0., 
                             xmax = 1.0, 
                             dir='nn', 
                             vexpr = 'self.chain.output_Z',
                             )

h_NN_comb_output   = Hist1D( 'output_comb',
                             xtitle = 'NN combined score',
                             nbins = 1000, 
                             xmin = 0., 
                             xmax = 1.0, 
                             dir='nn', 
                             vexpr = 'self.chain.output_comb',
                             )

h_NN_input_tau_E   = Hist1D( 'NN_input_tau_E' , 
                             xtitle='NN input E(#tau)',            
                             nbins=1000, 
                             xmin=   0., 
                             xmax=500., 
                             dir='nn', 
                             vexpr='self.chain.NN_input_tau_E'
                             )

h_NN_input_lep_px  = Hist1D( 'NN_input_lep_px',
                             xtitle='NN input p_{x}(lep)',
                             nbins=1000, 
                             xmin=-500., 
                             xmax=500., 
                             dir='nn', 
                             vexpr='self.chain.NN_input_lep_px'
                             )

h_NN_input_lep_pz  = Hist1D( 'NN_input_lep_pz', 
                             xtitle='NN input p_{z}(lep)',
                             nbins=1000,
                             xmin=-500., 
                             xmax=500., 
                             dir='nn', 
                             vexpr='self.chain.NN_input_lep_pz'
                             )

h_NN_input_lep_E   = Hist1D( 'NN_input_lep_E' , 
                             xtitle='NN input E(lep)',             
                             nbins=1000, 
                             xmin=   0., 
                             xmax=500., 
                             dir='nn', 
                             vexpr='self.chain.NN_input_lep_E'
                             )

h_NN_input_met_pz  = Hist1D( 'NN_input_met_pz', 
                             xtitle='NN input p_{z} (E_{T}^{miss})',
                             nbins=1000, 
                             xmin=-500., 
                             xmax=500., 
                             dir='nn', 
                             vexpr='self.chain.NN_input_met_pz'
                             )

h_NN_input_met_E   = Hist1D( 'NN_input_met_E' , 
                             xtitle='NN input E (E_{T}^{miss})',   
                             nbins=1000, 
                             xmin=   0., 
                             xmax=500., 
                             dir='nn', 
                             vexpr='self.chain.NN_input_met_E'
                             )

h_NN_input_mcoll   = Hist1D( 'NN_input_mcoll' , 
                             xtitle='NN input m_{coll}',           
                             nbins=1000, 
                             xmin=   0., 
                             xmax=500., 
                             dir='nn', 
                             vexpr='self.chain.NN_input_mcoll'
                             )

h_NN_input_mvis    = Hist1D( 'NN_input_mvis'  , 
                             xtitle='NN input m_{vis}',            
                             nbins=1000, 
                             xmin=   0., 
                             xmax=500., 
                             dir='nn', 
                             vexpr='self.chain.NN_input_mvis'
                             )

h_NN_input_mmmc    = Hist1D( 'NN_input_mmmc'  , 
                             xtitle='NN input m_{MMC}',            
                             nbins=1000, 
                             xmin=   0., 
                             xmax=500., 
                             dir='nn', 
                             vexpr='self.chain.NN_input_mmmc'
                             )

h_NN_input_boost   = Hist1D( 'NN_input_boost' , 
                             xtitle='NN input boost',              
                             nbins=1000, 
                             xmin=   0., 
                             xmax=500., 
                             dir='nn', 
                             vexpr='self.chain.NN_input_boost'
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

h_event_number_comp  = Hist2D( hname  = "h_event_number_comp",
                              xtitle  = "event_number",
                              ytitle  = "eventNumber", 
                              nbinsx  = 1000,#int(100000-10000),
                              xmin    = 10000.,
                              xmax    = 100000.,
                              nbinsy  = 1000,#int(100000-10000),
                              ymin    = 10000.,
                              ymax    = 100000.,
                              dir     = "nn",
                              vexpr   = "self.chain.event_number, self.chain.eventNumber",
                          )
# EOF
