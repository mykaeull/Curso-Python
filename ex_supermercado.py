print("--"*16)
print("MERCADINHO MYKAPYKA")
print("--"*12)
total_compra = 0
cont_prod = 0
cont_valor = 1
menor_valor = 0
while True:
    prod = str(input("Nome do produto: "))
    val = int(input("Preço: R$"))
    total_compra = total_compra + val
    if val > 1000:
        cont_prod = cont_prod + 1
    if cont_valor == 1:
        menor_valor = val
    else:
        if val < menor_valor:
            menor_valor = val
            prod_mais_barato = prod
    cont_valor = cont_valor + 1
    escolha = str(input("Deseja continuar? [S/N]")).upper()
    while escolha not in "SN":
        print("DADO INVÁLIDO...")
        escolha = str(input("Deseja continuar? [S/N]")).upper()
    if escolha == "N":
        print("=======FIM DO PROGRAMA=======")
        break
print(f"O total da compra foi R${total_compra}")
print(f"Temos {cont_prod} produtos custando mais de R$1000")
print(f"O produto mais barato foi {prod_mais_barato} que custa {menor_valor}")

