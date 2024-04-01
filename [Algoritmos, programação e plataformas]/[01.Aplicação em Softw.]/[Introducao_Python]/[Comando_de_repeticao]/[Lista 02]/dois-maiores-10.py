# Escreva umque solicita 10 números ao usuário, e ao final mostre
# os dois maioresnúmeros digitados pelo usuário.


print(f"\n\tOs dois maiores entre 10!")
maior = maior2 = 0

while True:
  try:
    for i in range(0, 10):
      n = float(input(f"Digite o {i+1}º valor: "))
      
      if i == 0:
        maior = maior2 = n
      elif n > maior:
        maior = maior2
      elif maior < n:
        maior2 = n
    print(f"\nMaior = {maior}\nMenor = {maior2} ")
    break
  except ValueError:
    print(f"\n\tDigite um valor válido!")
    continue