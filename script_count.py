# This scans my scripts directory and gives a count of the different types of scripts

# Load the library module
import os

# Set the variable path by getting the value from the OS environment variable scripts
path = os.getenv("scripts")
# Set the variable dropbox by getting the value from the OS environment variable dropbox
dropbox = os.getenv("dropbox")

# Function to clear the screen
def clear_screen():
    # Unix/Linux/MacOS/BSD/etc
    if os.name == "posix":
        # Clear the Screen
        os.system('clear')
    # DOS/Windows
    elif os.name in ("nt", "dos", "ce"):
        # Clear the Screen
        os.system('CLS')

# Start of the function to count the files in the scripts directory, it counts the extension when passed below
def count_files(path, extensions):
    # Set the counter to 0
    counter = 0
    # Loop through all the directories in the given path
    for root, dirs, files in os.walk(path):
        # For all the files
        for file in files:
            # Count the files
            counter += file.endswith(extensions)
    # Return the count
    return counter

# Start of the function just to count the files in the github directory
def github():
    # Joins the paths to get the github directory - 1.1
    github_dir = os.path.join(dropbox, 'github')
    # Get a count for all the files in the directory
    github_count = sum((len(f) for _, _, f in os.walk(github_dir)))
    # If the number of files is greater then 5, then print the following messages
    if github_count > 5:
        print '\nYou have too many in here, start uploading !!!!!'
        print 'You have: ' + str(github_count) + ' waiting to be uploaded to github!!'
    # Unless the count is 0, then print the following messages
    elif github_count == 0:
        print '\nGithub directory is all Clear'
    # If it is any other number then print the following message, showing the number outstanding.
    else:
        print '\nYou have: ' + str(github_count) + ' waiting to be uploaded to github!!'

# Start of the function just to count the files in the development directory
def development():
    # Joins the paths to get the development directory
    dev_dir = os.path.join(path, 'development')
    # Get a count for all the files in the directory
    dev_count = sum((len(f) for _, _, f in os.walk(dev_dir)))
    # If the number of files is greater then 10, then print the following messages
    if dev_count > 10:
        print '\nYou have too many in here, finish them or delete them !!!!!'
        print 'You have: ' + str(dev_count) + ' waiting to be finished!!'
    # Unless the count is 0, then print the following messages
    elif dev_count ==0:
        print '\nDevelopment directory is all clear'
    else:
        # If it is any other number then print the following message, showing the number outstanding.
        print '\nYou have: ' + str(dev_count) + ' waiting to be finished!!'
# Call the function to clear the screen
clear_screen()

print '\nYou have the following :\n'
# Run the count_files function to count the files with the extension we pass
print 'AutoIT:\t' + str(count_files(path, '.au3'))
print 'Batch:\t' + str(count_files(path, ('.bat', ',cmd')))
print 'Perl:\t' + str(count_files(path, '.pl'))
print 'PHP:\t' + str(count_files(path, '.php'))
print 'Python:\t' + str(count_files(path, '.py'))
print 'Shell:\t' + str(count_files(path, ('.ksh', '.sh', '.bash')))
print 'SQL:\t' + str(count_files(path, '.sql'))

# Call the github function
github()
# Call the development function
development()
