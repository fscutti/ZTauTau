import os,sys
for line in open(sys.argv[1],'r').readlines():
    line = line.strip()
    os.system('qsub '+line)
