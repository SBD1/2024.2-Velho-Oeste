import os
import psycopg2
from dotenv import load_dotenv
from psycopg2 import OperationalError

load_dotenv()

class ContainerConnection:
    connection = None

    @classmethod
    def connect(cls):
        """Conecta com o banco de dados no container"""

        if cls.connection is None:
            try:
                host = os.getenv('DB_HOST')
                db = os.getenv('DB_NAME')
                user = os.getenv('DB_USER')
                password = os.getenv('DB_PASSWORD')
            
                cls.connection = psycopg2.connect(
                    host=host,
                    database=db,
                    user=user,
                    password=password
                )

                print("Conexão feita com sucesso")
            except OperationalError as e:
                print(f"Erro ao estabelecer conexão: {e}")
                cls.connection = None
        else:
            print("Conexão já estabelecida")
        
        return cls.connection
    
    @classmethod
    def get_connection(cls):
        """Retorna a conexão existente ou cria uma"""
        if cls.connection is None:
            return Exception("Conexão não estabelecida")
        return cls.connection
    
    @classmethod
    def close(cls):
        """Fecha a conexão"""
        if cls.connection:
            cls.connection.close()
            cls.connection = None
            print("Conexão fechada")