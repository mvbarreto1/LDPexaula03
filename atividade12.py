senha_correta = "12345"

while True:
    senha = input("Digite a senha: ")
    if senha == senha_correta:
        print("Senha correta! Acesso permitido.")
        break  
    else:
        print("Senha incorreta. Tente novamente.")
