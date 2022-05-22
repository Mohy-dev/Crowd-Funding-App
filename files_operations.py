import os
from pathlib import Path


def file_exists(file):
    return os.path.isfile(file) and os.path.exists(file)


def is_file_empty(file):
    if not file_exists(file):
        return 1
    return os.path.getsize(file) == 0


def create__the_file(file_path):
    newFile = Path(file_path)
    newFile.touch(exist_ok=True)
    f = open(newFile)


def dir_exists(dir_path):
    return os.path.isdir(dir_path) and os.path.exists(dir_path)


def create_the_dir(file_dir):
    if not dir_exists(file_dir):
        os.makedirs(file_dir)
