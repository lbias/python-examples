# This will go through and backup all my automator services workflows

# Load the library module
import datetime
import os
import shutil

# Get Today's date
today    = datetime.date.today()
# Format it so we can use the format to create the directory
todaystr = today.isoformat()

# Set the variable by getting the value from the OS setting
confdir      = os.getenv("my_config")
# Set the variable by getting the value from the OS setting
dropbox      = os.getenv("dropbox")
# Set the variable as the name of the configuration file
conffile     = ('services.conf')
# Set the variable by combining the path and the file name
conffilename = os.path.join(confdir, conffile)
# Source directory of where the scripts are located
sourcedir    = os.path.expanduser('~/Library/Services/')
# Combine several settings to create
destdir      = os.path.join(dropbox, "My_backups" + "/" +
    "Automater_services" + todaystr + "/")

# Walk through the configuration file
for file_name in open(conffilename):
    # Strip out the blank lines from the configuration file
    fname = file_name.strip()
    # For the lines that are not blank
    if fname:
        # Get the name of the source files to backup
        sourcefile = os.path.join(sourcedir, fname)
        # Get the name of the destination file names
        destfile = os.path.join(destdir, fname)
        # Copy the directories
        shutil.copytree(sourcefile, destfile)
