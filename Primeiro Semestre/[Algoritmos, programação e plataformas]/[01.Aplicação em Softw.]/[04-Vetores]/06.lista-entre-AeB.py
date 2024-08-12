# Construa umprograma que leia dois números inteiros: a e b e uma lista com N valores inteiros (N fornecido pelo usuário).
# O programa deverá imprimir quantos elementos da Lista pertencem ao intervalo [a;b]
import os
print(f"\n\tListas em intervalo")

a = int(input("Digite o Valor de A: "))
b = int(input("Digite o Valor de B: "))
cont = 0
lista = []
ab = []

# for k in range(a+1, b):
#   ab.append(k)

# n = int(input("Digite o tamanho da lista: "))

# os.system('cls')
# for i in range(n):
#   lista.append(int(input(f"{i+1}º Número: ")))
#   if lista[i] in ab:
#     cont += 1

# print(f"\nO intervalo de {a} e {b} é ... {ab}")
# print(f"Sua lista é: {lista}")
# print(f"Há {cont} números da sua lista no intervalo de {a} e {b}")
if b < a:
  aux = b
  b = a
  a = aux

n = int(input("Digite o tamanho da lista: "))
for i in range(a+1, b):
  ab.append(i)

for nums in range(n):
  num = int(input(f"{nums+1}º Número: "))
  if num in ab:
    cont += 1

print(f"\nO intervalo de {a} e {b} é ... {ab}")
# print(f"Sua lista é: {lista}")
print(f"Há {cont} números da sua lista no intervalo de {a} e {b}")