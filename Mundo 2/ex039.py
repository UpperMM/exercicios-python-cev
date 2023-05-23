# Exercício Python 039: Faça um programa que leia o ano de nascimento de
# um jovem e informe, de acordo com a sua idade, se ele ainda vai se
# alistar ao serviço militar, se é a hora exata de se alistar ou se já
# passou do tempo do alistamento. Seu programa também deverá mostrar o
# tempo que falta ou que passou do prazo.

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
