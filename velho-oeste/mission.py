import psycopg2
from database import DataBase
import time

conn = DataBase().create_connection()
cur = conn.cursor()

class Mission:
    def create_mission_1(self):
        descricao = """ Após ouvir histórias sobre bandidos que aterrorizam 
        cidades vizinhas, você, caçador de recompensas, chega ao Saloon e 
        encontra o xerife, que apresenta seu primeiro contrato: capturar 
        um ladrão de cavalos conhecido por saquear vilas próximas. 
        O seu objetivo é Rastrear e capturar o ladrão vivo ou morto. O xerife sugere buscar 
        pistas no vilarejo de comércio."""
        tipo = "Principal"
        dinheiro = 50
        reputacao = 50

        command = """INSERT INTO Missao(tipo, dinheiro, descricao, reputacao)
        VALUES (%s, %s, %s, %s)"""
        try:
            cur.execute(command, (tipo, dinheiro, descricao, reputacao))
            conn.commit()
            print("Missão 1 criada")
        except (Exception, psycopg2.DatabaseError) as error:
            print(f'Erro na missão 1: {error}')
    
    def mission_2(self):
        pass


if __name__ == "__main__":
    mission1 = Mission().mission_1()




"""class Mission:
    def __init__(self, player_name):
        self.player_name = player_name
        self.reputation = 0
        self.money = 0

    def start(self):
        print(f"\nBem-vindo, {self.player_name}, ao Saloon.")
        print("Você ouve histórias de bandidos aterrorizando cidades vizinhas.")
        print("O xerife lhe entrega seu primeiro contrato.")
        print("\n[Objetivo] Rastrear e capturar o ladrão vivo ou morto.")
        print("O xerife sugere que você busque pistas no vilarejo de comércio.\n")
        
        self.search_for_clues()

    def search_for_clues(self):
        print("Você chega ao vilarejo de comércio.")
        print("Escolha uma ação:")
        print("1. Conversar com comerciantes.")
        print("2. Investigar a área ao redor do vilarejo.")
        
        choice = input("O que você faz? (1 ou 2): ")
        if choice == "1":
            print("\nOs comerciantes lhe dão informações sobre o ladrão.")
            print("Eles o viram indo para o norte, para a floresta.\n")
            self.confront_bandit()
        elif choice == "2":
            print("\nVocê investiga a área e encontra pegadas indo para o norte, em direção à floresta.\n")
            self.confront_bandit()
        else:
            print("\nEscolha inválida. Tente novamente.\n")
            self.search_for_clues()

    def confront_bandit(self):
        print("Você encontra o ladrão na floresta.")
        print("Escolha uma ação:")
        print("1. Tentar capturá-lo vivo.")
        print("2. Atacar e matá-lo.")
        
        choice = input("O que você faz? (1 ou 2): ")
        if choice == "1":
            print("\nApós uma luta, você consegue capturá-lo vivo.")
            self.reputation += 10  # Aumento moderado de reputação
            self.money += 100
        elif choice == "2":
            print("\nVocê o mata durante o confronto.")
            self.reputation += 5  # Aumento baixo de reputação
            self.money += 100
        else:
            print("\nEscolha inválida. Tente novamente.\n")
            self.confront_bandit()

        self.end_mission()

    def end_mission(self):
        print("\n[Missão Concluída!]")
        print(f"Reputação atual: {self.reputation}")
        print(f"Dinheiro ganho: ${self.money}\n")
        print("Obrigado por jogar!")

# Iniciar a missão
player_name = input("Digite o nome do seu personagem: ")
mission = Mission(player_name)
mission.start()
"""