# usando o cupom LINDODEMAIS a pessoa ganha 10% de desconto numa compra

valor_compra = float(input("Valor da compra: "))
possui_desconto = input("Possui desconto (sim/não)? ")

if possui_desconto == "sim":
    cupom = input("Insira o cupom: ")

    if cupom == "LINDODEMAIS":
        desconto = valor_compra * 0.10
        preco_final = valor_compra - desconto
        print(f"Preço final: {preco_final:.2f}")
else:
    print(f"Cupom não aplicado. Preço final: {valor_compra}")

"""
outra solução

valor = float(input("Digite o valor total da compra: "))
valor_final = valor
tem_cupom = input("Você possui cupom de desconto? (sim/não): ")
if tem_cupom == "sim":
  cupom = input("Digite o código do cupom: ")
  if cupom == "LINDODEMAIS":
    desconto = valor * 0.10
    valor_final = valor - desconto
  else:
    print("Cupom inválido. Nenhum desconto aplicado.")

print("Preço final: R$", valor_final)

"""