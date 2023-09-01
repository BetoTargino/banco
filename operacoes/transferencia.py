from banco import obterConta, banco


def transferir(contaOri: int, contaDes: int, valor: float) -> None:
    contaOrigem = obterConta(contaOri)
    contaDestino = obterConta(contaDes)
    if contaOrigem and contaDestino:
        if contaOrigem['saldo'] >= valor:
            contaOrigem['saldo'] -= valor
            contaDestino['saldo'] += valor
            print('Transferência realizada com sucesso!')
        else:
            print('Saldo insuficiente!')
    else:
        print('Uma ou mais contas não existem!')


if __name__ == '__main__':
    transferir(1, 2, 50)
    print(banco)
