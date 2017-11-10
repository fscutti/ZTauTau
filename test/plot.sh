#!bin/bash

# Strings are passed to the script but this is redundant!

#python ../ztautau/scripts/merge.py --var="tau_0_pt" --reg="presel_el16inc" --lab="TEST REGION" --icut="12" --input="/coepp/cephfs/share/atlas/LFV/test_v1" --output="./" --makeplot=True
#python ../ztautau/scripts/merge.py --var="tau_0_pt" --reg="presel_mu16inc" --lab="TEST REGION" --icut="14" --input="/coepp/cephfs/share/atlas/LFV/ac_v1/NN_allregions_ac" --output="./" --makeplot=False

#python ../ztautau/scripts/merge.py --var="cutflow_weighted" --reg="presel_mu15inc" --lab="TEST REGION" --input="/coepp/cephfs/share/atlas/LFV/ac_v10" --output="./" --printcutflow=True
#python ../ztautau/scripts/merge.py --var="cutflow_weighted" --reg="presel_mu16inc" --lab="TEST REGION" --input="/coepp/cephfs/share/atlas/LFV/ac_v10" --output="./" --printcutflow=True
#python ../ztautau/scripts/merge.py --var="cutflow_weighted" --reg="presel_el15inc" --lab="TEST REGION" --input="/coepp/cephfs/share/atlas/LFV/ac_v10" --output="./" --printcutflow=True
#python ../ztautau/scripts/merge.py --var="cutflow_weighted" --reg="presel_el16inc" --lab="TEST REGION" --input="/coepp/cephfs/share/atlas/LFV/ac_v10" --output="./" --printcutflow=True


#python ../ztautau/scripts/merge.py --var="output_Z" --reg="presel_mu15inc" --lab="TEST REGION" --icut="15" --input="/coepp/cephfs/share/atlas/LFV/ac_v12" --output="./" --makeplot=True
#python ../ztautau/scripts/merge.py --var="output_Z" --reg="presel_mu16inc" --lab="TEST REGION" --icut="15" --input="/coepp/cephfs/share/atlas/LFV/ac_v12" --output="./" --makeplot=True
#python ../ztautau/scripts/merge.py --var="output_Z" --reg="presel_el15inc" --lab="TEST REGION" --icut="15" --input="/coepp/cephfs/share/atlas/LFV/ac_v12" --output="./" --makeplot=True
#python ../ztautau/scripts/merge.py --var="output_Z" --reg="presel_el16inc" --lab="TEST REGION" --icut="15" --input="/coepp/cephfs/share/atlas/LFV/ac_v12" --output="./" --makeplot=True
#python ../ztautau/scripts/merge.py --var="cutflow_weighted" --reg="presel_mu16inc" --lab="TEST REGION" --icut="17" --input="/coepp/cephfs/share/atlas/LFV/ac_v12" --output="./" --printcutflow=True

python ../ztautau/scripts/merge.py --var="cutflow_weighted" --reg="presel_mu151p" --lab="TEST REGION" --icut="17" --input="/coepp/cephfs/share/atlas/LFV/ac_v13" --output="./" --printcutflow=True
python ../ztautau/scripts/merge.py --var="cutflow_weighted" --reg="presel_el151p" --lab="TEST REGION" --icut="17" --input="/coepp/cephfs/share/atlas/LFV/ac_v13" --output="./" --printcutflow=True

#python ../ztautau/scripts/merge.py --var="tau_0_pt" --reg="presel_muallinc" --lab="TEST REGION" --icut="15" --input="/coepp/cephfs/share/atlas/LFV/ac_v13" --output="./" --makeplot=True
#python ../ztautau/scripts/merge.py --var="tau_0_pt" --reg="presel_elallinc" --lab="TEST REGION" --icut="15" --input="/coepp/cephfs/share/atlas/LFV/ac_v13" --output="./" --makeplot=True
#python ../ztautau/scripts/merge.py --var="lep_0_pt" --reg="presel_muallinc" --lab="TEST REGION" --icut="15" --input="/coepp/cephfs/share/atlas/LFV/ac_v13" --output="./" --makeplot=True
#python ../ztautau/scripts/merge.py --var="lep_0_pt" --reg="presel_elallinc" --lab="TEST REGION" --icut="15" --input="/coepp/cephfs/share/atlas/LFV/ac_v13" --output="./" --makeplot=True
#python ../ztautau/scripts/merge.py --var="output_BDT" --reg="presel_muallinc" --lab="TEST REGION" --icut="15" --input="/coepp/cephfs/share/atlas/LFV/ac_v13" --output="./" --makeplot=True
#python ../ztautau/scripts/merge.py --var="output_BDT" --reg="presel_elallinc" --lab="TEST REGION" --icut="15" --input="/coepp/cephfs/share/atlas/LFV/ac_v13" --output="./" --makeplot=True
