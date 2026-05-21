# COMPRA DE INGRESSO
# pede dinheiro, ingresso disponivel sim ou não
# acontece compra se dinheiro >= 50 e ingresso disponível

dinheiro = float(input("Valor: "))
ingresso = input("Ingresso disponível (sim/não): ")

ing_disponivel = (ingresso == "sim")

if dinheiro >= 50 and (ing_disponivel):
    print("Compra realizada.")
else:
    print("Compra não realizada.")