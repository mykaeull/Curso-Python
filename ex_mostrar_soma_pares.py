cont = 6
soma = 0
for c in range(1, cont+1):
    num = int(input("{}ª número: ".format(c)))
    if (num%2) == 0:
        soma = soma + num
    else:
        soma = soma + 0
print(soma)
