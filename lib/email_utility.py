import smtplib
from email.message import EmailMessage

class email_utility:
    def __init__(self, _email, _password):
        self.email = _email
        self.email_password = _password

    def send_email(self, msg): 
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.login(self.email, self.email_password)
        server.send_message(msg)
        server.close()



