from urllib.request import urlopen

with urlopen('http://google.com') as response:
    for line in response:
        print(line)

import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

toaddr = "vinogradovpavel32@gmail.com"
fromaddr = "vinogradovpavel32@gmail.com"
mypass = ""

msg = MIMEMultipart()
msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = "Привет от питона"

body = "Это пробное сообщение"
msg.attach(MIMEText(body, 'plain'))

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(fromaddr, mypass)
text = msg.as_string()
server.sendmail(fromaddr, toaddr, text)
server.quit()