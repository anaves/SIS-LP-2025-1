
"""
Programa que imprime a soma de todos os números pares entre dois números quaisquer, incluindo-os
"""
num_inicial = int(input("Digite primeiro valor: "))
num_final = int(input("Digite segundo valor: "))
soma = 0
qtd = 0
while num_inicial <= num_final:
    #  ver se num eh par
    if num_inicial % 2 == 0:
        soma = soma + num_inicial
        print(f"soma parcial = {soma}")
        qtd = qtd + 1
    num_inicial += 1     # num = num + 1
print("="*20)
print(f"soma final = {soma}")
print(f"quantidade de pares = {qtd}")