soma = 0

while True:
   
    numero = int(input("Digite um número (negativo para sair): "))
    
    if numero < 0:
        break  
    
    soma += numero

print("A soma dos números positivos inseridos é:", soma)