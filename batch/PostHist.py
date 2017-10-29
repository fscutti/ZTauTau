# encoding: utf-8
'''
PostHist.py
this is the script to run for checking that 
all subjobs are successful and hadd the output
'''

import os
import collections
import subprocess


# input path
inpath = "/coepp/cephfs/share/atlas/LFV/july"

# basepath common to all output
outbasepath = "/coepp/cephfs/share/atlas/LFV/test_v1"

hadd_files = False


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

def hadd_cmd(outpath,outfile,inpath):
  cmd = 'hadd '
  cmd += '%s/%s.root ' % (outpath,outfile)
  cmd += '%s/*.root ' % inpath
  return cmd


outdir = {}

outdir["data"] = []
<<<<<<< HEAD
outdir["data"].append("NN_allregions_v2_data_main")
outdir["data"].append("NN_allregions_v2_data_osw")
outdir["data"].append("NN_allregions_v2_data_ssw")
outdir["data"].append("NN_allregions_v2_data_qcd")

outdir["mc"] = []
outdir["mc"].append("NN_allregions_v2_mc")
=======
outdir["data"].append("NN_allregions_v3_data_main")
outdir["data"].append("NN_allregions_v3_data_osw")
outdir["data"].append("NN_allregions_v3_data_ssw")
outdir["data"].append("NN_allregions_v3_data_qcd")

outdir["mc"] = []
outdir["mc"].append("NN_allregions_v3_mc")
>>>>>>> For AC
#outdir["mc"].append("NN_mc_missing")

jobtype = ["nominal"]


# fill the dictionaries

print "-------------------------"
print "Printing data summary ..."
print "-------------------------"

in_file_dict = gen_file_dict( os.path.join(inpath,"data") )

out_file_dict = {}
for d in outdir["data"]:
  out_file_dict[d] = {}
  for jt in jobtype:

    out_file_dict[d][jt] = gen_file_dict( os.path.join(outbasepath,d,jt,"data") )

    for odir,ofiles in out_file_dict[d][jt].iteritems():
      for idir, ifiles in in_file_dict.iteritems():
        if os.path.basename(odir) in idir:
          failed_files = []
          if collections.Counter(ifiles) != collections.Counter(ofiles):
            failed_files = find_list_diff(ifiles, ofiles)
            print
            print "WARNING!!! In output dir: %s " % odir
            print "from input dir:           %s " % idir
            print "the following files are missing:"
            print failed_files
            print
          if hadd_files and not failed_files:
            cmd = hadd_cmd( os.path.join(outbasepath,d,jt),  os.path.basename(odir), odir) 
            m = subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE)
            print m.communicate()[0]



print "-------------------------"
print "Printing MC summary ..."
print "-------------------------"

in_file_dict = gen_file_dict( os.path.join(inpath,"mc") )

out_file_dict = {}
for d in outdir["mc"]:
  out_file_dict[d] = {}
  for jt in jobtype:

    out_file_dict[d][jt] = gen_file_dict( os.path.join(outbasepath,d,jt,"mc") )
    for odir,ofiles in out_file_dict[d][jt].iteritems():
      for idir, ifiles in in_file_dict.iteritems():
        if os.path.basename(odir) in idir:
          failed_files = []
          if collections.Counter(ifiles) != collections.Counter(ofiles):
            failed_files = find_list_diff(ifiles, ofiles)
            print
            print "WARNING!!! In output dir: %s " % odir
            print "from input dir:           %s " % idir
            print "the following files are missing:"
            print failed_files
            print
          if hadd_files and not failed_files:
            cmd = hadd_cmd( os.path.join(outbasepath,d,jt),  os.path.basename(odir), odir) 
            m = subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE)
            print m.communicate()[0]

# EOF
