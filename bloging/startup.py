from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

import smtplib

smtp_server = smtplib.SMTP("smtp.yandex.ru", 587)  # Введите свои данные/настройки
smtp_server.starttls()
smtp_server.login("sender email", "your password")  # Введите свои данные/настройки

msg = MIMEMultipart()
msg["From"] = "sender email"  # Введите свои данные/настройки
msg["To"] = "recipient email"  # Введите свои данные/настройки
msg["Subject"] = "Тестовое письмо от Django"  # Введите свои данные/настройки

text = "Привет! Это тестовое письмо, отправленное с помощью Python-Django"
msg.attach(MIMEText(text, "plain"))


def send_congratulation_mail():
    smtp_server.sendmail("dsmile-python@yandex.ru", "Simpson6515@yandex.ru", msg.as_string())
    smtp_server.quit()
