# apenas pessoas acima de 1.60 podem usar um equipamento numa academia

altura = float(input("Digite sua altura: "))
altura_min = 1.60

if altura >= altura_min:
    print("Você pode usar esse equipamento.")
else:
    print("Você não pode usar esse equipamento.")