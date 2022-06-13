#!/bin/bash

pip uninstall -y scad_pm
rm -rf ../scad_pm.egg-info
rm -rf ../dist
rm -rf ../build

pushd ../
pip install .
popd

pip show -f scad_pm