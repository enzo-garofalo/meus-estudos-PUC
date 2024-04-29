# Elabore  um  programa  que  leia  uma  lista  de  no  máximo  20 
# elementos inteiros. Em seguida o programa deverá imprimir 
# a quantidade de valores múltiplos de 3.

print("\tMultiplos de 3 em lista: ")

lista = []
multiplos = 0

for i in range(20):
  num=int(input(f"Digite o {i+1}º número: "))
  lista.append(num)
  
  if lista[i]%3 == 0:
    multiplos += 1

print(lista)
if multiplos != 0:
  print(f"\n\tHá {multiplos} múltiplos de 3!")
else:
  print(f"\n\tNão Há múltiplos de 3!")
