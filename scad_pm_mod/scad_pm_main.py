#!/usr/bin/env python
import argparse
import logging

from scopeton.scope import Scope

from scad_pm_mod import config, dep_util, dependency_resolver, git_util
from scad_pm_mod.config import ArgsConfig

parser = argparse.ArgumentParser(description='Openscad package manager')
parser.add_argument('--v', action='store_true', help='verbose output')
parser.add_argument('--upgrade', action='store_true', help='upgrade packages')
parser.add_argument('--lib-path', dest='lib_path', default='./lib', help='library path')
parser.add_argument('--pm-file', dest='pm_file', help='pm file name')

args = parser.parse_args()
args_config = ArgsConfig()
args_config.__dict__ = vars(args)
logging.basicConfig(level=logging.DEBUG if args.v else logging.INFO)

scope = Scope()
scope.registerInstance(ArgsConfig, args_config)
scope.registerBean(
    config.YamlConfigParser,
    config.MainConfigParser,
    config.PmConfigParser,
    dep_util.DepUtil,
    dependency_resolver.DependencyResolver,
    git_util.GitFetcher
)

resolver = scope.getInstance(dependency_resolver.DependencyResolver)
resolver.run("./", args_config.pm_file)
