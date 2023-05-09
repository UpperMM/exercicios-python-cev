sexo = str(input("Informe seu sexo [F/M]: ")).strip().upper()[0]

while sexo not in "FM":
    sexo = (
        str(input("\033[31mDados inválidos.\033[m Digite corretamente [F/M]: "))
        .strip()
        .upper()[0]
    )

print(f"\033[32mSexo {sexo} registrado com sucesso!")
