#!/bin/bash
## Batch

INPATH="/coepp/cephfs/share/atlas/LFV/july_redown"
#INPATHFRIEND="/coepp/cephfs/share/atlas/LFV/friendsLFVH"
INPATHFRIEND="/coepp/cephfs/share/atlas/LFV/bdt_ff_v1"
INSCRIPT="../ztautau/run"
SCRIPT="ac.plotter.py"

#python  ${INSCRIPT}/${SCRIPT} \
#  --input ${INPATH}/mc/group.phys-higgs.ClhsH.mc15_13TeV.344084.PoPy8_ggH125_taumu.D2.e5003_s2726_r7772_r7676_p2949.1707nomv3r1_hist/group.phys-higgs.11716884._000001.hist-output.root \
#  --friendinput ${INPATHFRIEND}/mc/group.phys-higgs.ClhsH.mc15_13TeV.344084.PoPy8_ggH125_taumu.D2.e5003_s2726_r7772_r7676_p2949.1707nomv3r1_hist/group.phys-higgs.11716884._000001.hist-output.root.friend \
#  --sampletype="mc" \
#  --samplename="mc.hist-output" \
#  --events=1000 \
#--config="sys:TAUID_DN"

python  ${INSCRIPT}/${SCRIPT} \
  --input ${INPATH}/mc/group.phys-higgs.ClhsH.mc15_13TeV.344084.PoPy8_ggH125_taumu.D2.e5003_s2726_r7772_r7676_p2949.1707nomv3r1_hist/group.phys-higgs.11716884._000001.hist-output.root \
  --friendinput ${INPATHFRIEND}/mc/group.phys-higgs.ClhsH.mc15_13TeV.344084.PoPy8_ggH125_taumu.D2.e5003_s2726_r7772_r7676_p2949.1707nomv3r1_hist/group.phys-higgs.11716884._000001.hist-output.root.friend \
  --sampletype="mc" \
  --samplename="mc.hist-output" \
  --datatype="main" \
  --events=10000 \

python  ${INSCRIPT}/${SCRIPT} \
  --input ${INPATH}/data/group.phys-higgs.ClhsH.data16_13TeV.00304128.physics_Main.D2.f716_m1620_p2950.1707nomv3_hist/group.phys-higgs.11697324._000020.hist-output.root \
  --friendinput ${INPATHFRIEND}/data/group.phys-higgs.ClhsH.data16_13TeV.00304128.physics_Main.D2.f716_m1620_p2950.1707nomv3_hist/group.phys-higgs.11697324._000020.hist-output.root.friend \
  --sampletype="data" \
  --samplename="data.hist-output" \
  --datatype="main" \
  --events=10000\
