#!bin/bash

#-------------------#
#  HLT BDT VARS
#-------------------#

#python ../ztautau/scripts/merge.py --var="tau_pt" --reg="AntiIsoCR_OS" --lab="TEST REGION" --icut="3" --input="/coepp/cephfs/mel/laram1/ztautau/HIST_1201_MEDIUM" --output="./" --makeplot=False
#python ../ztautau/scripts/merge.py --var="tau_pt" --reg="AntiIsoCR_SS" --lab="TEST REGION" --icut="3" --input="/coepp/cephfs/mel/laram1/ztautau/HIST_1201_MEDIUM" --output="./" --makeplot=False
#python ../ztautau/scripts/merge.py --var="tau_pt" --reg="Wjets_OS" --lab="TEST REGION" --icut="3" --input="/coepp/cephfs/mel/laram1/ztautau/HIST_3011_truth_antitruth_mc" --output="./" --makeplot=False
#python ../ztautau/scripts/merge.py --var="tau_pt" --reg="Wjets_SS" --lab="TEST REGION" --icut="3" --input="/coepp/cephfs/mel/laram1/ztautau/HIST_3011_truth_antitruth_mc" --output="./" --makeplot=False
#python ../ztautau/scripts/merge.py --var="vis_mass" --reg="AntiIsoCR_OS_Tau1Track" --lab="TEST REGION" --icut="4" --input="/coepp/cephfs/mel/laram1/ztautau/HIST_1711_errthing" --output="./" --makeplot=True
#python ../ztautau/scripts/merge.py --var="vis_mass" --reg="AntiIsoCR_OS_Tau3Track" --lab="TEST REGION" --icut="4" --input="/coepp/cephfs/mel/laram1/ztautau/HIST_1711_errthing" --output="./" --makeplot=True
#python ../ztautau/scripts/merge.py --var="m_trans" --reg="Wjets_OS_Tau3Track" --lab="TEST REGION" --icut="4" --input="/coepp/cephfs/mel/laram1/ztautau/HIST_1711_errthing" --output="./" --makeplot=True
#python ../ztautau/scripts/merge.py --var="vis_mass" --reg="Wjets_OS_Tau3Track" --lab="TEST REGION" --icut="4" --input="/coepp/cephfs/mel/laram1/ztautau/HIST_1711_errthing" --output="./" --makeplot=True
#python ../ztautau/scripts/merge.py --var="m_trans" --reg="Wjets_OS_Tau1Track" --lab="TEST REGION" --icut="4" --input="/coepp/cephfs/mel/laram1/ztautau/HIST_1711_errthing" --output="./" --makeplot=True
#python ../ztautau/scripts/merge.py --var="vis_mass" --reg="Wjets_OS_Tau1Track" --lab="TEST REGION" --icut="4" --input="/coepp/cephfs/mel/laram1/ztautau/HIST_1711_errthing" --output="./" --makeplot=True
#python ../ztautau/scripts/merge.py --var="vis_mass" --reg="Wjets_OS_Tau1Track" --lab="TEST REGION" --icut="4" --input="/coepp/cephfs/mel/laram1/ztautau/HIST_1711_errthing" --output="./" --makeplot=True

#python ../ztautau/scripts/merge.py --var="HLT_tau_n_tracks" --reg="SR_Tau3Track" --lab="3-prong, pt cut 25 GeV" --icut="5" --input="/coepp/cephfs/mel/laram1/ztautau/HIST_1201_MEDIUM" --output="./" --makeplot=True
#python ../ztautau/scripts/merge.py --var="HLT_tau_n_tracks" --reg="SR_Tau3Track" --lab="3-prong, pt cut 85 GeV" --icut="5" --input="/coepp/cephfs/mel/laram1/ztautau/HIST_v25_taupt85_new" --output="./" --makeplot=True
##python ../ztautau/scripts/merge.py --var="HLT_frac_trks_iso_region" --reg="SR_25med_Tau1Track" --lab="TEST REGION" --icut="6" --input="/coepp/cephfs/mel/laram1/ztautau/HIST_0711_HLT_BDT_vars" --output="./" --makeplot=True
#python ../ztautau/scripts/merge.py --var="HLT_m_trk_EM_system" --reg="SR_ptonly_Tau1Track" --lab="TEST REGION" --icut="6" --input="/coepp/cephfs/mel/laram1/ztautau/HIST_2011_v23_new" --output="./" --makeplot=True
#python ../ztautau/scripts/merge.py --var="HLT_m_trk_EM_system" --reg="SR_25med_Tau1Track" --lab="TEST REGION" --icut="6" --input="/coepp/cephfs/mel/laram1/ztautau/HIST_2011_v23_new" --output="./" --makeplot=True
#python ../ztautau/scripts/merge.py --var="HLT_m_trk_EM_system" --reg="SR_Tau1Track" --lab="TEST REGION" --icut="5" --input="/coepp/cephfs/mel/laram1/ztautau/HIST_2011_v23_new" --output="./" --makeplot=True
#python ../ztautau/scripts/merge.py --var="HLT_1P_lead_trk_IP_sig" --reg="SR_Tau1Track" --lab="TEST REGION" --icut="5" --input="/coepp/cephfs/mel/laram1/ztautau/HIST_2011_v23_new" --output="./" --makeplot=True
#python ../ztautau/scripts/merge.py --var="HLT_trk_radius" --reg="SR_25med_Tau1Track" --lab="TEST REGION" --icut="6" --input="/coepp/cephfs/mel/laram1/ztautau/HIST_0711_HLT_BDT_vars" --output="./" --makeplot=True
#python ../ztautau/scripts/merge.py --var="HLT_lead_trk_p_frac" --reg="SR_25med_Tau1Track" --lab="TEST REGION" --icut="6" --input="/coepp/cephfs/mel/laram1/ztautau/HIST_0711_HLT_BDT_vars" --output="./" --makeplot=True
#python ../ztautau/scripts/merge.py --var="HLT_ratio_energy_to_trk_p" --reg="SR_25med_Tau1Track" --lab="TEST REGION" --icut="6" --input="/coepp/cephfs/mel/laram1/ztautau/HIST_0711_HLT_BDT_vars" --output="./" --makeplot=True
#python ../ztautau/scripts/merge.py --var="HLT_frac_EM_from_charged_pions" --reg="SR_Tau1Track" --lab="TEST REGION" --icut="5" --input="/coepp/cephfs/mel/laram1/ztautau/HIST_1711_errthing" --output="./" --makeplot=True
#python ../ztautau/scripts/merge.py --var="HLT_fcent" --reg="SR_25med_Tau1Track" --lab="TEST REGION" --icut="6" --input="/coepp/cephfs/mel/laram1/ztautau/HIST_0711_HLT_BDT_vars" --output="./" --makeplot=True

#python ../ztautau/scripts/merge.py --var="HLT_massTrkSysCorrected" --reg="SR_25med_Tau3Track" --lab="TEST REGION" --icut="6" --input="/coepp/cephfs/mel/laram1/ztautau/HIST_0711_HLT_BDT_vars" --output="./" --makeplot=True
#python ../ztautau/scripts/merge.py --var="HLT_frac_trks_iso_region" --reg="SR_25med_Tau3Track" --lab="TEST REGION" --icut="6" --input="/coepp/cephfs/mel/laram1/ztautau/HIST_0711_HLT_BDT_vars" --output="./" --makeplot=True
#python ../ztautau/scripts/merge.py --var="HLT_m_trk_EM_system" --reg="SR_25med_Tau3Track" --lab="TEST REGION" --icut="6" --input="/coepp/cephfs/mel/laram1/ztautau/HIST_0711_HLT_BDT_vars" --output="./" --makeplot=True
#python ../ztautau/scripts/merge.py --var="HLT_lead_trk_IP_sig" --reg="SR_25med_Tau3Track" --lab="TEST REGION" --icut="6" --input="/coepp/cephfs/mel/laram1/ztautau/HIST_0711_HLT_BDT_vars" --output="./" --makeplot=True
#python ../ztautau/scripts/merge.py --var="HLT_trk_radius" --reg="SR_25med_Tau3Track" --lab="TEST REGION" --icut="6" --input="/coepp/cephfs/mel/laram1/ztautau/HIST_0711_HLT_BDT_vars" --output="./" --makeplot=True
#python ../ztautau/scripts/merge.py --var="HLT_lead_trk_p_frac" --reg="SR_25med_Tau3Track" --lab="TEST REGION" --icut="6" --input="/coepp/cephfs/mel/laram1/ztautau/HIST_0711_HLT_BDT_vars" --output="./" --makeplot=True
#python ../ztautau/scripts/merge.py --var="HLT_ratio_energy_to_trk_p" --reg="SR_25med_Tau3Track" --lab="TEST REGION" --icut="6" --input="/coepp/cephfs/mel/laram1/ztautau/HIST_0711_HLT_BDT_vars" --output="./" --makeplot=True
#python ../ztautau/scripts/merge.py --var="HLT_frac_EM_from_charged_pions" --reg="SR_25med_Tau3Track" --lab="TEST REGION" --icut="6" --input="/coepp/cephfs/mel/laram1/ztautau/HIST_0711_HLT_BDT_vars" --output="./" --makeplot=True
#python ../ztautau/scripts/merge.py --var="HLT_fcent" --reg="SR_25med_Tau3Track" --lab="TEST REGION" --icut="6" --input="/coepp/cephfs/mel/laram1/ztautau/HIST_0711_HLT_BDT_vars" --output="./" --makeplot=True
#
#python ../ztautau/scripts/merge.py --var="HLT_pt_res_TProfile" --reg="SR_Tau1Track" --lab="TEST REGION" --icut="5" --input="/coepp/cephfs/mel/laram1/ztautau/HIST_0112_v23_truth_taupt_30" --output="../ztautau/scripts/HLT_pt_res_plot/" --makeplot=True
#python ../ztautau/scripts/merge.py --var="HLT_pt_res_TProfile" --reg="SR_Tau3Track" --lab="TEST REGION" --icut="5" --input="/coepp/cephfs/mel/laram1/ztautau/HIST_0112_v23_truth_taupt_30" --output="../ztautau/scripts/HLT_pt_res_plot/" --makeplot=True
#python ../ztautau/scripts/merge.py --var="HLT_pt_res" --reg="SR_Tau1Track" --lab="TEST REGION" --icut="5" --input="/coepp/cephfs/mel/laram1/ztautau/HIST_0112_v23_truth_taupt_30" --output="../ztautau/scripts/HLT_pt_res_plot/" --makeplot=False
#python ../ztautau/scripts/merge.py --var="HLT_pt_res" --reg="SR_Tau3Track" --lab="TEST REGION" --icut="5" --input="/coepp/cephfs/mel/laram1/ztautau/HIST_0112_v23_truth_taupt_30" --output="../ztautau/scripts/HLT_pt_res_plot/" --makeplot=False
#python ../ztautau/scripts/merge.py --var="HLT_jet_bdt_score" --reg="SR_25med" --lab="TEST REGION" --icut="5" --input="/coepp/cephfs/mel/laram1/ztautau/HIST_0211_v22_HLT_vars" --output="./" --makeplot=True
#python ../ztautau/scripts/merge.py --var="Presel_tau_pt" --reg="SR_25med" --lab="TEST REGION" --icut="5" --input="/coepp/cephfs/mel/laram1/ztautau/HIST_0311_v22_HLT_Presel_vars" --output="./" --makeplot=True
#python ../ztautau/scripts/merge.py --var="Presel_tau_phi" --reg="SR_25med" --lab="TEST REGION" --icut="5" --input="/coepp/cephfs/mel/laram1/ztautau/HIST_0311_v22_HLT_Presel_vars" --output="./" --makeplot=True
#python ../ztautau/scripts/merge.py --var="Presel_tau_pt" --reg="SR_25med" --lab="TEST REGION" --icut="5" --input="/coepp/cephfs/mel/laram1/ztautau/HIST_0311_v22_HLT_Presel_vars" --output="./" --makeplot=True
#python ../ztautau/scripts/merge.py --var="Presel_jet_bdt_score" --reg="SR_25med" --lab="TEST REGION" --icut="5" --input="/coepp/cephfs/mel/laram1/ztautau/HIST_0211_v22_HLT_vars" --output="./" --makeplot=True



