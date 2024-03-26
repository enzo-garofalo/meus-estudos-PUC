# Fazer um programa que faz a leitura consecutiva de N números inteiros x. 
# Construir um programa que identifica e imprime o MAIOR e o MENOR número entre os números digitados. 
# O valor de N também deve ser digitado e deve ser maior ou igual a 10. 

print(f"\tMaior e menor entre N números!")

n = int(input(f"\nDigite quantos números vão ser digitados: "))
i = 1
maior = menor = 0

if n >= 10:
  while i <= n:
    valor = int(input(f"Digite o {i}º valor: "))
    if i != 1: 
        if valor > maior:
          maior = valor
        elif valor < menor:
          menor = valor
    else:
       maior = menor = valor
    i += 1
  print(f"\n\tO maior valor é {maior} e o menor é {menor}")
else:
  print(f"\tO valor deve ser maior que 10!")