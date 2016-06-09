#!/usr/bin/env python
"""
condor.py

A python module for submitting condor jobs.  The user should use
the run function defined below.
"""

## std
import time
import os
import sys
import optparse
from glob import glob

## pyutils
import listutils
import pflock


path_of_this_file = os.path.abspath( __file__ )
dir_of_this_file = os.path.dirname( path_of_this_file )


#------------------------------------------------------------------------------
class Pool(object):

    #__________________________________________________________________________
    def __init__(self, n, **kw):
        self._n = n
        self._config = dict(kw)
        self._config.setdefault('universe', 'vanilla')
        self._config.setdefault('executable', '/bin/echo')
        self._config.setdefault('arguments', '')
        self._config.setdefault('output', 'stdout.log')
        self._config.setdefault('error', 'stdout.log')
        self._config.setdefault('getenv', 'True')
        self._config.setdefault('should_transfer_files', 'YES')
        self._config.setdefault('when_to_transfer_output', 'ON_EXIT_OR_EVICT')
    
    #__________________________________________________________________________
    def write_job_config(self, args, dirname, filename):
        assert len(args) == self._n, 'len(args) = %s,  self._n = %s' % (len(args), self._n)

        tmp = dict(self._config)
        tmp['time'] = time.ctime()
        tmp['user'] = os.environ['USER']
        template = """# condor config file
#
# %(filename)s
# %(time)s
# user: %(user)s
# generated by pyutils/condor.py
# see also: https://asrv-02.hep.upenn.edu/groups/pennatlastier3users/
#           http://www.cs.wisc.edu/condor/manual/
#------------------------------------------------------------------------------

#Use only the vanilla universe
universe = %(universe)s

# This is the executable to run.  If a script,
#   be sure to mark it #!<path to interp> on the first line
executable = %(executable)s

# This is the argument line to the Executable
arguments = %(arguments)s

# Filename for stdout, otherwise it is lost
output = %(output)s
error = %(error)s

# Copy the submittor's environment variables.  Usually required.
getenv = %(getenv)s

# Copy output files when done.  REQUIRED to run in a protected directory
should_transfer_files = %(should_transfer_files)s
when_to_transfer_output = %(when_to_transfer_output)s

# job queue (n = %(n)s)
#------------------------------------------------------------------------------
%(queue)s
#------------------------------------------------------------------------------
# EOF
"""
        queue = ''
        basedir = os.getcwd()
        for i in xrange(self._n):
            initialdir = os.path.join(basedir, dirname, 'job_%03i' % i)
            if not os.path.isdir(initialdir):
                print 'condor.py>  mkdir -p %s' % initialdir
                os.system('mkdir -p %s' % initialdir)
            queue += '# job %i\n' % i
            queue += 'initialdir = %s\n' % initialdir
            queue += 'arguments = %s\n' % args[i]
            queue += 'queue\n'
            queue += '\n'

        tmp['queue'] = queue
        tmp['filename'] = filename
        tmp['n'] = self._n

        f = open(filename, 'w')
        f.write(template % tmp)
        f.close()

    #__________________________________________________________________________
    def map(self, args, dirname='test'):
        filename = '%s/condor.job' % dirname
        self.write_job_config(args, dirname, filename)
        print 'condor.py>  condor_submit %s' % filename
        os.system('condor_submit %s' % filename)

# end of Pool class definition


#------------------------------------------------------------------------------
# free functions
#------------------------------------------------------------------------------

#______________________________________________________________________________
def run(exe, arg_template, input, dirname='condor_test', n_files=0, n_jobs=0,
       comma_sep_input=False, do_file_transfer=False):
    """
    exe: The name of the executable to be run.  Probably best to give
         the full path like '/home/user/my_job'
    arg_template: Should be the arguments given after the executable
         with a %s in place of where the input files will be given
         as a comma-separated list.
    input: a list of the input files to be divided among jobs.
    dirname: the name of the working directory for the condor job to
         create and run in.
    n_files: the number of files per sub-job.
    n_jobs: the number of sub-jobs.
    """

    # glob paths
    input_files = []
    for fn in input:
        if fn.count('*'):
            input_files.extend( glob(fn) )
        else:
            input_files.append(fn)

    assert input_files

    # divide input files
    if n_files:
        divided_files = [ x for x in listutils.chunk(input_files, n_files) ]
    elif n_jobs:
        divided_files = [ x for x in listutils.divide(input_files, n_jobs) ]
    else:
        divided_files = [ x for x in listutils.chunk(input_files, 1) ]

    divided_files = filter(None, divided_files)
    if n_jobs and n_jobs != len(divided_files):
        print 'condor.py>  There are only %s files for %s jobs.' % (len(divided_files), n_jobs)
        print 'condor.py>  Changing n_jobs = %s jobs.' % (len(divided_files))

    # make args list
    if do_file_transfer:
        args = []
        for files in divided_files:
            formatted_files = ','.join(files)
            additional_args = ''
            if comma_sep_input:
                additional_args += '--comma-sep-input'
            args.append( '"--script=%s --arg_template=\'%s\' --files=%s %s"' % (exe, arg_template, formatted_files, additional_args) )
        exe = os.path.join(dir_of_this_file, 'condor.py')
    
    else:
        if comma_sep_input:
            args = [ arg_template % (','.join(files)) for files in divided_files ]
        else:
            args = [ arg_template % (' '.join(files)) for files in divided_files ]
    

    # run
    pool = Pool(len(args), executable=exe)
    return pool.map(args, dirname=dirname)


