#!bin/bash

#-------------------#
#	SR
#-------------------#

python ../ztautau/scripts/merge.py --var="tau_pt" --reg="SR" --lab="TEST REGION" --icut="4" --input="/coepp/cephfs/mel/laram1/ztautau/HIST_0910_v22" --output="./" --makeplot=False

#python ../ztautau/scripts/merge.py --var="tau_pt" --reg="SR_SS" --lab="TEST REGION" --icut="4" --input="/coepp/cephfs/mel/laram1/ztautau/HIST_0410_new_mt_regions" --output="./" --makeplot=False

#python ../ztautau/scripts/merge.py --var="tau_phi" --reg="SR" --lab="TEST REGION" --icut="4" --input="/coepp/cephfs/mel/laram1/ztautau/HIST_0410_new_mt_regions" --output="./" --makeplot=True
#python ../ztautau/scripts/merge.py --var="tau_eta" --reg="SR" --lab="TEST REGION" --icut="4" --input="/coepp/cephfs/mel/laram1/ztautau/HIST_0410_new_mt_regions" --output="./" --makeplot=True
#python ../ztautau/scripts/merge.py --var="jet_bdt_score" --reg="SR" --lab="TEST REGION" --icut="4" --input="/coepp/cephfs/mel/laram1/ztautau/HIST_0410_new_mt_regions" --output="./" --makeplot=True
#python ../ztautau/scripts/merge.py --var="tau_pt" --reg="SR" --lab="TEST REGION" --icut="4" --input="/coepp/cephfs/mel/laram1/ztautau/HIST_0410_new_mt_regions" --output="./" --makeplot=True
#python ../ztautau/scripts/merge.py --var="tau_pt" --reg="SR" --lab="TEST REGION" --icut="4" --input="/coepp/cephfs/mel/laram1/ztautau/HIST_0410_new_mt_regions" --output="./" --makeplot=True

#python ../ztautau/scripts/merge.py --var="tau_pt" --reg="SR" --lab="TEST REGION" --icut="4" --input="/coepp/cephfs/mel/laram1/ztautau/HIST_1809_Wjets_estimation_new" --output="./" --makeplot=True

#python ../ztautau/scripts/merge.py --var="tau_pt" --reg="SR_SS25med" --lab="TEST REGION" --icut="5" --input="/coepp/cephfs/mel/laram1/ztautau/HIST_0610_all_triggers" --output="./" --makeplot=False

python ../ztautau/scripts/merge.py --var="tau_pt" --reg="SR_25med" --lab="TEST REGION" --icut="5" --input="/coepp/cephfs/mel/laram1/ztautau/HIST_0910_v22" --output="./" --makeplot=True

#--------------------#
#      OTHERS
#--------------------#

#python ../ztautau/scripts/merge.py --var="m_trans" --reg="AntiIsoCR_OS" --lab="TEST REGION" --icut="3" --input="/coepp/cephfs/mel/laram1/ztautau/HIST_1809_Wjets_estimation_new" --output="./" --makeplot=True

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

#python ../ztautau/scripts/merge.py --var="vis_mass" --reg="SR_OS_no_cuts_forvismass" --lab="TEST REGION" --icut="3" --input="/coepp/cephfs/mel/laram1/ztautau/HIST_0610_regions_for_vismassplot" --output="./" --makeplot=True

#----------------------#
#	LOWCSDP
#----------------------#

#python ../ztautau/scripts/merge.py --var="m_trans" --reg="SR_highSCDP" --lab="TEST REGION" --icut="3" --input="/coepp/cephfs/mel/laram1/ztautau/HIST_0410_new_mt_regions" --output="./" --makeplot=True
#python ../ztautau/scripts/merge.py --var="m_trans" --reg="SR_lowSCDP" --lab="TEST REGION" --icut="3" --input="/coepp/cephfs/mel/laram1/ztautau/HIST_0410_new_mt_regions" --output="./" --makeplot=True
#python ../ztautau/scripts/merge.py --var="tau_pt" --reg="SR_lowSCDP_25med" --lab="TEST REGION" --icut="5" --input="/coepp/cephfs/mel/laram1/ztautau/HIST_0610_all_triggers" --output="./" --makeplot=False
#python ../ztautau/scripts/merge.py --var="tau_pt" --reg="SR_lowSCDP_SS25med" --lab="TEST REGION" --icut="5" --input="/coepp/cephfs/mel/laram1/ztautau/HIST_0610_all_triggers" --output="./" --makeplot=False

