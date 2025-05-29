menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

Escolha uma opção: """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu).lower()

    if opcao == "d":
        try:
            valor = float(input("Valor do depósito: R$ "))
            if valor > 0:
                saldo += valor
                extrato += f"Depósito: R$ {valor:.2f}\n"
                print("Depósito realizado.")
            else:
                print("Informe um valor positivo.")
        except ValueError:
            print("Valor inválido.")

    elif opcao == "s":
        try:
            valor = float(input("Valor do saque: R$ "))

            excedeu_saldo = valor > saldo
            excedeu_limite = valor > limite
            excedeu_saques = numero_saques >= LIMITE_SAQUES

            if excedeu_saldo:
                print("Saldo insuficiente.")
            elif excedeu_limite:
                print(f"Limite de R$ {limite:.2f} excedido.")
            elif excedeu_saques:
                print("Limite de saques atingido.")
            elif valor > 0:
                saldo -= valor
                extrato += f"Saque: R$ {valor:.2f}\n"
                numero_saques += 1
                print("Saque realizado.")
            else:
                print("Informe um valor positivo.")
        except ValueError:
            print("Valor inválido.")

    elif opcao == "e":
        print("\n===== EXTRATO =====")
        print(extrato if extrato else "Sem movimentações.")
        print(f"Saldo: R$ {saldo:.2f}")
        print("===================")

    elif opcao == "q":
        print("Saindo...")
        break

    else:
        print("Opção inválida.")
