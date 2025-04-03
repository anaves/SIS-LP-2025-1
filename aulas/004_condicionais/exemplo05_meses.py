"""
Pergunte ao usuario o mes do ano em numeros entre 1 e 12. Seu programa deve retornar por extenso o mes correspondente.
Ex: 
mes = 1 -> retorna janeiro
mes = 7 -> retorna julho
...
se retorna mes do ano incorreto, seu programa deve informa mes invalido.
mes = 15 -> mes invalido
"""

mes_nascimento = int(input("Digite o mes que voce nasceu [1 e 12]: "))

if mes_nascimento == 1:
    print("Voce nasceu em janeiro")
elif mes_nascimento == 2:
    print("Voce nasceu em fevereiro")
elif mes_nascimento == 3:
    print("Voce nasceu em marco")
elif mes_nascimento == 4:
    print("Voce nasceu em abril")
elif mes_nascimento == 5:
    print("Voce nasceu em maio")
elif mes_nascimento == 6:
    print("Voce nasceu em junho")
elif mes_nascimento == 7:
    print("Voce nasceu em julho")
elif mes_nascimento == 8:
    print("Voce nasceu em agosto")
elif mes_nascimento == 9:
    print("Voce nasceu em setembro")
elif mes_nascimento == 10:
    print("Voce nasceu em outubro")
elif mes_nascimento == 11:
    print("Voce nasceu em novembro")
elif mes_nascimento == 12:
    print("Voce nasceu em dezembro")
else:
    print("Mes invalido")
