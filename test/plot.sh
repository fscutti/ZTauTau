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

python ../ztautau/scripts/merge.py --var="cutflow_weighted" --reg="presel_mu15inc" --lab="TEST REGION" --icut="17" --input="/coepp/cephfs/share/atlas/LFV/ac_v14" --output="./" --printcutflow=True
python ../ztautau/scripts/merge.py --var="cutflow_weighted" --reg="presel_el15inc" --lab="TEST REGION" --icut="17" --input="/coepp/cephfs/share/atlas/LFV/ac_v14" --output="./" --printcutflow=True
python ../ztautau/scripts/merge.py --var="cutflow_weighted" --reg="presel_mu16inc" --lab="TEST REGION" --icut="17" --input="/coepp/cephfs/share/atlas/LFV/ac_v14" --output="./" --printcutflow=True
python ../ztautau/scripts/merge.py --var="cutflow_weighted" --reg="presel_el16inc" --lab="TEST REGION" --icut="17" --input="/coepp/cephfs/share/atlas/LFV/ac_v14" --output="./" --printcutflow=True
python ../ztautau/scripts/merge.py --var="cutflow_weighted" --reg="presel_muallinc" --lab="TEST REGION" --icut="17" --input="/coepp/cephfs/share/atlas/LFV/ac_v14" --output="./" --printcutflow=True
python ../ztautau/scripts/merge.py --var="cutflow_weighted" --reg="presel_elallinc" --lab="TEST REGION" --icut="17" --input="/coepp/cephfs/share/atlas/LFV/ac_v14" --output="./" --printcutflow=True

