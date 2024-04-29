# Foram a notadas as idades e alturas de 30 alunos. 
# Faça um Programa que determine quantos alunos com mais de 13 anos possuem altura inferior à média de altura desses alunos.
print("\tIdade e altura de 30 alunos")
alunos = []
soma = cont = media = 0

for i in range(30):
  idade = int(input(f"\nDigite a idade do {i+1}º aluno: "))
  altura = float(input(f"Altura: "))
  alunos.append([idade, altura])
  
  soma += alunos[i][1]
  
media = soma/len(alunos)


for k in range(30):
  if alunos[k][0] > 13 and alunos[k][1] < media:
    cont += 1

print(f"\n\tA média das alturas é {media}!\n\tHá {cont} alunos abaixos da média.")