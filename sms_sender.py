from twilio.rest import Client

# Twilio account SID and authentication token
account_sid = 'Enter your twillio sid'
auth_token = 'Enter token id'

def send_sms(phone_number, message):
    client = Client(account_sid, auth_token)

    try:
        message = client.messages.create(
            body=message,
            from_="Enter twillio phone number",
            to=phone_number
        )
        print("SMS sent successfully!")
        print("Message SID:", message.sid)
    except Exception as e:
        print("An error occurred while sending the SMS:", str(e))


def main():
    phone_number = input("Enter the phone number (including the country code): ")
    message = input("Enter the message: ")

    send_sms(phone_number, message)


if __name__ == '__main__':
    main()
