import hashlib
import os

import json

def get_config():
    try:
        with open('config.json', 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

def update_config(config):
    with open('config.json', 'w') as f:
        json.dump(config, f, indent=4)

def should_process(filename, config):
    ext = os.path.splitext(filename)[1]
    if ext not in config:
        response = input(f"Should files with extension {ext} be processed? (yes/no): ")
        config[ext] = response.lower() == 'yes'
        update_config(config)
    return config[ext]
def hash_file(filename):
   """"This function returns the MD5 hash of the file."""
   h = hashlib.md5()
   try:
       with open(filename,'rb') as file:
           chunk = 0
           while chunk != b'':
               chunk = file.read(1024)
               h.update(chunk)
   except PermissionError:
       print(f"Permission denied: {filename}")
       return None
   return h.hexdigest()
def hash_files_in_folder(folder):
    file_hashes = {}
    duplicate_hashes = {}
    count=0
    config = get_config()
    for root, dirs, files in os.walk(folder):
        for file in files:
            filename = os.path.join(root, file)
            if should_process(filename, config):
                count = count + 1
                print("\nProcessing file" + str(count) + " " + filename)
                md5hash = hash_file(filename)
                if md5hash not in file_hashes.values():
                    file_hashes[filename] = md5hash
                else:
                    duplicate_hashes[filename] = md5hash
    return file_hashes, duplicate_hashes


folder = input("Enter the path to your folder: ")
file_hashes, duplicate_hashes = hash_files_in_folder(folder)

with open('log.txt', 'w') as f:
    f.write("Unique files:\n")
    for filename, md5hash in file_hashes.items():
        f.write(f"Filename: {filename}, MD5 Hash: {md5hash}\n")
    f.write("\nDuplicate files:\n")
    for filename, md5hash in duplicate_hashes.items():
        f.write(f"Filename: {filename}, MD5 Hash: {md5hash}\n")
