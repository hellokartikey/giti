import os
import sys
import platformdirs as pf


APP = "giti"
TEMPLATES_REPO = "https://github.com/github/gitignore"
DATA_DIR = pf.user_data_dir(APP)
TEMPLATES_DIR = os.path.join(pf.user_data_dir(APP), 'templates')
CONFIG_FILE = os.path.join(DATA_DIR, 'config.ini')


def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)