#-------------------#
#	SR
#-------------------#


#python ../ztautau/scripts/merge.py --var="tau_n_tracks" --reg="SR_Tau3Track" --lab="3-prong, pt cut 25 GeV" --icut="5" --input="/coepp/cephfs/mel/laram1/ztautau/HIST_1201_MEDIUM" --output="./" --makeplot=True
#python ../ztautau/scripts/merge.py --var="tau_pt" --reg="SR_Tau1Track" --lab="" --icut="5" --input="/coepp/cephfs/mel/laram1/ztautau/HIST_2901_v26_all_trigs" --output="./" --makeplot=True
#python ../ztautau/scripts/merge.py --var="tau_n_tracks" --reg="SR_Tau3Track" --lab="3-prong, pt cut 130 GeV" --icut="5" --input="/coepp/cephfs/mel/laram1/ztautau/HIST_2801_v25_taupt130" --output="./" --makeplot=True
#python ../ztautau/scripts/merge.py --var="tau_pt" --reg="SR_25med_Tau1Track" --lab="25med" --icut="6" --input="/coepp/cephfs/mel/laram1/ztautau/HIST_0712_v25_2016_MEDIUM" --output="./" --makeplot=True
python ../ztautau/scripts/merge.py --var="tau_eta" --reg="SR" --lab="Sig-Reg" --icut="4" --input="/coepp/cephfs/mel/laram1/ztautau/HIST_2801_v26" --output="./" --makeplot=True
python ../ztautau/scripts/merge.py --var="tau_pt" --reg="SR" --lab="" --icut="4" --input="/coepp/cephfs/mel/laram1/ztautau/HIST_2801_v26" --output="./" --makeplot=True
#python ../ztautau/scripts/merge.py --var="tau_pt" --reg="SR" --lab="" --icut="4" --input="/coepp/cephfs/mel/laram1/ztautau/HIST_1601_v26_2015" --output="./" --makeplot=False
#python ../ztautau/scripts/merge.py --var="tau_pt" --reg="SR_25med" --lab="" --icut="5" --input="/coepp/cephfs/mel/laram1/ztautau/HIST_1001_v26_MEDIUM_2015" --output="./" --makeplot=True
#python ../ztautau/scripts/merge.py --var="mu_eta" --reg="SR" --lab="" --icut="4" --input="/coepp/cephfs/mel/laram1/ztautau/HIST_2801_v26" --output="./" --makeplot=True
#python ../ztautau/scripts/merge.py --var="mu_phi" --reg="SR" --lab="" --icut="4" --input="/coepp/cephfs/mel/laram1/ztautau/HIST_2611_v23" --output="./" --makeplot=True
#python ../ztautau/scripts/merge.py --var="mu_pt" --reg="SR" --lab="" --icut="4" --input="/coepp/cephfs/mel/laram1/ztautau/HIST_2801_v26" --output="./" --makeplot=True
#python ../ztautau/scripts/merge.py --var="tau_pt" --reg="SR_25med_Tau3Track" --lab="" --icut="6" --input="/coepp/cephfs/mel/laram1/ztautau/HIST_1001_mu_pt_split_chains_TIGHT" --output="./" --makeplot=True
#python ../ztautau/scripts/merge.py --var="tau_pt" --reg="SR_Tau3Track" --lab="" --icut="5" --input="/coepp/cephfs/mel/laram1/ztautau/HIST_1001_mu_pt_split_chains_TIGHT" --output="./" --makeplot=True

#python ../ztautau/scripts/merge.py --var="tau_pt" --reg="SR_Tau3Track" --lab="" --icut="5" --input="/coepp/cephfs/mel/laram1/ztautau/HIST_0901_v25_2016_rqcd_mu_pt" --output="./" --makeplot=True
#python ../ztautau/scripts/merge.py --var="tau_pt" --reg="SR_25med_Tau3Track" --lab="tau 25 medium trigger" --icut="6" --input="/coepp/cephfs/mel/laram1/ztautau/HIST_0901_v25_2016_rqcd_mu_pt" --output="./" --makeplot=True
#python ../ztautau/scripts/merge.py --var="tau_pt" --reg="SR_35med_Tau3Track" --lab="tau 35 medium trigger" --icut="6" --input="/coepp/cephfs/mel/laram1/ztautau/HIST_1711_errthing" --output="./" --makeplot=True

#---------------------#
#	 2-D
#---------------------#

#python ../ztautau/scripts/merge.py --var="m_trans_vs_sumcosdphi" --reg="SR_SS_no_cuts_2D" --lab="TEST REGION" --icut="2" --input="/coepp/cephfs/mel/laram1/ztautau/HIST_2909_oldvismass_newwjetsregions_with2Dhist_SR_no_cuts" --output="./" --makeplot=True

#python ../ztautau/scripts/merge.py --var="met_reco_et_vs_sumcosdphi" --reg="SR_SS_no_cuts_2D" --lab="TEST REGION" --icut="2" --input="/coepp/cephfs/mel/laram1/ztautau/HIST_2909_oldvismass_newwjetsregions_with2Dhist_SR_no_cuts" --output="./" --makeplot=True

#python ../ztautau/scripts/merge.py --var="met_reco_et_vs_m_trans" --reg="SR_SS_no_cuts_2D" --lab="TEST REGION" --icut="2" --input="/coepp/cephfs/mel/laram1/ztautau/HIST_2909_oldvismass_newwjetsregions_with2Dhist_SR_no_cuts" --output="./" --makeplot=True
#
#python ../ztautau/scripts/merge.py --var="m_trans_vs_sumcosdphi" --reg="SR_OS_no_cuts_for2D" --lab="TEST REGION" --icut="2" --input="/coepp/cephfs/mel/laram1/ztautau/HIST_2909_oldvismass_newwjetsregions_with2Dhist_SR_no_cuts" --output="./" --makeplot=True

#python ../ztautau/scripts/merge.py --var="met_reco_et_vs_sumcosdphi" --reg="SR_OS_no_cuts_for2D" --lab="TEST REGION" --icut="2" --input="/coepp/cephfs/mel/laram1/ztautau/HIST_2909_oldvismass_newwjetsregions_with2Dhist_SR_no_cuts" --output="./" --makeplot=True

#python ../ztautau/scripts/merge.py --var="met_reco_et_vs_m_trans" --reg="SR_OS_no_cuts_for2D" --lab="TEST REGION" --icut="2" --input="/coepp/cephfs/mel/laram1/ztautau/HIST_2909_oldvismass_newwjetsregions_with2Dhist_SR_no_cuts" --output="./" --makeplot=True
#
#python ../ztautau/scripts/merge.py --var="m_trans_vs_sumcosdphi" --reg="SR_lowSCDP" --lab="TEST REGION" --icut="3" --input="/coepp/cephfs/mel/laram1/ztautau/HIST_2809_oldvismass_newwjetsregions_with2Dhist" --output="./" --makeplot=True

#python ../ztautau/scripts/merge.py --var="met_reco_et_vs_sumcosdphi" --reg="SR_lowSCDP" --lab="TEST REGION" --icut="3" --input="/coepp/cephfs/mel/laram1/ztautau/HIST_2809_oldvismass_newwjetsregions_with2Dhist" --output="./" --makeplot=True

