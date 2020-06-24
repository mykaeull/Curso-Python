cont_idade = 0
cont_idade_fem = 0
cont_sex_masc = 0
while True:
    print("--"*14)
    print("CADASTRE UMA PESSOA")
    print("--"*14)
    idade = int(input("IDADE: "))
    sexo = str(input("SEXO[M/F]: ")).upper()
    while sexo not in "MF":
        print("DADO INVÁLIDO...")
        sexo = str(input("SEXO[M/F]: ")).upper()
    escolha = str(input("Quer continuar? [S/N] ")).upper()
    while escolha not in "SN":
        print("DANO INVÁLIDO...")
        escolha = str(input("Quer continuar? [S/N] ")).upper()
    if idade > 18:
        cont_idade = cont_idade + 1
    if sexo == "M":
        cont_sex_masc = cont_sex_masc + 1
    if sexo == "F":
        if idade < 20:
            cont_idade_fem = cont_idade_fem + 1
    if escolha == "N":
        print("======= CADASTRAMENTO ENCERRADO =======")
        break
print(f"Total de pessoas com mais de 18 anos: {cont_idade}")
print(f"Ao todo temos {cont_sex_masc} homens cadastrados.")
print(f"E temos {cont_idade_fem} mulheres com menos de 20 anos.")
