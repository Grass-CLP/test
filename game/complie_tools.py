#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# created by Lipson on 11/5/18.
# email to LipsonChan@yahoo.com
#

import os
import shutil
import sys
import subprocess

from distutils.core import run_setup


def recur_files(path, file_func, suffixes, exclude=None):
    suffixes = [suffixes] if isinstance(suffixes, str) else suffixes
    exclude = [] if exclude is None else [exclude] if isinstance(exclude, str) else exclude

    for root, dirs, files in os.walk(path):
        for f in files:  # type: str
            suffix_i = f.rfind('.')
            suffix = f[suffix_i + 1:]

            if f in exclude or suffix not in suffixes:
                continue

            file_func(os.path.join(root, f))


def build(module_old, build_dir="build", temp_dir="temp", exclude_file=["__init__.py"]):
    os.system("mkdir -p {}".format(build_dir))
    all_pys = list()

    def add_file(f):
        all_pys.append(f)

    module_name = os.path.split(module_old)[-1]
    module_path = os.path.join(build_dir, module_name)
    shutil.rmtree(module_path, ignore_errors=True)
    shutil.copytree(module_old, module_path)
    recur_files(module_path, add_file, 'py', exclude=exclude_file)

    setup_script = "from distutils.core import setup\n" \
                   "from Cython.Build import cythonize\n" \
                   "setup(ext_modules=cythonize({}, nthreads=8))".format(all_pys)
    setup_file = os.path.join(module_path, 'setup.py')
    with open(setup_file, 'w') as f:
        f.write(setup_script)
    run_setup(setup_file, ['build_ext', '--build-lib', build_dir, '--build-temp', temp_dir])
    # subprocess.call(['python', setup_file, 'build_ext', '--build-lib', build_dir, '--build-temp', temp_dir])
    recur_files(module_path, os.remove, ['c', 'py', 'pyc'], exclude=exclude_file)
    # shutil.rmtree(temp_dir, ignore_errors=True)
    pass


if __name__ == "__main__":
    list_module = sys.argv[1:]
    for mod in list_module:
        print("======= build module: {} ========".format(mod))
        build(mod)
