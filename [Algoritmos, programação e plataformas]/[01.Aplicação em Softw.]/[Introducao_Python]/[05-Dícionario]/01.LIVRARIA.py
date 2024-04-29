# Crie um dicionário de livros, onde o código do livro é a chave e este dicionário, 
# para cada chave é constituído de uma lista com as outras informações(codigo, título, numero de autores, preço)

# Após a leitura dos dados, realizara as seguintes tarefas
#   • Buscar um livro pelo título, imprimir todas as suas informações se ele existir
#   • Buscar um livro pelo código, imprimir todas as suas informações se ele existir
#   • imprimir os dados dos livros com preço superior a R$50.00. Apresente os dados no formato de uma tabela
from prettytable import PrettyTable
import os
print("------Livraria com Dicionário------\n")
livros = {}
def cadastrar():
    os.system('CLS')
    print("---------Cadastro de livro-----------")   
    while True:
        try:
            codigo = input("Digite o código do livro: ")
            if codigo in livros.keys():
                print("\n---------Digite Outro código-------\n")
                continue
            titulo = input("Digite o Título: ").title()
            num_autores = int(input("Digite o número de autores: "))
            preco = float(input("Digite o preço do livro: "))
        except ValueError:
            print("\n------Digite um valor válido---------")
            continue

        livros[codigo]=[titulo, num_autores, preco]

        decisao = input("\nDeseja Cadastrar outro livro?\n[SIM/NÃO]: ").upper()
        if decisao in ["S", "SIM"]:
            cadastrar()
        elif decisao in ["N", "NÃO", "NAO"]:
            os.system('cls')
            menu()

def consultar():
    os.system('cls')
    while True:
        print("---------Consultar livros-------------")
        print("--------| 1- Por Título    |----------")
        print("--------| 2- Por Código    |----------")
        print("--------| 3- Por Preço     |----------")
        print("--------| 4- Voltar        |----------")
        print("--------------------------------------")           
        try:
            existe = False
            escolha = int(input("Como deseja Buscar: "))

            if escolha == 1:
                busca = input("Digite o título: ").title()
                for codigo, informacoes in livros.items():
                    if informacoes[0] == busca:
                        existe = True
                        print_table(informacoes, codigo)

                if existe == False: print("Não há livros com esse título\n" )

            elif escolha == 2:    
                busca = input("Digite o código: ")
                for codigo, informacoes in livros.items():
                    if codigo == busca:
                        existe = True
                        print_table(informacoes, codigo)

                if existe == False: print("Não há livros com esse código\n" )

            elif escolha == 3:
                print("\nLivros com Preços Superiores a R$ 50.00")
                for codigo, informacoes in livros.items():
                    if informacoes[2] > 50:
                        existe = True
                        print_table(informacoes, codigo)
                if existe == False: print("Não há livros com preço superior a R$50.00\n" )

            elif escolha == 4:
                os.system('cls')
                menu()
            else:
                print("------Digite valores válidos---------")
                continue
        except ValueError:
            os.system('cls')
            print("------Digite valores válidos---------")
            continue

def print_table(informacoes, codigo):
        table_consulta = PrettyTable(["Descrição", "Valor"])
        table_consulta.align = "l"
        table_consulta.add_row(["A. Código: ", codigo])
        table_consulta.add_row(["B. Título: ", informacoes[0]])
        table_consulta.add_row(["C. Número de autores: ", informacoes[1]])
        table_consulta.add_row(["D. Preço: ", f"R${informacoes[2]}"])           
        print(f"\n{table_consulta}\n")

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
                os.system('cls')
                print("------Digite valores válidos---------")
                continue
        except ValueError:
            os.system('cls')
            print("------Digite valores válidos---------")
            continue     

menu()