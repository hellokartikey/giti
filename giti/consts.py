import os
import platformdirs as pf


APP = "giti"
TEMPLATES_REPO = "https://github.com/github/gitignore"
DATA_DIR = pf.user_data_dir(APP)
CONFIG_FILE = os.path.join(DATA_DIR, 'config.ini')

