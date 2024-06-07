def remover_livro(livros):
    titulo = input("Digite o título do livro a ser removido: ").lower()
    for livro in list(livros):
        if livro['titulo'].lower() == titulo:
            livros.remove(livro)
            print(f"Livro '{titulo}' removido com sucesso.")
            return
    print(f"Livro '{titulo}' não encontrado.")
