# calcular o imc

print("*** Calcule seu IMC ***")

peso = float(input("Peso: "))
altura = float(input("Altura: "))
imc = peso / (altura * altura)

if imc >= 30:
    classificacao = "Obesidade"
elif imc >= 25:
    classificacao = "Sobrepeso"
elif imc >= 18.5:
    classificacao = "Peso normal"
else:
    classificacao = "Abaixo do peso"

print(f"Seu IMC é {imc:.2f}")
print(f"Classificação: {classificacao}")