#escreva um programa que pergunte a velocidade do carro de um usuario. caso utrapasse 80km/h exiba uma mensagem dizendo que o usuario foi multado nesse caso, exiba o valor da multa cobrando R$ 5 por km/h a cima de 80 km/h

velocidade = int(input('qual sua velocidade ?'))

if velocidade > 80:
    print(f"velocidade acima do permintido, multa gerada igual a :R${(velocidade-80) * 5}")
else:
      print('velocidade altorizada')