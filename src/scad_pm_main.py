#!/usr/bin/env python
import logging
import argparse

from scopeton.scope import Scope

import config
import dependency_resolver
from config import ArgsConfig

parser = argparse.ArgumentParser(description='Openscad package manager')
parser.add_argument('--v', action='store_true', help='verbose output')
parser.add_argument('--upgrade', action='store_true', help='upgrade packages')
parser.add_argument('--lib-path', dest='lib_path', default='./lib', help='library path')
parser.add_argument('--pm-file', dest='pm_file', default='scad_pm.yaml', help='pm file name')

args = parser.parse_args()
args_config = ArgsConfig()
args_config.__dict__ = vars(args)

logging.basicConfig(level=logging.DEBUG if args.v else logging.INFO)

scope = Scope()
scope.registerInstance(ArgsConfig, args_config)
scope.registerBean(
    config.YamlConfigParser,
    dependency_resolver.DependencyResolver
)

resolver = scope.getInstance(dependency_resolver.DependencyResolver)
parser = scope.getInstance(config.YamlConfigParser)

main_file = parser.parse(args_config.pm_file)
resolver.resolve(main_file)

#
# dep_file_name = args.pm_file
# lib_dir = os.path.join(os.getcwd(), args.lib_path)
#
# def parse_repo_dir(repo: str):
#     return repo.split("/")[-1].split(".")[0]
#
# def parse_line(path, line: str) -> Dep:
#     line = line.strip()
#     logging.info("parsing line: {}".format(line))
#     logging.info("path: {}".format(path))
#     return Dep(
#         path,
#         line,
#         parse_repo_dir(line),
#         line.startswith("#")
#     )
#
# def parse_scad_pm(path):
#     if not os.path.exists(path):
#         return []
#     with open(path, "rt") as f:
#         return map(lambda x: parse_line(lib_dir, x), f.readlines())
#
#
# def update_dep(dep: Dep):
#     if not args.upgrade:
#         logging.info("skipping upgrade, see --upgrade, for package: {}".format(dep))
#         return
#     logging.info("Updating dep: {}".format(dep))
#     proc_util.call(dep.full_dir(), ["git", "pull"])
#
# def download_dep(dep: Dep):
#     logging.info("Downloading dep: {}".format(dep))
#     proc_util.call(dep.path, ["git", "clone", dep.git_url])
#
# def resolve_dep(dep: Dep):
#     logging.debug("Resolving dep: {}".format(dep))
#     if not os.path.exists(dep.path):
#         os.mkdir(dep.path)
#     if not os.path.exists(dep.full_dir()):
#         download_dep(dep)
#     else:
#         update_dep(dep)
#
# def work_on_dep_file(dep_file):
#     pm = parse_scad_pm(dep_file)
#     for k in pm:
#         if k.skip:
#             continue
#         resolve_dep(k)
#         nested_dep_file = os.path.join(k.full_dir(), dep_file_name)
#         if os.path.exists(nested_dep_file):
#             logging.info("processing nested dep file: {}".format(nested_dep_file))
#             work_on_dep_file(nested_dep_file)
#
# if not os.path.exists(dep_file_name):
#     logging.error("No dep file found: {}".format(dep_file_name))
#     sys.exit(1)
#
# work_on_dep_file(dep_file_name)
