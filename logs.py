# This script will search for all *.log files in the given directory, zip them using the program you specify and then date stamp them

# Load the Library Module
import os
# Load just the strftime Module from Time
from time import strftime

# Set the Variable logsdir
logsdir = "c:\puttylogs"
# Set the Variable zip_program - 1.1
zip_program = "The Unarchiver.app"

# Find all the files in the directory
for files in os.listdir(logsdir):
    # Check to ensure the files in the directory end in .log
	if files.endswith(".log"):
        # Create the Variable files1, this is the files in the directory, then we add a suffix with the date and the zip extension
		files1 = files + "." + strftime("%Y-%m-%d") + ".zip"
        # Change directory to the logsdir
		os.chdir(logsdir)
        # Zip the logs into dated zip files for each server. - 1.1
		os.system(zip_program + " " +  files1 +" "+ files)
        # Remove the original log files
		os.remove(files)
