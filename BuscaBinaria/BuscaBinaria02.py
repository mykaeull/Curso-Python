vetor = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def binSearch(vetor, left, right, valor):
  if (right >= left):
    indice = int(left + (right - left)/2)
    print(indice)
    if (vetor[indice] == valor):
      return valor
    if (vetor[indice] > valor):
      return binSearch(vetor, left, indice-1, valor)
    return binSearch(vetor, indice+1, right, valor)
  return -1


print(binSearch(vetor, 0, len(vetor)-1, 8))