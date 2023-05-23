# Exercício Python 029: Escreva um programa que leia a velocidade de um
# carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele
# foi multado. A multa vai custar R$7,00 por cada Km acima do limite.

km = float(input("Qual a velocidade do carro em km? "))

multa_preco = (km - 80) * 7

if km >= 81:
    print(f"\033[31mHouve multa!\033[m Total a pagar: R${multa_preco:.2f}\033")
else:
    print("\033[32mNão houve multa!\033[m")
