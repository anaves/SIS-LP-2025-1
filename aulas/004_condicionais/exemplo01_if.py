numero = -4
p = numero > 0   # verificacao Verdadeira - True
print(f"valor de p: {p}")
# print(type(p))   # tipo booleana - bool
outro_numero = 1
q = outro_numero > 0
print(f"valor de q: {q}")
np = not p
print(f"negacao de p: {np}")
r = p and q
print(f"p E q: {r}")

if p:
    print(f"{numero} eh MAIOR que zero")
else:
    print(f"{numero} eh MENOR ou IGUAL a zero")

print("ok")