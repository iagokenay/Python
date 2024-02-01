# Leia um valor inteiro. 
# A seguir, calcule o menor número de notas possíveis (cédulas) no qual o valor pode ser decomposto. 
# As notas consideradas são de 100, 50, 20, 10, 5, 2 e 1. A seguir mostre o valor lido e a relação de notas necessárias.

# Entrada
# O arquivo de entrada contém um valor inteiro N (0 < N < 1000000).

# Saída
# Imprima o valor lido e, em seguida, a quantidade mínima de notas de cada tipo necessárias, conforme o exemplo fornecido.
# Não esqueça de imprimir o fim de linha após cada linha, caso contrário seu programa apresentará a mensagem: “Presentation Error”.

valor = int(input())
print(valor)
# 100
nota100 = valor//100
valor = valor%100
# 50
nota50 = valor//50
valor = valor%50
# 20
nota20 = valor//20
valor = valor%20
# 10
nota10 = valor//10
valor = valor%10
# 5
nota5 = valor//5
valor = valor%5
# 2
nota2 = valor//2
valor = valor%2
# 1
nota1 = valor//1
valor = valor%1
print(f"{nota100} nota(s) de R$ 100,00")
print(f"{nota50} nota(s) de R$ 50,00")
print(f"{nota20} nota(s) de R$ 20,00")
print(f"{nota10} nota(s) de R$ 10,00")
print(f"{nota5} nota(s) de R$ 5,00")
print(f"{nota2} nota(s) de R$ 2,00")
print(f"{nota1} nota(s) de R$ 1,00")