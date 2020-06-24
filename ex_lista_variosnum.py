lista = []
while True:
    num = int(input("Digite um número: "))
    lista.append(num)
    escolha = str(input("Quer continuar? [S/N]")).upper()
    if escolha not in "SN":
        print("DADO INVÁLIDO...")
        escolha = str(input("Quer continuar? [S/N]")).upper()
    if escolha == "N":
        break
print(f"Foram digitados {len(lista)} números.")
lista.sort(reverse=True)
print(f"Lista na ordem decrescente: {lista}")
if 5 in lista:
    print("O valor 5 está contido dentro da lista.")
else:
    print("Não existe valor 5 dentro da lista.")