num = int(input("Digite o número fatorial: "))
cont = 1
fatorial = 1
while cont <= num:
    fatorial = fatorial * cont
    cont = cont + 1
print("Valor fatorial de {}: {}".format(num, fatorial))