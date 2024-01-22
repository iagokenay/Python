# Faça um programa que leia três valores e apresente o maior dos três valores lidos seguido da mensagem “eh o maior”. 
# Utilize a fórmula:



# Obs.: a fórmula apenas calcula o maior entre os dois primeiros (a e b).
# Um segundo passo, portanto é necessário para chegar no resultado esperado.

# Entrada
# O arquivo de entrada contém três valores inteiros.

# Saída
# Imprima o maior dos três valores seguido por um espaço e a mensagem "eh o maior".

# for i in range(1):
#     item = input().split(" ")
#     a = int(item[0])
#     b = int(item[1])
#     c = int(item[2])
# maior = max(a,b,c)
# if a>b and a>c:
#     print(a,"eh o maior")
# elif b>a and b>c:
#     print(b,"eh o maior")
# elif c>a and c>b:
#     print(c,"eh o maior")
# print(maior,"eh o maior")

distancia = int(input())
gasto = float(input())


km = distancia / gasto

print("%.3f"%km,"km/l")