#______________________________________________________________________________
def transform_file_name_for_xrdcp(s):
    t = s.replace('/xrootd/srm/', 'root://hn.at3f//srm/')
    t = t.replace('/xrootd/atlasC/', 'root://hn.at3f//atlasC/')
    return t


#______________________________________________________________________________
def transform_file_name_output(s):
    dir_name = os.path.basename(os.path.dirname(s)) # get name of deepest sub-dir
    file_name = os.path.basename(s)
    return '%s_%s'  % (dir_name, file_name)


#______________________________________________________________________________
def check_for_missing(haves, wants):
    return [item for item in wants if not item in haves]


#______________________________________________________________________________
def file_transfer_main():
    print 'condor.py>  -------  Using pyutils/condor.file_transfer_main()  -------'
    sys.stdout.flush()
    
    parser = optparse.OptionParser(description="file_transfer_main")
    parser.add_option('--script',            dest='script',            default=None,      help='path to script')
    parser.add_option('--files',             dest='files',             default='',        help='comma separated list of files to transfer')
    parser.add_option('--output',            dest='output',            default=None,      help='location of output - only give if on /xrootd')
    parser.add_option('--arg_template',      dest='arg_template',      default='%s',      help='template for arguments with a %s where the comma-seperated input should go')
    parser.add_option('--comma-sep-input', dest='comma_sep_input', default=False, action='store_true',   help='comma seperate input files when call script?')
    parser.add_option('--no-transfer-input', dest='no_transfer_input', default=False, action='store_true',   help='Do not transfer input')
    options, args = parser.parse_args()
    if options.script is None :
        print 'condor.py>  Use --script to provide the full path to the script'
        sys.exit(-1)

    script_files = []
    if options.no_transfer_input :
        script_files = options.files.split(',')
    else :
        print 'condor.py>  copying input files with xrdcp...'
        sys.stdout.flush()
        file_names_to_copy = options.files.split(',')

        ## build dict storing info for each file to be transferred
        file_info_dict = dict()
        for fn in file_names_to_copy:
            # (in_name, out_name, n_tries)
            file_info_dict[fn] = (transform_file_name_for_xrdcp(fn), transform_file_name_output(fn), 0)

        ## read files location from first file
        ## config is location-dependent
        assert len(file_names_to_copy) > 0, 'No files to copy.'
        if file_names_to_copy[0].startswith('/xrootd/'):
            qpath = '/disk/userdata00/atlas_data2/rreece/pflock/xrdcp'
            cp = 'xrdcp'
            n_slots = 2
        else:
            qpath = '/disk/userdata00/atlas_data2/rreece/pflock/cp_disk'
            cp = 'cp'
            n_slots = 2
        
        ## wait for slot
        print 'condor.py>  waiting for slot...'
        sys.stdout.flush()
        i_slot, n_simult = pflock.wait_for_slot(qpath, n_slots)
        
        ## use xrdcp to copy files locally to the worker
        while file_names_to_copy:
            file_name = file_names_to_copy[0]
            in_name, out_name, n_tries = file_info_dict[file_name]

            ## increment n_tries
            n_tries += 1
            file_info_dict[file_name] = in_name, out_name, n_tries

            ## do copies
            print 'n_tries = ', n_tries, ', i_slot = ', i_slot, ', n_simult = ', n_simult
            sys.stdout.flush()
            cmd = '%s %s %s' % (cp, in_name, out_name)
            print 'condor.py>  %s' % cmd
            sys.stdout.flush()
            os.system(cmd)

            ## check for missing files
            files_we_have = glob('*')
            if out_name in files_we_have:
                print 'condor.py>  copied successfully.'
                file_names_to_copy.remove(file_name)
                script_files.append(out_name)

            sys.stdout.flush()

        ## release slot
        pflock.release_slot(qpath, i_slot)

        print 'condor.py>  ls -GAFlh'
        print 'condor.py>  -----------------------------------------------------------'
        sys.stdout.flush()
        os.system('ls -GAFlh')
        print ''

    print 'condor.py>  script: %s' % options.script
    print 'condor.py>  arg_template: %s' % options.arg_template
    print 'condor.py>  running your program...'
    if options.comma_sep_input:
        script_args = options.arg_template % (','.join(script_files))
    else:
        script_args = options.arg_template % (' '.join(script_files))
    cmd = '%s %s' % (options.script, script_args)
    print 'condor.py>  %s' % cmd
    sys.stdout.flush()
    os.system(cmd)
    sys.stdout.flush()
    print 'condor.py>  your program finished.'

    if not options.no_transfer_input :
        print 'condor.py>  removing local input files...'
        for f in script_files :
            cmd = 'rm %s' % f
            print 'condor.py>  %s' % cmd
            sys.stdout.flush()
            os.system(cmd)

    if options.output is not None :
        print 'condor.py>  copying your output with xrdcp...'
        for f in os.listdir('.') :
            cmd = 'xrdcp %s %s' % (f, options.output)
            print 'condor.py>  %s' % cmd
            sys.stdout.flush()
            os.system(cmd)

    print 'condor.py>  ls -GAFlh'
    print 'condor.py>  -----------------------------------------------------------'
    sys.stdout.flush()
    os.system('ls -GAFlh')
    print ''
    print 'condor.py>  done.'
    

#______________________________________________________________________________
if __name__ == '__main__': file_transfer_main()


