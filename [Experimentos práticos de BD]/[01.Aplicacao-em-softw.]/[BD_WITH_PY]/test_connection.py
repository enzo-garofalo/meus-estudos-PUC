# # Importação da biblioteca getpass para ocultar a entrada da senha
# import getpass
import oracledb as cx_Oracle

# # # Definição do nome de usuário e do serviço de conexão
# un = 'ENZODEV'
# cs = 'localhost/XEPDB1'

# # # Solicitação da senha do usuário de forma segura
# pw ='1234'

# # # Estabelecimento da conexão com o banco de dados Oracle
# with oracledb.connect(user=un, password=pw, dsn=cs) as connection:
#     # Criação de um cursor para executar comandos SQL
#     with connection.cursor() as cursor:
#         # Definição da consulta SQL para recuperar a data atual do banco de dados
#         sql = """SELECT * FROM PRODUTOS"""
#         # Execução da consulta SQL e iteração sobre os resultados
#         for r in cursor.execute(sql):
#             print(r)  # Impressão da data atual obtida do banco de dados

connection = cx_Oracle.connect(user='ENZODEV', password='1234', dsn='LOCALHOST:1521/XEPDB1')
cursor = connection.cursor()
cursor.execute("""SELECT * FROM PRODUTOS""")
for row in cursor:
    print(row)

cursor.close()
connection.close()