termo = int(input("Os 10 primeiros termos de uma PA\nPrimeiro termo: "))
razao = int(input("Razão: "))

contador = marcador_vezes = 0
vezes = 10

while vezes != 0:
    if contador != 0:
        termo += razao
    print(termo, end=" → ")
    contador += 1
    marcador_vezes += 1

    if marcador_vezes == vezes:
        vezes = int(input("PAUSA\nQuantos termos você quer mostrar a mais? "))
        marcador_vezes = 0

print(f"PA finalizada com {contador} termos exibidos.")
