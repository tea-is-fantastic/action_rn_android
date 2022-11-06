import os
import shutil

from scripts.tif_env import TEMP_PATH


def template_init():
    print('action_templates >> template_init >> chdir')
    shutil.rmtree(TEMP_PATH, ignore_errors=True)
    os.mkdir(TEMP_PATH)
    os.chdir(TEMP_PATH)
