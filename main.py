# Importa a classe Interface
from interface import Interface
from bd import BD

# Classe principal do programa
interface = Interface()

opcao = ""
while opcao != 0:
    interface.logotipo()
    interface.mostraMenuPrincipal()
    opcao = interface.selecionaOpcao([1, 2, 0])
    interface.limpaTela()

    # Tela de cadastro de filmes
    if opcao == 1:
        interface.mostraCadastroViagens()
        opcao = ""
        interface.limpaTela()

    # Tela de lista de filmes
    elif opcao == 2:
        #Mostrar tela para lista de filmes
        interface.mostrarListaViagens()
        opcao = ""
        interface.limpaTela()