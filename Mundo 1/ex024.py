# Exercício Python 024: Crie um programa que leia o nome de uma cidade
# diga se ela começa ou não com o nome "SANTO".

cidade = str(input("Digite o nome de uma cidade: ")).strip()

print(f"'{cidade}' começa com 'Santo'? {cidade.lower().split()[0] == 'santo'}")
