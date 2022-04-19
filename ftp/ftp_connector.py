# import needed python libraries
import ftplib
import os

# set directory of local machine 
#   Local directory needed for settings file
localDir = "C:\\ftp-connector"
os.chdir(localDir)

# grab .txt file containing login information
with open("ftpLoginInformation.txt") as file:
    loginInfo = file.read().splitlines()

# set up FTP network information
ftp = ftplib.FTP()
ftp.connect(loginInfo[0],int(loginInfo[1]))
ftp.login(loginInfo[2],loginInfo[3])

# set directory where files are to be saved
#   root of SD/USB drive
os.chdir("D:\\")

# set up function to grad file
def grabFile(filename):
    localfile = open(filename, 'wb')
    ftp.retrbinary('RETR ' + filename, localfile.write, 1024)
    localfile.close()
    return;
    
# run function
grabFile(filename=loginInfo[4])
grabFile(filename=loginInfo[5])
grabFile(filename=loginInfo[6])
  
  # close ftp connection
ftp.quit()
