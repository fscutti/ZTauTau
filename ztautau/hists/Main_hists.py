from histconfig import *


hist_list = []


## -------
## event
## -------
#hist_list.append(h_n_vx)
##hist_list.append(h_dummy)
#
## -------
## jets
## -------
#hist_list.append(h_jet_0_pt)
#
## -------
## MET
## -------
#hist_list.append(h_met_reco_et)
hist_list.append(h_tau0_eta         )
hist_list.append(h_tau0_phi         )
hist_list.append(h_tau0_pt          )
hist_list.append(h_lep0_eta         )
hist_list.append(h_lep0_phi         )
hist_list.append(h_lep0_pt          )
hist_list.append(h_lh_vis_m         )
hist_list.append(h_lh_mmc_mlm_m     )
hist_list.append(h_lh_mmc_maxw_m    )
hist_list.append(h_lh_mmc_mlnu3p    )
hist_list.append(h_lh_coll_m        )
hist_list.append(h_lh_coll_x0       )
hist_list.append(h_lh_coll_x1 	    )
hist_list.append(h_lh_lep_mt        )
hist_list.append(h_lh_tau_mt        )
hist_list.append(h_lh_dR            )
hist_list.append(h_lh_deta          )
hist_list.append(h_lh_met_cent      )
hist_list.append(h_met_reco_et      )
hist_list.append(h_NN_W_output      )
hist_list.append(h_NN_Z_output      )
hist_list.append(h_NN_comb_output   )
hist_presel = []
hist_presel.append(h_evt_nvx          )
hist_presel.append(h_evt_npvx         )
hist_presel.append(h_evt_navgint      )
hist_presel.append(h_evt_navgintcor   )
hist_presel.append(h_evt_n_jets       )
hist_presel.append(h_met_reco_sumet   )
hist_presel.append(h_met_reco_etx     )
hist_presel.append(h_met_reco_ety     )
#hist_presel.append(h_met_reco_phi     )
#hist_presel.append(h_NN_input_tau_E   )
#hist_presel.append(h_NN_input_tau_pz  )
#hist_presel.append(h_NN_input_lep_px  )
#hist_presel.append(h_NN_input_lep_pz  )
#hist_presel.append(h_NN_input_lep_E   )
#hist_presel.append(h_NN_input_met_px  )
#hist_presel.append(h_NN_input_met_py  )
#hist_presel.append(h_NN_input_met_pz  )
#hist_presel.append(h_NN_input_met_E   )
#hist_presel.append(h_NN_input_mcoll   )
#hist_presel.append(h_NN_input_mvis    )
#hist_presel.append(h_NN_input_mmmc    )
#hist_presel.append(h_NN_input_boost   )
                                                                                   
hist_presel = []                                                                   

