import pandas as pd
import smtplib

e = pd.read_excel("data1.xlsx") # write the location and xlsx file
email = e['Email'].values

print(email)


# setting server

server = smtplib.SMTP("smtp.gmail.com",587)
server.starttls()
# for login into account
server.login('email here','password here')
msg = """\

Type your message here

"""
subject = "Event Invitation"
body = "Subject:{}\n\n{}".format(subject,msg)

for emails in email:
    server.sendmail("your email",emails,body)
    print("Email send")
server.quit()    

