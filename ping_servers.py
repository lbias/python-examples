# This script will, depending on the arguments supplied will ping the servers associated with that application group.

# Load the Library Module
import os
# Load the Library Module
import subprocess
# Load the Library Module
import sys

# Help Menu if called
if '-h' in sys.argv or '--h' in sys.argv or '-help' in sys.argv or '--help' in sys.argv:
    print '''
You need to supply the application group for the servers you want to ping, i.e.
    dms
    swaps

Followed by the site i.e.
    155
    bromley'''
    sys.exit(0)
else:
    # If no arguments are passed,display the help/instructions on how to run the script
    if (len(sys.argv) < 3):
        sys.exit ('\nYou need to supply the app group. Usage : ' + filename + ' followed by the application group i.e. \n \t dms or \n \t swaps \n then the site i.e. \n \t 155 or \n \t bromley')

    # Set the variable appgroup as the first argument you supply
    appgroup = sys.argv[1]
    # Set the variable site as the second argument you supply
    site = sys.argv[2]

    # Check the os, if it's linux then
    if os.name == "posix":
        # This is the ping command
        myping = "ping -c 2 "
    # Check the os, if it's windows then
    elif os.name in ("nt", "dos", "ce"):
        # This is the ping command
        myping = "ping -n 2 "

    # If the argument passed is dms then
    if 'dms' in sys.argv:
        # Set the variable appgroup to dms
        appgroup = 'dms'
    # Else if the argment passed is swaps then
    elif 'swaps' in sys.argv:
        # Set the variable appgroup to swaps
        appgroup = 'swaps'

    # If the argument passed is 155 then
    if '155' in sys.argv:
        # Set the variable site to 155
        site = '155'
    # Else if the argument passed is bromley
    elif 'bromley' in sys.argv:
        # Set the variable site to bromley
        site = 'bromley'

# Sets a variable for the script name
filename = sys.argv[0]
# Set the variable logdir by getting the OS environment logs
logdir = os.getenv("logs")
# Set the variable logfile, using the arguments passed to create the logfile
logfile = 'ping_' + appgroup + '_' + site + '.log'
# Set the variable logfilename by joining logdir and logfile together
logfilename = os.path.join(logdir, logfile)
# Set the variable confdir from the OS environment variable - 1.2
confdir = os.getenv("my_config")
# Set the variable conffile - 1.2
conffile = (appgroup + '_servers_' + site + '.txt')
# Set the variable conffilename by joining confdir and conffile together - 1.2
conffilename = os.path.join(confdir, conffile)

# Open a logfile to write out the output
f = open(logfilename, "w")
# Open the config file and read each line - 1.2
for server in open(conffilename):
    # Run the ping command for each server in the list.
    ret = subprocess.call(myping + server, shell=True, stdout=f, stderr=subprocess.STDOUT)
    # Depending on the response
    if ret == 0:
        # Write out that you can receive a reponse
        f.write (server.strip() + " is alive" + "\n")
    else:
        # Write out you can't reach the box
        f.write (server.strip() + " did not respond" + "\n")

# Show the location of the logfile
print ("\n\tYou can see the results in the logfile : " + logfilename);
