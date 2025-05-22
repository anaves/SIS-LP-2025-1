
numero = 120

resultado = 0 
i = 1
achei = False
while not achei and resultado < numero:
    resultado = i*(i+1)*(i+2)
    if resultado == numero:
        print(f"{i} x {i+1} x {i+2} = {numero}")
        achei = True
    i = i + 1

print("FIM")