# Exercício Python 065: Crie um programa que leia vários números inteiros
# pelo teclado. No final da execução, mostre a média entre todos os
# valores e qual foi o maior e o menor valores lidos. O programa deve
# perguntar ao usuário se ele quer ou não continuar a digitar valores.

soma = maior = menor = contador = 0

escolha = " "

while escolha != "N":
    escolha = " "
    numero = int(input("Digite um número: "))
    if numero > maior:
        maior = numero
    if numero < menor or contador == 0:
        menor = numero
    contador += 1
    soma += numero

    while escolha not in "SN":
        escolha = str(input("Quer continuar? [S/N] ")).strip().upper()[0]

print(
    f"Você digitou {contador} números e a média foi {soma/contador}\nO maior valor foi {maior} e o menor foi {menor}."
)
