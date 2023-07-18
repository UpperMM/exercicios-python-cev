# Exercício Python 078: Faça um programa que leia 5 valores numéricos e
# guarde-os em uma lista. No final, mostre qual foi o maior e o menor
# valor digitado e as suas respectivas posições na lista.

lista_valores = []

for valores in range(5):
    lista_valores.append(int(input(f"digite o valor para a posição {valores}: ")))

print(f"\nVocê digitou os valores: {lista_valores}.")

print(f"O maior valor digitado foi {max(lista_valores)} nas posições", end=" ")

for pos, maior in enumerate((lista_valores)):
    if maior == max(lista_valores):
        print(pos, end="... ")

print(f"\nO menor valor digitado foi {min(lista_valores)} nas posições", end=" ")

for pos, menor in enumerate((lista_valores)):
    if menor == min(lista_valores):
        print(pos, end="... ")
