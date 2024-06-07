def marcar_como_emprestado(livros):
    titulo = input("Digite o título do livro a ser marcado como emprestado: ").lower()
    for livro in livros:
        if livro['titulo'].lower() == titulo:
            if livro['status'] == 'disponível':
                livro['status'] = 'emprestado'
                print(f"Livro '{titulo}' marcado como emprestado.")
            else:
                print(f"Livro '{titulo}' já está emprestado.")
            return
    print(f"Livro '{titulo}' não encontrado.")

