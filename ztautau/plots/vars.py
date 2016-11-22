# encoding: utf-8
'''
vars.py
description:
variables for plotting
'''

## modules
from var import Var

## Event variables
## ---------------------------------------
nmuons = Var(name = 'nmuons',
              path  = 'event',
              xmin  = 0,
              xmax  = 5,
              log   = False,
	      xmin2 = None,
	      xmax2 = None,
              )

pileup = Var(name = 'pileup',
              path  = 'event',
              xmin  = 0,
              xmax  = 40,
              log   = False,
	      xmin2 = None,
	      xmax2 = None,
              )

n_vx = Var(name = 'n_vx',
              path    = 'event',
              xmin    = 0,
              xmax    = 14,
     #         rebin   = 0,
              log     = False,
              xmin2 = None,
              xmax2 = None,
              )

n_bjets = Var(name = 'n_bjets',
	      path = 'event',
	      xmin = 0,
	      xmax = 5,
              xmin2 = None,
              xmax2 = None,
	      log = False,
	      )

n_jets = Var(name = 'n_jets',
              path = 'event',
              xmin = 0,
              xmin2 = None,
              xmax2 = None,
              xmax = 19,
              log = False,
              )

## Muon variables
## ---------------------------------------
mu_pt = Var(name = 'mu_pt',
              path    = 'muons',
              xmin    = 20,
              xmax    = 150,
              rebin   = 4,
              xmin2 = None,
              xmax2 = None,
              log     = False,
              )

mu_phi = Var(name = 'mu_phi',
              path    = 'muons',
              xmin    = -4,
              xmax    = 4,
              xmin2 = None,
              xmax2 = None,
              #rebin   = 2,
              log     = False,
              )

mu_eta = Var(name = 'mu_eta',
              path    = 'muons',
              xmin    = -3,
              xmax    = 3,
              xmin2 = None,
              xmax2 = None,
#              rebin   = 2,
              log     = False,
              )
              #

topoetcone20ptmev = Var(name = 'topoetcone20pt',
			path = 'muons',
			xmin = -0.5,
			xmax = 0.5,
              		xmin2 = None,
              		xmax2 = None,
			log = False,
			)

ptvarcone30ptmev = Var(name = 'ptvarcone30pt',
                        path = 'muons',
                        xmin = -0.5,
                        xmax = 0.5,
                        xmin2 = None,
                        xmax2 = None,
                        log = False,
                        )

topoetcone20mev = Var(name = 'topoetcone20',
                        path = 'muons',
                        xmin = -20000,
                        xmax = 200000,
                        xmin2 = None,
                        xmax2 = None,
                        log = False,
                        )

ptvarcone30mev = Var(name = 'ptvarcone30',
                        path = 'muons',
                        xmin = -30000,
                        xmax = 300000,
                        log = False,
                        xmin2 = None,
                        xmax2 = None,
                        )

topoetcone20pt = Var(name = 'topoetcone20pt',
			path = 'muons',
			xmin = -0.5,
			xmax = 0.5,
			log = False,
                        xmin2 = None,
                        xmax2 = None,
			)

ptvarcone30pt = Var(name = 'ptvarcone30pt',
                        path = 'muons',
                        xmin = -0.5,
                        xmax = 0.5,
                        log = False,
                        xmin2 = None,
                        xmax2 = None,
                        )

topoetcone20 = Var(name = 'topoetcone20',
                        path = 'muons',
                        xmin = -20,
                        xmax = 200,
                        log = False,
                        xmin2 = None,
                        xmax2 = None,
                        )

ptvarcone30 = Var(name = 'ptvarcone30',
                        path = 'muons',
                        xmin = -30,
                        xmax = 300,
                        log = False,
                        xmin2 = None,
                        xmax2 = None,
                        )

## Tau variables
## ---------------------------------------

tau_pt = Var(name = 'tau_pt',
              path    = 'taus',
              xmin    = 20,
              xmax    = 300,
              rebin   = 4,
              xmin2 = None,
              xmax2 = None,
              log     = False,
              )

