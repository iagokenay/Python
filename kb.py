mb = int(  input("informe mb = ")  )
kb = mb*1024
velocidade = 256
segundos = kb/velocidade

if segundos > 60:
    print(f"o valor selecionado em mb resulta em um total de {kb} em kb fornecendo uma velocidade de {segundos} minutos")

print(f"o valor selecionado em mb resulta em um total de {kb} em kb fornecendo uma velocidade de {segundos} segundos")


    