__winc_id__ = "ae539110d03e49ea8738fd413ac44ba8"
__human_name__ = "files"

import os
import zipfile
import shutil

parent_dir = os.path.split(os.path.realpath(__file__))[0]
cache_path_abs = parent_dir + "/cache"

def clean_cache():
    path = cache_path_abs
    if (os.path.exists(path)):
        shutil.rmtree(path)
    os.mkdir(path)


def cache_zip(zip_file_path, cache_dir_path):
    with zipfile.ZipFile(zip_file_path, "r") as myzip:
      myzip.extractall(cache_dir_path)

def cached_files():
    abs_path_parent = os.path.abspath(cache_path_abs)
    files = []
    for f in os.listdir(abs_path_parent):
        file_path = os.path.join(abs_path_parent, f)
        if (os.path.isfile(file_path)):
            files.append(file_path)
    return files

def find_password(files):
    for f in files:
        contents = open(f, "r").read()
        if "password" in contents:
            words = contents.split()
            for i in range(len(words)):
                if "password" in words[i]:
                    return words[i + 1]




