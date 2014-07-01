# -*- coding:utf-8 -*-
import sys
sys.path.append('./src')
from distutils.core import setup
from pyempty import __version__

setup(name='pyempty',
      version=__version__,
      description='empty python project template',
      long_description=open("README.md").read(),
      author='plq2013',
      author_email='plq2014@gmail.com',
      packages=['pyempty'],
      package_dir={'pyempty': 'src/pyempty'},
      package_data={'pyempty': ['stuff']},
      license="Public domain",
      platforms=["any"],
      url='https://github.com/plq2013/pyempty')
