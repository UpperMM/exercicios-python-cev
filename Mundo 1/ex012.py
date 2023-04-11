prec = float(input("Qual é o preço do produto? R$ "))

prec_desc = prec - (prec * 5 / 100)

print(f"O valor R${prec} com um desconto de 5% será R${prec_desc}.")
