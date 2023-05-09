from random import randint

contador_tentativa = 0
sorteado = randint(0, 10)

chute = int(input("Tente acertar o número entre 0 e 10: "))

while chute != sorteado:
    contador_tentativa += 1
    chute = int(input(f"\033[31mErrou!\033[m Tente novamente: "))


print(
    f"\033[32mAcertou!\033[m O número era {sorteado} e foram necessárias {contador_tentativa} tentativas para acertá-lo!."
)
