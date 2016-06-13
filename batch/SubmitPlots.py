#!/usr/bin/python

import os
import subprocess
import time
from ssdilep import plots

def make_tag(cat,var):
  return '_'.join([cat,var])

#---------------------
# Set environment
#---------------------
# Environment variables defined in batchsetup.sh

ana      = 'ssdilep'

indir    = 'HistMonVRTwoMu'
outdir   = 'PlotsMonVRTwoMu'

#indir    = 'HistVROneMu'
#outdir   = 'PlotsVROneMu'

USER    = os.getenv('USER')
MAIN    = os.getenv('MAIN')

inpath = os.path.join("/imports/rcs5_data",USER,ana)
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
JOBDIR    = "/imports/rcs5_data/%s/jobdir" % USER

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
# use it as such:
#regions["FOLDERNAME"]     = [icut, "plot label"]

#regions["FAKESVR1_NUM"]   = [5,  "numerator"]
#regions["FAKESVR1_LTDEN"] = [5,"loose+tight"]
#regions["FAKESVR1_TLDEN"] = [5,"tight+loose"]
#regions["FAKESVR1_LLDEN"] = [5,"loose+loose"]

#regions["FAKESVR2_NUM"]   = [6,  "numerator"]
#regions["FAKESVR2_LTDEN"] = [6,"loose+tight"]
#regions["FAKESVR2_TLDEN"] = [6,"tight+loose"]
#regions["FAKESVR2_LLDEN"] = [6,"loose+loose"]

#regions["FAKESVR3_NUM"]   = [6,  "numerator"]
#regions["FAKESVR3_LTDEN"] = [6,"loose+tight"]
#regions["FAKESVR3_TLDEN"] = [6,"tight+loose"]
#regions["FAKESVR3_LLDEN"] = [6,"loose+loose"]

regions["FAKESVR4_NUM"]   = [6,  "numerator"]
regions["FAKESVR4_LTDEN"] = [6,"loose+tight"]
regions["FAKESVR4_TLDEN"] = [6,"tight+loose"]
regions["FAKESVR4_LLDEN"] = [6,"loose+loose"]

#regions["FAKESVR5_NUM"]   = [6,  "numerator"]
#regions["FAKESVR5_LTDEN"] = [6,"loose+tight"]
#regions["FAKESVR5_TLDEN"] = [6,"tight+loose"]
#regions["FAKESVR5_LLDEN"] = [6,"loose+loose"]


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
  vars_list = plots.vars_mumu.vars_list
  #vars_list = plots.vars_fakes.vars_list

  for var in vars_list:

    job_vars['VAR']      = var.name
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

