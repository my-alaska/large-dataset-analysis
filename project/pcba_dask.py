import logging
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
    # Initial setup

    n_jobs = effective_n_jobs()
    print(f"Joblib effective n_jobs: {n_jobs}")

    ### Load molecule strings
    print("Loading molecules")
    pcba_molecules = load_pcba()[0]

    # Processing molecules with joblib
    print("Compute map fingerprint with joblib")

    ### Create fingerprint object
    print("Creating fingerprint object")
    fp = MAPFingerprint(n_jobs=-1,sparse=True)

    ### Run computation
    print("Computing with joblib backend")
    start = time()
    fps_joblib = fp.transform(pcba_molecules)
    end = time()
    print(f"computation time {end-start:.5} s")

    del fps_joblib

    # Processing molecules with Dask
    print("Compute map fingerprint with dask")

    ### Create local cluster
    print("Creating Dask cluster")
    cluster = LocalCluster(threads_per_worker=1)

    print(f"Dask cpu count: {CPU_COUNT}")

    print(f"Dask cluster scheduler address {cluster.scheduler_address}")

    ### Create dask client
    print("Creating Dask client")
    client = Client(cluster.scheduler_address)

    ### Run computation
    with joblib.parallel_config("dask"):
        print("Creating fingerprint object")
        fp = MAPFingerprint(n_jobs=-1,sparse=True)

        print("Computing with joblib backend")
        start = time()
        fps_dask = fp.transform(pcba_molecules)
        end = time()
        print(f"computation time {end - start:.5} s")

        del fps_dask

    # Closing client and cluster
    print("Closing Dask client")
    client.close()
    print("Closing Dask cluster")
    cluster.close()
