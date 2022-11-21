import multiprocessing
import os
import sys
from pathlib import Path

num_process = os.environ.get('DOIT_NUM_PROCESS')
if num_process:
    num_process = int(num_process)
elif sys.platform in ('darwin', 'win32'):
    num_process = 0
else:
    num_process = multiprocessing.cpu_count()

DOIT_CONFIG = {'backend': 'sqlite3',
               # 'default_tasks': ['dist'],
               'verbosity': 2,
               'num_process': num_process}

pythonpath = os.environ.get('PYTHONPATH')
src_py_paths = [str(Path('src_django').resolve())]

sys.path += src_py_paths
os.environ['PYTHONPATH'] = os.pathsep.join(
    src_py_paths + ([pythonpath] if pythonpath else []))

from src_doit import *  # NOQA
