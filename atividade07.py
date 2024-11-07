numero = int(input("Digite um número para ver a tabuada: "))


i = 1


while i <= 10:
    resultado = numero * i
    if resultado % 3 == 0:  
        print(f"{numero} x {i} = {resultado}")  
    i += 1 
