def maior(n):
    cont = maior = 0
    for valor in n:
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont += 1
    return maior

numeros = []
for c in range(1, 6):
    v = int(input(f"Digite o {c}ª valor: "))
    numeros.append(v)
mai = maior(numeros)
print(f"O maior valor dentre {numeros} é o {mai}.")



