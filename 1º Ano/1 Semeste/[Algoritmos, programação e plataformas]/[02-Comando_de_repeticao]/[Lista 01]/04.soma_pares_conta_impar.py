# Escreva um algoritmo que leia n de números inseridos pelo  usuário (n é fornecido pelo usuário) e 
# realize a soma dos números pares e conta quantos impares o usuário digitou. 
# O resultado da soma dos pares e o número de ímpares digitados deverá ser impresso no final

print(f"\tSoma dos pares e quantidade de impares!")

n = int(input("\nDigite a quantidade de números: "))
i = 1
pares = 0
impares = 0

while i <= n:
    num = float(input(f"Digite o {i}º número: "))
    if num % 2 == 0:
        pares += num
    else:
        impares += 1
    i += 1

print(f"\n\tSoma dos pares: {pares}\n\tNúmeros de impares: {impares}")



