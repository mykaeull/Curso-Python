n1 = int(input("PRIMEIRO NÚMERO: "))
n2 = int(input("SEGUNDO NÚMERO: "))
escolha = 0
while escolha != 5:
    escolha = int(input("""ESCOLHA QUAL OPERAÇÃO DESEJA EFETUAR:
    [1] SOMAR
    [2] MULTIPLICAR
    [3] MAIOR
    [4] NOVOS NÚMEROS
    [5] SAIR
    >>>>>>>>>>>>>>>>>: """))
    if escolha == 1:
        soma = n1 + n2
        print("SOMA:{}".format(soma))
    elif escolha == 2:
        mult = n1 * n2
        print("MULTIPLICAÇÃO:{}".format(mult))
    elif escolha == 3:
        if n1 > n2:
            print("O PRIMEIRO NÚMERO({}) É MAIOR QUE O SEGUNDO NÚMERO({}).".format(n1, n2))
        elif n1 == n2:
            print("OS DOIS NÚMEROS SÃO IGUAIS.")
        else:
            print("O SEGUNDO NÚMERO({}) É MAIOR QUE O PRIMEIRO NÚMERO({}).".format(n2, n1))
    elif escolha == 4:
        print("DIGITE OUTROS DOIS NÚMEROS.")
        n1 = int(input("PRIMEIRO NÚMERO: "))
        n2 = int(input("SEGUNDO NÚMERO: "))
    elif escolha > 5:
        print("ESCOLHA INVÁLIDA!")
print("FIM!")

