salario = float(input("Digite o salário do funcionário: R$"))

if salario <= 1250:
    salario_reajustado= salario + (salario * 15 / 100)   
else:
    salario_reajustado = salario + (salario * 10 / 100)
    print(
        f"R${salario} receberá um reajuste de 10%, e passará a ser R${salario_reajustado}"
    )
