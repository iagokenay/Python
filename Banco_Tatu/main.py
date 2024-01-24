from cliente import Cliente
from contas import Conta
from banco import Banco
from conta_especial import Conta_Especial

# pedro = Cliente ('Pedrinho noiado', 165414651645)

# maria = Cliente('Maria da Butina', 41651565 )
# joao = Cliente('Joao do gas', 51651654)
# maria = Cliente('Maria vai com as outras', 1156156)

# cont_pedro = Conta(pedro, 157, 33)
# cont_joao = Conta(joao, 123, 10000)
# cont_maria = Conta(maria, 190, 100000)

# print(f'A conta {cont_maria.clientes.nome} foi criada e tem o n° {cont_maria.numero} com saldo de R$ {cont_maria.saldo}')

# #print(pedro.nome, pedro.telefone)
# cont_maria.resumo()
# cont_maria.saque(1000)
# cont_maria.resumo()
# cont_maria.deposito(50000)
# cont_maria.resumo()
# cont_maria.saque(500000)
# cont_maria.resumo()
# cont_maria.extrato()


# print(pedro.nome, pedro.telefone)

# joao = Cliente("Jao do Mandioca", "999995552")
# maria = Cliente("Mariana conta 1", "97777888")
# jose = Cliente("Jose do Paeiro", "445468798")

# contaJM = Conta([joao, maria], 100)
# contaJ = Conta([jose], 10)

# tatu = Banco("Tatu")
# tatu.abre_conta(contaJM)
# tatu.abre_conta(contaJ)
# tatu.lista_contas()

joaomineiro = Cliente('joaomineiro', '377-1234')
maginato = Cliente('maginato', '355-1234')

contax1 = Conta([joaomineiro], 1, 1000)
contax2 = Conta_Especial([maginato],2, 1, 1000)

contax1.saque(50)
contax2.deposito(300)
contax1.saque(190)
contax2.deposito(95.15)
contax1.saque(800)
contax2.saque(1500)

contax1.extrato()
contax2.extrato()
