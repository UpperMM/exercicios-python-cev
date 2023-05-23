# Exercício Python 020: O mesmo professor do desafio 019 quer sortear a
# ordem de apresentação de trabalhos dos alunos. Faça um programa que leia
# o nome dos quatro alunos e mostre a ordem sorteada.

from random import shuffle

nome1 = str(input("Digite o 1º nome: "))
nome2 = str(input("Digite o 2º nome: "))
nome3 = str(input("Digite o 3º nome: "))
nome4 = str(input("Digite o 4º nome: "))

pessoas = [nome1, nome2, nome3, nome4]
shuffle(pessoas)

print(f"A ordem é: \033[32m{pessoas}\033[m.")
