#descobrir se uma pessoa pode ou não brincar num brinquedo para menor de 12 anos

idade = int(input("Digite sua idade: "))

if idade <= 12:
    print("Você pode brincar!")
else:
    print("Você não pode brincar!")

"""
outra solução

idade = int(input("Digite sua idade: "))
idade_limite = 12

if idade <= idade_limite:
  print("Você pode brincar!")
else:
  print("Você não pode brincar!")
"""