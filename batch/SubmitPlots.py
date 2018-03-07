#!/usr/bin/python

import os, sys
import subprocess
import time
from ztautau.hists import final_binning_hists
from ztautau.hists import Main_hists

def make_tag(cat,var):
  return '_'.join([cat,var])

from optparse import OptionParser

#-----------------
# input
#-----------------
parser = OptionParser()
parser.add_option('-i', '--indir', dest='indir',
                  help='input directory', default=None)
parser.add_option('-o', '--outdir', dest='outdir',
                  help='output directory', default=None)
parser.add_option('-b', '--background', dest='BKGD',
                  help='background estimation', default=None)
parser.add_option('-t', '--regiontype', dest='regiontype', 
                  help='region type', default=None)
parser.add_option('-p', '--plots', dest='plots', action="store_true",
                  help='make plots', default=False)
parser.add_option('-c', '--cutflow', dest='cutflow', action="store_true",
                  help='print cutflow', default=False)


(options, args) = parser.parse_args()
#---------------------
# Set environment
#---------------------
# Environment variables defined in batchsetup.sh

ana      = 'ztautau'

indir    = options.indir
outdir   = options.outdir
BKGD     = options.BKGD
REGTYPE  = options.regiontype

USER    = os.getenv('USER')
MAIN    = os.getenv('MAIN')

inpath = os.path.join("/coepp/cephfs/share/atlas/LFV/hists")
#inpath = os.path.join("/coepp/cephfs/mel/brianl/test")
INDIR   = os.path.join(inpath,indir)  
OUTDIR  = os.path.join(inpath,outdir)

if not os.path.isdir(OUTDIR): os.makedirs(OUTDIR)
if not os.path.isdir(OUTDIR+"/"+"log"): os.makedirs(OUTDIR+"/"+"log")

#---------------------
# Batch jobs options
#---------------------
AUTOBUILD = True
QUEUE     = 'long'
NCORES    = 4
BEXEC     = 'Plots.sh'
##JOBDIR    = "/imports/rcs5_data/%s/jobdir" % USER
JOBDIR    = "/coepp/cephfs/mel/%s/jobdir" % USER

#---------------------
# Batch jobs variables
#---------------------
INTARBALL = os.path.join(JOBDIR,'plotstarball_%s.tar.gz' % (time.strftime("d%d_m%m_y%Y_H%H_M%M_S%S")) )
SCRIPT    = os.path.join("./",ana,"scripts",'merge_v1.py')
#SCRIPT    = os.path.join("./",ana,"scripts",'merge.py')

job_vars={}
job_vars['INTARBALL'] = INTARBALL
job_vars['OUTDIR']    = OUTDIR
job_vars['INDIR']     = INDIR
job_vars['BKGD']      = BKGD
job_vars['SCRIPT']    = SCRIPT

regions = {}

# -----------------------------------------------
# use it as such:
# 
# regions["FOLDERNAME"]     = [icut, "plot label"]
# -----------------------------------------------
label = 'Tight\ ID' if 'tight' in REGTYPE else 'Medium\ ID'
regions["presel_muallinc"] = [14,"mu-had\ Preselection\ "+label]
regions["presel_elallinc"] = [14,"el-had\ Preselection\ "+label]
regions["sr1_muallinc"]    = [14,"mu-had\ SR1\ "+label]
regions["sr1_elallinc"]    = [14,"el-had\ SR1\ "+label]
regions["sr2_muallinc"]    = [14,"mu-had\ SR2\ "+label]
regions["sr2_elallinc"]    = [14,"el-had\ SR2\ "+label]
regions["sr3_muallinc"]    = [14,"mu-had\ SR3\ "+label]
regions["sr3_elallinc"]    = [14,"el-had\ SR3\ "+label]
#regions["highZ_muallinc"]  = [16,"mu-had High NN Z (>0.9)"]
#regions["highZ_elallinc"]  = [16,"el-had High NN Z (>0.9)"]
#regions["lowZ_muallinc"]   = [16,"mu-had Low NN Z (<0.1)"]
#regions["lowZ_elallinc"]   = [16,"el-had Low NN Z (<0.1)"]


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
  #vars_list= final_binning_hists.variables_NN+final_binning_hists.variables_BDT
  #vars_list = final_binning_hists.variables_out
  #vars_list = Main_hists.variables_out
  #vars_list = final_binning_hists.hist_ac
  vars_list = final_binning_hists.hist_fit
  #vars_list = final_binning_hists.hist_presel
  for var in vars_list:
    #print var.hname
    #continue
    job_vars['VAR']      = var.hname
    job_vars['REG']      = REG
    job_vars['ICUT']     = OPT[0]
    job_vars['LAB']      = OPT[1]
    job_vars['MAKEPLOT'] = options.plots
    job_vars['REGTYPE']  = REGTYPE+'_'+REG.split('_')[0]
    job_vars['PCW']      = options.cutflow
    
    VARS = []
    
    for vname in job_vars.keys(): VARS += ['%s=%s' % (vname,job_vars[vname])]
    
    cmd = 'qsub'
    cmd += ' -l nodes=1:ppn=%d'  % NCORES
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

