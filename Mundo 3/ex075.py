""" Exercício Python 075: Desenvolva um programa que leia quatro valores
pelo teclado e guarde-os em uma tupla. No final, mostre:

A) Quantas vezes apareceu o valor 9.
B) Em que posição foi digitado o primeiro valor 3.
C) Quais foram os números pares. """

numero = (
    int(input("Digite um número: ")),
    int(input("Digite mais um número: ")),
    int(input("Digite o penúltimo número: ")),
    int(input("Digite o último número: ")),
)

print(f"Você digitou os valores: {numero}.")

if 9 in numero:
    print(f"O valor 9 apareceu {numero.count(9)} vez(es).")
else:

    print("O valor 9 não aparece.")
if 3 in numero:
    print(f"O valor 3 apareceu na {numero.index(3) + 1}ª posição.")
else:
    print("O valor 3 não aparece.")

print("Os valores pares digitados foram: ", end="")

for valor in numero:
    if valor % 2 == 0:
        print(valor, end=" ")
