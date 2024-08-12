# Elabore umprograma que leia vários números inteiros, até
# o usuário digitar umnúmero negativo. Para cada número
# lido deverá ser calculado e impresso seu fatorial
num = 0
resultado = 1
while num >= 0:
  num = int(input("Número: "))
  resultado = 1
  print(f"{num}! = ", end="")
  for i in range(1, num+1):
    resultado *= i
    if i == num:
      print(f"{i}", end="")
    else:
      print(f"{i}*", end="")
   
  print(f" = {resultado}")
  