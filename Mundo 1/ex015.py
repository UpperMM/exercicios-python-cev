# Exercício Python 015: Escreva um programa que pergunte a quantidade de
# Km percorridos por um carro alugado e a quantidade de dias pelos quais
# ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60
# por dia e R$0,15 por Km rodado.

dias_alugados = float(input("Por quantos dias o carro foi alugado? "))
km = float(input("Por quantos km ele rodou? "))

pagamento = 60 * dias_alugados + 0.15 * km

print(f"O valor total a pagar será de \033[32mR$ {pagamento}\033[m.")
