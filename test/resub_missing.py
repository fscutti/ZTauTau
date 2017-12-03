head ="""
#!/bin/bash
## Batch
INPATH="/coepp/cephfs/share/atlas/LFV/july_redown"
INPATHFRIEND="/coepp/cephfs/share/atlas/LFV/bdt_v3_ff_test"
INSCRIPT="../ztautau/run"
SCRIPT="ac.plotter.py"
"""
template = """
python  ${INSCRIPT}/${SCRIPT} \\
  --input ${INPATH}/%s \\
  --friendinput ${INPATHFRIEND}/%s \\
  --sampletype="%s" \\
  --samplename="%s/%s.hist-output" \\
  --datatype=%s\\
"""
import sys, os
subfile = open(sys.argv[3], 'w')
subfile.write(head)
#####################################################
# Usage:
# python resub_missing <output of PostHist> <filepath> <out filename> <data or mc> <datatype>
####################################################
for file in open(sys.argv[1]):
    print file
    if not sys.argv[2] in file: continue
    file = file.strip()
    file = file.split('%s/' % sys.argv[2])[1]
    outfile = file.split('/')[-1].split('.hist')[0]
    print template % (sys.argv[2]+'/'+file, sys.argv[2]+'/'+file+'.friend', sys.argv[2], sys.argv[4], outfile, sys.argv[5])
    subfile.write(template % (sys.argv[2]+'/'+file, sys.argv[2]+'/'+file+'.friend', sys.argv[2], sys.argv[4], outfile, sys.argv[5]))

directory = sys.argv[4]
if not os.path.exists(directory):
    os.makedirs(directory) 