m_trans_vs_sumcosdphi = Var(name = 'm_trans_vs_sumcosdphi',
				path = 'taus',
			        xmin = 0,
				xmax = 200,
				#rebin = 2,
				xmin2 = -2,
				xmax2 = 2,
				log = False,
				)	

met_reco_et_vs_sumcosdphi = Var(name = 'met_reco_et_vs_sumcosdphi',
                                path = 'taus',
                                xmin = 0,
                                xmax = 1000,
                                #rebin = 2,
                                xmin2 = -2,
                                xmax2 = 2,
                                log = False,
                                )

met_reco_et_vs_m_trans = Var(name = 'met_reco_et_vs_m_trans',
                                path = 'taus',
                                xmin = 0,
                                xmax = 1000,
                                #rebin = 4,
                                xmin2 = 1,
                                xmax2 = 200,
                                log = False,
                                )

tau_phi = Var(name = 'tau_phi',
              path    = 'taus',
              xmin    = -4,
              xmax    = 4,
              xmin2 = None,
              xmax2 = None,
             # rebin   = 2,
              log     = False,
              )
              
tau_eta = Var(name = 'tau_eta',
              path    = 'taus',
              xmin    = -3,
              xmax    = 3,
             # rebin   = 2,
              xmin2 = None,
              xmax2 = None,
	      log     = False,
              )

tau_n_tracks = Var(name = 'tau_n_tracks',
              path    = 'taus',
              xmin    = 0,
              xmax    = 5,
             # rebin   = 2,
              xmin2 = None,
              xmax2 = None,
              log     = False,
              )

jet_bdt_score = Var(name  = 'jet_bdt_score',
	     path = 'taus',
	     xmin = 0.6,
	     xmax = 1,
	     rebin = 1,
	     log = False,
             xmin2 = None,
             xmax2 = None,
	     )

HLT_tau_eta = Var(name = 'HLT_tau_eta',
             path = 'taus',
             xmin = -6.0,
             xmax = 6.0,
             log = False,
             xmin2 = None,
             xmax2 = None,
             )

HLT_tau_phi = Var(name = 'HLT_tau_phi',
             path = 'taus',
             xmin = -5.0,
             xmax = 5.0,
             log = False,
             xmin2 = None,
             xmax2 = None,
             )

HLT_tau_pt = Var(name = 'HLT_tau_pt',
             path = 'taus',
             xmin = 20,
             xmax = 300,
             rebin = 4,
             log = False,
             xmin2 = None,
             xmax2 = None,
             )

HLT_jet_bdt_score = Var(name = 'HLT_jet_bdt_score',
             path = 'taus',
             xmin = 0,
             xmax = 1.5,
             log = False,
             xmin2 = None,
             xmax2 = None,
             )

HLT_tau_n_tracks = Var(name = 'HLT_tau_n_tracks',
             path = 'taus',
             xmin = 0,
             xmax = 5,
             log = False,
             xmin2 = None,
             xmax2 = None,
             )
 
HLT_tau_n_wide_tracks = Var(name = 'HLT_tau_n_wide_tracks',
             path = 'taus',
             xmin = 0,
             xmax = 5,
             log = False,
             xmin2 = None,
             xmax2 = None,
             )

HLT_pt_res = Var(name = 'HLT_pt_res',
             path = 'taus',
             xmin = -0.2,
             xmax = 0.2,
             rebin = 2,
             log = False,
             xmin2 = None,
             xmax2 = None,
             )

Presel_tau_eta = Var(name = 'Presel_tau_eta',
             path = 'taus',
             xmin = -6.0,
             xmax = 6.0,
             log = False,
             xmin2 = None,
             xmax2 = None,
             )

Presel_tau_phi = Var(name = 'Presel_tau_phi',
             path = 'taus',
             xmin = -5.0,
             xmax = 5.0,
             log = False,
             xmin2 = None,
             xmax2 = None,
             )

