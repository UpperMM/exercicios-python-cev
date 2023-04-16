valor = int(input("Digite um número: "))

print(
    f"Analisando o valor {valor}, seu antecessor é \033[31m{valor - 1}\033[m e seu sucessor \033[32m{valor + 1}\033[m."
)
