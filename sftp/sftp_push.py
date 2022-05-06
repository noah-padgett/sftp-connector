# import needed python libraries
import pysftp
import os
import warnings
import logging

# set directory of local machine 
#   Local directory needed for settings file
localDir = "C:\\sftp-connector"
os.chdir(localDir)

# set up logging error file
logging.basicConfig(filename="sftp_push_log.txt",level=logging.DEBUG);
logging.captureWarnings(True);


# grab .txt file containing login information
with open("sftpLoginInformation.txt") as file:
    loginInfo = file.read().splitlines();

# log into server
cnopts = pysftp.CnOpts();
cnopts.hostkeys = None;
# sftp = pysftp.Connection(
#   host="198.50.32.44",
#   username = "SpiritMeter",
#   password = "a9jeu6ix")

warnings.filterwarnings("ignore");
sftp = pysftp.Connection(
  host=loginInfo[0], 
  username = loginInfo[1], 
  password = loginInfo[2],
  cnopts=cnopts);
  
# Copy local file to server
localFile = loginInfo[3]+"\\"+loginInfo[4]
remoteFile="/Home/spiritmeter/Indausol/"+loginInfo[4]
sftp.put(
  localpath=localFile, 
  remotepath=remoteFile
);

logging.info("\n")
logging.info("File push log end")
logging.info("\n")

# close SFTP connection
sftp.close()

