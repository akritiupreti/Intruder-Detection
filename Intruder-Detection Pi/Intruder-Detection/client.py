from ftplib import FTP
import os


def run():
    ftp = FTP()
    server = "ftp.epizy.com"
    port = 21
    ftp.connect(server, port)
    ftp.login("epiz_33608356", "HwGN8xvq7ut")

    files = ftp.nlst()  # list of files on the server
    #print(files)

    for file in files:
        if file[-4:] == ".jpg":
            date = file[:file.find("_")]  # folder name will be the date
            if not date in os.listdir() or not file in os.listdir(date):  # if photo does not exist
                if not os.path.isdir(date):
                    os.mkdir(date)

                path = os.path.join(date, file)
                r = ftp.retrbinary('RETR %s' % file, open(path, 'wb').write)
                print(r)
            else:
                print("File already downloaded")


if __name__ == '__main__':
    run()
