# Exercício Python 047: Crie um programa que mostre na tela todos os
# números pares que estão no intervalo entre 1 e 50.

for sequencia in range(2, 51, 2):
    print(f"\033[1;32m{sequencia}\033[m,", end=" ")

print("acabou!")
