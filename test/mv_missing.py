import os, sys
import subprocess
#print file
#folder = 
#cmd = ["find", " -name",  "\"*%s*\"" % file, folder]
#print cmd
#m=subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE)
##print m.read()
#stdout, stderr = m.communicate()
#print stdout
import os, fnmatch
 

for infile in open(sys.argv[1]).readlines():
    infile=infile.strip()
    if infile.endswith('/'): continue
    print infile
    file=infile.split('higgs')[1].split('.')[1]
    inDIR = sys.argv[2]#'/coepp/cephfs/mel/brianl/ztautau/NN_allregions_ac'
    pattern = "*%s*" % file
    fileList = []

    # Walk through directory
    for dName, sdName, fList in os.walk(inDIR):
        for fileName in fList:
            if fnmatch.fnmatch(fileName, pattern): # Match search string
                fileList.append(os.path.join(dName, fileName))
    outpath = '/'.join(fileList[0].split('/')[:-1])
    print 'mv %s %s' % (infile, outpath)
    os.system('cp %s %s' % (infile, outpath))
