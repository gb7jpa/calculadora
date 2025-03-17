# TRABALHO DE A3 CALCULADORA DE FUNÇÃO DO SEGUNDO GRAU

# Biblioteca

from time import sleep

# Criando Variáveis e Opções para o programa 

opção = 4 
while opção != 5:
    if opção == 4:
      a = int(input("Valor de a(x²): "))
      b = int(input("Valor de b(x): "))
      c = int(input("Valor de c: "))
      delta = b**2 - 4*a*c
      x1 = (-b - delta**0.5) / (2*a)
      x2 = (-b + delta**0.5) / (2*a)
      sleep(0.2)

    # OPÇÕES USUÁRIO

    print('''  
   [ 1 ] Calcular função do segundo grau 
   [ 2 ] Somar raizes reais da função do segundo grau
   [ 3 ] Subtrair raizes reais da função do segundo grau
   [ 4 ] Novos Valores
   [ 5 ] Sair
    ''')
    opção = int(input('Qual sua opção? '))

    # CODANDO AS OPÇÕES 

    if opção == 1: 
    
      print("x1: ", x1)
      print("x2: ", x2)
      sleep(2)
    
    if opção == 2:
      print("Soma das raizes reais: ", x1+x2)
      sleep(2)

    if opção == 3:
      print("Subtração das raizes reais: ", x1-x2)
      sleep(2)
    
    elif opção == 5:
      print('Encerrando o programa... ')
      print('=-=' * 10)
      sleep(2)
      print('\nObrigado por usar a calculadora, volte sempre!🤝 ')
    
    elif opção <=0 or opção >5:
      print('Opção Inválida. Tente novamente')
      sleep(3.5)
    
    
    
    #####################################
    # ALUNO: GABRIEL RIBEIRO DOS SANTOS #
    # TURNO: MANHÃ                      #
    # MATRICULA: 1262327161             #
    # UNIDADE: IBMR BARRA               #
    #####################################