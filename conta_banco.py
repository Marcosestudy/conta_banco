contas = {}

while True:
    print(
        """
          Bem Vindo ao Banco CJB!
          [1] Criar conta
          [2] Depositar
          [3] Sacar
          [4] Ver Histórico
          [5] Ver Saldo
          [6] Sair
         """
    )
    opcao = int(input("Digite sua opção: "))

    if opcao == 1:
        numero_conta = int(input("Digite o número da sua conta: "))
        if numero_conta in contas:
            print("Número da conta já existe, tente novamente.")
        else:
            nome = input("Digite seu nome: ")
            senha = input("Digite sua senha: ")
            # Adicionando a nova conta ao dicionário `contas`
            contas[numero_conta] = {
                "nome": nome,
                "senha": senha,
                "saldo": 0,
                "historico": [],
            }
            print(f"Conta criada com sucesso! Número da conta: {numero_conta}")

    elif opcao == 2:
        numero_conta = int(input("Digite o número da conta: "))
        senha = input("Digite a senha: ")
        if numero_conta in contas and contas[numero_conta]["senha"] == senha:
            valor = float(input("Digite o valor para depositar: "))
            contas[numero_conta]["saldo"] += valor
            contas[numero_conta]["historico"].append(f"Depósito: R${valor}")
            print(
                f"Você depositou R${valor}. Saldo atual: R${contas[numero_conta]['saldo']}"
            )
        else:
            print("Conta não encontrada ou senha incorreta.")

    elif opcao == 3:
        numero_conta = int(input("Digite o número da sua conta: "))
        senha = input("Digite sua senha: ")
        if numero_conta in contas and contas[numero_conta]["senha"] == senha:
            valor_saque = float(input("Informe o valor do seu saque: "))
            if valor_saque <= contas[numero_conta]["saldo"]:
                contas[numero_conta]["saldo"] -= valor_saque
                contas[numero_conta]["historico"].append(f"Saque: R${valor_saque}")
                print(
                    f'Você sacou R${valor_saque}. Seu saldo é: R${contas[numero_conta]["saldo"]}'
                )
            else:
                print("Saldo insuficiente para saque!")
        else:
            print("Conta não encontrada ou senha incorreta.")

    elif opcao == 4:
        numero_conta = int(input("Informe o número da conta: "))
        senha = input("Informe a senha: ")
        if numero_conta in contas and contas[numero_conta]["senha"] == senha:
            if contas[numero_conta]["historico"]:
                print("Histórico de transações:")
                for transacao in contas[numero_conta]["historico"]:
                    print(transacao)
            else:
                print("Nenhum histórico disponível")
        else:
            print("Conta não encontrada ou senha inválida")

    elif opcao == 5:
        numero_conta = int(input("Digite o número da sua conta: "))
        senha = input("Digite sua senha: ")
        if numero_conta in contas and contas[numero_conta]["senha"] == senha:
            print(f'Seu saldo atual é: R${contas[numero_conta]["saldo"]}')
        else:
            print("Conta não encontrada ou senha inválida")

    elif opcao == 6:
        print("Obrigado por usar o banco CJB,volte sempre")
        break

    else:
        print("Opção inválida, tente novamente.")
