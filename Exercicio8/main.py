def filtrar_palavras_bo(nome_arquivo, novo_arquivo):
    try:
        with open(nome_arquivo, 'r', encoding='utf-8') as file:
            palavras = file.read().splitlines()
        resultado = [palavra for palavra in palavras if palavra.startswith('B') and palavra.endswith('o')]
        with open(novo_arquivo, 'w') as file:
            file.write("\n".join(resultado))
        print(f"Palavras filtradas salvas em '{novo_arquivo}'.")
    except Exception as e:
        print(f"Erro: {e}")

# Testando
filtrar_palavras_bo("palavras.txt", "resultado.txt")
