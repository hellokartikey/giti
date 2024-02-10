from giti import config, core, consts, parser, update


def main():
    argparser = parser.get_arg_parser()
    args = vars(argparser.parse_args())

    if args.get('update'):
        update.update_github_templates()
        return

    if args.get('list_templates'):
        core.list_templates()
        return

    if args.get('add'):
        core.add_template(*args.get('add'))
        return

    if args.get('set_default'):
        core.set_default_template(args.get('set_default'))
        return

    core.create_gitignore(*args.get('templates', ['default']))


if __name__ == '__main__':
    main()

