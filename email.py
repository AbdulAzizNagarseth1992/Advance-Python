import smtplib
import datetime as dt
import random
import email.csv


my_email = 'abdulaziznagarseth@gmail.com'
password = 'kzvo rnvh awip jvxj'

now = dt.datetime.now()
weekday = now.weekday()

if weekday == 0:
    with open("quotes.txt") as file:
        all_quotes = file.readlines()
        quote = random.choice(all_quotes)

    print(quote)

with smtplib.SMTP("smtp.gmail.com", 587, timeout=120) as connection:
    connection.starttls()
    connection.login(my_email, password)
    connection.sendmail(
        from_addr=my_email,
        to_addrs=email.csv,
        msg=f"Subject:Monday Motivation\n\n{quote}")