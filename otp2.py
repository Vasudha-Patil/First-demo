import random
import smtplib
from twilio.rest import Client

# Generate a 6-digit OTP
def generateOTP():
    return str(random.randint(100000, 999999))

# Send OTP over email using SMTP
def sendOTPOverEmail(email, otp):
    smtp_server = 'smtp.gmail.com'  # Replace with your SMTP server
    smtp_port = 587  # Replace with your SMTP port (e.g., 587 for TLS)
    smtp_username = 'vasudhavenkatpatil@gmail.com'  # Replace with your email
    smtp_password = 'qtbwgpqawlsxwcxc'  # Replace with your email password

    subject = 'Your OTP'
    message = f'Your OTP is: {otp}'

    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(smtp_username, smtp_password)

        msg = f'Subject: {subject}\n\n{message}'
        server.sendmail(smtp_username, email, msg)
        server.quit()
        print('OTP sent successfully via email!')
    except Exception as e:
        print(f'Error sending OTP via email: {str(e)}')

# Send OTP over mobile using Twilio (optional)
def sendOTPOverMobile(phone_number, otp):
    twilio_account_sid = 'AC72f0a54b0fa300722c44c88847dc4ce3'  # Replace with your Twilio Account SID
    twilio_auth_token = '7441917e6d04f7d9da7b6514fa5a41cc'    # Replace with your Twilio Auth Token

    try:
        client = Client(twilio_account_sid, twilio_auth_token)
        message = client.messages.create(
            to=phone_number,
            from_='+15418358453',  # Replace with your Twilio phone number
            body=f'Your OTP is: {otp}'
        )
        print('OTP sent successfully via Twilio!')
    except Exception as e:
        print(f'Error sending OTP via Twilio: {str(e)}')

# Validate an email address with basic check
def validateEmail(email):
    return '@' in email and '.' in email

# Validate a mobile number (basic check)
def validateMobile(mobile):
    return len(mobile) == 10 and mobile.isdigit()

# User input for email
email = input('Enter your email address: ')
if validateEmail(email):
    otp = generateOTP()
    sendOTPOverEmail(email, otp)
else:
    print('Invalid email address!')

# Optional: User input for mobile number (Twilio)
use_twilio = input('Do you want to send OTP via Twilio? (yes/no): ')
if use_twilio.lower() == 'yes':
    mobile = input('Enter your mobile number: ')
    if validateMobile(mobile):
        sendOTPOverMobile('+91' + mobile, otp)  # Replace '+1' with your country code
    else:
        print('Invalid mobile number!')