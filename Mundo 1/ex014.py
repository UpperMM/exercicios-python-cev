# Exercício Python 014: Escreva um programa que converta uma temperatura
# digitando em graus Celsius e converta para graus Fahrenheit.

celsius = float(input("Informe a temperatura em ºC: "))

print(f"A temperatura de {celsius}ºC corresponde a \033[32m{celsius*1.8+32}F\033[m!")
