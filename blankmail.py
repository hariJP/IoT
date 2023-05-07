import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# login credentials
username = 'h4r1pr4s47h@gmail.com'
password = 'termuxwave'

# message information
from_addr = 'h4r1pr4s47h@gmail.com'
to_addr = 'jhp952003@gmail.com'
subject = 'Test Email'
body = 'This is a test email sent using Python!'

# create message object
msg = MIMEMultipart()
msg['From'] = from_addr
msg['To'] = to_addr
msg['Subject'] = subject

# add body to message
msg.attach(MIMEText(body, 'plain'))

# create SMTP session and send email
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(username, password)
text = msg.as_string()
server.sendmail(from_addr, to_addr, text)
server.quit()

print('Email sent successfully!')
