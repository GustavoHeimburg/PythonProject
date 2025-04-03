def palindromo(palavra):
    palavra = palavra.lower()
    if palavra == palavra[::-1]:
        print(f"{palavra} É um palindromo")
    else:
        print(f"{palavra} Não é um palindromo")

texto = input("Digite a palavra: ")
palindromo(texto)