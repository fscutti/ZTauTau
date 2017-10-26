#!bin/bash

# Strings are passed to the script but this is redundant!

#python ../ztautau/scripts/merge.py --var="tau_0_pt" --reg="presel_mu161p" --lab="TEST REGION" --icut="11" --input="/coepp/cephfs/share/atlas/LFV/test_v1" --output="./" --makeplot=False

python ../ztautau/scripts/merge.py --var="cutflow" --reg="presel_mu16inc" --lab="TEST REGION" --input="/coepp/cephfs/share/atlas/LFV/test_v1" --output="./" --printcutflow=True


