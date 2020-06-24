valor = float(input("Valor da casa: R$"))
sal = float(input("Salário do comprador: R$"))
tempo = int(input("Quantos anos de financiamento? "))
valor_emprest = valor / (tempo*12)
valor_sal = sal * (30/100)
if valor_sal < valor_emprest:
    print("Para pagar uma casa de {} em {} anos a prestação será de R${:.2f}".format(valor, tempo, valor_emprest))
    print("EMPRÉSTIMO NEGADO!")
else:
    print("Para pagar uma casa de {} em {} anos a prestação será de R${:.2f}".format(valor, tempo, valor_emprest))
    print("EMPRÉSTIMO APROVADO!")

