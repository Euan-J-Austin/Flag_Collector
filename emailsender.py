import smtplib
import ssl
from email.message import EmailMessage

def send_email(recipient):
    email_receiver = recipient
    subject = 'Ello!'
    body = f"""
    Greetings,
    Ello, ello. Helloo.
    """
    em = EmailMessage()
    em['From'] = 'noah.flagcollector@gmail.com'
    em['To'] = str(recipient) 
    em['Subject'] = subject
    em.set_content(body)
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login('noah.flagcollector@gmail.com', passkey)
        smtp.sendmail('noah.flagcollector@gmail.com', email_receiver, em.as_string())

send_email('elvismonarchy@proton.me')