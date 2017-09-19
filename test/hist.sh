#!/bin/bash
## Batch
#python ../ztautau/run/j.plotter.py --input /data/fscutti/shared/v03/merged/nominal/physics_Main_00276262.root --sampletype="data" --events=300
#python ../ztautau/run/j.plotter.py \
#--input /lustre/atlas/group/higgs/TauTauHadHad/TNT/full/batch_p1443_current_merged/nominal/ttbar_allhad.root --sampletype="mc" ##--config="sys:FWEIGHT_UP"

#python ../ztautau/run/j.plotter.py --input /coepp/cephfs/mel/fscutti/ztautau/v15_r7772/merged/nominal/PoPy8_Wminustaunu.root --sampletype="mc" --events=500
#python ../ztautau/run/j.plotter.py --input /coepp/cephfs/mel/fscutti/ztautau/v15_r7772/merged/nominal/PoPy8_Wminustaunu.root --sampletype="mc" --events=10 --config="sys:MUID_DN"

# test for new lfv code
#python ../ztautau/run/j.plotter.py --input /coepp/cephfs/share/atlas/LFV/july/data/group.phys-higgs.ClhsH.data16_13TeV.00311481.physics_Main.D2.f758_m1710_p2950.1707nomv3_hist/group.phys-higgs.11697527._000013.hist-output.root --sampletype="data" --events=10 #--config="sys:MUID_DN"


python ../ztautau/run/j.plotter.py --input /coepp/cephfs/share/atlas/LFV/july/mc/group.phys-higgs.ClhsH.mc15_13TeV.410000.PoPy_P2012_ttb_nonallh.D2.e3698_s2608_s2183_r7725_r7676_p2949.1707nomv3_hist/group.phys-higgs.11697682._000030.hist-output.root --sampletype="mc" --events=1000 #--config="sys:MUID_DN"







