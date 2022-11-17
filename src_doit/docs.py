import subprocess
import sys
from pathlib import Path

from hat.doit import common
from hat.doit.docs import (SphinxOutputType,
                           build_sphinx)

__all__ = ['task_docs',
           'task_docs_dev',
           'task_docs_django']

current_dir = Path(__file__).resolve().parent
root_dir = current_dir.parent

docs_dir = root_dir / 'docs'
dst_docs_dir = root_dir / 'build' / 'docs'
django_dst_dir = dst_docs_dir / 'dev' / 'django'


def task_docs():
    """Docs - build documentation"""
    return {'actions': None,
            'task_dep': ['docs_dev']}


def task_docs_dev():
    """Docs - build developer documentation"""

    def build():
        # build_sphinx(src_dir=docs_dir / 'dev',
        #              dst_dir=dst_docs_dir / 'dev',
        #              project='Flexopt backend documentation',
        #              out_type=SphinxOutputType.HTML,
        #              extensions=['sphinx.ext.autodoc',
        #                          'sphinx.ext.napoleon',
        #                          'sphinx.ext.todo',
        #                          'sphinxcontrib.drawio',
        #                          'sphinxcontrib.programoutput'],
        #              version_path=Path('VERSION'),
        #              copyright='2022-2023, Koncar Digital')
        pass

    return {'actions': [build],
            'task_dep': ['docs_django']}


def task_docs_django():
    """Docs - build django documentation"""

    def build():
        # common.mkdir_p(django_dst_dir.parent)
        # subprocess.run([sys.executable, '-m', 'pdoc',
        #                '--html', '--skip-errors', '-f',
        #                '-o', str(django_dst_dir),
        #                'src_django'],
        #               stdout=subprocess.DEVNULL,
        #               stderr=subprocess.DEVNULL,
        #               check=True)
        pass

    return {'actions': [build]}
