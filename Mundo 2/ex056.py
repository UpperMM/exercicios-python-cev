contador = 0
idade_total = 0
maior_idade = 0
mulheres_abaixo_20 = 0
nome_homem_velho = ""

for pessoa in range(4):
    contador += 1
    # Exercício Python 056: Desenvolva um programa que leia o nome, idade e
    # sexo de 4 pessoas. No final do programa, mostre: a média de idade do
    # grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de
    # 20 anos.

    nome = str(input(f"---- {contador}ª pessoa ----\nNome: ")).strip()
    idade = int(input("Idade: "))
    sexo = str(input("Sexo(F/M): ")).upper().strip()

    idade_total += idade

    if idade > maior_idade and sexo == "M":
        maior_idade = idade
        nome_homem_velho = nome

    if idade < 20 and sexo == "F":
        mulheres_abaixo_20 += 1

print(
    f"A média de idades é \033[32m{idade_total/4}\033[m.\nO homem mais velho tem \033[32m{maior_idade} anos e se chama {nome_homem_velho}\033[m.\nAo todo, são \033[32m{mulheres_abaixo_20} mulheres\033[jm com menos de 20 anos."
)
