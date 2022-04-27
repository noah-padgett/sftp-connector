# import needed python libraries
import pysftp
import os
import warnings


# set directory of local machine 
#   Local directory needed for settings file
localDir = "C:\\sftp-connector"
#os.chdir(localDir)

# grab .txt file containing login information
with open("ftpLoginInformation.txt") as file:
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
localFile = localDir+"\\test_upload.txt";
sftp.put(localpath=localFile);

# close SFTP connection
sftp.close()

