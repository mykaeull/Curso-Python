lista = []
cont = 1
print("LISTA COM 5 ELEMENTOS")
while cont <= 5:
    num = int(input(f"Digite o {cont}ª número: "))
    lista.append(num)
    cont = cont + 1
print(f"LISTA: {lista}")
while True:
    print("""OPÇÕES
    [1] PARA ADICIONAR UM ELEMENTO NA LISTA
    [2] PARA ADICIONAR ELEMENTO NA POSIÇÃO DESEJADA
    [3] PARA SUBSTITUIR UM ELEMENTO NA POSIÇÃO DESEJADA
    [4] PARA REMOVER UM ELEMENTO
    [5] PARA REMOVER UM ELEMENTO PELA POSIÇÃO
    [6] PARA MOSTRAR LISTA ATUALIZADA
    [0] PARA SAIR""")
    escolha = int(input("ESCOLHA: "))
    if escolha == 1:
        novo_num1 = int(input("NÚMERO: "))
        lista.append(novo_num1)
    elif escolha == 2:
        novo_num2 = int(input("NÚMERO: "))
        pos_2 = int(input("POSIÇÃO: "))
        lista.insert(pos_2, novo_num2)
    elif escolha == 3:
        novo_num3 = int(input("NÚMERO: "))
        pos_3 = int(input("POSIÇÃO: "))
        lista[pos_3] = novo_num3
    elif escolha == 4:
        remov_num4 = int(input("NÚMERO QUE DESEJA REMOVER: "))
        if remov_num4 in lista:
            lista.remove(remov_num4)
        else:
            print("ESSE NÚMERO NÃO ESTÁ CONTIDO NA LISTA...")
    elif escolha == 5:
        remov_num5 = int(input("POSIÇÃO QUE DESEJA REMOVER: "))
        lista.pop(remov_num5)
    elif escolha == 6:
        print(f"LISTA ATUALIZADA: {lista}")
    elif escolha > 6:
        print("DADO INVÁLIDO...")
    elif escolha == 0:
        break
print("FIM DO PROGRAMA!")



