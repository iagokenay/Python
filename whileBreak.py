#while break para somar numeros 
s = 0

while True:
    v = int(input('digite numeros para somar e 0 para obter o resultado:'))
    if v==0:
        break
    s = s + v
print(s)