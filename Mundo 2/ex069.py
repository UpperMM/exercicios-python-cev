print("Cadastre uma pessoa")

maior_18 = homem = mulher_20 = 0

while True:
    sexo = opcao = " "
    idade = int(input("\nDigite a idade: "))

    while sexo not in "FM":
        sexo = str(input("Digite o sexo [F/M]: ")).strip().upper()[0]

    if idade > 18:
        maior_18 += 1
    if sexo == "M":
        homem += 1
    if sexo == "F" and idade < 20:
        mulher_20 += 1

    while opcao not in "SN":
        opcao = str(input("\nQuer continuar? [S/N] ")).strip().upper()[0]

    if opcao == "N":
        break

print(
    f"Total de pessoas com mais de 18 anos: {maior_18}\nAo todo temos {homem} homens cadastrados\nE temos {mulher_20} mulheres com menos de 20 anos."
)
