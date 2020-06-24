while True:
    n = int(input("Quer ver a tabuada de qual valor? "))
    cont = 1
    if n < 0:
        break
    while cont <= 10:
        result = n * cont
        print(f"{n} x {cont} = {result}")
        cont = cont + 1
print("FIM!")