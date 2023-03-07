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


def pesquise(lista, valor):
    for x,e in enumerate(lista):
        if e == valor:
            return x
    return None
L=[10, 20, 25, 30]
print(pesquise(L, 25))

print(pesquise(L, 27))