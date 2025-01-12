import logging
import sys
from time import time

from dask.system import CPU_COUNT
from skfp.datasets.moleculenet import load_pcba
from skfp.fingerprints import MAPFingerprint

import joblib
from dask.distributed import Client
from joblib import effective_n_jobs

from dask.distributed import LocalCluster

logging.getLogger('distributed').setLevel(logging.CRITICAL)
logging.getLogger('distributed.worker').setLevel(logging.CRITICAL)
logging.getLogger('distributed.scheduler').setLevel(logging.CRITICAL)
logging.getLogger('dask').setLevel(logging.CRITICAL)
logging.getLogger('dask.distributed').setLevel(logging.CRITICAL)

if __name__ == "__main__":
    if len(sys.argv) == 1:
        n_jobs_to_use = -1
    else:
        n_jobs_to_use = int(sys.argv[1])

    # Initial setup

    ### Load molecule strings
    print("Loading molecules")
    pcba_molecules = load_pcba()[0]

    # Processing molecules with joblib
    print("Compute map fingerprint with joblib")

    n_jobs = effective_n_jobs()
    print(f"Joblib effective n_jobs: {n_jobs}")
    print(f"Used n_jobs: {n_jobs_to_use if n_jobs_to_use > 0 else n_jobs}")

    ### Create fingerprint object
    print("Creating fingerprint object")
    fp = MAPFingerprint(n_jobs=n_jobs_to_use,sparse=True)

    ### Run computation
    print("Computing with joblib backend")
    start = time()
    fps_joblib = fp.transform(pcba_molecules)
    end = time()
    print(f"computation time {end-start:.5} s")

