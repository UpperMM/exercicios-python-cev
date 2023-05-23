# Exercício Python 061: Refaça o DESAFIO 051, lendo o primeiro termo e a
# razão de uma PA, mostrando os 10 primeiros termos da progressão usando a
# estrutura while.

termo = int(input("10 TERMOS DE UMA PA\nPrimeiro termo: "))
razao = int(input("Razão: "))

contador = 0

while contador != 10:
    print(termo, end=" → ")
    termo += razao
    contador += 1

print("acabou!")
