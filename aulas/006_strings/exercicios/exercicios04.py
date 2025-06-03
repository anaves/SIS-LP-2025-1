
"""
4. Faça um programa que decida se duas strings lidas do teclado são palíndromas mútuas, ou seja, se uma é igual à outra quando lida de traz para frente.
Exemplo: amor e roma.
"""

#amor
#roma
palavra1 = input("Palavra 1: ")
palavra2 = input("Palavra 2: ")
eh_palindromo = True
ultimo_indice = len(palavra1)-1
if len(palavra1) == len(palavra2):
    for indice in range(len(palavra1)):
        if palavra1[indice] != palavra2[ultimo_indice-indice]:
            print("nao sao palíndromas")
            eh_palindromo = False
else:
    print("nao sao palíndromas")
    eh_palindromo = False

print(f"Eh {eh_palindromo} que as palavras sao palindromas mutuas")