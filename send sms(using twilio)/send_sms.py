from twilio.rest import TwilioRestClient
import time

for i in range(1):
    # Your Account Sid and Auth Token from twilio.com/user/account
    account_sid = "AC591ab9edc48cd1af73639f9478fb4953"
    auth_token  = "b831db490e010e62c01a66a9f0502df1"
    client = TwilioRestClient(account_sid, auth_token)
     
    message = client.messages.create(
        body="You are Dude Bro!!",
        to="+91 9673261664",  # Replace with your phone number
        from_="+1 (201) 897-6022") # Replace with your Twilio number
    #print message.sid
    print message.error_message
    time.sleep(10)
