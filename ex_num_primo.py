num = int(input("Número: "))
if num%1 == 0 and num%num == 0 and num%2 == 1:
    print("NÚMERO PRIMO!")
else:
    print("NÚMERO NÃO PRIMO!")
print("FIM!")