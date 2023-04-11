cidade = str(input("Digite o nome de uma cidade: ")).strip()

print(f"'{cidade}' começa com 'Santo'? {cidade.lower().split()[0] == 'santo'}")
