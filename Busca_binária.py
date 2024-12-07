def busca_binaria(lista, alvo):
    inicio = 0
    fim = len(lista) - 1
    
    while inicio <= fim:
        meio = (inicio + fim) // 2 
        
        if lista[meio] == alvo:
            return True
        
        elif lista[meio] < alvo:
            inicio = meio + 1  
            
        else:
            fim = meio - 1  
    
    return False 

lista = [10, 20, 30, 40, 50]
alvo = 30
if busca_binaria(lista, alvo):
    print("Valor encontrado")
else:
    print("Valor não encontrado")