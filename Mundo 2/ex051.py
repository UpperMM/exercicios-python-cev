# Exercício Python 051: Desenvolva um programa que leia o primeiro termo e
# a razão de uma PA. No final, mostre os 10 primeiros termos dessa
# progressão.

termo = int(input("10 TERMOS DE UMA PA\nPrimeiro termo: "))
razao = int(input("Razão: "))

for pa in range(termo, termo + razao * 10, razao):
    print(f"{pa} ", end="→ ")

print("Acabou!")
