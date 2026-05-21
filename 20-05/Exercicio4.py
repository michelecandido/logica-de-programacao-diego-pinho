# Escreva um programa capaz de cadastrar o nome de 5 participantes em um evento. Para cada participante, basta cadastrar seu primeiro nome. Ao final, seu programa deve exibir o nome de todos os integrantes. Utilize uma lista para administrar os nomes do participantes.

participantes = []

nome1 = input("Qual é o nome do participante? ")
nome2 = input("Qual é o nome do participante? ")
nome3 = input("Qual é o nome do participante? ")
nome4 = input("Qual é o nome do participante? ")
nome5 = input("Qual é o nome do participante? ")

participantes.append(nome1)
participantes.append(nome2)
participantes.append(nome3)
participantes.append(nome4)
participantes.append(nome5)

print("Os participantes são: ")
for participante in participantes:
    print(participante)

"""
outra solução

participantes = []
participantes.append(input("Qual é o nome do participante? "))
participantes.append(input("Qual é o nome do participante? "))
participantes.append(input("Qual é o nome do participante? "))
participantes.append(input("Qual é o nome do participante? "))
participantes.append(input("Qual é o nome do participante? "))
	
print("Os participantes são: ")
for participante in participantes:
	print(participante)	
    
"""