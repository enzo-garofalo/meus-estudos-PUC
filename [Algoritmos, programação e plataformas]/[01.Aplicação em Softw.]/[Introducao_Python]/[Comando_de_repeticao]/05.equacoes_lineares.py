# Um sistema de equações lineares da forma:
#                 x = (c*e) - (b*f) / (a*e) - (b*d)
#                 y = (c*f) - (c*d) / (a*e) - (b*d)
# pode ser resolvido utilizando-se as seguintes fórmulas:
# repetir várias vezes a leitura do conjunto de coeficientes (a, b, c, d, e, f) e imprimir a solução x e y. 
# Antes de efetuar a divisão, verificar se ela pode ser feita. Em caso negativo, imprimir uma mensagem de que o
# sistema não tem solução. A repetição de leitura deve ser interrompida com a leitura de a, b, c, d iguais a zero).

print(f"\tSistema de equação linear!")

a = float(input("Digite o valor de A: "))
b = float(input("Digite o valor de B: "))
c = float(input("Digite o valor de c: "))
d = float(input("Digite o valor de D: "))
e = float(input("Digite o valor de E: "))
f = float(input("Digite o valor de F: "))

if a != 0 and b != 0 and c != 0 and d != 0:
    x = (c*e) - (b*f) / (a*e) - (b*d)
    y = (c*f) - (c*d) / (a*e) - (b*d)
    if x < 0 or y < 0:
        print(f"\n\tO sistema não tem solução!")
    else:
        print(f"\tO valor de x é {x:.2f} e o valor de y é {y:.2f}")
else:
    print(f"\n\tO sistema foi interrompido!")

        
    