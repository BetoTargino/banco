from banco import obterConta, banco

def depositar(conta: int, valor: float) -> None:
    cliente = obterConta(conta)
    if cliente:
        cliente["saldo"] = cliente["saldo"] + valor
        print('DEPÓSITO realizado com sucesso!')
    else:
        print('Cliente NÃO existe!')

if __name__ == '__main__':
    depositar(1,200)
    print(banco)