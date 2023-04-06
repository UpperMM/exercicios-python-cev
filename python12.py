salario = float(input("Qual é o salário do funcionário? R$"))

salario_reajustado = salario + (salario * 15 / 100)

print(
    f"O salário do funcionário, com um reajuste de 15%, irá de R${salario} para R${salario_reajustado}   "
)
