""" Exercício Python 081: Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:
A) Quantos números foram digitados.
B) A lista de valores, ordenada de forma decrescente.
C) Se o valor 5 foi digitado e está ou não na lista. """

lista = []

while True:
    opcao = " "

    lista.append(int(input("Digite um valor: ")))

    while opcao not in "SN":
        opcao = str(input("Quer continuar? [S/N] ")).strip().upper()[0]

    if opcao == "N":
        break

print(f"\nVocê digitou {len(lista)} elementos.")
lista.sort(reverse=True)
print(f"Os valores em ordem decrescente são: {lista}.")

if 5 in lista:
    print("O número 5 faz parte da lista!")
else:
    print("O número 5 não faz parte da lista!")
