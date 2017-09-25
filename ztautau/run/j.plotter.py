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

#_____________________________________________________________________________
def get_sys_dict(sys_name=None, sys_tree="NOMINAL",sys_friendtree="NN_NOMINAL", sys_var=None):
  return {"name":sys_name, "tree":sys_tree, "friendtree":sys_friendtree, "variation":sys_var}
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
    config['tree']       = sys_dict['tree']
    config['friendtree'] = sys_dict['friendtree'] 

    chain = ROOT.TChain(config['tree'])
    for fn in config['input']: chain.Add(fn)
    if config['friendinput']: 
      assert config['friendtree'], 'ERROR: name of friendtree not provided for friendfile %s'%config['friendinput']
      chain.AddFriend(config['friendtree'],config['friendinput'])

    ##-------------------------------------------------------------------------
    ## event loop
    ##-------------------------------------------------------------------------
    loop = pyframe.core.EventLoop(name='ztautau',
                                  sampletype=config['sampletype'],
                                  samplename=config['samplename'],
                                  outfile=config['samplename']+".root",
                                  quiet=False,
                                  )

    ## start preselection cutflow 
    ## ---------------------------------------
    loop += pyframe.algs.CutFlowAlg(key='presel')
    
    ## weights
    ## +++++++++++++++++++++++++++++++++++++++
    loop += ztautau.algs.weights.WeightTotal(cutflow='presel',key='weight_total')


    ## initialize and/or decorate objects
    ## ---------------------------------------
    loop += ztautau.algs.vars.Vars()

    ## cuts
    ## +++++++++++++++++++++++++++++++++++++++
    loop += ztautau.algs.algs.CutAlg(cutflow='presel',cut='AtLeastOneMuon') 

    
    ## weights configuration
    ## ---------------------------------------
    ## event
    ## +++++++++++++++++++++++++++++++++++++++
    
    
    ## objects
    ## +++++++++++++++++++++++++++++++++++++++
    loop += ztautau.algs.weights.ObjWeight(
            obj_name    = "tau_0",
            branch_name = "TauEffSF_JetBDTmedium",
            key         = "TauID",
            scale       = None,
            )
    


    ## configure histograms
    ## ---------------------------------------
    hist_list = []
    hist_list += ztautau.hists.Main_hists.hist_list
    hist_list += ztautau.hists.H2D_hists.hist_list
   


    ##-------------------------------------------------------------------------
    ## make plots
    ##-------------------------------------------------------------------------
    
    ## TEST region
    ## ---------------------------------------
    loop += ztautau.algs.algs.PlotAlg(
            region       = 'TEST',
            do_var_check = True,
            hist_list    = hist_list,
            plot_all     = False,
            cut_flow  = [
                          ['AtLeastOneMuon',["TauID"]],
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



