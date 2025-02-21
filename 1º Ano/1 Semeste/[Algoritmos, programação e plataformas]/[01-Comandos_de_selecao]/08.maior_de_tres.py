# Construir um programa que faz a leitura de três número inteiros e imprime o maior


print(f"\n\tO maior entre três!")

n1 = float(input(f"\nDigite o primeiro valor: "))
n2 = float(input(f"\nDigite o segundo valor: "))
n3 = float(input(f"\nDigite o terceiro valor: "))

if n1 > n2:
    maior = n1
else:
    maior = n2

if maior > n3:
    print(f"\tO maior valor é {maior}")
else:
    print(f"\tO maior valor é {n3}")
