# Faça um programa que, dada uma string, diga se ela e um palíndromo ou não. 
# Lembrando que umpalíndromo e uma palavra que tenha a propriedade de poder 
# ser lida tanto da direita para a esquerda como da esquerda para a direita
print(f"\n\tPalindromo!")
palavra = str(input("\nDigite a palavra: "))
invertida = palavra[::-1]
print(f"Essa palavra invertida fica: {invertida}")

invertida_tratada = palavra_tratada = ''
for letra in invertida:
  if letra != ' ':
    invertida_tratada += letra
invertida = invertida_tratada

for letra_p in palavra:
  if letra_p != ' ':
    palavra_tratada += letra_p
palavra = palavra_tratada

if invertida.upper() == palavra.upper(): 
  print(f"\n\t{palavra} é palíndromo!") 
else: 
  print(f"\n\t{palavra} não é palíndromo!")