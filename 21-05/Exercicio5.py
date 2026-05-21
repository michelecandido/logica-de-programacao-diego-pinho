# revisão: peça 5 números ao usuário usando um laço. no final, mostre:, a soma total, quantos números eram pares

numeros = []
soma = 0
pares = 0

for i in range(5):
    numeros.append(int(input("Digite um número: ")))
    soma = soma + numeros[i]

    if(numeros[i] % 2 == 0):
        pares = pares + 1

print(f"A soma total é {soma}. Há {pares} números pares.")