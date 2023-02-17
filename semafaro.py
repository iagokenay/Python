#FAÇA UM PROGRAMA QUE SIMULE UM
#SEMAFORO DE TRÂNSITO(aqueles com contagem)

#VERMELHO - 30 SEGUNDOS
#VERDE - 50 SEGUNDOS
#AMARELO - 5 SEGUNDOS

vermelho = 30
verde = 50
amarelo = 5

while vermelho > 0:
    print('vermelho', vermelho)
    vermelho = vermelho - 1
while verde > 0:
    print('verde', verde)
    verde = verde - 1
while amarelo > 0:
    print('amarelo', amarelo)
    amarelo = amarelo - 1