km = float(input("Qual a velocidade do carro em km? "))

multa_preco = (km - 80) * 7

if km >= 81:
    print(f"Houve multa! Total a pagar: R${multa_preco:.2f} ")
else:
    print("Não houve multa!")
