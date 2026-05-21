rg = input("Digite o seu RG: ")
cpf = input("Digite o seu CPF: ")

if rg == "" and cpf == "":
    print("Preencha o RG ou o CPF!")
else:
    print("Documentação cadastrada com sucesso!")

"""
outra solução (!= significa diferente de)

rg = input("Digite o seu RG: ")
cpf = input("Digite o seu CPF: ")

if rg != "" or cpf != "":
  print("Documentação cadastrada com sucesso!")
else:
  print("Preencha o RG ou CPF")

"""