import configparser
import os
import ast

from . import consts


class Config:
    update = 0
    default = ""
    templates = []

    def get_templates(self):
        return self.templates

    def set_templates(self, *args):
        self.templates = list(args)

    def get_default(self):
        return self.default

    def set_default(self, new):
        self.default = new

    def __init__(self, update=0, default="", templates=[]):
        self.update = update
        self.default = default
        self.templates = templates

    def to_dict(self):
        return {'update': self.update,
                'default': self.default,
                'templates': self.templates}


def read_config():
    if not check_if_config_exists():
        default_config()

    config = configparser.ConfigParser()
    config.read(consts.CONFIG_FILE)
    config_section = config['CONFIG']

    config_obj = Config()
    config_obj.update = config_section.getint('update')
    config_obj.default = config_section.get('default')
    config_obj.templates = ast.literal_eval(config_section.get('templates'))

    return config_obj


def default_config():
    if not os.path.isdir(consts.DATA_DIR):
        os.mkdir(consts.DATA_DIR)

    if not os.path.isdir(consts.TEMPLATES_DIR):
        os.mkdir(consts.TEMPLATES_DIR)

    config = configparser.ConfigParser()
    default = Config()
    config['CONFIG'] = default.to_dict()
    with open(consts.CONFIG_FILE, "w") as f:
        config.write(f)


def write_config():
    config_obj = configparser.ConfigParser()
    config_obj['CONFIG'] = config.to_dict()
    with open(consts.CONFIG_FILE, "w") as f:
        config_obj.write(f)


def check_if_config_exists():
    return os.path.isdir(consts.DATA_DIR) and \
        os.path.exists(consts.CONFIG_FILE)


def template_file(name: str):
    return os.path.join(consts.TEMPLATES_DIR, name)


config = read_config()
