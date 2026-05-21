import random

print("=== JOGO DA FORCA ===")

palavras = ["abacaxi", "tempestade", "dinossauro", "chocolate", "gato",
            "teclado", "cachorro", "oceano", "labirinto", "astronauta"]

palavra = random.choice(palavras)
num_letras = len(palavra)
print(f"A palavra tem {num_letras} letras.")

underscores = []

for i in palavra:
    i = "_"
    underscores.append(i)

vidas = 6
ja_tentadas = []
letras_erradas = []

while(True):
    print()
    print("Palavra: "+ " ".join(underscores))
    if(letras_erradas):
        print(f"Letras erradas: "+ ", ".join(letras_erradas))
    else:
        print(f"Letras erradas: nenhuma")
    print(f"Vidas restantes: {vidas}")

    # chute
    chute_letra = input("Digite uma letra: ").lower()

    if(chute_letra not in ja_tentadas):
        ja_tentadas.append(chute_letra)
    else:
        print("Você já usou essa letra! Tente outra.")
        continue

    for indice,i in enumerate(palavra):
        if(i == chute_letra):
            underscores[indice] = chute_letra
    
    # letra certa ou nao
    if(chute_letra in palavra):
        print("Letra correta!")

        if("_" not in underscores):
            print("\nPalavra: "+ " ".join(underscores))
            print(f"Parabéns! Você venceu! A palavra era: {palavra}")
            break
    else:
        if(chute_letra not in letras_erradas):
            letras_erradas.append(chute_letra)
            vidas = vidas - 1
        print(f"Letra errada! Você perdeu uma vida: {vidas}")

        if(vidas == 0):
            print(f"Você perdeu! A palavra certa era: {palavra}")
            break