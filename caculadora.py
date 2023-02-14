#calculadora 


resultado = 0
while True:
        
    n1 = float(input('digite valor 1:'))
    n2 = float(input('digite valor 2:'))
    op = input('informe a operaçao:')



    if op == '+':
        resultado = n1 + n2

    elif op == '-':
        resultado = n1 - n2

    elif op == '*':
        resultado = n1 * n2

    elif op == '/':
        resultado = n1 / n2

    else:
        print('opçao invalida:')
    print(f'o resultado é {resultado} /n')
