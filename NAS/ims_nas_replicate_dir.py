from webdav3.client import Client
import os
import json

def get_webdav_config():
    try:
        with open('webdav_config.json', 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        print("WebDAV config file not found")
        return None

# Create a Client object with the WebDAV config
config = get_webdav_config()
if config is not None:
    client = Client(config)
else:
    print("Cannot connect to WebDAV server")
    exit()

# Define the top directory on the WebDAV server
top_dir = input("Enter the path to your top folder: ")

# Define the local directory to replicate the folder structure
local_dir = "C:/temp/ims/webdav"

# Check if the local directory exists, if not, create it
if not os.path.exists(local_dir):
    os.makedirs(local_dir)

# Define a recursive function to copy the subdirectories from WebDAV server to local directory
def copy_subdirs(webdav_dir, local_dir, level, i):
    # Loop through the names in the WebDAV directory
    print("Level = " + str(level) )
    i = i + 1
    try:
        for name[level] in client.list(webdav_dir):
            count[level] = count[level] + 1
            if count[level] < 2:
                webdav_current_path[level] = name[level]
            else:
        #        if("/" in name and ".thumbnail" not in name):
                if ("/" in name):
                    print("Dir " + str(webdav_current_path))
                    level = level +1
                    webdav_dir = ""
                    for key, value in webdav_current_path.items():
                        webdav_dir = webdav_dir + value
                        #print(f"Key: {key}, Value: {value} , WebDir: {webdav_dir} , Level: {level}, I: {i}")
                    webdav_dir = webdav_dir + name[level]
                    copy_subdirs(webdav_dir, local_dir ,level , i)
        level = level -1
    except:
        print(f"problem with {webdav_dir}")

# Call the recursive function with the top directory as the initial argument
count = {0: 0, 1: 0, 2: 0}
webdav_current_path = {0: top_dir}
name = {0: top_dir}
copy_subdirs(top_dir, local_dir, 0, 0)

# Print a confirmation message
print(f"Folder structure from {top_dir} on WebDAV server replicated to {local_dir} on local machine.")

    #     print(webdav_path)admin

    #     res1 = client.resource(webdav_path)
    #     info = res1.info()
    #     if res1.is_dir():
    #         print(".. is a dir")
        # Join the name with the WebDAV and local directories to get the full paths
        # if(name == webdav_dir):
        #     webdav_path = os.path.join(webdav_dir, name)
        # else:
        #     webdav_path = webdav_dir
        # local_path = os.path.join(local_dir, name)
        # print(webdav_path + " " + local_path)
        # # Check if the WebDAV path is a subdirectory or not
        # if client.is_dir(webdav_path):
        #     # If it is a subdirectory, create a corresponding local subdirectory if it does not exist
        #     res1 = client.resource(webdav_path)
        #     info = res1.info()
        #     if res1.is_dir():
        #         print(".. is a dir")
        #     print(info)
        #     # if not os.path.exists(local_path):
        #     #     os.makedirs(local_path)
        #     # # Recursively copy the subdirectory contents from WebDAV server to local directory
        #     copy_subdirs(webdav_path, local_path)



