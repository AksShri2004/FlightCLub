from twilio.rest import Client
import smtplib
import users
import os

TWILIO_SID = os.getenv('TWILIO_SID')
TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")
TWILIO_VIRTUAL_NUMBER = os.getenv('TWILIO_VIRTUAL_NUMBER')
TWILIO_VERIFIED_NUMBER = os.getenv('TWILIO_VERIFIED_NUMBER')


class NotificationManager():

    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)
        # self.user = users.Post_User()

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_=TWILIO_VIRTUAL_NUMBER,
            to=TWILIO_VERIFIED_NUMBER,
        )
        # Prints if successfully sent.
        print(message.sid)
      

    def send_email(self, message):
        import requests
        
        self.my_email = str(os.getenv("my_email"))
        self.password = str(os.getenv("my_password"))
        self.endpoint = str(os.getenv("sheety_users_endpoint"))
      
        get_request = requests.get(url=self.endpoint)
        data = get_request.json()["users"]
        self.mail_list = [data["email"] for data in data]
        print(self.mail_list)
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=self.my_email, password=self.password)
            for n in self.mail_list:
                connection.sendmail(from_addr=self.my_email, to_addrs=n, msg=message)
          
          
