def criar_arquivo(nome_arquivo, conteudo):
    with open(nome_arquivo, 'w') as file:
        file.write(conteudo)
    print(f"Arquivo '{nome_arquivo}' criado com sucesso!")

criar_arquivo("teste.txt", "Boa Noite")
