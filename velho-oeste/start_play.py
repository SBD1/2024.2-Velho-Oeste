import psycopg2
from database import DataBase
import time

conn = DataBase().create_connection()
cur = conn.cursor()

class start:
    def history(self):
        pass

    def create_player(self):
        """Cria o Personagem"""
        print("Primeiramente, vamos criar o seu personagem.")
        name = input("Escolha o nome: ")
        
        command = """
            INSERT INTO Personagem(nome) VALUES (%s);
        """
        try:
            cur.execute(command, (name))
            conn.commit()
            print("Personagem criado com sucesso")
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)

if __name__ == "__main__":
    st = start().create_player()
    