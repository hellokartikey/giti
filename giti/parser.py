import argparse
import sys


def get_arg_parser():
    parser = argparse.ArgumentParser(
            prog="giti",
            description="Create .gitignore files from templates.")

    parser.add_argument('-u',
                        action='store_const',
                        const=True,
                        default=False,
                        dest='update',
                        help='update gitignore templates')

    parser.add_argument('-l',
                        action='store_const',
                        default=False,
                        const=True,
                        dest='list_templates',
                        help='list all installed templates')

    parser.add_argument('-a',
                        action='store',
                        default=None,
                        dest='add',
                        nargs=2,
                        metavar=('TEMPLATE', 'NAME'),
                        help='add custom template')

    parser.add_argument('-d',
                        action='store',
                        dest='set_default',
                        help='set default template',
                        metavar='DEFAULT')

    parser.add_argument('-o',
                        action='store',
                        default='.gitignore',
                        dest='output',
                        help='output file name')

    parser.add_argument('--config-file',
                        action='store_const',
                        default=False,
                        const=True,
                        dest='list_config_file',
                        help='show config file path')

    parser.add_argument('templates',
                        type=str,
                        nargs='*',
                        default=['default'],
                        help='name of gitignore template')

    return parser

