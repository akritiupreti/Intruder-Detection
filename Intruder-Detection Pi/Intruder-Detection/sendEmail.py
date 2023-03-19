import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import ssl
import time
from host import Host
import datetime


def run(isHome, credentials):
    currDate = str(datetime.date.today())
    currTime = time.ctime()[11:-5]
    filename = currDate + "_" + currTime
    attachment = open('intruder/intruder.jpg', 'rb')
    
    if isHome:
        obj = credentials
        obj.run(attachment, filename + ".jpg")
        return
    
    obj = credentials
    obj.run(attachment, filename + ".jpg")
    
    emails = []

    f = open("email/emails.txt", "r")
    for line in f:
        emails.append(line)

    f.close()

    from_address = 'arajupreti@gmail.com'
    password = 'qrvzmdwppwtfeaka' # app password generated by gmail

    msg = MIMEMultipart()

    msg['From'] = from_address

    msg['Subject'] = 'INTRUDER ALERT!'

    p = MIMEBase('application', 'octet-stream')

    p.set_payload((attachment).read())

    encoders.encode_base64(p)

    p.add_header('Content-Disposition', 'attachment; filename = %s' % filename)

    msg.attach(p)

    text = msg.as_string()
    context = ssl.create_default_context()
    for email in emails:
        s = smtplib.SMTP('smtp.gmail.com', 587)
        s.ehlo()  # check connection
        s.starttls(context=context)
        s.ehlo()  # check connection
        s.login(from_address, password)
        s.sendmail(from_address, email, text)
        s.quit()


if __name__ == '__main__':
    pass
