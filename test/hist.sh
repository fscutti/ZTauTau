#!/bin/bash
## Batch

INPATH="/coepp/cephfs/share/atlas/LFV/july"
INSCRIPT="../ztautau/run"
SCRIPT="brian.plotter.py"


python  ${INSCRIPT}/${SCRIPT} \
  --input ${INPATH}/mc/group.phys-higgs.ClhsH.mc15_13TeV.410000.PoPy_P2012_ttb_nonallh.D2.e3698_s2608_s2183_r7725_r7676_p2949.1707nomv3_hist/group.phys-higgs.11697682._000030.hist-output.root \
  --sampletype="mc" \
  --samplename="group.phys-higgs.11697682._000030.hist-output" \
  --events=1000 \
#--config="sys:TAUID_DN"


