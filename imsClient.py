import hashlib
import os

def hash_file(filename):
   """"This function returns the MD5 hash of the file."""
   h = hashlib.md5()
   with open(filename,'rb') as file:
       chunk = 0
       while chunk != b'':
           chunk = file.read(1024)
           h.update(chunk)
   return h.hexdigest()

def hash_files_in_folder(folder):
    """This function returns a list of tuples (filename, md5hash) for all files in a folder."""
    file_hashes = {}
    duplicate_hashes = {}
    for root, dirs, files in os.walk(folder):
        for file in files:
            filename = os.path.join(root, file)
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
