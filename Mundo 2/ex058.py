# Exercício Python 058: Melhore o jogo do DESAFIO 028 onde o computador
# vai "pensar" em um número entre 0 e 10. Só que agora o jogador vai
# tentar adivinhar até acertar, mostrando no final quantos palpites foram
# necessários para vencer.

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
