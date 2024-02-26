import sys

from giti import core, consts, parser, update


def main():
    argparser = parser.get_arg_parser()
    core.args = vars(argparser.parse_args())

    if core.args.get('list_config_file'):
        print(consts.CONFIG_FILE)
        return 0

    if core.args.get('update'):
        return update.update_github_templates()

    if core.args.get('list_templates'):
        return core.list_templates()

    if core.args.get('add'):
        return core.add_template()

    if core.args.get('set_default'):
        return core.set_default_template()

    return core.create_gitignore()


if __name__ == '__main__':
    sys.exit(main())
