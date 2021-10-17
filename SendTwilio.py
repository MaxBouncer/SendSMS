from os import error
from twilio.rest import Client
from decouple import config
import logging


# Enviando SMS pelo Twilio
class SendSMS:

    def __init__(self, numero, mensagem):
        self.__numero = numero
        self.__mensagem = mensagem

    def sendTwilio(self):
        account_sid = config('account_sid')
        auth_token = config('auth_token')
        from_ = config('from_')

        client = Client(account_sid, auth_token)

        try:
            client.api.account.messages.create(
                to=self.__numero,
                from_=config('from_'),
                body=self.__mensagem,
            )
        except:
            logging.error('Problema ao enviar SMS.')
        else:
            logging.info('Mensagem SMS enviada.')


sms = SendSMS('', 'Teste')
sms.sendTwilio()
