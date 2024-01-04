#exercicios
#crie funçoes que duplicam triplicam e quadruplicam o numero recebido como parametro

#modo simples 
# def duplicam(numero):
#     return numero*2
# def triplicam(numero):
#     return numero*3
# def quadruplicam(numero):
#     return numero*4
# numero = 4
# print(duplicam(numero))

#modo closure
# def criar_mutiplicador(mutiplicador):
#     def mutiplicar(numero):
#         return numero * mutiplicador
#     return mutiplicar

# duplicar = criar_mutiplicador(2)
# triplicar = criar_mutiplicador(3)
# quadruplicar = criar_mutiplicador(4)

# print(duplicar(2))
# print(triplicar(2))
# print(quadruplicar(2))

# maria pegou emprestimo de 1000 $
# para relizar pagamento em 5 anos 
# a data que ela pegou foi :  20/12/2020 vencimento dia 20 de cada mes
# crie a data do emprestimo 
# crie a data do final do imprestimo 
# mostre todas as data de  vencimento e valor de cada parcela
# from datetime import datetime
# from dateutil.relativedelta import relativedelta

# valor = 1_000_000

# data_emprestimo = datetime(2020, 12, 20)
# delta_anos = relativedelta(years=5)
# data_final = data_emprestimo + delta_anos
# data_pagamento = []
# data_parcela = data_emprestimo
# while data_parcela<data_final:
#     data_pagamento.append(data_parcela)
#     data_parcela+=relativedelta(months=+1)
# numero_parcela=len(data_pagamento)
# valor_par = valor / numero_parcela

# for pagamento in data_pagamento:
#     print(pagamento.strftime('%d/%m/%y'), f'R$ {valor_par:,.2f}')
# print()
# print(f'você pegou R${valor} em {numero_parcela} vezes de : R${valor_par:,.2f}' )
import calendar

print(calendar.calendar(2024))
   