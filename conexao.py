import MySQLdb
import hashlib
import datetime
import os

# Conexão com o banco de dados (aprimorada)
def conectar_banco():
    """
    Estabelece a conexão com o banco de dados MySQL.
    Retorna a conexão e o cursor para serem utilizados nas funções.
    """
    try:
        db = MySQLdb.connect(host="localhost", user="usuario", password="senha", database="ong_comunidade")
        cursor = db.cursor()
        print('Conexão com o banco de dados realizada com sucesso!')
        return db, cursor
    except MySQLdb.Error as e:
        print(f'Erro ao conectar com o banco de dados: {e}')
        return None, None

# Obter conexão e cursor
db, cursor = conectar_banco()

# Verificar se a conexão foi bem-sucedida
if not db or not cursor:
    exit()
