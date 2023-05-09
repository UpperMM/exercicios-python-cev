termo = int(input("10 TERMOS DE UMA PA\nPrimeiro termo: "))
razao = int(input("Razão: "))

contador = 0

while contador != 10:
    print(termo, end=" → ")
    termo += razao
    contador += 1

print("acabou!")
