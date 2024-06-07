def cadastrar_livro(livros):
    titulo = input("Digite o nome do livro: ")
    autor = input("Digite o autor do livro: ")
    ano = int(input("Digite o ano de publicação do livro: "))
    livro = {
        "titulo":titulo,
        "autor":autor,
        "ano":ano,
        "status": "disponível"
    }
    livros.append(livro)
    print(f"Livro {titulo} cadastrado com sucesso !")
