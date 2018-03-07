#!/bin/bash
## Batch

#INPATH="/coepp/cephfs/share/atlas/LFV/july_redown_sys1"
#INPATHFRIEND="/coepp/cephfs/share/atlas/LFV/bdt_v3_ff_test_sys1"
#INPATH="/coepp/cephfs/share/atlas/LFV/july_redown"
INPATHFRIEND="/coepp/cephfs/share/atlas/LFV/bdt_v3_ff_test"

#INPATHFRIEND="/coepp/cephfs/share/atlas/LFV/friendsLFVH"
#INPATHFRIEND="/coepp/cephfs/share/atlas/LFV/bdt_ff_v1"
#INPATHFRIEND="/coepp/cephfs/share/atlas/LFV/bdt_v3_ff_test"

INPATH="/coepp/cephfs/share/atlas/LFV/july_redown_slim_all"
INPATHFRIEND="/coepp/cephfs/share/atlas/LFV/mva_july_redown_slim_all"

INSCRIPT="../ztautau/run"
SCRIPT="presel.plotter.py"

#python  ${INSCRIPT}/${SCRIPT} \
#  --input ${INPATH}/mc/group.phys-higgs.ClhsH.mc15_13TeV.344084.PoPy8_ggH125_taumu.D2.e5003_s2726_r7772_r7676_p2949.1707nomv3r1_hist/group.phys-higgs.11716884._000001.hist-output.root \
#  --friendinput ${INPATHFRIEND}/mc/group.phys-higgs.ClhsH.mc15_13TeV.344084.PoPy8_ggH125_taumu.D2.e5003_s2726_r7772_r7676_p2949.1707nomv3r1_hist/group.phys-higgs.11716884._000001.hist-output.root.friend \
#  --sampletype="mc" \
#  --samplename="mc.hist-output" \
#  --events=1000 \
#--config="sys:TAUID_DN"
#python  ${INSCRIPT}/${SCRIPT} \
#  --input ${INPATH}/mc/group.phys-higgs.ClhsH.mc15_13TeV.345121.PoPy8EG_ggH125_tautaulm15hp20.D2.e5814_s2726_r7772_r7676_p3017.1707nomv3r2_hist/group.phys-higgs.11758912._000001.hist-output.root \
#  --friendinput ${INPATHFRIEND}/mc/group.phys-higgs.ClhsH.mc15_13TeV.345121.PoPy8EG_ggH125_tautaulm15hp20.D2.e5814_s2726_r7772_r7676_p3017.1707nomv3r2_hist/group.phys-higgs.11758912._000001.hist-output.root.friend \
#  --sampletype="mc" \
#  --samplename="mc.hist-output" \
#  --datatype="main" \
#  --events=10000 \

#python  ${INSCRIPT}/${SCRIPT} \
# --input ${INPATH}/mc/group.phys-higgs.ClhsH.mc15_13TeV.344774.Sh221_PDF30_Ztt_MHPT0_70_l15h20.D2.e5585_s2726_r7772_r7676_p3017.1707nomv3_hist/user.ademaria.12498238._000001.out.root \
# --sampletype="mc" \
# --samplename="mc.hist-output" \
# --datatype="main" \
# --events=1000 \

#python  ${INSCRIPT}/${SCRIPT} \
# --input ${INPATH}/mc/group.phys-higgs.ClhsH.mc15_13TeV.344774.Sh221_PDF30_Ztt_MHPT0_70_l15h20.D2.e5585_s2726_r7772_r7676_p3017.1707nomv3_hist/group.phys-higgs.11697100._000002.hist-output.root \
# --friendinput ${INPATHFRIEND}/mc/group.phys-higgs.ClhsH.mc15_13TeV.344774.Sh221_PDF30_Ztt_MHPT0_70_l15h20.D2.e5585_s2726_r7772_r7676_p3017.1707nomv3_hist/group.phys-higgs.11697100._000002.hist-output.root.friend \
# --sampletype="mc" \
# --samplename="mc.hist-output" \
# --datatype="main" \
# --events=1000 \
# --config="sys:TAUS_TRUEHADTAU_EFF_RECO_TOTAL_1up_TauEffSF_reco"

