import numpy as np
import string

# Solicita ao usuário para inserir a palavra a ser criptografada
palavra = input("Digite a palavra: ").upper()

# Dicionário para mapear letras para números
alfabeto = {' ':0, 'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8, 'I': 9, 'J': 10, 'K': 11, 'L': 12, 'M': 13, 'N': 14, 'O': 15, 'P': 16, 'Q': 17, 'R': 18, 'S': 19, 'T': 20, 'U': 21, 'V': 22, 'W': 23, 'X': 24, 'Y': 25, 'Z': 26}

# Inicializa a matriz de palavras em números
matriz_palavra_em_num = np.array([[], []])

# Se o comprimento da palavra for ímpar, adiciona um espaço
if len(palavra) % 2 != 0:
    palavra += ' '

letras = []

# Converte a palavra em números usando o alfabeto
for letra in range(len(palavra)):
    for chave, valor in alfabeto.items():
        if palavra[letra] == chave:
            letras.append(valor)

# Constrói a matriz de números
for i in range(0, len(palavra)-1, 2):  
    novaColuna = np.array([[letras[i]], [letras[i+1]]])
    matriz_palavra_em_num = np.append(matriz_palavra_em_num, novaColuna, axis=1)

# Define a matriz de chave
chaveMatriz = np.array([[3, 0], [2, 1]])

# Calcula a criptografia
criptografada = np.dot(chaveMatriz, matriz_palavra_em_num) % 26

# Imprime a matriz criptografada
print(criptografada.T)

# Converte os números criptografados de volta para letras e imprime a palavra criptografada
palavra_criptografada = ''
for linha in criptografada.T:
    for num in linha:
        if num == 0:  # Caso o número seja zero, o valor correspondente é 'Z'
            palavra_criptografada += 'Z'
        else:
            for chave, valor in alfabeto.items():
                if num == valor:
                    palavra_criptografada += chave

print(palavra_criptografada)