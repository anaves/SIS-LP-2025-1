"""
Escrever citacao bibliografia
ENTRADA: Joselito Ferreira Oliveira
SAIDA: OLIVEIRA, J. F.
"""
autor = input("ENTRADA: ")
# processamento
# dividir palavra pelo caracter ' ' : espaco
termos = autor.split(' ') 
print(f"Autor: {autor}")
print(f"Termos: {termos}")
tamanho = len(termos)
print(f"Tamanho termos: {tamanho}")
print(f"Caracteres autor: {len(autor)}")
print("----------------")
sobrenome = termos[tamanho-1].upper()
print(sobrenome, end=', ')
for indice in range(tamanho-1):
    nome = termos[indice]
    print(nome[0], end='. ')
print()
