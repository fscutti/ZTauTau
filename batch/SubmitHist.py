# encoding: utf-8
'''
SubmitHist.py
'''

## modules
import os, sys
import re
import subprocess
import time
from   ztautau.samples import samples

#_____________________________________________________________________________
def prepare_path(path):
    if not os.path.exists(path):
        #print 'preparing outpath: %s'%(path)
        os.makedirs(path)

#_____________________________________________________________________________
def sys_conf(name=None, main_path_mod=None,friend_path_mod=None,samples=None,nominal=None):
    return {"name":name, "main_path_mod":main_path_mod, "friend_path_mod":friend_path_mod,"samples":samples}

from optparse import OptionParser

#-----------------
# input
#-----------------
parser = OptionParser()
parser.add_option('-r', '--runscript', dest='runscript',
                  help='plotter script to run [presel, ac, tight]', default=None)
parser.add_option('-t', '--type', dest='datatype',
                  help='type of data to run [main, osw, ssw, qcd, ff, all]', default=None)
parser.add_option('-s', '--dosys', dest='DO_SYS', action="store_true",
                  help='do systematics?', default=False)
parser.add_option('-n', '--donom', dest='DO_NOM', action="store_true",
                  help='do nominal?', default=True)
parser.add_option('-m', '--inclmc', dest='INCLMC', action="store_true",
                  help='include mc?', default=False)
parser.add_option('-d', '--incldata', dest='INCLDATA', action="store_true",
                  help='include data?', default=False)


(options, args) = parser.parse_args()


## environment variables
## ---------------------
MAIN        = os.getenv('MAIN')                           # upper folder
USER        = os.getenv('USER')
NTUP        = '/coepp/cephfs/share/atlas/LFV/july_redown'        # global config input NTUP path
#FRIENDPATH  = '/coepp/cephfs/share/atlas/LFV/base_test_july_evtnofix' # path where friend input is located; same "granularity as NTUP"
#FRIENDPATH  = '/coepp/cephfs/share/atlas/LFV/bdt_ff_v1' # path where friend input is located; same "granularity as NTUP"
FRIENDPATH  = '/coepp/cephfs/share/atlas/LFV/bdt_v3_ff_test' # path where friend input is located; same "granularity as NTUP"

###########
# SLIMMED #
###########
NTUP        = '/coepp/cephfs/share/atlas/LFV/july_redown_slim_all'        # global config input NTUP path
FRIENDPATH  = '/coepp/cephfs/share/atlas/LFV/mva_july_redown_slim_all' # path where friend input is located; same "granularity as NTUP"
#NTUP        = '/coepp/cephfs/share/atlas/LFV/july_redown_slim_all_sys1'        # global config input NTUP path
#FRIENDPATH  = '/coepp/cephfs/share/atlas/LFV/mva_july_redown_slim_all_sys1' # path where friend input is located; same "granularity as NTUP"
###########

JOBDIR      = "/coepp/cephfs/mel/%s/jobdir" % USER        # The Melb cloud is twisted and does not recognize home dirs...
prepare_path(JOBDIR)
INTARBALL   = os.path.join(JOBDIR,'histtarball_%s.tar.gz' % (time.strftime("d%d_m%m_y%Y_H%H_M%M_S%S")) )
AUTOBUILD   = True                                        # auto-build tarball using Makefile.tarball
NJMAX       = 400
DATATYPE    = options.datatype

# outputs  
RUN         = 'NN_allregions_%s_%s' % (options.runscript, options.datatype)
OUTPATH     = "/coepp/cephfs/mel/%s/ztautau/%s"%(USER,RUN) # 
OUTPATH     = "/coepp/cephfs/share/atlas/LFV/%s"%(RUN) # 

# running
QUEUE       = "long"                             # length of pbs queue (short, long, extralong )
SCRIPT      = "./ztautau/run/%s.plotter.py" % options.runscript  # pyframe job script
BEXEC       = "Hist.sh"                          # exec script (probably dont change) 

DO_NOM      = options.DO_NOM                     # submit the nominal job
DO_SYS      = options.DO_SYS                     # submit the systematics job

TESTMODE    = False                              # submit only 1 sub-job (for testing)
NCORES      = 1

INCLMC      = options.INCLMC
INCLDATA    = options.INCLDATA

