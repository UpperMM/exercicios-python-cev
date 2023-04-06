nome = str(input("Digite um nome: ")).strip()

print(
    f"""Seu nome é maiúsculo é {nome.upper()}.
Em minúsculo é {nome.lower()}.
Seu nome tem ao todo {len(nome)- nome.count(' ')} letras!
Seu primeiro nome tem {nome.find(' ')} letras!"""
)
