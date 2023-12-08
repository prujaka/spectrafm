from setuptools import setup
from setuptools import find_packages

with open('requirements.txt') as f:
    content = f.readlines()
requirements = [x.strip() for x in content]

setup(name='spectrafm',
      version='0.1',
      install_requires=requirements,
      packages=find_packages())
