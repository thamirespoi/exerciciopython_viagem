import os
from bd import BD
# Classe para interface do usuário do programa

class Interface:
    # Construtor
    def __init__(self):
        self.banco = BD("catalogoViagens.db")

    def logotipo(self):
        print("============================")
        print("========== Viagens =========")
        print("============================")
        print()

    def limpaTela(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    # Função que permite o usuário escolher uma opção
    # opcoes = []
    def selecionaOpcao(self, opcoesPermitidas = []):
        opcaoSelecionada = input("Digite a opção desejada: ")

        # Verifica se digitou algo
        if opcaoSelecionada == "":
            return self.selecionaOpcao(opcoesPermitidas)

        # Tenta converter para números
        try:
            opcaoSelecionada = int(opcaoSelecionada)
        except ValueError:
            print("Opção Inválida!")
            return self.selecionaOpcao(opcoesPermitidas)

        # Verifica se a opção selecionada é uma das opções válidas
        if opcaoSelecionada not in opcoesPermitidas:
            print("Opção Inválida!")
            return self.selecionaOpcao(opcoesPermitidas)

        # Retorna o valor selecionado pelo usuário
        return opcaoSelecionada

    # Mostra menu principal do sistema
    def mostraMenuPrincipal(self):
        print("1 - Cadastrar Viagem")
        print("2 - Lista de Viagens")
        print("0 - Sair")
        print()

    def mostraCadastroViagens(self):
        self.logotipo()

        print("Insira os dados da viagem: ")
        print("(campos com * são obrigatórios)")
        print()

        cidade = self.solicitaValor('Digite o nome da cidade da viagem*: ', 'texto', False)
        pais = self.solicitaValor('Digite o nome do pais da viagem*: ', 'texto', False)
        continente = self.solicitaValor('Digite o nome da continente da viagem*: ', 'texto', False)
        preco = self.solicitaValor('Digite o preço da viagem*: ', 'texto', False)
        locomocao = self.solicitaValor('Digite a locomocao para fazer a viagem: ', 'texto', True)
        epoca = self.solicitaValor('Digite a melhor época do ano para essa viagem: ', 'texto', True)

        # Armazena os valores no banco de dados!
        valores = {
            "cidade": cidade,
            "pais": pais,
            "continente": continente,
            "preco": preco,
            "locomocao": locomocao,
            "epoca": epoca
        }

        self.banco.inserir('viagens', valores)

    def mostrarListaViagens(self):
        self.logotipo()
        print("Veja abaixo a lista de viagens cadastrados.")
        print()

        viagens = self.banco.buscaDados('viagens')

        for viagem in viagens:
            id, cidade, pais, continente, preco, locomocao, epoca = viagem

            print(f"Viagem {id}")
            print(f"{cidade} | {pais} | {continente}")
            print(preco)
            print(locomocao)
            print(epoca)

        input("Aperte Enteder para continuar..")
    
    # Solicita um valor do usuário e valida ele.
    # return valorDigitado
    def solicitaValor(self, legenda, tipo = 'texto', permiteNulo = False):
        valor = input(legenda)

        # Verifica se está vazio
        if valor == "" and not permiteNulo:
            print("Valor inválido!")
            return self.solicitaValor(legenda, tipo, permiteNulo)
        elif valor == "" and permiteNulo:
            return valor
        
        # Verifica se está no formato correto
        if tipo == 'numero':
            try:
                valor = float(valor)
            except ValueError:
                print("Valor Inválido!")
                return self.solicitaValor(legenda, tipo, permiteNulo)
            
        return valor