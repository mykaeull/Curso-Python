print("="*20)
a = float(input("Digite o valor da A: "))
print("="*20)
b = float(input("Digite o valor de B: "))
print("="*20)

import numpy as np
import matplotlib.pyplot as plt

eixo_x = []
eixo_y = []

for x in np.arange(0, 5, 1/10):
    y = (a*x) + b
    eixo_x.append(x)
    eixo_y.append(y)

plt.plot(eixo_x, eixo_y)
plt.show()





