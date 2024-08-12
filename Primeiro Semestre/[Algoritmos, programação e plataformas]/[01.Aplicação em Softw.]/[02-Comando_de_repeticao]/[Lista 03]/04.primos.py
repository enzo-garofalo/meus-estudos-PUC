# Implemente um programa que determine se um inteiro e  positivo dado pelo usuário, é primo.

print(F"\tSerá que é primo?")
num = int(input(F"\nDigite o número: "))
divisores = 0

if num == 0:
   print(f"\n\t{num} não é primo!")
else:
  
  for i in range(1, num+1):
    if num%i == 0:
      divisores += 1
  
  if divisores > 2:
    print(f"\n\t{num} não é primo!")
  else:
    print(f"\n\t{num} é primo!")