#python ../ztautau/scripts/merge.py --var="met_reco_et_vs_m_trans" --reg="SR_lowSCDP" --lab="TEST REGION" --icut="3" --input="/coepp/cephfs/mel/laram1/ztautau/HIST_2809_oldvismass_newwjetsregions_with2Dhist" --output="./" --makeplot=True
#
#python ../ztautau/scripts/merge.py --var="m_trans_vs_sumcosdphi" --reg="SR_highSCDP" --lab="TEST REGION" --icut="3" --input="/coepp/cephfs/mel/laram1/ztautau/HIST_2809_oldvismass_newwjetsregions_with2Dhist" --output="./" --makeplot=True

#python ../ztautau/scripts/merge.py --var="met_reco_et_vs_sumcosdphi" --reg="SR_highSCDP" --lab="TEST REGION" --icut="3" --input="/coepp/cephfs/mel/laram1/ztautau/HIST_2809_oldvismass_newwjetsregions_with2Dhist" --output="./" --makeplot=True

#python ../ztautau/scripts/merge.py --var="met_reco_et_vs_m_trans" --reg="SR_highSCDP" --lab="TEST REGION" --icut="3" --input="/coepp/cephfs/mel/laram1/ztautau/HIST_2809_oldvismass_newwjetsregions_with2Dhist" --output="./" --makeplot=True

#----------------------#
#	NO CUTS
#----------------------#

#python ../ztautau/scripts/merge.py --var="vis_mass" --reg="SR_OS_no_cuts_forvismass" --lab="TEST REGION" --icut="3" --input="/coepp/cephfs/mel/laram1/ztautau/HIST_1201_MEDIUM" --output="./" --makeplot=True

#----------------------#
#	LOWCSDP
#----------------------#

#python ../ztautau/scripts/merge.py --var="m_trans" --reg="SR_highSCDP" --lab="TEST REGION" --icut="3" --input="/coepp/cephfs/mel/laram1/ztautau/HIST_0410_new_mt_regions" --output="./" --makeplot=True
#python ../ztautau/scripts/merge.py --var="tau_pt" --reg="SR_lowSCDP" --lab="TEST REGION" --icut="4" --input="/coepp/cephfs/mel/laram1/ztautau/HIST_3011_truth_antitruth_mc" --output="./" --makeplot=True
#python ../ztautau/scripts/merge.py --var="tau_pt" --reg="SR_lowSCDP" --lab="TEST REGION" --icut="4" --input="/coepp/cephfs/mel/laram1/ztautau/HIST_3011_truth_antitruth_mc" --output="./" --makeplot=False

#python ../ztautau/scripts/merge.py --var="m_trans" --reg="SR_lowSCDP" --lab="TEST REGION" --icut="4" --input="/coepp/cephfs/mel/laram1/ztautau/HIST_1711_errthing" --output="./" --makeplot=True
#python ../ztautau/scripts/merge.py --var="m_trans" --reg="SR_lowSCDP_Tau1Track" --lab="TEST REGION" --icut="5" --input="/coepp/cephfs/mel/laram1/ztautau/HIST_1711_errthing" --output="./" --makeplot=True
#python ../ztautau/scripts/merge.py --var="m_trans" --reg="SR_lowSCDP_Tau3Track" --lab="TEST REGION" --icut="5" --input="/coepp/cephfs/mel/laram1/ztautau/HIST_1711_errthing" --output="./" --makeplot=True

#python ../ztautau/scripts/merge.py --var="vis_mass" --reg="SR_lowSCDP" --lab="TEST REGION" --icut="4" --input="/coepp/cephfs/mel/laram1/ztautau/HIST_1711_errthing" --output="./" --makeplot=True
#python ../ztautau/scripts/merge.py --var="vis_mass" --reg="SR_lowSCDP_Tau1Track" --lab="TEST REGION" --icut="5" --input="/coepp/cephfs/mel/laram1/ztautau/HIST_1711_errthing" --output="./" --makeplot=True
#python ../ztautau/scripts/merge.py --var="vis_mass" --reg="SR_lowSCDP_Tau3Track" --lab="TEST REGION" --icut="5" --input="/coepp/cephfs/mel/laram1/ztautau/HIST_1711_errthing" --output="./" --makeplot=True

#python ../ztautau/scripts/merge.py --var="tau_pt" --reg="SR_lowSCDP_25med" --lab="TEST REGION" --icut="5" --input="/coepp/cephfs/mel/laram1/ztautau/HIST_2810_v22_all_trigs_and_chains" --output="./" --makeplot=False
#python ../ztautau/scripts/merge.py --var="tau_pt" --reg="SR_lowSCDP_SS25med" --lab="TEST REGION" --icut="5" --input="/coepp/cephfs/mel/laram1/ztautau/HIST_2810_v22_all_trigs_and_chains" --output="./" --makeplot=False

#python ../ztautau/scripts/merge.py --var="tau_pt" --reg="SR_lowSCDP_lowMT" --lab="TEST REGION" --icut="4" --input="/coepp/cephfs/mel/laram1/ztautau/HIST_0410_new_mt_regions" --output="./" --makeplot=False
#python ../ztautau/scripts/merge.py --var="tau_pt" --reg="SR_lowSCDP_lowMT_SS" --lab="TEST REGION" --icut="4" --input="/coepp/cephfs/mel/laram1/ztautau/HIST_0410_new_mt_regions" --output="./" --makeplot=False

#python ../ztautau/scripts/merge.py --var="tau_pt" --reg="SR_lowSCDP_lowMT_Tau1Track" --lab="TEST REGION" --icut="5" --input="/coepp/cephfs/mel/laram1/ztautau/HIST_1809_Wjets_estimation_new" --output="./" --makeplot=True
#python ../ztautau/scripts/merge.py --var="tau_pt" --reg="SR_lowSCDP_lowMT_SS_Tau1Track" --lab="TEST REGION" --icut="5" --input="/coepp/cephfs/mel/laram1/ztautau/HIST_1809_Wjets_estimation_new" --output="./" --makeplot=True

#python ../ztautau/scripts/merge.py --var="tau_pt" --reg="SR_lowSCDP_lowMT_Tau3Track" --lab="TEST REGION" --icut="5" --input="/coepp/cephfs/mel/laram1/ztautau/HIST_1809_Wjets_estimation_new" --output="./" --makeplot=False
#python ../ztautau/scripts/merge.py --var="tau_pt" --reg="SR_lowSCDP_lowMT_SS_Tau3Track" --lab="TEST REGION" --icut="5" --input="/coepp/cephfs/mel/laram1/ztautau/HIST_1809_Wjets_estimation_new" --output="./" --makeplot=False

#---------------------------#
#   EFFICIENCIES v22 TAU PT
#---------------------------#

#     ONE PRONG  
#python ../ztautau/scripts/merge.py --var="tau_pt" --reg="SR_Tau1Track" --lab="TEST" --icut="5" --input="/coepp/cephfs/mel/laram1/ztautau/HIST_2801_v26" --output="./Hists_systematics/BDT_medium/" --makeplot=False
#python ../ztautau/scripts/merge.py --var="tau_pt" --reg="SR_25med_Tau1Track" --lab="TEST REGION" --icut="6" --input="/coepp/cephfs/mel/laram1/ztautau/HIST_2801_v26" --output="./Hists_systematics/BDT_medium/" --makeplot=False
#python ../ztautau/scripts/merge.py --var="tau_pt" --reg="SR_35med_Tau1Track" --lab="TEST REGION" --icut="6" --input="/coepp/cephfs/mel/laram1/ztautau/HIST_2901_v26_all_trigs" --output="./Hists_systematics/BDT_medium/" --makeplot=False
#python ../ztautau/scripts/merge.py --var="tau_pt" --reg="SR_50L1TAU12med_Tau1Track" --lab="TEST REGION" --icut="6" --input="/coepp/cephfs/mel/laram1/ztautau/HIST_2901_v26_all_trigs" --output="./Hists_systematics/BDT_medium/" --makeplot=False
#python ../ztautau/scripts/merge.py --var="tau_pt" --reg="SR_80med_Tau1Track" --lab="TEST REGION" --icut="6" --input="/coepp/cephfs/mel/laram1/ztautau/HIST_2901_v26_all_trigs" --output="./Hists_systematics/BDT_medium/" --makeplot=False
#python ../ztautau/scripts/merge.py --var="tau_pt" --reg="SR_80L1TAU60med_Tau1Track" --lab="TEST REGION" --icut="6" --input="/coepp/cephfs/mel/laram1/ztautau/HIST_2901_v26_all_trigs" --output="./Hists_systematics/BDT_medium/" --makeplot=False
#python ../ztautau/scripts/merge.py --var="tau_pt" --reg="SR_125med_Tau1Track" --lab="TEST REGION" --icut="6" --input="/coepp/cephfs/mel/laram1/ztautau/HIST_2901_v26_all_trigs" --output="./Hists_systematics/BDT_medium/" --makeplot=False
#python ../ztautau/scripts/merge.py --var="tau_pt" --reg="SR_160med_Tau1Track" --lab="TEST REGION" --icut="6" --input="/coepp/cephfs/mel/laram1/ztautau/HIST_2901_v26_all_trigs" --output="./Hists_systematics/BDT_medium/" --makeplot=False

#python ../ztautau/scripts/merge.py --var="tau_pt" --reg="SR_L1TAU12IMmed_Tau1Track" --lab="TEST REGION" --icut="6" --input="/coepp/cephfs/mel/laram1/ztautau/HIST_2901_v26_all_trigs" --output="./Hists_systematics/BDT_medium/" --makeplot=False
#python ../ztautau/scripts/merge.py --var="tau_pt" --reg="SR_tracktwo_Tau1Track" --lab="TEST REGION" --icut="6" --input="/coepp/cephfs/mel/laram1/ztautau/HIST_2901_v26_all_trigs" --output="./Hists_systematics/BDT_medium/" --makeplot=False
#python ../ztautau/scripts/merge.py --var="tau_pt" --reg="SR_ptonly_Tau1Track" --lab="TEST REGION" --icut="6" --input="/coepp/cephfs/mel/laram1/ztautau/HIST_2901_v26_all_trigs" --output="./Hists_systematics/BDT_medium/" --makeplot=False

