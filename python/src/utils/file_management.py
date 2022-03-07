from os import remove, listdir
from os.path import join
from . import selenium_info

def clearCache():
    for i in listdir(selenium_info.cache_path):
        remove(join(selenium_info.cache_path, i))