def main():
    """
    * configure the samples (input->output)
    * configure which samples to run for each systematic
    * prepare outdirs and build intarball
    * launch the jobs
    """
    global MAIN
    global USER
    #global NTUP
    global INTARBALL
    global AUTOBUILD
    global RUN
    global OUTPATH
    global QUEUE
    global SCRIPT
    global BEXEC
    global DO_NOM
    global DO_SYS
    global TESTMODE
    global INCLMC
    global INCLDATA

    ## get lists of samples
    all_mc   = samples.all_mc
    all_data = samples.all_data
    if INCLMC and INCLDATA:
        nominal = all_data + all_mc
    elif INCLMC:
        nominal = all_mc
    elif INCLDATA:
        nominal = all_data
    else:
        print "Please specify -a and/or -d"
    
    # the division b/w standard and tree systematics
    # is not essential here. Just to organise things
    # ["output folder name","sys path modifier","samples"]
    # The "sys path modifier" entry is passed as a different
    # argument for friend_sys and path_sys
    
    #from Systematics import sys_list
    sys_list = []
    #               sys_conf(name, main_path_mod, friend_path_mod, samples):
    #sys_list.append(sys_conf('MUON_ID_1down',                              'sys1', 'sys1', all_mc))
    #sys_list.append(sys_conf("MUON_ID_1up",                                'sys1', 'sys1', all_mc))
    #sys_list.append(sys_conf("MUON_MS_1down",                              'sys1', 'sys1', all_mc))
    #sys_list.append(sys_conf("MUON_MS_1up",                                'sys1', 'sys1', all_mc))
    #sys_list.append(sys_conf("MUON_SAGITTA_RESBIAS_1down",                 'sys1', 'sys1', all_mc))
    #sys_list.append(sys_conf("MUON_SAGITTA_RESBIAS_1up",                   'sys1', 'sys1', all_mc))
    #sys_list.append(sys_conf("MUON_SAGITTA_RHO_1down",                     'sys1', 'sys1', all_mc))
    #sys_list.append(sys_conf("MUON_SAGITTA_RHO_1up",                       'sys1', 'sys1', all_mc))
    #sys_list.append(sys_conf("MUON_SCALE_1down",                           'sys1', 'sys1', all_mc))
    #sys_list.append(sys_conf("MUON_SCALE_1up",                             'sys1', 'sys1', all_mc))
    #sys_list.append(sys_conf("EG_RESOLUTION_ALL_1down",                    'sys1', 'sys1', all_mc))
    #sys_list.append(sys_conf("EG_RESOLUTION_ALL_1up",                      'sys1', 'sys1', all_mc))
    #sys_list.append(sys_conf("EG_SCALE_ALLCORR_1down",                     'sys1', 'sys1', all_mc))
    #sys_list.append(sys_conf("EG_SCALE_ALLCORR_1up",                       'sys1', 'sys1', all_mc))
    #sys_list.append(sys_conf("EG_SCALE_E4SCINTILLATOR_1down",              'sys1', 'sys1', all_mc))
    #sys_list.append(sys_conf("EG_SCALE_E4SCINTILLATOR_1up",                'sys1', 'sys1', all_mc))
    #sys_list.append(sys_conf("EG_SCALE_LARCALIB_EXTRA2015PRE_1down",       'sys1', 'sys1', all_mc))
    #sys_list.append(sys_conf("EG_SCALE_LARCALIB_EXTRA2015PRE_1up",         'sys1', 'sys1', all_mc))
    #sys_list.append(sys_conf("EG_SCALE_LARTEMPERATURE_EXTRA2015PRE_1down", 'sys1', 'sys1', all_mc))
    #sys_list.append(sys_conf("EG_SCALE_LARTEMPERATURE_EXTRA2015PRE_1up",   'sys1', 'sys1', all_mc))
    #sys_list.append(sys_conf("EG_SCALE_LARTEMPERATURE_EXTRA2016PRE_1down", 'sys1', 'sys1', all_mc))
    #sys_list.append(sys_conf("EG_SCALE_LARTEMPERATURE_EXTRA2016PRE_1up",   'sys1', 'sys1', all_mc))
    #sys_list.append(sys_conf("TAUS_TRUEHADTAU_SME_TES_DETECTOR_1down",     'sys1', 'sys1', all_mc))
    #sys_list.append(sys_conf("TAUS_TRUEHADTAU_SME_TES_DETECTOR_1up",       'sys1', 'sys1', all_mc))
    #sys_list.append(sys_conf("TAUS_TRUEHADTAU_SME_TES_INSITU_1down",       'sys1', 'sys1', all_mc))
    #sys_list.append(sys_conf("TAUS_TRUEHADTAU_SME_TES_INSITU_1up",         'sys1', 'sys1', all_mc))
    #sys_list.append(sys_conf("TAUS_TRUEHADTAU_SME_TES_MODEL_1down",        'sys1', 'sys1', all_mc))
    #sys_list.append(sys_conf("TAUS_TRUEHADTAU_SME_TES_MODEL_1up",          'sys1', 'sys1', all_mc))
    #sys_list.append(sys_conf("MET_SoftTrk_ResoPara",                       'sys1', 'sys1', all_mc))
    #sys_list.append(sys_conf("MET_SoftTrk_ResoPerp",                       'sys1', 'sys1', all_mc))
    #sys_list.append(sys_conf("MET_SoftTrk_ScaleDown",                      'sys1', 'sys1', all_mc))
    #sys_list.append(sys_conf("MET_SoftTrk_ScaleUp",                        'sys1', 'sys1', all_mc))

    ## TAU ELEOLR
    ## EL CHANNEL ELEOLR
    ##sys_list.append(sys_conf("TAUS_TRUEELECTRON_EFF_ELEOLR_TOTAL_1down_TauEffSF_LooseEleBDTPlusVeto_electron",                      None, None, all_mc))
    #sys_list.append(sys_conf("TAUS_TRUEELECTRON_EFF_ELEOLR_TOTAL_1down_TauEffSF_MediumEleBDTPlusVeto_electron",                     None, None, all_mc))
    #sys_list.append(sys_conf("TAUS_TRUEELECTRON_EFF_ELEOLR_TOTAL_1down_TauEffSF_VeryLooseLlhEleOLR_electron",                       None, None, all_mc))
    ##sys_list.append(sys_conf("TAUS_TRUEELECTRON_EFF_ELEOLR_TOTAL_1up_TauEffSF_LooseEleBDTPlusVeto_electron",                        None, None, all_mc))
    #sys_list.append(sys_conf("TAUS_TRUEELECTRON_EFF_ELEOLR_TOTAL_1up_TauEffSF_MediumEleBDTPlusVeto_electron",                       None, None, all_mc))
    #sys_list.append(sys_conf("TAUS_TRUEELECTRON_EFF_ELEOLR_TOTAL_1up_TauEffSF_VeryLooseLlhEleOLR_electron",                         None, None, all_mc))
    ## MU CHANNEL ELEOLR
    #sys_list.append(sys_conf("TAUS_TRUEHADTAU_EFF_ELEOLR_TOTAL_1down_TauEffSF_HadTauEleOLR_tauhad",                                 None, None, all_mc))
    #sys_list.append(sys_conf("TAUS_TRUEHADTAU_EFF_ELEOLR_TOTAL_1up_TauEffSF_HadTauEleOLR_tauhad",                                   None, None, all_mc))
    ## TAU ID
    #if 'tight' in sys.argv[2]:
    #    sys_list.append(sys_conf("TAUS_TRUEHADTAU_EFF_JETID_TOTAL_1down_TauEffSF_JetBDTtight",                                          None, None, all_mc))
    #    sys_list.append(sys_conf("TAUS_TRUEHADTAU_EFF_JETID_TOTAL_1up_TauEffSF_JetBDTtight",                                            None, None, all_mc))
    #    sys_list.append(sys_conf("TAUS_TRUEHADTAU_EFF_JETID_HIGHPT_1down_TauEffSF_JetBDTtight",                                         None, None, all_mc))
    #    sys_list.append(sys_conf("TAUS_TRUEHADTAU_EFF_JETID_HIGHPT_1up_TauEffSF_JetBDTtight",                                           None, None, all_mc))
    #else:
    #    sys_list.append(sys_conf("TAUS_TRUEHADTAU_EFF_JETID_HIGHPT_1down_TauEffSF_JetBDTmedium",                                        None, None, all_mc))
    #    sys_list.append(sys_conf("TAUS_TRUEHADTAU_EFF_JETID_HIGHPT_1up_TauEffSF_JetBDTmedium",                                          None, None, all_mc))
    #    sys_list.append(sys_conf("TAUS_TRUEHADTAU_EFF_JETID_TOTAL_1down_TauEffSF_JetBDTmedium",                                         None, None, all_mc))
    #    sys_list.append(sys_conf("TAUS_TRUEHADTAU_EFF_JETID_TOTAL_1up_TauEffSF_JetBDTmedium",                                           None, None, all_mc))
    ## TAU RECO
    #sys_list.append(sys_conf("TAUS_TRUEHADTAU_EFF_RECO_HIGHPT_1down_TauEffSF_reco",                                                 None, None, all_mc))
    #sys_list.append(sys_conf("TAUS_TRUEHADTAU_EFF_RECO_HIGHPT_1up_TauEffSF_reco",                                                   None, None, all_mc))
    #sys_list.append(sys_conf("TAUS_TRUEHADTAU_EFF_RECO_TOTAL_1down_TauEffSF_reco",                                                  None, None, all_mc))
    #sys_list.append(sys_conf("TAUS_TRUEHADTAU_EFF_RECO_TOTAL_1up_TauEffSF_reco",                                                    None, None, all_mc))

    ## MU RECO
    #sys_list.append(sys_conf("MUON_EFF_STAT_1down_MuEffSF_Reco_QualMedium",                                                         None, None, all_mc))
    #sys_list.append(sys_conf("MUON_EFF_STAT_1up_MuEffSF_Reco_QualMedium",                                                           None, None, all_mc))
    #sys_list.append(sys_conf("MUON_EFF_STAT_LOWPT_1down_MuEffSF_Reco_QualMedium",                                                   None, None, all_mc))
    #sys_list.append(sys_conf("MUON_EFF_STAT_LOWPT_1up_MuEffSF_Reco_QualMedium",                                                     None, None, all_mc))
    #sys_list.append(sys_conf("MUON_EFF_SYS_1down_MuEffSF_Reco_QualMedium",                                                          None, None, all_mc))
    #sys_list.append(sys_conf("MUON_EFF_SYS_1up_MuEffSF_Reco_QualMedium",                                                            None, None, all_mc))
    #sys_list.append(sys_conf("MUON_EFF_SYS_LOWPT_1down_MuEffSF_Reco_QualMedium",                                                    None, None, all_mc))
    #sys_list.append(sys_conf("MUON_EFF_SYS_LOWPT_1up_MuEffSF_Reco_QualMedium",                                                      None, None, all_mc))
    ## MU TRIG
    ##sys_list.append(sys_conf("MUON_EFF_TrigStatUncertainty_1down_MuEffSF_HLT_mu14_QualMedium_IsoNone",                              None, None, all_mc))
    #sys_list.append(sys_conf("MUON_EFF_TrigStatUncertainty_1down_MuEffSF_HLT_mu20_iloose_L1MU15_OR_HLT_mu40_QualMedium_IsoNone",    None, None, all_mc))
    #sys_list.append(sys_conf("MUON_EFF_TrigStatUncertainty_1down_MuEffSF_HLT_mu26_ivarmedium_OR_HLT_mu50_QualMedium_IsoNone",       None, None, all_mc))
    ##sys_list.append(sys_conf("MUON_EFF_TrigStatUncertainty_1up_MuEffSF_HLT_mu14_QualMedium_IsoNone",                                None, None, all_mc))
    #sys_list.append(sys_conf("MUON_EFF_TrigStatUncertainty_1up_MuEffSF_HLT_mu20_iloose_L1MU15_OR_HLT_mu40_QualMedium_IsoNone",      None, None, all_mc))
    #sys_list.append(sys_conf("MUON_EFF_TrigStatUncertainty_1up_MuEffSF_HLT_mu26_ivarmedium_OR_HLT_mu50_QualMedium_IsoNone",         None, None, all_mc))
    ##sys_list.append(sys_conf("MUON_EFF_TrigSystUncertainty_1down_MuEffSF_HLT_mu14_QualMedium_IsoNone",                              None, None, all_mc))
    #sys_list.append(sys_conf("MUON_EFF_TrigSystUncertainty_1down_MuEffSF_HLT_mu20_iloose_L1MU15_OR_HLT_mu40_QualMedium_IsoNone",    None, None, all_mc))
    #sys_list.append(sys_conf("MUON_EFF_TrigSystUncertainty_1down_MuEffSF_HLT_mu26_ivarmedium_OR_HLT_mu50_QualMedium_IsoNone",       None, None, all_mc))
    ##sys_list.append(sys_conf("MUON_EFF_TrigSystUncertainty_1up_MuEffSF_HLT_mu14_QualMedium_IsoNone",                                None, None, all_mc))
    #sys_list.append(sys_conf("MUON_EFF_TrigSystUncertainty_1up_MuEffSF_HLT_mu20_iloose_L1MU15_OR_HLT_mu40_QualMedium_IsoNone",      None, None, all_mc))
    #sys_list.append(sys_conf("MUON_EFF_TrigSystUncertainty_1up_MuEffSF_HLT_mu26_ivarmedium_OR_HLT_mu50_QualMedium_IsoNone",         None, None, all_mc))
    ## MU ISO
    ##sys_list.append(sys_conf("MUON_ISO_STAT_1down_MuEffSF_IsoFixedCutTightIsoGradient",                                             None, None, all_mc))
    #sys_list.append(sys_conf("MUON_ISO_STAT_1down_MuEffSF_IsoGradient",                                                             None, None, all_mc))
    ##sys_list.append(sys_conf("MUON_ISO_STAT_1down_MuEffSF_IsoLoose",                                                                None, None, all_mc))
    ##sys_list.append(sys_conf("MUON_ISO_STAT_1up_MuEffSF_IsoFixedCutTightIsoGradient",                                               None, None, all_mc))
    #sys_list.append(sys_conf("MUON_ISO_STAT_1up_MuEffSF_IsoGradient",                                                               None, None, all_mc))
    ##sys_list.append(sys_conf("MUON_ISO_STAT_1up_MuEffSF_IsoLoose",                                                                  None, None, all_mc))
    ##sys_list.append(sys_conf("MUON_ISO_SYS_1down_MuEffSF_IsoFixedCutTightIsoGradient",                                              None, None, all_mc))
    #sys_list.append(sys_conf("MUON_ISO_SYS_1down_MuEffSF_IsoGradient",                                                              None, None, all_mc))
    ##sys_list.append(sys_conf("MUON_ISO_SYS_1down_MuEffSF_IsoLoose",                                                                 None, None, all_mc))
    ##sys_list.append(sys_conf("MUON_ISO_SYS_1up_MuEffSF_IsoFixedCutTightIsoGradient",                                                None, None, all_mc))
    #sys_list.append(sys_conf("MUON_ISO_SYS_1up_MuEffSF_IsoGradient",                                                                None, None, all_mc))
    ##sys_list.append(sys_conf("MUON_ISO_SYS_1up_MuEffSF_IsoLoose",                                                                   None, None, all_mc))
    ##sys_list.append(sys_conf("MUON_TTVA_STAT_1down_MuEffSF_TTVA",                                                                   None, None, all_mc))
    ##sys_list.append(sys_conf("MUON_TTVA_STAT_1up_MuEffSF_TTVA",                                                                     None, None, all_mc))
    ##sys_list.append(sys_conf("MUON_TTVA_SYS_1down_MuEffSF_TTVA",                                                                    None, None, all_mc))
    ##sys_list.append(sys_conf("MUON_TTVA_SYS_1up_MuEffSF_TTVA",                                                                      None, None, all_mc))

    ## ELE RECO
    #sys_list.append(sys_conf("EL_EFF_ID_TOTAL_1NPCOR_PLUS_UNCOR_1down_EleEffSF_offline_LooseAndBLayerLLH_d0z0_v11",                 None, None, all_mc))
    #sys_list.append(sys_conf("EL_EFF_ID_TOTAL_1NPCOR_PLUS_UNCOR_1down_EleEffSF_offline_MediumLLH_d0z0_v11",                         None, None, all_mc))
    #sys_list.append(sys_conf("EL_EFF_ID_TOTAL_1NPCOR_PLUS_UNCOR_1up_EleEffSF_offline_LooseAndBLayerLLH_d0z0_v11",                   None, None, all_mc))
    #sys_list.append(sys_conf("EL_EFF_ID_TOTAL_1NPCOR_PLUS_UNCOR_1up_EleEffSF_offline_MediumLLH_d0z0_v11",                           None, None, all_mc))
    ##sys_list.append(sys_conf("EL_EFF_Iso_TOTAL_1NPCOR_PLUS_UNCOR_1down_EleEffSF_Isolation_MediumLLH_d0z0_v11_isolFixedCutTight",    None, None, all_mc))
    #sys_list.append(sys_conf("EL_EFF_Iso_TOTAL_1NPCOR_PLUS_UNCOR_1down_EleEffSF_Isolation_MediumLLH_d0z0_v11_isolGradient",         None, None, all_mc))
    ##sys_list.append(sys_conf("EL_EFF_Iso_TOTAL_1NPCOR_PLUS_UNCOR_1down_EleEffSF_Isolation_MediumLLH_d0z0_v11_isolLoose",            None, None, all_mc))
    ##sys_list.append(sys_conf("EL_EFF_Iso_TOTAL_1NPCOR_PLUS_UNCOR_1up_EleEffSF_Isolation_MediumLLH_d0z0_v11_isolFixedCutTight",      None, None, all_mc))
    #sys_list.append(sys_conf("EL_EFF_Iso_TOTAL_1NPCOR_PLUS_UNCOR_1up_EleEffSF_Isolation_MediumLLH_d0z0_v11_isolGradient",           None, None, all_mc))
    ##sys_list.append(sys_conf("EL_EFF_Iso_TOTAL_1NPCOR_PLUS_UNCOR_1up_EleEffSF_Isolation_MediumLLH_d0z0_v11_isolLoose",              None, None, all_mc))
    #sys_list.append(sys_conf("EL_EFF_Reco_TOTAL_1NPCOR_PLUS_UNCOR_1down_EleEffSF_offline_RecoTrk",                                  None, None, all_mc))
    #sys_list.append(sys_conf("EL_EFF_Reco_TOTAL_1NPCOR_PLUS_UNCOR_1up_EleEffSF_offline_RecoTrk",                                    None, None, all_mc))

    ## STUPID LONG ELECTRON TRIGGERS
    #sys_list.append(sys_conf("EL_EFF_Trigger_TOTAL_1NPCOR_PLUS_UNCOR_1down_EleEffSF_e17_lhmedium_MediumLLH_d0z0_v11_isolGradient_2015",                         None, None, all_mc))
    #sys_list.append(sys_conf("EL_EFF_Trigger_TOTAL_1NPCOR_PLUS_UNCOR_1down_EleEffSF_e17_lhmedium_MediumLLH_d0z0_v11_isolLoose_2015",                            None, None, all_mc))
    #sys_list.append(sys_conf("EL_EFF_Trigger_TOTAL_1NPCOR_PLUS_UNCOR_1down_EleEffSF_e17_lhmedium_nod0_ivarloose_L1EM15HI_MediumLLH_d0z0_v11_isolGradient_2016", None, None, all_mc))
    #sys_list.append(sys_conf("EL_EFF_Trigger_TOTAL_1NPCOR_PLUS_UNCOR_1down_EleEffSF_e17_lhmedium_nod0_ivarloose_L1EM15HI_MediumLLH_d0z0_v11_isolLoose_2016",    None, None, all_mc))
    #sys_list.append(sys_conf("EL_EFF_Trigger_TOTAL_1NPCOR_PLUS_UNCOR_1up_EleEffSF_e17_lhmedium_MediumLLH_d0z0_v11_isolGradient_2015",                           None, None, all_mc))
    #sys_list.append(sys_conf("EL_EFF_Trigger_TOTAL_1NPCOR_PLUS_UNCOR_1up_EleEffSF_e17_lhmedium_MediumLLH_d0z0_v11_isolLoose_2015",                              None, None, all_mc))
    #sys_list.append(sys_conf("EL_EFF_Trigger_TOTAL_1NPCOR_PLUS_UNCOR_1up_EleEffSF_e17_lhmedium_nod0_ivarloose_L1EM15HI_MediumLLH_d0z0_v11_isolGradient_2016",   None, None, all_mc))
    #sys_list.append(sys_conf("EL_EFF_Trigger_TOTAL_1NPCOR_PLUS_UNCOR_1up_EleEffSF_e17_lhmedium_nod0_ivarloose_L1EM15HI_MediumLLH_d0z0_v11_isolLoose_2016",      None, None, all_mc))
    #sys_list.append(sys_conf("EL_EFF_TriggerEff_TOTAL_1NPCOR_PLUS_UNCOR_1down_efficiency_SINGLE_E_2015_e24_lhmedium_L1EM20VH_OR_e60_lhmedium_OR_e120_lhloose_2016_e26_lhtight_nod0_ivarloose_OR_e60_lhmedium_nod0_OR_e140_lhloose_nod0_MediumLLH_d0z0_v11_isolGradient", None, None, all_mc))
    #sys_list.append(sys_conf("EL_EFF_TriggerEff_TOTAL_1NPCOR_PLUS_UNCOR_1up_efficiency_SINGLE_E_2015_e24_lhmedium_L1EM20VH_OR_e60_lhmedium_OR_e120_lhloose_2016_e26_lhtight_nod0_ivarloose_OR_e60_lhmedium_nod0_OR_e140_lhloose_nod0_MediumLLH_d0z0_v11_isolGradient",   None, None, all_mc))
    #sys_list.append(sys_conf("EL_EFF_Trigger_TOTAL_1NPCOR_PLUS_UNCOR_1down_EleEffSF_SINGLE_E_2015_e24_lhmedium_L1EM20VH_OR_e60_lhmedium_OR_e120_lhloose_2016_e26_lhtight_nod0_ivarloose_OR_e60_lhmedium_nod0_OR_e140_lhloose_nod0_MediumLLH_d0z0_v11_isolFixedCutTight", None, None, all_mc))
    #sys_list.append(sys_conf("EL_EFF_Trigger_TOTAL_1NPCOR_PLUS_UNCOR_1down_EleEffSF_SINGLE_E_2015_e24_lhmedium_L1EM20VH_OR_e60_lhmedium_OR_e120_lhloose_2016_e26_lhtight_nod0_ivarloose_OR_e60_lhmedium_nod0_OR_e140_lhloose_nod0_MediumLLH_d0z0_v11_isolGradient",      None, None, all_mc))
    #sys_list.append(sys_conf("EL_EFF_Trigger_TOTAL_1NPCOR_PLUS_UNCOR_1down_EleEffSF_SINGLE_E_2015_e24_lhmedium_L1EM20VH_OR_e60_lhmedium_OR_e120_lhloose_2016_e26_lhtight_nod0_ivarloose_OR_e60_lhmedium_nod0_OR_e140_lhloose_nod0_MediumLLH_d0z0_v11_isolLoose",         None, None, all_mc))
    #sys_list.append(sys_conf("EL_EFF_Trigger_TOTAL_1NPCOR_PLUS_UNCOR_1up_EleEffSF_SINGLE_E_2015_e24_lhmedium_L1EM20VH_OR_e60_lhmedium_OR_e120_lhloose_2016_e26_lhtight_nod0_ivarloose_OR_e60_lhmedium_nod0_OR_e140_lhloose_nod0_MediumLLH_d0z0_v11_isolFixedCutTight",   None, None, all_mc))
    #sys_list.append(sys_conf("EL_EFF_Trigger_TOTAL_1NPCOR_PLUS_UNCOR_1up_EleEffSF_SINGLE_E_2015_e24_lhmedium_L1EM20VH_OR_e60_lhmedium_OR_e120_lhloose_2016_e26_lhtight_nod0_ivarloose_OR_e60_lhmedium_nod0_OR_e140_lhloose_nod0_MediumLLH_d0z0_v11_isolGradient",        None, None, all_mc))
    #sys_list.append(sys_conf("EL_EFF_Trigger_TOTAL_1NPCOR_PLUS_UNCOR_1up_EleEffSF_SINGLE_E_2015_e24_lhmedium_L1EM20VH_OR_e60_lhmedium_OR_e120_lhloose_2016_e26_lhtight_nod0_ivarloose_OR_e60_lhmedium_nod0_OR_e140_lhloose_nod0_MediumLLH_d0z0_v11_isolLoose",           None, None, all_mc))
    
    # JET NONSENSE
    #sys_list.append(sys_conf("jet_FT_EFF_Eigen_B_0_1down_global_effSF_MVX",                  None, None, all_mc))
    #sys_list.append(sys_conf("jet_FT_EFF_Eigen_B_0_1down_global_ineffSF_MVX",                None, None, all_mc))
    #sys_list.append(sys_conf("jet_FT_EFF_Eigen_B_0_1up_global_effSF_MVX",                    None, None, all_mc))
    #sys_list.append(sys_conf("jet_FT_EFF_Eigen_B_0_1up_global_ineffSF_MVX",                  None, None, all_mc))
    #sys_list.append(sys_conf("jet_FT_EFF_Eigen_B_1_1down_global_effSF_MVX",                  None, None, all_mc))
    #sys_list.append(sys_conf("jet_FT_EFF_Eigen_B_1_1down_global_ineffSF_MVX",                None, None, all_mc))
    #sys_list.append(sys_conf("jet_FT_EFF_Eigen_B_1_1up_global_effSF_MVX",                    None, None, all_mc))
    #sys_list.append(sys_conf("jet_FT_EFF_Eigen_B_1_1up_global_ineffSF_MVX",                  None, None, all_mc))
    #sys_list.append(sys_conf("jet_FT_EFF_Eigen_B_2_1down_global_effSF_MVX",                  None, None, all_mc))
    #sys_list.append(sys_conf("jet_FT_EFF_Eigen_B_2_1down_global_ineffSF_MVX",                None, None, all_mc))
    #sys_list.append(sys_conf("jet_FT_EFF_Eigen_B_2_1up_global_effSF_MVX",                    None, None, all_mc))
    #sys_list.append(sys_conf("jet_FT_EFF_Eigen_B_2_1up_global_ineffSF_MVX",                  None, None, all_mc))
    #sys_list.append(sys_conf("jet_FT_EFF_Eigen_C_0_1down_global_effSF_MVX",                  None, None, all_mc))
    #sys_list.append(sys_conf("jet_FT_EFF_Eigen_C_0_1down_global_ineffSF_MVX",                None, None, all_mc))
    #sys_list.append(sys_conf("jet_FT_EFF_Eigen_C_0_1up_global_effSF_MVX",                    None, None, all_mc))
    #sys_list.append(sys_conf("jet_FT_EFF_Eigen_C_0_1up_global_ineffSF_MVX",                  None, None, all_mc))
    #sys_list.append(sys_conf("jet_FT_EFF_Eigen_C_1_1down_global_effSF_MVX",                  None, None, all_mc))
    #sys_list.append(sys_conf("jet_FT_EFF_Eigen_C_1_1down_global_ineffSF_MVX",                None, None, all_mc))
    #sys_list.append(sys_conf("jet_FT_EFF_Eigen_C_1_1up_global_effSF_MVX",                    None, None, all_mc))
    #sys_list.append(sys_conf("jet_FT_EFF_Eigen_C_1_1up_global_ineffSF_MVX",                  None, None, all_mc))
    #sys_list.append(sys_conf("jet_FT_EFF_Eigen_C_2_1down_global_effSF_MVX",                  None, None, all_mc))
    #sys_list.append(sys_conf("jet_FT_EFF_Eigen_C_2_1down_global_ineffSF_MVX",                None, None, all_mc))
    #sys_list.append(sys_conf("jet_FT_EFF_Eigen_C_2_1up_global_effSF_MVX",                    None, None, all_mc))
    #sys_list.append(sys_conf("jet_FT_EFF_Eigen_C_2_1up_global_ineffSF_MVX",                  None, None, all_mc))
    #sys_list.append(sys_conf("jet_FT_EFF_Eigen_Light_0_1down_global_effSF_MVX",              None, None, all_mc))
    #sys_list.append(sys_conf("jet_FT_EFF_Eigen_Light_0_1down_global_ineffSF_MVX",            None, None, all_mc))
    #sys_list.append(sys_conf("jet_FT_EFF_Eigen_Light_0_1up_global_effSF_MVX",                None, None, all_mc))
    #sys_list.append(sys_conf("jet_FT_EFF_Eigen_Light_0_1up_global_ineffSF_MVX",              None, None, all_mc))
    #sys_list.append(sys_conf("jet_FT_EFF_Eigen_Light_1_1down_global_effSF_MVX",              None, None, all_mc))
    #sys_list.append(sys_conf("jet_FT_EFF_Eigen_Light_1_1down_global_ineffSF_MVX",            None, None, all_mc))
    #sys_list.append(sys_conf("jet_FT_EFF_Eigen_Light_1_1up_global_effSF_MVX",                None, None, all_mc))
    #sys_list.append(sys_conf("jet_FT_EFF_Eigen_Light_1_1up_global_ineffSF_MVX",              None, None, all_mc))
    #sys_list.append(sys_conf("jet_FT_EFF_Eigen_Light_2_1down_global_effSF_MVX",              None, None, all_mc))
    #sys_list.append(sys_conf("jet_FT_EFF_Eigen_Light_2_1down_global_ineffSF_MVX",            None, None, all_mc))
    #sys_list.append(sys_conf("jet_FT_EFF_Eigen_Light_2_1up_global_effSF_MVX",                None, None, all_mc))
    #sys_list.append(sys_conf("jet_FT_EFF_Eigen_Light_2_1up_global_ineffSF_MVX",              None, None, all_mc))
    #sys_list.append(sys_conf("jet_FT_EFF_Eigen_Light_3_1down_global_effSF_MVX",              None, None, all_mc))
    #sys_list.append(sys_conf("jet_FT_EFF_Eigen_Light_3_1down_global_ineffSF_MVX",            None, None, all_mc))
    #sys_list.append(sys_conf("jet_FT_EFF_Eigen_Light_3_1up_global_effSF_MVX",                None, None, all_mc))
    #sys_list.append(sys_conf("jet_FT_EFF_Eigen_Light_3_1up_global_ineffSF_MVX",              None, None, all_mc))
    #sys_list.append(sys_conf("jet_FT_EFF_Eigen_Light_4_1down_global_effSF_MVX",              None, None, all_mc))
    #sys_list.append(sys_conf("jet_FT_EFF_Eigen_Light_4_1down_global_ineffSF_MVX",            None, None, all_mc))
    #sys_list.append(sys_conf("jet_FT_EFF_Eigen_Light_4_1up_global_effSF_MVX",                None, None, all_mc))
    #sys_list.append(sys_conf("jet_FT_EFF_Eigen_Light_4_1up_global_ineffSF_MVX",              None, None, all_mc))
    #sys_list.append(sys_conf("jet_FT_EFF_extrapolation_1down_global_effSF_MVX",              None, None, all_mc))
    #sys_list.append(sys_conf("jet_FT_EFF_extrapolation_1down_global_ineffSF_MVX",            None, None, all_mc))
    #sys_list.append(sys_conf("jet_FT_EFF_extrapolation_1up_global_effSF_MVX",                None, None, all_mc))
    #sys_list.append(sys_conf("jet_FT_EFF_extrapolation_1up_global_ineffSF_MVX",              None, None, all_mc))
    #sys_list.append(sys_conf("jet_FT_EFF_extrapolation_from_charm_1down_global_effSF_MVX",   None, None, all_mc))
    #sys_list.append(sys_conf("jet_FT_EFF_extrapolation_from_charm_1down_global_ineffSF_MVX", None, None, all_mc))
    #sys_list.append(sys_conf("jet_FT_EFF_extrapolation_from_charm_1up_global_effSF_MVX",     None, None, all_mc))
    #sys_list.append(sys_conf("jet_FT_EFF_extrapolation_from_charm_1up_global_ineffSF_MVX",   None, None, all_mc))
    #sys_list.append(sys_conf("jet_JET_JvtEfficiency_1down_central_jets_global_effSF_JVT",    None, None, all_mc))
    #sys_list.append(sys_conf("jet_JET_JvtEfficiency_1down_central_jets_global_ineffSF_JVT",  None, None, all_mc))
    #sys_list.append(sys_conf("jet_JET_JvtEfficiency_1down_forward_jets_global_effSF_JVT",    None, None, all_mc))
    #sys_list.append(sys_conf("jet_JET_JvtEfficiency_1down_forward_jets_global_ineffSF_JVT",  None, None, all_mc))
    #sys_list.append(sys_conf("jet_JET_JvtEfficiency_1up_central_jets_global_effSF_JVT",      None, None, all_mc))
    #sys_list.append(sys_conf("jet_JET_JvtEfficiency_1up_central_jets_global_ineffSF_JVT",    None, None, all_mc))
    #sys_list.append(sys_conf("jet_JET_JvtEfficiency_1up_forward_jets_global_effSF_JVT",      None, None, all_mc))
    #sys_list.append(sys_conf("jet_JET_JvtEfficiency_1up_forward_jets_global_ineffSF_JVT",    None, None, all_mc))

    ## ensure output path exists
    prepare_path(OUTPATH)
    
    ## auto-build tarball
    if AUTOBUILD:
        print 'building input tarball %s...'% (INTARBALL)
        cmd = 'cd %s; make -f Makefile.hist TARBALL=%s' % (MAIN,INTARBALL)
        m = subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE)
        print m.communicate()[0]

    if DO_NOM: 
      submit(NTUP,FRIENDPATH,'nominal',None,None,nominal)
    
    if DO_SYS:
      for conf in sys_list:
        r_name = conf['name'].replace('SINGLE_E_2015_e24_lhmedium_L1EM20VH_OR_e60_lhmedium_OR_e120_lhloose_2016_e26_lhtight_nod0_ivarloose_OR_e60_lhmedium_nod0_OR_e140_lhloose_nod0_MediumLLH_d0z0_v11', 'ELE_TRIG')
        submit(NTUP,FRIENDPATH,r_name,conf['main_path_mod'],conf['friend_path_mod'],conf['samples'],config={'sys':conf['name']})
    


