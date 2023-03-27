""" import math
print(math.sin(3.1415)) """

import random
#choices retorna um inteiro aleatorio da lista
lista = [1,2,3,4,5,6,]
print(random.choices(lista))
#randint retorna um inteiro entre os celecionados 
print(random.randint(3,6))
#shuffle mistura aleatoriamente a lista
random.shuffle(lista)
print(lista)