def busca_simples(lista, alvo):
    for item in range(lista):
        print(item)
        if item == alvo:
            print(f'Item acima encontrado')
            return True

lista = 1000
alvo = 100
if busca_simples(lista, alvo):
    print('Encontrado')
else:
    print('Não encontrado')