# Elabore um programa que leia um conjunto de vários valores 
# inteiros  e  os  coloque  em  2  listas  conforme  forem  pares  ou 
# ímpares  (uma  lista  para  números  pares  e  outra  lista  para 
# números  ímpares).  A  leitura  dos  números  é  finalizada 
# quando um número negativo é lido.


print("\t Pares e ímpares em N números!")
impares = []
pares = []
num = 0 
while num >= 0:
  try:
    num = int(input("Número: "))

    if num%2 == 0 and num > 0:
      pares.append(num)
    elif num > 0:
      impares.append(num)

  except ValueError:
    print("Digite um número inteiro!")
    continue

print(f"\n\tPares: {pares}")
print(f"\tÍmpares: {impares}")