#!/bin/bash

pushd ../
rm -rf dist
python3 setup.py sdist
#twine register dist/* -r pypi
twine upload dist/*
popd