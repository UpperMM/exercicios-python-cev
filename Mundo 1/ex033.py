# Exercício Python 033: Faça um programa que leia três números e mostre
# qual é o maior e qual é o menor.

numero1 = int(input("Digite um número: "))
numero2 = int(input("Digite mais um número: "))
numero3 = int(input("E mais um: "))

menor = numero1
if numero2 < numero1 and numero2 < numero3:
    menor = numero2
if numero3 < numero1 and numero3 < numero2:
    menor = numero3

maior = numero1
if numero2 > numero1 and numero2 > numero3:
    maior = numero2
if numero3 > numero1 and numero3 > numero2:
    maior = numero3

print(f"O menor é \033[31m{menor}\033[m e o maior é \033[32m{maior}\033[m.")
