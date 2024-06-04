from tabulate import tabulate
boletim = {
    'Atividade 1': 10 ,  'Atividade 2': 'Á Definir' , 
    'Atividade 3': 'Á Definir' ,  'Prova 1': 10, 
    'Prova 2': 10 ,      'Teste 1': 'Á Definir' , 
    'Teste 2': 'Á Definir' ,      'Projeto Integrador': 'Á Definir'
          }

print(tabulate(boletim))
print(boletim[10])
provas = (0.3*boletim['Prova 1'])+(0.35*boletim['Prova 2'])
print(provas)
# print(boletim[1][0])