import os
from tabulate import tabulate
from colorama import Fore, Style
red = Fore.LIGHTRED_EX
green = Fore.LIGHTGREEN_EX
blue = Fore.LIGHTBLUE_EX
reset = Style.RESET_ALL

def calcular_algebra():
    os.system('cls')
    boletim = {
        'Atividade 1': 'Á Definir' ,  
        'Atividade 2': 'Á Definir' , 
        'Atividade 3': 'Á Definir' , 
        'Prova 1': 'Á Definir' , 
        'Prova 2': 'Á Definir' ,      
        'Teste 1': 'Á Definir' , 
        'Teste 2': 'Á Definir' ,      
        'Projeto Integrador': 'Á Definir'
        }
    
    boletim = def_notas(boletim)
    nao_feito = []
    # for nota in boletim.values():
    #     if nota == 0:



    provas = (0.3*boletim['Prova 1'])+(0.35*boletim['Prova 2'])
    media_testes = (0.15*(boletim['Teste 1']+boletim['Teste 2']))/2
    
    atividade = sorted([boletim['Atividade 1'], boletim['Atividade 2'], boletim['Atividade 3']])

    media_atividades = (atividade[0]+atividade[2] / 2)*0.10
    pi = boletim['Projeto Integrador'] * 0.1
    media_final = (10*(media_testes+provas+media_atividades+pi))/9

    print('Média Final:',media_final)


def def_notas(boletim):
    lista = []
    for disciplina, nota in boletim.items():
        os.system('cls')
        print('='*45)
        print('   Digite -1 Caso Ainda Não Tenha Feito')
        print('='*45)

        lista.append([disciplina, nota])
        print(tabulate(lista, headers= ["Nome", 'Nota'],tablefmt='fancy_grid'))
        lista.remove([disciplina, nota])
        print('='*45)
        
        nota = float(input(f'Defina Nota para {disciplina}: '))

        if nota == -1:
            nota = 'Não Feito'
            lista.append([disciplina, nota])
            nota = 0
        else:    
            lista.append([disciplina, nota])
        
        boletim[disciplina] = nota

    os.system('cls')
    print(blue+'='*45+reset)
    print('\t       Notas do Semestre')
    print(blue+'='*45+reset)
    print(tabulate(lista, headers= ["Nome", 'Nota'],tablefmt='fancy_grid'))
    print(blue+'='*45+reset)

    return boletim
def menu():
    while True:
        os.system('cls')
        print('='*22, 'Menu', '='*23)
        print('-'*16, '| 1- Algebra    |', '-'*16)
        print('-'*16, '| 2- Algoritmos |', '-'*16)
        print('-'*16, '| 3- Banco      |', '-'*16)
        print('-'*16, '| 4- Sair       |', '-'*16)
        print('='*51)
        escolha = int(input("O que deseja fazer? "))
        if escolha == 1:
            calcular_algebra()
            break
        elif escolha == 2:
            calcular_algoritmo() 
        elif escolha == 3:
            calcular_banco() 
        elif escolha == 4:
            print('='*20,'Até Logo','='*20)
            exit()
        else:
            print("Digite uma opção válida!")
            continue
            
menu()