import os
from prettytable import PrettyTable
from colorama import Fore, Back, Style
import oracledb 

# Conexão com o BD e criação de um cursor para manipular o BD;
connection = oracledb.connect(user='ENZODEV', password='1234', dsn='localhost:1521/XEPDB1')  
# connection = oracledb.connect(user='BD15022414', password='Jbwux1', dsn='BD-ACD:1521/XE')
cursor = connection.cursor()

def cadastrar_produto():
    # Limpa a tela do console (apenas Windows)
    os.system("cls")  

    print(Fore.LIGHTBLUE_EX+'='*8+" Cadastrar Produtos "+'='*8+Style.RESET_ALL)

    while True:
        try:
            nome = input("Nome do produto: ").title()
            descricao = input("Descrição: ")
            custo_compra = float(input("Custo de compra: R$ "))
            custo_fixo = float(input("Custo fixo/administrativo [%]: "))
            comissao_vendas = float(input("Comissão de vendas [%]: "))
            imposto = float(input("Imposto sobre a venda [%]: "))
            margem_lucro = float(input("Margem de lucro [%]: "))
            if (custo_fixo + imposto + margem_lucro) >= 100:
                print(Fore.RED+'='*5+" Digite valores válidos! "+'='*5+Style.RESET_ALL)
                continue
            else:
                print(Fore.LIGHTBLUE_EX+'='*36+Style.RESET_ALL)
                break
        except ValueError:
            print(Fore.RED+'='*5+" Digite valores válidos! "+'='*5+Style.RESET_ALL)
            continue

    # Insere e fixa os dados no banco
    cursor.execute(f"""INSERT INTO PRODUTOS(nome, descricao, custo_compra, custo_fixo, comissao_vendas, imposto, margem_lucro) 
                VALUES ('{nome}', '{descricao}', {custo_compra}, {custo_fixo}, {comissao_vendas}, {imposto}, {margem_lucro})""")
    connection.commit()

    # Retorna o código do produto - Identificador único gerado automaticamente pelo OracleDB
    cursor.execute("SELECT MAX(codigo) FROM PRODUTOS")
    codigo = cursor.fetchone()[0]

    sql_comma = (f"""SELECT * FROM PRODUTOS WHERE codigo = {codigo}""")
    
    print(Fore.GREEN+f"\n-----------------------PRODUTO CADASTRADO!------------------"+Style.RESET_ALL)

    consultor(sql_comma)
    
    escolha = input("Deseja cadastrar outro produto:\n[Sim/Não]: ").upper()
    if escolha in ['SIM', 'S']:
        cadastrar_produto()
    else:
        decisao()

def consultar_produtos():
    os.system('cls')
    while True:
        print(Fore.LIGHTBLUE_EX+'='*8+" Consultar Produtos "+'='*8+Style.RESET_ALL)
        print("---------| 1- Por Código  |---------")
        print("---------| 2- Por Nome    |---------")
        print("---------| 3- Todos       |---------")
        print("---------| 4- Voltar      |---------")
        print(Fore.LIGHTBLUE_EX+'='*36+Style.RESET_ALL)
        
        busca = int(input("Como deseja buscar? "))
        if busca == 1:
            codigo = int(input("\nDigite o código do produto: "))
            print()
            sql_comma = (f""" SELECT * FROM PRODUTOS WHERE codigo = {codigo} """)
            break
        elif busca == 2:
            nome = input("\nDigite o nome do produto: ").title()
            print()
            sql_comma = (f""" SELECT * FROM PRODUTOS WHERE nome = '{nome}' ORDER BY codigo """)
            break
        elif busca == 3:
            print()
            sql_comma = (f""" SELECT * FROM PRODUTOS ORDER BY codigo """)
            break
        elif busca == 4:
            os.system('cls')
            menu()
        else:
            os.system('cls')        
            print(Fore.RED+'='*5+" Digite uma opção válida! "+'='*5+Style.RESET_ALL)
            continue

    print(Fore.LIGHTBLUE_EX+'='*65+Style.RESET_ALL)
    existe = consultor(sql_comma)
    if existe == False:
        print('                        Produto não cadastrado!')
    print(Fore.LIGHTBLUE_EX+'='*65+'\n'+Style.RESET_ALL)

    escolha = input("Deseja buscar outro produto:\n[Sim/Não]: ").upper()
    if escolha in ['SIM', 'S']:
        consultar_produtos()
    else:
        decisao()

