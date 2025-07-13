import smtplib
from email.mime.text import MIMEText

def send_email(jobs, settings):
    body = "\n\n".join(
        f"{i+1}. {job['title']} ({job['location']})\nSource: {job['source']}\nPossibility: {job['possibility']}\nLink: {job['link']}"
        for i, job in enumerate(jobs)
    )
    msg = MIMEText(body)
    msg['Subject'] = '🌍 UAV Jobs Abroad (Today)'
    msg['From'] = settings['email']
    msg['To'] = settings['receiver']

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
        server.login(settings['email'], settings['password'])
        server.send_message(msg)