#python  ${INSCRIPT}/${SCRIPT} \
# --input ${INPATH}/mc/group.phys-higgs.ClhsH.mc15_13TeV.344084.PoPy8_ggH125_taumu.D2.e5003_s2726_r7772_r7676_p2949.1707nomv3r1_hist/group.phys-higgs.11716884._000001.hist-output.root \
# --friendinput ${INPATHFRIEND}/mc/group.phys-higgs.ClhsH.mc15_13TeV.344084.PoPy8_ggH125_taumu.D2.e5003_s2726_r7772_r7676_p2949.1707nomv3r1_hist/group.phys-higgs.11716884._000001.hist-output.root.friend \
# --sampletype="mc" \
# --samplename="mc.hist-output" \
# --datatype="main" \
# --events=1000 \
# --config="sys:TAUS_TRUEHADTAU_EFF_RECO_TOTAL_1up_TauEffSF_reco"

#python  ${INSCRIPT}/${SCRIPT} \
#  --input ${INPATH}/data/group.phys-higgs.ClhsH.data16_13TeV.00304128.physics_Main.D2.f716_m1620_p2950.1707nomv3_hist/group.phys-higgs.11697324._000020.hist-output.root \
#  --friendinput ${INPATHFRIEND}/data/group.phys-higgs.ClhsH.data16_13TeV.00304128.physics_Main.D2.f716_m1620_p2950.1707nomv3_hist/group.phys-higgs.11697324._000020.hist-output.root.friend \
#  --sampletype="data" \
#  --samplename="data.hist-output" \
#  --datatype="qcd" \
#  --events=3\


#python  ${INSCRIPT}/${SCRIPT} \
#  --input ${INPATH}/mc/group.phys-higgs.ClhsH.mc15_13TeV.364103.Sh221_PDF30_Zmumu_MHPT70_140_CVetoBVeto.D2.e5271_s2726_r7772_r7676_p3017.1707sys1_hist/group.phys-higgs.11719975._000001.hist-output.root \
#  --friendinput ${INPATHFRIEND}/mc/group.phys-higgs.ClhsH.mc15_13TeV.364103.Sh221_PDF30_Zmumu_MHPT70_140_CVetoBVeto.D2.e5271_s2726_r7772_r7676_p3017.1707sys1_hist/group.phys-higgs.11719975._000001.hist-output.root.friend \
#  --sampletype="mc" \
#  --samplename="mc.hist-output" \
#  --datatype="main" \
#  --events=10000 \
#  #--config="sys:MUON_ID_1down"

#python  ${INSCRIPT}/${SCRIPT} \
#  --input ${INPATH}/data/group.phys-higgs.ClhsH.data16_13TeV.00304128.physics_Main.D2.f716_m1620_p2950.1707nomv3_hist/group.phys-higgs.11697324._000020.hist-output.root \
#  --friendinput ${INPATHFRIEND}/data/group.phys-higgs.ClhsH.data16_13TeV.00304128.physics_Main.D2.f716_m1620_p2950.1707nomv3_hist/group.phys-higgs.11697324._000020.hist-output.root.friend \
#  --sampletype="data" \
#  --samplename="data.hist-output" \
#  --datatype="ff" \
#  #--events=1000\

#SCRIPT="presel.plotter.py"
#python  ${INSCRIPT}/${SCRIPT} \
# --input             ${INPATH}/mc/group.phys-higgs.ClhsH.mc15_13TeV.344084.PoPy8_ggH125_taumu.D2.e5003_s2726_r7772_r7676_p2949.1707nomv3r1_hist/user.ademaria.12498124._000001.out.root \
# --friendinput ${INPATHFRIEND}/mc/group.phys-higgs.ClhsH.mc15_13TeV.344084.PoPy8_ggH125_taumu.D2.e5003_s2726_r7772_r7676_p2949.1707nomv3r1_hist/user.ademaria.12498124._000001.out.root.friend \
# --sampletype="mc" \
# --samplename="mc_med.hist-output" \
# --datatype="main" \
## --events=10000 \

