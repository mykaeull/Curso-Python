lista = []
num = int(input("Digite quantos números você quer adicionar na lista: "))
cont = 0
while cont < num:
    v = int(input(f"Digite um valor para a posição {cont}: "))
    lista.append(v)
    if cont == 0:
        maior = lista[cont]
        menor = lista[cont]
    else:
        if lista[cont] > maior:
            maior = lista[cont]
        if lista[cont] < menor:
            menor = lista[cont]
    cont = cont + 1
print(lista)
print(f"Maior: {maior}")
print(f"Menor: {menor}")