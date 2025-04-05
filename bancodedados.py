import mysql.connector

conexao = mysql.connector.connect(

    host="localhost",
    user="root",
    password="admin",
    database="loja"
)

cursor = conexao.cursor()

nome = "Joao"
email = "joao@gmail.com"

sql = "INSERT INTO usuario (nome, email) VALUES (%s, %s)"
valores = (nome, email)

cursor.execute(sql, valores)
conexao.commit()
print(cursor.rowcount, "Registro inserido")

cursor.execute("Select * from usuario")
resultado = cursor.fetchall()

print("\nUsuario cadastrado com sucesso")
for liinha in resultado:
    print(liinha)

cursor.close()
conexao.close()
