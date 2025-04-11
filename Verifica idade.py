while True:
    idade = int(input("Digite sua idade: "))

    if idade >= 18:
        print("Aprovado")
    else:
        print("Você não tem idade suficiente")

    resposta = input("Digite S para repetir ou N para sair: ").upper()

    if resposta == 'S':
        print("Programa finalizado.")
        break
    elif resposta != 'N':
        print("Resposta inválida. O programa será encerrado.")
        break
