import psycopg2
from database import DataBase
import time

conn = DataBase().create_connection()
cur = conn.cursor()
    
class Mission:
    def create_mission_1(self):
        nome = "Início da Jornada"
        descricao = """Após ouvir histórias sobre bandidos que aterrorizam 
        cidades vizinhas, você, caçador de recompensas, chega ao Saloon e 
        encontra o xerife, que apresenta seu primeiro contrato: capturar 
        um ladrão de cavalos conhecido por saquear vilas próximas. 
        O seu objetivo é rastrear e capturar o ladrão vivo ou morto. O xerife sugere buscar 
        pistas no vilarejo de comércio."""
        tipo = "Principal"
        dinheiro = 50.00
        reputacao = 50

        self.insert_mission(nome, tipo, dinheiro, descricao, reputacao)

    def create_mission_2(self):
        nome = "O Cemitério Assombrado"
        descricao = """Os moradores relatam eventos estranhos no cemitério, 
        onde dizem ver fantasmas e ouvir vozes. O coveiro pede ajuda ao jogador 
        para investigar. Explore o cemitério à noite e enfrente bandidos que se 
        escondem nas tumbas. Após derrotá-los, encontre um mapa escondido que leva 
        a uma mina de ouro abandonada."""
        tipo = "Principal"
        dinheiro = 75.00
        reputacao = 40

        self.insert_mission(nome, tipo, dinheiro, descricao, reputacao)

    def create_mission_3(self):
        nome = "Perigo no Trem"
        descricao = """A dama do Saloon relata um assalto planejado a um trem carregado 
        de ouro e mercadorias valiosas. Intercepte a gangue no meio do deserto, aborde o trem, 
        enfrente os bandidos e proteja o carregamento."""
        tipo = "Principal"
        dinheiro = 120.00
        reputacao = 50

        self.insert_mission(nome, tipo, dinheiro, descricao, reputacao)

    def create_mission_4(self):
        nome = "O Ouro da Montanha"
        descricao = """Com o mapa da mina obtido no cemitério, o jogador é atraído para 
        explorar a montanha e encontrar uma mina que dizem guardar riquezas, mas que é protegida 
        por bandidos locais. Enfrente armadilhas, resolva enigmas e colete o ouro guardado pelos bandidos."""
        tipo = "Principal"
        dinheiro = 150.00
        reputacao = 60

        self.insert_mission(nome, tipo, dinheiro, descricao, reputacao)

    def create_mission_5(self):
        nome = "A Diligência"
        descricao = """O mercador de cavalos pede ajuda ao jogador para proteger uma diligência carregada 
        de suprimentos e remédios que será enviada para uma cidade próxima. Escolte a diligência por um caminho 
        infestado de bandidos e enfrente emboscadas."""
        tipo = "Secundária"
        dinheiro = 90.00
        reputacao = 30

        self.insert_mission(nome, tipo, dinheiro, descricao, reputacao)

    def create_mission_6(self):
        nome = "A Última Fronteira"
        descricao = """O xerife pede ajuda para capturar um dos criminosos mais procurados, o líder de uma gangue 
        de bandidos chamada de 'Os Renegados do Deserto'. Rastreie o esconderijo da gangue, infiltre-se no acampamento 
        e enfrente o chefe em uma grande batalha."""
        tipo = "Principal"
        dinheiro = 200.00
        reputacao = 100

        self.insert_mission(nome, tipo, dinheiro, descricao, reputacao)

    def insert_mission(self, nome, tipo, dinheiro, descricao, reputacao):
        command = """INSERT INTO MISSAO (nome, tipo, dinheiro, descricao, reputacao)
        VALUES (%s, %s, %s, %s, %s)"""
        try:
            cur.execute(command, (nome, tipo, dinheiro, descricao, reputacao))
            conn.commit()
            print(f"Missão '{nome}' criada com sucesso.")
        except (Exception, psycopg2.DatabaseError) as error:
            print(f"Erro ao criar a missão '{nome}': {error}")

if __name__ == "__main__":
    mission = Mission()
    mission.create_mission_1()
    mission.create_mission_2()
    mission.create_mission_3()
    mission.create_mission_4()
    mission.create_mission_5()
    mission.create_mission_6()
