#!/bin/bash

#SBATCH --job-name=molecular_fingerprints_pcba
#SBATCH --time=00:10:00
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --cpus-per-task=48
#SBATCH -A plgfastdnns-cpu
#SBATCH -p plgrid
#SBATCH --mem=64GB
#SBATCH --output="~/fingerprints/pcba_dask/output_joblib.out"
#SBATCH --error="~/fingerprints/pcba_dask/error_joblib.err"

cd $SLURM_SUBMIT_DIR

module load python/3.10.4
source ~/venvs/fingerprints/bin/activate

python ~/fingerprints/pcba_dask/pcba_joblib.py

