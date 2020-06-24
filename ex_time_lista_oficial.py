grupo_a = []
grupo_b = []
cont_a = 0
pos_a = 1
cont_b = 0
pos_b = 1
print("-="*12)
print("      BRASILEIRÃO")
print("-="*12)
print("")
print("~~"*21)
print("ADICIONE OS TIMES DO GRUPO A")
print("~~"*21)

while cont_a < 5:
    times_a = str(input(f"Insira o {pos_a}ª time do grupo A: "))
    print("--"*21)
    if times_a in grupo_a:
        print("Esse time já está na lista...")
        times_a = str(input(f"Insira o {pos_a}ª time do grupo A: "))
        grupo_a.append(times_a)
        print("--"*21)
    else:
        grupo_a.append(times_a)
    cont_a = cont_a + 1
    pos_a = pos_a + 1
grupo_a.sort()
print("GRUPO A ADICIONADO COM SUCESSO!")
print("~~"*21)
print("ADICIONE OS TIMES DO GRUPO B")
print("~~"*21)

while cont_b < 5:
    times_b = str(input(f"Insira o {pos_b}ª time do grupo B: "))
    print("--"*21)
    if times_b in grupo_b:
        print("Esse time já está na lista...")
        times_b = str(input(f"Insira o {pos_b}ª time do grupo B: "))
        grupo_b.append(times_b)
        print("--"*21)
    else:
        grupo_b.append(times_b)
    cont_b = cont_b + 1
    pos_b = pos_b + 1
grupo_b.sort()
print("GRUPO B ADICIONADO COM SUCESSO!")
print("~~"*21)

print(f"TIMES DO GRUPO A: {grupo_a}")
print(f"TIMES DO GRUPO B: {grupo_b}")
