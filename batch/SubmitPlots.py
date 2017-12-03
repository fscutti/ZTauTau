#!/usr/bin/python

import os, sys
import subprocess
import time
from ztautau.hists import final_binning_hists

def make_tag(cat,var):
  return '_'.join([cat,var])

#---------------------
# Set environment
#---------------------
# Environment variables defined in batchsetup.sh

ana      = 'ztautau'

indir    = sys.argv[1]#'ac_v14'
outdir   = sys.argv[2]#'plots_v4_ac_v14'

USER    = os.getenv('USER')
MAIN    = os.getenv('MAIN')

inpath = os.path.join("/coepp/cephfs/share/atlas/LFV")
INDIR   = os.path.join(inpath,indir)  
OUTDIR  = os.path.join(inpath,outdir)

if not os.path.isdir(OUTDIR): os.makedirs(OUTDIR)
if not os.path.isdir(OUTDIR+"/"+"log"): os.makedirs(OUTDIR+"/"+"log")

#---------------------
# Batch jobs options
#---------------------
AUTOBUILD = True
QUEUE     = 'short'
BEXEC     = 'Plots.sh'
##JOBDIR    = "/imports/rcs5_data/%s/jobdir" % USER
JOBDIR    = "/coepp/cephfs/mel/%s/jobdir" % USER

#---------------------
# Batch jobs variables
#---------------------
INTARBALL = os.path.join(JOBDIR,'plotstarball_%s.tar.gz' % (time.strftime("d%d_m%m_y%Y_H%H_M%M_S%S")) )
SCRIPT    = os.path.join("./",ana,"scripts",'merge.py')

job_vars={}
job_vars['INTARBALL'] = INTARBALL
job_vars['OUTDIR']    = OUTDIR
job_vars['INDIR']     = INDIR
job_vars['SCRIPT']    = SCRIPT

regions = {}

# -----------------------------------------------
# use it as such:
# 
# regions["FOLDERNAME"]     = [icut, "plot label"]
# -----------------------------------------------

regions["presel_muallinc"] = [15,"mu-had Preselection"]
regions["presel_elallinc"] = [15,"el-had Preselection"]
regions["sr1_muallinc"]    = [16,"mu-had SR1"]
regions["sr1_elallinc"]    = [16,"el-had SR1"]
regions["sr2_muallinc"]    = [16,"mu-had SR2"]
regions["sr2_elallinc"]    = [16,"el-had SR2"]
regions["sr3_muallinc"]    = [16,"mu-had SR3"]
regions["sr3_elallinc"]    = [16,"el-had SR3"]
regions["highZ_muallinc"]  = [16,"mu-had High NN Z (>0.9)"]
regions["highZ_elallinc"]  = [16,"el-had High NN Z (>0.9)"]
regions["lowZ_muallinc"]   = [16,"mu-had Low NN Z (<0.1)"]
regions["lowZ_elallinc"]   = [16,"el-had Low NN Z (<0.1)"]


#---------------------
# Make input tarball
#---------------------
if os.path.exists(os.path.join(INTARBALL)):
  print 'removing existing tarball %s...'% (INTARBALL)
  cmd = 'rm %s' % (INTARBALL)
  m = subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE)
  m.communicate()[0]

print 'building input tarball %s...'% (INTARBALL)
cmd = 'cd %s; make -f Makefile.plots TARBALL=%s' % (MAIN,INTARBALL)
m = subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE)
m.communicate()[0]


for REG,OPT in regions.iteritems():
  #vars_list = final_binning_hists.hist_list+final_binning_hists.hist_presel
  vars_list= final_binning_hists.variables_NN+final_binning_hists.variables_BDT
  for var in vars_list:
    job_vars['VAR']      = var.hname
    job_vars['REG']      = REG
    job_vars['ICUT']     = OPT[0]
    job_vars['LAB']      = OPT[1]
    job_vars['MAKEPLOT'] = True
    
    VARS = []
    
    for vname in job_vars.keys(): VARS += ['%s=%s' % (vname,job_vars[vname])]
    
    cmd = 'qsub'
    cmd += " -q %s" % QUEUE
    cmd += ' -v "%s"' % (','.join(VARS))
    cmd += ' -N j.plots.%s' % (make_tag(REG,job_vars['VAR']))
    cmd += ' -o %s/log' % (OUTDIR)
    cmd += ' -e %s/log' % (OUTDIR)
    cmd += ' %s' % BEXEC
    print cmd
    m = subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE)
    print m.communicate()[0]
 
## EOF

