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
              )

n_vx = Var(name = 'n_vx',
              path    = 'event',
              xmin    = 0,
              xmax    = 14,
     #         rebin   = 0,
              log     = False,
              )

n_bjets = Var(name = 'n_bjets',
	      path = 'event',
	      xmin = 0,
	      xmax = 5,
	      log = False,
	      )

n_jets = Var(name = 'n_jets',
              path = 'event',
              xmin = 0,
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
              log     = False,
              )

mu_phi = Var(name = 'mu_phi',
              path    = 'muons',
              xmin    = -4,
              xmax    = 4,
              #rebin   = 2,
              log     = False,
              )

mu_eta = Var(name = 'mu_eta',
              path    = 'muons',
              xmin    = -3,
              xmax    = 3,
#              rebin   = 2,
              log     = False,
              )
              #

topoetcone20ptmev = Var(name = 'topoetcone20pt',
			path = 'muons',
			xmin = -0.5,
			xmax = 0.5,
			log = False,
			)

ptvarcone30ptmev = Var(name = 'ptvarcone30pt',
                        path = 'muons',
                        xmin = -0.5,
                        xmax = 0.5,
                        log = False,
                        )

topoetcone20mev = Var(name = 'topoetcone20',
                        path = 'muons',
                        xmin = -20000,
                        xmax = 200000,
                        log = False,
                        )

ptvarcone30mev = Var(name = 'ptvarcone30',
                        path = 'muons',
                        xmin = -30000,
                        xmax = 300000,
                        log = False,
                        )

topoetcone20pt = Var(name = 'topoetcone20pt',
			path = 'muons',
			xmin = -0.5,
			xmax = 0.5,
			log = False,
			)

ptvarcone30pt = Var(name = 'ptvarcone30pt',
                        path = 'muons',
                        xmin = -0.5,
                        xmax = 0.5,
                        log = False,
                        )

topoetcone20 = Var(name = 'topoetcone20',
                        path = 'muons',
                        xmin = -20,
                        xmax = 200,
                        log = False,
                        )

ptvarcone30 = Var(name = 'ptvarcone30',
                        path = 'muons',
                        xmin = -30,
                        xmax = 300,
                        log = False,
                        )

## Tau variables
## ---------------------------------------
tau_pt = Var(name = 'tau_pt',
              path    = 'taus',
              xmin    = 20,
              xmax    = 300,
              rebin   = 4,
              log     = False,
              )
tau_phi = Var(name = 'tau_phi',
              path    = 'taus',
              xmin    = -4,
              xmax    = 4,
             # rebin   = 2,
              log     = False,
              )
              
tau_eta = Var(name = 'tau_eta',
              path    = 'taus',
              xmin    = -3,
              xmax    = 3,
             # rebin   = 2,
	      log     = False,
              )

tau_n_tracks = Var(name = 'tau_n_tracks',
              path    = 'taus',
              xmin    = 0,
              xmax    = 5,
             # rebin   = 2,
              log     = False,
              )

jet_bdt_score = Var(name  = 'jet_bdt_score',
	     path = 'taus',
	     xmin = 0.6,
	     xmax = 1,
	     rebin = 1,
	     log = False,
	     )

## MET variables
## ---------------------------------------
vis_mass = Var(name = 'vis_mass',
              path    = 'event',
              xmin    = 0,
              xmax    = 160,
              rebin   = 4,
              log     = False,
              )

sumcosdphi = Var(name = 'sumcosdphi',
              path    = 'event',
              xmin    = -2,
              xmax    = 2,
              #rebin   = 2,
              log     = False,
              )

m_trans = Var(name = 'm_trans',
              path    = 'event',
              xmin    = 0,
              xmax    = 200,
              rebin   = 4,
              log     = False,
              )

met_reco_et = Var(name = 'met_reco_et',
              path    = 'met',
              xmin    = 0,
              xmax    = 140,
              rebin   = 5,
              log     = False,
              )

met_reco_phi = Var(name = 'met_reco_phi',
              path    = 'met',
              xmin    = -3,
              xmax    = 3,
              rebin   = 2,
              log     = False,
              )

vars_list = []
vars_list.append(nmuons)
vars_list.append(mu_pt)
vars_list.append(tau_pt)
vars_list.append(met_reco_et)
vars_list.append(m_trans)
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

vars_dict = {}
for var in vars_list: vars_dict[var.name] = var.__dict__


## EOF


