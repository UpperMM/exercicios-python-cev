# Exercício Python 028: Escreva um programa que faça o computador "pensar"
# em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir
# qual foi o número escolhido pelo computador. O programa deverá escrever
# na tela se o usuário venceu ou perdeu.

from random import randint

chute = int(input("Tente acertar o número entre 0 e 5: "))

sorteado = randint(0, 5)

if chute == sorteado:
    print(f"\033[32mAcertou!\033[m O número era {sorteado}.")
else:
    print(f"\033[31mErrou!\033[m O número era {sorteado}.")
