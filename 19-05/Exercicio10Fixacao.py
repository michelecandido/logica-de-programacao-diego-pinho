# SISTEMA CELULAR
# pede bateria, carregador

bateria = int(input("Bateria: "))
carregador = input("Tem carregador (sim/não): ")

tem_carregador = (carregador == "sim")

if (tem_carregador):
    if bateria >= 20:
        print("Pode usar normalmente.")
    else:
        print("Conecte o carregador.")
else:
    print("Não possui carregador.")