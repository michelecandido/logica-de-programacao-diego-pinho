# revisão: peça dois números ao usuário e mostre:, a soma, a média com 2 casas decimais, qual dos dois é maior

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

soma = num1 + num2
media = (soma / 2)

if(num1 > num2):
    print(f"A soma dos dois é {soma}. A média é {media:.2f}. {num1} é maior que {num2}.")
elif(num2 > num1):
    print(f"A soma dos dois é {soma}. A média é {media:.2f}. {num2} é maior que {num1}.")
else:
    print(f"A soma dos dois é {soma}. A média é {media:.2f}. {num1} e {num2} são iguais.")