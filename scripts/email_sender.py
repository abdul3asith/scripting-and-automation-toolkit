import smtplib
from email.message import EmailMessage
import os
from dotenv import load_dotenv
from pathlib import Path
import schedule
import time

# env_path = Path(__file__).resolve().parents[1] / ".env"

# from_email = os.getenv("EMAIL_USER")
# app_password = os.getenv("EMAIL_PASS")

# if not from_email or not app_password:
#     raise Exception("❌ Email or App Password not found in environment variables!")



# load_dotenv(dotenv_path=env_path)
def email_send(subject, body, to_email, from_email, app_password, attachment_path=None):
    message = EmailMessage()
    message["Subject"] = subject
    message["From"] = from_email
    message["To"] = to_email
    message.set_content(body)

    if attachment_path and os.path.exists(attachment_path):
        with open(attachment_path, "rb") as f:
            file_data = f.read()
            file_name = os.path.basename(attachment_path)
            message.add_attachment(file_data, maintype="application", subtype="octet-stream", filename=file_name)

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(from_email, app_password)
        smtp.send_message(message)


    print("Email has been sent")


if __name__ == "__main__":
    subject = input("Subject: ")
    body = input("Body: ")
    to = input("Recipient Email: ")
    attachment = input("attachment: ")
    from_email = 'your_email'
    app_password = 'your_password'

    email_send(subject, body, to, from_email, app_password, attachment or None)


# schedule.every().day.at("14:30").do(email_send)


# while True:
#     schedule.run_pending()
#     time.sleep(1)

# scope - database of subject, recipients, body and send at scheduled time

