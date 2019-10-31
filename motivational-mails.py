import os
import smtplib
import imghdr
from email.message import EmailMessage
from datetime import date

SENDER_EMAIL_ADDRESS = os.environ.get('SENDER_EMAIL_LOGIN')
SENDER_EMAIL_PASSWORD = os.environ.get('SENDER_EMAIL_PASS')
RECEIVER_EMAIL_ADDRESS = os.environ.get('RECEIVER_EMAIL_LOGIN')

contacts = [RECEIVER_EMAIL_ADDRESS, 'doniak9@gmail.com', SENDER_EMAIL_ADDRESS]

msg = EmailMessage()
msg['Subject'] =  'Daily motivational message | DMM | As of ' + str(date.today())
msg['From'] = SENDER_EMAIL_ADDRESS
msg['To'] = ', '.join(contacts)
msg.set_content('I know that it might be difficult, but please... never give up! We all believe in you!')

with open('Ds6S7lJ.png', 'rb') as f:
    file_data = f.read()
    file_type = imghdr.what(f.name)
    file_name = f.name

msg.add_attachment(file_data, maintype='image', subtype=file_type, filename=file_name)

with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(SENDER_EMAIL_ADDRESS, SENDER_EMAIL_PASSWORD)

    smtp.send_message(msg)
