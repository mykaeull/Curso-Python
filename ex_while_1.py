sexo = str(input("Sexo[M/F]: ")).upper()
while sexo not in "MF":
    print("DÍGITO INVÁLIDO")
    sexo = str(input("Digite novamente o sexo[M/F]: ")).upper()
print("FIM!")