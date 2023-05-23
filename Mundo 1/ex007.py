# Exercício Python 007: Desenvolva um programa que leia as duas notas de
# um aluno, calcule e mostre a sua média.

numero1 = float(input("Digite um número: "))
numero2 = float(input("Digite outro número: "))

print(f"A média entre {numero1} e {numero2} é \033[32m{(numero1+numero2)/2}\033[m.")
