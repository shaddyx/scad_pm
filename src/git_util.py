import logging
import os

from scopeton.decorators import Inject

import config
import proc_util


class GitFetcher:
    @Inject()
    def __init__(self, conf: config.ArgsConfig):
        self.conf = conf

    def fetch(self, dep_config: config.YamlConfig, dep: config.Dependency):
        if not os.path.exists(self.conf.lib_path):
            os.mkdir(self.conf.lib_path)
        logging.info("Ful dir: {}".format(self.resolve_full_dir(dep_config, dep)))
        if not os.path.exists(self.resolve_full_dir(dep_config, dep)):
            self.download_dep(dep_config, dep)
        else:
            self.update_dep(dep_config, dep)

    def update_dep(self, dep_config: config.YamlConfig, dep: config.Dependency):
        if not self.conf.upgrade:
            logging.info("skipping upgrade, see --upgrade, for package: {}".format(dep))
            return
        logging.info("Updating dep: {}".format(dep))
        proc_util.call(self.resolve_full_dir(dep_config, dep), ["git", "pull"])

    def download_dep(self, dep_config: config.YamlConfig, dep: config.Dependency):
        logging.info("Downloading dep: {}".format(dep))
        proc_util.call(self.conf.lib_path, ["git", "clone", dep.url])

    def resolve_full_dir(self, dep_config: config.YamlConfig, dep: config.Dependency):
        return os.path.join(self.conf.lib_path, dep.path)

