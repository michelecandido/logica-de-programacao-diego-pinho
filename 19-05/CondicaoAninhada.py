# dizer se é criança, adulto ou adolescente

idade = int(input("Digite sua idade: "))

if (idade >= 18):
    print("Adulto.")
elif (idade >= 12):
    print("Adolescente.")
else:
    print("Criança.")