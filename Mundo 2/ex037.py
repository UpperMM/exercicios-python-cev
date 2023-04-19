numero = int(input("Digite um número inteiro: "))

print(
    "Escolha uma das bases de conversão:\n[ 1 ] Binário\n[ 2 ] Octal\n[ 3 ] Hexadecimal"
)

opcao = int(input("Sua opção: "))

if opcao == 1:
    print(
        f"{numero} convertido para binário é igual a \033[32m{bin(numero)[2:]}\033[m."
    )
elif opcao == 2:
    print(f"{numero} convertido para octal é igual a \033[32m{oct(numero)[2:]}\033[m.")
elif opcao == 3:
    print(
        f"{numero} convertido para hexadecimal é igual a \033[32m{hex(numero)[2:]}\033[m."
    )
else:
    print("Opção inexistente.")
