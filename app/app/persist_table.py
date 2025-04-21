import mysql.connector
from datetime import datetime
import hashlib

def persist_controle_financa(dados):
    try:

        valor = float(dados["valor"].replace(",", "."))
        tipo = dados["tipo"]
        descricao = dados["descricao"] 
        data = dados["data"]

        data = datetime.strptime(data, "%Y-%m-%d").date()

        db = mysql.connector.connect(
            host="localhost",
            user="usuario",
            password="minhasenha123",
            database="financa",
            port="3306"
        )

        cursor = db.cursor()
        sql = "INSERT INTO controle_transacao (valor, tipo, descricao, data_inclusao) VALUES (%s, %s, %s, %s)"
        cursor.execute(sql, (valor, tipo, descricao, data))
        db.commit()
        cursor.close()
        db.close()
        return True
    
    except Exception as e:
        print("Erro:", e)
        return False

def persist_usuario(dados):
    try:
        email = dados["email"]
        senha = dados["senha"]
        
        senha_criptografada = hashlib.sha256(senha.encode()).hexdigest()

        conn = mysql.connector.connect(
            host="localhost",
            user="usuario",
            password="minhasenha123",
            database="financa" 
        )

        cursor = conn.cursor()
        sql = "INSERT INTO usuario (email, senha) VALUES (%s, %s)"
        cursor.execute(sql, (email, senha_criptografada))
        conn.commit()

        cursor.close()
        conn.close()
        return True
    
    except mysql.connector.Error as err:
        print("Erro ao cadastrar:", err)
        return False
