for i in range(0,999):
    entrada = input('Digite um número: ')
    entrada_2 = input('Digite outro número: ')
    operador = input('Insira um operador [* / - + ]: ')
    if entrada.isdigit() and entrada_2.isdigit():
        pass
    else:
        print('ERROR. Insira dados válidos.')
        break

    entrada = int(entrada)
    entrada_2 = int(entrada_2)
        
    for j in operador:
        if operador == '+':
            calculo = entrada + entrada_2
            print(f'O resultado do seu cáculo foi {calculo}')
            
        if operador == '*':
            calculo = entrada * entrada_2
            print(f'O resultado do seu cáculo foi {calculo}')
            
        if operador == '-':
            calculo = entrada - entrada_2
            print(f'O resultado do seu cáculo foi {calculo}')
            
        if operador == '/':
            calculo = entrada / entrada_2
            print(f'O resultado do seu cáculo foi {calculo:.2f}')
            
    sair = input('Deseja sair? [s]im: ').lower().startswith('s')
    if sair is True:
        print('Saindo...')
        break
    