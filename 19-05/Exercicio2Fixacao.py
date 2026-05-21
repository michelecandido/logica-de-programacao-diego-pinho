# LOGIN DE REDE SOCIAL
# pede email, senha
# só funciona se email E senha não estiver vazio

email = input("Digite o e-mail: ")
senha = input("Digite a senha: ")

if email == "" or senha == "":
    print("Erro! Digite e-mail e senha.")
else:
    print("Login feito com sucesso.")