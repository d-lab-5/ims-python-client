from webdav3.client import Client
import hashlib
import os
import socket
import tempfile
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
       # Download the file from WebDAV server to a temporary location
       temp_file = os.path.join(tempfile.gettempdir(), filename)
       dest_folder = "C:/temp/ims"
       temp_file = dest_folder + filename
       if not os.path.exists(dest_folder + folder):
           os.makedirs(dest_folder + folder)
       if os.path.isfile(temp_file):
           # do this if the file exists and is a file
           print(f"The file {temp_file} is a file and exists in the local temp folder.")
       else:
           # do that if the file does not exist or is not a file
           print(f"The file {temp_file} does not exist in the temp dir, will download it.")
           client.download(filename, temp_file)
       with open(temp_file,'rb') as file:
           chunk = 0
           while chunk != b'':
               chunk = file.read(1024)
               h.update(chunk)
       # Delete the temporary file if keep_local_copy is false
       if not config['keep_local_copy']:
           os.remove(temp_file)
   except PermissionError:
       print(f"Permission denied: {filename}")
       return None
   return h.hexdigest()

def hash_files_in_folder(folder):
    file_hashes = {}
    duplicate_hashes = {}
    count=0
    config = get_config()
    for name in client.list(folder):
        filename = os.path.join(folder, name)
        if should_process(filename, config):
            if client.is_dir(filename):
                # Recursively hash files in subdirectory
                sub_file_hashes, sub_duplicate_hashes = hash_files_in_folder(filename)
                file_hashes.update(sub_file_hashes)
                duplicate_hashes.update(sub_duplicate_hashes)
            else:
                count = count + 1
                print("\nProcessing file" + str(count) + " " + filename)
                md5hash = hash_file(filename)
                if md5hash not in file_hashes.values():
                    file_hashes[filename] = md5hash
                else:
                    duplicate_hashes[filename] = md5hash
    return file_hashes, duplicate_hashes

def write_to_json(file_hashes, duplicate_hashes):
    data = {
        "hostname": socket.gethostname(),
        "webdav_hostname": config['webdav_hostname'],
        "unique_files": file_hashes,
        "duplicate_files": duplicate_hashes
    }
    # Write data to a local JSON file
    with open('log.json', 'w') as f:
        json.dump(data, f, indent=4)
    # Upload the JSON file to WebDAV server
    try:
        client.upload('log.json', 'log.json')
    except:
        print("Could not upload the log file, please check permissions!")
        return None


def write_to_txt(file_hashes, duplicate_hashes):
    # Write data to a local text file
    with open('log.txt', 'w') as f:
        f.write("Unique files:\n")
        for filename, md5hash in file_hashes.items():
            f.write(f"Filename: {filename}, MD5 Hash: {md5hash}\n")
        f.write("\nDuplicate files:\n")
        for filename, md5hash in duplicate_hashes.items():
            f.write(f"Filename: {filename}, MD5 Hash: {md5hash}\n")
    # Upload the text file to WebDAV server
    try:
        client.upload('log.txt', 'log.txt')
    except:
        print("Could not upload the log file, please check permissions!")
        return None


def get_webdav_config():
    try:
        with open('webdav_config.json', 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        print("WebDAV config file not found, please run ims_nas_config.py first!")
        return None

# Create a Client object with the WebDAV config
config = get_webdav_config()
if config is not None:
    client = Client(config)
    info = client.info("/")
    print("WEVDAV info: " + str(info))
else:
    print("Cannot connect to WebDAV server")
    exit()

folder = input("Enter the path to your folder: ")
file_hashes, duplicate_hashes = hash_files_in_folder(folder)
write_to_json(file_hashes, duplicate_hashes)
write_to_txt(file_hashes, duplicate_hashes)

