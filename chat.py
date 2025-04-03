import os

mensagem = []


nome = input("Digite seu nome: ")

while True:

        os.system('cls')

        if len(mensagem) > 0:
            for m in mensagem:
                print(m['nome'], "-", m['texto'])

                print("_____________")

                texto = input("Digite sua mensagem: ")
                if texto == "fim":
                    break

            mensagem.append({
                "nome": nome,
                "texto": texto
            })
