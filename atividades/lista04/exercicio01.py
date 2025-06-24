"""
Crie um programa que receba uma frase e conte quantas vogais (a, e, i, o, u) ela possui, considerando letras maiúsculas e minúsculas.
Entrada: frase = 'Programação é divertido'
Saída esperada: 8
"""
vogais = ['a','e','i','o','u']
# entrada de dados
frase =  input("Digite a frase: ")
# converter para minuscula
frase_min = frase.lower()
# contar quantas vogais
ocorrencia_a = frase.count('a')
ocorrencia_e = frase.count('e')
ocorrencia_i = frase.count('i')
ocorrencia_o = frase.count('o')
ocorrencia_u = frase.count('u')
total = ocorrencia_a+ocorrencia_e+ocorrencia_i+ocorrencia_o+ocorrencia_u
print(total)