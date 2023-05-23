# Exercício Python 025: Crie um programa que leia o nome de uma pessoa e
# diga se ela tem "SILVA" no nome.

nome = str(input("Digite um nome: ")).strip()

print(f"O nome {nome} tem 'Silva'? {'silva' in nome.lower().split()}")
