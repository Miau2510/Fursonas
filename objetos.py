import os
import sqlite3

conexao = sqlite3.connect('fursonas.db')
cursor = conexao.cursor()

# Criação da tabela
cursor.execute ('''
CREATE TABLE IF NOT EXISTS fursonas (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                especie TEXT NOT NULL,
                rel BOOLEAN NOT NULL,
                conj TEXT)
''')
conexao.commit()

# INSERIR DADOS
def salvar_fursona(nome, especie, rel, conj):
    comando = "INSERT INTO fursonas (nome, especie, rel, conj) VALUES (?, ?, ?, ?)"
    # Passar valores em tupla
    cursor.execute(comando, (nome, especie, rel, conj))
    conexao.commit()
    print(f"{nome} salvo no banco de dados!")
# Carregar Dados
def carregar_fursonas():
    comando = "SELECT * FROM fursonas"
    cursor.execute(comando)
    rows = cursor.fetchall()

    print("\n--- Lista de Fursonas no Banco ---")
    for row in rows:
        # Row [0] é ID, row [1] é nome, etc.
        print(f"ID: {row[0]} | Nome: {row[1]} | Espécie: {row[2]}")
# Definição de Classe
class Fursona:
    def __init__(self, nome: str, especie: str, rel: bool, conj=None):
        self.nome = nome.title()
        self.especie = especie

        self.rel = rel
        
        if self.rel:
            self.conj = conj.title() if conj else None
    # Método de Apresentação    
    def apres(self):

        info_base = f"Olá, meu nome é {self.nome}, sou um furry {self.especie}"
        
        if self.rel:
            return f"{info_base} e estou em um relacionamento com {self.conj}."
        else:
            return f"{info_base} e não estou em um relacionamento."

# Coleta de Dados
def fazer_cadastro():
    os.system('cls' if os.name == 'nt' else 'clear')
    #Pergunta quantos fursonas quer cadastrar
    qtd = int(input("Quantos fursonas voce deseja cadastrar? "))

    # Loop FOR (0 ao numero escolhido)
    for i in range(qtd):
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f"\n--- Cadastro do fursona #{i + 1} ---")
        
        nome = input("Nome: ")
        especie = input("Especie: ")
        
        # Lógica de relacionamento
        status_rel = input("Está em um relacionamento? (S/N): ").upper() == "S"
        
        if status_rel:
            conj = input("Nome do conjuge: ")
        else:
            conj = None
        
        # Cria o objeto e adiciona na lista_fursonas
        p = Fursona(nome, especie, status_rel, conj)
        salvar_fursona(p.nome, p.especie, p.rel, p.conj)
# Mostrar Fursonas
def mostrar_fursonas():
    os.system('cls' if os.name == 'nt' else 'clear')
    # Mostra todos os usuários cadastrados ao final
    input("Pressione 'Enter' para ver os resultados..." )
    print("="*30)
    print("--- Resultado dos Cadastros ---")
    print("="*30)
    carregar_fursonas()

# Remover Fursona
def remover_fursona(id_remover):
        os.system('cls' if os.name == 'nt' else 'clear')
        comando = "DELETE FROM fursonas WHERE id = ?"

        cursor.execute(comando, (id_remover,))
        conexao.commit()

        # Verifica se algo foi deletado
        if cursor.rowcount > 0:
            print(f"Fursona ID {id_remover} removido com sucesso.")
        else:
            print(f"Nenhum encontrado com o ID: {id_remover}.")

while True:
    print("="*30)
    print("--- Sistema de Cadastro e Busca de Fursonas ---")
    print("="*30)

    print("1. Cadastrar Novo Fursona")
    print("2. Ver Fursonas Cadastrados")
    print("3. Remover Fursonas (por ID)")
    print("4. Sair")
    escolha = input("Escolha uma opção: ")

    match escolha:
        case "1":
            fazer_cadastro()
        case "2":
            os.system('cls' if os.name == 'nt' else 'clear')
            carregar_fursonas()
            input("\nPressione 'Enter' para voltar ao menu principal...")
        case "3":
            os.system('cls' if os.name == 'nt' else 'clear')
            carregar_fursonas()
            id_alvo = int(input("\nDigite o ID do fursona que deseja remover: "))
            remover_fursona(id_alvo)
            input("\nPressione 'Enter' para voltar...")
        case "4":
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Saindo...")
            input("Pressione 'Enter' para fechar esta janela...")
            break
        case _:
            print("Opção Inválida! Tente novamente.")
            input()