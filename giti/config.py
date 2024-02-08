import configparser
import os

from . import consts


class Config:
    update = 0
    default = ""

    def __init__(self, options: dict = {}):
        self.update = int(options.get('update', '0'))
        self.default = options.get('default', "")

    def to_dict(self):
        return {'update': str(self.update), 'default': str(self.default)}


def read_config():
    config = configparser.ConfigParser()
    config.read(consts.CONFIG_FILE)
    return Config(config['CONFIG'])


def default_config():
    config = configparser.ConfigParser()
    default = Config()
    print(default.to_dict())
    config['CONFIG'] = default.to_dict()
    with open(consts.CONFIG_FILE, "w") as f:
        config.write(f)


def write_config(config: Config):
    config_obj = configparser.ConfigParser()
    config_obj['CONFIG'] = config.to_dict()
    with open(consts.CONFIG_FILE, "w") as f:
        config_obj.write(f)

