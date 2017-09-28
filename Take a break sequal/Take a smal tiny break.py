__author__ = 'shabadlamba'

import webbrowser
from twilio.rest import TwilioRestClient
import time


while (True):
    time.sleep(10)
    webbrowser.open("https://www.youtube.com/watch?v=lsSC2vx7zFQ")

    time.sleep(10)
    # Your Account Sid and Auth Token from twilio.com/user/account
    account_sid = "AC591ab9edc48cd1af73639f9478fb4953"
    auth_token  = "b831db490e010e62c01a66a9f0502df1"
    client = TwilioRestClient(account_sid, auth_token)

    message = client.messages.create(
        body="Time's Up!! Back to Work",
        to="+91 9673261664",  # Replace with your phone number
        from_="+1 201-897-6022") # Replace with your Twilio number
    print message.sid

    input = raw_input("Wanna rest set timer?(Y/N)")

    if input in "Nn":
        break