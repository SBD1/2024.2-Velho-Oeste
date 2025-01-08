import psycopg2

class DataBase ():
    def create_connection():
        connect = psycopg2.connect(
            host="localhost",
            database="velho_oeste_db",
            user="velho_oeste_user",
            password="vopassword")
        return connect