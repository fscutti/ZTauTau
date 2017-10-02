# encoding: utf-8
'''
PostHist.py
this is the script to run for checking that 
all subjobs are successful and hadd the output
'''

import os
import collections


# input path
inpath = "/coepp/cephfs/share/atlas/LFV/july"

# basepath common to all output
outbasepath = "/coepp/cephfs/share/atlas/LFV/FirstTestNN"

def gen_file_dict(path):
  file_dict = {}
  for dirname in os.listdir(path):
    if os.path.isdir(os.path.join(path,dirname)):
      file_dict[os.path.join(path,dirname)] = os.listdir(os.path.join(path,dirname))
  return file_dict

def find_list_diff(list1,list2):
  diff = []
  for l1 in list1:
    if not l1.split(".root")[0]+".root" in list2: 
      diff.append(l1)
  return diff


outdir = {}

outdir["data"] = []
outdir["data"].append("NN_data_main")
outdir["data"].append("NN_data_osw")
outdir["data"].append("NN_data_ssw")
outdir["data"].append("NN_data_qcd")

outdir["mc"] = []
outdir["mc"].append("NN_mc")
outdir["mc"].append("NN_mc_missing")

jobtype = ["nominal"]


# fill the dictionaries
in_file_dict = gen_file_dict( os.path.join(inpath,"data") )

print "-------------------------"
print "Printing data summary ..."
print "-------------------------"

out_file_dict = {}
for d in outdir["data"]:
  out_file_dict[d] = {}
  for jt in jobtype:

    out_file_dict[d][jt] = gen_file_dict( os.path.join(outbasepath,d,jt,"data") )

    for odir,ofiles in out_file_dict[d][jt].iteritems():
      for idir, ifiles in in_file_dict.iteritems():
        if os.path.basename(odir) in idir:
          if collections.Counter(ifiles) != collections.Counter(ofiles):
            print
            print "WARNING: in output dir %s " % odir
            print "from input dir %s " % idir
            print "the following files are missing:"
            print find_list_diff(ifiles, ofiles)
            print


print "-------------------------"
print "Printing MC summary ..."
print "-------------------------"

out_file_dict = {}
for d in outdir["mc"]:
  out_file_dict[d] = {}
  for jt in jobtype:

    out_file_dict[d][jt] = gen_file_dict( os.path.join(outbasepath,d,jt,"mc") )

    for odir,ofiles in out_file_dict[d][jt].iteritems():
      for idir, ifiles in in_file_dict.iteritems():
        if os.path.basename(odir) in idir:
          if collections.Counter(ifiles) != collections.Counter(ofiles):
            print
            print "WARNING: in output dir %s " % odir
            print "from input dir %s " % idir
            print "the following files are missing:"
            print find_list_diff(ifiles, ofiles)
            print


# EOF
