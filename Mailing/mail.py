# import smtplib

# message = """From: From Person aiswaryasaravanan1998@gmail.com
# To: To Person aishuat006@gmail.com
# Subject: Sending SMTP e-mail
# This is a test e-mail message.
# """

# try:
#     smtplib.SMTP('gmail.com',587).sendmail("aiswaryasaravanan1998@gmail.com","aishuat006@gmail.com",message)
#     print("Sent successfully")
# except Exception:
#     print("Sorry:(")


# Not coming :(


import smtplib
sender_mail = 'aiswaryasaravanan1998@gmail.com'
receivers_mail = ['aishuat006@gmail.com']
message = """From: From Person %s 
To: To Person %s 
Subject: Sending SMTP e-mail  
This is a test e-mail message. 
""" % (sender_mail, receivers_mail)
try:
    password = input('Enter the password')
    smtpObj = smtplib.SMTP('gmail.com', 587)
    smtpobj.login(sender_mail, password)
    smtpObj.sendmail(sender_mail, receivers_mail, message)
    print("Successfully sent email")
except Exception:
    print("Error: unable to send email")
    print(Exception)
