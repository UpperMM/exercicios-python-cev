# Exercício Python 036: Escreva um programa para aprovar o empréstimo
# bancário para a compra de uma casa. Pergunte o valor da casa, o salário
# do comprador e em quantos anos ele vai pagar. A prestação mensal não
# pode exceder 30% do salário ou então o empréstimo será negado.

valor = float(input("Empréstimo para comprar casa.\n\nDigite o valor da casa: R$ "))
salario = float(input("Digite seu salário: "))
anos = float(input("Digite em quantos anos deseja pagar: "))

if valor / (anos * 12) <= salario * 30 / 100:
    resultado = "\033[32mconcedido\033[m"
else:
    resultado = "\033[31mnegado\033[m"

print(
    f"Para pagar uma casa de R$ {valor:.2f} em {anos} anos a prestação mensal será de R$ {valor / (anos * 12):.2f}. Empréstimo foi {resultado}!"
)
