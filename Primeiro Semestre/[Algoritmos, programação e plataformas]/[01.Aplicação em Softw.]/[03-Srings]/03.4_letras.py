# Faça um programa que leia umnome e imprima as 4
# primeiras letras do nome

nome = str(input("Digite seu nome: "))

print(f"Primeiras 4 letras: ", end=" ")
for i in range(0, 4):
    print(f"{nome[i]}", end="")