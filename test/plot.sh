#!bin/bash

# Strings are passed to the script but this is redundant!

#python ../ztautau/scripts/merge.py --var="tau_pt" --reg="SR" --lab="TEST REGION" --icut="4" --input="/coepp/cephfs/mel/laram1/ztautau/TEST_0209" --output="./" --makeplot=True
#python ../ztautau/scripts/merge.py --var="tau_pt" --reg="SR_25med" --lab="TEST REGION" --icut="5" --input="/coepp/cephfs/mel/laram1/ztautau/TEST_0209" --output="./" --makeplot=True
#python ../ztautau/scripts/merge.py --var="tau_pt" --reg="SR_OS_no_cuts" --lab="TEST REGION" --icut="0" --input="/coepp/cephfs/mel/laram1/ztautau/HistEMU_new" --output="./" --makeplot=True

#     ONE PRONG  

#python ../ztautau/scripts/merge.py --var="tau_pt" --reg="SR_Tau1Track" --lab="TEST" --icut="5" --input="/coepp/cephfs/mel/laram1/ztautau/TEST_0209" --output="./" --makeplot=False
#python ../ztautau/scripts/merge.py --var="tau_pt" --reg="SR_25med_Tau1Track" --lab="TEST REGION" --icut="6" --input="/coepp/cephfs/mel/laram1/ztautau/TEST_0209" --output="./" --makeplot=False
#python ../ztautau/scripts/merge.py --var="tau_pt" --reg="SR_35med_Tau1Track" --lab="TEST REGION" --icut="6" --input="/coepp/cephfs/mel/laram1/ztautau/HISTv19_2015_ttb" --output="./" --makeplot=False

#     THREE PRONG  

python ../ztautau/scripts/merge.py --var="tau_pt" --reg="SR_Tau3Track" --lab="TEST" --icut="5" --input="/coepp/cephfs/mel/laram1/ztautau/TEST_0209" --output="./" --makeplot=False
python ../ztautau/scripts/merge.py --var="tau_pt" --reg="SR_25med_Tau3Track" --lab="TEST REGION" --icut="6" --input="/coepp/cephfs/mel/laram1/ztautau/TEST_0209" --output="./" --makeplot=False
#python ../ztautau/scripts/merge.py --var="tau_pt" --reg="SR_35med_Tau3Track" --lab="TEST REGION" --icut="6" --input="/coepp/cephfs/mel/laram1/ztautau/HISTv19_2015_ttb" --output="./" --makeplot=False

#SYSTEMATICS
#python ../ztautau/scripts/merge.py --var="tau_pt" --reg="SR" --lab="TEST REGION" --icut="4" --input="/coepp/cephfs/mel/laram1/ztautau/TEST_0209/TAUSF_SYS_DN" --output="./" --makeplot=False
#python ../ztautau/scripts/merge.py --var="tau_pt" --reg="SR_25med" --lab="TEST REGION" --icut="5" --input="/coepp/cephfs/mel/laram1/ztautau/TEST_0209/TAUSF_SYS_DN" --output="./" --makeplot=False
#
#python ../ztautau/scripts/merge.py --var="tau_pt" --reg="SR_Tau1Track" --lab="TEST" --icut="5" --input="/coepp/cephfs/mel/laram1/ztautau/TEST_0209/MUID_UP" --output="./" --makeplot=True
#python ../ztautau/scripts/merge.py --var="tau_pt" --reg="SR_25med_Tau1Track" --lab="TEST REGION" --icut="6" --input="/coepp/cephfs/mel/laram1/ztautau/TEST_0209/MUID_UP" --output="./" --makeplot=True
#
#   TESTS
#python ../ztautau/scripts/merge.py --var="tau_pt" --reg="AntiIsoCR_OS" --lab="AntiIso" --icut="3" --input="/coepp/cephfs/mel/laram1/ztautau/TEST_0209" --output="./" --makeplot=True
#python ../ztautau/scripts/merge.py --var="tau_pt" --reg="AntiIsoCR_SS" --lab="AntiIso" --icut="3" --input="/coepp/cephfs/mel/laram1/ztautau/TEST_0209" --output="./" --makeplot=True

#python ../ztautau/scripts/merge.py --var="tau_pt" --reg="AntiIsoCR_OS_25med" --lab="AntiIso" --icut="4" --input="/coepp/cephfs/mel/laram1/ztautau/TEST_0209" --output="./" --makeplot=True
#python ../ztautau/scripts/merge.py --var="tau_pt" --reg="AntiIsoCR_SS_25med" --lab="AntiIso" --icut="4" --input="/coepp/cephfs/mel/laram1/ztautau/TEST_0209" --output="./" --makeplot=True


