import argparse
import sys


def get_arg_parser():
    parser = argparse.ArgumentParser(
            prog="giti",
            description="Create .gitignore files from templates.")

    parser.add_argument('-u', '--update',
                        action='store_const',
                        const=True,
                        default=False,
                        dest='update',
                        help='update gitignore templates')

    '''
    parser.add_argument('-o', '--output',
                        action='store',
                        default='.gitignore',
                        dest='output',
                        help='output file name')
    '''

    parser.add_argument('templates',
                        type=str,
                        nargs='*',
                        default=['default'],
                        help='name of gitignore template')

    return parser

