# Exercício Python 023: Faça um programa que leia um número de 0 a 9999 e
# mostre na tela cada um dos dígitos separados.

numero = int(input("Digite um número com até 4 casas decimais: "))
numerostr = str(numero + 10000).strip()[:5]

print(
    f"O número digitado foi {numero}!\n\033[32mUnidade: {numerostr[4]}\nDezena: {numerostr[3]}\nCentena: {numerostr[2]}\nMilhar: {numerostr[1]}\033[m"
)
