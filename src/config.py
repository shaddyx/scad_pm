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

class DEP_TYPES:
    git = "git"

@dataclass_json()
@dataclasses.dataclass
class Dependency(object):
    url: str
    path: typing.Optional[str] = None
    dependency_type: str = DEP_TYPES.git

@dataclass_json()
@dataclasses.dataclass
class YamlConfig(object):
    dependencies: typing.List[Dependency]


class YamlConfigParser:
    @Inject()
    def __init__(self, args_config: ArgsConfig):
        self.args_config = args_config

    def parse(self, file: str):
        with open(file, "r") as stream:
            data = yaml.safe_load(stream)
            logging.info("Parsing data: {}".format(data))
            return self.map_data(data)

    def map_data(self, data):
        conf = YamlConfig.from_dict(data)  # type: YamlConfig
        for dep in conf.dependencies:
            if dep.path is None:
                dep.path = dep.url.split("/")[-1].split(".")[0]
        return conf
