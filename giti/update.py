import consts

import os

def update_github_templates():
    print("Updating templates...")

    if not os.path.isdir(consts.DATA_DIR):
        print("Creating data directory...")
        os.mkdir(consts.DATA_DIR)


