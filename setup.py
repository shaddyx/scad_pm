import setuptools
from setuptools import setup

setup(
    name='scad_pm',
    version='0.23',
    scripts=['scad_pm'],
    packages=["scad_pm_mod"],
    install_requires=[
        'pyyaml',
        'dataclasses_json',
        'scopeton'
   ]
)