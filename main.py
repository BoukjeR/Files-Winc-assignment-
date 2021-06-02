__winc_id__ = 'ae539110d03e49ea8738fd413ac44ba8'
__human_name__ = 'files'

import os, zipfile

def clean_cache():
    if os.path.isdir('Cache') is True:
        for file in os.scandir('C:/Users/Boukje Gergin/files/Cache'):
            os.remove(file.path)
    if os.path.isdir('Cache') is False:
        os.mkdir('Cache')
    
clean_cache()

def cache_zip(zip_file_path:str, cache_dir_path:str):
    clean_cache()
    for item in os.listdir(zip_file_path):
        if item.endswith('.zip'):
            file_name = os.path.abspath(item)
            zip_ref = zipfile.ZipFile(file_name)
            zip_ref.extractall(cache_dir_path)
            zip_ref.close()
        
cache_zip('C:/Users/Boukje Gergin/files/','C:/Users/Boukje Gergin/files/Cache')

def cached_files():
    cache_dir_path = 'C:/Users/Boukje Gergin/files/Cache'
    file_list = []
    for items in os.listdir(cache_dir_path):
        if os.path.isfile(os.path.join(cache_dir_path, items)):
            file_list.append(os.path.abspath(os.path.join(cache_dir_path, items)))
    return(file_list)

file_list = cached_files()

def find_password(file_list):
    for file in file_list:
        search_file = open(file, 'r')
        for line in search_file.readlines():
            if 'password' in line:
                search_file.close()
                return(line)
            else:
                search_file.close()

print(find_password(file_list))