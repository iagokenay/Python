arquivo = open('leads.txt','a')
nome = input('informe seu nome :')
email = input('informe seu e-mail : ')

arquivo.write(f'nome : {nome} e contato : {email}')