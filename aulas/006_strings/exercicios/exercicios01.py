"""
1. Escreva um programa que lê uma frase, uma
palavra antiga e uma palavra nova. O programa
deve imprimir a frase com as ocorrências da
palavra antiga substituídas pela palavra nova.
Exemplo:
 Frase: “Quem parte e reparte fica com a maior parte”
 Palavra antiga: “parte”
 Palavra nova: “parcela”
 Saída: “Quem parcela e reparcela fica com a maior parcela”
"""

print("-"*30)
frase = input("Frase: ")
antiga = input("Palavra antiga: ")
nova = input("Palavra nova: ")
# processamento

frase = frase.replace(antiga, nova)

print(f"Saida: {frase}")