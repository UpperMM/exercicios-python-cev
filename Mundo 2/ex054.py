contador = 0
maior = 0
menor = 0

for idade in range(7):
    contador += 1
    ano = int(input(f"Digite o {contador}º ano: "))
    if 2023 - ano >= 18:
        maior += 1
    else:
        menor += 1

print(
    f"Ao todo tivemos \033[32m{maior}\033[m pessoas maiores de idade.\nE também \033[31m{menor}\033[m menores de idade."
)
