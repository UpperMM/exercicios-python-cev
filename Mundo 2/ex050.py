soma = 0
contagem = 0
for repeticao in range(1, 7):
    valor = int(input(f"Digite o {repeticao}º valor: "))
    if valor % 2 == 0:
        contagem += 1
        soma += valor

print(f"Você informou {contagem} números PARES e a soma foi \033[32m{soma}\033[m!")
