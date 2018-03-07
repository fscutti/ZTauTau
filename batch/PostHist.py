# encoding: utf-8
'''
PostHist.py
this is the script to run for checking that 
all subjobs are successful and hadd the output
'''

import os
import collections
import subprocess


# input path
inpath = "/coepp/cephfs/share/atlas/LFV/july_redown"
inpath = "/coepp/cephfs/share/atlas/LFV/july_redown_slim_all"
#inpath = "/coepp/cephfs/share/atlas/LFV/july_redown_slim_all_sys1"

# basepath common to all output
outbasepath = "/coepp/cephfs/mel/brianl/ztautau/"
outbasepath = "/coepp/cephfs/share/atlas/LFV/"
#outbasepath = "/coepp/cephfs/share/atlas/LFV/hists/hists_slim_180213"
outbasepath = "/coepp/cephfs/share/atlas/LFV/hists/hists_slim_180228"

hadd_files = False
debug = False


def gen_file_dict(path):
  file_dict = {}
  for dirname in os.listdir(path):
    if os.path.isdir(os.path.join(path,dirname)):
      file_dict[os.path.join(path,dirname)] = os.listdir(os.path.join(path,dirname))
  return file_dict

def find_list_diff(list1,list2):
  diff = []
  for l1 in list1:
    l1 = l1.strip()
    if not l1.split(".root")[0]+".root" in list2: 
      diff.append(l1)
  return diff

def hadd_cmd(outpath,outfile,inpath):
  cmd = 'hadd '
  cmd += '%s/%s.root ' % (outpath,outfile)
  cmd += '%s/*.root ' % inpath
  return cmd


outdir = {}

outdir["data"] = []
###################################################
#                  PRESEL                         #
###################################################
#outdir["data"].append("NN_allregions_presel_main")
#outdir["data"].append("NN_allregions_presel_osw")
#outdir["data"].append("NN_allregions_presel_ssw")
#outdir["data"].append("NN_allregions_presel_qcd")
#outdir["data"].append("NN_allregions_presel_ff")
###################################################
#                  TIGHT                          #
###################################################
outdir["data"].append("NN_allregions_tight_main")
outdir["data"].append("NN_allregions_tight_osw")
outdir["data"].append("NN_allregions_tight_ssw")
outdir["data"].append("NN_allregions_tight_qcd")
#outdir["data"].append("NN_allregions_tight_ff")
###################################################
#                    AC                           #
###################################################
#outdir["data"].append("NN_allregions_ac_main")
#outdir["data"].append("NN_allregions_ac_osw")
#outdir["data"].append("NN_allregions_ac_ssw")
#outdir["data"].append("NN_allregions_ac_qcd")
#outdir["data"].append("NN_allregions_ac_ff")

outdir["mc"] = []
###################################################
#                  PRESEL                         #
###################################################
#outdir["mc"].append("NN_allregions_presel_main")
#outdir["mc"].append("NN_allregions_presel_osw")
#outdir["mc"].append("NN_allregions_presel_ssw")
#outdir["mc"].append("NN_allregions_presel_qcd")
#outdir["mc"].append("NN_allregions_presel_ff")
###################################################
#                  TIGHT                          #
###################################################
outdir["mc"].append("NN_allregions_tight_main")
outdir["mc"].append("NN_allregions_tight_osw")
outdir["mc"].append("NN_allregions_tight_ssw")
outdir["mc"].append("NN_allregions_tight_qcd")
#outdir["mc"].append("NN_allregions_tight_ff")
###################################################
#                    AC                           #
###################################################
#outdir["mc"].append("NN_allregions_ac_main")
#outdir["mc"].append("NN_allregions_ac_osw")
#outdir["mc"].append("NN_allregions_ac_ssw")
#outdir["mc"].append("NN_allregions_ac_qcd")
#outdir["mc"].append("NN_allregions_ac_ff")

