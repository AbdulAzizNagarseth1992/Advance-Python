import smtplib
import schedule
import time
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587 
SMTP_USERNAME = 'abdulaziznagarseth@gmail.com'
SMTP_PASSWORD = 'LOREM ISPUM LOREM ISPUM'
FROM_EMAIL = 'abc@gmail.com'
TO_EMAIL = 'def@gmail.com'
SUBJECT = 'Scheduled Email'

def send_email():
    message = MIMEMultipart()
    message['From'] = FROM_EMAIL
    message['To'] = TO_EMAIL
    message['Subject'] = SUBJECT
    body = 'This is a scheduled email sent using Python and Gmail.'
    message.attach(MIMEText(body, 'plain'))

    try:
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(SMTP_USERNAME, SMTP_PASSWORD)
            server.send_message(message)
            print('Email sent successfully!')
    except Exception as e:
        print(f'Error: {e}')

schedule.every().day.at("10:00").do(send_email)

while True:
    schedule.run_pending()
    time.sleep(60)
