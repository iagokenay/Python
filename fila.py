#fila = [1 , 2 , 3]

#fila.append (4)#insire um elemento no final da fila 

#fila.pop(0)#remove o primeiro da fila

#EXERCÍCIO

#UTILIZANDO O CONCEITO DE FILA

#FAÇA UM PROGRAMA DE SENHA PARA
#ATENDIMENTO EM UM AÇOUGUE

#O PROGRAMA DEVERÁ TER FUNÇÕES DE:
#- PEGAR SENHA
#- MOSTRAR QUEM ESTA NA FILA(SENHA)
#- CHAMAR SENHA – [ PAINEL ]


fila =[]
senha = 0
print(fila)

def pegasenha():
    global senha
    senha = senha + 1
    fila.append(senha)
    print(fila)
def chamarsenha():
    print('senha',fila.pop(0))
    print(fila)

while True:
    escolha = int(input('1 para pegar senha 2 para chamar senha:'))
    if escolha == 1:
        pegasenha()
    elif escolha == 2:
        chamarsenha()
    else:
        print('escolha invalida')