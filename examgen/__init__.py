# Les jeux de données sont petits : plusieurs threads OpenMP se gênent (jusqu'à 300 fois plus lent).
import os

os.environ.setdefault("OMP_NUM_THREADS", "1")
try:
    from threadpoolctl import threadpool_limits

    threadpool_limits(1)
except ImportError:
    pass
