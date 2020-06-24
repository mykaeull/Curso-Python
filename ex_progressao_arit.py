termo1 = int(input("Primeiro termo da PA: "))
razao = int(input("Razão da PA: "))
n_termos = int(input("PA de quantos termos? "))

for c in range(1, n_termos+1):
    termos = termo1 + (c - 1) * razao
    print(termos)
print("FIM!")

