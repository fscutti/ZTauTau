# This is a sample PBS script. It will request 1 processor on 1 node
# for 4 hours.
#   
#   Request 1 processors on 1 node 
#   
#PBS -l nodes=1:ppn=1


#
#   Request 4 gigabyte of memory per process
#
#PBS -l pmem=1gb
#!/bin/bash
STARTTIME=`date +%s`
date
env

#-------------------------------- ENV VARS -------------------------------
echo 
echo "Environment variables..."
echo " User name:   $USER"
echo " User home:   $HOME"
echo " Queue name:  $PBS_O_QUEUE"
echo " Job name:    $PBS_JOBNAME"
echo " Job-id:      $PBS_JOBID"
echo " Task-id:     $PBS_ARRAYID"
echo " Work dir:    $PBS_O_WORKDIR"
echo " Submit host: $PBS_O_HOST"
echo " Worker node: $HOSTNAME"
echo " Temp dir:    $TMPDIR"
echo " parameters passed: $*"
echo 

echo " SCRIPT:      $SCRIPT"
echo " OUTFILE:     $OUTFILE"
echo " OUTPATH:     $OUTPATH"
echo " CONFIG:      $CONFIG"
echo " INTARBALL:   $INTARBALL"

echo
export 

MYDIR=Hist_${RANDOM}${RANDOM}

#-------------------------------- NODE CONFIG ------------------------------
echo "going to tmp node dir: $TMPDIR"
cd $TMPDIR

echo "ls ${TMPDIR} -la"
ls ${TMPDIR} -la

echo "mkdir ${MYDIR}"
mkdir ${MYDIR}

echo "ls ${TMPDIR} -la"
ls ${TMPDIR} -la

echo "cd ${MYDIR}"
cd ${MYDIR}

setupATLAS
lsetup root

## copy over working area
##echo "ls /data/fscutti"
##ls /data/fscutti

## copy over working area
echo "copying input tarball ${INTARBALL}..."
cp $INTARBALL .
date
ENDTIME=`date +%s`
TOTALTIME=$(($ENDTIME-$STARTTIME))
echo "Total Time: ${TOTALTIME}s"
echo "extracting input tarball..."
tar xzf *.tar.gz
date
ENDTIME=`date +%s`
TOTALTIME=$(($ENDTIME-$STARTTIME))
echo "Total Time: ${TOTALTIME}s"
echo "done setting working area"
ls -alh 

echo 
echo "setting up workarea..."
source setup.sh

echo 
echo "reading in config file '${CONFIG}', line ${PBS_ARRAYID}"
## READ IN CONFIG
line=`sed -n -e ${PBS_ARRAYID}p ${CONFIG}`
echo ${line}
arrIN=(${line//;/ });
SAMPLE=${arrIN[0]}
INPUT=${arrIN[1]}
SAMPLETYPE=${arrIN[2]}
CFG=${arrIN[3]}
echo "SAMPLE:     ${SAMPLE}"
echo "SAMPLETYPE: ${SAMPLETYPE}"
echo "INPUT:      ${INPUT}"
echo "CFG:        ${CFG}"


echo
echo "copying input locally..."
TMPINPUT="`mktemp ntuple.XXXXXXX`.root"
echo cp ${INPUT} ${TMPINPUT}
cp ${INPUT} ${TMPINPUT}


echo ""
echo "executing job..."
echo ${SCRIPT} --input ${TMPINPUT} --sampletype ${SAMPLETYPE} --config "${CFG}"
${SCRIPT} --input ${TMPINPUT} --sampletype ${SAMPLETYPE} --config "${CFG}"

ls -alh

echo "finished execution"

echo 
echo "preparing output dir..."
if [ ! -d ${OUTPATH} ]; then mkdir ${OUTPATH}; fi

echo "copying output"
echo cp ${OUTFILE} ${OUTPATH}/${SAMPLE}.root 
cp ${OUTFILE} ${OUTPATH}/${SAMPLE}.root
chmod a+r ${OUTPATH}/${SAMPLE}.root

echo "cd ${TMPDIR}"
cd ${TMPDIR}

echo "ls ${TMPDIR} -la"
ls ${TMPDIR} -la

echo "rm -rf ${MYDIR}"
rm -rf ${MYDIR}

echo "ls ${TMPDIR} -la"
ls ${TMPDIR} -la

echo "finished job"

date
ENDTIME=`date +%s`
TOTALTIME=$(($ENDTIME-$STARTTIME))
echo "Total Time: ${TOTALTIME}s"







