# Peça uma temperatura em Celsius e mostre a classificação:
# Menor que 10: Muito frio
# Entre 10 e 25: Clima agradável
# Acima de 25: Calor
temperatura=float(input("Digite a temperatura: "))

if temperatura < 10:
    print("Muito frio")
elif temperatura >= 10 and temperatura < 25:
    print("Clima agradavel")
else:
    print("Calor")