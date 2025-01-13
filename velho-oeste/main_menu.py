from create_player import Start
import time

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
                pass
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
    
