from sqlalchemy import create_engine

def test_connection():
    try:
        # Formato de URL de conexão do SQLAlchemy
        engine = create_engine('postgresql://velho_oeste_user:vopassword@velho-oeste-postgres:5432/velho_oeste_db')
        connection = engine.connect()
        print("Conexão bem-sucedida ao banco de dados!")
        connection.close()
    except Exception as e:
        print(f"Erro na conexão: {e}")

if __name__ == "__main__":
    test_connection()
