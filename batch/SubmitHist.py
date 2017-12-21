# encoding: utf-8
'''
SubmitHist.py
'''

## modules
import os, sys
import re
import subprocess
import time
from   ztautau.samples import samples

#_____________________________________________________________________________
def prepare_path(path):
    if not os.path.exists(path):
        #print 'preparing outpath: %s'%(path)
        os.makedirs(path)

#_____________________________________________________________________________
def sys_conf(name=None, main_path_mod=None,friend_path_mod=None,samples=None):
  return {"name":name, "main_path_mod":main_path_mod, "friend_path_mod":friend_path_mod,"samples":samples}



## environment variables
## ---------------------
MAIN        = os.getenv('MAIN')                           # upper folder
USER        = os.getenv('USER')
NTUP        = '/coepp/cephfs/share/atlas/LFV/july_redown'        # global config input NTUP path
#FRIENDPATH  = '/coepp/cephfs/share/atlas/LFV/base_test_july_evtnofix' # path where friend input is located; same "granularity as NTUP"
#FRIENDPATH  = '/coepp/cephfs/share/atlas/LFV/bdt_ff_v1' # path where friend input is located; same "granularity as NTUP"
FRIENDPATH  = '/coepp/cephfs/share/atlas/LFV/bdt_v3_ff_test' # path where friend input is located; same "granularity as NTUP"
JOBDIR      = "/coepp/cephfs/mel/%s/jobdir" % USER        # The Melb cloud is twisted and does not recognize home dirs...
prepare_path(JOBDIR)
INTARBALL   = os.path.join(JOBDIR,'histtarball_%s.tar.gz' % (time.strftime("d%d_m%m_y%Y_H%H_M%M_S%S")) )
AUTOBUILD   = True                                        # auto-build tarball using Makefile.tarball
NJMAX       = 100
DATATYPE    = sys.argv[1]

# outputs  
RUN         = 'NN_allregions_%s_%s' % (sys.argv[2], sys.argv[1])
OUTPATH     = "/coepp/cephfs/mel/%s/ztautau/%s"%(USER,RUN) # 

# running
QUEUE       = "long"                             # length of pbs queue (short, long, extralong )
SCRIPT      = "./ztautau/run/%s.plotter.py" % sys.argv[2]  # pyframe job script
BEXEC       = "Hist.sh"                          # exec script (probably dont change) 

DO_NOM      = False                               # submit the nominal job
DO_SYS      = True                              # submit the nominal job

TESTMODE    = False                              # submit only 1 sub-job (for testing)
NCORES      = 4

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
    global DO_SYS
    global TESTMODE

    ## get lists of samples
    all_mc   = samples.all_mc
    all_data = samples.all_data
    if DATATYPE == 'main':
        nominal  = all_data + all_mc 
        #nominal  = all_mc
    else:
        nominal  = all_data
    
    # the division b/w standard and tree systematics
    # is not essential here. Just to organise things
    # ["output folder name","sys path modifier","samples"]
    # The "sys path modifier" entry is passed as a different
    # argument for friend_sys and path_sys
    
    sys_list = []
    sys_list.append(sys_conf('MUON_ID_1down','sys1','sys1',all_mc))


    ## ensure output path exists
    prepare_path(OUTPATH)
    
    ## auto-build tarball
    if AUTOBUILD:
        print 'building input tarball %s...'% (INTARBALL)
        cmd = 'cd %s; make -f Makefile.hist TARBALL=%s' % (MAIN,INTARBALL)
        m = subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE)
        print m.communicate()[0]

    if DO_NOM: 
      submit('nominal',None,None,nominal)
    
    if DO_SYS:
      for conf in sys_list:
        submit(conf['name'],conf['main_path_mod'],conf['friend_path_mod'],conf['samples'],config={'sys':conf['name']})
    


