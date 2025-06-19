palavra1 = input("Palavra 1: ")
palavra2 = input("Palavra 2: ")
palavra1 = palavra1.upper()
palavra2 = palavra2.upper()
# ordenacao -  sorted - ordenar
palavra1 = sorted(palavra1) 
palavra2 = sorted(palavra2)
print(f"palavra 1 ordenada {palavra1}")
print(f"palavra 2 ordenada {palavra2}")
if palavra1 == palavra2:
    print("Sao anagramas")
else:
    print("Nao sao anagramas")