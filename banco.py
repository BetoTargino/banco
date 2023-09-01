banco = [
    {'conta': 1, 'nome': 'Mariana', 'saldo': 159.99},
    {'conta': 2, 'nome': 'Jonas', 'saldo': 205.50},
    {'conta': 3, 'nome': 'Lucas', 'saldo': 378.89}
]

conta_Atual = 3

def adicionarConta(nome: str, saldo: float) -> None:
    global conta_Atual
    conta_Atual += 1
    cliente = {
        'conta': conta_Atual,
        'nome': nome,
        'saldo': saldo
    }
    banco.append(cliente)
    print('Cliente CADASTRADO com sucesso!')

def obterConta(conta: int) -> dict or None:
    for cliente in banco:
        if cliente['conta'] == conta:
            return cliente
    return None

def deletarConta(conta: int) -> None:
    cliente = obterConta(conta)
    if cliente:
        banco.remove(cliente)
        print('Cliente DELETADO com sucesso!')
    else:
        print('Cliente NÃO existe!')

def editarNome(novo_nome: str, conta: int) -> None:
    cliente = obterConta(conta)
    if cliente:
        cliente['nome'] = novo_nome
        print('Dados ALTERADOS com sucesso!')
    else:
        print('Cliente NÃO existe!')

def consultarCliente(conta: int) -> None:
    cliente = obterConta(conta)
    if cliente:
        print(f'N. Conta: {conta}')
        print(f"Cliente: {cliente['nome']}")
        print(f"Saldo: {cliente['saldo']}")
    else:
        print('Cliente NÃO existe!')

def listarTodasContas() -> None:
    for cliente in banco:
        consultarCliente(cliente['conta'])
        print('-----------------------------')

if __name__ == '__main__':
    adicionarConta('Beto','1290.99')
    for i in banco:
        print([i])
        print('--------------------------')
        print(obterConta(3))
        #print('--------------------------')
        #deletarConta(2)
        print('--------------------------')
        print(banco)
        print('--------------------------')
        editarNome('Lucas Sousa',3)
        print(banco)
        print('--------------------------')
        print(consultarCliente(4))
        print('--------------------------')
        listarTodasContas()