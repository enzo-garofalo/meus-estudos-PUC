# O índice de massa corpórea (IMC) de uma pessoa é igual ao peso
# (em quilogramas) dividido pelo quadrado de sua altura (em
# metros). Construa um programa que dados o peso e altura de
# uma pessoa, informe o valor de seu IMC

print("\nCalculadora de IMC!")

peso = float(input("\tDigite o peso (KG): "))
altura = float(input("\n\tDigite a altura (metros): "))

print(f"\nO valor de IMC é {peso/altura**2:.2f}")