data_nasc = int(input("Ano de nascimento:"))
idade = 2020 - data_nasc
if idade < 18:
    tempo_alist = 18 - idade
    print("Quem nasceu em {} tem {} anos em 2020.".format(data_nasc, idade))
    print("Ainda faltam {} anos para o seu alistamento militar.".format(tempo_alist))
elif idade == 18:
    print("Quem nasceu em {} tem {} anos em 2020.".format(data_nasc, idade))
    print("Você tem que se alistar IMEDIATAMENTE!")
else:
    tempo_alist = idade - 18
    print("Quem nasceu em {} tem {} anos em 2020.".format(data_nasc, idade))
    print("Você já deveria ter se alistado há {} anos.".format(tempo_alist))
