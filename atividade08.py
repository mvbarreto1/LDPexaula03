soma = 0
contador = 0


while True:
    
    nota = float(input("Digite a nota do aluno (ou -1 para sair): "))
    
   
    if nota == -1:
        break
    
 
    if 0 <= nota <= 10:
        soma += nota 
        contador += 1  
    else:
        print("Nota inválida. A nota deve estar entre 0 e 10.")


if contador > 0:
    media = soma / contador  
    print(f"A média das notas inseridas é: {media:.2f}")
else:
    print("Nenhuma nota válida foi inserida.")
