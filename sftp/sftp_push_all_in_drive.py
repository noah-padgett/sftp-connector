# import needed python libraries
import pysftp
import os
import warnings
import logging

# specific imports
from os import walk

# set directory of local machine 
#   Local directory needed for settings file
localDir = "C:\\sftp-connector"
#os.chdir(localDir)

# set up logging error file
logging.basicConfig(filename="sftp_push_log.txt",level=logging.DEBUG);
logging.captureWarnings(True);


# grab .txt file containing login information
with open("sftpLoginInformation.txt") as file:
    inputs = file.read().splitlines();

# log into server
cnopts = pysftp.CnOpts();
cnopts.hostkeys = None;
# sftp = pysftp.Connection(
#   host="198.50.32.44",
#   username = "SpiritMeter",
#   password = "a9jeu6ix")

warnings.filterwarnings("ignore");
sftp = pysftp.Connection(
  host=inputs[0], 
  username = inputs[1], 
  password = inputs[2],
  cnopts=cnopts);
  
  
# get list of all files in folder
filenames = next(walk(inputs[3]), (None, None, []))[2] # [] if no file

# loop through filenames and copy local file to server
for fn in filenames:
  localFile = inputs[3]+"\\"+fn
  remoteFile = "/Home/spiritmeter/Indausol/"+fn
  # send to SFTP server
  sftp.put(
    localpath=localFile, 
    remotepath=remoteFile
  );


logging.info("\n")
logging.info("File push log end")
logging.info("\n")

# close SFTP connection
sftp.close()

