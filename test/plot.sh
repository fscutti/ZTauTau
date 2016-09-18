#!bin/bash

# Strings are passed to the script but this is redundant!
#python ../ztautau/scripts/merge.py --var="tau_pt" --reg="SR_lowSCDP_lowMT_SS" --lab="TEST REGION" --icut="4" --input="/coepp/cephfs/mel/laram1/ztautau/HIST_1309_Wjets_estimation" --output="./" --makeplot=False
#python ../ztautau/scripts/merge.py --var="tau_pt" --reg="SR_SS" --lab="TEST REGION" --icut="4" --input="/coepp/cephfs/mel/laram1/ztautau/HIST_1309_Wjets_estimation" --output="./" --makeplot=False
#python ../ztautau/scripts/merge.py --var="tau_pt" --reg="SR" --lab="TEST REGION" --icut="4" --input="/coepp/cephfs/mel/laram1/ztautau/HIST_1309_Wjets_estimation" --output="./" --makeplot=False
#python ../ztautau/scripts/merge.py --var="sumcosdphi" --reg="SR" --lab="TEST REGION" --icut="4" --input="/coepp/cephfs/mel/laram1/ztautau/HIST_1309_Wjets_estimation" --output="./" --makeplot=True
#python ../ztautau/scripts/merge.py --var="tau_pt" --reg="SR_25med" --lab="TEST REGION" --icut="5" --input="/coepp/cephfs/mel/laram1/ztautau/HIST_1309_Wjets_estimation" --output="./" --makeplot=False
#python ../ztautau/scripts/merge.py --var="tau_pt" --reg="SR_35med" --lab="TEST REGION" --icut="5" --input="/coepp/cephfs/mel/laram1/ztautau/TEST_0209" --output="./" --makeplot=False
#python ../ztautau/scripts/merge.py --var="sumcosdphi" --reg="SR" --lab="TEST REGION" --icut="4" --input="/coepp/cephfs/mel/laram1/ztautau/HIST_1309_Wjets_estimation" --output="./" --makeplot=True

#     ONE PRONG  
#python ../ztautau/scripts/merge.py --var="tau_pt" --reg="SR_lowSCDP_lowMT_Tau1Track" --lab="TEST REGION" --icut="5" --input="/coepp/cephfs/mel/laram1/ztautau/HIST_1309_Wjets_estimation" --output="./" --makeplot=False
#python ../ztautau/scripts/merge.py --var="tau_pt" --reg="SR_lowSCDP_lowMT_SS_Tau1Track" --lab="TEST REGION" --icut="5" --input="/coepp/cephfs/mel/laram1/ztautau/HIST_1309_Wjets_estimation" --output="./" --makeplot=False
#python ../ztautau/scripts/merge.py --var="tau_pt" --reg="SR_Tau1Track" --lab="TEST" --icut="5" --input="/coepp/cephfs/mel/laram1/ztautau/HIST_1309_Wjets_estimation" --output="./" --makeplot=False
#python ../ztautau/scripts/merge.py --var="tau_pt" --reg="SR_SS_Tau1Track" --lab="TEST" --icut="5" --input="/coepp/cephfs/mel/laram1/ztautau/HIST_1309_Wjets_estimation" --output="./" --makeplot=False

#python ../ztautau/scripts/merge.py --var="tau_pt" --reg="SR_25med_Tau1Track" --lab="TEST REGION" --icut="6" --input="/coepp/cephfs/mel/laram1/ztautau/HIST_1309_Wjets_estimation" --output="./" --makeplot=False
#python ../ztautau/scripts/merge.py --var="tau_pt" --reg="SR_35med_Tau1Track" --lab="TEST REGION" --icut="6" --input="/coepp/cephfs/mel/laram1/ztautau/TEST_0209" --output="./" --makeplot=False

#     THREE PRONG  
#python ../ztautau/scripts/merge.py --var="tau_pt" --reg="SR_lowSCDP_lowMT_Tau3Track" --lab="TEST REGION" --icut="5" --input="/coepp/cephfs/mel/laram1/ztautau/HIST_1309_Wjets_estimation" --output="./" --makeplot=False
#python ../ztautau/scripts/merge.py --var="tau_pt" --reg="SR_lowSCDP_lowMT_SS_Tau3Track" --lab="TEST REGION" --icut="5" --input="/coepp/cephfs/mel/laram1/ztautau/HIST_1309_Wjets_estimation" --output="./" --makeplot=False
python ../ztautau/scripts/merge.py --var="tau_pt" --reg="SR_Tau3Track" --lab="TEST" --icut="5" --input="/coepp/cephfs/mel/laram1/ztautau/HIST_1309_Wjets_estimation" --output="./" --makeplot=False
#python ../ztautau/scripts/merge.py --var="tau_pt" --reg="SR_SS_Tau3Track" --lab="TEST" --icut="5" --input="/coepp/cephfs/mel/laram1/ztautau/HIST_1309_Wjets_estimation" --output="./" --makeplot=False

#python ../ztautau/scripts/merge.py --var="tau_pt" --reg="SR_Tau3Track" --lab="TEST" --icut="5" --input="/coepp/cephfs/mel/laram1/ztautau/HIST_0809_tauptcut35GeV_SYS_VARS" --output="./" --makeplot=False
python ../ztautau/scripts/merge.py --var="tau_pt" --reg="SR_25med_Tau3Track" --lab="TEST REGION" --icut="6" --input="/coepp/cephfs/mel/laram1/ztautau/HIST_1309_Wjets_estimation" --output="./" --makeplot=False
#python ../ztautau/scripts/merge.py --var="tau_pt" --reg="SR_35med_Tau3Track" --lab="TEST REGION" --icut="6" --input="/coepp/cephfs/mel/laram1/ztautau/TEST_0209" --output="./" --makeplot=False

#SYSTEMATICS
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


