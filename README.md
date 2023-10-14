# ims-python-client
Manage files and sync with AWS Amplify backend 

# ims_scan_folder.py
In this script, the input function is used to prompt you for the path to the folder you want to hash. The function hash_files_in_folder walks through all files in the folder and its subfolders and computes their MD5 hashes.

Please note that you need to have the os and hashlib modules available in your Python environment to run this script. If they’re not installed, you can add them using pip: pip install os hashlib. Also, be aware that while MD5 is a widely used algorithm, it is vulnerable to hash collisions and is not recommended for functions requiring high security.

# ims_move_duplicates.py
In this script, the move_duplicates function iterates over each line in the duplicate files section. For each line, it checks if the line is not empty (to skip the last line which is ‘\n’), extracts the filename, checks if the file exists, and then moves it to the destination folder.

Please note that you need to have the os and shutil modules available in your Python environment to run this script. If they’re not installed, you can add them using pip: pip install os shutil.

Also, be aware that this script moves the files, meaning that they will no longer be available at their original location. If you want to keep a copy of the files at their original location, you can replace shutil.move with shutil.copy. Finally, please replace 'log.txt' and 'C:\\temp\\ims-duplicates' with the path to your log file and the destination folder you want to use.