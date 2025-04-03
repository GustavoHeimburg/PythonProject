notas = []

for x in range(3):
    codigo_aluno = input("Digite o nome do aluno: ")
    nota = float(input("Digite a nota do aluno: "))
    resultado = [codigo_aluno, nota]
    notas.append(resultado)

    print("Quantidade de notas", len(notas))

    for n in notas:
        codigo_aluno = n [0]
        nota = n[1]
        resultado = ["O aluno ",codigo_aluno, " Tirou ",nota, " na prova."]
        print(resultado)