""" Exercício Python 059: Crie um programa que leia dois valores e mostre um menu na tela:
[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa
Seu programa deverá realizar a operação solicitada em cada caso. """

from time import sleep

operacao = 0

valor1 = int(input("1º valor: "))
valor2 = int(input("2º valor: "))

opcoes = """
Escolha uma opcão:

    [1] soma
    [2] subtração
    [3] divisão
    [4] multiplicação
    [5] maior número
    [6] novos números
    [7] sair do programa"""

while operacao != "sair":
    print(opcoes)

    escolha = input("\n>>>> Qual é a sua escolha? ")

    if escolha == "1":
        operacao = "soma"
        resultado = valor1 + valor2
    elif escolha == "2":
        operacao = "subtração"
        resultado = valor1 - valor2
    elif escolha == "3":
        operacao = "divisão"
        resultado = valor1 / valor2
    elif escolha == "4":
        operacao = "multiplicação"
        resultado = valor1 * valor2
    elif escolha == "5":
        operacao = "maior número"
        if valor1 > valor2:
            print(f"\n{valor1} é maior que {valor2}!")
        elif valor1 < valor2:
            print(f"\n{valor2} é maior que {valor1}!")
        elif valor1 == valor2:
            print("\nAmbos os números são iguais!")
    elif escolha == "6":
        print("\nInforme os novos valores: ")
        valor1 = int(input("1º valor: "))
        valor2 = int(input("2º valor: "))
    elif escolha == "7":
        print("\nFinalizando...")
        sleep(1.5)
        operacao = "sair"
    else:
        print("\nOpção inválida!")

    if escolha in ["1", "2", "3", "4"]:
        print(f"\nA {operacao} entre {valor1} e {valor2} é {resultado}!")

    print("\n", 11 * "=-=")

    sleep(5)
