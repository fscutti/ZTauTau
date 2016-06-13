"""
This script retrieves a list of samples 
from the grid using tags specifed in the 
sample name. It launches the script Get.sh 
for each of the samples in parallel using PBS.
"""

import os
import sys
import subprocess

from pyutils.utils import recreplace, mcstrings


# ---------------------------
# details of grid sample name
# ---------------------------
user  = "lixia"
samp  = "00284285"
jtag  = "*15_13TeV.*%s*ntup-v03" % samp
#jtype = "lptnp"
jtype = "lhtnp"
sys   = None
if not sys: sys = "nominal"


# -------------------
# details of this job
# -------------------
SCRIPT     = "Get.sh"
OUTDIR     = "/data/%s/shared/v03" % os.getenv("USER")
OUTMERGED  = os.path.join(OUTDIR,"merged",sys)
OUTHIST    = os.path.join(OUTDIR,"hist",sys)
OUTLOGS    = os.path.join(OUTDIR,"log",sys)
JOB_TAG    = jtag
QUEUE      = "long"
JOBDIR    = "/data/%s/jobdir" % os.getenv("USER")

dir_list = []
dir_list.append(os.path.join(OUTDIR,"hist"))
dir_list.append(os.path.join(OUTDIR,"hist",sys))
dir_list.append(os.path.join(OUTDIR,"merged"))
dir_list.append(os.path.join(OUTDIR,"merged",sys))
dir_list.append(os.path.join(OUTDIR,"log"))
dir_list.append(os.path.join(OUTDIR,"log",sys))

for d in dir_list:
 if not os.path.exists(d):
   os.makedirs(d)


# --------------------------------
# lilst of samples to be retrieved
# --------------------------------
outjobs_hist = "%s_%s_%s_hist.txt" % (user, jtype, jtag)
outjobs_hist = recreplace(outjobs_hist,[["*","X"]])


# --------------------------
# download sample with rucio
# --------------------------
infile_hist = os.path.join(JOBDIR,outjobs_hist)

with open(infile_hist,"w") as f:
  cmd = "rucio list-dids"
  cmd += " %s.%s:" % ("user",user)
  cmd += "%s.%s.%s.*%s_hist*" % ("user",user,jtype,jtag)
  #cmd += "%s.%s.%s.*%s*hist*" % ("user",user,jtype,jtag)
  print cmd
  m = subprocess.Popen(cmd,shell=True,stdout=f)
  print m.communicate()[0]
f.close()

outputs = {}

rep = []
rep.append([" ",""])
rep.append(["\n",""])
rep.append(["|",""])
rep.append(["CONTAINER",""])
rep.append(["user.%s:"%user,""])

with open(infile_hist) as f: lines = f.readlines()
for l in lines:
  if not "CONTAINER" in l: continue
  if "duplicates" in l: continue
  key = recreplace(l.replace("_hist",""),rep)
  outputs[key] = {}
  print key
  outputs[key]["hist"] = recreplace(l,rep)
f.close()

jrep = []
jrep.append(["user",""])
jrep.append([user,""])
jrep.append([":",""])
jrep.append(["..",""])
jrep.append([".root",""])

# ----------------------
# Send the jobs with PBS
# ----------------------
for k,v in outputs.iteritems():
  print 'downloading %s ...' % k
  job_name = recreplace(k,jrep)
  if job_name.startswith("."): job_name = job_name[1:]
  if "physics_Main" in job_name: id = k.split(".")[5]+"_"+k.split(".")[4]
  else: id = k.split(".")[5]
  #merged = recreplace(id, mcstrings)
  merged = id
  
  vars=[]
  vars+=["HISTFILE=%s"      % v["hist"]      ]
  vars+=["MERGEDHIST=%s"    % merged+".root" ] 
  vars+=["OUTHIST=%s"       % OUTHIST        ]
  vars+=["OUTMERGED=%s"     % OUTMERGED      ]

  VARS = ','.join(vars)

  cmd = 'qsub'
  cmd += ' -q %s'       % QUEUE
  cmd += ' -v "%s"'     % VARS
  cmd += ' -N j.get.%s' % job_name
  cmd += ' -j n -o %s'  % OUTLOGS
  cmd += ' -e %s'       % OUTLOGS
  cmd += ' %s'          % SCRIPT
  
  print cmd
  m = subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE)
  print m.communicate()[0]

# EOF
