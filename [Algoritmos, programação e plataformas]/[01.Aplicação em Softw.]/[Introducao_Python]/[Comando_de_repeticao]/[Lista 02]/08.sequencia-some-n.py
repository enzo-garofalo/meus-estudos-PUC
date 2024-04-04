# Dada a sequência matemática de números 2, 3, 5,8,13, 21....
# Construa umprograma que calcule a soma desta sequência para
# os N primeiros termo onde, N é fornecido pelo usuário
# • Exemplo: N=5 S= 2+3+5+8+13 =31
print(f"\n\tSequencia e soma!")
novo = 0
n1 = 2 
n2 = 3
soma = n1 + n2
n = int(input("Digite a quantidade de elementos da sequência: "))

if n == 1:
  soma = n1
  print(soma)
else:
  print(f"\nSequência:\n{n1} + {n2}", end="")
  for i in range(0, n-2):
    novo = n1 + n2
    soma += novo
    n1 = n2
    n2 = novo 
    print(f" + {novo}", end="")
  print(f"\n\n\tSoma da sequncia =",soma)
