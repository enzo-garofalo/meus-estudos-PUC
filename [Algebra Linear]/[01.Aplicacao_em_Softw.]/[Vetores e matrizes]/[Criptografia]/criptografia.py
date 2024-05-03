import numpy as np

palavra = input("Digite a palavra: ").upper()
alfabeto = {' ': 0,'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8, 'I': 9, 'J': 10, 'K': 11, 'L': 12, 'M': 13, 'N': 14, 'O': 15, 'P': 16, 'Q': 17, 'R': 18, 'S': 19, 'T': 20, 'U': 21, 'V': 22, 'W': 23, 'X': 24, 'Y': 25, 'Z': 26}
matriz_palavra_em_num = np.array([[], []])
letras = []

if len(palavra) % 2 != 0:
    palavra += ' '

for letra in range(len(palavra)):
    for chave, valor in alfabeto.items():
        if palavra[letra] == chave:
            letras.append(valor)

for i in range(0, len(palavra)-1, 2):  
    novaColuna = np.array([[letras[i]], [letras[i+1]]])
    matriz_palavra_em_num = np.append(matriz_palavra_em_num, novaColuna, axis=1)

print("-"*50)
print(f"Matriz da palavra {palavra} em número:")
print(matriz_palavra_em_num)
print("-"*50)

chaveMatriz = np.array([[3, 0], [2, 1]])
criptografada = np.dot(chaveMatriz, matriz_palavra_em_num) % 26


print(f"Matriz da palavra {palavra} criptografada:")
print(criptografada)
print("-"*50)

palavra_criptografada = ''
for linha in criptografada.T:
    for num in linha:
        if num == 0:  
            palavra_criptografada += 'Z'
        else:
            for chave, valor in alfabeto.items():
                if num == valor:
                    palavra_criptografada += chave

if palavra[-1:] == " ":
    palavra_criptografada = palavra_criptografada[:-1]

print(f" {palavra} == {palavra_criptografada}")