import setuptools
from setuptools import setup

setup(
    name='scad_pm',
    version='0.24',
    scripts=['scad_pm'],
    packages=["scad_pm_mod"],
    url="https://github.com/shaddyx/scad_pm",
    install_requires=[
        'pyyaml',
        'dataclasses_json',
        'scopeton'
   ]
)