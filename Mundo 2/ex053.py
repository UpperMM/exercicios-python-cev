# Exercício Python 053: Crie um programa que leia uma frase qualquer e
# diga se ela é um palíndromo, desconsiderando os espaços.

frase = str(input(("Digite uma frase: "))).strip().upper()
palavras = frase.split()
inverso = "".join(palavras)[::-1]

if inverso == frase:
    print(f"{inverso}/{frase} \033[32mé um palíndromo\033[32m.")

else:
    print(f"{inverso}/{frase} \033[31mnão é um palíndromo\033[m.")
