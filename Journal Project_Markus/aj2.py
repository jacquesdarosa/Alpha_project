import os
import time
import datetime
import smtplib # optional and advanced 
from colorama import * # optional
from art      import * # optional
from email.mime.multipart                        import * # optional and advanced 
from email.mime.text                             import * # optional and advanced 
from email.message                               import * # optional and advanced 


 # email function 14 # optional and advanced 

def gmail_send(subject, message, from_mail, to, password):
    global link
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(from_mail, password)
    msg            = EmailMessage()
    message        = f'{message}'
    msg.set_content(message)
    msg['Subject'] = subject
    msg['From']    = from_mail
    msg['To']      = to
    server.send_message(msg)

now       = datetime.datetime.today().strftime("%H:%M:%S %d-%m-%Y")
print(now)

# display current journal
# art

new_entry = input("ENTER DIARY ENTRY HERE >>>")
with open("journal.txt", "a") as file:
    file.write(now + "" + new_entry + "\n")


