import random # aleatorios
quantidade = int(input("Quantidade de numeros: "))
soma = 0
for i in range(quantidade): # [0,1,2,3,4,5,6,7]
    sorteado = random.randint(1,10)
    print(sorteado)
    soma = soma + sorteado

print(f"soma foi de {soma}")