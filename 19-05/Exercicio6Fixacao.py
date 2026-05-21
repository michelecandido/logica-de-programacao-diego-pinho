# SISTEMA BIBLIOTECA
# pede dias atraso

dias_atraso = int(input("Dias em atraso: "))


if dias_atraso >= 5:
    print("Multa alta.")
elif dias_atraso >= 1:
    print("Multa leve")
else:
    print("Livro entregue no prazo.")