#h_evt_nvx        .apply_final_binning({'xmin':     0, 'xmax':   50, 'nbins': 50}); hist_presel.append( h_evt_nvx        )
#h_evt_npvx       .apply_final_binning({'xmin':     0, 'xmax':    5, 'nbins':  5}); hist_presel.append( h_evt_npvx       )
#h_evt_navgint    .apply_final_binning({'xmin':     0, 'xmax':   50, 'nbins': 50}); hist_presel.append( h_evt_navgint    )
#h_evt_navgintcor .apply_final_binning({'xmin':     0, 'xmax':   50, 'nbins': 50}); hist_presel.append( h_evt_navgintcor )
#h_evt_n_jets     .apply_final_binning({'xmin':     0, 'xmax':    8, 'nbins':  8}); hist_presel.append( h_evt_n_jets     )
#h_met_reco_sumet .apply_final_binning({'xmin':    0., 'xmax': 100., 'nbins': 10}); hist_presel.append( h_met_reco_sumet )
#h_met_reco_etx   .apply_final_binning({'xmin':    0., 'xmax': 100., 'nbins': 10}); hist_presel.append( h_met_reco_etx   )
#h_met_reco_ety   .apply_final_binning({'xmin':    0., 'xmax': 100., 'nbins': 10}); hist_presel.append( h_met_reco_ety   )
#h_met_reco_phi   .apply_final_binning({'xmin':  -3.2, 'xmax':  3.2, 'nbins': 20}); hist_presel.append( h_met_reco_phi   )
#h_NN_input_tau_pz.apply_final_binning({'xmin': -150., 'xmax': 150., 'nbins': 25}); hist_presel.append( h_NN_input_tau_pz)
#h_NN_input_tau_E .apply_final_binning({'xmin':    0., 'xmax': 200., 'nbins': 20}); hist_presel.append( h_NN_input_tau_E )
#h_NN_input_lep_px.apply_final_binning({'xmin': -150., 'xmax': 150., 'nbins': 25}); hist_presel.append( h_NN_input_lep_px)
#h_NN_input_lep_pz.apply_final_binning({'xmin': -150., 'xmax': 150., 'nbins': 25}); hist_presel.append( h_NN_input_lep_pz)
#h_NN_input_lep_E .apply_final_binning({'xmin':    0., 'xmax': 150., 'nbins': 25}); hist_presel.append( h_NN_input_lep_E )
#h_NN_input_met_px.apply_final_binning({'xmin': -150., 'xmax': 150., 'nbins': 25}); hist_presel.append( h_NN_input_met_px)
#h_NN_input_met_py.apply_final_binning({'xmin': -150., 'xmax': 150., 'nbins': 25}); hist_presel.append( h_NN_input_met_py)
#h_NN_input_met_pz.apply_final_binning({'xmin': -150., 'xmax': 150., 'nbins': 25}); hist_presel.append( h_NN_input_met_pz)
#h_NN_input_met_E .apply_final_binning({'xmin':    0., 'xmax': 150., 'nbins': 25}); hist_presel.append( h_NN_input_met_E )
#h_NN_input_mcoll .apply_final_binning({'xmin':   50., 'xmax': 300., 'nbins': 25, 'blind_range' : [100,150]}); hist_presel.append( h_NN_input_mcoll )
#h_NN_input_mvis  .apply_final_binning({'xmin':   50., 'xmax': 300., 'nbins': 25, 'blind_range' : [100,150]}); hist_presel.append( h_NN_input_mvis  )
#h_NN_input_mmmc  .apply_final_binning({'xmin':   50., 'xmax': 300., 'nbins': 25, 'blind_range' : [100,150]}); hist_presel.append( h_NN_input_mmmc  )
#h_NN_input_boost .apply_final_binning({'xmin': -100., 'xmax': 100., 'nbins': 25}); hist_presel.append( h_NN_input_boost )
#h_tau0_eta       .apply_final_binning({'xmin':  -2.5, 'xmax':  2.5, 'nbins': 20});   hist_list.append(h_tau0_eta      )
#h_tau0_phi       .apply_final_binning({'xmin':  -3.2, 'xmax':  3.2, 'nbins': 20});   hist_list.append(h_tau0_phi      )
#h_tau0_pt        .apply_final_binning({'xmin':   20., 'xmax': 100., 'nbins': 16});   hist_list.append(h_tau0_pt       )
#h_lep0_eta       .apply_final_binning({'xmin':  -2.5, 'xmax':  2.5, 'nbins': 20});   hist_list.append(h_lep0_eta      )
#h_lep0_phi       .apply_final_binning({'xmin':  -3.2, 'xmax':  3.2, 'nbins': 20});   hist_list.append(h_lep0_phi      )
#h_lep0_pt        .apply_final_binning({'xmin':   20., 'xmax': 100., 'nbins': 16});   hist_list.append(h_lep0_pt       )
#
#h_lh_vis_m       .apply_final_binning({'xmin':   50., 'xmax': 300., 'nbins': 25, 'blind_range' : [100,151]});   hist_list.append(h_lh_vis_m )
#h_lh_mmc_mlm_m   .apply_final_binning({'xmin':   50., 'xmax': 300., 'nbins': 25, 'blind_range' : [100,151]});   hist_list.append(h_lh_mmc_mlm_m  )
#h_lh_mmc_maxw_m  .apply_final_binning({'xmin':   50., 'xmax': 300., 'nbins': 25, 'blind_range' : [100,151]});   hist_list.append(h_lh_mmc_maxw_m )
#h_lh_mmc_mlnu3p  .apply_final_binning({'xmin':   50., 'xmax': 300., 'nbins': 25, 'blind_range' : [100,151]});   hist_list.append(h_lh_mmc_mlnu3p )
#h_lh_coll_m      .apply_final_binning({'xmin':   50., 'xmax': 300., 'nbins': 25, 'blind_range' : [100,151]});   hist_list.append(h_lh_coll_m     )
#h_lh_coll_x0     .apply_final_binning({'xmin':    0., 'xmax':   1., 'nbins': 25});   hist_list.append(h_lh_coll_x0    )
#h_lh_coll_x1 	 .apply_final_binning({'xmin':    0., 'xmax':   1., 'nbins': 25});   hist_list.append(h_lh_coll_x1    )       
#h_lh_lep_mt      .apply_final_binning({'xmin':    0., 'xmax': 200., 'nbins': 20});   hist_list.append(h_lh_lep_mt     )
#h_lh_tau_mt      .apply_final_binning({'xmin':    0., 'xmax': 200., 'nbins': 20});   hist_list.append(h_lh_tau_mt     )
#h_lh_dR          .apply_final_binning({'xmin':    0., 'xmax':   5., 'nbins': 20});   hist_list.append(h_lh_dR         )
#h_lh_deta        .apply_final_binning({'xmin':    0., 'xmax':   5., 'nbins': 20});   hist_list.append(h_lh_deta       )
#h_lh_met_cent    .apply_final_binning({'xmin':    0., 'xmax':  1.5, 'nbins': 15});   hist_list.append(h_lh_met_cent   )
#h_met_reco_et    .apply_final_binning({'xmin':    0., 'xmax': 100., 'nbins': 10});   hist_list.append(h_met_reco_et   )
#h_NN_W_output    .apply_final_binning({'xmin':    0., 'xmax':   1., 'nbins': 10, 'blind_range' : [0.7,1.1]});   hist_list.append(h_NN_W_output   )
#h_NN_Z_output    .apply_final_binning({'xmin':    0., 'xmax':   1., 'nbins': 10, 'blind_range' : [0.7,1.1]});   hist_list.append(h_NN_Z_output   )
#h_NN_comb_output .apply_final_binning({'xmin':    0., 'xmax':   1., 'nbins': 10, 'blind_range' : [0.7,1.1]});   hist_list.append(h_NN_comb_output)
#h_BDT_output     .apply_final_binning({'xmin':    0., 'xmax':   1., 'nbins': 10, 'blind_range' : [0.7,1.1]});   hist_list.append(h_BDT_output    )

