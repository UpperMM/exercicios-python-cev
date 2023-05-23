# Exercício Python 052: Faça um programa que leia um número inteiro e diga
# se ele é ou não um número primo.

numero = int(input("Digite um número: "))
num_divisores = 0

for divisor in range(1, numero + 1):
    if numero % divisor == 0:
        print("\033[32m", end="")
        num_divisores += 1
    else:
        print("\033[31m", end="")
    print(f"{divisor} ", end="")

if num_divisores == 2:
    classificacao = "\033[32mÉ PRIMO!"
else:
    classificacao = "\033[31mNÃO É PRIMO!"

print(
    f"\n\033[mO número {numero} foi divisível {num_divisores} vezes. O número indicado {classificacao}"
)
