from random import randint

chute = int(input("Tente acertar o número entre 0 e 5: "))

sorteado = randint(0, 5)

if chute == sorteado:
    print(f"\033[32mAcertou!\033[m O número era {sorteado}.")
else:
    print(f"\033[31mErrou!\033[m O número era {sorteado}.")
