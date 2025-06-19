palavra1 = sorted(input("Palavra 1: ").upper())
palavra2 = sorted(input("Palavra 2: ").upper())
if sorted(palavra1) == sorted(palavra2):
    print("Sao anagramas")
else:
    print("Nao sao anagramas")