#     THREE PRONG  

#python ../ztautau/scripts/merge.py --var="tau_pt" --reg="SR_Tau3Track" --lab="TEST" --icut="5" --input="/coepp/cephfs/mel/laram1/ztautau/HIST_2801_v26" --output="./Hists_systematics/BDT_medium/" --makeplot=False
#python ../ztautau/scripts/merge.py --var="tau_pt" --reg="SR_25med_Tau3Track" --lab="TEST REGION" --icut="6" --input="/coepp/cephfs/mel/laram1/ztautau/HIST_2801_v26" --output="./Hists_systematics/BDT_medium/" --makeplot=False
#python ../ztautau/scripts/merge.py --var="tau_pt" --reg="SR_35med_Tau3Track" --lab="TEST REGION" --icut="6" --input="/coepp/cephfs/mel/laram1/ztautau/HIST_2901_v26_all_trigs" --output="./Hists_systematics/BDT_medium/" --makeplot=False
#python ../ztautau/scripts/merge.py --var="tau_pt" --reg="SR_50L1TAU12med_Tau3Track" --lab="TEST REGION" --icut="6" --input="/coepp/cephfs/mel/laram1/ztautau/HIST_2901_v26_all_trigs" --output="./Hists_systematics/BDT_medium/" --makeplot=False
#python ../ztautau/scripts/merge.py --var="tau_pt" --reg="SR_80med_Tau3Track" --lab="TEST REGION" --icut="6" --input="/coepp/cephfs/mel/laram1/ztautau/HIST_2901_v26_all_trigs" --output="./Hists_systematics/BDT_medium/" --makeplot=False
#python ../ztautau/scripts/merge.py --var="tau_pt" --reg="SR_80L1TAU60med_Tau3Track" --lab="TEST REGION" --icut="6" --input="/coepp/cephfs/mel/laram1/ztautau/HIST_2901_v26_all_trigs" --output="./Hists_systematics/BDT_medium/" --makeplot=False
#python ../ztautau/scripts/merge.py --var="tau_pt" --reg="SR_125med_Tau3Track" --lab="TEST REGION" --icut="6" --input="/coepp/cephfs/mel/laram1/ztautau/HIST_2901_v26_all_trigs" --output="./Hists_systematics/BDT_medium/" --makeplot=False
#python ../ztautau/scripts/merge.py --var="tau_pt" --reg="SR_160med_Tau3Track" --lab="TEST REGION" --icut="6" --input="/coepp/cephfs/mel/laram1/ztautau/HIST_2901_v26_all_trigs" --output="./Hists_systematics/BDT_medium/" --makeplot=False
#python ../ztautau/scripts/merge.py --var="tau_pt" --reg="SR_L1TAU12IMmed_Tau3Track" --lab="TEST REGION" --icut="6" --input="/coepp/cephfs/mel/laram1/ztautau/HIST_2901_v26_all_trigs" --output="./Hists_systematics/BDT_medium/" --makeplot=False
#
#python ../ztautau/scripts/merge.py --var="tau_pt" --reg="SR_tracktwo_Tau3Track" --lab="TEST REGION" --icut="6" --input="/coepp/cephfs/mel/laram1/ztautau/HIST_2901_v26_all_trigs" --output="./Hists_systematics/BDT_medium/" --makeplot=False
#python ../ztautau/scripts/merge.py --var="tau_pt" --reg="SR_ptonly_Tau3Track" --lab="TEST REGION" --icut="6" --input="/coepp/cephfs/mel/laram1/ztautau/HIST_2901_v26_all_trigs" --output="./Hists_systematics/BDT_medium/" --makeplot=False
#
##---------------------------#
#   EFFICIENCIES v22 TAU ETA
#---------------------------#

###     ONE PRONG  
#python ../ztautau/scripts/merge.py --var="tau_eta" --reg="SR_Tau1Track" --lab="TEST" --icut="5" --input="/coepp/cephfs/mel/laram1/ztautau/HIST_0501_v26_taupt_30" --output="./Hists_systematics/BDT_medium/" --makeplot=False
#python ../ztautau/scripts/merge.py --var="tau_eta" --reg="SR_25med_Tau1Track" --lab="TEST REGION" --icut="6" --input="/coepp/cephfs/mel/laram1/ztautau/HIST_0501_v26_taupt_30" --output="./Hists_systematics/BDT_medium/" --makeplot=True
#python ../ztautau/scripts/merge.py --var="tau_eta" --reg="SR_35med_Tau1Track" --lab="TEST REGION" --icut="6" --input="/coepp/cephfs/mel/laram1/ztautau/HIST_1311_taupt40" --output="./" --makeplot=False
#python ../ztautau/scripts/merge.py --var="tau_eta" --reg="SR_50L1TAU12med_Tau1Track" --lab="TEST REGION" --icut="6" --input="/coepp/cephfs/mel/laram1/ztautau/HIST_1311_taupt55" --output="./" --makeplot=False
#python ../ztautau/scripts/merge.py --var="tau_eta" --reg="SR_80med_Tau1Track" --lab="TEST REGION" --icut="6" --input="/coepp/cephfs/mel/laram1/ztautau/HIST_1311_taupt85" --output="./" --makeplot=False
#python ../ztautau/scripts/merge.py --var="tau_eta" --reg="SR_80L1TAU60med_Tau1Track" --lab="TEST REGION" --icut="6" --input="/coepp/cephfs/mel/laram1/ztautau/HIST_1311_taupt85" --output="./" --makeplot=False
#python ../ztautau/scripts/merge.py --var="tau_eta" --reg="SR_125med_Tau1Track" --lab="TEST REGION" --icut="6" --input="/coepp/cephfs/mel/laram1/ztautau/HIST_1711_taupt130" --output="./" --makeplot=False
#python ../ztautau/scripts/merge.py --var="tau_eta" --reg="SR_160med_Tau1Track" --lab="TEST REGION" --icut="6" --input="/coepp/cephfs/mel/laram1/ztautau/HIST_1711_taupt165" --output="./" --makeplot=False

#python ../ztautau/scripts/merge.py --var="tau_eta" --reg="SR_L1TAU12IMmed_Tau1Track" --lab="TEST REGION" --icut="6" --input="/coepp/cephfs/mel/laram1/ztautau/HIST_0501_v26_taupt_30" --output="./" --makeplot=False
#python ../ztautau/scripts/merge.py --var="tau_eta" --reg="SR_tracktwo_Tau1Track" --lab="TEST REGION" --icut="6" --input="/coepp/cephfs/mel/laram1/ztautau/HIST_0501_v26_taupt_30" --output="./" --makeplot=False
#python ../ztautau/scripts/merge.py --var="tau_eta" --reg="SR_ptonly_Tau1Track" --lab="TEST REGION" --icut="6" --input="/coepp/cephfs/mel/laram1/ztautau/HIST_0501_v26_taupt_30" --output="./" --makeplot=False
#     THREE PRONG  

#python ../ztautau/scripts/merge.py --var="tau_eta" --reg="SR_Tau3Track" --lab="TEST" --icut="5" --input="/coepp/cephfs/mel/laram1/ztautau/HIST_0501_v26_taupt_30" --output="./Hists_systematics/BDT_medium/" --makeplot=False
#python ../ztautau/scripts/merge.py --var="tau_eta" --reg="SR_25med_Tau3Track" --lab="TEST REGION" --icut="6" --input="/coepp/cephfs/mel/laram1/ztautau/HIST_0501_v26_taupt_30" --output="./Hists_systematics/BDT_medium/" --makeplot=False
#python ../ztautau/scripts/merge.py --var="tau_eta" --reg="SR_35med_Tau3Track" --lab="TEST REGION" --icut="6" --input="/coepp/cephfs/mel/laram1/ztautau/HIST_1311_taupt40" --output="./" --makeplot=False
#python ../ztautau/scripts/merge.py --var="tau_eta" --reg="SR_50L1TAU12med_Tau3Track" --lab="TEST REGION" --icut="6" --input="/coepp/cephfs/mel/laram1/ztautau/HIST_1311_taupt55" --output="./" --makeplot=False
#python ../ztautau/scripts/merge.py --var="tau_eta" --reg="SR_80med_Tau3Track" --lab="TEST REGION" --icut="6" --input="/coepp/cephfs/mel/laram1/ztautau/HIST_1311_taupt85" --output="./" --makeplot=False
#python ../ztautau/scripts/merge.py --var="tau_eta" --reg="SR_80L1TAU60med_Tau3Track" --lab="TEST REGION" --icut="6" --input="/coepp/cephfs/mel/laram1/ztautau/HIST_1311_taupt85" --output="./" --makeplot=False
#python ../ztautau/scripts/merge.py --var="tau_eta" --reg="SR_125med_Tau3Track" --lab="TEST REGION" --icut="6" --input="/coepp/cephfs/mel/laram1/ztautau/HIST_1711_taupt130" --output="./" --makeplot=False
#python ../ztautau/scripts/merge.py --var="tau_eta" --reg="SR_160med_Tau3Track" --lab="TEST REGION" --icut="6" --input="/coepp/cephfs/mel/laram1/ztautau/HIST_1711_taupt165" --output="./" --makeplot=False
#
#python ../ztautau/scripts/merge.py --var="tau_eta" --reg="SR_L1TAU12IMmed_Tau3Track" --lab="TEST REGION" --icut="6" --input="/coepp/cephfs/mel/laram1/ztautau/HIST_0501_v26_taupt_30" --output="./" --makeplot=False
#python ../ztautau/scripts/merge.py --var="tau_eta" --reg="SR_tracktwo_Tau3Track" --lab="TEST REGION" --icut="6" --input="/coepp/cephfs/mel/laram1/ztautau/HIST_0501_v26_taupt_30" --output="./" --makeplot=False
#python ../ztautau/scripts/merge.py --var="tau_eta" --reg="SR_ptonly_Tau3Track" --lab="TEST REGION" --icut="6" --input="/coepp/cephfs/mel/laram1/ztautau/HIST_0501_v26_taupt_30" --output="./" --makeplot=False

