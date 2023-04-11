numero = int(input("Digite um número com até 4 casas decimais: "))
numerostr = str(numero + 10000).strip()[:5]

print(
    f"O número digitado foi {numero}!\nUnidade: {numerostr[4]}\nDezena: {numerostr[3]}\nCentena: {numerostr[2]}\nMilhar: {numerostr[1]}"
)
