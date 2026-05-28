def main():
    menu = """
================ MENU ================
[d]\tDepositar
[s]\tSacar
[e]\tExtrato
[q]\tSair
=> """

    saldo = 0.0
    limite = 500.0
    extrato = ""
    numero_saques = 0
    LIMITE_SAQUES = 3

    while True:
        opcao = input(menu).strip().lower()

        if opcao == "d":
            try:
                valor = float(input("Informe o valor do depósito: R$ "))
                if valor > 0:
                    saldo += valor
                    extrato += f"Depósito:\tR$ {valor:.2f}\n"
                    print("\n=== Depósito realizado com sucesso! ===")
                else:
                    print("\n@@@ Operação falhou! O valor informado é inválido. @@@")
            except ValueError:
                print("\n@@@ Operação falhou! Digite um valor numérico válido. @@@")

        elif opcao == "s":
            try:
                valor = float(input("Informe o valor do saque: R$ "))

                excedeu_saldo = valor > saldo
                excedeu_limite = valor > limite
                excedeu_saques = numero_saques >= LIMITE_SAQUES

                if excedeu_saldo:
                    print("\n@@@ Operação falhou! Você não tem saldo suficiente. @@@")
                elif excedeu_limite:
                    print("\n@@@ Operação falhou! O valor do saque excede o limite permitido por transação. @@@")
                elif excedeu_saques:
                    print("\n@@@ Operação falhou! Número máximo de saques diários excedido. @@@")
                elif valor > 0:
                    saldo -= valor
                    extrato += f"Saque:\t\tR$ {valor:.2f}\n"
                    numero_saques += 1
                    print("\n=== Saque realizado com sucesso! ===")
                else:
                    print("\n@@@ Operação falhou! O valor informado é inválido. @@@")
            except ValueError:
                print("\n@@@ Operação falhou! Digite um valor numérico válido. @@@")

        elif opcao == "e":
            print("\n================ EXTRATO ================")
            print("Não foram realizadas movimentações." if not extrato else extrato)
            print(f"\nSaldo:\t\tR$ {saldo:.2f}")
            print("==========================================")

        elif opcao == "q":
            print("\nObrigado por utilizar o nosso sistema bancário!")
            break

        else:
            print("\n@@@ Operação inválida, por favor selecione novamente a operação desejada. @@@")


if __name__ == "__main__":
    main()
