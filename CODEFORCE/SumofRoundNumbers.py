vezes = int(input('vezes: '))

listaFinal = []

listaTamanho = []

for i in range(0, vezes):

  n = int(input('numero: '))

  nString = str(n)

  nStringLista = list(nString)

  b = 10**(len(nString) - 1)

  c = 0

  newLista = []

  while c < len(nString):
    a = int(nStringLista[c])
    d = int(a * b)
    newLista.append(d)
    b = b / 10
    c += 1
  while 0 in newLista:
    newLista.remove(0)
  listaTamanho.append(len(newLista))
  listaFinal.append(newLista)

print('')

for c in range(0, len(listaFinal)):
  print(listaTamanho[c])
  print(listaFinal[c])