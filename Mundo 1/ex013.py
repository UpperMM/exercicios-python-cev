salario = float(input("Qual é o salário do funcionário? R$ "))

salario_reajustado = salario + (salario * 15 / 100)

print(
    f"O salário do funcionário, com um reajuste de 15%, irá de \033[31mR$ {salario}\033[m para \033[32mR$ {salario_reajustado}\033[m."
)
