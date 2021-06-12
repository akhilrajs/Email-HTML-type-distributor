import smtplib
import ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import csv
import time

sender_email = "protectthewhitecoatimamsnkl@gmail.com"
# receiver_email = "receiver_mail@gmail.com"
password = "1qw2er3ty"

message = MIMEMultipart("alternative")
message["Subject"] = "IMA MSN KERALA"
message["From"] = sender_email

context = ssl.create_default_context()
session = smtplib.SMTP('smtp.gmail.com', 587) #use gmail with port
session.starttls(context = context)
session.login(sender_email, password)

with open('test_2.html', 'r', encoding="utf8") as file:
    data = file.read().replace('\n', '')
count = 0

with open("mail_list.csv") as file:
    reader = csv.reader(file)
    next(reader)
    for name, email, link in reader:
        # Create the plain-text and HTML version of your message
        html = data.format(name=name, link=link)

        # Add HTML/plain-text parts to MIMEMultipart message
        # The email client will try to render the last part first
        message.attach(MIMEText(html, "html"))

        session.sendmail(
            sender_email, email, message.as_string()
        )

        count += 1
        print(str(count) + ". Sent to " + email)

        if(count%80 == 0):
            session.quit()
            print("Server cooldown for 100 seconds")
            time.sleep(100)
            session.starttls(context = context)
            session.login(sender_email, password)

session.quit()