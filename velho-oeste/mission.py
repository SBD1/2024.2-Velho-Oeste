import psycopg2
from database import DataBase
import random

conn = DataBase().create_connection()
cur = conn.cursor()


class Mission():
    def search_player(self):
        cur.execute("""SELECT * FROM Personagem_principal AS pp  
                    JOIN Personagem AS p ON p.idpersonagem=pp.idpersonagem;""")
        player = cur.fetchone()
        return player
                    
    def search_mission(self, id):
        cur.execute(f"SELECT * FROM missao WHERE idmissao = {id};")
        mission = cur.fetchone()
        return mission

    def search_npc(self):
        cur.execute("""SELECT * FROM npc   
                    JOIN Personagem AS p ON npc.idpersonagem=p.idpersonagem;""")
        npc = cur.fetchone()
        return npc
    
    def fight(self, player, npc):
        player_name = player[5]
        npc_name = npc[4]

        print("Para completar essa missão você deve enfrentar o líder dos bandidos.")
        print(f"{player_name} VS {npc_name}")

        life_npc = 100
        life_player = 100

        cont = 1
        while life_player > 0 and life_npc > 0:
            print(f"Turno {cont}")

            #Turno do Jogador
            attack = random.randint(20 // 2, 20)
            life_npc -= attack

            if life_npc <= 0:
                print(f"{player_name} venceu o combate, missão concluída!")
                # update para missao concluida --> Trigger para update da experiencia
                return
        
            #Turno do NPC
            attack = random.randint(20 // 2, 20)
            life_player -= attack

            if life_player <= 0:
                print(f"{npc_name} venceu o combate, missão fracassada!")
                # update para missao concluida --> Trigger para update da experiencia
                print("Tentar novamente? 1 - Sim, 2 - Não")
                return

            cont += 1


    def Mission_1(self):
        mission = Mission()
        try:
            player = mission.search_player()
            mission_1 = mission. search_mission(21) 
            npc = mission.search_npc() 
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        # Descrição da Missão
        '''Execução do Combate'''
        description = mission_1[3]
        print(description)
        mission.fight(player, npc)
        mission.mission_2()
    
    def mission_2(self):
        pass
        
if __name__ == "__main__":
    Mission().Mission_1()
