# Exercício Python 074: Crie um programa que vai gerar cinco números
# aleatórios e colocar em uma tupla. Depois disso, mostre a listagem de
# números gerados e também indique o menor e o maior valor que estão na
# tupla.

from random import randint

posicao = 0

numeros_sorteados = (
    randint(1, 10),
    randint(1, 10),
    randint(1, 10),
    randint(1, 10),
    randint(1, 10),
)

print("Os números sorteados foram: ", end="")

for repeticao in numeros_sorteados:
    if posicao == 4:
        print(f"{repeticao}.")
        break
    print(f"{repeticao}", end=", ")
    posicao += 1

print(
    f"""
O menor número sorteado foi: {min(numeros_sorteados)}.

o maior número sorteado foi: {max(numeros_sorteados)}. """
)
