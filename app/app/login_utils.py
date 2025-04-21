import mysql.connector
import hashlib

def check_login(dados):
    email = dados["email"]
    senha = dados["senha"]
    senha_criptografada = hashlib.sha256(senha.encode()).hexdigest()

    db = mysql.connector.connect(
        host="localhost",
        user="usuario",
        password="minhasenha123",
        database="financa",
        port="3306"
    )

    cursor = db.cursor()
    cursor.execute("SELECT * FROM usuario WHERE email = %s AND senha = %s", (email, senha_criptografada))
    usuario = cursor.fetchone()
    cursor.close()

    if usuario: 
        return True
    else:
        return False

