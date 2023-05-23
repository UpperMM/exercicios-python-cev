# Exercício Python 057: Faça um programa que leia o sexo de uma pessoa,
# mas só aceite os valores 'M' ou 'F'. Caso esteja errado, peça a
# digitação novamente até ter um valor correto.

sexo = str(input("Informe seu sexo [F/M]: ")).strip().upper()[0]

while sexo not in "FM":
    sexo = (
        str(input("\033[31mDados inválidos.\033[m Digite corretamente [F/M]: "))
        .strip()
        .upper()[0]
    )

print(f"\033[32mSexo {sexo} registrado com sucesso!")
