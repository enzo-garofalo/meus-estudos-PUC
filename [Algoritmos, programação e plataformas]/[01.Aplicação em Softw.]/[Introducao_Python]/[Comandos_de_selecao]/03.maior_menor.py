# Construa um programa que leia dois valores e diga qual é o maior entre eles.

print(f"\nMaior ou menor!")

n1 = float(input(f"\nDigite o primeiro valor: "))
n2 = float(input(f"Digite o segundo valor: "))

if n1 > n2:
    print(f"\n\tO número {n1} é maior do que {n2}!")
elif n1 == n2:
    print(f"\n\tOs números são iguais.")
else:
    print(f"\n\tO número {n2} é maior do que {n1}!")