# Crie um dicionário de livros, onde o código do livro é a chave e este dicionário, 
# para cada chave é constituído de uma lista com as outras informações(codigo, título, numero de autores, preço)

# Após a leitura dos dados, realizara as seguintes tarefas
#   • Buscar um livro pelo título, imprimir todas as suas informações se ele existir
#   • Buscar um livro pelo código, imprimir todas as suas informações se ele existir
#   • imprimir os dados dos livros com preço superior a R$50.00. Apresente os dados no formato de uma tabela

from prettytable import prettytable
import os

print("------Biblioteca com dicionários-----\n")
livros = {}
informacao = []

def cadastrar():
        os.system('CLS')
        print("---------Cadastro de livro-----------")
                
        while True:
            try:
                codigo = input("Digite o código do livro: ")
                titulo = input("Digite o Título: ")
                num_autores = int(input("Digite o número de autores: "))
                preco = float(input("Digite o preço do livro: "))
            except ValueError:
                print("------Digite um valor válido---------")
            
            informacao.append(titulo)
            informacao.append(num_autores)
            informacao.append(preco)
            
            livros[codigo] = informacao
        
            
            while True:
                decisao = input("\nDeseja Cadastrar outro livro?\n[SIM/NÃO]: ").upper()
                if decisao in ["S", "SIM"]:
                    cadastrar()
                elif decisao in ["N", "NÃO", "NAO"]:
                    os.system('cls')
                    menu()
                else:
                    print("------Digite um valor válido---------")
            
def consultar():
        os.system('cls')
        while True:
            print("---------Consultar livros-------------")
            print("--------| 1- Por Título    |----------")
            print("--------| 2- Por Código    |----------")
            print("--------| 3- Por Preço     |----------")
            print("--------------------------------------")           
            try:
                escolha = int(input("Como deseja Buscar: "))
                if escolha == 1:
                    os.system('CLS')
                    print("")
                elif escolha == 2:
                    os.system('CLS')
                    print("")
                elif escolha == 3:
                    os.system('CLS')
                    print("")
                else:
                    print("------Digite valores válidos---------")
                    continue
            except ValueError:
                print("------Digite valores válidos---------")
                continue
def menu():
    while True:
        try:
            print("--------------Menu-------------------")
            print("--------| 1- Cadastrar    |----------")
            print("--------| 2- Consultar    |----------")
            print("--------| 3- Sair         |----------")
            print("-------------------------------------")
            escolha = int(input("O que deseja fazer: "))

            if escolha == 1:
                cadastrar()
            elif escolha == 2:
                consultar()
            elif escolha == 3:
                print("\n")
                print("--------------Até Logo!--------------")
                exit()
            else:
                print("------Digite valores válidos---------")
                continue
        except ValueError:
            print("------Digite valores válidos---------")
            continue
            
menu()