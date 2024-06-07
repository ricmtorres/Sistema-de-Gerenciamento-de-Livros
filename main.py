from menu import menu
from adicionar import cadastrar_livro
from exibir import exibir_livros
from pesquisar import pesquisar_livro
from marcar_emprestado import marcar_como_emprestado
from remover import remover_livro


def main():
    livros = []
    while True:
        opcao = menu()

        if opcao == '1':
            cadastrar_livro(livros)
        elif opcao == '2':
            exibir_livros(livros)
        elif opcao == '3':
            pesquisar_livro(livros)
        elif opcao == '4':
            marcar_como_emprestado(livros)
        elif opcao == '5':
            remover_livro(livros)
        elif opcao == '6':
            print("Saindo....")
            break
        else:
            print("Opção invalida ! Tente novamente.")


if __name__ == '__main__':
    main()
