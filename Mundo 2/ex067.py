# Exercício Python 067: Faça um programa que mostre a tabuada de vários
# números, um de cada vez, para cada valor digitado pelo usuário. O
# programa será interrompido quando o número solicitado for negativo.

while True:
    numero = int(input("Digite um número para ver sua tabuada: "))
    if numero < 0:
        break
    print(13 * "=-=")
    for vezes in range(1, 11):
        print(f"{numero} X {vezes:2} = {numero*vezes}")
    print(13 * "=-=")

print("Programa encerrado.")
