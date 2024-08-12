# Um usuário deseja utilizar um sistema protegido por senha. Ele 
# tem 3 tentativas para acertar a senha correta. Defina uma senha 
# (tipo int) e faça um programa que solicite a senha do usuário. 
# Enquanto ele não acertar o programa deverá imprimir “Acesso 
# negado”. Caso contrário, deverá imprimir “Acesso liberado”.

print(f"\tSistema protegido por Senha!")
senha = "1234"
attempts = 3
while True:
  if attempts == 0:
    print(f"\n\tAcesso Negado.")
    break

  attempt = input(f"\nDigite sua senha: ")

  if attempt == senha:
    print(f"\n\tAcesso Liberado.")
    break
  else:
    attempts -= 1
    print(f"Você tem {attempts} tentativas!")