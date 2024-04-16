# Importação da biblioteca getpass para ocultar a entrada da senha
import getpass
import oracledb

# Definição do nome de usuário e do serviço de conexão
un = 'ENZODEV'
cs = 'localhost/XEPDB1'

# Solicitação da senha do usuário de forma segura
pw = getpass.getpass(f'Enter password for {un}@{cs}: ')

# Estabelecimento da conexão com o banco de dados Oracle
with oracledb.connect(user=un, password=pw, dsn=cs) as connection:
    # Criação de um cursor para executar comandos SQL
    with connection.cursor() as cursor:
        # Definição da consulta SQL para recuperar a data atual do banco de dados
        sql = """select sysdate from dual"""
        # Execução da consulta SQL e iteração sobre os resultados
        for r in cursor.execute(sql):
            print(r)  # Impressão da data atual obtida do banco de dados