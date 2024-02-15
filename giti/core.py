import os

from . import consts
from . import config
from .consts import eprint

def create_gitignore(*args):
    for template in args:
        if template == 'default':
            if not config.config.default:
                eprint("No default template set")
                return 1

            print("Initializing default template...")
            return 0

        print(f"Template: {template}")


def list_templates():
    default = config.config.default
    templates = config.config.templates

    if len(templates) == 0:
        print("There are no templates installed.")
        return 1

    print("Listing all templates")
    for t in templates:
        if t == default:
            print(f" {t} [default]")
            continue
        print(f" {t}")

    if len(templates) > 1:
        print(f"{len(templates)} templates installed.")
    else:
        print("1 template installed.")

    return 0


def set_default_template(template: str):
    if template not in config.config.templates:
        eprint("Template not installed")
        return 1

    config.config.default = template
    config.write_config()

    return 0


def add_template(file: str, name: str):
    if not os.path.exists(file):
        eprint(f"{file}: no such file")
        return 1

    if name not in config.config.templates:
        config.config.templates.append(name)
    else:
        print(f"Template {name} already exists. Replace it? [y/N]: ", end='')
        if input().lower() != 'y':
            return 1

    with open(file, 'r') as rf, open(config.template_file(name), 'w') as wf:
        wf.write(rf.read())

    if len(config.config.templates) == 1:
        config.config.default = name

    config.write_config()

    return 0

