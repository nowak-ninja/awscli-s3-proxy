#!/bin/bash

rm -rf dist build
pip install twine setuptools wheel
python setup.py sdist bdist_wheel
# twine upload --repository-url https://upload.pypi.org/legacy/ dist/*
