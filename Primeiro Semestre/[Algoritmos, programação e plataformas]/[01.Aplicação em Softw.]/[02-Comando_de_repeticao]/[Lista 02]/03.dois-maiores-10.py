# Escreva umque solicita 10 números ao usuário, e ao final mostre
# os dois maioresnúmeros digitados pelo usuário.


print(f"\n\tOs dois maiores entre 10!\n")
maior = maior2 = 0

while True:
  try:
    for i in range(0, 10):
      n = float(input(f"Digite o {i+1}º valor: "))
      
      if i == 0:
        maior = maior2 = n
      
      elif n > maior:
        maior2 = maior
        maior = n

      elif n > maior2 and n < maior:
        maior2 = n
    
    print(f"\n\tMaior = {maior:.2f} | Segundo Maior = {maior2:.2f} ")
    break
  except ValueError:
    print(f"\n\tDigite um valor válido!")
    continue