# Abaixo há uma lista com 10 nomes cadastrados. Escreva um programa que pergunta a um usuário pela posição e você precisa dizer quem é o usuário que a ocupa. Mas tem um porém, a posição que o usuário te dará é de 1 até um número qualquer.

#Se o número for menor do que 1 ou maior do que 10, entregue uma mensagem dizendo: posição inválida. Caso contrário, mostre quem ocupa a posição.

nomes = [
	"Ana", "João", "Maria", 
	"Pedro", "Lucas", "Paula", 
	"Rafael", "Clara", "Marcos", "Sofia"
]

resposta = int(input("Digite uma posição de 1 a 10: "))
posicao = (resposta <= len(nomes) and resposta >= 1 )

if not posicao:
    print("Opa, essa posição é inválida!")
else:
    participante = nomes[resposta - 1]
    print(f"O participante nesse posição é {participante}.")