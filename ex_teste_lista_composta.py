lista1 = []
lista2 = []
cont = 0
cont_idade = 0
while cont < 3:
    nome = str(input("NOME: "))
    idade = int(input("IDADE: "))
    lista1.append(nome)
    lista1.append(idade)
    if lista1[1] > 17:
        cont_idade = cont_idade + 1
    lista2.append(lista1[:])
    lista1.clear()
    cont = cont + 1
print(f"DADOS SALVOS: {lista2}")
print(f"{cont_idade} pessoas são maiores de idade.")
