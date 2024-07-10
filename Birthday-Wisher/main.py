from datetime import datetime
import pandas
import random
import smtplib

today = (datetime.now().month, datetime.now().day)

MY_EMAIL = ""  # enter email to send from in the quotes
MY_PASSWORD = ""  # enter app password for email in the quotes

data = pandas.read_csv("birthdays.csv")
birthday_dict = {(data_row.month, data_row.day): data_row for (index, data_row) in data.iterrows()}

if today in birthday_dict:
    person = birthday_dict[today]
    letter_template = f"./letter-templates/letter_{random.randint(1, 3)}.txt"
    with open(letter_template) as file:
        contents = file.read()
        new_contents = contents.replace("[NAME]", person["name"])

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL, to_addrs=person["email"],
                            msg=f"Subject:Happy Birthday!\n\n{new_contents}")
