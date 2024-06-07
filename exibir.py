def exibir_livros(livros):
    if not livros:
        print("Nenhum livro cadastrado.")
        return

    for idx, livro in enumerate(livros):
        print(f"\nLivro {idx + 1}")
        print(f"Título: {livro['titulo']}")
        print(f"Autor: {livro['autor']}")
        print(f"Ano: {livro['ano']}")
        print(f"Status: {livro['status']}")

