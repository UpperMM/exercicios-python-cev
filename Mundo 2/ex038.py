num1 = int(input("Comparador de números\n\nDigite o 1º número: "))
num2 = int(input("Digite o 2º número: "))

if num1 > num2:
    print(f"\033[32m{num1}\033[m é maior que \033[31m{num2}\033[m!")
elif num1 < num2:
    print(f"\033[32m{num2}\033[m é maior que \033[31m{num1}\033[m!")
else:
    print("Ambos são \033[32miguais!\033[m")
