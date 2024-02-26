import os

from . import config
from .consts import eprint


args = dict()


def create_gitignore():
    templates = args.get('templates')

    if os.path.exists(output := args.get('output', '.gitignore')):
        if_overwrite = input(f"{output} already exists. Overwrite? [y/N] ")
        if if_overwrite.lower() != 'y':
            return 1

    if templates == 'default':
        return create_default_gitignore()

    return create_gitignore_from_templates(*args.get('templates'))


def create_default_gitignore():
    if not config.config.get_default():
        eprint("No default template set")
        return 1

    create_gitignore_from_templates(config.config.get_default())

    return 0


def create_gitignore_from_templates(*templates):
    with open(args.get("output", '.gitignore'), 'w') as f:
        content = "# .gitignore generated using giti\n"
        content += f"# Templates: {' '.join(templates)}\n\n"

        for t in templates:
            with open(config.template_file(t), 'r') as r:
                content += f"# --- {t}\n\n"
                content += r.read()
                content += "\n"

        f.write(content)

    if len(templates) > 1:
        print(f"Initializing templates: {' '.join(templates)}")
    else:
        print(f"Initializing template: {' '.join(templates)}")

    return 0


def list_templates():
    default = config.config.get_default()
    templates = config.config.get_templates()

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


def set_default_template():
    template = args.get('set_default')

    if template not in config.config.get_templates():
        eprint("Template not installed")
        return 1

    config.config.set_default(template)
    config.write_config()

    return 0


def add_template():
    file, name = args.get("add", ('.gitignore', 'custom'))

    if not os.path.exists(file):
        eprint(f"{file}: no such file")
        return 1

    if name not in (templates := config.config.get_templates()):
        templates.append(name)
    else:
        print(f"Template {name} already exists. Replace it? [y/N]: ", end='')
        if input().lower() != 'y':
            return 1

    with open(file, 'r') as rf, open(config.template_file(name), 'w') as wf:
        wf.write(rf.read())

    if len(config.config.get_templates()) == 1:
        config.config.set_default(name)

    config.write_config()

    return 0
