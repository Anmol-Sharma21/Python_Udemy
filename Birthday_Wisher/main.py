import smtplib

my_email = "anmol.pythontest@gmail.com"
my_password = "vyitymcetjrepnqz"

with smtplib.SMTP("smtp.gmail.com", 587) as connection:
    connection.starttls()
    connection.login(user=my_email, password=my_password)
    connection.sendmail(from_addr=my_email, to_addrs="anmol.pythontest@yahoo.com", msg="Subject: Hello\n\nThis is a test email.")


# import datetime as dt
#
# now = dt.datetime.now()
# print(now)