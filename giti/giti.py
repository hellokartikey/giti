import parser
import update

def main():
    argparser = parser.get_arg_parser()
    args = vars(argparser.parse_args())

    print(args)

    if args.get('update'):
        update.update_github_templates()



if __name__ == '__main__':
    main()

