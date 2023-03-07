# definição de uma função 

def soma(a,b):
    print(a+b)

def sub(a,b):
    print(a-b)

soma(1,3)
soma(6,9)
sub(1,1)
sub(9,8)

# funçao com return apos uma chamada 

def soma2(a,b):
    return a+b

print (soma2(3,3))

#pesquisa em lista

def pesquise(lista, valor):
    for x,e in enumerate(lista):
        if e == valor:
            return x
    return None
L=[10, 20, 25, 30]
print(pesquise(L, 25))
print(pesquise(L, 27))

#calculo da media de uma lista

def soma3(L1):
    total=0
    for e in L1:
        total+=e
    return total
def media(L1):
    return(soma3(L1)/len(L1))

L1 = [20, 23, 26, 33, 40]

print(soma3(L1))
print(media(L1))