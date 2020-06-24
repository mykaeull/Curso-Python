vetor = [1, 2, 3, 4, 5, 6, 7, 8, 9]

inicial = 0

final = len(vetor) - 1

encontrado = False

busca = 8

while (inicial <= final) and encontrado == False:
  meio = int((inicial + final) / 2)
  print(meio)
  if vetor[meio] == busca:
    n = busca
    encontrado = True
  elif vetor[meio] > busca:
    final = meio - 1
  elif vetor[meio] < busca:
    inicial = meio + 1

print(n)