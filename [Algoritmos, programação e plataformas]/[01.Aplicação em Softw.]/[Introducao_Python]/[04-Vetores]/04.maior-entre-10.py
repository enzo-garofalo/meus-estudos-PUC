# Elabore um programa que leia uma lista de no máximo 10
# elementos reais, o programa deverá imprimir o maior e
# segundo maior elemento e suas respectivas posições na
# lista

print("\tOs dois maiores de 10")

maior = maior2 = 0
imaior = imaior2 = 0
lista = []

# for i in range(10):
#   num = int(input(F"{i+1}º Número: "))
#   lista.append(num)

#   if num > maior:

#     maior2 = maior
#     maior = num

#     imaior2 = imaior
#     imaior = i
    
#   elif num > maior2:
#     maior2 = num
#     imaior2 = i

for i in range(10):
  num = float(input(f'Digite {i+1}º núm.: '))
  lista.append(num)
for index in range(10):
  if lista[index] > maior:
    maior2 = maior
    imaior2 = imaior
    
    maior = lista[index]
    imaior = index
  elif lista[index] > maior2:
    maior2 = lista[index]
    imaior2 = index

print(f"\n\tLista: {lista}")
print(f"\t{maior} está na posição: {imaior}")
print(f"\t{maior2} está na posição: {imaior2}")