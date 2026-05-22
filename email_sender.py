import smtplib

from email.mime.text import MIMEText

from email.mime.multipart import MIMEMultipart


def send_email(
    receiver_email,
    subject,
    message
):

    sender_email = "himanshuvijay23@gmail.com"

    app_password = "iiow zjzn ypzo ttzk"


    # Create Message
    msg = MIMEMultipart()

    msg["From"] = sender_email

    msg["To"] = receiver_email

    msg["Subject"] = subject


    # Email Body
    msg.attach(
        MIMEText(message, "plain")
    )


    # Connect Gmail Server
    server = smtplib.SMTP(
        "smtp.gmail.com",
        587
    )

    server.starttls()


    # Login
    server.login(
        sender_email,
        app_password
    )


    # Send Email
    server.send_message(msg)

    server.quit()