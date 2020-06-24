import random
num = int(input("Escolha um número aleatório entre 1 e 10: "))
result = random.randint(1, 10)
print(result)
i = 2
while i > 0:
    if num == result:
        print("Parabéns, você venceu!")
        i = i - 2
    else:
        if i > 0:
            print("Você errou!")
            print("Você tem mais", i, "chance")
            num = int(input("Tente novamente:"))
            i = i - 1
        else:
            print("Você perdeu!")











