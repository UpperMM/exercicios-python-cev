# Exercício Python 009: Faça um programa que leia um número Inteiro
# qualquer e mostre na tela a sua tabuada.

num = int(input("Digite o número que você deseja ver a tabuada: "))

print(
    f"{'-'*11}\n{num} x {1:2} = {num*1}\n{num} x {2:2} = {num*2}\n{num} x {3:2} = {num*3}\n{num} x {4:2} = {num*4}\n{num} x {5:2} = {num*5}\n{num} x {6:2} = {num*6}\n{num} x {7:2} = {num*7}\n{num} x {8:2} = {num*8}\n{num} x {9:2} = {num*9}\n{num} x {10:2} = {num*10}\n{'-'*11}"
)
