# This script will check to see if all of the environment variables I require are set

import os

# Set the variable confdir from the OS environment variable
confdir = os.getenv("my_config")
# Set the variable conffile
conffile = 'env_check.conf'
# Set the variable conffilename by joining confdir and conffile together
conffilename = os.path.join(confdir, conffile)


# Open the config file and read all the settings
for env_check in open(conffilename):
    # Set the variable as itself, but strip the extra text out
    env_check = env_check.strip()
    # Format the Output to be in Square Brackets
    print '[{}]'.format(env_check)
    # Set the variable newenv to get the settings from the OS what is currently set for the settings out the configfile
    newenv = os.getenv(env_check)

    # If it doesn't exist
    if newenv is None:
        # Print it is not set
        print env_check, 'is not set'
    # Else if it does exist
    else:
        # Print out the details
        print 'Current Setting for {}={}\n'.format(env_check, newenv)
