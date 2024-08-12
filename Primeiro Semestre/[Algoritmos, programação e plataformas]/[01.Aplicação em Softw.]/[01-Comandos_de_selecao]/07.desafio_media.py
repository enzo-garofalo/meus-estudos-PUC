# Construir um programa que faz a leitura de duas
# notas de um aluno, N1 - 40% e N2 - 60%, e os respectivos pesos, P1 e P2. O programa deve calcular a média 
# ponderada alcançada por aluno e apresentar:
# • A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
# • A mensagem "Reprovado", se a média for menor do que sete;
# • A mensagem "Aprovado com Distinção", se a média for igual a dez

print(f"\n\tMédia!")

n1 = float(input(f"\nDigite a nota de peso 1: "))
n2 = float(input(f"Digite a nota de peso 2: "))

media = (n1*0.4) + (n2*0.6)

if media >= 7 and media < 10:
    print(F"\tO aluno está aprovado!")
elif media < 7:
    print(F"\tO aluno está reprovado!")
else:
    print(f"\nO aluno está aprovado com distinção!")