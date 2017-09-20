# encoding: utf-8
'''
SubmitHist.py
'''

## modules
import os
import re
import subprocess
import time
from   ztautau.samples import samples

## environment variables
MAIN   = os.getenv('MAIN') # upper folder
USER   = os.getenv('USER')

## global config
# input NTUP path
NTUP='/data/fscutti/test/merged' 

# The Melb cloud is twisted and does not recognize home dirs...
JOBDIR = "/data/%s/jobdir" % USER 
INTARBALL = os.path.join(JOBDIR,'histtarball_%s.tar.gz' % (time.strftime("d%d_m%m_y%Y_H%H_M%M_S%S")) )

# auto-build tarball using Makefile.tarball
AUTOBUILD = True                

# outputs
RUN = 'HistTEST'

OUTPATH="/data/%s/ztautau/%s"%(USER,RUN) # 
#OUTFILE="ntuple.root"         # file output by pyframe job 

# running
QUEUE="long"                         # length of pbs queue (short, long, extralong )
SCRIPT="./ztautau/run/j.plotter.py"  # pyframe job script
BEXEC="Hist.sh"                      # exec script (probably dont change) 
DO_NOM = True                        # submit the nominal job
DO_NTUP_SYS = False                  # submit the NTUP systematics jobs
DO_PLOT_SYS = False                  # submit the plot systematics jobs
TESTMODE = False                     # submit only 1 sub-job (for testing)

NCORES = 1

def main():
    """
    * configure the samples (input->output)
    * configure which samples to run for each systematic
    * prepare outdirs and build intarball
    * launch the jobs
    """
    global MAIN
    global USER
    global NTUP
    global INTARBALL
    global AUTOBUILD
    global RUN
    global OUTPATH
    #global OUTFILE
    global QUEUE
    global SCRIPT
    global BEXEC
    global DO_NOM
    global DO_NTUP_SYS
    global DO_PLOT_SYS
    global TESTMODE

    ## get lists of samples
    all_mc   = samples.all_mc
    all_data = samples.all_data
    nominal  = all_data + all_mc 
   

    
    ntup_sys = [
        ['SYS1_UP',                  all_mc],
        ['SYS1_DN',                  all_mc],
        ]    
    
    plot_sys = [
        ['SYS2_UP',                  all_mc],
        ['SYS2_DN',                  all_mc],
        ]    

    
    all_sys = ntup_sys + plot_sys

    ## ensure output path exists
    prepare_path(OUTPATH)
    
    ## auto-build tarball
    if AUTOBUILD:
        print 'building input tarball %s...'% (INTARBALL)
        cmd = 'cd %s; make -f Makefile.hist TARBALL=%s' % (MAIN,INTARBALL)
        m = subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE)
        print m.communicate()[0]

    if DO_NOM: submit('nominal','nominal',nominal)
    if DO_NTUP_SYS: 
      for sys,samps in ntup_sys:
            submit(sys,sys,samps)
    if DO_PLOT_SYS:  
      for sys,samps in plot_sys:
            submit(sys,'nominal',samps,config={'sys':sys})


def submit(tag,job_sys,samps,config={}):
    """
    * construct config file 
    * prepare variable list to pass to job
    * submit job
    """
    global MAIN
    global USER
    global NTUP
    global INTARBALL
    global AUTOBUILD
    global RUN
    global OUTPATH
    #global OUTFILE
    global QUEUE
    global SCRIPT
    global BEXEC
    global DO_NOM
    global DO_NTUP_SYS
    global DO_PLOT_SYS
    global TESTMODE

    ## construct config file
    ## ---------------------
    cfg = os.path.join(JOBDIR,'Config%s.%s'%(RUN,tag))
    f = open(cfg,'w')

    for s in samps:

        ## input & output
        sinput = input_file(s,job_sys) 
        soutput = output_file(s,job_sys)

        ## sample type
        stype  = s.type

        ## config
        sconfig = {}
        sconfig.update(config)
        sconfig.update(s.config)
        sconfig_str = ",".join(["%s:%s"%(key,val) for key,val in sconfig.items()])

        line = ';'.join([s.name,sinput,soutput,stype,sconfig_str])
        
        if not file_exists(absoutpath,s.name+".root"): f.write('%s\n'%line)

    f.close()

    # configure input path 
    # --------------------
    abscfg     = os.path.abspath(cfg)
    absintar   = os.path.abspath(INTARBALL)
    nsubjobs   = len(samps)
    if TESTMODE: nsubjobs = 1


    prepare_path(absoutpath)
    prepare_path(abslogpath)

    vars=[]
    vars+=["CONFIG=%s"    % abscfg     ]
    vars+=["INTARBALL=%s" % absintar   ]
    vars+=["OUTPATH=%s"   % absoutpath ]
    vars+=["SCRIPT=%s"    % SCRIPT     ]
    vars+=["NCORES=%d"    % NCORES     ]

    VARS = ','.join(vars)

    cmd = 'qsub'
    cmd += ' -l nodes=1:ppn=%d' % NCORES
    cmd += ' -q %s'             % QUEUE
    cmd += ' -v "%s"'           % VARS
    cmd += ' -N j.hist.%s'      % tag
    cmd += ' -j oe -o %s/log'   % abslogpath
    cmd += ' -t1-%d'            % nsubjobs
    cmd += ' %s'                % BEXEC 
    print cmd
    m = subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE)
    print m.communicate()[0]

def prepare_path(path):
    if not os.path.exists(path):
        print 'preparing outpath: %s'%(path)
        os.makedirs(path)

def input_file(sample,sys):
    global NTUP
    sinput = sample.infile
    
    if sys!='nominal': sys='sys_'+sys
    sinput += '.root'
    sinput = os.path.join(NTUP,sys,sinput) 
    return sinput

def file_exists(path,file):
    if os.path.exists(path):
      return file in os.listdir(os.path.join(path))
    else: return False

def output_file(sample,sys):
    soutput = sample.name
    soutput += '.root'
    return soutput

if __name__=='__main__': main()


## EOF



