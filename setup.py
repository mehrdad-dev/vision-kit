from setuptools import find_packages, setup
from codecs import open
from os import path


HERE = path.abspath(path.dirname(__file__))
with open(path.join(HERE, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='vision-kit',
    packages=find_packages(include=['vision-kit']),
    version='0.1.0',
    description='Vision kit - Usefull tools for your computer vision project with TensorFlow',
    long_description=long_description,
    url="https://github.com/mehrdad-dev/vision-kit",    
    author='Mehrdad Mohammdian',
    install_requires=['tensorflow'],
    license'GPL-3.0',
)


