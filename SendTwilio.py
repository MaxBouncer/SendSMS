from twilio.rest import Client
from decouple import config
import logging


# Enviando SMS pelo Twilio


# smsTwilio('+5521988857740', 'Teste 3')


class SendSMS:

    def __init__(self, numero, mensagem) -> None:
        self.numero = numero
        self.mensagem = mensagem

    def sendTwilio(numero, mensagem):
        account_sid = config('account_sid')
        auth_token = config('auth_token')
        from_ = config('from_')

        client = Client(account_sid, auth_token)

        # client.api.account.messages.create(
        #     to=numero,
        #     from_=config('from'),
        #     body=mensagem,
        # )
        logging.info('Mensagem SMS enviada.')
        print('passei aqui')
        print(f'{numero} e {mensagem}')
        print(f'{account_sid} & {auth_token} & {from_}')

    # sendTwilio('+5521988857740', 'Teste 3')


SendSMS.sendTwilio('A', 'B')
