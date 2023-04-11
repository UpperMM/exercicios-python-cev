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
