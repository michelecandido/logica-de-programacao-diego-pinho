# revisão: peça uma senha. enquanto a senha digitada for diferente de "python123", continue pedindo novamente. quando acertar, mostre "acesso liberado".

while(True):
    senha = input("Digite a senha correta: ")

    if(senha != "python123"):
        print("Senha incorreta, tente novamente.")
    else:
        print("Acesso liberado.")
        break