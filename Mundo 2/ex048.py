# Exercício Python 048: Faça um programa que calcule a soma entre todos os
# números que são múltiplos de três e que se encontram no intervalo de 1
# até 500.

soma = 0
contagem = 0
for sequencia in range(1, 501, 2):
    if sequencia % 3 == 0:
        contagem += 1
        soma += sequencia

print(f"A soma de todos os {contagem} valores solicitados é \033[32m{soma}\033[m!")
