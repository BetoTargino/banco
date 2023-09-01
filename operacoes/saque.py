from banco import obterConta, banco

def sacar(conta: int, valor: float) -> None:
    cliente = obterConta(conta)
    if cliente:
        if cliente['saldo'] >= valor:
            cliente['saldo'] = cliente['saldo'] - valor
            print('SAQUE realizado com sucesso!')
        else:
            print('Saldo INSUFICIENTE!')
    else:
        print('Cliente NÃO existe!')

if __name__ == '__main__':
    sacar(1,100)
    print(banco)
