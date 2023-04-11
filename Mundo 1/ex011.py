larg = float(input("Largura da parede: "))
alt = float(input("Altura da parede: "))

area = larg * alt
tinta = 2

print(
    f"Sua parede tem a dimensão de {larg}x{alt} e sua área é de {area}m².\nPara pintar essa parede, você precisará de \033[32m{area/tinta}l\033[m de tinta."
)
