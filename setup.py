#!/usr/bin/env python
import sys
from setuptools import setup

requires = []

setup(
    name='awscli-plugin-proxy',
    packages=['awscli_plugin_proxy'],
    version='0.5',
    description='Proxy plugin for AWS CLI',
    long_description=open('README.md').read(),
    author='Sebastian Nowak',
    author_email='sebastian@nowak.ninja',
    url='https://github.com/cyralinc/awscli-plugin-proxy',
    download_url='https://codeload.github.com/cyralinc/awscli-plugin-proxy/zip/refs/heads/master',
    keywords=['awscli', 'plugin', 'proxy'],
    install_requires=requires,
    classifiers = []
)
