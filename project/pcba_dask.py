import logging
from time import time
import sys

from mpi4py import MPI

from dask.system import cpu_count
from skfp.datasets.moleculenet import load_pcba
from skfp.fingerprints import MAPFingerprint

import joblib
from dask.distributed import Client

from dask_mpi import initialize

logging.getLogger('distributed').setLevel(logging.CRITICAL)
logging.getLogger('distributed.worker').setLevel(logging.CRITICAL)
logging.getLogger('distributed.scheduler').setLevel(logging.CRITICAL)
logging.getLogger('dask').setLevel(logging.CRITICAL)
logging.getLogger('dask.distributed').setLevel(logging.CRITICAL)

if __name__ == "__main__":
    # Initial setup
    initialize()

    print("initialized dask mpi")
    sys.stdout.flush()

    ### Load molecule strings
    print("Loading molecules")
    pcba_molecules = load_pcba()[0]

    # Processing molecules with Dask
    print("Compute map fingerprint with dask")
    sys.stdout.flush()

    ### Create dask client
    print("Creating Dask client")
    sys.stdout.flush()
    client = Client()

    print(f"Dask client n_threads: {len(client.nthreads())}")
    sys.stdout.flush()

    ### Run computation
    with joblib.parallel_config("dask"):
        print("Creating fingerprint object")
        sys.stdout.flush()
        fp = MAPFingerprint(n_jobs=-1,sparse=True)

        print("Computing with dask backend")
        sys.stdout.flush()
        start = time()
        fps_dask = fp.transform(pcba_molecules)
        end = time()

        print(f"computation time {end - start:.5} s")
        sys.stdout.flush()

        del fps_dask

    # Closing client and cluster
    print("Closing Dask client")
    sys.stdout.flush()

    client.close()

