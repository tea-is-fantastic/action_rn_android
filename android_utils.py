import os

from scripts.tif_env import TEMP_PATH
from scripts.tif_yaml import app_yaml

android_path = os.path.join(TEMP_PATH, app_yaml.name, 'android')
android_src = os.path.join(android_path, "app", "src", "main")
android_java = os.path.join(android_src, "java", *app_yaml.apk.split('.'))
