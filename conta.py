minutos = int(input('quantos minutos voce utilizou este mes = '))

if minutos < 200 :
    preço = 0.20
else:
    if minutos < 400:
        preço = 0.18
    else:
        preço = 0.15
print(f'total de fatura mensal igual a = {minutos*preço}')