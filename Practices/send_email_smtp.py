import smtplib
from socket import gaierror



port = 2525 
smtp_server = "smtp.mailtrap.io"
login = "--------------" # your login generated by Mailtrap
password = "-------------" # your password generated by Mailtrap

# specify the sender’s and receiver’s email addresses
sender = "automatic_email@test.com"
receiver = "mailtrap@example.com"

# type your message: use two newlines (\n) to separate the subject from the message body, and use 'f' to  automatically insert variables in the text
message = f"""\
Subject: Dear User
To: {receiver}
From: {sender}

This is my First automatic Email sent using SMTP Protocol."""

try:
    #send your message with credentials specified above
    with smtplib.SMTP(smtp_server, port) as server:
        server.login(login, password)
        server.sendmail(sender, receiver, message)

    # tell the script to report if your message was sent or which errors need to be fixed 
    print('Sent')
except (gaierror, ConnectionRefusedError):
    print('Failed to connect to the server. Bad connection settings?')
except smtplib.SMTPServerDisconnected:
    print('Failed to connect to the server. Wrong user/password?')
except smtplib.SMTPException as e:
    print('SMTP error occurred: ' + str(e))

input("Press any key to continue")