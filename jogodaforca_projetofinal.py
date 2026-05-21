import random

print("=== JOGO DA FORCA ===")

palavras = ["abacaxi", "tempestade", "dinossauro", "chocolate", "gato",
            "teclado", "cachorro", "oceano", "labirinto", "astronauta"]

palavra = random.choice(palavras)
num_letras = len(palavra)
print(f"A palavra tem {num_letras} letras.")

while(True):
    underscores = []

    for i in palavra:
        i = "_"
        underscores.append(i)
    print("Palavra: "+ " ".join(underscores))

    #print("Letras erradas: nenhuma")
    #print("Vidas restantes: 6")
    #input("Digite uma letra: ")
    break