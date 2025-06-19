nomes = []
notas = []
qtd = 40

print("---lancar notas---")
for indice in range(qtd):
    nom = input("digite nome: ")
    valor = float(input(f"digite nota do {nom}: "))
    nomes.append(nom)
    notas.append(valor)
### fora do for
media = sum(notas)/len(notas)
print("------")
print(f"media: {media:.2f}")
print("------")
for i in range(len(notas)):
    print(f"{i}- {nomes[i]}: {notas[i]}")
    if notas[i] > media:
        print(f"Parabens {nomes[i]}!!!")