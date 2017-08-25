# This will list all the files in the given directory, it will also go through all the subdirectories as well

# Load the library module
import os

# Set the variable logdir by getting the value from the OS environment variable logs
logdir  = os.getenv("logs")
# Set the variable logfile
logfile = 'script_list.log'
# Set the varable path by getting the value from the OS environment variable scripts - 1.2
path    = os.getenv("scripts")

# Set the variable logfilename by joining logdir and logfile together
logfilename = os.path.join(logdir, logfile)
# Set the variable log and open the logfile for writing
log = open(logfilename, 'w')

# Go through the directories and the subdirectories
for dirpath, dirname, filenames in os.walk(path):
    # Get all the filenames
    for filename in filenames:
        # Write the full path out to the logfile
        log.write(os.path.join(dirpath, filename)+'\n')

# Small message informing the user the file has been created
print ("\nYour logfile " , logfilename, "has been created")
