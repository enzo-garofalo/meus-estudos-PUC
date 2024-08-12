filmes = {}

for i in range(3):
  codigo_inavalido = True
  while codigo_inavalido == True:
    cod = int(input(f'\nCódigo do {i+1}º filme: '))
    if cod in filmes.keys():
      print(f'\n\tDigite Outro Código')
    else:
      codigo_inavalido = False
  
  titulo = input('Digite o título: ')
  diretor = input('Diretor: ')
  ano = int(input('Ano: '))

  filmes[cod] = [titulo, diretor, ano]  
  print('-'*70)

print(filmes)