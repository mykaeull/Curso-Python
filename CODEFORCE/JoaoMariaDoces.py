lista = []

t = int(input('tamanho: '))

c = 0

d = 0

jogada = 0

partida = True

maria = 0

maria2 = 0

joao = 0

joao2 = 0

while c < t:
    n = int(input('numero: '))
    lista.append(n)
    c += 1

while len(lista) != 0:
    if jogada == 0:
        maria = lista[d]
        jogada += 1
        lista.remove(lista[d])
    else:
        if partida == True:
            while (joao < maria or joao == maria) and len(lista) != 0:
                e = (len(lista) - 1)
                joao = joao + lista[e]
                lista.remove(lista[e])
            joao1 = joao
            joao2 = joao2 + joao1
            joao = 0
            partida = False
        elif partida == False:
            while (maria < joao or maria == joao) and len(lista) != 0:
                maria = maria + lista[d]
                lista.remove(lista[d])
            maria1 = maria
            maria2 = maria2 + maria1
            maria = 0
            partida = True

print("")
print("Maria: ", maria2)
print("Joao: ", joao2)