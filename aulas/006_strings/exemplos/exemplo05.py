texto = "     ... aorem ipsum dolor sit amet consectetur adipisicing elit. Iure est aliquam laboriosam sequi numquam eius corporis voluptatum officiis, incidunt officia accusantium ab. Vel odit debitis ut officia? A, quaerat architecto!       ...         "
# encontra apenas a primeira ocorrencia
ind = texto.find('a')
print(ind)
comprimento = len(texto) # total de caracteres
ind = -10 
while ind != -1:
    if ind != -10: 
        ind = texto.find('a', ind+1, comprimento)
    else:
        ind = texto.find('a')

    print(f'indices {ind}')

print(texto, end='|')

# remove espacos do inicio e fim da string
texto =  texto.strip()
print("\n-----")
print(texto, end='|')
print()