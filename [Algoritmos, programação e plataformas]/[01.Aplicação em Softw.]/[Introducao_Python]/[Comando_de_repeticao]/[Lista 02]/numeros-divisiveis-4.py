# Elabore umprograma que leia umnúmero e imprima todos os
# números divisíveis por 4 que sejammenores que este número lido

print(f"\n\tNúmeros divisíveis por 4!")

while True:
  try:
    n = int(input("Digite o número: "))
    for i in range(0, n, 4):
      print(f"4 X {i//4} = {i}")
    print(f"\n\tValores menores que {n} divisíveis por 4!")
    break
  except ValueError:
    print("Digite um valor inteiro!")
    continue