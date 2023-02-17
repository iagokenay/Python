#Crie um programa em Linguagem Python que solicite
#a senha de um usuário e depois, peça pra digitar novamente
#até que as duas senhas sejam correspondentes


print('confirmaçao de senha:')
while True:
    s1 = int(input('digite uma senha : '))

    s2 = int(input('confirme sua senha : '))

    if s1 == s2:
        print('senha confirmada parabens !')
        break
    else:
        print('senha errada!')
