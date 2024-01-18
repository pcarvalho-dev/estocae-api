from app.services.aws import ses
from config import Config


class EmailService(object):
    def __init__(self, *args, **kwargs):

        self.conn = ses

    def send_aws(self, RECIPIENT, SUBJECT, TEXT,
                 SENDER=Config.AWS_EMAIL_SENDER):
        """
        It sends an email.
        
        :param RECIPIENT: The email address of the recipient
        :param SUBJECT: The subject of the email
        :param TEXT: The body of the email
        :param SENDER: The email address that will be shown as the sender of the email, defaults to
        comunidadecis@febracis.com.br (optional)
        :return: The response from the send_email method.
        """
                 

        CHARSET = "UTF-8"
        BODY_TEXT = TEXT
        BODY_HTML = TEXT
        try:
            response = self.conn.send_email(
                Destination={
                    'ToAddresses': [
                        RECIPIENT,
                    ],
                },
                Message={
                    'Body': {
                        'Html': {
                            'Charset': CHARSET,
                            'Data': BODY_HTML,
                        },
                        'Text': {
                            'Charset': CHARSET,
                            'Data': BODY_TEXT,
                        },
                    },
                    'Subject': {
                        'Charset': CHARSET,
                        'Data': SUBJECT,
                    },
                },
                Source=SENDER
            )
            if response['ResponseMetadata']['HTTPStatusCode'] == 200:
                return True
            else:
                return False
        except:
            return False
