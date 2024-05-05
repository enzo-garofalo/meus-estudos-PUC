import numpy as np
import os

def text_to_matrix(text):
    text = text.upper().replace(" ", "")
    matrix = []
    for char in text:
        matrix.append(ord(char) - ord('A') + 1)  # Convertendo letras para números de 1 a 26
    matrix = np.array(matrix)
    if len(matrix) % 2 != 0:
        matrix = np.append(matrix, [0])  # Se ímpar, adiciona 'A' no final
    matrix = matrix.reshape(-1, 2).T  # Matriz 2xN
    return matrix

def matrix_to_text(matrix):
    text = ''
    for num in matrix.flatten():
        if num == 0:
            text += ' '
        else:
            text += chr(num + ord('A') - 1)
    return text

def criptografar():
    os.system('cls')
    palavra = input("Digite a palavra: ")
    matriz_palavra_em_num = text_to_matrix(palavra)
    chaveMatriz = np.array([[4, 3], [1, 2]])
    criptografada = np.dot(chaveMatriz, matriz_palavra_em_num) % 26
    palavra_criptografada = matrix_to_text(criptografada)
    print("-"*50)
    print(f"Matriz da palavra {palavra} criptografada:")
    print(criptografada)
    print("-"*50)
    print(f"{palavra} == {palavra_criptografada}")

def decifrar():
    palavra_criptografada = input("Digite a palavra criptografada: ")
    matriz_palavra_em_num = text_to_matrix(palavra_criptografada)
    chaveMatrizInversa = np.array([[2, -3], [-1, 4]])  # Inversa da matriz chave
    decifrada = np.dot(chaveMatrizInversa, matriz_palavra_em_num) % 26
    palavra_decifrada = matrix_to_text(decifrada)
    print("-"*50)
    print(f"Matriz da palavra criptografada {palavra_criptografada} decifrada:")
    print(decifrada)
    print("-"*50)
    print(f"{palavra_criptografada} == {palavra_decifrada}")

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
            print('-'*10, 'Digite uma opção válida', '-'*10)
            continue

if __name__ == '__main__':
    menu()