#python ../ztautau/scripts/merge.py --var="tau_pt" --reg="SR_lowSCDP" --lab="TEST REGION" --icut="4" --input="/coepp/cephfs/mel/laram1/ztautau/HIST_0510" --output="./" --makeplot=False
#python ../ztautau/scripts/merge.py --var="tau_pt" --reg="SR_SS_lowSCDP" --lab="TEST REGION" --icut="4" --input="/coepp/cephfs/mel/laram1/ztautau/HIST_0510" --output="./" --makeplot=False

#python ../ztautau/scripts/merge.py --var="tau_pt" --reg="SR_lowSCDP_lowMT" --lab="TEST REGION" --icut="4" --input="/coepp/cephfs/mel/laram1/ztautau/HIST_0410_new_mt_regions" --output="./" --makeplot=False
#python ../ztautau/scripts/merge.py --var="tau_pt" --reg="SR_lowSCDP_lowMT_SS" --lab="TEST REGION" --icut="4" --input="/coepp/cephfs/mel/laram1/ztautau/HIST_0410_new_mt_regions" --output="./" --makeplot=False

#python ../ztautau/scripts/merge.py --var="tau_pt" --reg="SR_lowSCDP_lowMT_Tau1Track" --lab="TEST REGION" --icut="5" --input="/coepp/cephfs/mel/laram1/ztautau/HIST_1809_Wjets_estimation_new" --output="./" --makeplot=True
#python ../ztautau/scripts/merge.py --var="tau_pt" --reg="SR_lowSCDP_lowMT_SS_Tau1Track" --lab="TEST REGION" --icut="5" --input="/coepp/cephfs/mel/laram1/ztautau/HIST_1809_Wjets_estimation_new" --output="./" --makeplot=True

#python ../ztautau/scripts/merge.py --var="tau_pt" --reg="SR_lowSCDP_lowMT_Tau3Track" --lab="TEST REGION" --icut="5" --input="/coepp/cephfs/mel/laram1/ztautau/HIST_1809_Wjets_estimation_new" --output="./" --makeplot=False
#python ../ztautau/scripts/merge.py --var="tau_pt" --reg="SR_lowSCDP_lowMT_SS_Tau3Track" --lab="TEST REGION" --icut="5" --input="/coepp/cephfs/mel/laram1/ztautau/HIST_1809_Wjets_estimation_new" --output="./" --makeplot=False
#
#----------------------#
#   EFFICIENCIES v19
#----------------------#

#     ONE PRONG  

#python ../ztautau/scripts/merge.py --var="tau_pt" --reg="SR" --lab="TEST" --icut="4" --input="/coepp/cephfs/mel/laram1/ztautau/HIST_0610_all_triggers" --output="./" --makeplot=True

#python ../ztautau/scripts/merge.py --var="tau_pt" --reg="SR_Tau1Track" --lab="TEST" --icut="5" --input="/coepp/cephfs/mel/laram1/ztautau/HIST_0610_all_triggers" --output="./" --makeplot=False
#python ../ztautau/scripts/merge.py --var="tau_pt" --reg="SR_25med_Tau1Track" --lab="TEST REGION" --icut="6" --input="/coepp/cephfs/mel/laram1/ztautau/HIST_0610_all_triggers" --output="./" --makeplot=False
#python ../ztautau/scripts/merge.py --var="tau_pt" --reg="SR_35med_Tau1Track" --lab="TEST REGION" --icut="6" --input="/coepp/cephfs/mel/laram1/ztautau/HIST_0610_all_triggers" --output="./" --makeplot=False
#python ../ztautau/scripts/merge.py --var="tau_pt" --reg="SR_50L1TAU12med_Tau1Track" --lab="TEST REGION" --icut="6" --input="/coepp/cephfs/mel/laram1/ztautau/HIST_0610_all_triggers" --output="./" --makeplot=False
#python ../ztautau/scripts/merge.py --var="tau_pt" --reg="SR_80med_Tau1Track" --lab="TEST REGION" --icut="6" --input="/coepp/cephfs/mel/laram1/ztautau/HIST_0610_all_triggers" --output="./" --makeplot=False
#python ../ztautau/scripts/merge.py --var="tau_pt" --reg="SR_80L1TAU60med_Tau1Track" --lab="TEST REGION" --icut="6" --input="/coepp/cephfs/mel/laram1/ztautau/HIST_0610_all_triggers" --output="./" --makeplot=False
#python ../ztautau/scripts/merge.py --var="tau_pt" --reg="SR_125med_Tau1Track" --lab="TEST REGION" --icut="6" --input="/coepp/cephfs/mel/laram1/ztautau/HIST_0610_all_triggers" --output="./" --makeplot=False
#python ../ztautau/scripts/merge.py --var="tau_pt" --reg="SR_160med_Tau1Track" --lab="TEST REGION" --icut="6" --input="/coepp/cephfs/mel/laram1/ztautau/HIST_0610_all_triggers" --output="./" --makeplot=False

