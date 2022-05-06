import os
import warnings
import logging

# specific imports
from os import walk # get file names
from datetime import datetime # check for time
from datetime import timedelta # computes time difference

def is_file_older_than (file, delta): 
    cutoff = datetime.utcnow() - delta
    mtime = datetime.utcfromtimestamp(os.path.getmtime(file))
    if mtime < cutoff:
        return True
    return False


# set directory of local machine 
#   Local directory needed for settings file
localDir = "C:\\sftp-connector"
#os.chdir(localDir)

# set up logging error file
logging.basicConfig(filename="file_delete_log.txt",level=logging.DEBUG);
logging.captureWarnings(True);


# grab .txt file containing login information
with open("sftpLoginInformation.txt") as file:
    inputs = file.read().splitlines();  

# grab files
# get list of all files in folder
filenames = next(walk(inputs[3]), (None, None, []))[2] # [] if no file

  
# use of function above


# loop through filenames and copy local file to server
for fn in filenames:
  localFile = inputs[3]+"\\"+fn
  flag = is_file_older_than(localFile, timedelta(days=int(inputs[4])))

  if flag == True: 
    os.remove(localFile)
    
