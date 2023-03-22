from ftplib import FTP
import time


class Host:
    def __init__(self):
        self.ftp = FTP()
        self.server = "ftp.epizy.com"
        self.port = 21
        print("Connecting to server...")
        self.ftp.connect(self.server, self.port)
        self.ftp.login("epiz_33843178", "QOMgsUul412mh")
        print("Connected!")

    def getStatus(self):
        print("Getting status...")
        self.ftp.cwd('/htdocs')
        files = self.ftp.nlst()
        print("Done!")
        if "on.txt" in files:
            return True
        else:
            return False

    def getFlag(self):
        self.ftp.cwd('/htdocs')
        print("Fetching status...")
        files = self.ftp.nlst()
        # wait for user to configure settings in app
        while "incomplete.txt" in files:
            print("Waiting for owner's response...")
            files = self.ftp.nlst()
            time.sleep(5)

        self.ftp.rename("complete.txt", "incomplete.txt")
        print("Fetched!")
        if "00.txt" in files:
            return "00", None
        elif "10.txt" in files:
            return "10", None
        else:
            name = None
            for file in files:
                if file[:5] == "name_":
                    name = file[5:]
            return "11", name

    def run(self, file, filename):
        self.ftp.cwd('/htdocs/photos')
        filename = filename.replace(":", ".")
        r = self.ftp.storbinary('STOR %s' % filename, file)
        #print(r)  # should be: 226 Transfer OK

    def closeConnection(self):
        self.ftp.quit()

if __name__ == '__main__':
    pass
