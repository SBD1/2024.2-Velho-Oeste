import psycopg2

class Mission:
    def __init__(self, conn):
        self.conn = conn
        self.cur = conn.cursor()

    def list_missions(self):
        """Lista todas as missões com id e nome"""
        self.cur.execute("SELECT id, nome FROM MISSAO;")
        missions = self.cur.fetchall()

        if not missions:
            print("Nenhuma missão encontrada.")
            return []

        print("Missões disponíveis:")
        for mission in missions:
            print(f"{mission[0]} - {mission[1]}")

        return missions

    def get_mission_details(self, mission_id):
        """Exibe os detalhes de uma missão selecionada"""
        self.cur.execute("SELECT nome, descricao, dinheiro, reputacao FROM MISSAO WHERE id = %s;", (mission_id,))
        mission = self.cur.fetchone()

        if mission:
            print(f"\nMissão: {mission[0]}")
            print(f"Descrição: {mission[1]}")
            print(f"Recompensa: R${mission[2]:.2f}")
            print(f"Reputação: {mission[3]}")
        else:
            print("Missão não encontrada.")