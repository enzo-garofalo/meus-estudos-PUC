# Faça um algoritmo que leia uma quantidade não determinada de 
# números positivos. Calcule a quantidade de números pares e 
# ímpares, a média de valores pares e a média geral dos números 
# lidos. O número que encerrará a leitura será zero.

print(f"\n\tQuantidade pares, impares e média!")
num = pares = impares = soma = 0
qtd = 1
while True:
  try:
    num = float(input(f"{qtd}º Número: "))
    qtd += 1
    soma += num
    if num == 0:
      break
    elif num % 2:
      impares += 1
      continue
    else:
      pares += 1
      continue
    
  except ValueError:
    print("Digite um valor válido!")
    continue

print(f"\n\tPrograma interrompido pelo 0!\n")
print(f"Quantidade de números totais: {impares+pares}")
print(f"Quantidade de números pares: {pares}")
print(f"Quantidade de números ímpares: {impares}")
print(f"Média geral: {soma/(pares+impares)}")