# CADASTRO EM JOGO ONLINE
# pede nick e idade
# só cadastra se nick não estiver vazio e idade acima 13

nickname = input("Nickname: ")
idade = int(input("Idade: "))

tem_nick = (nickname)

if tem_nick and idade >= 13:
    print("Cadastrado com sucesso.")
else:
    print("Não foi possível completar a ação.")