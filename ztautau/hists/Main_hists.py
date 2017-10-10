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

import itertools as it
variables_NN      = [
                    h_NN_input_tau_E ,
                    h_NN_input_lep_px,
                    h_NN_input_lep_pz,
                    h_NN_input_lep_E ,
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
comb_2d  = it.combinations(variables_NN, 2 )
combs_2d = []
for c in comb_2d:
    combs_2d.append(Hist2D( hname  = 'h_'+c[0].hname+'_'+c[1].hname,
                            xtitle = c[0].xtitle,
                            ytitle = c[1].xtitle,
                            nbinsx = c[0].nbins,
                            xmin   = c[0].xmin,
                            xmax   = c[0].xmax,
                            nbinsy = c[1].nbins,
                            ymin   = c[1].xmin,
                            ymax   = c[1].xmax,
                            dir    = 'nn',
                            vexpr  = c[0].vexpr+' , '+c[1].vexpr
                            ))
hist_presel+=combs_2d
#hist_presel.append(h_event_number_comp)
