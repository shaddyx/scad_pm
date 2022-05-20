# scad_pm - A simple package manager for OpenScad

The idea of this project is to create a simple package manager to use it to download openscad libraries

## installation
```commandline
pip install scad_pm
```

Also, please note that git must be installed as a pre-requisite

## supported repositories

At the moment scad_pm supports downloading libraries from the git repository.

## supported formats

The dependency file should be placed to the project root, for now 2 formats are supported 

#### pm format (scad.pm): 

Example:
```
    git@github.com:nophead/NopSCADlib.git
    git@github.com:revarbat/BOSL2.git
    git@github.com:shaddyx/openscad_tools.git#3086f4c
```
the format is pretty simple, you can just specifiy 1 git url per line.

If you want to checkout the specific branch or revision - you should use the following format:

git_url#revision

example:
```commandline
git@github.com:shaddyx/openscad_tools.git#3086f4c
```
where 3086f4c is the branch name or revision hash


#### yaml format (scad_pm.yaml):

```yml
dependencies:
  -
    url: git@github.com:revarbat/BOSL2.git
  -
    url: git@github.com:shaddyx/openscad_tools.git
    revision: 3086f4c
```

## usage
just type 
```commandline
scad_pm
```
from the command line and wait while scad pm put all dependencies into the ./lib directory

## output

by default scad_pm will put downloaded libraries to ./lib directory near the pm file

