import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Sender and receiver info
sender_email = "mdabucse@gmail.com"
receiver_email = "mohamedabubakkar.s2022ai-ds@sece.ac.in"
password = "yosr hgyo zheh pnjg "  # Use App Password if 2FA is enabled

# Create the email
message = MIMEMultipart("alternative")
message["Subject"] = "Test Email from Python"
message["From"] = sender_email
message["To"] = receiver_email

# Email body
text = "Hi,\nThis is a test email sent from Python."
html = """\
<html>
  <body>
    <p>Hi,<br>
       This is a <b>test email</b> sent from <i>Python</i>.
    </p>
  </body>
</html>
"""

# Attach text and HTML parts
part1 = MIMEText(text, "plain")
part2 = MIMEText(html, "html")
message.attach(part1)
message.attach(part2)

# Send email using Gmail's SMTP server
try:
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message.as_string())
    print("Email sent successfully!")
except Exception as e:
    print(f"Error: {e}")
