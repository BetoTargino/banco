from operacoes import consulta, saque, deposito, transferencia
from banco import *

def menu():
    while True:
        print('_________ BEM VINDO AO MENU __________')
        print('1 - Adicionar Conta')
        print('2 - Editar Nome')
        print('3 - Excluir Conta')
        print('4 - Consultar Conta')
        print('5 - Listar Todas as Contas')
        print('6 - Consultar Saldo')
        print('7 - Fazer Depósito')
        print('8 - Fazer Saque')
        print('9 - Transferência')
        print('10 - SAIR')
        opcao = int(input('Selecione uma opção: '))

        if opcao == 1:
            nome = str(input('Digite o nome do cliente: '))
            saldo = float(input('Digite o saldo: '))
            adicionarConta(nome, saldo)
        elif opcao == 2:
            conta = int(input('Digite o número da conta a ser editada: '))
            novoNome = str(input('Digite o no nome: '))
            editarNome(novoNome, conta)
        elif opcao == 3:
            conta = int(input('Digite a conta que deseja excluir: '))
            deletarConta(conta)
            print('Conta deletada com sucesso!')
        elif opcao == 4:
            conta = int(input('Qual o Número da conta que deseja consultar: '))
            consultarCliente(conta)
        elif opcao == 5:
            listarTodasContas()
        elif opcao == 6:
            conta = int(input('Digite o número da conta a ser consultado o saldo: '))
            consultarCliente(conta)
        elif opcao == 7:
            conta = int(input('Qual conta deseja fazer o depósito: '))
            valor = float(input('Digite o valor a ser depositado: '))
            deposito.depositar(conta,valor)
        elif opcao == 8:
            conta = int(input('Digite o número da conta de saque: '))
            valor = float(input('Digite o valor de saque: '))
            saque.sacar(conta, valor)
        elif opcao == 9:
            contaOrigem = int(input('Digite o número da conta de Origem: '))
            contaDestino = int(input('Digite o numero da conta de Destino: '))
            valor = float(input('Digite o valor de transferência: '))
            transferencia.transferir(contaOrigem,contaDestino,valor)

        elif opcao == 10:
            break

menu()