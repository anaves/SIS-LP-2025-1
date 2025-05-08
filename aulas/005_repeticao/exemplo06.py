numero_inicial = int(input("Primeiro valor: "))
numero_final = int(input("Segundo valor: "))

for i in range(numero_inicial, numero_final+1):     # i - iterador
    if i%2 == 0:
        print(i)
