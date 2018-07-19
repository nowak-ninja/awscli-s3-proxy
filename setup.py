#!/usr/bin/env python
import sys
from setuptools import setup

requires = ['awscli>=1.11.0']

setup(
    name='awscli-plugin-s3-proxy',
    packages=['awscli_plugin_s3_proxy'],
    version='0.4',
    description='S3 proxy plugin for AWS CLI',
    long_description=open('README.md').read(),
    author='Sebastian Nowak',
    author_email='snowak@bluesoft.net.pl',
    url='https://github.com/nowak-ninja/awscli-plugin-s3-proxy',
    download_url='https://github.com/nowak-ninja/awscli-plugin-s3-proxy/archive/0.4.tar.gz',
    keywords=['awscli', 'plugin', 's3', 'proxy'],
    install_requires=requires,
    classifiers = []
)
