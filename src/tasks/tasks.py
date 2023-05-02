import smtplib

from email.message import EmailMessage

from celery import Celery

from src.tasks.config import smtp_settings


celery = Celery('tasks', broker="redis://localhost:6379")


@celery.task
def send_welcome_email(username: str, user_email: str):
    email = EmailMessage()
    email['Subject'] = 'Рады вас приветствовать!'
    email['From'] = smtp_settings.user
    email['To'] = f'{user_email}'

    email.set_content(
        '<div>'
        f'<h1>Здравствуйте, {username}. Спасибо за регистрацию!🤩</h1>'
        '</div>',
        subtype='html'
    )
    with smtplib.SMTP_SSL(smtp_settings.host, smtp_settings.port) as server:
        server.login(smtp_settings.user, smtp_settings.password)
        server.send_message(email)

