# Exercício Python 072: Crie um programa que tenha uma dupla totalmente
# preenchida com uma contagem por extenso, de zero até vinte. Seu programa
# deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por
# extenso.

numeros_extenso = (
    "zero",
    "um",
    "dois",
    "três",
    "quatro",
    "cinco",
    "seis",
    "sete",
    "oito",
    "nove",
    "dez",
    "onze",
    "doze",
    "treze",
    "catorze",
    "quinze",
    "dezesseis",
    "dezessete",
    "dezoito",
    "dezenove",
    "vinte",
)

numero = 0

while True:

    opcao = " "

    while True:
        numero = int(input("Digite um número entre 0 e 20: "))
        if 0 <= numero <= 20:
            break

        print("Tente novamente.", end=" ")

    print(f"Você digitou o número {numeros_extenso[numero]}!")

    while opcao not in "SN":
        opcao = str(
            input("Deseja digitar outro número? [S/N] ")).strip().upper()[0]

    if opcao == "N":
        break
