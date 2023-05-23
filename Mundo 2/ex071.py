# Exercício Python 071: Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues.
# OBS: considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.

print("Banco CEV")

while True:
    valor = int(input("Qual valor você quer sacar? R$ "))
    if valor >= 50:
        nota_50 = valor // 50
        resto = valor % 50
        print(f"total de {nota_50} cédulas de R$ 50")
    if resto >= 20:
        nota_20 = resto // 20
        resto %= 20
        print(f"total de {nota_20} cédulas de R$ 20")
    if resto >= 10:
        nota_10 = resto // 10
        resto %= 10
        print(f"total de {nota_10} cédulas de R$ 10")
    if resto >= 1:
        nota_1 = resto
        print(f"total de {nota_1} cédulas de R$ 1")
    break
