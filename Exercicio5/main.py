def soma_multiplos_de_tres(nome_arquivo):
    try:
        with open(nome_arquivo, 'r') as file:
            numeros = [int(linha.strip()) for linha in file]
        soma = sum(num for num in numeros if num % 3 == 0)
        print(f"Soma dos múltiplos de 3: {soma}")
    except Exception as e:
        print(f"Erro: {e}")

soma_multiplos_de_tres("numeros.txt")
