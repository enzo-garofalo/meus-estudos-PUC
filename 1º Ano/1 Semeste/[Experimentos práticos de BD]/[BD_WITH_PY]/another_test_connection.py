import oracledb
import getpass


userpwd = getpass.getpass("Enter password: ")

connection = oracledb.connect(user="ENZODEV", password=userpwd,
                              dsn="cadastron_bd/orclpdb")