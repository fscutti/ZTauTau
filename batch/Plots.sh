# This is a sample PBS script. It will request 1 processor on 1 node
# for 1 hours.
#   
#   Request 4 processors on 1 node 
#   
#PBS -l nodes=1:ppn=4


#PBS -l walltime=8:00:00
#
#   Request 4 gigabyte of memory per process
#
#PBS -l pmem=1gb
#!/bin/bash
STARTTIME=`date +%s`
date

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

echo " VAR:       $VAR"
echo " REG:       $REG"
echo " LAB:       $LAB"
echo " ICUT:      $ICUT"
echo " MAKEPLOT:  $MAKEPLOT"
echo " INDIR:     $INDIR"
echo " BKGD:      $BKGD"
echo " OUTDIR:    $OUTDIR"
echo " SCRIPT:    $SCRIPT"
echo " INTARBALL: $INTARBALL"

echo 
export 

MYDIR=Plots_${RANDOM}${RANDOM}

#-------------------------------- NODE CONFIG ------------------------------
echo "going to tmp node dir: $TMPDIR"
cd $TMPDIR

#echo "ls ${TMPDIR} -la"
#ls ${TMPDIR} -la

echo "mkdir ${MYDIR}"
mkdir ${MYDIR}

#echo "ls ${TMPDIR} -la"
#ls ${TMPDIR} -la

echo "cd ${MYDIR}"
cd ${MYDIR}

setupATLAS
lsetup root

## copy over working area
echo "copying input tarball ${INTARBALL}..."
cp $INTARBALL .
date
ENDTIME=`date +%s`
TOTALTIME=$(($ENDTIME-$STARTTIME))
echo "Total Time: ${TOTALTIME}s"

echo "extracting input tarball..."
tar xvzf *.tar.gz 
#ls -alh

date
ENDTIME=`date +%s`
TOTALTIME=$(($ENDTIME-$STARTTIME))
echo "Total Time: ${TOTALTIME}s"
echo "done setting working area"

echo 
echo "setting up workarea..."
source setup.sh

cgcreate -a ${USER}:people -t ${USER}:people -g cpu,memory:user/${USER}/${PBS_JOBID}
MEMLIMIT="$((3 * 4))"
echo "${MEMLIMIT}g" > /cgroup/memory/user/${USER}/${PBS_JOBID}/memory.limit_in_bytes
echo $$ > /cgroup/memory/user/${USER}/${PBS_JOBID}/tasks

echo ""
echo "executing job..."
echo "python ${SCRIPT} --var=${VAR} --reg=${REG} --lab=${LAB} --icut=${ICUT} --makeplot=${MAKEPLOT} --input=${INDIR} --output=${OUTDIR} --background=${BKGD} --regiontype=${REGTYPE} --printcutflow=${PCW}"
python ${SCRIPT} --var=${VAR} --reg=${REG} --lab=${LAB} --icut=${ICUT}  --makeplot=${MAKEPLOT} --input=${INDIR} --output=${OUTDIR} --background=${BKGD} --regiontype=${REGTYPE} --printcutflow=${PCW}
echo "finished execution"

echo "copying output"
echo "listing"

echo "cp ./*.eps ${OUTDIR}"
cp ./*.eps ${OUTDIR}
echo "cp ./*.png ${OUTDIR}"
cp ./*.png ${OUTDIR}
echo "cp ./*.root ${OUTDIR}"
cp ./*.root ${OUTDIR}

echo "cd ${TMPDIR}"
cd ${TMPDIR}

#echo "ls ${TMPDIR} -la"
#ls ${TMPDIR} -la

echo "rm -rf ${MYDIR}"
rm -rf ${MYDIR}

#echo "ls ${TMPDIR} -la"
#ls ${TMPDIR} -la

echo "finished job"

date
ENDTIME=`date +%s`
TOTALTIME=$(($ENDTIME-$STARTTIME))
echo "Total Time: ${TOTALTIME}s"


