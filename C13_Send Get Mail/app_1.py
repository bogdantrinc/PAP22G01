import smtplib


from email.message import EmailMessage


mail_text = """
Body would go here
"""
msg = EmailMessage()
msg.set_content(mail_text)

print(msg)
msg['Subject'] = f'The contents of Body would go here'
msg['From'] = "utilizatorultau@gmail.com"
msg['To'] = 'bogdan_tranc@yahoo.com'
print(msg)
s = smtplib.SMTP_SSL('smtp.gmail.com', 465)
s.login(user='utilizatorultau@gmail.com', password='unutilizatorrandom')
s.send_message(msg)
s.quit()