# Exercício Python 017: Faça um programa que leia o comprimento do cateto
# oposto e do cateto adjacente de um triângulo retângulo. Calcule e mostre
# o comprimento da hipotenusa.

from math import hypot

oposto = float(input("Digite o comprimento do cateto oposto: "))
adjacente = float(input("Digite o comprimento do cateto adjacente: "))

hipotenusa = hypot(oposto, adjacente)

print(f"A hipotenusa vai medir \033[32m{hipotenusa:.2f}\033[m.")
