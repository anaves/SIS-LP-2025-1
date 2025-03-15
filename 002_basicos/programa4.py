# Faca um algoritmo que calcule o valor a pagar em uma lanchonete, dada a quantidade de pasteis comprados e o preco de cada pastel, e a quantidade de refrigerantes comprados e o preco de cada refrigerante, determine o valor a ser pago!

# ENTRADA
valor_pastel = int(input("Digite o valor do pastel: R$ "))
valor_refri = int(input("Digite o valor do refri: R$ "))
qtd_pastel = int(input("Digite a qtd de pasteis: "))
qtd_refri = int(input("Digite a qtd de refri: "))
# PROCESSAMENTO
pagar_pastel = valor_pastel*qtd_pastel
pagar_refri = valor_refri*qtd_refri
pagar_total = pagar_pastel + pagar_refri
# SAIDA
print("-"*30)
print("VALOR PASTEIS R$ ", pagar_pastel)
print(f"VALOR REFRI R$ {pagar_refri}")
print(f"VALOR TOTAL R$ {pagar_total}")

