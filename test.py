import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Replace these with your details
your_email = 'anasshaaban@yahoo.com'
your_app_password = 'ljeghppuzyixrmeg'  # Use your app-specific password here
recipient_email = 'anooshani@yahoo.com'

# Create the MIME message
msg = MIMEMultipart()
msg['From'] = your_email
msg['To'] = recipient_email
msg['Subject'] = 'Test Email from Python'
body = 'This is a test email sent from a Python script using Yahoo SMTP.'
msg.attach(MIMEText(body, 'plain'))

# Send the email
try:
    server = smtplib.SMTP('smtp.mail.yahoo.com', 587)
    server.set_debuglevel(1)  # Enable debug output to see the communication with the server
    server.starttls()
    server.login(your_email, your_app_password)
    text = msg.as_string()
    server.sendmail(your_email, recipient_email, text)
    server.quit()
    print("Email sent successfully!")
except Exception as e:
    print(f"Failed to send email: {e}")