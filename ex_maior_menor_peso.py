cont = 3
maior_peso = 0
menor_peso = 0
for c in range(1, cont+1):
    peso = float(input("Peso {}: ".format(c)))
    if c == 1:
        maior_peso = peso
        menor_peso = peso
    else:
        if peso > maior_peso:
            maior_peso = peso
        if peso < menor_peso:
            menor_peso = peso
print("MAIOR PESO: {}".format(maior_peso))
print("MENOR PESO: {}".format(menor_peso))