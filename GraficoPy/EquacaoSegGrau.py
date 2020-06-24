print("="*20)
a = float(input("Digite o valor de A: "))
print("="*20)
b = float(input("Digite o valor de B: "))
print("="*20)
c = float(input("Digite o valor de C: "))
print("="*20)

delta = (b**2) - (4*a*c)

if delta < 0:
    print('A equação não possui raiz real.')

x1 = ((-(b)) + (delta**(1/2))) / (a*2)
x2 = ((-(b)) - (delta**(1/2))) / (a*2)
xV = (-(b)) / (2*a)
yV = (-(delta)) / (4*a)

print("Delta=", delta)
print("="*20)
print("X1=", x1)
print("="*20)
print("X2=", x2)
print("="*20)
print("Xv=", xV)
print("="*20)
print("Yv=", yV)
print("="*20)

import matplotlib.pyplot as plt
import numpy as np

eixo_x = []
eixo_y = []

#Consertar a variação

for x in np.arange(abs(x1), abs(x2), 1/10):
    xis = -x
    y = (a*(xis**2)) + (b*xis) + c
    eixo_x.append(xis)
    eixo_y.append(y)

plt.plot(eixo_x, eixo_y)
plt.show()

