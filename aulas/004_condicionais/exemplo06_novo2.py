mes = int(input("Digite o mes: "))

if mes in [1,3,5,7,8,10,12]:
    print("31 dias")
elif mes in [4,6,9,11]:
    print("30 dias")
elif mes == 2:
    print("28 ou 29 dias")
else:
    print("mes incorreto")