#     THREE PRONG  

#python ../ztautau/scripts/merge.py --var="tau_pt" --reg="SR_Tau3Track" --lab="TEST" --icut="5" --input="/coepp/cephfs/mel/laram1/ztautau/HIST_0610_all_triggers" --output="./" --makeplot=False
#python ../ztautau/scripts/merge.py --var="tau_pt" --reg="SR_25med_Tau3Track" --lab="TEST REGION" --icut="6" --input="/coepp/cephfs/mel/laram1/ztautau/HIST_0610_all_triggers" --output="./" --makeplot=False
#python ../ztautau/scripts/merge.py --var="tau_pt" --reg="SR_35med_Tau3Track" --lab="TEST REGION" --icut="6" --input="/coepp/cephfs/mel/laram1/ztautau/HIST_0610_all_triggers" --output="./" --makeplot=False
#python ../ztautau/scripts/merge.py --var="tau_pt" --reg="SR_50L1TAU12med_Tau3Track" --lab="TEST REGION" --icut="6" --input="/coepp/cephfs/mel/laram1/ztautau/HIST_0610_all_triggers" --output="./" --makeplot=False
#python ../ztautau/scripts/merge.py --var="tau_pt" --reg="SR_80med_Tau3Track" --lab="TEST REGION" --icut="6" --input="/coepp/cephfs/mel/laram1/ztautau/HIST_0610_all_triggers" --output="./" --makeplot=False
#python ../ztautau/scripts/merge.py --var="tau_pt" --reg="SR_80L1TAU60med_Tau3Track" --lab="TEST REGION" --icut="6" --input="/coepp/cephfs/mel/laram1/ztautau/HIST_0610_all_triggers" --output="./" --makeplot=False
#python ../ztautau/scripts/merge.py --var="tau_pt" --reg="SR_125med_Tau3Track" --lab="TEST REGION" --icut="6" --input="/coepp/cephfs/mel/laram1/ztautau/HIST_0610_all_triggers" --output="./" --makeplot=False
#python ../ztautau/scripts/merge.py --var="tau_pt" --reg="SR_160med_Tau3Track" --lab="TEST REGION" --icut="6" --input="/coepp/cephfs/mel/laram1/ztautau/HIST_0610_all_triggers" --output="./" --makeplot=False
#
#----------------------#
#   EFFICIENCIES v22
#----------------------#

#     ONE PRONG  

#python ../ztautau/scripts/merge.py --var="tau_pt" --reg="SR" --lab="TEST" --icut="4" --input="/coepp/cephfs/mel/laram1/ztautau/HIST_0910_v22" --output="./" --makeplot=True

