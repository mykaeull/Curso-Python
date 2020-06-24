lista_geral = []
lista_parcial = []
lista_maior = []

while True:
    nome = str(input("NOME: "))
    peso = int(input("PESO: "))
    lista_parcial.append(nome)
    lista_parcial.append(peso)
    if len(lista_geral) == 0:
        maior = lista_parcial[1]
        menor = lista_parcial[1]
    else:
        if lista_parcial[1] > maior:
            maior = lista_parcial[1]
            lista_maior.insert(0, maior)
        if lista_parcial[1] < menor:
            menor = lista_parcial[1]
    lista_geral.append(lista_parcial[:])
    lista_parcial.clear()
    escolha = str(input("Quer continuar?[S/N] ")).upper()
    while escolha not in "SN":
        print("DANO INVÁLIDO...")
        escolha = str(input("Quer continuar?[S/N] ")).upper()
    if escolha == "N":
        break

print("-="*25)
print(f"LISTA DOS DADOS CADASTRADOS: {lista_geral}")
print(f"{len(lista_geral)} PESSOAS FORAM CADASTRADAS.")


