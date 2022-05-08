import logging

from scopeton.decorators import Inject
from scopeton.scope import Scope

import config
import git_util


class DependencyResolver:
    @Inject()
    def __init__(self, scope: Scope, conf: config.ArgsConfig, parser: config.MainConfigParser, fetcher: git_util.GitFetcher):
        self.conf = conf
        self.parser = parser
        self.scope = scope
        self.fetcher = fetcher

    def resolve(self, dep_config: config.YamlConfig):
        logging.info("resolving dependencies: {}".format(dep_config))
        for dep in dep_config.dependencies:
            self._resolve_dep(dep_config, dep)

    def _resolve_dep(self, dep_config: config.YamlConfig, dep: config.Dependency):
        logging.info("Resolving dependency: {}".format(dep))
        self.fetcher.fetch(dep_config, dep)


