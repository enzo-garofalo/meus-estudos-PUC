# Escrever um algoritmo que leia uma quantidade desconhecida de números e conte quantos deles estão nos seguintes intervalos:
# [0.25], [26,50], [51,75] e [76,100]. A entrada de dados deve terminar quando for lido um número negativo.

print(f"\tQuantidade entre intervalos!")
c1 = c2 = c3 = c4 = i = 0

while i >= 0:
  i = float(input("Digite um número: "))
  if i >= 0 and i <= 25:
    c1 += 1
  elif i >= 26 and i <= 50:
    c2 += 1
  elif i >= 51 and i <= 75:
    c3 += 1
  elif i >= 76 and i <= 100:
    c4 += 1
  elif i < 0:
    print(f"\n\tContagem interrompida!")

print(f"Intervalo entre 0 e 25: {c1}")
print(f"Intervalo entre 26 e 50: {c2}")
print(f"Intervalo entre 51 e 75: {c3}")
print(f"Intervalo entre 76 e 100: {c4}")

