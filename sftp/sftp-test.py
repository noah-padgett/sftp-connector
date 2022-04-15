import paramiko
paramiko.util.log_to_file("paramiko.log")

# Open a transport
host,port = "192.168.1.114",21
transport = paramiko.Transport((host,port))

# Auth    
username,password = "ftpTestUser","password"
transport.connect(None,username,password)

# Go!    
sftp = paramiko.SFTPClient.from_transport(transport)

# Download
filepath = "/etc/passwd"
localpath = "/home/remotepasswd"
sftp.get(filepath,localpath)
