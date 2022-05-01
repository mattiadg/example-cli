__all__ = ["__CMD_REGISTER__"]

import importlib
import os


__CMD_REGISTER__ = {}


def register(name):
    def wrap(cls):
        __CMD_REGISTER__[name] = cls
        return cls
    return wrap


parent_dir = os.path.dirname(__file__)

for file in os.listdir(parent_dir):
    if file.endswith(".py"):
        module = importlib.import_module("."+file[:-len(".py")], "cmd")
