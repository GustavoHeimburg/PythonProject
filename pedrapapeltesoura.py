import random

def jogar():
    opcoes = ["pedra" , "papel", "tesoura"]

    jogador = input("Escolha Pedra - Papel - tesoura: ").lower()
    if jogador not in opcoes:
        print("Escolha invalida")
        return

    pc = random.choice(opcoes)

    print(f"\nVoce escolheu: {jogador}")
    print(f"O computador escolheu: {pc}\n")

    if jogador == pc:
        print("Empate")
    elif (jogador == "pedra" and pc == "tesoura") or \
         (jogador == "papel" and pc == "pedra") or \
         (jogador == "tesoura" and pc == "papel"):
        print("Voce ganhou!!!")
    else:
        print("Voce perdeu!")

jogar()
