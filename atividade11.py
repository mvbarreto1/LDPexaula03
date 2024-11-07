while True:
    try:
        numero = int(input("Digite um número entre 1 e 10: "))
        if 1 <= numero <= 10:
            print(f"Número válido: {numero}")
            break  
        else:
            print("Número fora do intervalo. Tente novamente.")
    except ValueError:
        print("Entrada inválida! Por favor, digite um número inteiro.")
