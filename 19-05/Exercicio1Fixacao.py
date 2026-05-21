# SISTEMA DE CINEMA
# pedir idade, se é estudante
# meia entrada: se for estudante ou tiver menos de 12

idade = int(input("Idade: "))
estudante = input("Você é estudante (sim/não)? ")

eh_estudante = (estudante == "sim")

if idade <= 12 or (eh_estudante):
    print("Paga meia entrada.")
else:
    print("Paga entrada inteira.")