nascimento = int(input("Ano de nascimento: "))
idade = 2023 - nascimento

print(f"Quem nasceu em {nascimento} tem {idade} ano(s) em 2023.")

if idade == 18:
    print("Você deve se alistar \033[1mIMEDIATAMENTE!\033[m")
elif idade < 18:
    print(
        f"Ainda falta(m) \033[32m{18 - idade} ano(s)\033[m para o alistamento, que será em {nascimento + 18}."
    )
else:
    print(
        f"Você deveria ter se alistado há \033[31m{idade - 18} ano[s]\033[m, em {nascimento + 18}."
    )
