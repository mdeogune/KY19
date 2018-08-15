import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

msg = MIMEMultipart()
msg['From'] = 'kashiyatra@iitbhu.ac.in'
msg['To'] = 'rishabh.ag342@gmail.com'
msg['Subject'] = 'simple email in python'
message = 'here is the email'
msg.attach(MIMEText(message))

mailserver = smtplib.SMTP('smtp.gmail.com', 587)
# identify ourselves to smtp gmail client
mailserver.ehlo()
# secure our email with tls encryption
mailserver.starttls()
# re-identify ourselves as an encrypted connection
mailserver.ehlo()
mailserver.login('kashiyatra@itbhu.ac.in', 'biggerandbetter18')

mailserver.sendmail('Kashiyatra','rishabh.ag342@gmail.com',msg.as_string())

mailserver.quit()