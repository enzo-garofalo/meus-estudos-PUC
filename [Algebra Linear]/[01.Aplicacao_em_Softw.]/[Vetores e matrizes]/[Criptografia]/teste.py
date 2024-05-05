import numpy as np
import os

alfabeto = {' ': 0,'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8, 'I': 9, 'J': 10, 'K': 11, 'L': 12, 'M': 13, 'N': 14, 'O': 15, 'P': 16, 'Q': 17, 'R': 18, 'S': 19, 'T': 20, 'U': 21, 'V': 22, 'W': 23, 'X': 24, 'Y': 25, 'Z': 26}

def criptografar():
    palavra = input("Digite a palavra: ").upper()
    if len(palavra) % 2 != 0:
        palavra += "A"
    matriz_palavra_em_num = palavra_em_matriz(palavra)

    print("-"*50)
    print(f"Matriz da palavra  {palavra} em número:")
    print(matriz_palavra_em_num)
    print("-"*50)

    chaveMatriz = np.array([[4, 3], [1, 2]])
    criptografada = np.dot(chaveMatriz, matriz_palavra_em_num) % 26

    print(f"Matriz da palavra  {palavra} criptografada:")
    print(criptografada)
    print("-"*50)

    print(f" {palavra} == {monta_palavra(criptografada)}")

def decifrar():
    palavra_criptografada = input("Digite a palavra criptografada: ").upper()
    if len(palavra_criptografada) % 2 != 0:
        palavra_criptografada += "A"
    matriz_palavra_em_num = palavra_em_matriz(palavra_criptografada)

    chaveMatrizInversa = np.array([[2, -3], [-1, 4]])
    det = 8
    matriz_palavra_em_num = np.dot(chaveMatrizInversa, matriz_palavra_em_num) % 26

    print('-'*50) 
    print(matriz_palavra_em_num)
    print('-'*50)

    print(f" {palavra_criptografada} == {monta_palavra(matriz_palavra_em_num)}")

def palavra_em_matriz(palavra):
    letras = [alfabeto[ch] for ch in palavra]
    matriz_palavra_em_num = np.array(letras).reshape(-1, 2).T
    return matriz_palavra_em_num

def monta_palavra(matriz):
    palavra_formada = ''
    for linha in matriz.T:
        for num in linha:
            palavra_formada += chr(num + 64) if num != 0 else 'Z'
    return palavra_formada

def menu():
    while True:
        print('-'*10, 'Cifras de Hill', '-'*10)
        print('-'*5, '| 1 - Criptografar    |','-'*6)
        print('-'*5, '| 2 - Descriptografar |', '-'*6)
        print('-'*36)
        escolha = int(input("O que deseja fazer? "))
        if escolha == 1:
            criptografar()
            break
        elif escolha == 2:
            decifrar()
            break
        else:
            os.system('cls')
            print('-'*10, 'Digite uma opção', '-'*10)
            continue
      
if __name__ == '__main__':
    menu()