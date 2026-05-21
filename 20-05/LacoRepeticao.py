nomes = []

for i in range(3):
    nomes.append(input(f"Digite o nome {i + 1}: "))

for i in range(len(nomes)):
    print(f"- {nomes[i]}")