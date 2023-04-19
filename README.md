# PythonScripts
Some python Scripts


reNamer

Open a command prompt or terminal window.

Navigate to the directory where the script is located using the cd command.

Run the script by typing python reNamer.py and pressing Enter.

The script will prompt you to enter the location of the folder containing the files you want to rename. 

Type the path of the folder and press Enter. Make sure you use forward slashes (/) or double backslashes (\) instead of single backslashes () when entering the path.

If the entered path is invalid, the script will give an "Error: Invalid source folder path" and exit.

If the entered path is valid, The script will prompt you to enter the location of the folder to write the new files to. Type the path of the folder and press Enter.

If the entered path is invalid, the script will give an "Error: Invalid destination folder path" and exit.

If the entered path is valid, The script will prompt you to enter the main name that the files will share. Type the main name and press Enter.

If the entered main name is invalid, the script will give an "Error: Invalid main name" and exit.

If the entered main name is valid, the script will iterate through all files in the source folder, get the creation time of each file, convert it to
a formatted string, generate a new file name by appending the formatted creation time string to the main name, check if a file with the same name already exists in the destination folder, if not it will rename the file and move it to the destination folder and do this for all files found in the source folder.

If a file with the same name already exists in the destination folder, the script will give an "Error: {new_file_name} already exists in destination folder" and skip that file.

After iterating through all files in the source folder, the script will print "File renaming successful!"

Note that this script only work for windows os, and it will create the destination folder if it does not exist before moving the files.
