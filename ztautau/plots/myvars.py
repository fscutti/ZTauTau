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

## Muon variables
## ---------------------------------------
mu_pt = Var(name = 'mu_pt',
              path    = 'muons',
              xmin    = 0,
              xmax    = 150,
              rebin   = 10,
              log     = False,
              )

## Tau variables
## ---------------------------------------
tau_pt = Var(name = 'tau_pt',
              path    = 'taus',
              xmin    = 0,
              xmax    = 150,
              rebin   = 10,
              log     = False,
              )

## MET variables
## ---------------------------------------
met_reco_et = Var(name = 'met_reco_et',
              path    = 'met',
              xmin    = 0,
              xmax    = 150,
              rebin   = 10,
              log     = False,
              )



vars_list = []
vars_list.append(nmuons)
vars_list.append(mu_pt)
vars_list.append(tau_pt)
vars_list.append(met_reco_et)

vars_dict = {}
for var in vars_list: vars_dict[var.name] = var.__dict__


## EOF


