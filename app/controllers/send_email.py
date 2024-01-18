from flask import render_template

from app.services.aws.email import EmailService
from config import Config


class SendEmail:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def reset_pass(self, code):
        code_pass = code
        subject = "Resetar Senha"
        path_file = 'email/reset_with_code.html'
        body = render_template(path_file,
                               name=self.name,
                               code=code_pass)

        EmailService().send_aws(RECIPIENT=self.email, SUBJECT=subject, TEXT=body)

    def welcome_user_admin(self, password):
        subject = "Seja Bem Vindo"
        path_file = 'email/welcome_admin.html'
        admin_url = Config.ADMIN_HTTPS
        body = render_template(path_file,
                               name=self.name,
                               email=self.email,
                               password=password,
                               admin_url=admin_url)

        EmailService().send_aws(RECIPIENT=self.email, SUBJECT=subject, TEXT=body)

    def welcome_client(self, password):
        subject = "Seja Bem Vindo"
        path_file = 'email/welcome_client.html'
        body = render_template(path_file,
                               name=self.name,
                               email=self.email,
                               password=password)

        EmailService().send_aws(RECIPIENT=self.email, SUBJECT=subject, TEXT=body)
