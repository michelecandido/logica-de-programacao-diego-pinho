# revisão: peça o nome e a idade da pessoa. mostre uma mensagem dizendo se ela é maior de idade ou menor de idade.

nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))

if(idade >= 18):
    print(f"{nome}, você é maior de idade.")
else:
    print(f"{nome}, você é menor de idade.")