# encoding: utf-8
'''
SubmitHist.py

quick start:
Go to the Global Variable config below, setup specifics for your analysis, 
and launch - should be pretty straight forward. 


description:
Batch submission script for the pyframe analysis.  One
 job is made for each systematic config (eg. nominal, TES_UP, etc...):
    j.plot.nominal[XXX]
    j.plot.TES_UP[XXX]
    ...

The job is split into one sub-job per output sample (so there can be 100s of
subjobs). Since each sub-job runs over a different sample and may have
different setup configurations, the config for the job is stored in a config
file that contains one-line per sub-job. Each line contains 4 entries delimited
by the ';' character: 
    <sample name>;<input file>;<sample type>;<config>

An example config file might look like this: 
    periodL;/lustre/atlas/group/higgs/TauTauHadHad//full/_p1443_v00-02-08_merged/nominal/periodL.root;data;
    Ztautau;/lustre/atlas/group/higgs/TauTauHadHad//full/_p1443_v00-02-08_merged/nominal/Ztautau.root;mc;
    DYtautau_180M250;/lustre/atlas/group/higgs/TauTauHadHad//full/_p1443_v00-02-08_merged/nominal/DYtautau_180M250.root;mc;
    Zprime2000tautau_DYtautau_180M250;/lustre/atlas/group/higgs/TauTauHadHad//full/_p1443_v00-02-08_merged/nominal/DYtautau_180M250.root;mc;ZPNOSM:2000
    Zprime2000tautau_DYtautau_250M400;/lustre/atlas/group/higgs/TauTauHadHad//full/_p1443_v00-02-08_merged/nominal/DYtautau_250M400.root;mc;ZPNOSM:2000
    ...

The line number in the config file corresponds to the PBS subjob index, so the
line is extracted from the config file in the .exec.sh script, and decoded
to setup the job.


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
#NTUP='/coepp/cephfs/mel/fscutti/ztautau/v03/merged' 
NTUP='/coepp/cephfs/mel/laram1/v19/2016'
#NTUP='/coepp/cephfs/mel/laram1/v17'

# The Melb cloud is twisted and does not recognize home dirs...
#JOBDIR = "/data/%s/jobdir" % USER 
JOBDIR = "/coepp/cephfs/mel/%s/jobdir" % USER 
INTARBALL = os.path.join(JOBDIR,'histtarball_%s.tar.gz' % (time.strftime("d%d_m%m_y%Y_H%H_M%M_S%S")) )


# auto-build tarball using Makefile.tarball
AUTOBUILD = True                

# outputs

RUN = 'HIST_1809_Wjets_estimation_new_the_broken_ones'
#RUN = 'HistECHIDNA_missingdata_onemore'

#OUTPATH="/data/%s/ztautau/%s"%(USER,RUN) # 
OUTPATH="/coepp/cephfs/mel/%s/ztautau/%s"%(USER,RUN) # 
OUTFILE="ntuple.root"         # file output by pyframe job 

# running
QUEUE="long"                         # length of pbs queue (short, long, extralong )
SCRIPT="./ztautau/run/j.plotter.py"  # pyframe job script
BEXEC="Hist.sh"                      # exec script (probably dont change) 
DO_NOM = True                        # submit the nominal job
DO_SYS = True                  # submit the NTUP systematics jobs
TESTMODE = False                     # submit only 1 sub-job (for testing)


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
    global OUTFILE
    global QUEUE
    global SCRIPT
    global BEXEC
    global DO_NOM
    global DO_SYS
    global TESTMODE

    ## get lists of samples
    all_mc   = samples.all_mc
    all_data = samples.all_data
    nominal  = all_data + all_mc 

    all_sys = [
	
	#['MUSF_STAT_UP',                  all_mc],
        #['MUSF_STAT_DN',                  all_mc],
	#['TAUSF_SYS_UP',                  all_mc],
        #['TAUSF_SYS_DN',                  all_mc],
	#['MUSF_SYS_UP',                  all_mc],
        #['MUSF_SYS_DN',                  all_mc],
	#['MUMS_UP',                  all_mc],
	#['MUMS_DN',                  all_mc],
	#['MUSCALE_UP',                  all_mc],
	#['MUSCALE_DN',                  all_mc],
	#['MUID_UP',                  all_mc],
	#['MUID_DN',                  all_mc],
	['METSCALE_UP',                  all_mc],
	['METSCALE_DN',                  all_mc],
	['METResoPara',			 all_mc],
	#['METResoPerp', 		 all_mc],
 	['PILEUP_UP', 			all_mc],
        ['PILEUP_DN',                   all_mc],	
        ]    
    
    ## ensure output path exists
    prepare_path(OUTPATH)
    
    ## auto-build tarball
    if AUTOBUILD:
        print 'building input tarball %s...'% (INTARBALL)
        cmd = 'cd %s; make -f Makefile.hist TARBALL=%s' % (MAIN,INTARBALL)
        m = subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE)
        print m.communicate()[0]

    if DO_NOM: submit('nominal','nominal',nominal)
    
    if DO_SYS:  
      for sys,samps in all_sys:
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
    global OUTFILE
    global QUEUE
    global SCRIPT
    global BEXEC
    global DO_NOM
    global DO_SYS
    global TESTMODE

    ## construct config file
    cfg = os.path.join(JOBDIR,'ConfigHistZtautau.%s'%tag)
    f = open(cfg,'w')
    for s in samps:

        ## input
        sinput = input_file(s,job_sys) 

        ## sample type
        stype  = s.type

        ## config
        sconfig = {}
        sconfig.update(config)
        sconfig.update(s.config)
        sconfig_str = ",".join(["%s:%s"%(key,val) for key,val in sconfig.items()])

        line = ';'.join([s.name,sinput,stype,sconfig_str])
        f.write('%s\n'%line) 

    f.close()

    abscfg     = os.path.abspath(cfg)
    absintar   = os.path.abspath(INTARBALL)
    absoutpath = os.path.abspath(os.path.join(OUTPATH,tag))
    abslogpath = os.path.abspath(os.path.join(OUTPATH,'log_%s'%tag))
    nsubjobs   = len(samps)
    if TESTMODE: nsubjobs = 1

    prepare_path(absoutpath)
    prepare_path(abslogpath)

    vars=[]
    vars+=["CONFIG=%s" % abscfg]
    vars+=["INTARBALL=%s" % absintar]
    vars+=["OUTFILE=%s" % OUTFILE]
    vars+=["OUTPATH=%s" % absoutpath]
    vars+=["SCRIPT=%s" % SCRIPT]
     
    VARS = ','.join(vars)

    cmd = 'qsub'
    cmd += " -q %s" % QUEUE
    cmd += ' -v "%s"' % VARS
    cmd += ' -N j.hist.%s' % (tag)
    cmd += ' -j oe -o %s/log' % (abslogpath)
    cmd += ' -t1-%d' % (nsubjobs)
    cmd += ' %s' % BEXEC
    print cmd
    m = subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE)
    print m.communicate()[0]

def prepare_path(path):
    if not os.path.exists(path):
        print 'preparing outpath: %s'%(path)
        os.makedirs(path)

def input_file(sample,sys):
    global NTUP
    sinput = sample.name
    
    #if sys!='nominal': sys='sys_'+sys
    sinput += '.root'
    #sinput = os.path.join(NTUP,sys,sinput) 
    sinput = os.path.join(NTUP,'nominal',sinput) 
    return sinput

if __name__=='__main__': main()


## EOF
