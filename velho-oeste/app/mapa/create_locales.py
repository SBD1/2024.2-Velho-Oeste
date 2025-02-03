import psycopg2
from database import DataBase
import time

conn = DataBase().create_connection()
cur = conn.cursor()

class Locales:
    """Cria o Mundo"""
    def create_world(self):        
        command = """
            INSERT INTO Mundo(nome) 
            VALUES (%s) RETURNING idMundo;
            """
        try:
            cur.execute(command, ("Velho Oeste",))
            id_world = cur.fetchone()[0]
            conn.commit()
            print("Mundo criado com sucesso")
            return id_world
        except (Exception, psycopg2.DatabaseError) as error:
            print(f'Erro em criar mundo: {error}')
    
    def create_location(self):
        locais = [
        "Região Central",
        "Região Norte",
        "Região Sul",
        "Região Leste",
        "Região Oeste",
        "Região Noroeste",
        "Região Sudoeste",
    ]
        ids = []
        command = """INSERT INTO LOCALIZACAO (nome, idMundo) 
            VALUES (%s, %s) RETURNING idLocal;"""
        
        try:
            id_world = Locales().create_world()
            for local in locais:
                cur.execute(command, (local, id_world))
                id_local = cur.fetchone()[0]  
                ids.append((id_local, local))
            conn.commit()
            print("Localizações criadas com sucesso")
            return ids
        except (Exception, psycopg2.DatabaseError) as error:
            print(f"Erro em criar localização: {error}")

    def create_cities(self):
        cities = [
            (1, 'Saloon', 'Região Central'),
            (1, 'Delegacia', 'Região Central'),
            (2, 'Montanhas', 'Região Norte'),
            (4, 'Vila de Comércio', 'Região Leste'),
            (3, 'Minas de Ouro', 'Região Oeste'),
            (5, 'Deserto', 'Região Sul'),
            (6, 'Reserva Indígena', 'Região Noroeste'),
            (7, 'Cemitério', 'Região Sudoeste')
        ]

        command = """INSERT INTO CIDADE (idLocal, nome, localizacao) 
                    VALUES (%s, %s, %s)"""
        
        try:
            locations = Locales().create_location()
            for id_local, city_name, city_location in cities:  # Desempacotando 3 valores
                # Encontre o ID da localização correspondente
                id_local_found = next((id for id, name in locations if name == city_location), None)
                if id_local_found is None:
                    print(f"Localização não encontrada para {city_location}.")
                    continue
                cur.execute(command, (id_local_found, city_name, city_location))
            conn.commit()
            print("Cidades criadas com sucesso")
        except (Exception, psycopg2.DatabaseError) as error:
            print(f"Erro em criar cidade: {error}")





if __name__ == "__main__":
    locais = Locales()
    locais.create_cities()