def consultor(sql_comma):
    existe = False
    for linha in cursor.execute(sql_comma):

        if len(linha) > 0:
            existe = True

        table_consulta = PrettyTable(["Descrição", "Valor", "%"])
        table_consulta.align = "l"

        codigo = linha[0]
        nome = linha[1]
        descricao = linha[2]

        custo_compra = linha[3]
        custo_fixo = linha[4]
        comissao_vendas = linha[5]
        imposto = linha[6]
        margem_lucro = linha[7]

        preco_venda, receita_bruta,imposto_valor,custo_fixo_valor, comissao_vendas_valor, rentabilidade, outros_custos = calcular_preco(custo_compra,custo_fixo,comissao_vendas,imposto,margem_lucro)
        lucro, cor = calcular_lucro(margem_lucro)

        table_consulta.title = cor +f"Código: {codigo} | {nome} | {descricao}"+ Style.RESET_ALL

        table_consulta.add_row(["A. Preço de venda", f"R$ {preco_venda:.2f}", f"{(preco_venda*100)/preco_venda:.2f}%"])
        table_consulta.add_row(["B. Custo de Aquisição (Fornecedor)", f"R$ {custo_compra:.2f}", f"{(custo_compra*100)/preco_venda:.2f}%"])
        table_consulta.add_row(["C. Receita Bruta (A-B)", f"R$ {receita_bruta:.2f}", f"{(receita_bruta*100)/preco_venda:.2f}%"])
        table_consulta.add_row(["D. Custo Fixo/Administrativo", f"R$ {custo_fixo_valor:.2f}", f"{custo_fixo:.2f}%"])
        table_consulta.add_row(["E. Comissão de Vendas", f"R$ {comissao_vendas_valor:.2f}", f"{comissao_vendas:.2f}%"])
        table_consulta.add_row(["F. Impostos", f"R$ {imposto_valor:.2f}", f"{imposto:.2f}%"])
        table_consulta.add_row(["G. Outros Custos (D+E+F)", f"R$ {outros_custos:.2f}", f"{(outros_custos*100)/preco_venda:.2f}%"])
        table_consulta.add_row(["H. Rentabilidade", f"R$ {rentabilidade:.2f}", f"{margem_lucro:.2f}%"])
        table_consulta.add_row(["Lucro", f"{lucro}", "-----"])

        print(table_consulta)

    return existe

def alterar_produtos():
    os.system('CLS')
    print(Fore.GREEN+f"\n------------------ALTERAR----------------------"+Style.RESET_ALL) 
    
    sql_comma = ("""SELECT * FROM PRODUTOS ORDER BY codigo""")

    todas_tabelas = input("\nDeseja mostrar as tabelas cadastradas?\n[Sim/Não]: ")
    todas_tabelas = todas_tabelas.upper()
    
    if todas_tabelas == "SIM" or todas_tabelas == "S":
        consultar_produtos(sql_comma)
    
    chamar_codigo = int(input(f"\nQual produto deseja alterar?\nIdenfique pelo código: "))
         
    selecionar_linha = input("Condição que deseja alterar: ").upper()
    

    if selecionar_linha in ['NOME', 'DESCRICAO', 'DESCRIÇÃO']:
        if selecionar_linha == 'DESCRIÇÃO':
            selecionar_linha = 'DESCRICAO'
        alterar_valor = input("Digite novo valor: ")
        cursor.execute(f"UPDATE PRODUTOS SET {selecionar_linha} = '{alterar_valor}' WHERE codigo = {chamar_codigo}")
    else:
        alterar_valor = float("Digite novo valor: ")
        cursor.execute(f"UPDATE PRODUTOS SET {selecionar_linha} = {alterar_valor} WHERE codigo = {chamar_codigo}")

    connection.commit()
    
    print(Fore.GREEN+f"\n------------------PRODUTO ALTERADO!------------------"+Style.RESET_ALL)
    
    decisao()