Presel_tau_pt = Var(name = 'Presel_tau_pt',
             path = 'taus',
             xmin = 20,
             xmax = 300,
             rebin = 4,
             log = False,
             xmin2 = None,
             xmax2 = None,
             )

Presel_tau_n_tracks = Var(name = 'Presel_tau_n_tracks',
             path = 'taus',
             xmin = 0,
             xmax = 5,
             log = False,
             xmin2 = None,
             xmax2 = None,
             )
 
Presel_tau_n_wide_tracks = Var(name = 'Presel_tau_n_wide_tracks',
             path = 'taus',
             xmin = 0,
             xmax = 5,
             log = False,
             xmin2 = None,
             xmax2 = None,
             )
        
HLT_ratio_trkemsys_pt = Var(name = 'HLT_ratio_trkemsys_pt',
             path = 'taus',
             xmin = 0,
             xmax = 3,
	     rebin = 2,
             log = False,
             xmin2 = None,
             xmax2 = None,
             )

HLT_1P_frac_trks_iso_region = Var(name = 'HLT_1P_frac_trks_iso_region',
             path = 'taus',
             xmin = 0,
             xmax = 1,
	     rebin = 2,
             log = False,
             xmin2 = None,
             xmax2 = None,
             )

HLT_3P_trans_flightpath_sig = Var(name = 'HLT_3P_trans_flightpath_sig',
             path = 'taus',
             xmin = -10,
             xmax = 10,
	     rebin = 2,
             log = False,
             xmin2 = None,
             xmax2 = None,
             )

HLT_3P_massTrkSysCorrected = Var(name = 'HLT_3P_massTrkSysCorrected',
             path = 'taus',
             xmin = 0,
             xmax = 6000,
	     rebin = 2,
             log = False,
             xmin2 = None,
             xmax2 = None,
             )
HLT_m_trk_EM_system = Var(name = 'HLT_m_trk_EM_system',
             path = 'taus',
             xmin = 0,
             xmax = 6000,
	     rebin = 2,
             log = False,
             xmin2 = None,
             xmax2 = None,
             )

HLT_1P_lead_trk_IP_sig = Var(name = 'HLT_1P_lead_trk_IP_sig',
             path = 'taus',
             xmin = 0,
             xmax = 2,
	     rebin = 2,
             log = False,
             xmin2 = None,
             xmax2 = None,
             )

HLT_3P_dRmax = Var(name = 'HLT_3P_dRmax',
             path = 'taus',
             xmin = 0,
             xmax = 0.2,
	     rebin = 2,
             log = False,
             xmin2 = None,
             xmax2 = None,
             )
HLT_trk_radius = Var(name = 'HLT_trk_radius',
             path = 'taus',
             xmin = 0,
             xmax = 0.2,
	     rebin = 2,
             log = False,
             xmin2 = None,
             xmax2 = None,
             )

HLT_lead_trk_p_frac = Var(name = 'HLT_lead_trk_p_frac',
             path = 'taus',
             xmin = 0,
             xmax = 10,
	     rebin = 2,
             log = False,
             xmin2 = None,
             xmax2 = None,
             )

HLT_ratio_energy_to_trk_p = Var(name = 'HLT_ratio_energy_to_trk_p',
             path = 'taus',
             xmin = 0,
             xmax = 10,
	     rebin = 2,
             log = False,
             xmin2 = None,
             xmax2 = None,
             )

HLT_frac_EM_from_charged_pions = Var(name = 'HLT_frac_EM_from_charged_pions',
             path = 'taus',
             xmin = -1,
             xmax = 1,
	     rebin = 2,
             log = False,
             xmin2 = None,
             xmax2 = None,
             )

HLT_fcent = Var(name = 'HLT_fcent',
             path = 'taus',
             xmin = 0,
             xmax = 1,
	     rebin = 2,
             log = False,
             xmin2 = None,
             xmax2 = None,
             )

