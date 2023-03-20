from ftplib import FTP
import time


class Host:
    def __init__(self):
        self.ftp = FTP()
        self.server = "ftp.epizy.com"
        self.port = 21
        self.ftp.connect(self.server, self.port)
        self.ftp.login("epiz_33608356", "HwGN8xvq7ut")

    def getStatus(self):
        files = self.ftp.nlst()
        if "on.txt" in files:
            return True
        else:
            return False

    def getFlag(self):
        print("Fetching status")
        files = self.ftp.nlst()
        print(files)
        # wait for user to configure settings in app
        while "incomplete.txt" in files:
            print("Still incomplete")
            files = self.ftp.nlst()
            time.sleep(5)

        self.ftp.rename("complete.txt", "incomplete.txt")
        print("Fetched!")
        if "00.txt" in files:
            return "00"
        elif "01.txt" in files:
            return "01"
        else:
            name = None
            for file in files:
                if file[:5] == "name_":
                    name = file[5:]
            return "11", name

    def run(self, file, filename):
        #files = self.ftp.nlst() #list of files on the server
        #print(files)

        filename = filename.replace(":", ".")
        r = self.ftp.storbinary('STOR %s' % filename, file)
        #print(r)  # should be: 226 Transfer OK

    def closeConnection(self):
        self.ftp.quit()


if __name__ == '__main__':
    pass