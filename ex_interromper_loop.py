cont = 0
soma = 0
while True:
    n = int(input("Digite um número: "))
    if n == 999:
        break
    cont = cont + 1
    soma = soma + n
print(f"Você digitou {cont} números")
print(f"A soma dos números digitados é igual a {soma}")