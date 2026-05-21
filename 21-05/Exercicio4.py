# revisão: peça um número e mostre a tabuada dele de 1 até 10 usando for.

numero = int(input("Digite um número: "))

print(f"=== TABUADA DO {numero} ===")
for i in range(10):
    i = i + 1
    print(f"{numero} x {i} = {numero*i}")