def submit(job_name,job_sys_path,friend_sys_path,samps,config={}):
    """
    * construct config file 
    * prepare variable list to pass to job
    * submit job
    """
    global MAIN
    global USER
    global NTUP
    global FRIENDPATH
    global NJMAX
    global INTARBALL
    global AUTOBUILD
    global RUN
    global OUTPATH
    global QUEUE
    global SCRIPT
    global BEXEC
    global DO_NOM
    global DO_SYS
    global TESTMODE
    global DATATYPE
    
    assert (NJMAX<=600), "Error: please, not more than 600 subjobs per array!"

    ## construct config file
    ## ---------------------
    nsubjobs = 0
    nrun     = 1
    nlines   = 0
    f_dict   = {} 
    
    if job_sys_path: NTUP = "_".join([NTUP,job_sys_path])  

    outrootpath = os.path.abspath(os.path.join(OUTPATH,job_name))
    logrootpath = os.path.abspath(os.path.join(OUTPATH,'log_%s'%job_name))
    
    prepare_path(outrootpath)
    prepare_path(logrootpath)

    absintar   = os.path.abspath(INTARBALL)
   
    data_subdir = None
    mc_subdir = None 
    
    totsubjob = 0
    # not efficienct. Who cares?
    for s in samps:
      if s.type == "data":
        if not data_subdir: data_subdir = get_subdir( os.path.join(NTUP,'data') )
        in_data  = input_files(data_subdir,s,job_sys_path) 
        for infile in in_data: totsubjob += 1
      if s.type == "mc":
        if not mc_subdir: mc_subdir = get_subdir( os.path.join(NTUP,'mc') )
        in_mc  = input_files(mc_subdir,s,job_sys_path) 
        if not in_mc: continue # This is just temporary!!! Skip on non existing files
        for infile in in_mc: totsubjob += 1

    if FRIENDPATH:
       if friend_sys_path:  FRIENDPATH = "_".join([FRIENDPATH,friend_sys_path])  


    for s in samps:
        
        # configure output path 
        absoutpath = os.path.abspath(os.path.join(outrootpath,s.type,s.name))
        
        prepare_path(absoutpath)

        ## input & output
        #sinputs  = input_files(all_subdir,s,job_sys_path) # enable job_sys_path to take corr. input

        sinputs = []

        if s.type == "data":
          if not data_subdir: data_subdir = get_subdir( os.path.join(NTUP,'data') )
          sinputs  = input_files(data_subdir,s,job_sys_path) 
        if s.type == "mc":
          if not mc_subdir: mc_subdir = get_subdir( os.path.join(NTUP,'mc') )
          sinputs  = input_files(mc_subdir,s,job_sys_path) 
          if not sinputs: continue # This is just temporary!!! Skip on non existing files

        for infile in sinputs:
           soutput  = output_file(s,infile,job_sys_path) # replace job_sys_path with job_name
           
           if file_exists(absoutpath,soutput): continue
           
           ## config
           sconfig = {}
           sconfig.update(config)
           sconfig.update(s.config)
           sconfig_str = ",".join(["%s:%s"%(key,val) for key,val in sconfig.items()])
           
           # abspath of infile
           infpath = os.path.join(NTUP,s.type,infile)
           infpathfriend = ""
           
           if FRIENDPATH:
              infriend = infile.replace(NTUP,FRIENDPATH)+".friend"
           
           # write many lines here
           line = ';'.join([s.name,infpath,infriend,soutput,s.type,DATATYPE,sconfig_str])

           cfg = os.path.join(JOBDIR,'Config%s.%s.run.%s'%(RUN,job_name,nrun))
           abslogpath = os.path.abspath(os.path.join(logrootpath,"log_run_%d"%nrun))
           
           if not str(nrun) in f_dict.keys():
             """
             WIP
             if file_exists(JOBDIR,'Config%s.%s.run.%s'%(RUN,job_name,nrun)): 
               
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
             vars+=["CONFIG=%s"     % abscfg       ]
             vars+=["INTARBALL=%s"  % absintar     ]
             vars+=["OUTPATH=%s"    % outrootpath  ]
             vars+=["SCRIPT=%s"     % SCRIPT       ]
             vars+=["NCORES=%d"     % NCORES       ]
             
             VARS = ','.join(vars)
             
             cmd = 'qsub'
             cmd += ' -l nodes=1:ppn=%d'  % NCORES
             cmd += ' -q %s'              % QUEUE
             cmd += ' -v "%s"'            % VARS
             cmd += ' -N j.hist.%s'       % job_name
             cmd += ' -j oe -o %s/log'    % abslogpath
             cmd += ' -t1-%d'             % nlines
             cmd += ' %s'                 % BEXEC 
             print cmd
             
             #m = subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE)
             #print m.communicate()[0]

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



