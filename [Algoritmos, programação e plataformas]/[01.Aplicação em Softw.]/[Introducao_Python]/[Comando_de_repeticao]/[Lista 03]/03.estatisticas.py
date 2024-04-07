# Faça um programa que receba a idade, altura e peso de 25 pessoas. 
# Calcule e mostre:
#     - a.A quantidade de pessoas com idade superior a 50 anos
#     - b.A média das alturas das pessoas com a idade entre 10 e 20 anos
#     - c.O percentual de pessoas com peso inferior a 50 quilos.

print(f"\n\tRegistro de pessoas")
pessoas = 1
peso_menor_50 = soma_altura_adolescente = adolescentes = mais_50 = idade = altura = peso = 0

while pessoas <= 4:
  print(f"\n\tCadastro {pessoas}º pessoa")
  idade = int(input(f"Digite a idade: "))
  altura =  float(input(f"Digite a altura [M]: "))

  if altura > 100:
    altura = (altura/100)

  peso = float(input("Digite o peso [KG]: "))
  if idade > 50:
    mais_50 += 1
  elif idade >= 10 and idade <= 20:
    adolescentes += 1
    soma_altura_adolescente += altura
  elif peso < 50:
    peso_menor_50 += 1

  pessoas +=1

print(f"\n\tEntre {pessoas-1} pessoas: ")
print(f"Há {mais_50} pessoas com mais de 50 anos.")
print(f"A média de altura de pré-adolescentes e adolecentes é {soma_altura_adolescente/adolescentes:.2f}M.")
print(f"Há {(peso_menor_50*100)/pessoas:.2f}% de pessoas com menos de 50 Kg")
