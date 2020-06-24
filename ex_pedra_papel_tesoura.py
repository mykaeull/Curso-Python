import random
import time

escolha = int(input("""Suas opções:
[0] PEDRA
[1] PAPEL
[2] TESOURA
Qual é a sua jogada? """))
result = random.randint(0, 2)
print("JO")
time.sleep(1)
print("KEN")
time.sleep(1)
print("PÔ")
time.sleep(1)
if escolha == 0 and result == 1:
    print("-="*12)
    print("Jogador jogou PEDRA")
    print("Computador jogou PAPEL")
    print("-="*12)
    print("COMPUTADOR VENCEU!")
elif escolha == 1 and result == 0:
    print("-=" * 12)
    print("Jogador jogou PAPEL")
    print("Computador jogou PEDRA")
    print("-=" * 12)
    print("JOGADOR VENCEU!")
elif escolha == 2 and result == 0:
    print("-=" * 12)
    print("Jogador jogou TESOURA")
    print("Computador jogou PEDRA")
    print("-=" * 12)
    print("COMPUTADOR VENCEU!")
elif escolha == 0 and result == 2:
    print("-=" * 12)
    print("Jogador jogou PEDRA")
    print("Computador jogou TESOURA")
    print("-=" * 12)
    print("JOGADOR VENCEU!")
elif escolha == 1 and result == 2:
    print("-=" * 12)
    print("Jogador jogou PAPEL")
    print("Computador jogou TESOURA")
    print("-=" * 12)
    print("COMPUTADOR VENCEU!")
elif escolha == 2 and result == 1:
    print("-=" * 12)
    print("Jogador jogou TESOURA")
    print("Computador jogou PAPEL")
    print("-=" * 12)
    print("JOGADOR VENCEU!")
elif escolha == 0 and result == 0:
    print("-=" * 12)
    print("Jogador jogou PEDRA")
    print("Computador jogou PEDRA")
    print("-=" * 12)
    print("EMPATE!")
elif escolha == 1 and result == 1:
    print("-=" * 12)
    print("Jogador jogou PAPEL")
    print("Computador jogou PAPEL")
    print("-=" * 12)
    print("EMPATE!")
elif escolha == 2 and result == 2:
    print("-=" * 12)
    print("Jogador jogou TESOURA")
    print("Computador jogou TESOURA")
    print("-=" * 12)
    print("EMPATE!")
else:
    print("JOGADA INVÁLIDA!")