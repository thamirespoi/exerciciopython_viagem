import sqlite3

# Classe para lidar com o banco de dados
class BD:
    # Construtor
    def __init__(self, banco_dados):
        self.conectarBanco(banco_dados)

    # Conecta no arquivo de banco de dados e cria um cursor
    def conectarBanco(self, banco_dados):
        self.banco = sqlite3.connect(banco_dados)
        self.cursor = self.banco.cursor()

        self.criarTabelaViagens()

    def criarTabelaViagens(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS viagens(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                cidade TEXT NOT NULL,
                pais TEXT NOT NULL,
                continente TEXT NOT NULL,
                preco TEXT NOT NULL,
                locomocao TEXT NULL,
                epoca TEXT NULL
            )
        """)

    def inserir(self, tabela, valores):
        colunas = ', '.join(valores.keys())
        placeholders = ', '.join(['?'] * len(valores))

        # Cria a sql do banco de dados
        sql = f"INSERT INTO {tabela} ({colunas}) VALUES ({placeholders})"

        # Executa a sql no banco de dados
        self.cursor.execute(sql, tuple(valores.values()))

        # Confirma as alterações do banco
        self.banco.commit()

        # Verifica se deu certo o armazenamento
        if self.cursor.lastrowid:
            print(f"{tabela} salvo com sucesso!")
            return True
        else:
            print("Erro ao cadastrar dados!")
            return False
        
    def buscaDados(self, tabela, campos = '*'):
        sql = f"SELECT {campos} FROM {tabela}"
        self.cursor.execute(sql)

        # Pega todos os dados retornados pelo banco
        # e guarda na variavel dados
        dados = self.cursor.fetchall()
        return dados