jobtype = ["nominal"]
do_sys  = False
if do_sys:
    #jobtype.append("TAUS_TRUEELECTRON_EFF_ELEOLR_TOTAL_1down_TauEffSF_LooseEleBDTPlusVeto_electron")
    jobtype.append("TAUS_TRUEELECTRON_EFF_ELEOLR_TOTAL_1down_TauEffSF_MediumEleBDTPlusVeto_electron")
    jobtype.append("TAUS_TRUEELECTRON_EFF_ELEOLR_TOTAL_1down_TauEffSF_VeryLooseLlhEleOLR_electron")
    #jobtype.append("TAUS_TRUEELECTRON_EFF_ELEOLR_TOTAL_1up_TauEffSF_LooseEleBDTPlusVeto_electron")
    jobtype.append("TAUS_TRUEELECTRON_EFF_ELEOLR_TOTAL_1up_TauEffSF_MediumEleBDTPlusVeto_electron")
    jobtype.append("TAUS_TRUEELECTRON_EFF_ELEOLR_TOTAL_1up_TauEffSF_VeryLooseLlhEleOLR_electron")
    jobtype.append("TAUS_TRUEHADTAU_EFF_ELEOLR_TOTAL_1down_TauEffSF_HadTauEleOLR_tauhad")
    jobtype.append("TAUS_TRUEHADTAU_EFF_ELEOLR_TOTAL_1up_TauEffSF_HadTauEleOLR_tauhad")
    jobtype.append("TAUS_TRUEHADTAU_EFF_JETID_HIGHPT_1down_TauEffSF_JetBDTmedium")
    #jobtype.append("TAUS_TRUEHADTAU_EFF_JETID_HIGHPT_1down_TauEffSF_JetBDTtight")
    jobtype.append("TAUS_TRUEHADTAU_EFF_JETID_HIGHPT_1up_TauEffSF_JetBDTmedium")
    #jobtype.append("TAUS_TRUEHADTAU_EFF_JETID_HIGHPT_1up_TauEffSF_JetBDTtight")
    jobtype.append("TAUS_TRUEHADTAU_EFF_JETID_TOTAL_1down_TauEffSF_JetBDTmedium")
    #jobtype.append("TAUS_TRUEHADTAU_EFF_JETID_TOTAL_1down_TauEffSF_JetBDTtight")
    jobtype.append("TAUS_TRUEHADTAU_EFF_JETID_TOTAL_1up_TauEffSF_JetBDTmedium")
    #jobtype.append("TAUS_TRUEHADTAU_EFF_JETID_TOTAL_1up_TauEffSF_JetBDTtight")
    jobtype.append("TAUS_TRUEHADTAU_EFF_RECO_HIGHPT_1down_TauEffSF_reco")
    jobtype.append("TAUS_TRUEHADTAU_EFF_RECO_HIGHPT_1up_TauEffSF_reco")
    jobtype.append("TAUS_TRUEHADTAU_EFF_RECO_TOTAL_1down_TauEffSF_reco")
    jobtype.append("TAUS_TRUEHADTAU_EFF_RECO_TOTAL_1up_TauEffSF_reco")
    jobtype.append("MUON_EFF_STAT_1down_MuEffSF_Reco_QualMedium")
    jobtype.append("MUON_EFF_STAT_1up_MuEffSF_Reco_QualMedium")
    jobtype.append("MUON_EFF_STAT_LOWPT_1down_MuEffSF_Reco_QualMedium")
    jobtype.append("MUON_EFF_STAT_LOWPT_1up_MuEffSF_Reco_QualMedium")
    jobtype.append("MUON_EFF_SYS_1down_MuEffSF_Reco_QualMedium")
    jobtype.append("MUON_EFF_SYS_1up_MuEffSF_Reco_QualMedium")
    jobtype.append("MUON_EFF_SYS_LOWPT_1down_MuEffSF_Reco_QualMedium")
    jobtype.append("MUON_EFF_SYS_LOWPT_1up_MuEffSF_Reco_QualMedium")
    #jobtype.append("MUON_EFF_TrigStatUncertainty_1down_MuEffSF_HLT_mu14_QualMedium_IsoNone")
    jobtype.append("MUON_EFF_TrigStatUncertainty_1down_MuEffSF_HLT_mu20_iloose_L1MU15_OR_HLT_mu40_QualMedium_IsoNone")
    jobtype.append("MUON_EFF_TrigStatUncertainty_1down_MuEffSF_HLT_mu26_ivarmedium_OR_HLT_mu50_QualMedium_IsoNone")
    #jobtype.append("MUON_EFF_TrigStatUncertainty_1up_MuEffSF_HLT_mu14_QualMedium_IsoNone")
    jobtype.append("MUON_EFF_TrigStatUncertainty_1up_MuEffSF_HLT_mu20_iloose_L1MU15_OR_HLT_mu40_QualMedium_IsoNone")
    jobtype.append("MUON_EFF_TrigStatUncertainty_1up_MuEffSF_HLT_mu26_ivarmedium_OR_HLT_mu50_QualMedium_IsoNone")
    #jobtype.append("MUON_EFF_TrigSystUncertainty_1down_MuEffSF_HLT_mu14_QualMedium_IsoNone")
    jobtype.append("MUON_EFF_TrigSystUncertainty_1down_MuEffSF_HLT_mu20_iloose_L1MU15_OR_HLT_mu40_QualMedium_IsoNone")
    jobtype.append("MUON_EFF_TrigSystUncertainty_1down_MuEffSF_HLT_mu26_ivarmedium_OR_HLT_mu50_QualMedium_IsoNone")
    #jobtype.append("MUON_EFF_TrigSystUncertainty_1up_MuEffSF_HLT_mu14_QualMedium_IsoNone")
    jobtype.append("MUON_EFF_TrigSystUncertainty_1up_MuEffSF_HLT_mu20_iloose_L1MU15_OR_HLT_mu40_QualMedium_IsoNone")
    jobtype.append("MUON_EFF_TrigSystUncertainty_1up_MuEffSF_HLT_mu26_ivarmedium_OR_HLT_mu50_QualMedium_IsoNone")
    #jobtype.append("MUON_ISO_STAT_1down_MuEffSF_IsoFixedCutTightIsoGradient")
    jobtype.append("MUON_ISO_STAT_1down_MuEffSF_IsoGradient")
    #jobtype.append("MUON_ISO_STAT_1down_MuEffSF_IsoLoose")
    #jobtype.append("MUON_ISO_STAT_1up_MuEffSF_IsoFixedCutTightIsoGradient")
    jobtype.append("MUON_ISO_STAT_1up_MuEffSF_IsoGradient")
    #jobtype.append("MUON_ISO_STAT_1up_MuEffSF_IsoLoose")
    #jobtype.append("MUON_ISO_SYS_1down_MuEffSF_IsoFixedCutTightIsoGradient")
    jobtype.append("MUON_ISO_SYS_1down_MuEffSF_IsoGradient")
    #jobtype.append("MUON_ISO_SYS_1down_MuEffSF_IsoLoose")
    #jobtype.append("MUON_ISO_SYS_1up_MuEffSF_IsoFixedCutTightIsoGradient")
    jobtype.append("MUON_ISO_SYS_1up_MuEffSF_IsoGradient")
    #jobtype.append("MUON_ISO_SYS_1up_MuEffSF_IsoLoose")
    #jobtype.append("MUON_TTVA_STAT_1down_MuEffSF_TTVA")
    #jobtype.append("MUON_TTVA_STAT_1up_MuEffSF_TTVA")
    #jobtype.append("MUON_TTVA_SYS_1down_MuEffSF_TTVA")
    #jobtype.append("MUON_TTVA_SYS_1up_MuEffSF_TTVA")
    jobtype.append("EL_EFF_ID_TOTAL_1NPCOR_PLUS_UNCOR_1down_EleEffSF_offline_LooseAndBLayerLLH_d0z0_v11")
    jobtype.append("EL_EFF_ID_TOTAL_1NPCOR_PLUS_UNCOR_1down_EleEffSF_offline_MediumLLH_d0z0_v11")
    jobtype.append("EL_EFF_ID_TOTAL_1NPCOR_PLUS_UNCOR_1up_EleEffSF_offline_LooseAndBLayerLLH_d0z0_v11")
    jobtype.append("EL_EFF_ID_TOTAL_1NPCOR_PLUS_UNCOR_1up_EleEffSF_offline_MediumLLH_d0z0_v11")
    #jobtype.append("EL_EFF_Iso_TOTAL_1NPCOR_PLUS_UNCOR_1down_EleEffSF_Isolation_MediumLLH_d0z0_v11_isolFixedCutTight")
    #jobtype.append("EL_EFF_Iso_TOTAL_1NPCOR_PLUS_UNCOR_1down_EleEffSF_Isolation_MediumLLH_d0z0_v11_isolGradient")
    #jobtype.append("EL_EFF_Iso_TOTAL_1NPCOR_PLUS_UNCOR_1down_EleEffSF_Isolation_MediumLLH_d0z0_v11_isolLoose")
    #jobtype.append("EL_EFF_Iso_TOTAL_1NPCOR_PLUS_UNCOR_1up_EleEffSF_Isolation_MediumLLH_d0z0_v11_isolFixedCutTight")
    #jobtype.append("EL_EFF_Iso_TOTAL_1NPCOR_PLUS_UNCOR_1up_EleEffSF_Isolation_MediumLLH_d0z0_v11_isolGradient")
    #jobtype.append("EL_EFF_Iso_TOTAL_1NPCOR_PLUS_UNCOR_1up_EleEffSF_Isolation_MediumLLH_d0z0_v11_isolLoose")
    #jobtype.append("EL_EFF_Reco_TOTAL_1NPCOR_PLUS_UNCOR_1down_EleEffSF_offline_RecoTrk")
    #jobtype.append("EL_EFF_Reco_TOTAL_1NPCOR_PLUS_UNCOR_1up_EleEffSF_offline_RecoTrk")
    #jobtype.append("EL_EFF_TriggerEff_TOTAL_1NPCOR_PLUS_UNCOR_1up_efficiency_ELE_TRIG_isolGradient")
    #jobtype.append("EL_EFF_Trigger_TOTAL_1NPCOR_PLUS_UNCOR_1down_EleEffSF_ELE_TRIG_isolFixedCutTight")
    #jobtype.append("EL_EFF_Trigger_TOTAL_1NPCOR_PLUS_UNCOR_1down_EleEffSF_ELE_TRIG_isolGradient")
    #jobtype.append("EL_EFF_Trigger_TOTAL_1NPCOR_PLUS_UNCOR_1down_EleEffSF_ELE_TRIG_isolLoose")
    #jobtype.append("EL_EFF_Trigger_TOTAL_1NPCOR_PLUS_UNCOR_1up_EleEffSF_ELE_TRIG_isolFixedCutTight")
    #jobtype.append("EL_EFF_Trigger_TOTAL_1NPCOR_PLUS_UNCOR_1up_EleEffSF_ELE_TRIG_isolGradient")
    #jobtype.append("EL_EFF_Trigger_TOTAL_1NPCOR_PLUS_UNCOR_1up_EleEffSF_ELE_TRIG_isolLoose")


