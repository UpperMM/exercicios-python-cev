"""Exercício Python 084: Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
A) Quantas pessoas foram cadastradas.
B) Uma listagem com as pessoas mais pesadas.
C) Uma listagem com as pessoas mais leves."""

pessoas = list()
dados = list()
nome_maior = list()
nome_menor = list()

while True:

    opcao = " "

    dados.append(str(input("Nome da pessoa: ")))
    dados.append(float(input("Peso da pessoa: ")))
    pessoas.append(dados[:])
    dados.clear()
    while opcao not in "SN":
        opcao = str(input("Quer cadastrar mais alguém? [S/N] ")).strip().upper()[0]

    if opcao == "N":
        break

maior = menor = pessoas[0][1]

for pessoa in pessoas:
    if pessoa[1] >= maior:
        nome_maior.append(pessoa[0])
        maior = pessoa[1]
    if pessoa[1] <= menor:
        nome_menor.append(pessoa[0])
        menor = pessoa[1]

print(f"Foram cadastradas {len(pessoas)} pessoas.")
print(f"O maior peso foi {maior}kg, de {nome_maior}.")
print(f"O menor peso foi {menor}kg, de {nome_menor}.")