#SCRIPT="tight.plotter.py"
#python  ${INSCRIPT}/${SCRIPT} \
# --input             ${INPATH}/mc/group.phys-higgs.ClhsH.mc15_13TeV.344084.PoPy8_ggH125_taumu.D2.e5003_s2726_r7772_r7676_p2949.1707nomv3r1_hist/user.ademaria.12498124._000002.out.root \
# --friendinput ${INPATHFRIEND}/mc/group.phys-higgs.ClhsH.mc15_13TeV.344084.PoPy8_ggH125_taumu.D2.e5003_s2726_r7772_r7676_p2949.1707nomv3r1_hist/user.ademaria.12498124._000002.out.root.friend \
# --sampletype="mc" \
# --samplename="mc_tight.hist-output" \
# --datatype="main" \
# --events=10000 \
# --input             ${INPATH}/mc/group.phys-higgs.ClhsH.mc15_13TeV.364108.Sh221_PDF30_Zmumu_MHPT140_280_BFilter.D2.e5271_s2726_r7772_r7676_p3017.1707nomv3_hist/user.ademaria.12499100._000016.out.root \
# --friendinput ${INPATHFRIEND}/mc/group.phys-higgs.ClhsH.mc15_13TeV.364108.Sh221_PDF30_Zmumu_MHPT140_280_BFilter.D2.e5271_s2726_r7772_r7676_p3017.1707nomv3_hist/user.ademaria.12499100._000016.out.root.friend \
 #--config="sys:TAUS_TRUEHADTAU_EFF_RECO_TOTAL_1up_TauEffSF_reco"

#python  ${INSCRIPT}/${SCRIPT} \
# --input             ${INPATH}/data/group.phys-higgs.ClhsH.data16_13TeV.00311481.physics_Main.D2.f758_m1710_p2950.1707nomv3_hist/user.ademaria.12496168._000013.out.root        \
# --friendinput ${INPATHFRIEND}/data/group.phys-higgs.ClhsH.data16_13TeV.00311481.physics_Main.D2.f758_m1710_p2950.1707nomv3_hist/user.ademaria.12496168._000013.out.root.friend \
# --sampletype="data" \
# --samplename="data.hist-output" \
# --datatype="main" \
# --events=10000 \
# --config="sys:TAUS_TRUEHADTAU_EFF_RECO_TOTAL_1up_TauEffSF_reco"

#INPATH="/coepp/cephfs/share/atlas/LFV/july_redown_slim_all_sys1"
#INPATHFRIEND="/coepp/cephfs/share/atlas/LFV/mva_july_redown_slim_all_sys1"
#python  ${INSCRIPT}/${SCRIPT} \
# --input             ${INPATH}/mc/group.phys-higgs.ClhsH.mc15_13TeV.345121.PoPy8EG_ggH125_tautaulm15hp20.D2.e5814_s2726_r7772_r7676_p3017.1707nomv3r2_hist/345121.root        \
# --friendinput ${INPATHFRIEND}/mc/group.phys-higgs.ClhsH.mc15_13TeV.345121.PoPy8EG_ggH125_tautaulm15hp20.D2.e5814_s2726_r7772_r7676_p3017.1707nomv3r2_hist/345121.root.friend \
# --sampletype="mc" \
# --samplename="mc_sys1.hist-output" \
# --datatype="main" \
# --events=10000 \
# --config="sys:EG_RESOLUTION_ALL_1down"

INPATH="/coepp/cephfs/share/atlas/LFV/july_redown_slim_all_hadd"
INPATHFRIEND="/coepp/cephfs/share/atlas/LFV/mva_july_redown_slim_all_hadd"
SCRIPT="tight_slice.plotter.py"
python  ${INSCRIPT}/${SCRIPT} \
 --input             ${INPATH}/mc/group.phys-higgs.ClhsH.mc15_13TeV.344084.PoPy8_ggH125_taumu.D2.e5003_s2726_r7772_r7676_p2949.1707nomv3r1_hist/344084.root \
 --friendinput ${INPATHFRIEND}/mc/group.phys-higgs.ClhsH.mc15_13TeV.344084.PoPy8_ggH125_taumu.D2.e5003_s2726_r7772_r7676_p2949.1707nomv3r1_hist/344084.root.friend \
 --sampletype="mc" \
 --samplename="mc_tight_slice1.hist-output" \
 --datatype="main" \
 --minentry=0 \
 --maxentry=50000 \
 --config sys:jet_FT_EFF_Eigen_B_0_1down_global_effSF_MVX \

