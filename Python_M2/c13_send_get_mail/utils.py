
import smtplib


from email.message import EmailMessage


mail_text = """
Body would go here
"""
msg = EmailMessage()
msg.set_content(mail_text)

print(msg)
msg['Subject'] = f'The contents of Body would go here'
msg['From'] = "abcd@abcdefoiashd.com"
msg['To'] = 'ozy24us@gmail.com'

username_ = 'pinkiwinkiwinki555'
password_ = '1234pinki'

print(msg)
s = smtplib.SMTP_SSL('smtp.gmail.com', 465)
s.login(user=username_, password=password_)
s.send_message(msg)
s.quit()