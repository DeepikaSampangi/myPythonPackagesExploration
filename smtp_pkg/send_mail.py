import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


from_id = 'deepikasampangi@gmail.com'
to_id = 'deepikasampangi@gmail.com'
message = MIMEMultipart('alternative')
message['From'] = 'deepikasampangi@gmail.com'
message['To'] = 'deepikasampangi@gmail.com'
message['Subject'] = 'Trial from Script'
body = MIMEText('Heyy There, trials mail','text')
message.attach(body)

try:
    s = smtplib.SMTP('smtp.gmail.com','587')
    s.ehlo()
    s.starttls()
    s.ehlo()
    s.sendmail(from_id,to_id,message.as_string())
except Exception as exc:
    print("Failed:", str(exc))


