#!/bin/bash

#SBATCH --job-name=molecular_fingerprints_pcba_joblib_seq
#SBATCH --time=00:10:00
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --cpus-per-task=48
#SBATCH -A plgfastdnns-cpu
#SBATCH -p plgrid
#SBATCH --mem=64GB
#SBATCH --output="results/output_joblib_seq.out"
#SBATCH --error="results/error_joblib_seq.err"

cd $SLURM_SUBMIT_DIR

module load python/3.10.4
source ~/venvs/fingerprints/bin/activate

python ~/fingerprints/pcba_dask/pcba_joblib.py 1

