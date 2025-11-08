import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv
import os

load_dotenv()

smtp_server = os.getenv("SMTP_SERVER")
smtp_port = os.getenv("SMTP_PORT")
sender_email = os.getenv("SENDER_EMAIL")
email_password = os.getenv("EMAIL_PASSWORD")

def send_email(recipient, subject,  body):

    try:
            message = MIMEMultipart()
            message["FROM"] = sender_email
            message["TO"] = recipient
            message["Subject"] = subject
            message.attach(MIMEText(body, "plain"))
        # Setup server
            server = smtplib.SMTP(smtp_server, smtp_port)

            server.starttls()

        # Logging to mail
            server.login(sender_email, email_password)

        # Send mail
            server.sendmail(sender_email, recipient, message.as_string())
            server.quit()
            return True, "Sent Successfully"

    except Exception as e:
        
          return False, f'Unable to send mail: {e}'
    

