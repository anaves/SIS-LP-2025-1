opcao = 's'

while opcao == 's':
    numero = int(input("digite: "))

    contar = 0
    for divisor in range(1, numero+1):
        resto = numero % divisor
        if resto == 0:
            contar = contar + 1

    if contar == 2:
        print(f"{numero} primo")
    else:
        print(f"{numero} nao primo")
    opcao = input("continuar? ")
    