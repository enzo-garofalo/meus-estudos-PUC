# Construa um programa que seja constituído de uma lista GAB de 10 elementos caracteres ( esta lista pode ser constituída somente dos caracteres a, b, c, d e e. 
# O programa irá ler o nome e a resposta de 10 alunos de uma turma e deverá imprimir a nota de cada aluno (considerando que cada questão vale 1,0 ponto). 
# O programa deverá também imprimir a média da sala
import os
print("\n\tCorreção das provas!")
gab = ['a', 'b', 'c', 'd', 'e',
       'e', 'a', 'c', 'd', 'e']
notas = []
total_pontos = 0

for aluno in range(2):
  os.system('cls')
  nota_aluno = 0
  print(f'\n{aluno+1}º aluno:')
  nome = input('Digite o nome: ')
  for questao in range(10):
    resposta = input(f"Digite a resposta da {questao+1}º questão: ")
    if resposta == gab[questao]:
      nota_aluno += 1
      total_pontos += 1
  notas.append([nome, nota_aluno])

print('\n'+'-'*70)
print("Média da sala = ", total_pontos/2)
print("Notas: ",notas)