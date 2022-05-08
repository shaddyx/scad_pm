import logging
import os

from scopeton.decorators import Inject

import config
import dep_util
import proc_util


class GitFetcher:
    @Inject()
    def __init__(self, conf: config.ArgsConfig, dep_util: dep_util.DepUtil):
        self.conf = conf
        self.dep_util = dep_util

    def fetch(self, dep_config: config.FileConfig, dep: config.Dependency):
        if not os.path.exists(self.conf.lib_path):
            os.mkdir(self.conf.lib_path)
        logging.info("Ful dir: {}".format(self.dep_util.resolve_full_dir(dep_config, dep)))
        if not os.path.exists(self.dep_util.resolve_full_dir(dep_config, dep)):
            self.download_dep(dep_config, dep)
        else:
            self.update_dep(dep_config, dep)

    def update_dep(self, dep_config: config.FileConfig, dep: config.Dependency):
        self.goto_revision(dep_config, dep)
        if not self.conf.upgrade:
            logging.info("skipping upgrade, see --upgrade, for package: {}".format(dep))
            return
        logging.info("Updating dep: {}".format(dep))
        proc_util.call(self.dep_util.resolve_full_dir(dep_config, dep), ["git", "pull"])

    def download_dep(self, dep_config: config.FileConfig, dep: config.Dependency):
        logging.info("Downloading dep: {}".format(dep))
        proc_util.call(self.conf.lib_path, ["git", "clone", dep.url])
        self.goto_revision(dep_config, dep)

    def goto_revision(self, dep_config: config.FileConfig, dep: config.Dependency):
        if dep.revision is not None:
            proc_util.call(self.dep_util.resolve_full_dir(dep_config, dep), ["git", "checkouut", dep.revision])


