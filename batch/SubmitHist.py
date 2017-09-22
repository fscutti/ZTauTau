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

def prepare_path(path):
    if not os.path.exists(path):
        #print 'preparing outpath: %s'%(path)
        os.makedirs(path)

## environment variables
## ---------------------
MAIN        = os.getenv('MAIN')                    # upper folder
USER        = os.getenv('USER')
NTUP        = '/coepp/cephfs/share/atlas/LFV/july' # global config input NTUP path
JOBDIR      = "/coepp/cephfs/mel/%s/jobdir" % USER             # The Melb cloud is twisted and does not recognize home dirs...
prepare_path(JOBDIR)
INTARBALL   = os.path.join(JOBDIR,'histtarball_%s.tar.gz' % (time.strftime("d%d_m%m_y%Y_H%H_M%M_S%S")) )
AUTOBUILD   = True                                 # auto-build tarball using Makefile.tarball
NJMAX       = 500

# outputs  
RUN         = 'HistTEST'
OUTPATH     = "/coepp/cephfs/mel/%s/ztautau/%s"%(USER,RUN) # 

# running
QUEUE       = "long"                             # length of pbs queue (short, long, extralong )
SCRIPT      = "./ztautau/run/j.plotter.py"       # pyframe job script
BEXEC       = "Hist.sh"                          # exec script (probably dont change) 
DO_NOM      = True                               # submit the nominal job
DO_NTUP_SYS = False                              # submit the NTUP systematics jobs
DO_PLOT_SYS = False                              # submit the plot systematics jobs
TESTMODE    = False                              # submit only 1 sub-job (for testing)
NCORES      = 1

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
    global NJMAX
    global INTARBALL
    global AUTOBUILD
    global RUN
    global OUTPATH
    global QUEUE
    global SCRIPT
    global BEXEC
    global DO_NOM
    global DO_NTUP_SYS
    global DO_PLOT_SYS
    global TESTMODE
    
    assert (NJMAX<=600), "Error: please, not more than 600 subjobs per array!"

    ## construct config file
    ## ---------------------
    nsubjobs = 0
    nrun     = 1
    nlines   = 0
    f_dict   = {} 

    data_subdir = get_subdir( os.path.join(NTUP,'data') )
    mc_subdir = get_subdir( os.path.join(NTUP,'mc') )

    all_subdir = data_subdir + mc_subdir

    outrootpath = os.path.abspath(os.path.join(OUTPATH,tag))
    logrootpath = os.path.abspath(os.path.join(OUTPATH,'log_%s'%tag))
    
    prepare_path(outrootpath)
    prepare_path(logrootpath)

    absintar   = os.path.abspath(INTARBALL)
   
   
    totsubjob = 0
    # not efficienct. Who cares?
    for s in samps:
        sinputs  = input_files(all_subdir,s,job_sys) 
        for infile in sinputs:
          #soutput  = output_file(s,infile,job_sys)
          #if file_exists(os.path.abspath(os.path.join(outrootpath,s.type,s.name)),soutput): continue
          totsubjob += 1


    for s in samps:
        
        # configure output path 
        absoutpath = os.path.abspath(os.path.join(outrootpath,s.type,s.name))
        
        prepare_path(absoutpath)

        ## input & output
        sinputs  = input_files(all_subdir,s,job_sys) 
         
        for infile in sinputs:
           soutput  = output_file(s,infile,job_sys)
           
           if file_exists(absoutpath,soutput): continue
           
           ## config
           sconfig = {}
           sconfig.update(config)
           sconfig.update(s.config)
           sconfig_str = ",".join(["%s:%s"%(key,val) for key,val in sconfig.items()])
           
           # abspath of infile
           infpath = os.path.join(NTUP,s.type,infile)

           # write many lines here
           line = ';'.join([s.name,infpath,soutput,s.type,sconfig_str])
           
           cfg = os.path.join(JOBDIR,'Config%s.%s.run.%s'%(RUN,tag,nrun))
           abslogpath = os.path.abspath(os.path.join(logrootpath,"log_run_%d"%nrun))
           
           if not str(nrun) in f_dict.keys():
             """
             WIP
             if file_exists(JOBDIR,'Config%s.%s.run.%s'%(RUN,tag,nrun)): 
               
               # resubmission of failed jobs
               cfg = cfg.replace(".run.",".resub.")
               abslogpath = abslogpath.replace("_run_","_resub_")
             """ 
             f_dict[str(nrun)] = open(cfg,'w')
           prepare_path(abslogpath)
           
           f_dict[str(nrun)].write('%s\n'%line)
           nlines += 1
           nsubjobs += 1 
           
           if nsubjobs >= nrun*NJMAX or nsubjobs==totsubjob:
             
             f_dict[str(nrun)].close()
             
             nrun += 1
             
             # configure input path 
             # --------------------
             abscfg     = os.path.abspath(cfg)
             if TESTMODE: nsubjobs = 1
             
             vars=[]
             vars+=["CONFIG=%s"    % abscfg       ]
             vars+=["INTARBALL=%s" % absintar     ]
             vars+=["OUTPATH=%s"   % outrootpath  ]
             vars+=["SCRIPT=%s"    % SCRIPT       ]
             vars+=["NCORES=%d"    % NCORES       ]
             
             VARS = ','.join(vars)
             
             cmd = 'qsub'
             cmd += ' -l nodes=1:ppn=%d'  % NCORES
             cmd += ' -q %s'              % QUEUE
             cmd += ' -v "%s"'            % VARS
             cmd += ' -N j.hist.%s'       % tag
             cmd += ' -j oe -o %s/log'    % abslogpath
             cmd += ' -t1-%d'             % nlines
             cmd += ' %s'                 % BEXEC 
             print cmd
             
             m = subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE)
             print m.communicate()[0]

             nlines = 0

def input_files(subdirs,sample,sys):
    global NTUP
    for sdir in subdirs:
      if sample.name in sdir:
        return get_subfile(os.path.join(NTUP,sample.type,sdir))

def output_file(sample,infile,sys):
    return os.path.basename(infile)

def file_exists(path,file):
    if os.path.exists(path):
      return file in os.listdir(os.path.join(path))
    else: return False

def get_subdir(mydir):
    return [name for name in os.listdir(mydir)
            if os.path.isdir(os.path.join(mydir, name))]

def get_subfile(mydir):
    return [os.path.join(mydir,name) for name in os.listdir(mydir)
            if os.path.isfile(os.path.join(mydir, name))]


if __name__=='__main__': main()

## EOF



