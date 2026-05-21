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
print("Palavra: "+ " ".join(underscores))

vidas = 6
ja_tentadas = []
letras_erradas = []

while(True):
    print("Palavra: "+ " ".join(underscores))
    print(f"Letras erradas: "+ ", ".join(underscores))
    print(f"Vidas restantes: {vidas}")

    chute_letra = input("Digite uma letra: ").lower()
    break