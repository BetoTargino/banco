from banco import obterConta, banco

def consultarSaldo(conta: int) -> None:
    cliente = obterConta(conta)
    if cliente:
        print(f'Nome: {cliente["nome"]}')
        print(f'Saldo: {cliente["saldo"]}')
    else:
        print('Conta NÃO existe!')


if __name__ == "__main__":
    consultarSaldo(3)
#    print(banco)

