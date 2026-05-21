participantes = []

while(True):
    print("===============================")
    print("   Participantes - EVENTO ABC  ")
    print("===============================")
    print("1 - Cadastrar participante")
    print("2 - Listar participantes")
    print("3 - Atualizar participantes")
    print("4 - Remover participantes")
    print("0 - Sair")
    print("===============================")

    escolha = int(input("Escolha uma opção: "))

    if(escolha == 1):
        participante = input("Digite o nome do participante: ")
        participantes.append(participante)
    
    elif(escolha == 2):
        if(len(participantes) > 0):
            print("Lista de participantes inscritos:")

            for indice,participante in enumerate(participantes):
                print(f"{indice} - {participante}")
        else:
            print("Nenhum participante cadastrado.")

    elif(escolha == 3):
        indice = int(input("Qual é o índice do participante? "))
        participante_atualizado = input("Digite o novo nome: ")
        participantes[indice] = participante_atualizado
        print("Participante atualizado com sucesso!")

    elif(escolha == 4):
        indice = int(input("Qual é o índice do participante? "))
        participantes.pop(indice)
        print("Participante removido com sucesso.")

    elif(escolha == 0):
        print("Saindo do sistema...")
        break

    else:
        print("Opção inválida.")