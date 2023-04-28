num = int(input("Digite o número que você deseja ver a tabuada: "))
for multiplicacao in range(1, 11):
    print(f"\033[32m{num} x {multiplicacao:2} = {num*multiplicacao}")
