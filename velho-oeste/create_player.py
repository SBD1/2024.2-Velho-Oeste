import psycopg2
from database import DataBase
import time

conn = DataBase().create_connection()
cur = conn.cursor()

class Start:
    def history(self):
        pass
    """Cria o Personagem"""
    def create_player(self):
        
        print("Primeiramente, vamos criar o seu personagem.")
        name = input("Escolha o nome: ")
        
        command = """
            INSERT INTO Personagem(nome, classe) 
            VALUES (%s, %s) RETURNING idPersonagem;
            """
        try:
            cur.execute(command, (name, "Principal"))
            id_player = cur.fetchone()[0]
            conn.commit()
            return id_player
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)

    """Criação do Personagem Principal"""
    def create_main_player(self, idPersonagem):
        command = """INSERT INTO Personagem_principal(idPersonagem, inventario, reputacao)
                                VALUES (%s, %s, %s)"""
        try:
            
            item = ("Pistola", "Laço")
            cur.execute(command, (idPersonagem, item, 50))
            conn.commit()
            return item
        except(Exception, psycopg2.DatabaseError) as error:
            print(f'Erro na criação do personagem principal: {error}')
    
    """Criação do Inventario"""
    def create_player_inventory(self):
        command = """INSERT INTO inventario(idPersonagem, item) 
                    VALUES (%s, %s)"""
        try:
            st = Start()
            idPersonagem = st.create_player()
            item = st.create_main_player(idPersonagem)
            cur.execute(command, (idPersonagem, item))
            conn.commit()
        except(Exception, psycopg2.DatabaseError) as error:
            print(f'Erro na criação do inventario: {error}')

if __name__ == "__main__":
    Start().create_inventory()
    