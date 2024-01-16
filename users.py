class CreateUser:
  def __init__(self):
    self.first_name = input("Enter your First name: ")
    self.last_name = input("Enter you Last Name: ")
    self.email = input("Enter your Email: ")
    self.confirm_email = input("Confirm your Email: ")

  def email_check(self):
    if self.email == self.confirm_email:
      print("You are in the club!")

class Post_User(CreateUser):
  def __init__(self):
    super().__init__()
    self.user_data = {
      "user" :
      {
        "firstName" : self.first_name,
        "lastName" : self.last_name,
        "email" : self.email
      }
    }
    import requests
    import os
    self.endpoint = str(os.getenv("sheety_users_endpoint"))
    if self.email == self.confirm_email:
      post_request = requests.post(url = self.endpoint, json = self.user_data)
      print(post_request.text)
