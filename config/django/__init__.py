import os
from config.env import environ, env

BASE_DIR = environ.Path(__file__) - 3
env.read_env(os.path.join(BASE_DIR, ".env"))

mode = env("DJANGO_CONFIG_MODE")

if mode == "base":
    from config.django.base import *
else:
    raise RuntimeError(f"Config {mode} not found")
