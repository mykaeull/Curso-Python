print("---------- SISTEMA LOCADORA ----------")
print("")
ficha = [{'filme': 'STAR WARS: A AMEAÇA FANTASMA'},
         {'filme': 'PUP FICTION'},
         {'filme': 'PARASITA'}]
while True:
    print("""OPÇÕES
[1] MOSTRAR LISTA DE FILMES
[2] ADICIONAR FILME À LISTA
[3] REMOVER FILME DA LISTA
[4] PESQUISAR FILME PELO NOME
[5] ATUALIZAR LISTA DE FILMES  
[0] SAIR""")
    escolha = int(input("ESCOLHA: "))
    if escolha == 1:
        print("FILMES:")
        for f in ficha:
            for k, v in f.items():
                print(f"{v}")
            print("--" * 20)
    if escolha == 2:
        filme = str(input("NOME DO FILME: "))
        add_filme = {'filme': filme}
        ficha.append(add_filme)
    if escolha == 3:
        f_rem = str(input("NOME DO FILME QUE DESEJA REMOVER: ")).upper()
        for f in ficha:
            for k, v in f.items():
                if f_rem == v:
                    ficha.remove(f)
    if escolha == 4:
        filme = str(input("NOME DO FILME: "))
        for f in ficha:
            for k, v in f.items():
                if filme == v:
                    print(v)
                else:
                    print("ERRO")
    if escolha == 5:
        print("FILMES:")
        for f in ficha:
            for k, v in f.items():
                print(f"{v}")
            print("--" * 20)
    if escolha == 0:
        break
print("FIM DO PROGRAMA!")





