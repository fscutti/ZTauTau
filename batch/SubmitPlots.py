#!/usr/bin/python

import os
import subprocess
import time
from ztautau import plots

def make_tag(cat,var):
  return '_'.join([cat,var])

#---------------------
# Set environment
#---------------------
# Environment variables defined in batchsetup.sh

ana      = 'ztautau'

<<<<<<< HEAD
indir    = 'HistKOALA'
outdir   = 'PlotsKOALA_SR'
=======
indir    = 'Hist_allregions'
outdir   = 'Plots_allregions'
>>>>>>> 2065d524ff182c29c1ff4af30511c7734dca1618


USER    = os.getenv('USER')
MAIN    = os.getenv('MAIN')

#inpath = os.path.join("/imports/rcs5_data",USER,ana)
inpath  = os.path.join("/data/laram1/ztautau")
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

<<<<<<< HEAD
# SIGNAL REGION ---------------------------------
"""
regions["SR"] 		= [4,"SR"]
"""
regions['SR_Tau3Track'] = [5,'SR_Tau3Track']
regions['SR_Tau1Track'] = [5,'SR_Tau1Track']
"""
regions["SR_25med"] 	= [5,"SR_25med"]

regions['SR_25med_Tau1Track'] = [6,'SR_25med_Tau1Track']
regions["SR_25med_Tau3Track"] = [6,"SR_25med_Tau3Track"]

regions['SR_25med_lowPT_Tau1Track'] = [7,'SR_25med_lowPT_Tau1Track']
regions['SR_25med_highPT_Tau1Track'] = [7,'SR_25med_highPT_Tau1Track']
regions['SR_25med_lowPT_Tau3Track'] = [7,'SR_25med_lowPT_Tau3Track']
regions['SR_25med_highPT_Tau3Track'] = [7,'SR_25med_highPT_Tau3Track']

regions["SR_highPT"] 	= [5,"SR_highPT"]
regions["SR_lowPT"] 	= [5,"SR_lowPT"]
regions['SR_highPT_Tau1Track'] = [6,'SR_highPT_Tau1Track']
regions['SR_lowPT_Tau1Track'] = [6,'SR_lowPT_Tau1Track']
regions['SR_highPT_Tau3Track'] = [6,'SR_highPT_Tau3Track']
regions['SR_lowPT_Tau3Track'] = [6,'SR_lowPT_Tau3Track']

"""
# SS SIGNAL REGION ------------------------------
"""
regions["SR_SS"]	= [4, "SR_SS"]
regions['SR_SS_Tau3Track'] = [5,'SR_SS_Tau3Track']
regions['SR_SS_Tau1Track'] = [5,'SR_SS_Tau1Track']

regions["SR_SS_25med"]  = [5, "SR_25med"]

regions['SR_SS_25med_Tau1Track'] = [6,'SR_SS_25med_Tau1Track']
regions['SR_SS_25med_Tau3Track'] = [6,'SR_SS_25med_Tau3Track']

regions['SR_SS_25med_lowPT_Tau1Track'] = [7,'SR_SS_25med_lowPT_Tau1Track']
regions['SR_SS_25med_highPT_Tau1Track'] = [7,'SR_SS_25med_highPT_Tau1Track']
regions['SR_SS_25med_lowPT_Tau3Track'] = [7,'SR_SS_25med_lowPT_Tau3Track']
regions['SR_SS_25med_highPT_Tau3Track'] = [7,'SR_SS_25med_highPT_Tau3Track']

regions["SR_SS_highPT"] = [5, "SR_SS_highPT"]
regions["SR_SS_lowPT"] 	= [5, "SR_SS_lowPT"]
regions['SR_SS_highPT_Tau1Track'] = [6,'SR_SS_highPT_Tau1Track']
regions['SR_SS_lowPT_Tau1Track'] = [6,'SR_SS_lowPT_Tau1Track']
regions['SR_SS_highPT_Tau3Track'] = [6,'SR_SS_highPT_Tau3Track']
regions['SR_SS_lowPT_Tau3Track'] = [6,'SR_SS_lowPT_Tau3Track']
"""
# WJETS SS --------------------------------------
"""
regions["Wjets_SS"] 	   = [3, "Wjets_SS"]
regions["Wjets_SS_Tau1Track"] = [4,"Wjets_SS_Tau1Track"]
regions["Wjets_SS_Tau3Track"] = [4,"Wjets_SS_Tau3Track"]


regions["Wjets_SS_25med"]  = [4, "Wjets_SS_25med"]

regions["Wjets_SS_highPT"] = [4, "Wjets_SS_highPT"]
regions["Wjets_SS_lowPT"]  = [4, "Wjets_SS_lowPT"]
"""

# WJETS OS --------------------------------------
"""
regions["Wjets_OS"]	   = [3, "Wjets_OS"]
regions["Wjets_OS_Tau1Track"] = [4,"Wjets_OS_Tau1Track"]
regions["Wjets_OS_Tau3Track"] = [4,"Wjets_OS_Tau3Track"]


regions["Wjets_OS_25med"]  = [4, "Wjets_OS_25med"]

regions["Wjets_OS_highPT"] = [4, "Wjets_OS_highPT"]
regions["Wjets_OS_lowPT"]  = [4, "Wjets_OS_lowPT"]
"""

# ANTI ISO SS -----------------------------------
"""
regions["AntiIsoCR_SS"]	       = [2, "AntiIso_SS"]
regions["AntiIsoCR_SS_Tau1Track"] = [3,"AntiIso_SS_Tau1Track"]
regions["AntiIsoCR_SS_Tau3Track"] = [3,"AntiIso_SS_Tau3Track"]

regions["AntiIsoCR_SS_25med"]  = [3, "AntiIso_SS_25med"]

regions["AntiIsoCR_SS_highPT"] = [3, "AntiIso_SS_highPT"]
regions["AntiIsoCR_SS_lowPT"]  = [3, "AntiIso_SS_lowPT"]
"""
# ANTI ISO OS -----------------------------------
"""
regions["AntiIsoCR_OS"]	       = [2, "AntiIso_OS"]
regions["AntiIsoCR_OS_Tau1Track"] = [3,"AntiIso_OS_Tau1Track"]
regions["AntiIsoCR_OS_Tau3Track"] = [3,"AntiIso_OS_Tau3Track"]

regions["AntiIsoCR_OS_25med"]  = [3, "AntiIso_OS_25med"]

regions["AntiIsoCR_OS_highPT"] = [3, "AntiIso_OS_highPT"]
regions["AntiIsoCR_OS_lowPT"]  = [3, "AntiIso_OS_lowPT"]
"""
=======
regions["SR"] = [4,"loose+loose"]

>>>>>>> 2065d524ff182c29c1ff4af30511c7734dca1618

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
  vars_list = plots.vars.vars_list
  #vars_list = plots.vars_fakes.vars_list

  for var in vars_list:

    job_vars['VAR']      = var.name
    job_vars['REG']      = REG
    job_vars['ICUT']     = str(OPT[0])
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

