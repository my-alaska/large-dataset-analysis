#!/bin/bash
# usage: sbatch pcba_dask.sh  

#SBATCH --job-name=molecular_fingerprints_pcba_dask
#SBATCH --time=01:00:00
#SBATCH --nodes=2
#SBATCH --ntasks-per-node=48
#SBATCH --cpus-per-task=1
#SBATCH -A plgfastdnns-cpu
#SBATCH -p plgrid
#SBATCH --mem=64GB
#SBATCH --output="fingerprints/pcba_dask/output_dask.out"
#SBATCH --error="fingerprints/pcba_dask/error_dask.err"

cd $SLURM_SUBMIT_DIR

module load python/3.10.4
source /net/people/plgrid/plgpiotrztych/venvs/fingerprints/bin/activate

module load openmpi
mpiexec python /net/people/plgrid/plgpiotrztych/fingerprints/pcba_dask/pcba_dask.py
