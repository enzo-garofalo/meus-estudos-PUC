# Escreva umprograma que calcule e imprima o valor de S:
# S = 1/1 + 3/2 + 5/3 + 7/4 °°° 99/50
print(f"\n\tDescobrindo Valor de S!\n")

numerador = -1
s = 0
for denominador in range(1,51):
  numerador += 2
  print(f"({numerador}/{denominador})", end=" ")
  if numerador < 99:
    print("+", end=" ")
  else:
    print("=")
  s += numerador/denominador

print(f"\n\n\tO valor de S é: {s:.2f}")
    