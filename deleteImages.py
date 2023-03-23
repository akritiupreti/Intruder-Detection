from ftplib import FTP

ftp = FTP()
username = "epiz_33843178"
password = "QOMgsUul412mh"
print("Connecting...")
ftp.connect("ftp.epizy.com", 21)
ftp.login(username, password)
print("Connected!")

ftp.cwd("/htdocs/photos")
files = ftp.nlst()
for file in files:
    if file.endswith(".jpg"):
        ftp.delete(file)

print("All images deleted!")