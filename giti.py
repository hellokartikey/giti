import sys

from giti import config, core, consts, parser, update


def main():
    argparser = parser.get_arg_parser()
    args = vars(argparser.parse_args())

    if args.get('list_config_file'):
        print(consts.CONFIG_FILE)
        sys.exit(0)

    if args.get('update'):
        sys.exit(update.update_github_templates())

    if args.get('list_templates'):
        sys.exit(core.list_templates())

    if args.get('add'):
        sys.exit(core.add_template(*args.get('add')))
        return

    if args.get('set_default'):
        sys.exit(core.set_default_template(args.get('set_default')))

    return sys.exit(core.create_gitignore(*args.get('templates', ['default'])))


if __name__ == '__main__':
    main()

