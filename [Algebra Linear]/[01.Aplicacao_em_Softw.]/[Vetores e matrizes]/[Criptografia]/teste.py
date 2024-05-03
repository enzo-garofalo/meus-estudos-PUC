#Criptografia
import numpy as np
import string

letras = list(string.ascii_uppercase)
A = np.array([[3,0],[2,1]])
Letras_num = []
Palavra_A = str("BOLA")
P1 = np.array([[],[]])

for i in range(len(Palavra_A)):
    letra = Palavra_A[i]
    Letras_num.append((letras.index(Palavra_A[i])+1))

for i in range(0,((len(Palavra_A))-1),2):
    nova_coluna = np.array([[Letras_num[i]],[Letras_num[i+1]]],dtype=int)
    P1 = np.append(P1,nova_coluna,axis=1)
print(P1)

AP = A.dot(P1)
Pmod = AP%26
print(AP)
print(Pmod)

Crip_Palavra = str()
lenPalavra_A = int(len(Palavra_A)/2)
for x in range(0, lenPalavra_A,1):
    index_linha0 = int(Pmod[0,x]-1)
    index_linha1 = int(Pmod[1,x]-1)
    Crip_Palavra = Crip_Palavra + (letras[index_linha0])+ (letras[index_linha1])


print(Crip_Palavra)