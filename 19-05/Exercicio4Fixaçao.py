# ENTREGA DE COMIDA
# pede valor do pedido, se possui cupom
# frete grátis de pedido acima de 100 ou tem cupom

valor = float(input("Valor do pedido: "))
cupom = input("Possui cupom (sim/não): ")

possui_cupom = (cupom == "sim")

if valor >= 100 or (possui_cupom):
    print("Frete grátis!")
else:
    print("Não possui frete grátis.")