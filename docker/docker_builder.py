import os
import sys
from distutils.dir_util import copy_tree
from pathlib import Path
from shutil import copyfile, rmtree


def copy_dir(src, dst, dir_name):
    copy_tree(str(src / dir_name), str(dst / dir_name))


def copy_file(src, dst, file_name):
    copyfile(str(src / file_name), str(dst / file_name))


def rm_dir(dst, dir_name):
    rmtree(str(dst / dir_name))


def rm_file(dst, file_name):
    os.remove(str(dst / file_name))


def copy_to_backend(parent_dir):
    src = parent_dir.parent
    dst = parent_dir / 'backend'

    copy_dir(src, dst, 'src_django')
    copy_dir(src, dst, 'schemas')
    copy_file(src, dst, 'manage.py')
    copy_file(src, dst, 'requirements.pip.txt')
    copy_file(src, dst, '.env')


def copy_to_frontend(parent_dir):
    src = parent_dir.parent
    dst = parent_dir / 'frontend'

    copy_dir(src, dst, 'src_front')

    dst = dst / 'src_front'
    rm_dir(dst, '.vs')
    rm_dir(dst, 'node_modules')
    rm_file(dst, 'package-lock.json')


def main():
    parent_dir = Path(__file__).resolve().parent
    print('Copying backend files...')
    copy_to_backend(parent_dir)
    print('Copying frontend files...')
    copy_to_frontend(parent_dir)
    print('Copying done.')


if __name__ == '__main__':
    sys.exit(main())
