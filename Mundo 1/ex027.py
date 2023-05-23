# Exercício Python 027: Faça um programa que leia o nome completo de uma
# pessoa, mostrando em seguida o primeiro e o último nome separadamente.

nome = str(input("Digite um nome: ")).split()

print(f"Primeiro nome: \033[32m{nome[0]}\033[m\nÚltimo nome: \033[31m{nome[-1]}\033[m")
