# Construir um programa que faz a leitura de dois valores inteiros A e
# B. Se os valores forem iguais deverá somar os dois, caso contrário
# multiplique A por B. Ao final de qualquer um dos cálculos deve-se
# atribuir o resultado para uma variável C e mostrar seu conteúdo na
# tela

print(f"\tABC!")

a = int(input("\nDigite o valor de A: "))
b = int(input("Digite o valor de B: "))

if a == b:
    c = a+b
    print(f"\t{a} + {b} = {c}")
else:
    c = a*b
    print(f"\t{a} X {b} = {c}")