# fill the dictionaries

print "-------------------------"
print "Printing data summary ..."
print "-------------------------"

in_file_dict = gen_file_dict( os.path.join(inpath,"data") )

out_file_dict = {}
files_out = {}
for d in outdir["data"]:
  out_file_dict[d] = {}
  files_out['data_'+d] = {}
  for jt in jobtype:

    files_out['data_'+d][jt] = []
    out_file_dict[d][jt] = gen_file_dict( os.path.join(outbasepath,d,jt,"data") )

    for odir,ofiles in out_file_dict[d][jt].iteritems():
      for idir, ifiles in in_file_dict.iteritems():
        if os.path.basename(odir) in idir:
          failed_files = []
          if collections.Counter(ifiles) != collections.Counter(ofiles):
            failed_files = find_list_diff(ifiles, ofiles)
            if debug:
                print
                print "WARNING!!! In output dir: %s " % odir
                print "from input dir:           %s " % idir
                print "the following files are missing:"
                print failed_files
                print
            for f in failed_files:
                files_out['data_'+d][jt].append(idir+'/'+f)
          if hadd_files and not failed_files:
            cmd = hadd_cmd( os.path.join(outbasepath,d,jt),  os.path.basename(odir), odir) 
            m = subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE)
            print m.communicate()[0]



