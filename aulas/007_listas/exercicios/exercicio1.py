
# preencher das listas
n_elementos = 5

A = []
# preencher A
print("--A--")
for indice in range(n_elementos):
    valor = float(input("Valor: "))
    A.append(valor)
print(A)

B = []
print("--B--")
for indice in range(n_elementos):
    valor = float(input("Valor: "))
    B.append(valor)
print(B)

C = []
print("--C--")
for indice in range(n_elementos):
    r = A[indice]+B[indice]
    C.append(r)
print(C)