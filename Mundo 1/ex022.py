""" Exercício Python 022: Crie um programa que leia o nome completo de uma pessoa e mostre:
- O nome com todas as letras maiúsculas e minúsculas.
- Quantas letras ao todo (sem considerar espaços).
- Quantas letras tem o primeiro nome. """

nome = str(input("Digite um nome: ")).strip()
nome_separado = nome.split()

print(
    f"Seu nome é maiúsculo é {nome.upper()}.\nEm minúsculo é {nome.lower()}.\nSeu nome tem ao todo {len(nome)-nome.count(' ')} letras!\nSeu primeiro nome tem {len(nome_separado[0])} letras!"
)
