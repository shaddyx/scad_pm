import logging

from scopeton.decorators import Inject

import config


class DependencyResolver:
    @Inject()
    def __init__(self, conf: config.ArgsConfig, parser: config.YamlConfigParser):
        self.conf = conf
        self.parser = parser

    def resolve(self, dep_config: config.YamlConfig):
        for dep in dep_config.dependencies:
            self._resolve_dep(dep_config, dep)
        logging.info("resolving dependencies")

    def _resolve_dep(self, dep_config: config.YamlConfig, dep: config.Dependency):
        logging.info("Resolving dependency: {}".format(dep))
        
