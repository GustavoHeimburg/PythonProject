import random

numSecreto = random.randint(1, 100)

while True:
    tentativa = int(input("Digite um numero: "))

    if tentativa < numSecreto:
        print("Tente um numero maior")
    elif tentativa > numSecreto:
        print("Tente um numero menor")
    else:
        print("Voce acertou o numero")
        break


