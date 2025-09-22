# The smtplib module allows Python applications to send emails, which is crucial for features like user registration, password reset, and notifications.

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(sender, recipient, subject, body):
    # Create message
    msg = MIMEMultipart()
    msg['From'] = sender
    msg['To'] = recipient
    msg['Subject'] = subject
    
    # Add body to email
    msg.attach(MIMEText(body, 'plain'))
    
    # Send email
    try:
        server = smtplib.SMTP('localhost')  # Use your SMTP server
        server.sendmail(sender, recipient, msg.as_string())
        server.quit()
        print("Email sent successfully")
    except Exception as e:
        print(f"Error sending email: {e}")

# Example usage
send_email(
    'noreply@example.com', 
    'user@example.com', 
    'Welcome to Our Service', 
    'Thank you for registering with our service.'
)

# For production web applications, you would typically use more robust email handling with proper error handling, HTML content, and potentially asynchronous processing .

