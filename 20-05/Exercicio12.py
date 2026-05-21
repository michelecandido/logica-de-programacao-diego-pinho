# refatorar com while

"""numeros = [1,2,3,4,5,6,7,8,9,10]
for numero in range(len(numeros)):
    print(numero)"""

numeros = [1,2,3,4,5,6,7,8,9,10]
contador = 0

while (contador < len(numeros)):
    numero = numeros[contador]
    print(numero)
    contador = contador + 1