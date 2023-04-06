from random import randint

chute = int(input("Tente acertar o número entre 0 e 5: "))

sorteado = randint(0, 5)

if chute == sorteado:
    print(f"Acertou! O número era {sorteado}.")
else:
    print(f"Errou! O número era {sorteado}.")
