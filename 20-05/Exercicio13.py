# Elabore um programa que faz a soma dos números que o usuário inserir enquanto eles forem positivos. A partir do momento que o usuário inserir um número menor que zero, a conta deve ser encerrada.

numero = int(input("Digite um número: "))
cont = 0

while (numero >= 0):
    resultado = numero + cont
    cont = resultado
    numero = int(input("Digite um número: "))

print(f"A soma dos números é: {resultado}")

"""
outra solução

valor = 0
soma = 0
while(valor >= 0):
    soma += valor
    valor = int(input("Digite um número: "))
print(f"A soma dos números é: {soma}")

"""