def submit(NTUP,FRIENDPATH,job_name,job_sys_path,friend_sys_path,samps,config={}):
    """
    * construct config file 
    * prepare variable list to pass to job
    * submit job
    """
    global MAIN
    global USER
    #global FRIENDPATH
    global NJMAX
    global INTARBALL
    global AUTOBUILD
    global RUN
    global OUTPATH
    global QUEUE
    global SCRIPT
    global BEXEC
    global DO_NOM
    global DO_SYS
    global TESTMODE
    global DATATYPE
    
    assert (NJMAX<=600), "Error: please, not more than 600 subjobs per array!"

    ## construct config file
    ## ---------------------
    nsubjobs = 0
    nrun     = 1
    nlines   = 0
    f_dict   = {} 
    
    if job_sys_path: NTUP = "_".join([NTUP,job_sys_path])  

    outrootpath = os.path.abspath(os.path.join(OUTPATH,job_name))
    logrootpath = os.path.abspath(os.path.join(OUTPATH,'log_%s'%job_name))
    
    prepare_path(outrootpath)
    prepare_path(logrootpath)

    absintar   = os.path.abspath(INTARBALL)
   
    data_subdir = None
    mc_subdir = None 
    
    totsubjob = 0
    # not efficienct. Who cares?
    for s in samps:
      if s.type == "data":
        if not data_subdir: data_subdir = get_subdir( os.path.join(NTUP,'data') )
        in_data  = input_files(NTUP,data_subdir,s,job_sys_path) 
        for infile in in_data: totsubjob += 1
      if s.type == "mc":
        if not mc_subdir: mc_subdir = get_subdir( os.path.join(NTUP,'mc') )
        in_mc  = input_files(NTUP,mc_subdir,s,job_sys_path) 
        if not in_mc: continue # This is just temporary!!! Skip on non existing files
        for infile in in_mc: totsubjob += 1

    if FRIENDPATH:
       if friend_sys_path:  FRIENDPATH = "_".join([FRIENDPATH,friend_sys_path])  


    for s in samps:
        
        # configure output path 
        absoutpath = os.path.abspath(os.path.join(outrootpath,s.type,s.name))
        
        prepare_path(absoutpath)

        ## input & output
        #sinputs  = input_files(all_subdir,s,job_sys_path) # enable job_sys_path to take corr. input

        sinputs = []

        if s.type == "data":
          if not data_subdir: data_subdir = get_subdir( os.path.join(NTUP,'data') )
          sinputs  = input_files(NTUP,data_subdir,s,job_sys_path) 
        if s.type == "mc":
          if not mc_subdir: mc_subdir = get_subdir( os.path.join(NTUP,'mc') )
          sinputs  = input_files(NTUP,mc_subdir,s,job_sys_path) 
          if not sinputs: continue # This is just temporary!!! Skip on non existing files

        for infile in sinputs:
           soutput  = output_file(s,infile,job_sys_path) # replace job_sys_path with job_name
           
           if file_exists(absoutpath,soutput): continue
           
           ## config
           sconfig = {}
           sconfig.update(config)
           sconfig.update(s.config)
           sconfig_str = ",".join(["%s:%s"%(key,val) for key,val in sconfig.items()])
           
           # abspath of infile
           infpath = os.path.join(NTUP,s.type,infile)
           infpathfriend = ""
           infriend      = ""
           
           if FRIENDPATH:
              infriend = infile.replace(NTUP,FRIENDPATH)+".friend"
           
           # write many lines here
           if infriend == "":
               line = ';'.join([s.name,infpath,soutput,s.type,DATATYPE,sconfig_str])
           else:
               line = ';'.join([s.name,infpath,infriend,soutput,s.type,DATATYPE,sconfig_str])

           cfg = os.path.join(JOBDIR,'Config%s.%s.run.%s'%(RUN,job_name,nrun))
           abslogpath = os.path.abspath(os.path.join(logrootpath,"log_run_%d"%nrun))
           
           if not str(nrun) in f_dict.keys():
             """
             WIP
             if file_exists(JOBDIR,'Config%s.%s.run.%s'%(RUN,job_name,nrun)): 
               
               # resubmission of failed jobs
               cfg = cfg.replace(".run.",".resub.")
               abslogpath = abslogpath.replace("_run_","_resub_")
             """ 
             f_dict[str(nrun)] = open(cfg,'w')
           prepare_path(abslogpath)
           
           f_dict[str(nrun)].write('%s\n'%line)
           nlines += 1
           nsubjobs += 1 
           
           if nsubjobs >= nrun*NJMAX or nsubjobs==totsubjob:
             
             f_dict[str(nrun)].close()
             
             nrun += 1
             
             # configure input path 
             # --------------------
             abscfg     = os.path.abspath(cfg)
             if TESTMODE: nsubjobs = 1
             
             vars=[]
             vars+=["CONFIG=%s"     % abscfg       ]
             vars+=["INTARBALL=%s"  % absintar     ]
             vars+=["OUTPATH=%s"    % outrootpath  ]
             vars+=["SCRIPT=%s"     % SCRIPT       ]
             vars+=["NCORES=%d"     % NCORES       ]
             
             VARS = ','.join(vars)
             
             cmd = 'qsub'
             cmd += ' -l nodes=1:ppn=%d'  % NCORES
             cmd += ' -q %s'              % QUEUE
             cmd += ' -v "%s"'            % VARS
             cmd += ' -N j.hist.%s'       % job_name
             cmd += ' -j oe -o %s/log'    % abslogpath
             cmd += ' -t1-%d'             % nlines
             cmd += ' %s'                 % BEXEC 
             print cmd
             
             m = subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE)
             print m.communicate()[0]

             nlines = 0

def gen_file_dict(path):
  file_dict = {}
  for dirname in os.listdir(path):
    if os.path.isdir(os.path.join(path,dirname)):
      file_dict[os.path.join(path,dirname)] = os.listdir(os.path.join(path,dirname))
  return file_dict

def input_files(NTUP,subdirs,sample,sys):
    #global NTUP
    for sdir in subdirs:
      if sample.name in sdir:
        return get_subfile(os.path.join(NTUP,sample.type,sdir))

def output_file(sample,infile,sys):
    return os.path.basename(infile)

def file_exists(path,file):
    if os.path.exists(path):
      return file in os.listdir(os.path.join(path))
    else: return False

def get_subdir(mydir):
    return [name for name in os.listdir(mydir)
            if os.path.isdir(os.path.join(mydir, name))]

def get_subfile(mydir):
    return [os.path.join(mydir,name) for name in os.listdir(mydir)
            if os.path.isfile(os.path.join(mydir, name))]


if __name__=='__main__': main()

## EOF



