numero = int(input("Digite um número: "))

if numero % 2 == 0:
    print(f"{numero} é um número \033[32mpar!\033[m")
else:
    print(f"{numero} é um número \033[31mímpar!\033[m")
