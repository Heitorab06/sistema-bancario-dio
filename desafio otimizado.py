#criar função depositar(positional), saque(kw only) e extrato(positional e kw)
#criar funcao criar cliente(armazenar em uma lista, nome, nascimento, cpf e endereço) e criar conta, e vincular

def depositar(valor, saldo, extrato, /,):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"

    else:
        print("Operação falhou! O valor informado é inválido.")
    return saldo, extrato

        
def sacar(*, valor, saldo, limite, numero_saques, LIMITE_SAQUES):
    excedeu_saldo = valor > saldo

    excedeu_limite = valor > limite

    excedeu_saques = numero_saques >= LIMITE_SAQUES

    if excedeu_saldo:
         print("Operação falhou! Você não tem saldo suficiente.")

    elif excedeu_limite:
         print("Operação falhou! O valor do saque excede o limite.")

    elif excedeu_saques:
        print("Operação falhou! Número máximo de saques excedido.")

    elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1

    else:
         print("Operação falhou! O valor informado é inválido.") 
    return saldo, extrato
         
def mostrar_extrato(saldo, /, *, extrato):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")
    
    
def cadastrar_cliente(clientes):
    cpf = input("Informe o CPF: ")
    cpf = cpf.replace(".", "")
    cpf = cpf.replace("-", "")
    
    cliente = checar_cliente(clientes, cpf)

    if cliente:
        print("\n============ Já existe cliente com esse CPF! ============")
        return

    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

    clientes.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

    print("=== Cliente criado com sucesso! ===")
    
    
def criar_conta(clientes, numero_conta, agencia):
    cpf = input("Informe o CPF do cliente: ")
    cliente = checar_cliente(clientes, cpf)

    if cliente:
        print("\n=== Conta criada com sucesso! ===")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": cliente}

    print("================ Usuário não encontrado, fluxo de criação de conta encerrado! ================")
    
def checar_cliente(clientes, cpf):
    
    for cliente in clientes:
        if(cliente["cpf"] == cpf):
            return cliente
        
    return False
    
def listar_contas(contas):
    for conta in contas:
        print(conta)

def main():
    
    menu = """

    [d] Depositar
    [s] Sacar
    [e] Extrato
    [c] Cadastrar Cliente
    [C] Criar conta
    [L] Listar Contas
    [q] Sair

    => """

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    LIMITE_SAQUES = 3
    AGENCIA = "0001"
    clientes = []
    contas = []
    numero_da_conta = 0
    numero_contas = 0
    
    while True:

        opcao = input(menu)

        if opcao == "d":
            valor = float(input("Informe o valor do depósito: "))
            depositar(valor, saldo, extrato)

        elif opcao == "s":
            valor = float(input("Informe o valor do saque: "))
            sacar(valor=valor, saldo=saldo, limite=limite, numero_saques=numero_saques, LIMITE_SAQUES=LIMITE_SAQUES)

        elif opcao == "e":
            mostrar_extrato(saldo, extrato=extrato)
        
        elif opcao == "c":
            cadastrar_cliente(clientes)
            
        elif opcao == "C":
            numero_da_conta = len(contas) + 1
            contas.append(criar_conta(clientes, numero_da_conta, AGENCIA))

        elif opcao == "L":
            listar_contas(contas)
        
        elif opcao == "q":
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")
            
main()