## MET variables
## ---------------------------------------
vis_mass = Var(name = 'vis_mass',
              path    = 'event',
              xmin    = 0,
              xmax    = 160,
              rebin   = 4,
              xmin2 = None,
              xmax2 = None,
              log     = False,
              )

sumcosdphi = Var(name = 'sumcosdphi',
              path    = 'event',
              xmin    = -2,
              xmax    = 2,
              #rebin   = 2,
              xmin2 = None,
              xmax2 = None,
              log     = False,
              )

lowsumcosdphi = Var(name = 'lowsumcosdphi',
              path    = 'event',
              xmin    = -2,
              xmax    = -0.6,
              #rebin   = 2,
              xmin2 = None,
              xmax2 = None,
              log     = False,
              )


m_trans = Var(name = 'm_trans',
              path    = 'event',
              xmin    = 0,
              xmax    = 200,
              xmin2 = None,
              xmax2 = None,
              rebin   = 4,
              log     = False,
              )

met_reco_et = Var(name = 'met_reco_et',
              path    = 'met',
              xmin    = 0,
              xmax    = 140,
              rebin   = 5,
              xmin2 = None,
              xmax2 = None,
              log     = False,
              )

met_reco_phi = Var(name = 'met_reco_phi',
              path    = 'met',
              xmin    = -3,
              xmax    = 3,
              rebin   = 2,
              xmin2 = None,
              xmax2 = None,
              log     = False,
              )

vars_list = []
vars_list.append(nmuons)
vars_list.append(mu_pt)
vars_list.append(tau_pt)
vars_list.append(met_reco_et)
vars_list.append(m_trans)
vars_list.append(lowsumcosdphi)
vars_list.append(sumcosdphi)
vars_list.append(vis_mass)
vars_list.append(n_vx)
vars_list.append(tau_phi)
vars_list.append(mu_phi)
vars_list.append(tau_eta)
vars_list.append(mu_eta)
vars_list.append(met_reco_phi)
vars_list.append(tau_n_tracks)
vars_list.append(jet_bdt_score) 
vars_list.append(n_bjets)
vars_list.append(n_jets)
vars_list.append(topoetcone20pt)
vars_list.append(ptvarcone30pt)
vars_list.append(ptvarcone30)
vars_list.append(topoetcone20)
vars_list.append(topoetcone20ptmev)
vars_list.append(ptvarcone30ptmev)
vars_list.append(ptvarcone30mev)
vars_list.append(topoetcone20mev)
vars_list.append(m_trans_vs_sumcosdphi)
vars_list.append(met_reco_et_vs_sumcosdphi)
vars_list.append(met_reco_et_vs_m_trans)
vars_list.append(pileup)
vars_list.append(HLT_tau_eta)
vars_list.append(HLT_tau_pt)
vars_list.append(HLT_tau_phi)
vars_list.append(HLT_tau_n_wide_tracks)
vars_list.append(HLT_tau_n_tracks)
vars_list.append(HLT_jet_bdt_score)
vars_list.append(HLT_pt_res)
vars_list.append(Presel_tau_eta)
vars_list.append(Presel_tau_pt)
vars_list.append(Presel_tau_phi)
vars_list.append(Presel_tau_n_wide_tracks)
vars_list.append(Presel_tau_n_tracks)
vars_list.append(HLT_ratio_trkemsys_pt)
vars_list.append(HLT_1P_frac_trks_iso_region)
vars_list.append(HLT_m_trk_EM_system)
vars_list.append(HLT_1P_lead_trk_IP_sig)
vars_list.append(HLT_trk_radius)
vars_list.append(HLT_lead_trk_p_frac)
vars_list.append(HLT_ratio_energy_to_trk_p)
vars_list.append(HLT_frac_EM_from_charged_pions)
vars_list.append(HLT_fcent)
vars_list.append(HLT_3P_dRmax)
vars_list.append(HLT_3P_massTrkSysCorrected)
vars_list.append(HLT_3P_trans_flightpath_sig)

vars_dict = {}
for var in vars_list: vars_dict[var.name] = var.__dict__


## EOF


