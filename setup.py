from setuptools import find_packages, setup

setup(
    name='PyLCU',
    packages=find_packages(),
    version='0.1.0',
    description='A Python wrapper for the League of Legends Client (LCU)',
    author='Fletcher Henneman',
    license='MIT',
)

#python setup.py bdist_wheel
#pip install /path/to/wheelfile.whl
#import pylcu