print "-------------------------"
print "Printing MC summary ..."
print "-------------------------"

in_file_dict = gen_file_dict( os.path.join(inpath,"mc") )

out_file_dict = {}
for d in outdir["mc"]:
  files_out['mc_'+d] = {}
  out_file_dict[d] = {}
  for jt in jobtype:

    files_out['mc_'+d][jt] = []
    out_file_dict[d][jt] = gen_file_dict( os.path.join(outbasepath,d,jt,"mc") )
    for odir,ofiles in out_file_dict[d][jt].iteritems():
      for idir, ifiles in in_file_dict.iteritems():
        if os.path.basename(odir) in idir:
          failed_files = []
          if collections.Counter(ifiles) != collections.Counter(ofiles):
            failed_files = find_list_diff(ifiles, ofiles)
            if debug:
                print
                print "WARNING!!! In output dir: %s " % odir
                print "from input dir:           %s " % idir
                print "the following files are missing:"
                print failed_files
                print
            for f in failed_files:
                files_out['mc_'+d][jt].append(idir+'/'+f)
          if hadd_files and not failed_files:
            cmd = hadd_cmd( os.path.join(outbasepath,d,jt),  os.path.basename(odir), odir) 
            m = subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE)
            print m.communicate()[0]

# Write missing files to single txt file
for key_dir, outdir in files_out.items():
    for key_syst, files in outdir.items():
        missing_files = open('missing/missing_files_%s__%s.txt' % (key_dir, key_syst), 'w')
        for item in files:
            missing_files.write("%s\n" % item)
        missing_files.close()
# EOF
