arq = open('aula.txt','r')

for n in arq.readlines():
    print(n)



arq.close()