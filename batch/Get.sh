#!/bin/bash

# This is a sample PBS script. 
# It will request 1 processor 
# on 1 node for 1 hours.

#PBS -S /bin/bash

# ------------------------------  
# Request 1 processors on 1 node 
# ------------------------------ 
#PBS -l nodes=1:ppn=1
#PBS -m n

# --------  
# Walltime
# --------
#PBS -l walltime=24:00:00

# ----------------------------------------
# Request 1 gigabyte of memory per process
# ----------------------------------------
#PBS -l pmem=1gb


STARTTIME=`date +%s`
date

echo 
echo "Environment variables..."
echo " User name:     $USER"
echo " User home:     $HOME"
echo " Queue name:    $PBS_O_QUEUE"
echo " Job name:      $PBS_JOBNAME"
echo " Job-id:        $PBS_JOBID"
echo " Work dir:      $PBS_O_WORKDIR"
echo " Submit host:   $PBS_O_HOST"
echo " Worker node:   $HOSTNAME"
echo " Temp dir:      $TMPDIR"
echo " parameters passed: $*"
echo 

echo " SCRIPT:        $SCRIPT"
echo " HISTFILE:      $HISTFILE"
echo " MERGEDHIST:    $MERGEDHIST"
echo " OUTHIST:       $OUTHIST"
echo " OUTMERGED:     $OUTMERGED"

echo
export 

MYDIR=Get_${RANDOM}${RANDOM}

# ----------------
# This is the job!
# ----------------

export X509_USER_PROXY=/data/${USER}/jobdir/x509up_u1132
setupATLAS
lsetup rucio
lsetup root

echo ""
echo "executing job..."

echo "-----> ls ${TMPDIR} -la"
ls ${TMPDIR} -la

echo "-----> rm -rf ${MYDIR}"
rm -rf ${MYDIR}

#echo "-----> rm -rf *.root"
#rm -rf *.root

echo "-----> ls ${TMPDIR} -la"
ls ${TMPDIR} -la

echo "-----> mkdir ${TMPDIR}/${MYDIR} "
mkdir ${TMPDIR}/${MYDIR} 

echo "-----> ls ${TMPDIR} -la"
ls ${TMPDIR} -la


# ----------------------------
# download and merge tree file
# ----------------------------
echo "-----> rucio download --dir=${TMPDIR}/${MYDIR} ${HISTFILE}"
rucio download --dir=${TMPDIR}/${MYDIR} ${HISTFILE}

echo "-----> ls ${TMPDIR}/${MYDIR}/${HISTFILE} -la"
ls ${TMPDIR}/${MYDIR}/${HISTFILE} -la

echo "-----> cp -rf ${TMPDIR}/${MYDIR}/${HISTFILE} ${OUTHIST}"
cp -rf ${TMPDIR}/${MYDIR}/${HISTFILE} ${OUTHIST}

echo "-----> cd ${TMPDIR}/${MYDIR}/${HISTFILE}"
cd ${TMPDIR}/${MYDIR}/${HISTFILE}

echo "-----> hadd ${MERGEDHIST} *.root*"
hadd ${MERGEDHIST} *.root*

echo "-----> cp ${MERGEDHIST} ${TMPDIR}/${MYDIR}"
cp ${MERGEDHIST} ${TMPDIR}/${MYDIR}

echo "-----> cd ${TMPDIR}/${MYDIR}"
cd ${TMPDIR}/${MYDIR}

echo "-----> ls ${TMPDIR}/${MYDIR} -la"
ls ${TMPDIR}/${MYDIR} -la



# ----------------------------------
# copy output locally and clean area
# ----------------------------------
echo "-----> cp ${MERGEDHIST} ${OUTMERGED}"
cp ${MERGEDHIST} ${OUTMERGED}

echo "-----> cd ${TMPDIR}"
cd ${TMPDIR}

echo "-----> rm -rf ${MYDIR}"
rm -rf ${MYDIR}

#echo "-----> rm -rf *.root"
#rm -rf *.root

echo "-----> ls ${TMPDIR} -la"
ls ${TMPDIR} -la

# EOF

