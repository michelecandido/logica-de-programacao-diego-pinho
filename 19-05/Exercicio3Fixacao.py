# ACESSO À PISCINA
# pede idade, sabe nadar sim ou não
# pode entrar sozinha se tiver 12 anos ou mais e sabe nadar

idade = int(input("Idade: "))
sabe_nadar = input("Você sabe nadar (sim/não)? ")

nada = (sabe_nadar == "sim")

if idade >= 12 and (nada):
    print("Tem acesso à piscina.")
else:
    print("Não tem acesso à piscina.")