import itertools as it
variables_NN      = [
                    h_NN_input_tau_E ,
                    h_NN_input_tau_pz,
                    h_NN_input_lep_px,
                    h_NN_input_lep_pz,
                    h_NN_input_lep_E ,
                    h_NN_input_met_px,
                    h_NN_input_met_py,
                    h_NN_input_met_pz,
                    h_NN_input_met_E ,
                    h_NN_input_mcoll ,
                    h_NN_input_mvis  ,
                    h_NN_input_mmmc  ,
                    h_NN_input_boost ,
                    h_NN_W_output,
                    h_NN_Z_output,
                    h_NN_comb_output
                    ]

variables_BDT     = [
                    h_tau0_eta  ,
                    h_tau0_phi  ,
                    h_tau0_pt   ,
                    h_lep0_eta  ,
                    h_lep0_phi  ,
                    h_lep0_pt   ,
                    h_NN_input_mcoll ,
                    h_NN_input_mvis  ,
                    h_BDT_output,
                    h_met_reco_et ,
                    h_met_reco_phi,
                    h_lh_lep_mt  ,
                    h_lh_tau_mt  ,
                    h_lh_scdp    ,
                    h_lh_dR      ,
                    h_lh_deta    ,
                    ]

bdt_2d = it.combinations(variables_BDT, 2 )
nn_2d  = it.combinations(variables_NN,  2 )
combs_2d = []
for c in list(bdt_2d)+list(nn_2d):
    combs_2d.append(Profile( hname  = c[0].hname+'_'+c[1].hname,
                             xtitle = c[0].xtitle,
                             ytitle = c[1].xtitle,
                             nbinsx = c[0].nbins,
                             xmin   = c[0].xmin,
                             xmax   = c[0].xmax,
                             nbinsy = c[1].nbins,
                             ymin   = c[1].xmin,
                             ymax   = c[1].xmax,
                             dir    = 'profile',
                             vexpr  = c[0].vexpr+' , '+c[1].vexpr
                             ))
    combs_2d.append( Hist2D( hname  = c[0].hname+'_'+c[1].hname,
                             xtitle = c[0].xtitle,
                             ytitle = c[1].xtitle,
                             nbinsx = c[0].nbins,
                             xmin   = c[0].xmin,
                             xmax   = c[0].xmax,
                             nbinsy = c[1].nbins,
                             ymin   = c[1].xmin,
                             ymax   = c[1].xmax,
                             dir    = 'hist_2d',
                             vexpr  = c[0].vexpr+' , '+c[1].vexpr
                             ))
hist_test=combs_2d
#hist_presel.append(h_event_number_comp)
hist_presel = variables_NN+variables_BDT+combs_2d#+hist_presel
hist_presel = hist_presel
hist_combs  = combs_2d
hist_ac = [h_tau0_pt]#variables_NN+variables_BDT+hist_presel
hist_fit = [h_BDT_output,h_NN_W_output,h_NN_Z_output,h_NN_comb_output,h_NN_input_mcoll]
#hist_fit = [h_NN_input_mcoll]
