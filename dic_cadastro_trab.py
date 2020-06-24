ficha = []
nome = str(input("NOME: "))
nasc = int(input("ANO DE NASCIMENTO: "))
cart = int(input("CARTEIRA DE TRABALHO (0 não tem): "))
add_nome = {'nome': nome}
ficha.append(add_nome)
idade = 2020 - nasc
add_idade = {'idade': idade}
ficha.append(add_idade)
add_cart = {'carteira': cart}
ficha.append(add_cart)
if cart == 0:
    print("--"*20)
    for i in ficha:
        for k, v in i.items():
            print(f"{k} tem o valor {v}")
else:
    cont = int(input("ANO DE CONTRATAÇÃO: "))
    sal = int(input("SALÁRIO: R$"))
    print("--"*20)
    add_cont = {'contratação': cont}
    ficha.append(add_cont)
    add_sal = {'salário': sal}
    ficha.append(add_sal)
    for i in ficha:
        for k, v in i.items():
            print(f"{k} tem o valor {v}")

