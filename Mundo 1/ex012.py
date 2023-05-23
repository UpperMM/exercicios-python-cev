# Exercício Python 012: Faça um algoritmo que leia o preço de um produto e
# mostre seu novo preço, com 5% de desconto.

prec = float(input("Qual é o preço do produto? R$ "))

prec_desc = prec - (prec * 5 / 100)

print(
    f"O valor R$ \033[31m{prec}\033[m, com um desconto de 5%, será \033[32mR$ {prec_desc}\033[m."
)
