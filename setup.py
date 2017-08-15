#!/usr/bin/env python

from setuptools import setup, find_packages
import smartbytes

with open("README.rst", "r") as f:
    long_description = f.read()

setup(name='smartbytes-monitor',
      version=smartbytes.__version__,
      description=' Python package to monitor your airtel network stats like remaining data, days left, etc',
      long_description=long_description,
      author='Ritiek Malhotra',
      author_email='ritiekmalhotra123@gmail.com',
      packages = find_packages(),
      entry_points={
            'console_scripts': [
                  'smartbytes = smartbytes.smartbytes:command_line',
            ]
      },
      url='https://www.github.com/ritiek/smartbytes-monitor',
      keywords=['airtel', 'stats', 'monitor', 'data-usage', 'smartbytes-tracker'],
      license='MIT',
      download_url='https://github.com/ritiek/smartbytes-monitor/archive/v' + smartbytes.__version__ + '.tar.gz',
      classifiers=[],
      install_requires=[
            'BeautifulSoup4',
      ]
)
