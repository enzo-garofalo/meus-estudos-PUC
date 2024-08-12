# Faça um programa que dadas as medidas de uma sala em metro
# (comprimento e largura), bem como o preço do metro quadrado
# do carpete, informe o custo total para forrar o piso da sala

print("\nCalculadora para forrar a sala!")

valor = float(input("\n\tInforme o valor do metro quadrado: "))

comp = float(input("\n\n\tDigite o comprimento da sala (metros): "))
larg = float(input("\n\tDigite a largura da sala (metros): "))

print(f"\nValor para forrar a sala: {(comp*larg)*valor}")