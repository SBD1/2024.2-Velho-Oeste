import psycopg2
import random
from connection.db import ContainerConnection
import os
import sys


conn = ContainerConnection.connect()
cur = conn.cursor()


class Mission():
    def search_player(self, id):
        cur.execute(f"""SELECT * FROM Personagem_principal AS pp  
                    JOIN Personagem AS p ON p.idpersonagem=pp.idpersonagem
                    WHERE p.IdPersonagem = {id};""")
        player = cur.fetchone()
        return player
                    
    def search_mission(self, id):
        cur.execute(f"SELECT * FROM missao WHERE id = {id};")
        mission = cur.fetchone()
        return mission

    def search_npc(self):
        cur.execute("""SELECT * FROM npc LEFT JOIN Personagem 
                    ON npc.idpersonagem = Personagem.idpersonagem;""")
        npc = cur.fetchone()
        return npc
    
    import os

    def clear_terminal():
        """Função para limpar o terminal"""
        os.system('cls' if os.name == 'nt' else 'clear')

    def fight(self, player, npc):
        player_name = player[4]
        npc_name = npc[4]

        print("\nPara completar essa missão, você deve enfrentar o líder dos bandidos.\n")
        print(f"⚔️  {player_name} VS {npc_name} ⚔️\n")

        life_player = 100
        life_npc = 100
        turn = 1

        while life_player > 0 and life_npc > 0:
            os.system('clear')  

            print(f"🎲 **Turno {turn}** 🎲")
            print(f"{player_name}: ❤️ {life_player} | {npc_name}: ❤️ {life_npc}\n")

            print("Escolha onde quer atacar:")
            print("1️⃣ - Cabeça (30-50 de dano)")
            print("2️⃣ - Peito (10-20 de dano)")
            print("3️⃣ - Perna (5-15 de dano)")

            try:
                choice = int(input("👉 Escolha: "))
                if choice == 1:
                    attack_player = random.randint(30, 50)
                elif choice == 2:
                    attack_player = random.randint(10, 20)
                elif choice == 3:
                    attack_player = random.randint(5, 15)
                else:
                    print("❌ Escolha inválida! Perdeu a vez.") 
                    attack_player = 0
            except ValueError:
                print("❌ Entrada inválida! Perdeu a vez.")
                attack_player = 0

            # Turno do Jogador
            life_npc -= attack_player
            print(f"\n💥 {player_name} atacou {npc_name} e causou {attack_player} de dano!")

            if life_npc <= 0:
                print(f"\n🎉 {player_name} venceu o combate! Missão concluída!")
                return

            # Turno do NPC
            attack_npc = random.randint(10, 40)
            life_player -= attack_npc
            print(f"🔥 {npc_name} contra-atacou e causou {attack_npc} de dano!\n")

            if life_player <= 0:
                print(f"\n💀 {npc_name} venceu o combate! Missão fracassada!")
                return

            # Exibe status atual
            print(f"📊 **Status Atual:**")
            print(f"❤️ {player_name}: {life_player} | ❤️ {npc_name}: {life_npc}")
            print(f"🔺 {player_name} está {'vencendo' if life_player > life_npc else 'perdendo'} a batalha!\n")

            input("Pressione Enter para continuar para o próximo turno...")  
            turn += 1



    def Mission_1(self, IdPersonagem):
        mission = Mission()
        try:
            player = mission.search_player(IdPersonagem)
            mission_1 = mission. search_mission(1) 
            npc = mission.search_npc() 
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        description = mission_1[2]
        print(description)
        mission.fight(player, npc)
        mission.mission_2()
    
    def mission_2(self):
        pass
        
if __name__ == "__main__":
    # Mission().Mission_1()
    Mission().search_player()
