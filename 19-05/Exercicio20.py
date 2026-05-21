"""
para participar de aulas praticas de direção: maior de 18 e possui RG ou CNH
se não tiver documento, só pode fazer acompanhada
perguntar idade, documento, acompanhada ou não
"""
print("*** AULAS DE DIREÇÃO ***")

idade = int(input("Idade: "))
documento = input("Documento (sim/não): ")
acompanhado = input("Acompanhado (sim/não): ")

if idade >= 18:
    if documento == "sim" or acompanhado == "sim":
        print("Pode participar.")
    else:
        print("Não pode participar.")
else:
    print("Não pode participar.")

"""
outra solução

idade = int(input("Idade: "))
documento = input("Possui documento? (sim/nao): ")
acompanhado = input("Está acompanhado de um responsável? (sim/nao): ")

tem_documento = (documento == "sim")
esta_acompanhado = (acompanhado == "sim")

if idade >= 18 and (tem_documento or esta_acompanhado):
	print("Pode participar.")
else:
	print("Não pode participar.")
    
"""