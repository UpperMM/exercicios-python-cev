prec = float(input("Qual é o preço do produto? R$ "))

prec_desc = prec - (prec * 5 / 100)

print(
    f"O valor R$ \033[31m{prec}\033[m, com um desconto de 5%, será \033[32mR$ {prec_desc}\033[m."
)
