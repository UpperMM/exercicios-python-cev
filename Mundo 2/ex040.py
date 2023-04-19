nota1 = float(input("1º nota: "))
nota2 = float(input("2º nota: "))
media = (nota1 + nota2) / 2

if 7 <= media:
    resultado = "\033[32mAPROVADO\033[m"
elif 5 <= media < 7:
    resultado = "em \033[31mRECUPERAÇÃO\033[m"
else:
    resultado = "\033[31mREPROVADO\033[m"

print(
    f"Tirando {nota1} e {nota2}, a média do aluno é {media:.1f}\nO aluno está {resultado}!"
)
