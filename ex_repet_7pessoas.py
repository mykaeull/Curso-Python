cont = 5
menores = 0
maiores = 0
for c in range(1, cont+1):
    data_nasc = int(input("Data de nascimento da {}ª pessoa: ".format(c)))
    idade = 2020 - data_nasc
    if idade < 18:
        menores = menores + 1
    else:
        maiores = maiores + 1
print("~~"*40)
print("{} PESSOAS SÃO MENORES DE IDADE E {} PESSOAS SÃO MAIORES DE IDADE.".format(menores, maiores))
print("~~"*40)