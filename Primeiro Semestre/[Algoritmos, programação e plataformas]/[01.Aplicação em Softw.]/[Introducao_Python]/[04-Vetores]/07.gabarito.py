# Construa um programa que seja constituído de uma lista GAB de 10 elementos caracteres ( esta lista pode ser constituída somente dos caracteres a, b, c, d e e. 
# O programa irá ler o nome e a resposta de 10 alunos de uma turma e deverá imprimir a nota de cada aluno (considerando que cada questão vale 1,0 ponto). 
# O programa deverá também imprimir a média da sala
import os
print("\n\tCorreção das provas!")
gab = ['a', 'b', 'c', 'd', 'e', 'e', 'a', 'c', 'd', 'e']
soma = media = pontos = 0
notas = []
questoes = []

for aluno in range(2):
  print(f"Digite as respostas do {aluno+1}º aluno")
  nome = input("Nome: ")

  for resposta in range(10):
    questoes.append(input(f"Digite a {resposta+1}ª resposta: "))
    if questoes[resposta] == gab[resposta]:
      pontos += 1
      
  os.system('cls')
  notas.append([nome, pontos])
  pontos = 0
  soma += notas[aluno][1]

media = soma / len(notas)
print("Média da sala = ", media)
print("Notas: ",notas)