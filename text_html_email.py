### Text/ HTML Email -> for Gmail
import os
import smtplib
from email.message import EmailMessage
import time
import pandas as pd

start_time = time.time()
### Credentials
def read_credentials():
    userId = password = ""
    with open('credentials.txt','r') as f:
        file = f.readlines()
        userId = file[0].strip()
        password = file[1].strip()
        return userId, password
EMAIL_ADDRESS,EMAIL_PASSWORD = read_credentials()
### Email Subject
with open('subject.txt','r') as f:
        subject = f.readlines()
        subject = "".join(subject)
### Email Body
with open('body.txt','r') as f:
        body = f.readlines()
        body = "".join(body)
### Contacts
df = pd.read_excel('contacts.xlsx')
mylist = df['contacts'].tolist()
contacts = []
for index in range(len(mylist)):
        contacts.append(mylist[index].strip())
### Message
msg = EmailMessage()
msg['Subject'] = subject 
msg['From'] = EMAIL_ADDRESS
msg['To'] = contacts
msg.set_content(body)
### HTML Alternative
msg.add_alternative("""\
<!DOCTYPE html>
<html>
    <body>
        <h1 style="color:SlateGray;">This is an HTML Email!</h1>
    </body>
</html>
""", subtype = 'html')

# we use SSL Encryption now
with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp: # 465 port number
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
    smtp.send_message(msg)

total_time = (time.time() - start_time)/60
os.system('clear')
print("Email(s) sent in {:.2f} minutes.".format(total_time),'\n')
print("------------------ Emailing Complete ------------------",'\n')