# Exercício Python 055: Faça um programa que leia o peso de cinco pessoas.
# No final, mostre qual foi o maior e o menor peso lidos.

contador = 0
maior = 0
menor = 0

for pessoas in range(5):
    contador += 1
    peso = float(input(f"Digite o peso da {contador}ª pessoa: "))
    if pessoas == 0:
        maior = peso
        menor = peso
    if peso > maior:
        maior = peso
    else:
        menor = peso

print(f"O maior peso foi \033[31m{maior}Kg.\033[m\nE o menor \033[32m{menor}Kg\033[m.")