#---------------------------#
#   EFFICIENCIES v22 pileup
#---------------------------#

##     ONE PRONG  
#python ../ztautau/scripts/merge.py --var="pileup" --reg="SR_Tau1Track" --lab="TEST" --icut="5" --input="/coepp/cephfs/mel/laram1/ztautau/HIST_0501_v26_taupt_30" --output="./Hists_systematics/BDT_medium/" --makeplot=False
#python ../ztautau/scripts/merge.py --var="pileup" --reg="SR_25med_Tau1Track" --lab="TEST REGION" --icut="6" --input="/coepp/cephfs/mel/laram1/ztautau/HIST_0501_v26_taupt_30" --output="./Hists_systematics/BDT_medium/" --makeplot=False
#python ../ztautau/scripts/merge.py --var="pileup" --reg="SR_35med_Tau1Track" --lab="TEST REGION" --icut="6" --input="/coepp/cephfs/mel/laram1/ztautau/HIST_1311_taupt40" --output="./" --makeplot=False
#python ../ztautau/scripts/merge.py --var="pileup" --reg="SR_50L1TAU12med_Tau1Track" --lab="TEST REGION" --icut="6" --input="/coepp/cephfs/mel/laram1/ztautau/HIST_1311_taupt55" --output="./" --makeplot=False
#python ../ztautau/scripts/merge.py --var="pileup" --reg="SR_80med_Tau1Track" --lab="TEST REGION" --icut="6" --input="/coepp/cephfs/mel/laram1/ztautau/HIST_1311_taupt85" --output="./" --makeplot=False
#python ../ztautau/scripts/merge.py --var="pileup" --reg="SR_80L1TAU60med_Tau1Track" --lab="TEST REGION" --icut="6" --input="/coepp/cephfs/mel/laram1/ztautau/HIST_1311_taupt85" --output="./" --makeplot=False
#python ../ztautau/scripts/merge.py --var="pileup" --reg="SR_125med_Tau1Track" --lab="TEST REGION" --icut="6" --input="/coepp/cephfs/mel/laram1/ztautau/HIST_1711_taupt130" --output="./" --makeplot=False
#python ../ztautau/scripts/merge.py --var="pileup" --reg="SR_160med_Tau1Track" --lab="TEST REGION" --icut="6" --input="/coepp/cephfs/mel/laram1/ztautau/HIST_1711_taupt165" --output="./" --makeplot=False

#python ../ztautau/scripts/merge.py --var="pileup" --reg="SR_L1TAU12IMmed_Tau1Track" --lab="TEST REGION" --icut="6" --input="/coepp/cephfs/mel/laram1/ztautau/HIST_0501_v26_taupt_30" --output="./" --makeplot=False
#python ../ztautau/scripts/merge.py --var="pileup" --reg="SR_tracktwo_Tau1Track" --lab="TEST REGION" --icut="6" --input="/coepp/cephfs/mel/laram1/ztautau/HIST_0501_v26_taupt_30" --output="./" --makeplot=False
#python ../ztautau/scripts/merge.py --var="pileup" --reg="SR_ptonly_Tau1Track" --lab="TEST REGION" --icut="6" --input="/coepp/cephfs/mel/laram1/ztautau/HIST_0501_v26_taupt_30" --output="./" --makeplot=False

#     THREE PRONG  

#python ../ztautau/scripts/merge.py --var="pileup" --reg="SR_Tau3Track" --lab="TEST" --icut="5" --input="/coepp/cephfs/mel/laram1/ztautau/HIST_0501_v26_taupt_30" --output="./Hists_systematics/BDT_medium/" --makeplot=False
#python ../ztautau/scripts/merge.py --var="pileup" --reg="SR_25med_Tau3Track" --lab="TEST REGION" --icut="6" --input="/coepp/cephfs/mel/laram1/ztautau/HIST_0501_v26_taupt_30" --output="./Hists_systematics/BDT_medium/" --makeplot=False
#python ../ztautau/scripts/merge.py --var="pileup" --reg="SR_35med_Tau3Track" --lab="TEST REGION" --icut="6" --input="/coepp/cephfs/mel/laram1/ztautau/HIST_1311_taupt40" --output="./" --makeplot=False
#python ../ztautau/scripts/merge.py --var="pileup" --reg="SR_50L1TAU12med_Tau3Track" --lab="TEST REGION" --icut="6" --input="/coepp/cephfs/mel/laram1/ztautau/HIST_1311_taupt55" --output="./" --makeplot=False
#python ../ztautau/scripts/merge.py --var="pileup" --reg="SR_80med_Tau3Track" --lab="TEST REGION" --icut="6" --input="/coepp/cephfs/mel/laram1/ztautau/HIST_1311_taupt85" --output="./" --makeplot=False
#python ../ztautau/scripts/merge.py --var="pileup" --reg="SR_80L1TAU60med_Tau3Track" --lab="TEST REGION" --icut="6" --input="/coepp/cephfs/mel/laram1/ztautau/HIST_1311_taupt85" --output="./" --makeplot=False
#python ../ztautau/scripts/merge.py --var="pileup" --reg="SR_125med_Tau3Track" --lab="TEST REGION" --icut="6" --input="/coepp/cephfs/mel/laram1/ztautau/HIST_1711_taupt130" --output="./" --makeplot=False
#python ../ztautau/scripts/merge.py --var="pileup" --reg="SR_160med_Tau3Track" --lab="TEST REGION" --icut="6" --input="/coepp/cephfs/mel/laram1/ztautau/HIST_1711_taupt165" --output="./" --makeplot=False
#
#python ../ztautau/scripts/merge.py --var="pileup" --reg="SR_L1TAU12IMmed_Tau3Track" --lab="TEST REGION" --icut="6" --input="/coepp/cephfs/mel/laram1/ztautau/HIST_0501_v26_taupt_30" --output="./" --makeplot=False
#python ../ztautau/scripts/merge.py --var="pileup" --reg="SR_tracktwo_Tau3Track" --lab="TEST REGION" --icut="6" --input="/coepp/cephfs/mel/laram1/ztautau/HIST_0501_v26_taupt_30" --output="./" --makeplot=False
#python ../ztautau/scripts/merge.py --var="pileup" --reg="SR_ptonly_Tau3Track" --lab="TEST REGION" --icut="6" --input="/coepp/cephfs/mel/laram1/ztautau/HIST_0501_v26_taupt_30" --output="./" --makeplot=False
#
#
#-----------------#
#   SYSTEMATICS
#-----------------#

#for b in {625..775..50}
#do 
#	python ../ztautau/scripts/merge.py --kwsys="$b" --var="tau_pt" --reg="SR_50L1TAU12med_Tau1Track" --lab="TEST" --icut="6" --input="/coepp/cephfs/mel/laram1/ztautau/RQCD_Hists/HIST_0511_KW" --output="./" --makeplot=True
#done
#for b in {625..775..50}
#do 
#	python ../ztautau/scripts/merge.py --kwsys="$b" --var="tau_pt" --reg="SR_50L1TAU12med_Tau3Track" --lab="TEST" --icut="6" --input="/coepp/cephfs/mel/laram1/ztautau/RQCD_Hists/HIST_0511_KW" --output="./" --makeplot=True
#done
#
#for b in {625..775..50}
#do 
#	python ../ztautau/scripts/merge.py --kwsys="$b" --var="tau_pt" --reg="SR_80med_Tau1Track" --lab="TEST" --icut="6" --input="/coepp/cephfs/mel/laram1/ztautau/RQCD_Hists/HIST_0511_KW" --output="./" --makeplot=True
#done
#for b in {625..775..50}
#do 
#	python ../ztautau/scripts/merge.py --kwsys="$b" --var="tau_pt" --reg="SR_80med_Tau3Track" --lab="TEST" --icut="6" --input="/coepp/cephfs/mel/laram1/ztautau/RQCD_Hists/HIST_0511_KW" --output="./" --makeplot=True
#done
#for b in {625..775..50}
#do 
#	python ../ztautau/scripts/merge.py --kwsys="$b" --var="tau_pt" --reg="SR_80L1TAU60med_Tau1Track" --lab="TEST" --icut="6" --input="/coepp/cephfs/mel/laram1/ztautau/RQCD_Hists/HIST_0511_KW" --output="./" --makeplot=True
#done
#for b in {625..775..50}
#do 
#	python ../ztautau/scripts/merge.py --kwsys="$b" --var="tau_pt" --reg="SR_125med_Tau3Track" --lab="TEST" --icut="6" --input="/coepp/cephfs/mel/laram1/ztautau/RQCD_Hists/HIST_0511_KW" --output="./" --makeplot=True
#done
##
#for b in {625..775..50}
#do 
#	python ../ztautau/scripts/merge.py --kwsys="$b" --var="tau_pt" --reg="SR_125med_Tau1Track" --lab="TEST" --icut="6" --input="/coepp/cephfs/mel/laram1/ztautau/RQCD_Hists/HIST_0511_KW" --output="./" --makeplot=True
#done
#for b in {625..775..50}
#do 
#	python ../ztautau/scripts/merge.py --kwsys="$b" --var="tau_pt" --reg="SR_160med_Tau3Track" --lab="TEST" --icut="6" --input="/coepp/cephfs/mel/laram1/ztautau/RQCD_Hists/HIST_0511_KW" --output="./" --makeplot=True
#done
##
#for b in {625..775..50}
#do 
#	python ../ztautau/scripts/merge.py --kwsys="$b" --var="tau_pt" --reg="SR_160med_Tau1Track" --lab="TEST" --icut="6" --input="/coepp/cephfs/mel/laram1/ztautau/RQCD_Hists/HIST_0511_KW" --output="./" --makeplot=True
#done
#for b in {625..1075..50}
##do 
##	python ../ztautau/scripts/merge.py --kwsys="$b" --var="tau_pt" --reg="SR" --lab="TEST" --icut="4" --input="/coepp/cephfs/mel/laram1/ztautau/RQCD_Hists/HIST_0511_KW" --output="./" --makeplot=True
#done

