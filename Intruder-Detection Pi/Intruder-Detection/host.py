import paramiko
import socket
from ftplib import FTP
import os


def run(file, filename):
    ftp = FTP()
    server = "ftp.epizy.com"
    port = 21
    ftp.connect(server, port)
    ftp.login("epiz_33608356","HwGN8xvq7ut")

    files = ftp.nlst() #list of files on the server
    #print(files)

    filename = filename.replace(":", ".")
    r = ftp.storbinary('STOR %s' % filename, file)
    print(r)  # should be: 226 Transfer OK


if __name__ == '__main__':
    pass