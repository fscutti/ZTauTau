head ="""#!/bin/bash
#PBS -V
#PBS -q long
cd $PBS_O_WORKDIR
echo "ROOT SETUP"
setupATLAS
lsetup root
cd /coepp/cephfs/mel/brianl/lfv/fscutti_plotter/
source setup.sh
cd /coepp/cephfs/mel/brianl/lfv/fscutti_plotter/test/
INPATH="/coepp/cephfs/share/atlas/LFV/july_redown"
INPATHFRIEND="/coepp/cephfs/share/atlas/LFV/bdt_v3_ff_test"
OUTPATH="/coepp/cephfs/mel/brianl/lfv/fscutti_plotter/test/"
INSCRIPT="../ztautau/run"
SCRIPT="presel.plotter.py"
"""
template = """
python  ${INSCRIPT}/${SCRIPT} \\
  --input ${INPATH}/%s \\
  --friendinput ${INPATHFRIEND}/%s \\
  --sampletype="%s" \\
  --samplename="%s/%s.hist-output" \\
  --datatype=%s\\
"""

#############################################################
# Usage:
# python SubmitMissing.py <output of PostHist> <sampletype> <folder output> <datatype>
#############################################################
import sys, os, subprocess

# Make directory
directory = sys.argv[3]
if not os.path.exists(directory):
    os.makedirs(directory) 

# Loop over 
for file in open(sys.argv[1]):
    print file
    if not sys.argv[2] in file: continue
    file = file.strip()
    file = file.split('%s/' % sys.argv[2])[1]
    outfile = file.split('/')[-1].split('.hist')[0]
    subfile = open(sys.argv[3]+'/'+outfile+'.sh', 'w')
    subfile.write(head)
    #print template % (sys.argv[2]+'/'+file, sys.argv[2]+'/'+file+'.friend', sys.argv[2], sys.argv[3], outfile, sys.argv[4])
    subfile.write(template % (sys.argv[2]+'/'+file, sys.argv[2]+'/'+file+'.friend', sys.argv[2], sys.argv[3], outfile, sys.argv[4]))
os.system('chmod -R 777 '+sys.argv[3])
    #cmd = 'qsub '+sys.argv[3]+'/'+outfile+'.sh'
    #print cmd
    #m = subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE)                                                                                    
    #print m.communicate()[0]
os.system('find '+sys.argv[3]+' -type f > resub_files.txt')
for line in open('resub_files.txt', 'r').readlines():
    line = line.strip()
    os.system('qsub '+line)
