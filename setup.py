import os
from setuptools import setup

path = os.path.abspath(os.path.dirname(__file__))

# Get the long description from the README file
with open(os.path.join(path, 'README.rst'), encoding='utf-8') as f:
  long_description = f.read()

# Get requirements from file
with open(os.path.join(path, 'requirements.txt')) as f:
  requirements = f.read().splitlines()

setup(name='kodijsonrpc',
      version='1.0',
      description='Kodi JSON-RPC client',
      long_description=long_description,
      url='http://github.com/davgeo/kodijsonrpc',
      author='David George',
      author_email='dcg.git@gmail.com',
      license='MIT',
      packages=["kodijsonrpc"],
      install_requires=requirements)
