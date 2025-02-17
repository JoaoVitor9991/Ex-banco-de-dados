import mysql.connector
def conectar():
        return mysql.connector.connect(
            host ="localhost",
            user ="root",
            password = "",
            database="login_formulario"
        )
conexao = conectar()
cursor = conexao.cursor()

sql_verificar = "SELECT * FROM usuario"  
cursor.execute(sql_verificar)
usuarios = cursor.fetchall()

if usuarios:
        print("Encontrado")
        for usuario in usuarios:
                print(usuario)
else:
    print("Não")

cursor.close()
conexao.close()