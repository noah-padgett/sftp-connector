# import needed python libraries
import pysftp
import os

# set directory of local machine 
#   Local directory needed for settings file
localDir = "C:\\ftp-connector"
os.chdir(localDir)

# grab .txt file containing login information
with open("ftpLoginInformation.txt") as file:
    loginInfo = file.read().splitlines()

# log into server
sftp = pysftp.Connection(
  host=loginInfo[0], 
  username = loginInfo[1], 
  password = loginInfo[2])

# Copy server to local
sftp.get_r("/","C:\\")

# close SFTP connection
sftp.close()
