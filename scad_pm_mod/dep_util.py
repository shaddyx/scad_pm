import os

from scopeton.decorators import Inject

from scad_pm_mod import config


class DepUtil:
    @Inject()
    def __init__(self, conf: config.ArgsConfig):
        self.conf = conf

    def resolve_full_dir(self, dep_config: config.FileConfig, dep: config.Dependency):
        return os.path.join(dep_config.dep_path, self.conf.lib_path, dep.path)