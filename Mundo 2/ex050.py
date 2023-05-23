# Exercício Python 050: Desenvolva um programa que leia seis números
# inteiros e mostre a soma apenas daqueles que forem pares. Se o valor
# digitado for ímpar, desconsidere-o

soma = 0
contagem = 0
for repeticao in range(1, 7):
    valor = int(input(f"Digite o {repeticao}º valor: "))
    if valor % 2 == 0:
        contagem += 1
        soma += valor

print(f"Você informou {contagem} números PARES e a soma foi \033[32m{soma}\033[m!")
