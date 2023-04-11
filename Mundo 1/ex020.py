from random import shuffle

nome1 = str(input("Digite o 1º nome: "))
nome2 = str(input("Digite o 2º nome: "))
nome3 = str(input("Digite o 3º nome: "))
nome4 = str(input("Digite o 4º nome: "))

pessoas = [nome1, nome2, nome3, nome4]
shuffle(pessoas)

print(f"A ordem é: \033[32m{pessoas}\033[m.")

