# DIY information management system
IMS is a do-it-yourself simple information management system designed to streamline and organize files across multiple PCs and 
laptops. Leveraging the robust capabilities of AWS Amplify for the backend, IMS ensures efficient file management. 
The user interface comprises Python scripts for granular control and Gatsby web apps for an intuitive, web-based experience. 
IMS is aimed at maintaining a clutter-free digital environment at home.”

# Local scripts
## ims_scan_folder.py
In this script, the input function is used to prompt you for the path to the folder you want to hash. 
The function `hash_files_in_folder` walks through all files in the folder and its subfolders, checks their file extensions 
against a configuration stored in a JSON file, and computes their MD5 hashes if they should be processed according to the 
configuration.

The configuration is stored in a file named `config.json`. 
If a file extension is not in the configuration, the script will prompt you to decide whether files with that extension 
should be processed and update the configuration accordingly.

Please note that you need to have the `os`, `hashlib`, and `json` modules available in your Python environment to run this script.
If they’re not installed, you can add them using pip: `pip install os hashlib json`. 
Also, be aware that while MD5 is a widely used algorithm, it is vulnerable to hash collisions and is not recommended 
for functions requiring high security.

## ims_move_duplicates.py
In this script, the move_duplicates function iterates over each line in the duplicate files section. 
For each line, it checks if the line is not empty (to skip the last line which is ‘\n’), extracts the filename, 
checks if the file exists, and then moves it to the destination folder.

Please note that you need to have the os and shutil modules available in your Python environment to run this script. 
If they’re not installed, you can add them using pip: `pip install os shutil`.

Also, be aware that this script moves the files, meaning that they will no longer be available at their original location. 
If you want to keep a copy of the files at their original location, you can replace `shutil.move` with `shutil.copy`. 
Finally, please replace `log.txt` and `C:\\temp\\ims-duplicates` with the path to your log file and the destination folder 
you want to use.