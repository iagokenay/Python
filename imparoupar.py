# decubra se o numero dado pelo usuario e impar ou par 

numero = int(input('indique um numero : '))

resultado = numero % 2

if resultado == 0:
    print('numero par!')
else:
    print('numero impar') 