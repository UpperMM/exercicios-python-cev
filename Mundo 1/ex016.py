# Exercício Python 016: Crie um programa que leia um número Real qualquer
# pelo teclado e mostre na tela a sua porção Inteira.

from math import floor

num = float(input("Digite um valor: "))

print(f"O valor digitado foi {num} e sua porção inteira é \033[32m{floor(num)}\033[m.")
