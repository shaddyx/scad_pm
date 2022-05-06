#!/usr/bin/env python

import argparse

# parser = argparse.ArgumentParser(description='Openscad package manager')
# args = parser.parse_args()
import os.path
import logging
logging.basicConfig(level=logging.INFO)

import proc_util
from scad_dep import Dep

dep_file_name = "scad.pm"
lib_dir = os.path.join(os.getcwd(), "./lib")

def parse_repo_dir(repo: str):
    return repo.split("/")[-1].split(".")[0]

def parse_line(path, line) -> Dep:
    logging.info("parsing line: {}".format(line))
    logging.info("path: {}".format(path))
    return Dep(path, line, parse_repo_dir(line))

def parse_scad_pm(path):
    if not os.path.exists(path):
        return []
    with open(path, "rt") as f:
        return map(lambda x: parse_line(lib_dir, x), f.readlines())


def update_dep(dep: Dep):
    logging.info("Updating dep: {}".format(dep))
    proc_util.call(dep.full_dir(), ["git", "pull"])

def download_dep(dep: Dep):
    logging.info("Downloading dep: {}".format(dep))
    proc_util.call(dep.path, ["git", "clone", dep.git_url])

def resolve_dep(dep: Dep):
    if not os.path.exists(dep.path):
        os.mkdir(dep.path)
    if not os.path.exists(dep.full_dir()):
        download_dep(dep)
    else:
        update_dep(dep)

def work_on_dep_file(dep_file):
    pm = parse_scad_pm(dep_file)
    #logging.info("found lines: {}".format(list(pm)))
    for k in pm:
        resolve_dep(k)
        nested_dep_file = os.path.join(k.full_dir(), dep_file_name)
        if os.path.exists(nested_dep_file):
            work_on_dep_file(nested_dep_file)

work_on_dep_file(dep_file_name)
