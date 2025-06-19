# criar lista - estrutura de dados
notas = [100,200,500]
notas.append(9)
print(notas)
print(len(notas))
notas.append(55)
print(notas)
print(len(notas))
notas.append(350)
print(notas)
print(len(notas))
soma = sum(notas)
print(f"a soma = {soma}")
for indice in range(len(notas)):
    valor = notas[indice]
    print(f"{indice} -> conteudo {valor}")