import os
import smtplib

EMAIL_ADDRESS = os.environ.get('SENDER_EMAIL_LOGIN')
EMAIL_PASSWORD = os.environ.get('SENDER_EMAIL_PASS')

with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.ehlo()

    smtp.login(SENDER_EMAIL_ADDRESS, SENDER_EMAIL_PASSWORD)

    subject = "You're closer than you think!"
    body = 'I know that it might be difficult, but please... never give up! We all believe in you!'

    msg = f'Subject: {subject}\n\n{body}'

    smtp.sendmail(SENDER_EMAIL_ADDRESS, RECEIVER_EMAIL_ADDRESS, msg)
