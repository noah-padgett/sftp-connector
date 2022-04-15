import ftplib
import os

# set directory of local machine
localDir = "C:\\Users\\noahp\\Documents\\GitHub\\sftp-connector\\ftp"
os.chdir(localDir)

# grab .txt file containing login information
with open("ftpLoginInformation.txt") as file:
    loginInfo = file.read().splitlines()

# set up FTP network information
ftp = ftplib.FTP()
ftp.connect(loginInfo[0],int(loginInfo[1]))
ftp.login(loginInfo[2],loginInfo[3])
# set up function to grad file
def grabFile(filename):
    localfile = open(filename, 'wb')
    ftp.retrbinary('RETR ' + filename, localfile.write, 1024)
    localfile.close()
    return;
    
# run function
grabFile(filename='lease.csv')
grabFile(filename='NGL.csv')
grabFile(filename='shiptran.csv')
  
  # close ftp connection
ftp.quit()
