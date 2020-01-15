import os
import smtplib
import imghdr
from email.message import EmailMessage
from datetime import date
import time
import urllib.request
import requests
from bs4 import BeautifulSoup
from random import randint
import re

SENDER_EMAIL_ADDRESS = os.environ.get('SENDER_EMAIL_LOGIN')
SENDER_EMAIL_PASSWORD = os.environ.get('SENDER_EMAIL_PASS')

rsp = input('Please, enter your e-mail address: ')
try:
    if rsp != "":
        RECEIVER_EMAIL_ADDRESS = rsp
    else:
        RECEIVER_EMAIL_ADDRESS = os.environ.get('RECEIVER_EMAIL_LOGIN')
except:
    print("unknown error occured")
    exit

contacts = [RECEIVER_EMAIL_ADDRESS, SENDER_EMAIL_ADDRESS]
url = 'https://www.goodreads.com/quotes/tag/inspiration?page=' + str(randint(1,100))
response = requests.get(url)

if response.status_code != 200:
    msg_content = 'It seems that Goodreads mirror is offline for some reason... however, don\'t give up!'
else:
    soup = BeautifulSoup(response.text, "html.parser")
    [x.extract() for x in soup.findAll('script')]
    tags = soup.find_all(class_="quoteText")
    tag_number = randint(0,len(tags)-1)
    tag_content = tags[tag_number]
    
    # content of the quote
    tag_quote = tag_content.text.strip()
    tag_quote = str(re.sub('\n','',tag_quote))
    msg_content = tag_quote

msg = EmailMessage()
msg['Subject'] =  'Daily motivational message | DMM | ' + str(date.today())
msg['From'] = SENDER_EMAIL_ADDRESS
msg['To'] = ', '.join(contacts)
msg.set_content("Quote of the day: \n\n" + msg_content)

with open('Ds6S7lJ.png', 'rb') as f:
    file_data = f.read()
    file_type = imghdr.what(f.name)
    file_name = f.name

msg.add_attachment(file_data, maintype='image', subtype=file_type, filename=file_name)

with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(SENDER_EMAIL_ADDRESS, SENDER_EMAIL_PASSWORD)
    smtp.send_message(msg)

print("Message has been sent successfully")