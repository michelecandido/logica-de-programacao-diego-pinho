#Crie um programa que peça ao usuário para digitar um número inteiro entre 1 e 10. Em seguida, o programa deve imprimir a tabuada desse número, do 1 ao 10, utilizando o laço de repetição for in… range.

numero = int(input("Digite um número de 1 a 10: "))

print(f"Tabuada do {numero}")
for i in range(10):
    vezes = i + 1
    resultado = numero * vezes
    print(f"{numero} x {vezes} = {resultado}")