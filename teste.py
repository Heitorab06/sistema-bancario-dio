#deposito, saque e extrato
#armazenear cada deposito e saque
#3 saques diarios, limite de 500 reais

saldo = 0
opcao = 0
contador_deposito = 0
contador_saque = 0
valor_depositos = 0
valor_saques = 0
extrato = ''
while(opcao != 3):
    print('''
        -----Menu-----

        [0] Depósito
        [1] Saque
        [2] Extrato
        [3] Sair
    ''')

    opcao = int(input("Digite a opção: "))

    if(opcao == 0):
        deposito = float(input("Digite o valor a ser depositado"))
        saldo += deposito
        valor_depositos += deposito
        contador_deposito += 1
        extrato += f"Depósito de valor {deposito}\n"
        print("Depósito efetuado com sucesso!")

    elif(opcao == 1):
        contador_saque += 1
        if(contador_saque > 3):
            print("Quantidade de saques diários atingido")
            continue

        saque = float(input("Digite o valor para ser sacado"))

        if(saque > saldo):
            print("Saldo insuficiente")
        else:
            saldo -= saque
            valor_saques += saque
            extrato += f"Saque de valor {saque}\n"
            print("Saque efetuado com sucesso!")

    elif(opcao == 2):
        print(extrato)
        print(f"Valor na conta: {saldo}")
        
    elif(opcao == 3):
        break
    else:
        print("Opção inválida, tente novamente")
