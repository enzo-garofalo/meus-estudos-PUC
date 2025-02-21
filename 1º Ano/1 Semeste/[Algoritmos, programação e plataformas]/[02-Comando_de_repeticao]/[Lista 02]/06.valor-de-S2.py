# Escreva umprograma que calcule e imprima o valor de S:
# S = 1/1 - 2/4 + 3/9 - 4/16 °°° -10/100
print(f"\n\tDescobrindo Valor de S!\n")

denominador = s = 0

for numerador in range(1,11):

  denominador = numerador**2

  if numerador % 2 == 0:
    print(f"- ({numerador}/{denominador})", end=" ")
    s -= numerador/denominador

  else:
    print(f"+ ({numerador}/{denominador})", end=" ")
    s += numerador/denominador

print(f"\n\n\tO valor de S é: {s:.2f}")