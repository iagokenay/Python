pratos = []
def adicinar():
    pratos.append('x')
    print(pratos)

def lavar():
    if len(pratos) > 0:
        pratos.pop()
    else:
        print('sem pratos sujos')

#--------usuario
while True:
    escolha = input('adicionar ou lavar : ')
    if escolha == 'adicionar':
         adicinar()
    elif escolha == 'lavar':
       lavar()
    else:
        print('opção invalida')
    print(pratos)