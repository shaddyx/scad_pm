import dataclasses
import logging
import typing

import scopeton.scope
from dataclasses_json import dataclass_json
import yaml

# @dataclasses.dataclass
# @dataclass_json
from scopeton.decorators import Inject


class ArgsConfig:
    lib_path: str
    upgrade: bool
    v: bool
    pm_file: str

    def __str__(self):
        return "{}:[{}]".format(self.__class__.__name__, self.__dict__)


@dataclasses.dataclass
@dataclass_json
class Dependency(object):
    url: str

    def __init__(self, url: str):
        self.url = url


@dataclasses.dataclass
@dataclass_json
class YamlConfig(object):
    dependencies: typing.List[Dependency]

    def __init__(self, dependencies: typing.List[Dependency]):
        self.dependencies = dependencies

    def __hash__(self):
        return 1


class YamlConfigParser:
    @Inject()
    def __init__(self, scope: scopeton.scope.Scope, args_config: ArgsConfig):
        self.args_config = args_config
        scope.registerInstance(YamlConfig, self._parse())

    def parse(self, file: str):
        with open(file, "r") as stream:
            data = yaml.safe_load(stream)
            logging.info("Parsing data: {}".format(data))
            return YamlConfig.from_dict(data)
