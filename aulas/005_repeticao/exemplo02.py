numero = int(input("Digite primeiro valor "))
numero_final = int(input("Digite segundo valor "))

pares = 0
while numero <= numero_final:
    print(numero)
    if numero % 2 == 0:
        # par
        print(f" par")
        pares = pares + 1
    numero += 1   # numero = numero + 1
print("-------")
print(f'PAR: tem {pares} numeros')