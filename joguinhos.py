idade = int(input("digite sua idade: "))

if idade >= 18:
    print("voce possui {} anos".format(idade))
else:
    print("Nao aprovado")


numero = int(input("digite um numero: "))
if numero % 2 == 0:
    print("Numero é par")
else:
    print("Numero impar")