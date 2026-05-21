# VERIFICAÇÃO PROMOÇÃO
# pede idade, primeira compra
# ganha desconto se idade >= 60 ou primeira compra

idade = int(input("Digite sua idade: "))
compra = input("Primeira compra (sim/não): ")

primeira_compra = (compra == "sim")

if idade >= 60 or (primeira_compra):
    print("Promoção aplicada.")
else:
    print("Promoção não aplicada.")