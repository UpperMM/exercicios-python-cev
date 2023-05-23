# Exercício Python 034: Escreva um programa que pergunte o salário de um
# funcionário e calcule o valor do seu aumento. Para salários superiores a
# R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o
# aumento é de 15%.

salario = float(input("Digite o salário do funcionário: R$"))

if salario <= 1250:
    salario_reajustado = salario + (salario * 15 / 100)
    porcentagem = 15
else:
    salario_reajustado = salario + (salario * 10 / 100)
    porcentagem = 15 - 5

print(
    f"R${salario} receberá um reajuste de \033[1;32m{porcentagem}%\033[m, e passará a ser \033[1;32mR${salario_reajustado}\033[m"
)
