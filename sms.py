from twilio import rest

# Your Account Sid and Auth Token form twilio.com/user/account
account_sid = "AC7138e23293a48e12392dc7f483956873"
auth_token = "1653d56be5c4a5ccbbf7237ad62d4b39"
client = rest.TwilioRestClient(account_sid, auth_token)

message = client.sms.message.create(
	body ="hi somendra how are you",
	to ="+919089620677",   #Replace with your phone number
	from_="+12014250896")  #Replace with your twilio number

print(message.sid)
