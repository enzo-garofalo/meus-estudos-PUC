# Faça um programa que, dada uma string, diga se ela e um palíndromo ou não. 
# Lembrando que umpalíndromo e uma palavra que tenha a propriedade de poder 
# ser lida tanto da direita para a esquerda como da esquerda para a direita
print(f"\n\tPalindromo!")
palavra = str(input("\nDigite a palavra: "))
invertida = palavra[::-1]
print(f"Essa palavra invertida fica: {invertida}")
if invertida.upper() == palavra.upper(): 
  print(f"\n\t{palavra} é palíndromo!") 
else: 
  print(f"\n\t{palavra} não é palíndromo!")