#for n in {10..40..1} 
#do
#	python ../ztautau/scripts/merge.py --toposys="$n" --var="tau_pt" --reg="SR" --lab="TEST" --icut="4" --input="/coepp/cephfs/mel/laram1/ztautau/RQCD_Hists/HIST_0511_KW" --output="./" --makeplot=True
#done

#
#for b in {10..30..1}
#do 
#	python ../ztautau/scripts/merge.py --toposys="$b" --var="tau_pt" --reg="SR_ptonly_Tau1Track" --lab="TEST" --icut="6" --input="/coepp/cephfs/mel/laram1/ztautau/HIST_1411_RQCD_chains" --output="./" --makeplot=True
#done

#for n in {10..30..1}
#do 
#	python ../ztautau/scripts/merge.py --toposys="$n" --var="tau_pt" --reg="SR_ptonly_Tau3Track" --lab="TEST" --icut="6" --input="/coepp/cephfs/mel/laram1/ztautau/HIST_1411_RQCD_chains" --output="./" --makeplot=True
#done

#for b in {10..30..1}
#do 
#	python ../ztautau/scripts/merge.py --toposys="$b" --var="tau_pt" --reg="SR_tracktwo_Tau1Track" --lab="TEST" --icut="6" --input="/coepp/cephfs/mel/laram1/ztautau/HIST_1411_RQCD_chains" --output="./" --makeplot=True
#done

#for n in {10..30..1}
#do 
#	python ../ztautau/scripts/merge.py --toposys="$n" --var="tau_pt" --reg="SR_tracktwo_Tau3Track" --lab="TEST" --icut="6" --input="/coepp/cephfs/mel/laram1/ztautau/HIST_1411_RQCD_chains" --output="./" --makeplot=True
#done

#for b in {10..30..1}
#do 
#	python ../ztautau/scripts/merge.py --toposys="$b" --var="tau_pt" --reg="SR_L1TAU12IMmed_Tau1Track" --lab="TEST" --icut="6" --input="/coepp/cephfs/mel/laram1/ztautau/HIST_1411_RQCD_chains" --output="./" --makeplot=True
#done

#for n in {10..30..1}
#do 
#	python ../ztautau/scripts/merge.py --toposys="$n" --var="tau_pt" --reg="SR_L1TAU12IMmed_Tau3Track" --lab="TEST" --icut="6" --input="/coepp/cephfs/mel/laram1/ztautau/HIST_1411_RQCD_chains" --output="./" --makeplot=True
#done

#for n in {10..15..1}
#do 
#	python ../ztautau/scripts/merge.py --sysptvar="$n" --var="tau_pt" --reg="SR_160med_Tau3Track" --lab="TEST" --icut="6" --input="/coepp/cephfs/mel/laram1/ztautau/HIST_1011_RQCD_ptvar" --output="./" --makeplot=True
#
#done

#for b in {10..30..1}
#do 
#	python ../ztautau/scripts/merge.py --toposys="$b" --var="tau_pt" --reg="SR" --lab="TEST" --icut="4" --input="/coepp/cephfs/mel/laram1/ztautau/HIST_0911_RQCD_25_test" --output="./" --makeplot=True
#done

#for n in {10..30..1}
#do
#	python ../ztautau/scripts/merge.py --toposys="$n" --var="tau_pt" --reg="SR_25med" --lab="TEST" --icut="5" --input="/coepp/cephfs/mel/laram1/ztautau/HIST_0911_RQCD_25_test" --output="./" --makeplot=True
#done

#for b in {10..40..1}
#do 
#	python ../ztautau/scripts/merge.py --toposys="$b" --var="tau_pt" --reg="SR_35med_Tau1Track" --lab="TEST" --icut="6" --input="/coepp/cephfs/mel/laram1/ztautau/HIST_2610_RQCD_35" --output="./" --makeplot=True
#done

#for n in {10..40..1}
#do
#	python ../ztautau/scripts/merge.py --toposys="$n" --var="tau_pt" --reg="SR_35med_Tau3Track" --lab="TEST" --icut="6" --input="/coepp/cephfs/mel/laram1/ztautau/HIST_2610_RQCD_35" --output="./" --makeplot=True
#done

#for n in {10..40..1} 
#do
#	python ../ztautau/scripts/merge.py --sysptvar="$n" --var="tau_pt" --reg="SR_Tau3Track" --lab="TEST" --icut="5" --input="/coepp/cephfs/mel/laram1/ztautau/HIST_2610_RQCD_35" --output="./" --makeplot=True
#done

#for n in {27..40..1} 
#do
#	python ../ztautau/scripts/merge.py --toposys="$n" --var="tau_pt" --reg="SR_35med" --lab="TEST" --icut="5" --input="/coepp/cephfs/mel/laram1/ztautau/HIST_2610_RQCD_35" --output="./" --makeplot=True
#done


#for m in {27..40..1}
#do 
#	python ../ztautau/scripts/merge.py --toposys="$m" --var="tau_pt" --reg="SR_35med" --lab="TEST" --icut="5" --input="/coepp/cephfs/mel/laram1/ztautau/HIST_2610_RQCD_35" --output="./" --makeplot=True
#done

#for m in {10..40..1}
#do 
#	python ../ztautau/scripts/merge.py --sysptvar="$m" --var="tau_pt" --reg="SR" --lab="TEST" --icut="4" --input="/coepp/cephfs/mel/laram1/ztautau/HIST_2610_RQCD_25" --output="./" --makeplot=True
#done

#for s in {625..1075..50}
#do
#	python ../ztautau/scripts/merge.py --kwsys="$s" --var="tau_pt" --reg="SR" --lab="SR" --icut="4" --input="/coepp/cephfs/mel/laram1/ztautau/HIST_0909_kw_sys_take3" --output="./" --makeplot=False
#done


###### BDT LOOSE ####


#---------------------------#
#   EFFICIENCIES v22 TAU PT
#---------------------------#

#     ONE PRONG  
#python ../ztautau/scripts/merge.py --var="tau_pt" --reg="SR_Tau1Track" --lab="TEST" --icut="5" --input="/coepp/cephfs/mel/laram1/ztautau/HIST_0501_loose_v26" --output="./Hists_systematics/BDT_loose/" --makeplot=False
#python ../ztautau/scripts/merge.py --var="tau_pt" --reg="SR_25med_Tau1Track" --lab="TEST REGION" --icut="6" --input="/coepp/cephfs/mel/laram1/ztautau/HIST_0501_loose_v26" --output="./Hists_systematics/BDT_loose/" --makeplot=False
#python ../ztautau/scripts/merge.py --var="tau_pt" --reg="SR_35med_Tau1Track" --lab="TEST REGION" --icut="6" --input="/coepp/cephfs/mel/laram1/ztautau/HIST_0501_loose_v26" --output="./Hists_systematics/BDT_loose/" --makeplot=False
#python ../ztautau/scripts/merge.py --var="tau_pt" --reg="SR_50L1TAU12med_Tau1Track" --lab="TEST REGION" --icut="6" --input="/coepp/cephfs/mel/laram1/ztautau/HIST_0501_loose_v26" --output="./Hists_systematics/BDT_loose/" --makeplot=False
#python ../ztautau/scripts/merge.py --var="tau_pt" --reg="SR_80med_Tau1Track" --lab="TEST REGION" --icut="6" --input="/coepp/cephfs/mel/laram1/ztautau/HIST_0501_loose_v26" --output="./Hists_systematics/BDT_loose/" --makeplot=False
#python ../ztautau/scripts/merge.py --var="tau_pt" --reg="SR_80L1TAU60med_Tau1Track" --lab="TEST REGION" --icut="6" --input="/coepp/cephfs/mel/laram1/ztautau/HIST_0501_loose_v26" --output="./Hists_systematics/BDT_loose/" --makeplot=False
#python ../ztautau/scripts/merge.py --var="tau_pt" --reg="SR_125med_Tau1Track" --lab="TEST REGION" --icut="6" --input="/coepp/cephfs/mel/laram1/ztautau/HIST_0501_loose_v26" --output="./Hists_systematics/BDT_loose/" --makeplot=False
#python ../ztautau/scripts/merge.py --var="tau_pt" --reg="SR_160med_Tau1Track" --lab="TEST REGION" --icut="6" --input="/coepp/cephfs/mel/laram1/ztautau/HIST_0501_loose_v26" --output="./Hists_systematics/BDT_loose/" --makeplot=False
#
#python ../ztautau/scripts/merge.py --var="tau_pt" --reg="SR_L1TAU12IMmed_Tau1Track" --lab="TEST REGION" --icut="6" --input="/coepp/cephfs/mel/laram1/ztautau/HIST_0501_loose_v26" --output="./Hists_systematics/BDT_loose/" --makeplot=False
#python ../ztautau/scripts/merge.py --var="tau_pt" --reg="SR_tracktwo_Tau1Track" --lab="TEST REGION" --icut="6" --input="/coepp/cephfs/mel/laram1/ztautau/HIST_0501_loose_v26" --output="./Hists_systematics/BDT_loose/" --makeplot=False
#python ../ztautau/scripts/merge.py --var="tau_pt" --reg="SR_ptonly_Tau1Track" --lab="TEST REGION" --icut="6" --input="/coepp/cephfs/mel/laram1/ztautau/HIST_0501_loose_v26" --output="./Hists_systematics/BDT_loose/" --makeplot=False

#     THREE PRONG  

