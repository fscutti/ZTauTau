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
              xmin    = 0,
              xmax    = 150,
              rebin   = 4,
              log     = False,
              )

mu_phi = Var(name = 'mu_phi',
              path    = 'muons',
              xmin    = -3,
              xmax    = 3,
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
              

## Tau variables
## ---------------------------------------
tau_pt = Var(name = 'tau_pt',
              path    = 'taus',
              xmin    = 0,
              xmax    = 150,
              rebin   = 4,
              log     = False,
              )
tau_phi = Var(name = 'tau_phi',
              path    = 'taus',
              xmin    = -3,
              xmax    = 3,
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
              rebin   = 2,
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
              rebin   = 10,
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

vars_dict = {}
for var in vars_list: vars_dict[var.name] = var.__dict__


## EOF


