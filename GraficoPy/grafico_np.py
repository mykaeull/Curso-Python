import numpy as np
import matplotlib.pyplot as plt
import csv

pais = []
quantidade = []
preco = []
ano = 2016

def obterDados():
    with open('C:/Users/mykaeull/Desktop/ImpSuco.csv') as csvfile:
        readCSV = csv.reader(csvfile, delimited = ';')
        for row in readCSV:
            if (float(row[(ano - 1969)*2]) > 0):
                pais.append(row[1][0:3])
                quantidade.append(float(row[(ano - 1969)*2]))
                preco.append(row[(ano - 1969)*2 + 1])

    print(pais)
    print(quantidade)
    print(preco)

if __name__ == '__main__':
    obterDados()