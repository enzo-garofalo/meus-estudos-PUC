# Escreva umprograma que leia a idade e o primeiro nome de
# várias pessoas. Seu programa deve terminar quando uma  idade negativa for digitada. 
# Ao terminar, seu programa deve escrever o nome e a idade da pessoa mais jovem e mais velha.
print(f"\n\tIdade e nomes!")

idade = idade_jovem = idade_velho = 0
nome = ""
nome_mais_novo = nome_mais_velho = ""


while idade >= 0:
  nome = str(input(f"\nDigite o nome: "))
  idade = int(input(f"Digite a idade: "))


  if idade_jovem == 0 and idade_velho == 0:
    idade_velho = idade_jovem = idade

  elif idade > idade_velho:
    idade_velho = idade
    nome_mais_velho = nome

  elif idade < idade_jovem and idade > 0:
    idade_jovem = idade
    nome_mais_novo = nome

print(f"\nPessoa mais velha: {nome_mais_velho} com {idade_velho}")
print(f"Pessoa mais nova: {nome_mais_novo} com {idade_jovem}")