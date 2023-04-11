nome = str(input("Digite um nome: ")).strip()
nome_separado = nome.split()

print(
    f"Seu nome é maiúsculo é {nome.upper()}.\nEm minúsculo é {nome.lower()}.\nSeu nome tem ao todo {len(nome)-nome.count(' ')} letras!\nSeu primeiro nome tem {len(nome_separado[0])} letras!"
)