def decisao():
 
    while True:
        escolha = input(f"\nVocê deseja retornar ao menu?\n[Sim/Não]: ")
        escolha = escolha.upper()
        if escolha in ["SIM", "S"]:
            os.system("cls")
            menu()
        elif escolha in ["NÃO", "NAO", "N"]:
            print(Fore.LIGHTBLUE_EX+'='*11+" Até logo! "+'='*12+Style.RESET_ALL)
            exit()
        else:
            print(Fore.RED+'='*4+" Digite uma opção válida! "+'='*4+Style.RESET_ALL)
            continue
        
def calcular_preco(custo_compra, custo_fixo, comissao_vendas, imposto, margem_lucro):
    
    preco_venda = (custo_compra) / (1 - ((custo_fixo + comissao_vendas + imposto + margem_lucro) / 100))   
    receita_bruta = preco_venda-custo_compra
    imposto_valor = (preco_venda*imposto)/100
    custo_fixo_valor = preco_venda*((custo_fixo)/100)
    comissao_vendas_valor = (preco_venda*comissao_vendas)/100 
    rentabilidade = (preco_venda * margem_lucro) / 100
    outros_custos = preco_venda*(custo_fixo + comissao_vendas + imposto)/100

    return preco_venda, receita_bruta,imposto_valor,custo_fixo_valor, comissao_vendas_valor, rentabilidade, outros_custos

def calcular_lucro(margem_lucro):
        
        if margem_lucro > 20:
            margem_lucro = Fore.GREEN+f"Alto"+Style.RESET_ALL
            cor = Fore.GREEN
        elif margem_lucro > 10:
            margem_lucro =  Fore.YELLOW+f"Médio"+Style.RESET_ALL            
            cor = Fore.YELLOW

        elif margem_lucro > 0:
            margem_lucro = Fore.LIGHTYELLOW_EX+f"Baixo"+Style.RESET_ALL
            cor = Fore.LIGHTYELLOW_EX

        elif margem_lucro == 0:
            margem_lucro = Fore.BLACK+f"Equilíbrio"+Style.RESET_ALL
            cor = Fore.BLACK

        else:
            margem_lucro =  Fore.RED+f"Prejuízo"+Style.RESET_ALL        
            cor = Fore.RED
        
        return margem_lucro, cor

def menu():
    while True:
        try:
            print(Fore.LIGHTBLUE_EX+'='*13+" MENU "+'='*15+Style.RESET_ALL)
            print("--------| 1- Cadastrar |----------")
            print("--------| 2- Listar    |----------")
            print("--------| 3- Alterar   |----------")
            print("--------| 4- Excluir   |----------")
            print("--------| 5- Sair      |----------")
            print(Fore.LIGHTBLUE_EX+"="+'='*33+Style.RESET_ALL)
            escolha = int(input("O que deseja fazer? "))
            # Verifica a escolha do usuário
            match escolha:
                case 1:
                    cadastrar_produto()
                    break 
                case 2:
                    consultar_produtos()
                    break
                case 3:
                    alterar_produtos()
                    break
                # case 4:
                    # excluir_produto()
                case 5:
                    print()
                    print(Fore.LIGHTBLUE_EX+'='*11+" ATÉ LOGO! "+'='*12+Style.RESET_ALL)
                    exit()  
                case default:
                    os.system("cls")
                    print(Back.RED+'='*4+" Digite uma opção válida! "+'='*4+Style.RESET_ALL)  
                    menu()
        except ValueError:
            os.system('cls')
            print(Fore.RED+'='*4+" Digite uma opção válida! "+'='*4+Style.RESET_ALL)
            continue

if __name__ == '__main__':
    print(Back.LIGHTBLUE_EX + "      BEM VINDO AO CADASTRON!     " + Style.RESET_ALL)
    menu()