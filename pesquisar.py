def pesquisar_livro(livros):
    tipo = input("Pesquisar por título ou autor? ").lower()

    if tipo not in ["titulo", "autor"]:
        print("Tipo de pesquisa inválido. Por favor, escolha 'titulo' ou 'autor'.")
        return

    termo = input(f"Digite o {tipo} para busca: ").lower()
    resultados = [livro for livro in livros if termo in livro[tipo].lower()]

    if not resultados:
        print("Nenhum livro encontrado.")
    else:
        for livro in resultados:
            print(f"\nTítulo: {livro['titulo']}")
            print(f"Autor: {livro['autor']}")
            print(f"Ano: {livro['ano']}")
            print(f"Status: {livro['status']}")