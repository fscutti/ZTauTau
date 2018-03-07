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
    
    is_treesys, is_wtsys = False, False
    sys_tree = [
    "MUON_ID_1down",
    "MUON_ID_1up",
    "MUON_MS_1down",
    "MUON_MS_1up",
    "MUON_SAGITTA_RESBIAS_1down",
    "MUON_SAGITTA_RESBIAS_1up",
    "MUON_SAGITTA_RHO_1down",
    "MUON_SAGITTA_RHO_1up",
    "MUON_SCALE_1down",
    "MUON_SCALE_1up",
    "EG_RESOLUTION_ALL_1down",
    "EG_RESOLUTION_ALL_1up",
    "EG_SCALE_ALLCORR_1down",
    "EG_SCALE_ALLCORR_1up",
    "EG_SCALE_E4SCINTILLATOR_1down",
    "EG_SCALE_E4SCINTILLATOR_1up",
    "EG_SCALE_LARCALIB_EXTRA2015PRE_1down",
    "EG_SCALE_LARCALIB_EXTRA2015PRE_1up",
    "EG_SCALE_LARTEMPERATURE_EXTRA2015PRE_1down",
    "EG_SCALE_LARTEMPERATURE_EXTRA2015PRE_1up",
    "EG_SCALE_LARTEMPERATURE_EXTRA2016PRE_1down",
    "EG_SCALE_LARTEMPERATURE_EXTRA2016PRE_1up",
    "TAUS_TRUEHADTAU_SME_TES_DETECTOR_1down",
    "TAUS_TRUEHADTAU_SME_TES_DETECTOR_1up",
    "TAUS_TRUEHADTAU_SME_TES_INSITU_1down",
    "TAUS_TRUEHADTAU_SME_TES_INSITU_1up",
    "TAUS_TRUEHADTAU_SME_TES_MODEL_1down",
    "TAUS_TRUEHADTAU_SME_TES_MODEL_1up",
    "MET_SoftTrk_ResoPara",
    "MET_SoftTrk_ResoPerp",
    "MET_SoftTrk_ScaleDown",
    "MET_SoftTrk_ScaleUp",
    ]
    if sys:
        for syst in sys_tree:
            if sys in syst:
                is_treesys = True

    sys_wt = [
    "TauEffSF_reco",
    "TauEffSF_JetBDTmedium",
    "TauEffSF_HadTauEleOLR_tauhad",
    "MuEffSF_TTVA",
    "MuEffSF_Reco_QualMedium",
    "MuEffSF_IsoGradient",
    "MuEffSF_IsoLoose",
    "EleEffSF_offline_RecoTrk",
    "EleEffSF_offline_MediumLLH_d0z0_v11",
    "EleEffSF_Isolation_MediumLLH_d0z0_v11_isolGradient",
    "EleEffSF_Isolation_MediumLLH_d0z0_v11_isolLoose",
    "MuEffSF_HLT_mu20_iloose_L1MU15_OR_HLT_mu40_QualMedium_IsoNone",
    "MuEffSF_HLT_mu26_ivarmedium_OR_HLT_mu50_QualMedium_IsoNone",
    "EleEffSF_SINGLE_E_2015_e24_lhmedium_L1EM20VH_OR_e60_lhmedium_OR_e120_lhloose_2016_e26_lhtight_nod0_ivarloose_OR_e60_lhmedium_nod0_OR_e140_lhloose_nod0_MediumLLH_d0z0_v11_isolGradient",
    #"global_effSF_MVX",
    #"global_ineffSF_MVX",
    #"central_jets_global_effSF_JVT",
    ]
    if sys and not is_treesys:
        for syst in sys_wt:
            if 'down' in sys:
                dirn = '1down_'
            elif 'up' in sys:
                dirn = '1up_'
            if syst in sys:
                is_wtsys = True
    
    #print '_'.join(sys.split('_')[:-1])
    if   sys == None: sys_dict = get_sys_dict()
    # This is how you tell the weights what is the direction of the variation
    # Within the weight implementation, an alternative branch has to be retrieved for SYS_XX weights,
    # based on the value of sys_var, while for TREE_SYS_XX no preconfiguartion of sys_var is necessary.
    elif sys == 'SYS_UP':            sys_dict = get_sys_dict(sys_name = sys, sys_var = "up")
    elif sys == 'SYS_UP':            sys_dict = get_sys_dict(sys_name = sys, sys_var = "dn")
    elif sys == 'TREESYS_UP':        sys_dict = get_sys_dict(sys_name = sys, sys_tree = "MySysTreeName",  sys_var = "up")
    elif sys == 'TREESYS_DN':        sys_dict = get_sys_dict(sys_name = sys, sys_tree = "MySysTreeName",  sys_var = "dn")
    elif is_treesys or is_wtsys:
        if 'up' in sys:
            sys_dir = 'up'
        elif 'down' in sys:
            sys_dir = 'dn'
        if is_treesys:
            sys_dict = get_sys_dict(sys_tree = sys,       sys_friendtree = "NN_"+sys,    sys_var = sys_dir)
        else:
            sys_dict = get_sys_dict(sys_tree = 'NOMINAL', sys_friendtree = "NN_NOMINAL", sys_var = sys)
    else: 
        assert False, "Invalid sys %s!"%(sys)
    
    ## build chain
    config['tree'] = sys_dict['tree']
    config['friendtree'] = sys_dict['friendtree'] 
    
    chain = ROOT.TChain(config['tree'])
    for fn in config['input']: chain.Add(fn)
    print config
    if 'friendinput' in config.keys():
        if config['friendinput']: 
          assert config['friendtree'], 'ERROR: name of friendtree not provided for friendfile %s'%config['friendinput']
          chain.AddFriend(config['friendtree'],config['friendinput'])

    ##-------------------------------------------------------------------------
    ## event loop
    ##-------------------------------------------------------------------------
    loop = pyframe.core.EventLoop(name='ztautau',
                                  sampletype=config['sampletype'],
                                  samplename=config['samplename'],
                                  friendtree=config['friendtree'],
                                  outfile=config['samplename']+".root",
                                  quiet=False,
                                  )

    ## start preselection cutflow 
    ## ---------------------------------------
    loop += pyframe.algs.CutFlowAlg(key='PreselMu2016')
    
    ## weights
    ## +++++++++++++++++++++++++++++++++++++++
    isSig = False
    for x in [345078,345124,345077,345125,345213,345214,345215,345216,345218,345219,341123,341156,345121,345122,345074,345075,345211,345212,345217]:
        dsid = config['input'][0].split('/')[-2].split('.')
        if str(x) in dsid:
            #print x, dsid
            isSig=True
    loop += ztautau.algs.weights.WeightTotal(cutflow='PreselMu2016',key='weight_total', isSig=isSig)
    if config['datatype'] == 'ff': 
        #loop += ztautau.algs.weights.FFTotal_New(cutflow='PreselMu2016',key='FF_presel', 
        #                                         ff_file='/coepp/cephfs/share/atlas/LFV/FF/LFV/SM_like/FF_nominal.root', 
        #                                         r_file ='/coepp/cephfs/share/atlas/LFV/FF/LFV/SM_like/R_nominal.root' ,
        #                                         isfilter=True)
        loop += ztautau.algs.weights.FFTotal_New(cutflow='PreselMu2016',key='FF_presel', 
                                                 ff_file='/coepp/cephfs/share/atlas/LFV/phuong/fakefactors/FF_medium.root', 
                                                 r_file ='/coepp/cephfs/share/atlas/LFV/phuong/fakefactors/R_medium.root' ,
                                                 isfilter=False)
        loop += ztautau.algs.weights.FFTotal_New(cutflow='PreselMu2016',key='FF_sr1',    
                                                 ff_file='/coepp/cephfs/share/atlas/LFV/phuong/fakefactors/FF_medium.root', 
                                                 r_file ='/coepp/cephfs/share/atlas/LFV/phuong/fakefactors/R_medium.root' ,
                                                 isfilter=False)
        loop += ztautau.algs.weights.FFTotal_New(cutflow='PreselMu2016',key='FF_sr2',    
                                                 ff_file='/coepp/cephfs/share/atlas/LFV/phuong/fakefactors/FF_medium.root', 
                                                 r_file ='/coepp/cephfs/share/atlas/LFV/phuong/fakefactors/R_medium.root' ,
                                                 isfilter=False)
        loop += ztautau.algs.weights.FFTotal_New(cutflow='PreselMu2016',key='FF_sr3',    
                                                 ff_file='/coepp/cephfs/share/atlas/LFV/phuong/fakefactors/FF_medium.root', 
                                                 r_file ='/coepp/cephfs/share/atlas/LFV/phuong/fakefactors/R_medium.root' ,
                                                 isfilter=False)


    ## initialize and/or decorate objects
    ## ---------------------------------------
    #loop += ztautau.algs.vars.Vars()

    ## cuts
    ## +++++++++++++++++++++++++++++++++++++++
    #loop += ztautau.algs.algs.CutAlg(cutflow='presel',cut='AtLeastOneMuon') 

    
    ## weights configuration
    ## ---------------------------------------
    ## event
    ## +++++++++++++++++++++++++++++++++++++++
    
    
    ## objects
    ## +++++++++++++++++++++++++++++++++++++++
    loop += ztautau.algs.weights.ObjWeight(
            obj_name    = "tau_0",
            branch_name = "TauEffSF_reco",
            key         = "TauReco",
            scale       = sys_dict["variation"],
            )
    loop += ztautau.algs.weights.ObjWeight(
            obj_name    = "tau_0",
            branch_name = "TauEffSF_JetBDTmedium",
            key         = "TauIDMedium",
            scale       = sys_dict['variation'],
            )
    #loop += ztautau.algs.weights.ObjWeight(
    #        obj_name    = "tau_0",
    #        branch_name = "TauEffSF_JetBDTloose",
    #        key         = "TauLoose",
    #        scale       = sys_dict["variation"],
    #        )
    loop += ztautau.algs.weights.ObjWeight(
            obj_name    = "tau_0",
            branch_name = "TauEffSF_HadTauEleOLR_tauhad",
            key         = "TauEVetoMu",
            scale       = sys_dict["variation"],
            )
    loop += ztautau.algs.weights.ObjWeight(
            obj_name    = "tau_0",
            branch_name = "TauEffSF_MediumEleBDTPlusVeto_electron",
            key         = "TauEVetoEl1p",
            scale       = sys_dict["variation"],
            )
    loop += ztautau.algs.weights.ObjWeight(
            obj_name    = "tau_0",
            branch_name = "TauEffSF_VeryLooseLlhEleOLR_electron",
            key         = "TauEVetoEl3p",
            scale       = sys_dict["variation"],
            )
    loop += ztautau.algs.weights.ObjWeight(
            obj_name    = "lep_0",
            branch_name = "MuEffSF_TTVA",
            key         = "MuonTTVA",
            scale       = sys_dict["variation"],
            )
    loop += ztautau.algs.weights.ObjWeight(
            obj_name    = "lep_0",
            branch_name = "MuEffSF_Reco_QualMedium",
            key         = "MuonRecoID",
            scale       = sys_dict["variation"],
            )
    loop += ztautau.algs.weights.ObjWeight(
            obj_name    = "lep_0",
            branch_name = "MuEffSF_IsoGradient",
            key         = "MuonIsoGrad",
            scale       = sys_dict["variation"],
            )
    loop += ztautau.algs.weights.ObjWeight(
            obj_name    = "lep_0",
            branch_name = "MuEffSF_IsoLoose",
            key         = "MuonIsoLoose",
            scale       = sys_dict["variation"],
            )
    loop += ztautau.algs.weights.ObjWeight(
            obj_name    = "lep_0",
            branch_name = "EleEffSF_offline_RecoTrk",
            key         = "ElecRecoTrk",
            scale       = sys_dict["variation"],
            )
    loop += ztautau.algs.weights.ObjWeight(
            obj_name    = "lep_0",
            branch_name = "EleEffSF_offline_MediumLLH_d0z0_v11",
            key         = "ElecID",
            scale       = sys_dict["variation"],
            )
    loop += ztautau.algs.weights.ObjWeight(
            obj_name    = "lep_0",
            branch_name = "EleEffSF_Isolation_MediumLLH_d0z0_v11_isolGradient",
            key         = "ElecIsoGrad",
            scale       = sys_dict["variation"],
            )
    loop += ztautau.algs.weights.ObjWeight(
            obj_name    = "lep_0",
            branch_name = "EleEffSF_Isolation_MediumLLH_d0z0_v11_isolLoose",
            key         = "ElecIsoLoose",
            scale       = sys_dict["variation"],
            )
    loop += ztautau.algs.weights.ObjWeight(
            obj_name    = "lep_0",
            branch_name = "MuEffSF_HLT_mu20_iloose_L1MU15_OR_HLT_mu40_QualMedium_IsoNone",
            key         = "MuonTrig2015",
            scale       = sys_dict["variation"],
            )
    loop += ztautau.algs.weights.ObjWeight(
            obj_name    = "lep_0",
            branch_name = "MuEffSF_HLT_mu26_ivarmedium_OR_HLT_mu50_QualMedium_IsoNone",
            key         = "MuonTrig2016",
            scale       = sys_dict["variation"],
            )
    loop += ztautau.algs.weights.ObjWeight(
            obj_name    = "lep_0",
            branch_name = "EleEffSF_SINGLE_E_2015_e24_lhmedium_L1EM20VH_OR_e60_lhmedium_OR_e120_lhloose_2016_e26_lhtight_nod0_ivarloose_OR_e60_lhmedium_nod0_OR_e140_lhloose_nod0_MediumLLH_d0z0_v11_isolGradient",
            key         = "ElecTrig2015",
            scale       = sys_dict["variation"],
            )
    loop += ztautau.algs.weights.ObjWeight(
            obj_name    = "lep_0",
            branch_name = "EleEffSF_SINGLE_E_2015_e24_lhmedium_L1EM20VH_OR_e60_lhmedium_OR_e120_lhloose_2016_e26_lhtight_nod0_ivarloose_OR_e60_lhmedium_nod0_OR_e140_lhloose_nod0_MediumLLH_d0z0_v11_isolGradient",
            key         = "ElecTrig2016",
            scale       = sys_dict["variation"],
            )
    loop += ztautau.algs.weights.ObjWeight(
            obj_name    = "jet",
            branch_name = "global_effSF_MVX",
            key         = "JetEff",
            scale       = sys_dict["variation"],
            )
    loop += ztautau.algs.weights.ObjWeight(
            obj_name    = "jet",
            branch_name = "global_ineffSF_MVX",
            key         = "JetIneff",
            scale       = sys_dict["variation"],
            )
    loop += ztautau.algs.weights.ObjWeight(
            obj_name    = "jet",
            branch_name = "central_jets_global_effSF_JVT",
            key         = "JetJVTEff",
            scale       = sys_dict["variation"],
            )
    loop += ztautau.algs.weights.ObjWeight(
            obj_name    = "jet",
            branch_name = "central_jets_global_ineffSF_JVT",
            key         = "JetJVTIneff",
            scale       = sys_dict["variation"],
            )
    loop += ztautau.algs.weights.ObjWeight(
            obj_name    = "jet",
            branch_name = "forward_jets_global_effSF_JVT",
            key         = "JetJVTFwdEff",
            scale       = sys_dict["variation"],
            )
    loop += ztautau.algs.weights.ObjWeight(
            obj_name    = "jet",
            branch_name = "forward_jets_global_ineffSF_JVT",
            key         = "JetJVTFwdIneff",
            scale       = sys_dict["variation"],
            )
    


    ### configure histograms
    ### ---------------------------------------
    #hist_list = []
    #hist_list += ztautau.hists.Main_hists.hist_list
    #hist_presel = []
    #hist_presel += ztautau.hists.Main_hists.hist_presel
    #hist_list += ztautau.hists.H2D_hists.hist_list
   


    ##-------------------------------------------------------------------------
    ## make plots
    ##-------------------------------------------------------------------------
    
    if not 'datatype' in config.keys():
        suffix = '_'
    else:
        if config['datatype'] == 'qcd': 
            suffix = '_antiiso'
        elif config['datatype'] == 'osw':
            suffix = '_osaidcr'
        elif config['datatype'] == 'ssw':
            suffix = '_sswjtcr'
        else:
            suffix = '_'

    def replace_cut(cuts, rm_cut, add_cut):
        newcuts = []
        count = False
        for cut in cuts:
            if cut == rm_cut:
                if add_cut: newcuts.append(add_cut)
                count = True
            else: newcuts.append(cut)
        if not count:
            raise ValueError ("Cut %s not found! Please look into this!" % rm_cut[0])
        return newcuts

    import itertools as it
    chan = ['mu', 'el']
    year = ['15', '16']
    trck = ['1p', '3p']
    comb = list(it.product(chan, year, trck))
    cutflow = {'mu': {'15': {'1p': [], '3p': []}, '16': {'1p': [], '3p': []}}, 'el': {'15': {'1p': [], '3p': []}, '16': {'1p': [], '3p': []}}}
    ## Canonical region name
    regname = {'mu': {'15': {'1p': [], '3p': []}, '16': {'1p': [], '3p': []}}, 'el': {'15': {'1p': [], '3p': []}, '16': {'1p': [], '3p': []}}}
    for c in comb:
        lep  = 'Muon' if c[0] == 'mu' else 'Elec' if c[0] =='el' else None
        if lep == 'Muon':
            lepsf    = ['MuonRecoID']
            tauevsf  = ['TauEVetoMu']
        else:
            lepsf    = ['ElecRecoTrk', 'ElecID' ]
            tauevsf  = ['TauEVetoEl%s' % c[2]]

        cutflow[c[0]][c[1]][c[2]] += [[c[2]                      , None ],
                                      ['%sOnly' % lep            , None ],
                                      #['TrueTau'                , #None ],
                                      ['20%s%sTrig' % (c[1],lep) , ['%sTrig20%s' % (lep,c[1])] ],
                                      ['PVX'                     , None ],
                                      ['LepQual'                 , lepsf ],
                                      ['LepIso'                  , ['%sIsoGrad' % lep] ],
                                      ['TauQual'                 , ['TauReco'] ],
                                      ['OS'                      , None ],
                                      ['TauID'                   , ['TauIDMedium'] ],
                                      ['NoJetFake'               , None ],
                                      ['LepPt'                   , None ],
                                      ['TauPt'                   , None ],
                                      ['tauEveto'                , tauevsf ],
                                      ['SCDP'                    , None ],
                                      ]
        regname[c[0]][c[1]][c[2]] = c[0]+c[1]+c[2]
        if not config['datatype'] == 'main':
            cutflow[c[0]][c[1]][c[2]] = replace_cut(cutflow[c[0]][c[1]][c[2]], ['NoJetFake', None], ['IsJetFake', None])
        if  config['datatype'] == 'qcd': 
            cutflow[c[0]][c[1]][c[2]] = replace_cut(cutflow[c[0]][c[1]][c[2]], ['LepIso', ['%sIsoGrad' % lep]], ['LepAntiIso',   None])
        elif config['datatype'] == 'osw':
            cutflow[c[0]][c[1]][c[2]] = replace_cut(cutflow[c[0]][c[1]][c[2]], ['TauID',  ['TauIDMedium']],     ['TauLooseNMed', None])
        elif config['datatype'] == 'ssw':
            cutflow[c[0]][c[1]][c[2]] = replace_cut(cutflow[c[0]][c[1]][c[2]], ['OS', None], ['SS', None])
            cutflow[c[0]][c[1]][c[2]] = replace_cut(cutflow[c[0]][c[1]][c[2]], ['TauID',  ['TauIDMedium']],     ['TauLoose',     None])
        elif config['datatype'] == 'ff' :
            cutflow[c[0]][c[1]][c[2]] = replace_cut(cutflow[c[0]][c[1]][c[2]], ['TauID',  ['TauIDMedium']],     ['TauAntiID',    None])
        #if not isSig:
        #    cutflow[c[0]][c[1]][c[2]] = replace_cut(cutflow[c[0]][c[1]][c[2]], ['TrueTau', None ], ['TrueTauNotSig', None])

        #print cutflow[c[0]][c[1]][c[2]]

    ## ---------------------------------------
    print "Running over SR"
    jetsf = ['JetEff', 'JetIneff', 'JetJVTEff', 'JetJVTIneff', 'JetJVTFwdEff', 'JetJVTFwdIneff']
    #jetsf = None
    if config['datatype'] == 'ff': 
        ff = {'presel': ['FF_presel']+jetsf, 'sr1': ['FF_sr1']+jetsf, 'sr2': ['FF_sr2']+jetsf, 'sr3': ['FF_sr3']+jetsf}
    else:
        ff = {'presel': jetsf, 'sr1': jetsf, 'sr2': jetsf, 'sr3': jetsf}
    #ff = {'presel': None, 'sr1': None, 'sr2': None, 'sr3': None}
    for c in comb:
        loop += ztautau.algs.algs.PlotAlg(
                region       = 'presel'+suffix+regname[c[0]][c[1]][c[2]],
                do_var_check = True,
                #hist_list    = ztautau.hists.Main_hists.hist_presel,
                hist_list    = ztautau.hists.Main_hists.hist_fit,
                plot_all     = False,
                cut_flow  =  cutflow[c[0]][c[1]][c[2]]+[['Presel', ff['presel']]],
                )
        loop += ztautau.algs.algs.PlotAlg(
                region       = 'sr1'+suffix+regname[c[0]][c[1]][c[2]],
                do_var_check = True,
                #hist_list    = ztautau.hists.Main_hists.hist_presel,
                hist_list    = ztautau.hists.Main_hists.hist_fit,
                plot_all     = False,
                cut_flow  =  cutflow[c[0]][c[1]][c[2]]+[['SR1', ff['sr1']]],
                )
        loop += ztautau.algs.algs.PlotAlg(
                region       = 'sr2'+suffix+regname[c[0]][c[1]][c[2]],
                do_var_check = True,
                #hist_list    = ztautau.hists.Main_hists.hist_presel,
                hist_list    = ztautau.hists.Main_hists.hist_fit,
                plot_all     = False,
                cut_flow  =  cutflow[c[0]][c[1]][c[2]]+[['SR2', ff['sr2']]],
                )
        loop += ztautau.algs.algs.PlotAlg(
                region       = 'sr3'+suffix+regname[c[0]][c[1]][c[2]],
                do_var_check = True,
                #hist_list    = ztautau.hists.Main_hists.hist_presel,
                hist_list    = ztautau.hists.Main_hists.hist_fit,
                plot_all     = False,
                cut_flow  =  cutflow[c[0]][c[1]][c[2]]+[['SR3', ff['sr3']]],
                )

    print "Starting copy"
    loop += pyframe.algs.HistCopyAlg()
    print "Copy done"

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

