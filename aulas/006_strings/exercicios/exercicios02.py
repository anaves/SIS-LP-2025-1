"""
2. Faça um programa que lê uma frase e retorna o número de palavras que a frase contém. Considere que a palavra pode começar e/ou terminar por espaços.
"""
# opcao: print(f"A frase tem {len(input("Frase: ").strip().split(' '))} palavras")

# input -> leio valor em seguida removo espacos do inicio e fim da frase (strip)!
frase = input("Frase: ").strip().split(' ')
# separar pelo caracter espaco --> split
frase_separada = frase.split(' ')
print(frase_separada)
qtd_palavras = len(frase_separada)
print(f"A frase tem {qtd_palavras} palavras")
