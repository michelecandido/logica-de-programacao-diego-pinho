# ENTRADA CAMPEONATP
# pede idade, autorizacao
# pode participar se tem 18+ ou autorizacao

idade = int(input("Idade: "))
autorizacao = input("Autorização (sim/não): ")

tem_autorizacao = (autorizacao == "sim")

if idade >= 18 or (tem_autorizacao):
    print("Pode entrar.")
else:
    print("Não pode entrar.")