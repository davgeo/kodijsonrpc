from setuptools import setup

with open('requirements.txt') as f:
  requirements = f.read().splitlines()

setup(name='kodijsonrpc',
      version='0.1',
      description='Kodi JSON-RPC client',
      url='http://github.com/davgeo/kodijsonrpc',
      author='David George',
      author_email='dcg.git@gmail.com',
      license='MIT',
      packages=["kodijsonrpc"],
      install_requires=requirements)
