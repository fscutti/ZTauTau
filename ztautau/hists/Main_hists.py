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
hist_presel.append(h_met_reco_phi     )
hist_presel.append(h_NN_input_tau_E   )
hist_presel.append(h_NN_input_lep_px  )
hist_presel.append(h_NN_input_lep_pz  )
hist_presel.append(h_NN_input_lep_E   )
hist_presel.append(h_NN_input_met_pz  )
hist_presel.append(h_NN_input_met_E   )
hist_presel.append(h_NN_input_mcoll   )
hist_presel.append(h_NN_input_mvis    )
hist_presel.append(h_NN_input_mmmc    )
hist_presel.append(h_NN_input_boost   )
hist_presel+=combs_2d
#hist_presel.append(h_event_number_comp)
