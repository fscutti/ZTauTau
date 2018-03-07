import os, sys
import subprocess
import fnmatch
 
#####################################
# Usage:
# python mv_missing <input file> <directory>
#####################################

for infile in open(sys.argv[1]).readlines():
    infile=infile.strip()
    if infile.endswith('/'): continue
    print infile
    #file=infile.split('higgs')[1].split('.')[1]
    file=infile.split('ademaria')[1].split('.')[1]
    inDIR = sys.argv[2]#'/coepp/cephfs/mel/brianl/ztautau/NN_allregions_ac'
    pattern = "*%s*" % file
    fileList = []

    # Walk through directory
    for dName, sdName, fList in os.walk(inDIR):
        for fileName in fList:
            if fnmatch.fnmatch(fileName, pattern): # Match search string
                fileList.append(os.path.join(dName, fileName))
    if len(fileList) < 1: 
        print "cannot find folder to place", infile
        continue
    outpath = '/'.join(fileList[0].split('/')[:-1])
    print 'mv %s %s' % (infile, outpath)
    os.system('cp %s %s' % (infile, outpath))
