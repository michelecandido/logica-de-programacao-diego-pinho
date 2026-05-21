lousa = []

frase = input("Qual é a frase? ")
qntd = int(input("Quantas vezes ele deve repetir a frase? "))

for i in range(qntd):
    lousa.append(frase)

for i in range(len(lousa)):
    print(lousa[i])

"""
outra solução

frase = input("Qual é a frase? ")
n_repeticoes = int(input("Quantas vezes ele deve repetir a frase? "))

for _ in range(n_repeticoes):
	print(frase)

"""