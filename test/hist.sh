#!/bin/bash
## Batch

INPATH="/coepp/cephfs/share/atlas/LFV/july"
INPATHFRIEND="/coepp/cephfs/share/atlas/LFV/friendsLFVH"
INSCRIPT="../ztautau/run"
SCRIPT="brian.plotter.py"

python  ${INSCRIPT}/${SCRIPT} \
  --input ${INPATH}/mc/group.phys-higgs.ClhsH.mc15_13TeV.344084.PoPy8_ggH125_taumu.D2.e5003_s2726_r7772_r7676_p2949.1707nomv3r1_hist/group.phys-higgs.11716884._000001.hist-output.root \
  --friendinput ${INPATHFRIEND}/mc/group.phys-higgs.ClhsH.mc15_13TeV.344084.PoPy8_ggH125_taumu.D2.e5003_s2726_r7772_r7676_p2949.1707nomv3r1_hist/group.phys-higgs.11716884._000001.hist-output.root.friend \
  --sampletype="mc" \
  --samplename="group.phys-higgs.11697682._000030.hist-output" \
  --events=1000 \
#--config="sys:TAUID_DN"


