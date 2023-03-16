#UTILIZANDO DICIONÁRIO:
#Parte 1 - PROGRAMA PERMITE QUE
#O USUÁRIO CADASTRE PRODUTO
#E VALOR

#Parte 2 -MOSTRE A TABELA DE
#PRODUTOS

#Parte 3 -USUARIO ESCOLHE UM
#PRODUTO E O PROGRAMA
#MOSTRA SEU VALOR

comida = {}

for i in range(4):
    produto = input('nome do produto:')
    valor = input('valor do produto:')
    comida[produto] = valor

print(comida)

escolha = input('escolha um produto: ')

if escolha in comida:
    print(f'valor={comida[escolha]}')
else:
    ('produto fora de estoque')

