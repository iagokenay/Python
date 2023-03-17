alunos ={}

for i in range(3):
    nome = input('nome: ')
    nota = float(input('nota:'))

    if nota >= 7:
        situacao = 'aprovado'
    else:
        situacao = 'reprovdo'
    alunos[nome] = situacao

print(alunos)