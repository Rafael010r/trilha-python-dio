def menu():
    menu = """\n
    ================MENU===============
    [d]\t Depositar
    [s]\t Sacar
    [e]\t Extrato
    [c]\t Criar conta
    [l]\t Listar contas
    [n]\t Novo Usuario
    [q]\t Sair
    """
    return str(input(menu)).lower()


def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
        print(f"Deposito realizado com sucesso no valor de R${valor:.2f}")
    else:
        print("Operação falhou! O valor informado é inválido.")
    return saldo, extrato


def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    if numero_saques > limite_saques:
        print("Limite de saques excedido")
    elif valor > saldo:
        print("Operação falhou! Saldo suficiente.")
    elif valor > limite:
        print("Operação falhou! O valor do saque acima do limite.")
    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1
        print("Saque realizado com sucesso")
    return saldo, extrato


def mostrar_extrato(saldo, /, *, extrato):
    print("\n================ EXTRATO ================")
    if not extrato:
        print("Não foram realizadas movimentações.")
    else:
        print(extrato)

    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")


def cadastrar_usuario(usuarios):
    cpf = input("Informe o CPF (apenas numeros): ")
    usuario = buscar_usuario(cpf, usuarios)

    if usuario:
        print("Usuario já cadastrado")
        return

    nome = str(input("Informe o Nome completo: "))
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input(
        "Informe o endereço (logradouro, num, bairro, cidade / uf): "
    )

    usuarios.append(
        {
            "nome": nome,
            "data_nascimento": data_nascimento,
            "cpf": cpf,
            "endereco": endereco,
        }
    )
    print("Usuario criado com sucesso!")


def buscar_usuario(cpf, usuarios):
    usuarios_filtrados = [
        usuario for usuario in usuarios if usuario["cpf"] == cpf
    ]
    return usuarios_filtrados[0] if usuarios_filtrados else None


def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o cpf do usuario: ")
    usuario = buscar_usuario(cpf, usuarios)

    if usuario:
        print("----- Conta criada com sucesso -----")
        return {
            "agencia": agencia,
            "numero_conta": numero_conta,
            "usuario": usuario,
        }
    print("Usuario não encontrado, cadastre o usuario primeiro! ")


def listar_contas(contas):
    for conta in contas:
        linha = f"""
            Agencia:\t{conta['agencia']}
            C/C:\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
        print("=" * 100)
        print(linha)


def main():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []

    while True:
        opcao = menu()

        if opcao == "d":
            valor = float(input("Informe o valor do depósito: "))
            saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao == "s":
            valor = float(input("Informe o valor do saque: "))
            saldo, extrato = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES,
            )

        elif opcao == "e":
            mostrar_extrato(saldo, extrato=extrato)
        elif opcao == "c":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)

        elif opcao == "l":
            listar_contas(contas)

        elif opcao == "n":
            cadastrar_usuario(usuarios)

        elif opcao == "q":
            break

        else:
            print("Operação inválida, por favor tente novamente.")


main()