#python ../ztautau/scripts/merge.py --var="tau_pt" --reg="SR_Tau1Track" --lab="TEST" --icut="5" --input="/coepp/cephfs/mel/laram1/ztautau/HIST_0910_v22" --output="./" --makeplot=False
#python ../ztautau/scripts/merge.py --var="tau_pt" --reg="SR_25med_Tau1Track" --lab="TEST REGION" --icut="6" --input="/coepp/cephfs/mel/laram1/ztautau/HIST_0910_v22" --output="./" --makeplot=False
#python ../ztautau/scripts/merge.py --var="tau_pt" --reg="SR_35med_Tau1Track" --lab="TEST REGION" --icut="6" --input="/coepp/cephfs/mel/laram1/ztautau/HIST_0910_v22" --output="./" --makeplot=False
#python ../ztautau/scripts/merge.py --var="tau_pt" --reg="SR_50L1TAU12med_Tau1Track" --lab="TEST REGION" --icut="6" --input="/coepp/cephfs/mel/laram1/ztautau/HIST_0910_v22" --output="./" --makeplot=False
#python ../ztautau/scripts/merge.py --var="tau_pt" --reg="SR_80med_Tau1Track" --lab="TEST REGION" --icut="6" --input="/coepp/cephfs/mel/laram1/ztautau/HIST_0910_v22" --output="./" --makeplot=False
#python ../ztautau/scripts/merge.py --var="tau_pt" --reg="SR_80L1TAU60med_Tau1Track" --lab="TEST REGION" --icut="6" --input="/coepp/cephfs/mel/laram1/ztautau/HIST_0910_v22" --output="./" --makeplot=False
#python ../ztautau/scripts/merge.py --var="tau_pt" --reg="SR_125med_Tau1Track" --lab="TEST REGION" --icut="6" --input="/coepp/cephfs/mel/laram1/ztautau/HIST_0910_v22" --output="./" --makeplot=False
#python ../ztautau/scripts/merge.py --var="tau_pt" --reg="SR_160med_Tau1Track" --lab="TEST REGION" --icut="6" --input="/coepp/cephfs/mel/laram1/ztautau/HIST_0910_v22" --output="./" --makeplot=False

#     THREE PRONG  

#python ../ztautau/scripts/merge.py --var="tau_pt" --reg="SR_Tau3Track" --lab="TEST" --icut="5" --input="/coepp/cephfs/mel/laram1/ztautau/HIST_0910_v22" --output="./" --makeplot=False
#python ../ztautau/scripts/merge.py --var="tau_pt" --reg="SR_25med_Tau3Track" --lab="TEST REGION" --icut="6" --input="/coepp/cephfs/mel/laram1/ztautau/HIST_0910_v22" --output="./" --makeplot=False
#python ../ztautau/scripts/merge.py --var="tau_pt" --reg="SR_35med_Tau3Track" --lab="TEST REGION" --icut="6" --input="/coepp/cephfs/mel/laram1/ztautau/HIST_0910_v22" --output="./" --makeplot=False
#python ../ztautau/scripts/merge.py --var="tau_pt" --reg="SR_50L1TAU12med_Tau3Track" --lab="TEST REGION" --icut="6" --input="/coepp/cephfs/mel/laram1/ztautau/HIST_0910_v22" --output="./" --makeplot=False
#python ../ztautau/scripts/merge.py --var="tau_pt" --reg="SR_80med_Tau3Track" --lab="TEST REGION" --icut="6" --input="/coepp/cephfs/mel/laram1/ztautau/HIST_0910_v22" --output="./" --makeplot=False
#python ../ztautau/scripts/merge.py --var="tau_pt" --reg="SR_80L1TAU60med_Tau3Track" --lab="TEST REGION" --icut="6" --input="/coepp/cephfs/mel/laram1/ztautau/HIST_0910_v22" --output="./" --makeplot=False
#python ../ztautau/scripts/merge.py --var="tau_pt" --reg="SR_125med_Tau3Track" --lab="TEST REGION" --icut="6" --input="/coepp/cephfs/mel/laram1/ztautau/HIST_0910_v22" --output="./" --makeplot=False
#python ../ztautau/scripts/merge.py --var="tau_pt" --reg="SR_160med_Tau3Track" --lab="TEST REGION" --icut="6" --input="/coepp/cephfs/mel/laram1/ztautau/HIST_0910_v22" --output="./" --makeplot=False


#-----------------#
#   SYSTEMATICS
#-----------------#

