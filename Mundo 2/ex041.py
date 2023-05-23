""" Exercício Python 041: A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
- Até 9 anos: MIRIM
- Até 14 anos: INFANTIL
- Até 19 anos: JÚNIOR
- Até 25 anos: SÊNIOR
- Acima de 25 anos: MASTER """

nascimento = int(input("Ano de nascimento: "))
idade = 2023 - nascimento

if idade <= 9:
    categoria = "\033[32mMIRIM\033[m"
elif idade <= 14:
    categoria = "\033[32mINFANTIL\033[m"
elif idade <= 19:
    categoria = "\033[32mJUNIOR\033[m"
elif idade <= 25:
    categoria = "\033[32mSÊNIOR\033[m"
else:
    categoria = "\033[32mMASTER\033[m"

print(f"O atleta tem {idade} ano(s) em 2023\nClassificação: {categoria}")
