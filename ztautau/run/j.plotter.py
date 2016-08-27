#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
j.postprocessor.py
"""

## std modules
import os,re

## ROOT
import ROOT
ROOT.gROOT.SetBatch(True)

## my modules
import pyframe

## local modules
import ztautau

#GeV = 1000.0

#_____________________________________________________________________________
def get_sys_dict(sys_name=None, sys_tree="NOMINAL", sys_var=None):
  return {"name":sys_name, "tree":sys_tree, "variation":sys_var}

#_____________________________________________________________________________
def analyze(config):
  
    ##-------------------------------------------------------------------------
    ## setup
    ##-------------------------------------------------------------------------
    config['do_var_log'] = True
    main_path = os.getenv('MAIN')
    

    ##-------------------------------------------------------------------------
    ## systematics 
    ##-------------------------------------------------------------------------
    
    """
    pass systematics on the command line like this:
    python j.plotter.py --config="sys:SYS_UP"
    """
    config.setdefault('sys',None)

    sys = config['sys']
    
    """
    IMPORTANT: no not really. This docstring is useless
    https://www.youtube.com/watch?v=sjJBpw5WNtU
    """

    sys_dict = None
    
    if   sys == None: sys_dict = get_sys_dict()
    
    # this is how you tell the weights 
    # what is the direction of the variation
    elif sys == 'SYS_UP':     sys_dict = get_sys_dict(sys_name = sys, sys_var = "up")
    elif sys == 'SYS_UP':     sys_dict = get_sys_dict(sys_name = sys, sys_var = "dn")
    elif sys == 'TREESYS_UP': sys_dict = get_sys_dict(sys_name = sys, sys_tree = "MySysTreeName", sys_var = "up")
    elif sys == 'TREESYS_DN': sys_dict = get_sys_dict(sys_name = sys, sys_tree = "MySysTreeName", sys_var = "dn")
    elif sys == 'MUID_DN':    sys_dict = get_sys_dict(sys_name = sys, sys_tree = "MUONS_ID_1down", sys_var = "dn")
    else: 
        assert False, "Invalid sys %s!"%(sys)
    
    ## build chain
    config['tree'] = sys_dict['tree']
    
    chain = ROOT.TChain(config['tree'])
    for fn in config['input']: chain.Add(fn)

    ##-------------------------------------------------------------------------
    ## event loop
    ##-------------------------------------------------------------------------
    loop = pyframe.core.EventLoop(name='ztautau',
                                  sampletype=config['sampletype'],
                                  outfile='ntuple.root',
                                  quiet=False,
                                  )
    
    ## build and pt-sort objects
    ## ---------------------------------------
    #loop += pyframe.algs.ListBuilder(
    #    prefixes = ['lep_0_','tau_0_','jet_0_'],
    #    keys = ['muons','taus','jets'],
    #    )
    #loop += pyframe.algs.AttachTLVs(
    #    keys = ['muons','taus','jets'],
    #    )
    # just a decoration of particles ...
    #loop += ztautau.algs.vars.ParticlesBuilder(
    #    key='muons',
    #    )
    
    """
    ## build MET
    ## ---------------------------------------
    loop += ztautau.algs.met.METCLUS(
        prefix='metFinalClus',
        key = 'met_clus',
        )
    loop += ztautau.algs.met.METTRK(
        prefix='metFinalTrk',
        key = 'met_trk',
        )
   
    ## initialize and/or decorate objects
    ## ---------------------------------------
    loop += ztautau.algs.vars.PairsBuilder(
        obj_keys=['muons'],
        pair_key='mu_pairs',
        met_key='met_clus', 
        )
    """ 

    ## start preselection cutflow 
    ## ---------------------------------------
    loop += pyframe.algs.CutFlowAlg(key='presel')
    
    ## weights
    ## +++++++++++++++++++++++++++++++++++++++
    #loop += ztautau.algs.weights.MCEventWeight(cutflow='presel',key='weight_mc_event')
    #loop += ztautau.algs.weights.Pileup(cutflow='presel',key='weight_pileup')
    loop += ztautau.algs.weights.WeightTotal(cutflow='presel',key='weight_total')
   
    ## cuts
    ## +++++++++++++++++++++++++++++++++++++++
    #loop += ztautau.algs.algs.CutAlg(cutflow='presel',cut='AtLeastOneMuon') 

    
    ## weights configuration
    ## ---------------------------------------
    ## event
    ## +++++++++++++++++++++++++++++++++++++++
    """ 
    loop += ztautau.algs.EvWeights.MuTrigSF(
            is_single_mu = True,
            mu_trig_level="Loose_Loose",
            mu_trig_chain="HLT_mu20_iloose_L1MU15_OR_HLT_mu50",
            key='SingleMuonTrigSF',
            scale=None,
            )
    
    """
    """
    loop += ztautau.algs.EvWeights.MuTrigSF(
            is_di_mu = True,
            mu_trig_level="Loose_Loose",
            mu_trig_chain="HLT_2mu10",
            key='DiMuonTrigSF',
            scale=None,
            )
    """ 
    ## objects
    ## +++++++++++++++++++++++++++++++++++++++
    """
    loop += ztautau.algs.ObjWeights.MuAllSF(
            #mu_level="Tight",
            mu_index=0,
            key='MuLeadAllSF',
            scale=None,
            )
    loop += ztautau.algs.ObjWeights.MuAllSF(
            #mu_level="NotTight",
            mu_index=1,
            key='MuSubLeadAllSF',
            scale=None,
            )
    """ 
    ##-------------------------------------------------------------------------
    ## make plots
    ##-------------------------------------------------------------------------
    
    ## TEST region
    ## ---------------------------------------
    loop += ztautau.algs.algs.PlotAlg(
            region    = 'TEST',
            plot_all  = False,
            cut_flow  = [
              ['AtLeastOneMuon',None],
              ['MuonPt24',None],
              ],
            )
    
    loop += pyframe.algs.HistCopyAlg()

    ##-------------------------------------------------------------------------
    ## run the job
    ##-------------------------------------------------------------------------
    loop.run(chain, 0, config['events'],
            branches_on_file = config.get('branches_on_file'),
            do_var_log = config.get('do_var_log'),
            )
#______________________________________________________________________________
if __name__ == '__main__':
    pyframe.config.main(analyze)



