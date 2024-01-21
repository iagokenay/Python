# # Escreva um programa que leia três valores com ponto flutuante de dupla precisão: A, B e C. Em seguida, calcule e mostre:
# # a) a área do triângulo retângulo que tem A por base e C por altura.
# # b) a área do círculo de raio C. (pi = 3.14159)
# # c) a área do trapézio que tem A e B por bases e C por altura.
# # d) a área do quadrado que tem lado B.
# # e) a área do retângulo que tem lados A e B.
# # Entrada
# # O arquivo de entrada contém três valores com um dígito após o ponto decimal.

# # Saída
# # O arquivo de saída deverá conter 5 linhas de dados. 
# # Cada linha corresponde a uma das áreas descritas acima,
# # sempre com mensagem correspondente e um espaço entre os dois pontos e o valor.
# # O valor calculado deve ser apresentado com 3 dígitos após o ponto decimal.
# for i in range(1):
#     item = input().split(" ")
#     A =float(item[0])
#     B =float(item[1])
#     C =float(item[2])

# pi = 3.14159
# # a) a área do triângulo retângulo que tem A por base e C por altura.
# area1 = (A*C)/2
# # b) a área do círculo de raio C. (pi = 3.14159)
# area2 = pi*C**2
# # c) a área do trapézio que tem A e B por bases e C por altura.
# area3 = (A+B)*C /2
# # d) a área do quadrado que tem lado B.
# area4 = B**2
# # e) a área do retângulo que tem lados A e B.
# area5 = A*B


# print("TRIANGULO: %.3f"%area1)
# print("CIRCULO: %.3f"%area2)
# print("TRAPEZIO: %.3f"%area3)
# print("QUADRADO: %.3f"%area4)
# print("RETANGULO: %.3f"%area5)

for i in range(1):
    item = input().split(" ")
    a = int(item[0])
    b = int(item[1])
    c = int(item[2])
maior = max(a,b,c)
# if a>b and a>c:
#     print(a,"eh o maior")
# elif b>a and b>c:
#     print(b,"eh o maior")
# elif c>a and c>b:
#     print(c,"eh o maior")
print(maior,"eh o maior")
