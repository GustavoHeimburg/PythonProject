def numeroDiferente(n):
    soma = 0

    for i in range(1,n):
        if i % 2 == 0:
            soma +=i

    if soma == n:
        print(f"{n} É um numero perfeito")
    else:
        print(f"{n} Não é um numero perfeito")

num = int(input("Digite um numero: "))
numeroDiferente(num)


