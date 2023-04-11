nome = str(input("Digite um nome: ")).split()

print(f"Primeiro nome: \033[32m{nome[0]}\033[m\nÚltimo nome: \033[31m{nome[-1]}\033[m")
