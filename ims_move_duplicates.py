import os
import shutil
import re

def move_duplicates(logfile, dest_folder):
    """This function reads a log file and moves the duplicate files into a specified folder."""
    duplicate_lines = []
    duplicates_section = 0
    with open(logfile, 'r') as f:
        lines = f.readlines()
    for line in lines:
        # print(line)
        match = re.search('Duplicate files:',line)
        if match:
            print("Pattern found:", match.group())
            duplicates_section = 1
        else:
            if duplicates_section:
                duplicate_lines.append(line)
                print(line)
                if not os.path.exists(dest_folder):
                    os.makedirs(dest_folder)
                if line.strip():  # check if line is not empty
                    filename = line.split(', ')[0][10:]
                    if os.path.exists(filename):
                        shutil.move(filename, os.path.join(dest_folder, os.path.basename(filename)))

logfile = 'log.txt'
dest_folder = 'C:\\temp\\ims-duplicates'
move_duplicates(logfile, dest_folder)
