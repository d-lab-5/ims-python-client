import json

# Define the name of the JSON config file
config_file = 'webdav_config.json'

# Define the keys and prompts for the config entries
config_keys = ['webdav_hostname', 'webdav_login', 'webdav_password', 'keep_local_copy', 'local_temp_dir']
config_prompts = {
    'webdav_hostname': "Enter the WebDAV hostname (e.g. https://webdav.server.com): ",
    'webdav_login': "Enter the WebDAV login: ",
    'webdav_password': "Enter the WebDAV password: ",
    'keep_local_copy': "Enter true or false to keep or delete the local copy in the temp dir: ",
    'local_temp_dir' : "Enter local temp dir:"
}

# Try to load the existing config file if it exists
try:
    with open(config_file, 'r') as f:
        config = json.load(f)
except FileNotFoundError:
    # If the file does not exist, create an empty config dictionary
    config = {}

# Loop through the config keys and prompt for the values
for key in config_keys:
    # Show the existing value if it exists, otherwise show a blank input
    if key in config:
        value = input(config_prompts[key] + f"[{config[key]}] ")
    else:
        value = input(config_prompts[key])
    # If the input is not empty, update the config dictionary with the new value
    if value != "":
        config[key] = value

# Write the updated config dictionary to the JSON file
with open(config_file, 'w') as f:
    json.dump(config, f, indent=4)

# Print a confirmation message
print(f"Config file {config_file} created or updated successfully.")