python ../ztautau/scripts/merge.py --var="output_BDT" --reg="presel_muallinc" --lab="TEST REGION" --icut="15" --input="/coepp/cephfs/share/atlas/LFV/ac_v14" --output="./" --makeplot=True
python ../ztautau/scripts/merge.py --var="output_BDT" --reg="presel_elallinc" --lab="TEST REGION" --icut="15" --input="/coepp/cephfs/share/atlas/LFV/ac_v14" --output="./" --makeplot=True
python ../ztautau/scripts/merge.py --var="tau_0_pt" --reg="presel_muallinc" --lab="TEST REGION" --icut="15" --input="/coepp/cephfs/share/atlas/LFV/ac_v14" --output="./" --makeplot=True
python ../ztautau/scripts/merge.py --var="tau_0_pt" --reg="presel_elallinc" --lab="TEST REGION" --icut="15" --input="/coepp/cephfs/share/atlas/LFV/ac_v14" --output="./" --makeplot=True
python ../ztautau/scripts/merge.py --var="tau_0_eta" --reg="presel_muallinc" --lab="TEST REGION" --icut="15" --input="/coepp/cephfs/share/atlas/LFV/ac_v14" --output="./" --makeplot=True
python ../ztautau/scripts/merge.py --var="tau_0_eta" --reg="presel_elallinc" --lab="TEST REGION" --icut="15" --input="/coepp/cephfs/share/atlas/LFV/ac_v14" --output="./" --makeplot=True
python ../ztautau/scripts/merge.py --var="tau_0_phi" --reg="presel_muallinc" --lab="TEST REGION" --icut="15" --input="/coepp/cephfs/share/atlas/LFV/ac_v14" --output="./" --makeplot=True
python ../ztautau/scripts/merge.py --var="tau_0_phi" --reg="presel_elallinc" --lab="TEST REGION" --icut="15" --input="/coepp/cephfs/share/atlas/LFV/ac_v14" --output="./" --makeplot=True
python ../ztautau/scripts/merge.py --var="lep_0_pt" --reg="presel_muallinc" --lab="TEST REGION" --icut="15" --input="/coepp/cephfs/share/atlas/LFV/ac_v14" --output="./" --makeplot=True
python ../ztautau/scripts/merge.py --var="lep_0_pt" --reg="presel_elallinc" --lab="TEST REGION" --icut="15" --input="/coepp/cephfs/share/atlas/LFV/ac_v14" --output="./" --makeplot=True
python ../ztautau/scripts/merge.py --var="lep_0_eta" --reg="presel_muallinc" --lab="TEST REGION" --icut="15" --input="/coepp/cephfs/share/atlas/LFV/ac_v14" --output="./" --makeplot=True
python ../ztautau/scripts/merge.py --var="lep_0_eta" --reg="presel_elallinc" --lab="TEST REGION" --icut="15" --input="/coepp/cephfs/share/atlas/LFV/ac_v14" --output="./" --makeplot=True
python ../ztautau/scripts/merge.py --var="lep_0_phi" --reg="presel_muallinc" --lab="TEST REGION" --icut="15" --input="/coepp/cephfs/share/atlas/LFV/ac_v14" --output="./" --makeplot=True
python ../ztautau/scripts/merge.py --var="lep_0_phi" --reg="presel_elallinc" --lab="TEST REGION" --icut="15" --input="/coepp/cephfs/share/atlas/LFV/ac_v14" --output="./" --makeplot=True
python ../ztautau/scripts/merge.py --var="output_Z" --reg="presel_muallinc" --lab="TEST REGION" --icut="15" --input="/coepp/cephfs/share/atlas/LFV/ac_v14" --output="./" --makeplot=True
python ../ztautau/scripts/merge.py --var="output_Z" --reg="presel_elallinc" --lab="TEST REGION" --icut="15" --input="/coepp/cephfs/share/atlas/LFV/ac_v14" --output="./" --makeplot=True
python ../ztautau/scripts/merge.py --var="output_W" --reg="presel_muallinc" --lab="TEST REGION" --icut="15" --input="/coepp/cephfs/share/atlas/LFV/ac_v14" --output="./" --makeplot=True
python ../ztautau/scripts/merge.py --var="output_W" --reg="presel_elallinc" --lab="TEST REGION" --icut="15" --input="/coepp/cephfs/share/atlas/LFV/ac_v14" --output="./" --makeplot=True
python ../ztautau/scripts/merge.py --var="lephad_mt_tau_0_met" --reg="presel_muallinc" --lab="TEST REGION" --icut="15" --input="/coepp/cephfs/share/atlas/LFV/ac_v14" --output="./" --makeplot=True
python ../ztautau/scripts/merge.py --var="lephad_mt_tau_0_met" --reg="presel_elallinc" --lab="TEST REGION" --icut="15" --input="/coepp/cephfs/share/atlas/LFV/ac_v14" --output="./" --makeplot=True
python ../ztautau/scripts/merge.py --var="lephad_deta" --reg="presel_muallinc" --lab="TEST REGION" --icut="15" --input="/coepp/cephfs/share/atlas/LFV/ac_v14" --output="./" --makeplot=True
python ../ztautau/scripts/merge.py --var="lephad_deta" --reg="presel_elallinc" --lab="TEST REGION" --icut="15" --input="/coepp/cephfs/share/atlas/LFV/ac_v14" --output="./" --makeplot=True
python ../ztautau/scripts/merge.py --var="lephad_dr" --reg="presel_muallinc" --lab="TEST REGION" --icut="15" --input="/coepp/cephfs/share/atlas/LFV/ac_v14" --output="./" --makeplot=True
python ../ztautau/scripts/merge.py --var="lephad_dr" --reg="presel_elallinc" --lab="TEST REGION" --icut="15" --input="/coepp/cephfs/share/atlas/LFV/ac_v14" --output="./" --makeplot=True
python ../ztautau/scripts/merge.py --var="lephad_mt_lep_0_met" --reg="presel_muallinc" --lab="TEST REGION" --icut="15" --input="/coepp/cephfs/share/atlas/LFV/ac_v14" --output="./" --makeplot=True
python ../ztautau/scripts/merge.py --var="lephad_mt_lep_0_met" --reg="presel_elallinc" --lab="TEST REGION" --icut="15" --input="/coepp/cephfs/share/atlas/LFV/ac_v14" --output="./" --makeplot=True
python ../ztautau/scripts/merge.py --var="NN_input_lep_E" --reg="presel_muallinc" --lab="TEST REGION" --icut="15" --input="/coepp/cephfs/share/atlas/LFV/ac_v14" --output="./" --makeplot=True
python ../ztautau/scripts/merge.py --var="NN_input_lep_E" --reg="presel_elallinc" --lab="TEST REGION" --icut="15" --input="/coepp/cephfs/share/atlas/LFV/ac_v14" --output="./" --makeplot=True
python ../ztautau/scripts/merge.py --var="NN_input_lep_pz" --reg="presel_muallinc" --lab="TEST REGION" --icut="15" --input="/coepp/cephfs/share/atlas/LFV/ac_v14" --output="./" --makeplot=True
python ../ztautau/scripts/merge.py --var="NN_input_lep_pz" --reg="presel_elallinc" --lab="TEST REGION" --icut="15" --input="/coepp/cephfs/share/atlas/LFV/ac_v14" --output="./" --makeplot=True
python ../ztautau/scripts/merge.py --var="NN_input_lep_px" --reg="presel_muallinc" --lab="TEST REGION" --icut="15" --input="/coepp/cephfs/share/atlas/LFV/ac_v14" --output="./" --makeplot=True
python ../ztautau/scripts/merge.py --var="NN_input_lep_px" --reg="presel_elallinc" --lab="TEST REGION" --icut="15" --input="/coepp/cephfs/share/atlas/LFV/ac_v14" --output="./" --makeplot=True
python ../ztautau/scripts/merge.py --var="NN_input_boost" --reg="presel_muallinc" --lab="TEST REGION" --icut="15" --input="/coepp/cephfs/share/atlas/LFV/ac_v14" --output="./" --makeplot=True
python ../ztautau/scripts/merge.py --var="NN_input_boost" --reg="presel_elallinc" --lab="TEST REGION" --icut="15" --input="/coepp/cephfs/share/atlas/LFV/ac_v14" --output="./" --makeplot=True
python ../ztautau/scripts/merge.py --var="NN_input_met_E" --reg="presel_muallinc" --lab="TEST REGION" --icut="15" --input="/coepp/cephfs/share/atlas/LFV/ac_v14" --output="./" --makeplot=True
python ../ztautau/scripts/merge.py --var="NN_input_met_E" --reg="presel_elallinc" --lab="TEST REGION" --icut="15" --input="/coepp/cephfs/share/atlas/LFV/ac_v14" --output="./" --makeplot=True
python ../ztautau/scripts/merge.py --var="NN_input_met_pz" --reg="presel_muallinc" --lab="TEST REGION" --icut="15" --input="/coepp/cephfs/share/atlas/LFV/ac_v14" --output="./" --makeplot=True
python ../ztautau/scripts/merge.py --var="NN_input_met_pz" --reg="presel_elallinc" --lab="TEST REGION" --icut="15" --input="/coepp/cephfs/share/atlas/LFV/ac_v14" --output="./" --makeplot=True
python ../ztautau/scripts/merge.py --var="NN_input_tau_E" --reg="presel_muallinc" --lab="TEST REGION" --icut="15" --input="/coepp/cephfs/share/atlas/LFV/ac_v14" --output="./" --makeplot=True
python ../ztautau/scripts/merge.py --var="NN_input_tau_E" --reg="presel_elallinc" --lab="TEST REGION" --icut="15" --input="/coepp/cephfs/share/atlas/LFV/ac_v14" --output="./" --makeplot=True
python ../ztautau/scripts/merge.py --var="NN_input_mvis" --reg="presel_muallinc" --lab="TEST REGION" --icut="15" --input="/coepp/cephfs/share/atlas/LFV/ac_v14" --output="./" --makeplot=True
python ../ztautau/scripts/merge.py --var="NN_input_mvis" --reg="presel_elallinc" --lab="TEST REGION" --icut="15" --input="/coepp/cephfs/share/atlas/LFV/ac_v14" --output="./" --makeplot=True
python ../ztautau/scripts/merge.py --var="NN_input_mcoll" --reg="presel_muallinc" --lab="TEST REGION" --icut="15" --input="/coepp/cephfs/share/atlas/LFV/ac_v14" --output="./" --makeplot=True
python ../ztautau/scripts/merge.py --var="NN_input_mcoll" --reg="presel_elallinc" --lab="TEST REGION" --icut="15" --input="/coepp/cephfs/share/atlas/LFV/ac_v14" --output="./" --makeplot=True
python ../ztautau/scripts/merge.py --var="NN_input_mmc" --reg="presel_muallinc" --lab="TEST REGION" --icut="15" --input="/coepp/cephfs/share/atlas/LFV/ac_v14" --output="./" --makeplot=True
python ../ztautau/scripts/merge.py --var="NN_input_mmc" --reg="presel_elallinc" --lab="TEST REGION" --icut="15" --input="/coepp/cephfs/share/atlas/LFV/ac_v14" --output="./" --makeplot=True
python ../ztautau/scripts/merge.py --var="met_reco_et" --reg="presel_muallinc" --lab="TEST REGION" --icut="15" --input="/coepp/cephfs/share/atlas/LFV/ac_v14" --output="./" --makeplot=True
python ../ztautau/scripts/merge.py --var="met_reco_et" --reg="presel_elallinc" --lab="TEST REGION" --icut="15" --input="/coepp/cephfs/share/atlas/LFV/ac_v14" --output="./" --makeplot=True
python ../ztautau/scripts/merge.py --var="output_comb" --reg="presel_muallinc" --lab="TEST REGION" --icut="15" --input="/coepp/cephfs/share/atlas/LFV/ac_v14" --output="./" --makeplot=True
python ../ztautau/scripts/merge.py --var="output_comb" --reg="presel_elallinc" --lab="TEST REGION" --icut="15" --input="/coepp/cephfs/share/atlas/LFV/ac_v14" --output="./" --makeplot=True
