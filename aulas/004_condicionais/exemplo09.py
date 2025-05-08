  
#9- Peça ao usuário que digite uma senha. Se a senha for "admin123", mostre "Acesso concedido", senão, "Senha incorreta".

senha_digitada = input("Digite a senha: ")

if senha_digitada == "admin123":
    print("acesso concedido")
else:
    print("senha incorreta")