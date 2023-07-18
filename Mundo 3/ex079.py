# Exercício Python 079: Crie um programa onde o usuário possa digitar
# vários valores numéricos e cadastre-os em uma lista. Caso o número já
# exista lá dentro, ele não será adicionado. No final, serão exibidos
# todos os valores únicos digitados, em ordem crescente.

lista_valores = []

while True:

    opcao = " "

    valor = int(input("Digite um valor: "))

    if valor not in lista_valores:
        lista_valores.append(valor)
        print("Valor adicionado com sucesso!")
    else:
        print("Valor repetido. Não vou adicionar!")

    while opcao not in "SN":
        opcao = str(input("Quer continuar? [S/N] ")).strip().upper()[0]

    if opcao == "N":
        break

lista_valores.sort()

print(f"Você digitou os valores: {lista_valores}")
