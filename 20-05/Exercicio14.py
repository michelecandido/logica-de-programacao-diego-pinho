import random

n1 = random.randint(1,10)
n2 = random.randint(1,10)

resultado = n1 * n2
chute = 0

while(chute != resultado):
    print(f"Qual é o resultado da conta {n1} x {n2}?")
    chute = int(input("Resultado: "))
    if chute == resultado:
        break
    print("Poxa, você errou! Tente novamente!")

print("Parabéns, você acertou!")