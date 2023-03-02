from ftplib import FTP
import os


class Host:
    def __init__(self):
        self.ftp = FTP()
        server = "ftp.epizy.com"
        port = 21
        self.ftp.connect(server, port)
        self.ftp.login("epiz_33608356", "HwGN8xvq7ut")

    def getStatus(self):
        files = self.ftp.nlst()
        self.ftp.quit()
        if "on.txt" in files:
            return True
        else:
            return False

    def run(self, file, filename):
        files = self.ftp.nlst() #list of files on the server
        #print(files)

        filename = filename.replace(":", ".")
        r = self.ftp.storbinary('STOR %s' % filename, file)
        #print(r)  # should be: 226 Transfer OK

        self.ftp.quit()


if __name__ == '__main__':
    pass