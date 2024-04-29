# Implemente os exercícios pedidos na aula Teórica de Listas
import os

def lista_uma_linha():
  os.system('cls')
  lista = []
  for i in range(10):
    num = int(input(f"{i+1}º Número: "))
    lista.append(num)

  print("\nLista em uma linha: ")
  for e in range(len(lista)):
    print(lista[e], end=" ")

  main()

def busca_quinze():
  lista = []
  for i in range(15):
    os.system('cls')
    num = int(input(f"{i+1}º Número: "))
    lista.append(num)
  
  print("Faça sua busca!")
  while True:
    num_busca = int(input(f"Número buscado: "))
    if num_busca in lista:
      print(f"\t{num_busca} está na lista!")
    else:
      print(f"\t{num_busca} não está na lista!")

    escolha = (input("\nQuer buscar outro número? ")).upper()
    if escolha == "S" or escolha == "SIM":
      os.system('cls')
      continue
    else:
      main()

def lista_dez():
  lista = []
  maiores = 0
  for i in range(10):
    num = int(input(f"{i+1}º Número: "))
    if num > 29:
      maiores += 1
    lista.append(num)
  
  os.system('cls')

  print(f"\nA média dos números é: {sum(lista)/len(lista)}")
  print(f"O maior dos números é: {max(lista)}")
  print(f"A quantidade de números maiores que 29: {maiores}")
  print(f"Lista em uma linha: ")
  
  for e in range(len(lista)):
    print(lista[e], end=" ")
  
  main()

def main():
  escolha = int(input(F"\nDigite qual exercício deseja executar: "))
  if escolha == 1:
    lista_uma_linha()
  elif escolha == 2:
    busca_quinze()
  elif escolha == 3:
    lista_dez()
  else:
    print("\nDigite uma opção válida!")
    main()

main()