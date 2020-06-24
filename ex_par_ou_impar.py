import random

v = 0
print("-="*14)
print("VAMOS JOGAR PAR OU ÍMPAR")
print("-="*14)
while True:
    jog = int(input("Digite um valor: "))
    maq = random.randint(1, 10)
    escolha = str(input("PAR OU ÍMPAR[P/I]? ")).upper()
    result = jog + maq
    print("--"*14)
    print(f"Você jogou {jog} e o computador jogou {maq}. O total é {result}")
    print("--"*14)
    if escolha == "P":
        if result % 2 == 0:
            print("Você venceu!")
            v = v + 1
        else:
            print("Você perdeu!")
            break
    elif escolha == "I":
        if result % 2 == 1:
            print("Você venceu!")
            v = v + 1
        else:
            print("Você perdeu!")
            break
    print("Vamos jogar novamente...")
print(f"GAME OVER! VOCÊ VENCEU {v} VEZES.")
