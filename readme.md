# scad_pm - a Simple package manager for OpenScad

The idea of this project is to create a simple package manager to use it to download openscad libraries

## installation
```commandline
pip install scad_pm
```

## supported repositories

At the moment scad_pm supports downloading libraries from the git repository.

## supported formats

The dependency file should be placed to the repository root, for now 2 formats are supported 

pm format (scad.pm): 

```
    git@github.com:nophead/NopSCADlib.git
    git@github.com:revarbat/BOSL2.git
    git@github.com:shaddyx/openscad_tools.git
```

yaml format (scad_pm.yaml):

```yml
dependencies:
  -
    url: git@github.com:shaddyx/openscad_tools.git
```

## usage
just type 
```commandline
scad_pm
```
from the command line

## output

by default scad_pm will put downloaded libraries to ./lib directory near the pm file

