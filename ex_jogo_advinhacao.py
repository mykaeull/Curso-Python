import time
import random

print("-=-=-=-=-= JOGO DA ADIVINHAÇÃO =-=-=-=-=-")
time.sleep(1)
n_jogador = int(input("Digite um número entre 1 e 5: "))
n_maquina = random.randint(1, 5)
n_tentativas = 1
while n_jogador != n_maquina:
    print("Você perdeu!")
    print("Tente novamente.")
    n_jogador = int(input("Digite um número entre 1 e 5: "))
    n_tentativas = n_tentativas + 1
if n_tentativas == 1:
    print("Parabéns!")
    print("Você venceu na {}ª tentativa".format(n_tentativas))
else:
    print("Parabéns!")
    print("Você venceu após {} tentativas".format(n_tentativas))
print("FIM!")
