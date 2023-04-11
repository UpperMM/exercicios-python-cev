dias_alugados = float(input("Por quantos dias o carro foi alugado? "))
km = float(input("Por quantos km ele rodou? "))

pagamento = 60 * dias_alugados + 0.15 * km

print(f"O valor total a pagar será de R${pagamento}")