#python ../ztautau/scripts/merge.py --var="tau_pt" --reg="SR_Tau3Track" --lab="TEST" --icut="5" --input="/coepp/cephfs/mel/laram1/ztautau/HIST_0501_loose_v26" --output="./Hists_systematics/BDT_loose/" --makeplot=False
#python ../ztautau/scripts/merge.py --var="tau_pt" --reg="SR_25med_Tau3Track" --lab="TEST REGION" --icut="6" --input="/coepp/cephfs/mel/laram1/ztautau/HIST_0501_loose_v26" --output="./Hists_systematics/BDT_loose/" --makeplot=False
#python ../ztautau/scripts/merge.py --var="tau_pt" --reg="SR_35med_Tau3Track" --lab="TEST REGION" --icut="6" --input="/coepp/cephfs/mel/laram1/ztautau/HIST_0501_loose_v26" --output="./Hists_systematics/BDT_loose/" --makeplot=False
#python ../ztautau/scripts/merge.py --var="tau_pt" --reg="SR_50L1TAU12med_Tau3Track" --lab="TEST REGION" --icut="6" --input="/coepp/cephfs/mel/laram1/ztautau/HIST_0501_loose_v26" --output="./Hists_systematics/BDT_loose/" --makeplot=False
#python ../ztautau/scripts/merge.py --var="tau_pt" --reg="SR_80med_Tau3Track" --lab="TEST REGION" --icut="6" --input="/coepp/cephfs/mel/laram1/ztautau/HIST_0501_loose_v26" --output="./Hists_systematics/BDT_loose/" --makeplot=False
#python ../ztautau/scripts/merge.py --var="tau_pt" --reg="SR_80L1TAU60med_Tau3Track" --lab="TEST REGION" --icut="6" --input="/coepp/cephfs/mel/laram1/ztautau/HIST_0501_loose_v26" --output="./Hists_systematics/BDT_loose/" --makeplot=False
#python ../ztautau/scripts/merge.py --var="tau_pt" --reg="SR_125med_Tau3Track" --lab="TEST REGION" --icut="6" --input="/coepp/cephfs/mel/laram1/ztautau/HIST_0501_loose_v26" --output="./Hists_systematics/BDT_loose/" --makeplot=False
#python ../ztautau/scripts/merge.py --var="tau_pt" --reg="SR_160med_Tau3Track" --lab="TEST REGION" --icut="6" --input="/coepp/cephfs/mel/laram1/ztautau/HIST_0501_loose_v26" --output="./Hists_systematics/BDT_loose/" --makeplot=False
#python ../ztautau/scripts/merge.py --var="tau_pt" --reg="SR_L1TAU12IMmed_Tau3Track" --lab="TEST REGION" --icut="6" --input="/coepp/cephfs/mel/laram1/ztautau/HIST_0501_loose_v26" --output="./Hists_systematics/BDT_loose/" --makeplot=False

#python ../ztautau/scripts/merge.py --var="tau_pt" --reg="SR_tracktwo_Tau3Track" --lab="TEST REGION" --icut="6" --input="/coepp/cephfs/mel/laram1/ztautau/HIST_0501_loose_v26" --output="./Hists_systematics/BDT_loose/" --makeplot=False
#python ../ztautau/scripts/merge.py --var="tau_pt" --reg="SR_ptonly_Tau3Track" --lab="TEST REGION" --icut="6" --input="/coepp/cephfs/mel/laram1/ztautau/HIST_0501_loose_v26" --output="./Hists_systematics/BDT_loose/" --makeplot=False


###### BDT TIGHT ####


#---------------------------#
#   EFFICIENCIES v22 TAU PT
#---------------------------#

##     ONE PRONG  
#python ../ztautau/scripts/merge.py --var="tau_pt" --reg="SR_Tau1Track" --lab="TEST" --icut="5" --input="/coepp/cephfs/mel/laram1/ztautau/HIST_0501_tight_v26" --output="./Hists_systematics/BDT_tight/" --makeplot=False
#python ../ztautau/scripts/merge.py --var="tau_pt" --reg="SR_25med_Tau1Track" --lab="TEST REGION" --icut="6" --input="/coepp/cephfs/mel/laram1/ztautau/HIST_0501_tight_v26" --output="./Hists_systematics/BDT_tight/" --makeplot=False
#python ../ztautau/scripts/merge.py --var="tau_pt" --reg="SR_Tau1Track" --lab="TEST" --icut="5" --input="/coepp/cephfs/mel/laram1/ztautau/HIST_0501_tight_v26" --output="./Hists_systematics/BDT_tight/" --makeplot=False
#python ../ztautau/scripts/merge.py --var="tau_pt" --reg="SR_25med_Tau1Track" --lab="TEST REGION" --icut="6" --input="/coepp/cephfs/mel/laram1/ztautau/HIST_0501_tight_v26" --output="./Hists_systematics/BDT_tight/" --makeplot=False
#python ../ztautau/scripts/merge.py --var="tau_pt" --reg="SR_35med_Tau1Track" --lab="TEST REGION" --icut="6" --input="/coepp/cephfs/mel/laram1/ztautau/HIST_0501_tight_v26" --output="./Hists_systematics/BDT_tight/" --makeplot=False
#python ../ztautau/scripts/merge.py --var="tau_pt" --reg="SR_50L1TAU12med_Tau1Track" --lab="TEST REGION" --icut="6" --input="/coepp/cephfs/mel/laram1/ztautau/HIST_0501_tight_v26" --output="./Hists_systematics/BDT_tight/" --makeplot=False
#python ../ztautau/scripts/merge.py --var="tau_pt" --reg="SR_80med_Tau1Track" --lab="TEST REGION" --icut="6" --input="/coepp/cephfs/mel/laram1/ztautau/HIST_0501_tight_v26" --output="./Hists_systematics/BDT_tight/" --makeplot=False
#python ../ztautau/scripts/merge.py --var="tau_pt" --reg="SR_80L1TAU60med_Tau1Track" --lab="TEST REGION" --icut="6" --input="/coepp/cephfs/mel/laram1/ztautau/HIST_0501_tight_v26" --output="./Hists_systematics/BDT_tight/" --makeplot=False
#python ../ztautau/scripts/merge.py --var="tau_pt" --reg="SR_125med_Tau1Track" --lab="TEST REGION" --icut="6" --input="/coepp/cephfs/mel/laram1/ztautau/HIST_0501_tight_v26" --output="./Hists_systematics/BDT_tight/" --makeplot=False
#python ../ztautau/scripts/merge.py --var="tau_pt" --reg="SR_160med_Tau1Track" --lab="TEST REGION" --icut="6" --input="/coepp/cephfs/mel/laram1/ztautau/HIST_0501_tight_v26" --output="./Hists_systematics/BDT_tight/" --makeplot=False

#python ../ztautau/scripts/merge.py --var="tau_pt" --reg="SR_L1TAU12IMmed_Tau1Track" --lab="TEST REGION" --icut="6" --input="/coepp/cephfs/mel/laram1/ztautau/HIST_1001_mu_pt_split_chains_TIGHT" --output="./Hists_systematics/BDT_tight/" --makeplot=False
#python ../ztautau/scripts/merge.py --var="tau_pt" --reg="SR_tracktwo_Tau1Track" --lab="TEST REGION" --icut="6" --input="/coepp/cephfs/mel/laram1/ztautau/HIST_1001_mu_pt_split_chains_TIGHT" --output="./Hists_systematics/BDT_tight/" --makeplot=False
#python ../ztautau/scripts/merge.py --var="tau_pt" --reg="SR_ptonly_Tau1Track" --lab="TEST REGION" --icut="6" --input="/coepp/cephfs/mel/laram1/ztautau/HIST_1001_mu_pt_split_chains_TIGHT" --output="./Hists_systematics/BDT_tight/" --makeplot=False

