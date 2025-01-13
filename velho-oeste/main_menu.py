from create_player import Start
from database import DataBase
import time
import psycopg2

conn = DataBase().create_connection()
cur = conn.cursor()

class Menu:
    def main_menu(self):
        while True:
            escolha = input("Escolha uma opção:")
            if escolha == '1':
                player = Start().create_inventory()
                break
                #missao
            elif escolha == '2':
                #consulta para as missoes
                self.list_missions()
                break
            elif escolha == '3':
                pass
            elif escolha == '4':
                pass
            elif escolha == '5':
                pass
            elif escolha == '6':
                print("Obrigado por Jogar ;)")
            else:
                print("Opção Inválida, tente novamente.")
    

    def list_missions(self):
        try:
            # Consultar todas as missões do banco de dados
            query = "SELECT idMissao, nome, tipo, dinheiro, reputacao, descricao FROM MISSAO"
            cur.execute(query)
            missions = cur.fetchall()

            if not missions:
                print("\nNenhuma missão disponível.\n")
                return

            print("\n=== Missões que você encontrará no jogo ===\n")
            for mission in missions:
                id_missao, nome, tipo, dinheiro, reputacao, descricao = mission
                print(f"ID: {id_missao}")
                print(f"Nome: {nome}")
                print(f"Tipo: {tipo}")
                print(f"Recompensa: ${dinheiro:.2f}")
                print(f"Reputação: {reputacao} pontos")
                print("Descrição:")
                print(descricao)
                print("-" * 50)
        except (Exception, psycopg2.DatabaseError) as error:
            print(f"Erro ao listar missões: {error}")


if __name__ == "__main__":
    def history(message, seconds):
        print(message)
        time.sleep(seconds)
    history("O velho oeste é um lugar repleto de mistérios", 3)
    history("É um lugar onde sobrevivem apenas os fortes e corajosos ", 3)
    history("Onde se vencer se torna o herói ", 2.5)
    history("Se perder ", 2)
    history("Você morre...", 2)

    print('''
            =======================================
                    Bem Vindo ao Velho Oeste
            =======================================
                  1 - Iniciar o Jogo
                  2 - Conhecer Missões
                  3 - Conhecer NPC's
                  4 - Explorar o mundo
                  5 - Explorar Missões
                  6 - Sair
                '''
            )
    menu = Menu().main_menu()
    
