#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import find_packages, setup
from codecs import open
from os import path


HERE = path.abspath(path.dirname(__file__))
with open(path.join(HERE, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()


try:
    with open(path.join(HERE, 'requirements.txt'), encoding='utf-8') as f:
        REQUIRED = f.read().split('\n')
except:
    REQUIRED = []

def setup_package():
    setup(
        name='kit-vision',
#        packages=find_packages(include=['kit-vision']),
        version='0.0.6',
        classifiers=[
            "Intended Audience :: Science/Research",
            "Intended Audience :: Developers",    
            "Topic :: Software Development",
            "Topic :: Scientific/Engineering",        
            "Programming Language :: Python :: 3",
            "Programming Language :: Python :: 3.8",
            "Programming Language :: Python :: 3.9",
            "Programming Language :: Python :: 3.10",        
            "License :: OSI Approved :: MIT License",
            "Operating System :: OS Independent",
        ],    
        python_requires='>=3.5',                # Minimum version requirement of the package    
#        py_modules=["vkit"],                    # Name of the python package    
#        package_dir={'':'vkit'},                # Directory of the source code of the package    
        packages=["vkit"],
        include_package_data=True,        
        description='Vision kit - Usefull tools for your computer vision project with TensorFlow',        
        long_description=long_description,
        long_description_content_type='text/markdown',
        url="https://github.com/mehrdad-dev/vision-kit",        
        author='Mehrdad Mohammdian',
        install_requires=REQUIRED,
        license='MIT',
    )

if __name__ == "__main__":
    setup_package()

