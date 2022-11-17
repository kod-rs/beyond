import subprocess
import sys
from pathlib import Path

from . import docs
from .docs import *  # NOQA

__all__ = ['task_test',
           *docs.__all__]

current_dir = Path(__file__).resolve().parent
root_dir = current_dir.parent
django_dir = root_dir / 'src_django'
test_dir = root_dir / 'api' / 'tests'
test_python_package = 'src_django.api.tests'


def task_test():
    """Test - run pytest tests"""

    def run(*args):
        args = [f'{test_python_package}.{arg}' if '-' not in arg
                else arg
                for arg in args]

        subprocess.run([sys.executable, 'manage.py', 'test', *args],
                       cwd=str(root_dir),
                       check=True)

    return {'actions': [lambda args: run(*(args or []))],
            'pos_arg': 'args'}
