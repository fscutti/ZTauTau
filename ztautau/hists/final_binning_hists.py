from histconfig import *


hist_list = []
h_tau0_eta         .apply_final_binning({'xmin':  -2.5, 'xmax':  2.5, 'nbins': 20});   hist_list.append(h_tau0_eta      )
h_tau0_phi         .apply_final_binning({'xmin':  -3.2, 'xmax':  3.2, 'nbins': 20});   hist_list.append(h_tau0_phi      )
h_tau0_pt          .apply_final_binning({'xmin':   20., 'xmax': 100., 'nbins': 16});   hist_list.append(h_tau0_pt       )
h_lep0_eta         .apply_final_binning({'xmin':  -2.5, 'xmax':  2.5, 'nbins': 20});   hist_list.append(h_lep0_eta      )
h_lep0_phi         .apply_final_binning({'xmin':  -3.2, 'xmax':  3.2, 'nbins': 20});   hist_list.append(h_lep0_phi      )
h_lep0_pt          .apply_final_binning({'xmin':   20., 'xmax': 100., 'nbins': 16});   hist_list.append(h_lep0_pt       )
h_lh_vis_m         .apply_final_binning({'xmin':   50., 'xmax': 300., 'nbins': 25});   hist_list.append(h_lh_vis_m      )
h_lh_mmc_mlm_m     .apply_final_binning({'xmin':   50., 'xmax': 300., 'nbins': 25});   hist_list.append(h_lh_mmc_mlm_m  )
h_lh_mmc_maxw_m    .apply_final_binning({'xmin':   50., 'xmax': 300., 'nbins': 25});   hist_list.append(h_lh_mmc_maxw_m )
h_lh_mmc_mlnu3p    .apply_final_binning({'xmin':   50., 'xmax': 300., 'nbins': 25});   hist_list.append(h_lh_mmc_mlnu3p )
h_lh_coll_m        .apply_final_binning({'xmin':   50., 'xmax': 300., 'nbins': 25});   hist_list.append(h_lh_coll_m     )
h_lh_coll_x0       .apply_final_binning({'xmin':    0., 'xmax':   1., 'nbins': 25});   hist_list.append(h_lh_coll_x0    )
h_lh_coll_x1 	   .apply_final_binning({'xmin':    0., 'xmax':   1., 'nbins': 25});   hist_list.append(h_lh_coll_x1    )       
h_lh_lep_mt        .apply_final_binning({'xmin':    0., 'xmax': 200., 'nbins': 20});   hist_list.append(h_lh_lep_mt     )
h_lh_tau_mt        .apply_final_binning({'xmin':    0., 'xmax': 200., 'nbins': 20});   hist_list.append(h_lh_tau_mt     )
h_lh_dR            .apply_final_binning({'xmin':    0., 'xmax':   5., 'nbins': 20});   hist_list.append(h_lh_dR         )
h_lh_deta          .apply_final_binning({'xmin':    0., 'xmax':   5., 'nbins': 20});   hist_list.append(h_lh_deta       )
h_lh_met_cent      .apply_final_binning({'xmin':    0., 'xmax':  1.5, 'nbins': 15});   hist_list.append(h_lh_met_cent   )
h_met_reco_et      .apply_final_binning({'xmin':    0., 'xmax': 100., 'nbins': 10});   hist_list.append(h_met_reco_et   )
h_NN_W_output      .apply_final_binning({'xmin':    0., 'xmax':   1., 'nbins': 10});   hist_list.append(h_NN_W_output   )
h_NN_Z_output      .apply_final_binning({'xmin':    0., 'xmax':   1., 'nbins': 10});   hist_list.append(h_NN_Z_output   )
h_NN_comb_output   .apply_final_binning({'xmin':    0., 'xmax':   1., 'nbins': 10});   hist_list.append(h_NN_comb_output)
                                                                                   
hist_presel = []                                                                   
h_evt_nvx        .apply_final_binning({'xmin':     0, 'xmax':   50, 'nbins': 50}); hist_presel.append( h_evt_nvx        )
h_evt_npvx       .apply_final_binning({'xmin':     0, 'xmax':    5, 'nbins':  5}); hist_presel.append( h_evt_npvx       )
h_evt_navgint    .apply_final_binning({'xmin':     0, 'xmax':   50, 'nbins': 50}); hist_presel.append( h_evt_navgint    )
h_evt_navgintcor .apply_final_binning({'xmin':     0, 'xmax':   50, 'nbins': 50}); hist_presel.append( h_evt_navgintcor )
h_evt_n_jets     .apply_final_binning({'xmin':     0, 'xmax':    8, 'nbins':  8}); hist_presel.append( h_evt_n_jets     )
h_met_reco_sumet .apply_final_binning({'xmin':    0., 'xmax': 100., 'nbins': 10}); hist_presel.append( h_met_reco_sumet )
h_met_reco_etx   .apply_final_binning({'xmin':    0., 'xmax': 100., 'nbins': 10}); hist_presel.append( h_met_reco_etx   )
h_met_reco_ety   .apply_final_binning({'xmin':    0., 'xmax': 100., 'nbins': 10}); hist_presel.append( h_met_reco_ety   )
h_met_reco_phi   .apply_final_binning({'xmin':  -3.2, 'xmax':  3.2, 'nbins': 20}); hist_presel.append( h_met_reco_phi   )
h_NN_input_tau_E .apply_final_binning({'xmin':    0., 'xmax': 200., 'nbins': 20}); hist_presel.append( h_NN_input_tau_E )
h_NN_input_lep_px.apply_final_binning({'xmin': -150., 'xmax': 150., 'nbins': 25}); hist_presel.append( h_NN_input_lep_px)
h_NN_input_lep_pz.apply_final_binning({'xmin': -150., 'xmax': 150., 'nbins': 25}); hist_presel.append( h_NN_input_lep_pz)
h_NN_input_lep_E .apply_final_binning({'xmin':    0., 'xmax': 150., 'nbins': 25}); hist_presel.append( h_NN_input_lep_E )
h_NN_input_met_pz.apply_final_binning({'xmin': -150., 'xmax': 150., 'nbins': 25}); hist_presel.append( h_NN_input_met_pz)
h_NN_input_met_E .apply_final_binning({'xmin':    0., 'xmax': 150., 'nbins': 25}); hist_presel.append( h_NN_input_met_E )
h_NN_input_mcoll .apply_final_binning({'xmin':   50., 'xmax': 300., 'nbins': 25}); hist_presel.append( h_NN_input_mcoll )
h_NN_input_mvis  .apply_final_binning({'xmin':   50., 'xmax': 300., 'nbins': 25}); hist_presel.append( h_NN_input_mvis  )
h_NN_input_mmmc  .apply_final_binning({'xmin':   50., 'xmax': 300., 'nbins': 25}); hist_presel.append( h_NN_input_mmmc  )
h_NN_input_boost .apply_final_binning({'xmin': -100., 'xmax': 100., 'nbins': 25}); hist_presel.append( h_NN_input_boost )

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
import itertools as it
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

hist_dict = {}
for h in hist_list+hist_presel: 
  hist_dict[h.hname] = h.__dict__




