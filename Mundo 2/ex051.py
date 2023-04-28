termo = int(input("10 TERMOS DE UMA PA\nPrimeiro termo: "))
razao = int(input("Razão: "))

for pa in range(termo, termo + razao * 10, razao):
    print(f"{pa} ", end="→ ")

print("Acabou!")
