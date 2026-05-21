# Agora para cada nome também temos um sobrenome cadastrado. Mas temos um PROBLEMÃO. A lista de nomes foi escrita ao contrário. Por exemplo, o nome completo do João é João Gomes e não João Souza! Faça o mesmo que exercício anterior mas agora apresente o nome inteiro.

nomes = [
	"Ana", "João", "Maria", 
	"Pedro", "Lucas", "Paula", 
	"Rafael", "Clara", "Marcos", "Sofia"
]

sobrenomes = [
	"Silva", "Souza", "Oliveira", 
  "Santos", "Pereira", "Costa", 
  "Almeida", "Ferreira", "Gomes", "Barbosa"
]

posicao = int(input("Digite uma posição de 1 a 10: "))

if posicao <= len(nomes) and posicao >= 1:
    nome = nomes[posicao - 1]
    sobrenome = sobrenomes[len(sobrenomes) - posicao]
    numero = len(nomes) - 1

    print(f"Quem ocupa a posição {numero} é o(a)... {nome} {sobrenome}.")
else:
    print("Opa, essa posição é inválida!")

"""
outra solução

if posicao < 1 or posicao > len(nomes):
  print("Opa, essa posição é inválida!")
else:
  sobrenome = sobrenomes[len(sobrenomes) - posicao]
  nome_completo = f"{nomes[posicao - 1]} {sobrenome}"
  print(f"Quem ocupa a posição {posicao} é o(a)... {nome_completo}!")

"""