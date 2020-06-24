cont = 3
teste = [4]
for c in range(1, cont+1):
    print(c)
    teste[c] = str(input("{}ª Nome:".format(c)))
print(teste)