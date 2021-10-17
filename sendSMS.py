from twilio.rest import Client
import mysql.connector
import logging
from SendTwilio import smsTwilio
from datetime import date
from decouple import config as conf

data = str(date.today())
print(data)

if __name__ == '__main__':
    logging.basicConfig(
        level=logging.DEBUG,
        format='%(asctime)s %(name)s %(levelname)s %(message)s',
        # filename=data + 'send_sms.log',
        filename='/home/roberto/send_sms/logs/send_sms.log',
        filemode='a',
    )
    logging.getLogger(__name__)
    logging.debug('Send_SMS initialized')


def __init__(self):
    logging.getLogger(__name__)
    logging.debug('Send_SMS initialized')
    print('AQUIIII')


class Send_SMS():

    # Consulta banco MySQL para saber se tem jogo hoje.

    def jogos():

        config = {
            'user': conf('user'),
            'password': conf('password'),
            'host': conf('host'),
            'database': conf('database')
        }

        conn = mysql.connector.connect(**config)
        curr = conn.cursor()

        try:
            jogos = curr.execute(
                "SELECT DISTINCT * FROM proximosjogos WHERE str_to_date(data, '%d/%m/%Y') = '17/10/2021'")
        except Exception as erro:
            print(erro)
        finally:
            conn.close()

        return jogos

    jogo = jogos()
    print(jogo)

#     def sendSMS():
#         config = {
#             'user': 'tabela',
#             'password': 'P@ssW0rd',
#             'host': 'srv-mysql-prd',
#             'database': 'tabela',
#             # 'raise_on_warnings': True # DA EXEÇÃO EM CASO DE WARNINGS
#         }
#         conn = mysql.connector.connect(**config)
#         curr = conn.cursor()
#         jogos = ''
#         mensagem = ''

#         try:
#             logging.debug('Consultando base para pegar os jogos do dia.')
#             curr.execute("SELECT DISTINCT nrodada, partida, data, hora, man_sigla, man_nome, vis_sigla, vis_nome, local FROM proximosjogos \
#                 WHERE str_to_date(data, '%d/%m/%Y') = curdate() \
#                 AND serie = 'A' AND (man_sigla = 'FLA' or vis_nome = 'FLA') ORDER BY str_to_date(data, '%d/%m/%Y')")
#             jogos = curr.fetchone()
#         except Exception as erro:
#             logging.warning('Erro ao buscar jogos.')
#             print(erro)
#         except ConnectionError as erro:
#             logging.error('Erro ao se conectar a base de dados.')
#             print(erro)
#         finally:
#             conn.close()
#             logging.debug('Fechando conexão com banco')

#         if jogos:
#             nrodada, partida, data, hora, man_sigla, man_nome, vis_sigla, vis_nome, local = jogos[
#                 0]
#             mensagem = (f'\nHoje tem emoção, hoje tem jogo do Mengão!\nàs {hora}h teremos a partida {partida} \
#         pela {nrodada}º rodada do campeonato Brasileiro. {man_nome} vs {vis_nome} no estádio do {local}')

#             smsTwilio("", mensagem)
#             # Enviando SMS pelo Twilio
#             # account_sid = ''
#             # auth_token = ''
#             # client = Client(account_sid, auth_token)
#             # client.api.account.messages.create(
#             #     to="+",
#             #     from_="+",
#             #     body=mensagem,
#             # )
#             logging.info('Mensagem SMS enviada.1')

#         else:
#             mensagem = ('sem jogos')
#             logging.debug('Não há SMS à ser enviada. (Não há jogos).')

#     # # Enviando SMS pelo TeleSign
#     # customer_id = ""
#     # api_key = ""

#     # phone_number = ""
#     # message_type = "ARN"


# Send_SMS.sendSMS()
