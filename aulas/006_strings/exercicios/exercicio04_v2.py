palavra1 = input("palavra 1: ")
palavra2 = input("palavra 2: ")

if palavra1 == palavra2[::-1]:
    print("palindromo")
else:
    print("nao palindromo")

