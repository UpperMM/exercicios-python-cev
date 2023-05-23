# Exercício Python 010: Crie um programa que leia quanto dinheiro uma
# pessoa tem na carteira e mostre quantos dólares ela pode comprar.

real = float(input("Quanto você tem na sua carteira? R$ "))

print(f"Com R$ {real} você poderia comprar \033[32m$ {real/5.01:.2f}\033[m.")
