# Escreva umprograma que, utilizando a fórmula que converte um grau Fahrenheit em Celsius, imprime uma tabela com graus em
# Fahrenheit e Celsius, iniciando no grau 30o F até 50o F, de 2 em 2 graus. 
# Aprendi tabela em https://medium.com/@michaelperssonse/python-tutorial-prettytable-2e505be61630
from prettytable import PrettyTable, ALL

table = PrettyTable()
table.padding_width = 5


table.add_column("F°",[])
table.add_column("C°",[])

for f in range(30,52,2):
  c = (f-32)*5/9
  c = round(c)
  table.add_row([f,c])

print(f"{table}")