#python ../ztautau/scripts/merge.py --var="tau_pt" --reg="SR" --lab="TEST REGION" --icut="4" --input="/coepp/cephfs/mel/laram1/ztautau/TEST_0209/TAUSF_SYS_DN" --output="./" --makeplot=False
#python ../ztautau/scripts/merge.py --var="tau_pt" --reg="SR_25med" --lab="TEST REGION" --icut="5" --input="/coepp/cephfs/mel/laram1/ztautau/TEST_0209/TAUSF_SYS_DN" --output="./" --makeplot=False

#for b in {10..40..1}
#do 
#	python ../ztautau/scripts/merge.py --toposys="$b" --var="tau_pt" --reg="SR_35med_Tau1Track" --lab="TEST" --icut="6" --input="/coepp/cephfs/mel/laram1/ztautau/HIST_0809_tauptcut35GeV_rqcdsys" --output="./" --makeplot=True
#done

#for n in {10..40..1} #NB NB NB 20 to 40
#do 
#	python ../ztautau/scripts/merge.py --toposys="$n" --var="tau_pt" --reg="SR_35med_Tau3Track" --lab="TEST" --icut="6" --input="/coepp/cephfs/mel/laram1/ztautau/HIST_0809_tauptcut35GeV_rqcdsys" --output="./" --makeplot=True
#done

#for m in {14..40..1}
#do 
#	python ../ztautau/scripts/merge.py --toposys="$m" --var="tau_pt" --reg="SR_35med" --lab="TEST" --icut="5" --input="/coepp/cephfs/mel/laram1/ztautau/HIST_0809_tauptcut35GeV_rqcdsys" --output="./" --makeplot=True
#done

#
#for b in {10..40..1}
#do 
#	python ../ztautau/scripts/merge.py --toposys="$b" --var="tau_pt" --reg="SR_Tau1Track" --lab="TEST" --icut="5" --input="/coepp/cephfs/mel/laram1/ztautau/HIST_0809_tauptcut35GeV_rqcdsys" --output="./" --makeplot=True
#done

#for n in {10..40..1}
#do 
#	python ../ztautau/scripts/merge.py --toposys="$n" --var="tau_pt" --reg="SR_Tau3Track" --lab="TEST" --icut="5" --input="/coepp/cephfs/mel/laram1/ztautau/HIST_0809_tauptcut35GeV_rqcdsys" --output="./" --makeplot=True
#done

#for m in {10..40..1}
#do 
#	python ../ztautau/scripts/merge.py --toposys="$m" --var="tau_pt" --reg="SR" --lab="TEST" --icut="4" --input="/coepp/cephfs/mel/laram1/ztautau/HIST_0809_tauptcut35GeV_rqcdsys" --output="./" --makeplot=True
#done

#for s in {625..1075..50}
#do
#	python ../ztautau/scripts/merge.py --kwsys="$s" --var="tau_pt" --reg="SR" --lab="SR" --icut="4" --input="/coepp/cephfs/mel/laram1/ztautau/HIST_0909_kw_sys_take3" --output="./" --makeplot=False
#done

#python ../ztautau/scripts/merge.py --var="tau_pt" --reg="SR_25med_Tau1Track" --lab="TEST REGION" --icut="6" --input="/coepp/cephfs/mel/laram1/ztautau/TEST_0209/MUID_UP" --output="./" --makeplot=True
#
#   TESTS
#python ../ztautau/scripts/merge.py --var="tau_pt" --reg="AntiIsoCR_OS" --lab="AntiIso" --icut="3" --input="/coepp/cephfs/mel/laram1/ztautau/TEST_0209" --output="./" --makeplot=True
#python ../ztautau/scripts/merge.py --var="tau_pt" --reg="AntiIsoCR_SS" --lab="AntiIso" --icut="3" --input="/coepp/cephfs/mel/laram1/ztautau/TEST_0209" --output="./" --makeplot=True

#python ../ztautau/scripts/merge.py --var="tau_pt" --reg="AntiIsoCR_OS_25med" --lab="AntiIso" --icut="4" --input="/coepp/cephfs/mel/laram1/ztautau/TEST_0209" --output="./" --makeplot=True
#python ../ztautau/scripts/merge.py --var="tau_pt" --reg="AntiIsoCR_SS_25med" --lab="AntiIso" --icut="4" --input="/coepp/cephfs/mel/laram1/ztautau/TEST_0209" --output="./" --makeplot=True


