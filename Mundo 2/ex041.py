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
