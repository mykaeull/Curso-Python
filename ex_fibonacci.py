num = int(input("Digite um número: "))
n1 = 0
n2 = 1
print("{} - {}".format(n1, n2), end="")
cont = 3
while cont <= num:
    n3 = n1 + n2
    print(" - {}".format(n3), end="")
    n1 = n2
    n2 = n3
    cont = cont + 1
print(" - FIM!")