km = float(input("Qual a velocidade do carro em km? "))

multa_preco = (km - 80) * 7

if km >= 81:
    print(f"\033[31mHouve multa!\033[m Total a pagar: R${multa_preco:.2f}\033")
else:
    print("\033[32mNão houve multa!\033[m")