##     THREE PRONG  
#
#python ../ztautau/scripts/merge.py --var="tau_pt" --reg="SR_Tau3Track" --lab="TEST" --icut="5" --input="/coepp/cephfs/mel/laram1/ztautau/HIST_0501_tight_v26" --output="./Hists_systematics/BDT_tight/" --makeplot=True
#python ../ztautau/scripts/merge.py --var="tau_pt" --reg="SR_25med_Tau3Track" --lab="TEST REGION" --icut="6" --input="/coepp/cephfs/mel/laram1/ztautau/HIST_0501_tight_v26" --output="./Hists_systematics/BDT_tight/" --makeplot=True
#python ../ztautau/scripts/merge.py --var="tau_pt" --reg="SR_Tau3Track" --lab="TEST" --icut="5" --input="/coepp/cephfs/mel/laram1/ztautau/HIST_0501_tight_v26" --output="./Hists_systematics/BDT_tight/" --makeplot=False
#python ../ztautau/scripts/merge.py --var="tau_pt" --reg="SR_25med_Tau3Track" --lab="TEST REGION" --icut="6" --input="/coepp/cephfs/mel/laram1/ztautau/HIST_0501_tight_v26" --output="./Hists_systematics/BDT_tight/" --makeplot=False
#python ../ztautau/scripts/merge.py --var="tau_pt" --reg="SR_Tau3Track" --lab="TEST" --icut="5" --input="/coepp/cephfs/mel/laram1/ztautau/HIST_0501_tight_v26" --output="./Hists_systematics/BDT_tight/" --makeplot=False
#python ../ztautau/scripts/merge.py --var="tau_pt" --reg="SR_25med_Tau3Track" --lab="TEST REGION" --icut="6" --input="/coepp/cephfs/mel/laram1/ztautau/HIST_0501_tight_v26" --output="./Hists_systematics/BDT_tight/" --makeplot=False
#python ../ztautau/scripts/merge.py --var="tau_pt" --reg="SR_35med_Tau3Track" --lab="TEST REGION" --icut="6" --input="/coepp/cephfs/mel/laram1/ztautau/HIST_0501_tight_v26" --output="./Hists_systematics/BDT_tight/" --makeplot=False
#python ../ztautau/scripts/merge.py --var="tau_pt" --reg="SR_50L1TAU12med_Tau3Track" --lab="TEST REGION" --icut="6" --input="/coepp/cephfs/mel/laram1/ztautau/HIST_0501_tight_v26" --output="./Hists_systematics/BDT_tight/" --makeplot=False
#python ../ztautau/scripts/merge.py --var="tau_pt" --reg="SR_80med_Tau3Track" --lab="TEST REGION" --icut="6" --input="/coepp/cephfs/mel/laram1/ztautau/HIST_0501_tight_v26" --output="./Hists_systematics/BDT_tight/" --makeplot=False
#python ../ztautau/scripts/merge.py --var="tau_pt" --reg="SR_80L1TAU60med_Tau3Track" --lab="TEST REGION" --icut="6" --input="/coepp/cephfs/mel/laram1/ztautau/HIST_0501_tight_v26" --output="./Hists_systematics/BDT_tight/" --makeplot=False
#python ../ztautau/scripts/merge.py --var="tau_pt" --reg="SR_125med_Tau3Track" --lab="TEST REGION" --icut="6" --input="/coepp/cephfs/mel/laram1/ztautau/HIST_0501_tight_v26" --output="./Hists_systematics/BDT_tight/" --makeplot=False
#python ../ztautau/scripts/merge.py --var="tau_pt" --reg="SR_160med_Tau3Track" --lab="TEST REGION" --icut="6" --input="/coepp/cephfs/mel/laram1/ztautau/HIST_0501_tight_v26" --output="./Hists_systematics/BDT_tight/" --makeplot=False
#python ../ztautau/scripts/merge.py --var="tau_pt" --reg="SR_L1TAU12IMmed_Tau3Track" --lab="TEST REGION" --icut="6" --input="/coepp/cephfs/mel/laram1/ztautau/HIST_1001_mu_pt_split_chains_TIGHT" --output="./Hists_systematics/BDT_tight/" --makeplot=False
#
#python ../ztautau/scripts/merge.py --var="tau_pt" --reg="SR_tracktwo_Tau3Track" --lab="TEST REGION" --icut="6" --input="/coepp/cephfs/mel/laram1/ztautau/HIST_1001_mu_pt_split_chains_TIGHT" --output="./Hists_systematics/BDT_tight/" --makeplot=False
#python ../ztautau/scripts/merge.py --var="tau_pt" --reg="SR_ptonly_Tau3Track" --lab="TEST REGION" --icut="6" --input="/coepp/cephfs/mel/laram1/ztautau/HIST_1001_mu_pt_split_chains_TIGHT" --output="./Hists_systematics/BDT_tight/" --makeplot=False

###### BDT LOOSE 2015 ####


#---------------------------#
#   EFFICIENCIES v22 TAU PT
#---------------------------#

#     ONE PRONG  
#python ../ztautau/scripts/merge.py --var="tau_pt" --reg="SR_Tau1Track" --lab="TEST" --icut="5" --input="/coepp/cephfs/mel/laram1/ztautau/HIST_0101_v26_loose_tau25" --output="./Hists_systematics/2015/BDT_loose/" --makeplot=False
#python ../ztautau/scripts/merge.py --var="tau_pt" --reg="SR_25med_Tau1Track" --lab="TEST REGION" --icut="6" --input="/coepp/cephfs/mel/laram1/ztautau/HIST_0101_v26_loose_tau25" --output="./Hists_systematics/2015/BDT_loose/" --makeplot=False
#python ../ztautau/scripts/merge.py --var="tau_pt" --reg="SR_35med_Tau1Track" --lab="TEST REGION" --icut="6" --input="/coepp/cephfs/mel/laram1/ztautau/HIST_1201_LOOSE" --output="./Hists_systematics/2015/BDT_loose/" --makeplot=False
#python ../ztautau/scripts/merge.py --var="tau_pt" --reg="SR_50L1TAU12med_Tau1Track" --lab="TEST REGION" --icut="6" --input="/coepp/cephfs/mel/laram1/ztautau/HIST_1201_LOOSE" --output="./Hists_systematics/2015/BDT_loose/" --makeplot=False
#python ../ztautau/scripts/merge.py --var="tau_pt" --reg="SR_80med_Tau1Track" --lab="TEST REGION" --icut="6" --input="/coepp/cephfs/mel/laram1/ztautau/HIST_1201_LOOSE" --output="./Hists_systematics/2015/BDT_loose/" --makeplot=False
#python ../ztautau/scripts/merge.py --var="tau_pt" --reg="SR_80L1TAU60med_Tau1Track" --lab="TEST REGION" --icut="6" --input="/coepp/cephfs/mel/laram1/ztautau/HIST_1201_LOOSE" --output="./Hists_systematics/2015/BDT_loose/" --makeplot=False
#python ../ztautau/scripts/merge.py --var="tau_pt" --reg="SR_125med_Tau1Track" --lab="TEST REGION" --icut="6" --input="/coepp/cephfs/mel/laram1/ztautau/HIST_1201_LOOSE" --output="./Hists_systematics/2015/BDT_loose/" --makeplot=False
#python ../ztautau/scripts/merge.py --var="tau_pt" --reg="SR_160med_Tau1Track" --lab="TEST REGION" --icut="6" --input="/coepp/cephfs/mel/laram1/ztautau/HIST_1201_LOOSE" --output="./Hists_systematics/2015/BDT_loose/" --makeplot=False
##
#python ../ztautau/scripts/merge.py --var="tau_pt" --reg="SR_L1TAU12IMmed_Tau1Track" --lab="TEST REGION" --icut="6" --input="/coepp/cephfs/mel/laram1/ztautau/HIST_1201_LOOSE" --output="./Hists_systematics/2015/BDT_loose/" --makeplot=False
#python ../ztautau/scripts/merge.py --var="tau_pt" --reg="SR_tracktwo_Tau1Track" --lab="TEST REGION" --icut="6" --input="/coepp/cephfs/mel/laram1/ztautau/HIST_1201_LOOSE" --output="./Hists_systematics/2015/BDT_loose/" --makeplot=False
#python ../ztautau/scripts/merge.py --var="tau_pt" --reg="SR_ptonly_Tau1Track" --lab="TEST REGION" --icut="6" --input="/coepp/cephfs/mel/laram1/ztautau/HIST_1201_LOOSE" --output="./Hists_systematics/2015/BDT_loose/" --makeplot=False
#
#     THREE PRONG  

#python ../ztautau/scripts/merge.py --var="tau_pt" --reg="SR_Tau3Track" --lab="TEST" --icut="5" --input="/coepp/cephfs/mel/laram1/ztautau/HIST_0101_v26_loose_tau25" --output="./Hists_systematics/2015/BDT_loose/" --makeplot=False
#python ../ztautau/scripts/merge.py --var="tau_pt" --reg="SR_25med_Tau3Track" --lab="TEST REGION" --icut="6" --input="/coepp/cephfs/mel/laram1/ztautau/HIST_0101_v26_loose_tau25" --output="./Hists_systematics/2015/BDT_loose/" --makeplot=False
#python ../ztautau/scripts/merge.py --var="tau_pt" --reg="SR_35med_Tau3Track" --lab="TEST REGION" --icut="6" --input="/coepp/cephfs/mel/laram1/ztautau/HIST_1201_LOOSE" --output="./Hists_systematics/2015/BDT_loose/" --makeplot=False
#python ../ztautau/scripts/merge.py --var="tau_pt" --reg="SR_50L1TAU12med_Tau3Track" --lab="TEST REGION" --icut="6" --input="/coepp/cephfs/mel/laram1/ztautau/HIST_1201_LOOSE" --output="./Hists_systematics/2015/BDT_loose/" --makeplot=False
#python ../ztautau/scripts/merge.py --var="tau_pt" --reg="SR_80med_Tau3Track" --lab="TEST REGION" --icut="6" --input="/coepp/cephfs/mel/laram1/ztautau/HIST_1201_LOOSE" --output="./Hists_systematics/2015/BDT_loose/" --makeplot=False
#python ../ztautau/scripts/merge.py --var="tau_pt" --reg="SR_80L1TAU60med_Tau3Track" --lab="TEST REGION" --icut="6" --input="/coepp/cephfs/mel/laram1/ztautau/HIST_1201_LOOSE" --output="./Hists_systematics/2015/BDT_loose/" --makeplot=False
#python ../ztautau/scripts/merge.py --var="tau_pt" --reg="SR_125med_Tau3Track" --lab="TEST REGION" --icut="6" --input="/coepp/cephfs/mel/laram1/ztautau/HIST_1201_LOOSE" --output="./Hists_systematics/2015/BDT_loose/" --makeplot=False
#python ../ztautau/scripts/merge.py --var="tau_pt" --reg="SR_160med_Tau3Track" --lab="TEST REGION" --icut="6" --input="/coepp/cephfs/mel/laram1/ztautau/HIST_1201_LOOSE" --output="./Hists_systematics/2015/BDT_loose/" --makeplot=False
#python ../ztautau/scripts/merge.py --var="tau_pt" --reg="SR_L1TAU12IMmed_Tau3Track" --lab="TEST REGION" --icut="6" --input="/coepp/cephfs/mel/laram1/ztautau/HIST_1201_LOOSE" --output="./Hists_systematics/2015/BDT_loose/" --makeplot=False

#python ../ztautau/scripts/merge.py --var="tau_pt" --reg="SR_tracktwo_Tau3Track" --lab="TEST REGION" --icut="6" --input="/coepp/cephfs/mel/laram1/ztautau/HIST_1201_LOOSE" --output="./Hists_systematics/2015/BDT_loose/" --makeplot=False
#python ../ztautau/scripts/merge.py --var="tau_pt" --reg="SR_ptonly_Tau3Track" --lab="TEST REGION" --icut="6" --input="/coepp/cephfs/mel/laram1/ztautau/HIST_1201_LOOSE" --output="./Hists_systematics/2015/BDT_loose/" --makeplot=False


